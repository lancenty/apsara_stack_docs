#!/usr/bin/env python3
"""解压中文整包到 docs_zh/<版本>/<分类>/<产品>/ 并生成 PDF 清单。

ZIP 内部结构：阿里云 企业版 <ver> <产品名> <日期>/<PDF 文件名>.pdf
输出结构：docs_zh/<版本短名>/<一级分类>/<产品名>/<PDF>
"""
from __future__ import annotations

import csv
import json
import pathlib
import re
import shutil
import zipfile
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "downloads" / "zh_bundles"
DEST = ROOT / "docs_zh"
MANIFEST_CSV = ROOT / "outputs" / "中文三版本PDF清单.csv"
MANIFEST_JSON = ROOT / "outputs" / "中文三版本PDF清单.json"
VER_SHORT = {
    "v_3_18_6_20250430": "v3.18.6-0430",
    "v_3_18_6_20260730": "v3.18.6-SP2607",
    "v_3_18_6_20261030": "v3.18.6-1030",
}


def safe(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip().rstrip(".")


def main() -> None:
    rows = []
    for ver, short in VER_SHORT.items():
        manifest = json.loads((ROOT / "outputs" / f"products_{ver}.json").read_text(encoding="utf-8"))["data"]
        meta = {x["code"]: x for x in manifest}
        for zpath in sorted((SRC / ver).glob("*.zip")):
            code = zpath.stem
            info = meta.get(code, {})
            category = safe(info.get("category", "未分类"))
            product = safe(info.get("name", code))
            out_dir = DEST / short / category / product
            out_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(zpath) as z:
                for member in z.namelist():
                    if member.endswith("/") or not member.lower().endswith(".pdf"):
                        continue
                    # 丢弃 ZIP 内的第一层日期目录，只保留文件名
                    fname = safe(pathlib.PurePosixPath(member).name)
                    dest = out_dir / fname
                    if not dest.exists():
                        with z.open(member) as src, dest.open("wb") as dst:
                            shutil.copyfileobj(src, dst)
                    rows.append({
                        "version": ver,
                        "version_short": short,
                        "category": category,
                        "product": product,
                        "code": code,
                        "file": fname,
                        "path": str(dest.relative_to(ROOT)).replace("\\", "/"),
                        "size": dest.stat().st_size,
                    })

    MANIFEST_CSV.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["version", "version_short", "category", "product", "code", "file", "path", "size"])
        w.writeheader()
        w.writerows(rows)
    MANIFEST_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    print("PDF total", len(rows))
    for ver, short in VER_SHORT.items():
        sub = [r for r in rows if r["version"] == ver]
        print(f"{short}: {len(sub)} PDF, {len(set(r['code'] for r in sub))} products, {sum(r['size'] for r in sub)/1024**3:.2f} GiB")
    print("CSV", MANIFEST_CSV)
    print("JSON", MANIFEST_JSON)


if __name__ == "__main__":
    main()
