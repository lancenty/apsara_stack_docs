#!/usr/bin/env python3
"""定向下载英文文档：3.18.6 家族全部 + 老版本独有文档。

目标集合：
- docs/en 中文件名或 PDF 封面含 3.18.6（含 v3.18.6-2607）的全部文档；
- outputs/legacy_only_docs.csv 中「复核后真正老版本独有」的英文文档。
下载源：data/apsara_latest_manifest.csv 的英文 url；若本地文件名曾因过长被缩短，
通过 outputs/long_en_names_fix.csv 映射回原始 OSS 文件名再取 URL。

输出目录：downloads/en/<一级分类>/<二级产品>/<文件名>
默认 dry-run；--apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import os
import pathlib
import re
import subprocess
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed

from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_EN = ROOT / "docs/en"
OUT = ROOT / "downloads/en"
MANIFEST_IN = ROOT / "data/apsara_latest_manifest.csv"
RENAME_MAP = ROOT / "outputs/long_en_names_fix.csv"
LEGACY = ROOT / "outputs/legacy_only_docs.csv"
MANIFEST_OUT = OUT / "download_manifest.csv"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
RETRIES = 8


def long_path(p: pathlib.Path) -> str:
    return "\\\\?\\" + str(p.resolve())


def cover(p: pathlib.Path) -> str:
    try:
        t = PdfReader(long_path(p)).pages[0].extract_text() or ""
        return unicodedata.normalize("NFKC", re.sub(r"\s+", " ", t))
    except Exception:
        return ""


def build_targets() -> list[dict]:
    with MANIFEST_IN.open(encoding="utf-8-sig") as f:
        urls = {r["filename"]: r for r in csv.DictReader(f) if r["language"] == "英文"}
    with RENAME_MAP.open(encoding="utf-8-sig") as f:
        renamed = {r["new_name"]: r["old_name"] for r in csv.DictReader(f)}
    with LEGACY.open(encoding="utf-8-sig") as f:
        legacy = {r["filename"] for r in csv.DictReader(f)
                  if r["language"] == "英文" and r["has_same_product_guide_36"] == "False"}

    tasks = []
    for p in sorted(DOCS_EN.rglob("*.pdf")):
        is36 = bool(re.search(r"3\.18\.6", p.name, re.I) or re.search(r"3\.18\.6", cover(p), re.I))
        is_legacy = p.name in legacy
        if not (is36 or is_legacy):
            continue
        rel = p.relative_to(ROOT)
        src_name = renamed.get(p.name, p.name)
        row = urls.get(src_name)
        if not row:
            raise RuntimeError(f"manifest 中找不到 URL: {p.name} -> {src_name}")
        tasks.append({
            "group": "3.18.6" if is36 else "legacy-only",
            "category": rel.parts[2],
            "product": rel.parts[3],
            "filename": p.name,
            "url": row["url"],
            "expected_size": row.get("size_bytes") or "",
        })
    return tasks


def fetch(t: dict) -> tuple[dict, bool, str]:
    dest = OUT / t["category"] / t["product"] / t["filename"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    # downloads/en 比 docs/en 路径更长，部分原始文件名会超 MAX_PATH，全程用长路径前缀
    dest_lp = pathlib.Path(long_path(dest))
    if dest_lp.exists() and dest_lp.stat().st_size > 1024:
        return t, True, f"skip {dest_lp.stat().st_size}"
    part = dest.with_suffix(dest.suffix + ".part")
    part_lp = pathlib.Path(long_path(part))
    cmd = [
        "curl", "-sS", "-L", "--retry", str(RETRIES), "--retry-all-errors",
        "--connect-timeout", "20", "--max-time", "600",
        "-A", UA, "-o", str(part_lp), t["url"],
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=700)
    except subprocess.TimeoutExpired:
        return t, False, "timeout"
    if r.returncode != 0:
        return t, False, (r.stderr.strip().splitlines() or ["curl error"])[-1][:200]
    if not part_lp.exists() or part_lp.stat().st_size < 1024:
        return t, False, "too small"
    with part_lp.open("rb") as f:
        if f.read(5) != b"%PDF-":
            return t, False, "not PDF"
    os.replace(str(part_lp), str(dest_lp))
    return t, True, str(dest_lp.stat().st_size)


def shorten_overlong() -> int:
    """downloads/en 比 docs/en 路径更深，把普通路径打不开的文件按既有规则缩短。"""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "sle", ROOT / "scripts/shorten_long_en_names.py"
    )
    sle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sle)

    with MANIFEST_OUT.open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    changed = 0
    for r in rows:
        p = OUT / r["category"] / r["product"] / r["filename"]
        try:
            with p.open("rb") as fp:
                fp.read(5)
            continue
        except OSError:
            pass
        ver, date = sle.cover(p)
        gtype = next((g for g in sle.GUIDES if g in p.stem), "Guide")
        prod = sle.fit_product(sle.short_product(p.parent.name, p.stem), ver, gtype, date)
        if prod.startswith("for Kubernetes"):
            prod = "ACK One Distributed Cloud"
        new = f"{ver} {prod} {gtype} {date}.pdf"
        dest = p.parent / new
        if dest.exists() and dest != p:
            raise RuntimeError(f"缩短后文件名冲突: {dest}")
        os.rename(sle.long_path(p), sle.long_path(dest))
        r["filename"] = new
        changed += 1
    if changed:
        with MANIFEST_OUT.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    return changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--jobs", type=int, default=5)
    args = ap.parse_args()

    tasks = build_targets()
    print(f"目标文档 {len(tasks)} 份（3.18.6 {sum(1 for t in tasks if t['group']=='3.18.6')}、老版本独有 {sum(1 for t in tasks if t['group']=='legacy-only')}）")
    if not args.apply:
        print("[DRY-RUN] 未下载。示例：")
        for t in tasks[:5]:
            print("  ", t["group"], t["category"], t["product"], t["filename"])
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(fetch, t): t for t in tasks}
        done = 0
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                _, ok, note = fut.result()
            except Exception as e:
                ok, note = False, repr(e)[:200]
            done += 1
            results.append((t, ok, note))
            if done % 25 == 0 or not ok:
                print(f"[{done}/{len(tasks)}] {'OK' if ok else 'FAIL'} {t['filename'][:70]} {note}", flush=True)

    with MANIFEST_OUT.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["group", "category", "product", "filename", "url", "expected_size", "ok", "note"])
        for t, ok, note in sorted(results, key=lambda x: (x[0]["group"], x[0]["category"], x[0]["product"], x[0]["filename"])):
            w.writerow([t["group"], t["category"], t["product"], t["filename"], t["url"], t["expected_size"], ok, note])

    ok_count = sum(1 for _, ok, _ in results if ok)
    shortened = shorten_overlong()
    print(f"[APPLIED] 成功 {ok_count}/{len(tasks)}，缩短超长文件名 {shortened} 份，清单 {MANIFEST_OUT}")
    return 0 if ok_count == len(tasks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
