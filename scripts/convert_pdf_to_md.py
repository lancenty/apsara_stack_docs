"""Offline bilingual Apsara Stack PDF archive converter."""

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
if (ROOT / ".conversion-env" / "pymupdf").is_dir():
    sys.path.insert(0, str(ROOT / ".conversion-env"))
try:
    import pymupdf
except ImportError:
    raise SystemExit("请先运行 python -m pip install -r requirements-pdfmd.txt")
from doc_identity import (
    ASSETS_DIR_RE,
    load_registry,
    save_registry,
    validate_document_id_fields,
)
from pdfmd_media import atomic_write

_LEGACY_ASSET_REF = re.compile(r'(?:!\[[^\]\n]*\]\(|<img\b[^>]*?\bsrc=["\'])assets/')


def native(path):
    absolute = str(Path(path).resolve())
    if os.name == "nt" and not absolute.startswith("\\\\?\\"):
        absolute = "\\\\?\\UNC\\" + absolute[2:] if absolute.startswith("\\\\") else "\\\\?\\" + absolute
    return Path(absolute)


def fingerprint(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def rule_version():
    h = hashlib.sha256(pymupdf.VersionBind.encode())
    h.update(os.environ.get("PDFMD_WEBP_QUALITY", "").strip().encode("utf-8"))
    for module in sorted(Path(__file__).parent.glob("pdfmd_*.py")):
        h.update(module.read_bytes())
    return h.hexdigest()[:16]


@contextmanager
def run_lock(root):
    """The OS releases this advisory lock even if a batch process is killed."""
    root.mkdir(parents=True, exist_ok=True)
    with (root / ".conversion.lock").open("a+b") as lock:
        if lock.tell() == 0:
            lock.write(b"0")
            lock.flush()
        lock.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise SystemExit(f"另一个转换任务正在写入 {root}") from exc
        yield


def records_from(path):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["source"]: r for r in data["documents"]}


def save_manifest(path, records):
    documents = [records[k] for k in sorted(records)]
    summary = {s: sum(r["status"] == s for r in documents) for s in ("ok","review","failed")}
    doc_ids = [r.get("document_id") for r in documents if r.get("document_id")]
    id_counts = Counter(doc_ids)
    summary.update(
        documents=len(documents),
        pages=sum(r.get("pages", 0) for r in documents),
        images=sum(r.get("images", 0) for r in documents),
        unique_document_ids=len(id_counts),
        id_ok=sum(r.get("id_status") == "ok" for r in documents),
        id_overrides=sum(r.get("id_source") == "override" for r in documents),
        id_anomalies=sum(r.get("id_status") != "ok" for r in documents),
        id_conflicts=sum(1 for cnt in id_counts.values() if cnt > 1),
        package_versions=len({r.get("package_version") for r in documents if r.get("package_version")}),
        product_codes=len({r.get("product_code") for r in documents if r.get("product_code")}),
    )
    data = dict(format=3, summary=summary, documents=documents)
    atomic_write(path, (json.dumps(data, ensure_ascii=False, indent=2)+"\n").encode("utf-8"))


def discover(inputs, requested):
    found = {}
    for src in inputs:
        src = native(src)
        base = src if src.is_dir() else src.parent
        files = [src] if src.is_file() else native(src).rglob("*.pdf")
        if not src.exists():
            raise ValueError(f"输入路径不存在 {src}")
        for p in files:
            if p.suffix.lower() != ".pdf":
                raise ValueError(f"请输入 PDF 文件或目录 {p}")
            f = native(p)
            if f.is_relative_to(native(DOCS)):
                rel = f.relative_to(native(DOCS))
            else:
                rel = f.relative_to(native(base))
            lang = next(("cn" if s == "zh" else s for s in rel.parts if s in {"cn","zh","en"}), "")
            if requested and not lang:
                with pymupdf.open(str(f)) as doc:
                    lang = "cn" if re.search(r"[\u3400-\u9fff]", doc[0].get_text()) else "en"
            if requested and requested != lang:
                continue
            key = rel.as_posix()
            if key in found and found[key][0] != f:
                raise ValueError(f"两个输入映射到同一个文件 {key}")
            found[key] = (f, rel.with_suffix(".md"), lang)
    return found


def valid_cached(record, path, source_hash, version):
    from pdfmd_document import ASSET
    if (not record or record["status"] not in ("ok","review")
            or record.get("sha256") != source_hash or record.get("rules") != version
            or not path.is_file() or path.stat().st_size != record.get("bytes")):
        return False
    assets_dir = record.get("assets_dir", "")
    if not assets_dir or not ASSETS_DIR_RE.fullmatch(assets_dir):
        return False
    if record.get("assets_path") != (Path(record["output"]).parent / assets_dir).as_posix():
        return False
    if validate_document_id_fields(record):
        return False
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != record.get("md_sha256"):
        return False
    text = data.decode("utf-8")
    if _LEGACY_ASSET_REF.search(text):
        return False
    refs = set(ASSET.findall(text))
    if any(not ref.startswith(assets_dir + "/") for ref in refs):
        return False
    if sorted(Path(ref).name for ref in refs) != record.get("assets"):
        return False
    return all((path.parent / ref).is_file() and (path.parent / ref).stat().st_size for ref in refs)


def run_one(key, item, root, previous, version, force):
    source, rel, lang = item
    target = root / rel
    rec = dict(source=key, output=rel.as_posix(), rules=version)
    try:
        rec["sha256"] = fingerprint(source)
        if not force and valid_cached(previous, target, rec["sha256"], version):
            return previous, True
        # Process isolation bounds memory on long manuals and contains native PDF parsing failures.
        cp = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker",
                             str(source), str(target), lang, key, rec["sha256"]],
                            capture_output=True, env={**os.environ, "PYTHONUTF8":"1"})
        if cp.returncode:
            errors = (cp.stderr or cp.stdout).decode("utf-8", errors="replace")
            raise RuntimeError(errors.strip()[-1600:] or f"Worker process exit {cp.returncode}")
        msg = cp.stdout.decode("utf-8").splitlines()
        result = next(line[12:] for line in reversed(msg) if line.startswith("PDFMDRESULT "))
        rec.update(json.loads(result))
        rec["assets_path"] = (rel.parent / rec["assets_dir"]).as_posix()
        rec.update(status="review" if rec["issues"] else "ok", md_sha256=fingerprint(target))
    except Exception as error:
        rec.update(status="failed", issues=[{"page":None, "reason":str(error)}])
    return rec, False


def _find_conflicts(records):
    by_id = defaultdict(list)
    by_assets = defaultdict(list)
    for rec in records.values():
        if rec.get("document_id"):
            by_id[rec["document_id"]].append(rec["source"])
        if rec.get("assets_path"):
            by_assets[rec["assets_path"]].append(rec["source"])
    id_conflicts = {k: v for k, v in by_id.items() if len(v) > 1}
    asset_conflicts = {k: v for k, v in by_assets.items() if len(v) > 1}
    return id_conflicts, asset_conflicts


def main():
    if sys.argv[1:2] == ["--worker"]:
        from pdfmd_document import convert
        result = convert(*sys.argv[2:7])
        print("PDFMDRESULT " + json.dumps(result, ensure_ascii=True))
        return 0
    ap = argparse.ArgumentParser(description="将阿里云专有云 PDF 转换为可离线阅读的 Markdown。")
    ap.add_argument("input", type=Path, nargs="*", help="PDF 或目录；默认为 docs/")
    ap.add_argument("--output", type=Path, default=ROOT / "markdown")
    ap.add_argument("--language", choices=("cn","zh","en"))
    ap.add_argument("--jobs", type=int, default=min(6, os.cpu_count() or 1))
    ap.add_argument("--force", action="store_true", help="强制重建选中的文件")
    args = ap.parse_args()
    if args.jobs < 1:
        ap.error("--jobs 必须大于零")
    selection = discover(args.input or [DOCS], "cn" if args.language=="zh" else args.language)
    if not selection:
        ap.error("没有匹配的 PDF 文件")
    root = native(args.output)
    with run_lock(root):
        manifest = root / "manifest.json"
        records = records_from(manifest)
        version = rule_version()
        ordered = sorted(selection, key=lambda k:selection[k][0].stat().st_size, reverse=True)
        total, failed, skipped, reviews = len(ordered), 0, 0, 0
        print(f"Converting {total} PDF(s), {args.jobs} worker(s), rules {version}", flush=True)
        started = time.monotonic()
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            pending = [pool.submit(run_one, k, selection[k], root, records.get(k), version, args.force) for k in ordered]
            for i, job in enumerate(as_completed(pending), 1):
                rec, cached = job.result()
                skipped += cached
                failed += rec["status"] == "failed"
                reviews += rec["status"] == "review"
                records[rec["source"]] = rec
                if not cached:
                    save_manifest(manifest, records)
                if not cached or i == total:
                    print(f'[{i}/{total}] {"cached" if cached else rec["status"]} {rec["source"]}', flush=True)
                if rec["status"] == "failed":
                    print(rec["issues"][0]["reason"], file=sys.stderr, flush=True)
        id_conflicts, asset_conflicts = _find_conflicts(records)
        if id_conflicts or asset_conflicts:
            for doc_id, srcs in sorted(id_conflicts.items()):
                print(f"Document ID conflict {doc_id}: {srcs}", file=sys.stderr, flush=True)
            for apath, srcs in sorted(asset_conflicts.items()):
                print(f"Assets path conflict {apath}: {srcs}", file=sys.stderr, flush=True)
            failed += len(id_conflicts) + len(asset_conflicts)
        if not id_conflicts and not asset_conflicts:
            existing_reg = load_registry().get("documents", {})
            updated_reg = dict(existing_reg)
            for rec in records.values():
                if rec.get("status") in ("ok", "review") and rec.get("id_status") == "ok" and rec.get("sha256"):
                    updated_reg[rec["sha256"]] = {
                        "document_id": rec["document_id"],
                        "source": rec["source"],
                        "assets_dir": rec["assets_dir"],
                        "language": rec["language"],
                        "package_version": rec["package_version"],
                        "platform_version": rec["platform_version"],
                        "category": rec.get("category", ""),
                        "product_code": rec["product_code"],
                        "product": rec["product"],
                        "document_key": rec["document_key"],
                        "base_document_key": rec.get("base_document_key", ""),
                        "document_version": rec["document_version"],
                        "id_source": rec.get("id_source", "rules"),
                    }
            if updated_reg != existing_reg:
                save_registry(updated_reg)
        print(f"Finished in {time.monotonic()-started:.1f}s; skipped={skipped} review={reviews} failed={failed}", flush=True)
        return int(bool(failed))


if __name__ == "__main__":
    raise SystemExit(main())
