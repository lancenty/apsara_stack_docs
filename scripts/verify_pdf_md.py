"""Audit Markdown against source files, including an optional offline render check."""

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import re
from functools import lru_cache

from convert_pdf_to_md import (
    _LEGACY_ASSET_REF,
    DOCS,
    ROOT,
    discover,
    fingerprint,
    native,
    records_from,
    rule_version,
)
from doc_identity import (
    ASSETS_DIR_RE,
    extract_cover_from_markdown,
    load_overrides,
    load_registry,
    load_rules,
    resolve_identity,
    validate_document_id_fields,
)
from pdfmd_document import ASSET
from pdfmd_media import atomic_write
import pymupdf


ANCHOR = re.compile(r'<a id="(section-[^"]+)"></a>')
LOCAL_LINK = re.compile(r'\]\(#(section-[^)]+)\)')
FENCE = re.compile(r"^[\s>]*(`{3,})([a-z][\w-]*)?\s*$")


@lru_cache(maxsize=1)
def _identity_configs():
    return load_rules(), load_overrides(), load_registry()


def _display_len(path):
    text = str(path)
    if text.startswith("\\\\?\\UNC\\"):
        return len("\\\\" + text[8:])
    if text.startswith("\\\\?\\"):
        return len(text[4:])
    return len(text)


@lru_cache(maxsize=20000)
def asset_ok(path, size, mtime):
    return size > 0 and fingerprint(path).startswith(path.stem)


def fences(md):
    active = count = 0
    for line in md.splitlines():
        if "```" not in line:
            continue
        match = FENCE.fullmatch(line)
        if not match:
            continue
        size, language = len(match[1]), match[2]
        if not active and language:
            count += 1
            active = size
        elif active and not language and size >= active:
            active = 0
    if active:
        raise ValueError("Unclosed code fence")
    return count


@lru_cache(maxsize=1)
def renderer():
    from markdown_it import MarkdownIt
    return MarkdownIt("commonmark", {"html": True}).enable("table")


def rendered_check(md, anchors, sources, table_count, code_count):
    html = renderer().render(md)
    urls = set(re.findall(r'<img\s+[^>]*?src="((?:assets|[a-z0-9][a-z0-9._-]*\.assets)/[^"]+)"', html))
    ids = ANCHOR.findall(html)
    links = re.findall(r'<a href="#(section-[^"]+)"', html)
    failures = []
    if Counter(ids) != Counter(anchors) or Counter(links) != Counter(anchors):
        failures.append("rendered contents links/anchors differ")
    if len(re.findall(r"<h[1-6](?:\s|>)", html)) < len(anchors):
        failures.append("missing rendered headings")
    if urls != sources:
        failures.append(f"rendered image differences {sorted(sources.symmetric_difference(urls))[:5]}")
    checks = (("table", html.count("<table>"), table_count),
              ("code", html.count("<pre><code"), code_count))
    for label, actual, expected in checks:
        if actual != expected:
            failures.append(f"rendered {label} count {actual}, expected {expected}")
    return failures


def check(item):
    key, source, root, record, version, render = item
    issues = []
    max_asset_len = 0
    try:
        if not record or record["status"] == "failed":
            raise ValueError("Missing successful conversion record")
        if record["rules"] != version or fingerprint(source) != record["sha256"]:
            issues.append("Source or converter fingerprint changed")
        issues.extend(validate_document_id_fields(record))
        target = root / record["output"]
        data = target.read_bytes()
        if hashlib.sha256(data).hexdigest() != record["md_sha256"]:
            issues.append("Markdown fingerprint mismatch")
        md = data.decode("utf-8")
        rules, overrides, registry = _identity_configs()
        ident = resolve_identity(
            source_key=key,
            cover_lines=extract_cover_from_markdown(md),
            pdf_sha256=record["sha256"],
            rules=rules,
            overrides=overrides,
            registry=registry,
        )
        if ident["id_status"] != "ok":
            issues.append(f"Document ID resolution anomaly: {ident['id_anomalies']}")
        if ident["document_id"] != record.get("document_id"):
            issues.append(
                f"Document ID drift: manifest={record.get('document_id')!r}, resolved={ident['document_id']!r}"
            )
        if ident["assets_dir"] != record.get("assets_dir"):
            issues.append(
                f"Assets dir drift: manifest={record.get('assets_dir')!r}, resolved={ident['assets_dir']!r}"
            )
        assets_dir = record.get("assets_dir", "")
        if not assets_dir or not ASSETS_DIR_RE.fullmatch(assets_dir):
            issues.append(f"Invalid assets_dir: {assets_dir!r}")
        expected_assets_path = (Path(record["output"]).parent / assets_dir).as_posix() if assets_dir else ""
        if record.get("assets_path") != expected_assets_path:
            issues.append(
                f"assets_path mismatch: manifest={record.get('assets_path')!r}, expected={expected_assets_path!r}"
            )
        with pymupdf.open(str(source)) as pdf:
            if len(pdf) != record["pages"] or record["body_pages"] != len(pdf)-record["first_body"]+1:
                issues.append("Source page accounting differs")
        anchors = ANCHOR.findall(md)
        if (len(set(anchors)) != len(anchors) or len(anchors) != record["headings"]
                or Counter(LOCAL_LINK.findall(md)) != Counter(anchors)):
            issues.append("Contents links or body anchors differ")
        if _LEGACY_ASSET_REF.search(md):
            issues.append("Legacy shared assets/ reference found in Markdown")
        sources = set(ASSET.findall(md))
        if len(sources) != record["images"]:
            issues.append("Referenced image count differs")
        if assets_dir:
            bad_prefix = [link for link in sources if not link.startswith(assets_dir + "/")]
            if bad_prefix:
                issues.append(f"Cross-document or invalid asset reference(s): {sorted(bad_prefix)[:3]}")
        expected_names = sorted(Path(link).name for link in sources)
        if expected_names != record.get("assets", []):
            issues.append("Manifest assets list differs from Markdown references")
        for link in sources:
            path = target.parent / link
            max_asset_len = max(max_asset_len, _display_len(path))
            stat = path.stat()
            if not asset_ok(path, stat.st_size, stat.st_mtime_ns):
                issues.append(f"Incorrect image bytes {link}")
        if assets_dir:
            asset_folder = target.parent / assets_dir
            if asset_folder.is_dir():
                expected_set = set(expected_names)
                unexpected = [p.name for p in asset_folder.iterdir() if not p.is_file() or p.name not in expected_set]
                if unexpected:
                    issues.append(f"Orphan files in independent assets directory: {unexpected[:3]}")
                if not expected_set and any(asset_folder.iterdir()):
                    issues.append("Non-empty assets directory for document with 0 images")
        code_count = fences(md)
        if render:
            issues.extend(rendered_check(md, anchors, sources, record["tables"], code_count))
        return key, issues, code_count, max_asset_len
    except Exception as exc:
        return key, [*issues, str(exc)], 0, max_asset_len


def main():
    ap = argparse.ArgumentParser(description="核验本地 PDF、转换清单、MD 及其图片。")
    ap.add_argument("input", type=Path, nargs="*")
    ap.add_argument("--output", type=Path, default=ROOT / "markdown")
    ap.add_argument("--render", action="store_true", help="同时实际渲染 Markdown 并检查生成的结构")
    ap.add_argument("--report", type=Path, help="将结果写入 JSON 文件")
    ap.add_argument("--jobs", type=int, default=1)
    args = ap.parse_args()
    if args.jobs < 1:
        ap.error("--jobs 必须大于零")
    if args.render:
        try:
            renderer()
        except ImportError:
            ap.error("渲染核验需要 markdown-it-py，请先安装 requirements-pdfmd.txt")
    root = native(args.output)
    records = records_from(root / "manifest.json")
    inputs = discover(args.input or [DOCS], None)
    if not inputs:
        ap.error("没有匹配的 PDF")
    issues = {}
    version = rule_version()
    tasks = [(k, f, root, records.get(k), version, args.render) for k,(f,_,_) in inputs.items()]
    counts = Counter(documents=len(tasks), code_blocks=0)
    max_asset_path_len = 0
    pool = ProcessPoolExecutor(args.jobs) if args.jobs > 1 else None
    try:
        results = pool.map(check, tasks, chunksize=1) if pool else map(check, tasks)
        for key, errors, blocks, asset_len in results:
            counts["code_blocks"] += blocks
            max_asset_path_len = max(max_asset_path_len, asset_len)
            if errors:
                issues[key] = errors
            r = records.get(key, {})
            for field in ("pages","body_pages","headings","tables","table_joins","images"):
                counts[field] += r.get(field, 0)
    finally:
        if pool:
            pool.shutdown()

    by_id = defaultdict(list)
    by_assets_path = defaultdict(list)
    id_overrides = 0
    id_anomalies = 0
    for key in inputs:
        r = records.get(key) or {}
        if r.get("document_id"):
            by_id[r["document_id"]].append(key)
        if r.get("assets_path"):
            by_assets_path[r["assets_path"]].append(key)
        if r.get("id_source") == "override":
            id_overrides += 1
        if r.get("id_status") != "ok":
            id_anomalies += 1

    id_conflicts = {k: v for k, v in by_id.items() if len(v) > 1}
    asset_conflicts = {k: v for k, v in by_assets_path.items() if len(v) > 1}
    for doc_id, srcs in sorted(id_conflicts.items()):
        for src in srcs:
            issues.setdefault(src, []).append(f"Duplicate document_id {doc_id}: {srcs}")
    for apath, srcs in sorted(asset_conflicts.items()):
        for src in srcs:
            issues.setdefault(src, []).append(f"Shared assets_path {apath}: {srcs}")

    if args.input:
        shared_dirs = sorted(
            {
                str(parent / "assets")
                for _, (_, rel, _) in inputs.items()
                for parent in [root / rel.parent]
                if (parent / "assets").is_dir()
            }
        )
    else:
        shared_dirs = sorted(str(p) for p in root.rglob("assets") if p.is_dir())
    if shared_dirs:
        issues.setdefault("__shared_assets__", []).extend(
            f"Legacy shared assets directory present: {d}" for d in shared_dirs
        )

    counts["unique_document_ids"] = len(by_id)
    counts["unique_assets_paths"] = len(by_assets_path)
    counts["shared_asset_dirs_found"] = len(shared_dirs)
    counts["id_overrides"] = id_overrides
    counts["id_anomalies"] = id_anomalies
    counts["id_conflicts"] = len(id_conflicts)
    counts["max_asset_path_len"] = max_asset_path_len
    counts["failed_checks_documents"] = len(issues)
    result = dict(rules=version, rendered=args.render, summary=counts, errors=issues)
    if args.report:
        atomic_write(native(args.report), (json.dumps(result,ensure_ascii=False,indent=2)+"\n").encode())
    print(json.dumps(result, ensure_ascii=True))
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
