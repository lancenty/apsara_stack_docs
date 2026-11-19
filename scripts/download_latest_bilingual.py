#!/usr/bin/env python3
"""Download the latest bilingual Apsara Stack documents from the local manifest."""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import os
import tempfile
import threading
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "apsara_latest_manifest.csv"
LANG_DIRS = {"\u4e2d\u6587": "docs/cn", "\u82f1\u6587": "docs/en"}
UA = "Mozilla/5.0 (compatible; ApsaraDocsArchive/1.0)"
PRINT_LOCK = threading.Lock()


def fetch(row: dict[str, str]) -> tuple[str, str]:
    language = row["language"]
    folder = ROOT / LANG_DIRS[language]
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / row["filename"]
    expected = int(row["size_bytes"] or 0)
    if target.exists() and (not expected or target.stat().st_size == expected):
        return "skip", row["filename"]

    fd, temp_name = tempfile.mkstemp(prefix=".download-", suffix=".part", dir=folder)
    os.close(fd)
    try:
        with requests.get(row["url"], headers={"User-Agent": UA}, stream=True, timeout=(20, 180)) as response:
            response.raise_for_status()
            with open(temp_name, "wb") as output:
                for chunk in response.iter_content(1024 * 128):
                    if chunk:
                        output.write(chunk)
        actual = os.path.getsize(temp_name)
        with open(temp_name, "rb") as source:
            if source.read(5) != b"%PDF-":
                raise ValueError("response is not a PDF")
        if expected and actual != expected:
            raise ValueError(f"size mismatch: expected {expected}, received {actual}")
        os.replace(temp_name, target)
        return "ok", row["filename"]
    except Exception:
        try:
            os.remove(temp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("all", "zh", "en"), default="all")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    with MANIFEST.open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    if args.language == "zh":
        rows = [row for row in rows if row["language"] == "\u4e2d\u6587"]
    elif args.language == "en":
        rows = [row for row in rows if row["language"] == "\u82f1\u6587"]

    counts = {"ok": 0, "skip": 0, "fail": 0}
    failures: list[tuple[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(fetch, row): row for row in rows}
        for future in concurrent.futures.as_completed(jobs):
            row = jobs[future]
            try:
                status, _name = future.result()
                counts[status] += 1
                if counts[status] % 25 == 0:
                    with PRINT_LOCK:
                        print(f"Progress: downloaded={counts['ok']} present={counts['skip']} failed={counts['fail']}", flush=True)
            except Exception as error:
                counts["fail"] += 1
                failures.append((row["filename"], f"{type(error).__name__}: {error}"))

    print(f"Done: downloaded={counts['ok']} already_present={counts['skip']} failed={counts['fail']}")
    if failures:
        outputs = ROOT / "outputs"
        outputs.mkdir(parents=True, exist_ok=True)
        with (outputs / "download_failures.txt").open("w", encoding="utf-8") as output:
            for name, error in failures:
                output.write(f"{name}\t{error}\n")
        print("Failure details: outputs/download_failures.txt")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
