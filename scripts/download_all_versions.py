#!/usr/bin/env python3
"""全量下载两个平台所有版本文档。

中文：outputs/zh_all_versions_plan.csv  -> downloads/zh_all_versions/<ver>/<code>.zip
英文：outputs/en_all_versions_plan.csv  -> downloads/en_all_versions/<ver>/<filename>

使用 curl 重试 + Windows 长路径前缀；默认 dry-run，--apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import os
import pathlib
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = pathlib.Path(__file__).resolve().parents[1]
ZH_PLAN = ROOT / "outputs/zh_all_versions_plan.csv"
EN_PLAN = ROOT / "outputs/en_all_versions_plan.csv"
ZH_OUT = ROOT / "downloads/zh_all_versions"
EN_OUT = ROOT / "downloads/en_all_versions"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
RETRIES = 8


def long_path(p: pathlib.Path) -> str:
    return "\\\\?\\" + str(p.resolve())


def curl_get(url: str, dest: pathlib.Path, expect: bytes) -> tuple[bool, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dl = pathlib.Path(long_path(dest))
    if dl.exists() and dl.stat().st_size > 1024:
        return True, f"skip {dl.stat().st_size}"
    part = dest.with_suffix(dest.suffix + ".part")
    pl = pathlib.Path(long_path(part))
    cmd = [
        "curl", "-sS", "-L", "--retry", str(RETRIES), "--retry-all-errors",
        "--connect-timeout", "20", "--max-time", "900",
        "-A", UA, "-o", str(pl), url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=1000)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if r.returncode != 0:
        return False, (r.stderr.strip().splitlines() or ["curl error"])[-1][:200]
    if not pl.exists() or pl.stat().st_size < 1024:
        return False, "too small"
    with pl.open("rb") as f:
        if f.read(len(expect)) != expect:
            return False, f"bad header {f.read(8)!r}"
    os.replace(str(pl), str(dl))
    return True, str(dl.stat().st_size)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--platform", choices=("all", "zh", "en"), default="all")
    args = ap.parse_args()

    jobs = []
    if args.platform in ("all", "zh"):
        with ZH_PLAN.open(encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                jobs.append(("zh", r, ZH_OUT / r["version"] / (r["code"] + ".zip")))
    if args.platform in ("all", "en"):
        with EN_PLAN.open(encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                ver = r["version"] or "unknown"
                jobs.append(("en", r, EN_OUT / ver / r["filename"]))

    print(f"总任务 {len(jobs)}（中文 {sum(1 for j in jobs if j[0]=='zh')}、英文 {sum(1 for j in jobs if j[0]=='en')}）", flush=True)
    if not args.apply:
        print("[DRY-RUN] 未下载")
        for kind, r, p in jobs[:5]:
            print(" ", kind, p.relative_to(ROOT))
        return 0

    results: dict[str, list] = {"zh": [], "en": []}
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {}
        for kind, r, p in jobs:
            expect = b"PK" if kind == "zh" else b"%PDF-"
            futs[ex.submit(curl_get, r["url"], p, expect)] = (kind, r, p)
        done = 0
        for fut in as_completed(futs):
            kind, r, p = futs[fut]
            try:
                ok, note = fut.result()
            except Exception as e:
                ok, note = False, repr(e)[:200]
            done += 1
            results[kind].append((r, ok, note))
            if done % 100 == 0 or not ok:
                print(f"[{done}/{len(jobs)}] {'OK' if ok else 'FAIL'} {kind} {p.name[:70]} {note}", flush=True)

    if results["zh"]:
        with (ZH_OUT / "download_manifest.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["version", "code", "name", "category", "url", "ok", "note"])
            for r, ok, note in sorted(results["zh"], key=lambda x: (x[0]["version"], x[0]["code"])):
                w.writerow([r["version"], r["code"], r["name"], r["category"], r["url"], ok, note])
    if results["en"]:
        with (EN_OUT / "download_manifest.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["version", "product", "name", "filename", "url", "ok", "note"])
            for r, ok, note in sorted(results["en"], key=lambda x: (x[0]["version"], x[0]["filename"])):
                w.writerow([r["version"], r["product"], r["name"], r["filename"], r["url"], ok, note])

    for kind in ("zh", "en"):
        okc = sum(1 for _, ok, _ in results[kind] if ok)
        print(f"{kind.upper()} done {okc}/{len(results[kind])}", flush=True)
    return 0 if all(ok for rs in results.values() for _, ok, _ in rs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
