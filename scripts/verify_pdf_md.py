"""Audit Markdown against source files, including an optional offline render check."""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import re
from functools import lru_cache

from convert_pdf_to_md import DOCS, ROOT, discover, fingerprint, native, records_from, rule_version
from pdfmd_document import ASSET
from pdfmd_media import atomic_write
import pymupdf


ANCHOR = re.compile(r'<a id="(section-[^"]+)"></a>')
LOCAL_LINK = re.compile(r'\]\(#(section-[^)]+)\)')
FENCE = re.compile(r"^[\s>]*(`{3,})([a-z][\w-]*)?\s*$")


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
    urls = set(re.findall(r'<img\s+[^>]*?src="(assets/[^"]+)"', html))
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
    try:
        if not record or record["status"] == "failed":
            raise ValueError("Missing successful conversion record")
        if record["rules"] != version or fingerprint(source) != record["sha256"]:
            issues.append("Source or converter fingerprint changed")
        target = root / record["output"]
        data = target.read_bytes()
        if hashlib.sha256(data).hexdigest() != record["md_sha256"]:
            issues.append("Markdown fingerprint mismatch")
        md = data.decode("utf-8")
        with pymupdf.open(str(source)) as pdf:
            if len(pdf) != record["pages"] or record["body_pages"] != len(pdf)-record["first_body"]+1:
                issues.append("Source page accounting differs")
        anchors = ANCHOR.findall(md)
        if (len(set(anchors)) != len(anchors) or len(anchors) != record["headings"]
                or Counter(LOCAL_LINK.findall(md)) != Counter(anchors)):
            issues.append("Contents links or body anchors differ")
        sources = set(ASSET.findall(md))
        if len(sources) != record["images"]:
            issues.append("Referenced image count differs")
        for link in sources:
            path = target.parent / link
            stat = path.stat()
            if not asset_ok(path, stat.st_size, stat.st_mtime_ns):
                issues.append(f"Incorrect image bytes {link}")
        code_count = fences(md)
        if render:
            issues.extend(rendered_check(md, anchors, sources, record["tables"], code_count))
        return key, issues, code_count
    except Exception as exc:
        return key, [*issues, str(exc)], 0


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
    pool = ProcessPoolExecutor(args.jobs) if args.jobs > 1 else None
    try:
        results = pool.map(check, tasks, chunksize=1) if pool else map(check, tasks)
        for key, errors, blocks in results:
            counts["code_blocks"] += blocks
            if errors:
                issues[key] = errors
            r = records.get(key, {})
            for field in ("pages","body_pages","headings","tables","table_joins","images"):
                counts[field] += r.get(field, 0)
    finally:
        if pool:
            pool.shutdown()
    counts["failed_checks_documents"] = len(issues)
    result = dict(rules=version, rendered=args.render, summary=counts, errors=issues)
    if args.report:
        atomic_write(native(args.report), (json.dumps(result,ensure_ascii=False,indent=2)+"\n").encode())
    print(json.dumps(result, ensure_ascii=True))
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
