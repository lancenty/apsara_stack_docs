#!/usr/bin/env python3
"""核验两个平台全量下载结果。"""
from __future__ import annotations

import csv
import pathlib
import zipfile
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
ZH = ROOT / "downloads/zh_all_versions"
EN = ROOT / "downloads/en_all_versions"


def check(root: pathlib.Path, kind: str) -> None:
    with (root / "download_manifest.csv").open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    bad = []
    total = 0
    for r in rows:
        if kind == "zh":
            p = root / r["version"] / (r["code"] + ".zip")
        else:
            p = root / (r["version"] or "unknown") / r["filename"]
        lp = pathlib.Path("\\\\?\\" + str(p.resolve()))
        if not lp.exists():
            bad.append(("missing", str(p)))
            continue
        sz = lp.stat().st_size
        total += sz
        try:
            with lp.open("rb") as fp:
                head = fp.read(4)
            if kind == "zh":
                if head[:2] != b"PK" or not zipfile.is_zipfile(lp):
                    bad.append(("bad zip", str(p)))
            else:
                if head != b"%PDF":
                    bad.append(("bad pdf", str(p)))
        except Exception as e:
            bad.append((repr(e), str(p)))
    print(f"{kind.upper()} rows={len(rows)} ok={sum(r['ok']=='True' for r in rows)} "
          f"bad={len(bad)} size={total/1024**3:.2f}GiB parts={len(list(root.rglob('*.part')))}")
    versions = Counter(r["version"] for r in rows)
    print("  versions:", dict(versions))
    for x in bad[:20]:
        print("  BAD", x)


def main() -> None:
    check(ZH, "zh")
    check(EN, "en")


if __name__ == "__main__":
    main()
