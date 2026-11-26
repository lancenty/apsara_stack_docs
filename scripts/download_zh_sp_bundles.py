#!/usr/bin/env python3
"""批量下载中文专有云企业版整包 ZIP（0430 / 0730 / 1030）。

数据源：帮助中心 /apsara/api/products?type=enterprise&version=<ver> 返回的 downloadUrl。
特性：并发下载、断点续传、失败重试、进度日志、可仅下载指定版本。
用法：
    python scripts/download_zh_sp_bundles.py
    python scripts/download_zh_sp_bundles.py --versions v_3_18_6_20260730
    python scripts/download_zh_sp_bundles.py --jobs 6
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "downloads" / "zh_bundles"
MANIFEST = OUT_DIR / "download_manifest.csv"
LOG = OUT_DIR / "download.log"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
VERSIONS = ["v_3_18_6_20250430", "v_3_18_6_20260730", "v_3_18_6_20261030"]
RETRIES = 8


def log(msg: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def curl_download(url: str, dest: pathlib.Path) -> tuple[bool, str]:
    """用 curl 下载，带重试；返回 (ok, note)。curl 对该 OSS 比 urllib 稳定。"""
    part = dest.with_suffix(dest.suffix + ".part")
    cmd = [
        "curl", "-sS", "-L", "--retry", str(RETRIES), "--retry-all-errors",
        "--connect-timeout", "20", "--max-time", "600",
        "-A", UA, "-o", str(part), url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=700)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if r.returncode != 0:
        return False, (r.stderr.strip().splitlines() or ["curl error"])[-1][:200]
    if not part.exists() or part.stat().st_size < 1024:
        return False, "too small"
    part.replace(dest)
    return True, str(dest.stat().st_size)


def fetch_one(item: dict, ver: str) -> tuple[str, str, bool, str]:
    code = item["code"]
    name = item["name"]
    category = item["category"]
    url = "https:" + item["downloadUrl"]
    dest = OUT_DIR / ver / f"{code}.zip"
    if dest.exists() and dest.stat().st_size > 1024:
        return ver, code, True, f"skip {dest.stat().st_size}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    ok, note = curl_download(url, dest)
    return ver, code, ok, note


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--versions", nargs="*", default=VERSIONS)
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG.touch(exist_ok=True)

    tasks: list[tuple[dict, str]] = []
    for ver in args.versions:
        src = ROOT / "outputs" / f"products_{ver}.json"
        if not src.exists():
            log(f"MISSING manifest {src}")
            continue
        data = json.loads(src.read_text(encoding="utf-8"))["data"]
        tasks.extend((x, ver) for x in data)
    log(f"total {len(tasks)} bundles, jobs={args.jobs}")

    results: list[tuple[str, str, str, str, str, str, bool, str]] = []
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(fetch_one, item, ver): (item, ver) for item, ver in tasks}
        done = 0
        for fut in as_completed(futs):
            item, ver = futs[fut]
            try:
                _, code, ok, note = fut.result()
            except Exception as e:
                code, ok, note = item["code"], False, repr(e)[:200]
            done += 1
            results.append((ver, item["category"], item["name"], code, "https:" + item["downloadUrl"], "", ok, note))
            log(f"[{done}/{len(tasks)}] {'OK ' if ok else 'FAIL'} {ver} {item['name']} {note}")

    with MANIFEST.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["version", "category", "name", "code", "url", "size", "ok", "note"])
        w.writerows(sorted(results))

    ok = sum(1 for r in results if r[6])
    log(f"DONE ok={ok} fail={len(results) - ok} manifest={MANIFEST}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
