#!/usr/bin/env python3
"""准备两个平台全量下载清单。

中文：读取 outputs/api_all_versions/products_<ver>.json（14 个企业版版本）的全部 downloadUrl。
英文：从英文下载源页内嵌 cardArray 提取全部 PDF href（952 个唯一链接）。

输出：
  outputs/zh_all_versions_plan.csv
  outputs/en_all_versions_plan.csv
"""
from __future__ import annotations

import csv
import html
import json
import pathlib
import re
import urllib.parse
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
ZH_API = ROOT / "outputs/api_all_versions"
EN_PAGE = ROOT / ".workbuddy/en_download_page.html"
ZH_PLAN = ROOT / "outputs/zh_all_versions_plan.csv"
EN_PLAN = ROOT / "outputs/en_all_versions_plan.csv"


def main() -> None:
    # 中文
    zh = []
    for p in sorted(ZH_API.glob("products_*.json")):
        ver = p.stem[len("products_"):]
        data = json.loads(p.read_text(encoding="utf-8")).get("data") or []
        for item in data:
            url = item.get("downloadUrl") or ""
            if url.startswith("//"):
                url = "https:" + url
            if not url:
                continue
            zh.append({
                "version": ver,
                "code": item.get("code", ""),
                "name": item.get("name", ""),
                "category": item.get("category", ""),
                "url": url,
            })
    with ZH_PLAN.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["version", "code", "name", "category", "url"])
        w.writeheader()
        w.writerows(zh)

    # 英文
    s = html.unescape(EN_PAGE.read_text(encoding="utf-8", errors="replace"))
    cards = re.findall(r"\{[^{}]*?\"href\":\"https://apsarastackdocument[^{}]*?\}", s)
    en = []
    seen = set()
    for raw in cards:
        try:
            obj = json.loads(raw)
        except Exception:
            continue
        url = obj.get("href", "")
        if not url or url in seen:
            continue
        seen.add(url)
        filename = pathlib.PurePosixPath(
            urllib.parse.urlparse(url).path
        ).name
        filename = urllib.parse.unquote(filename)
        en.append({
            "version": obj.get("Version", ""),
            "product": obj.get("Product", ""),
            "name": obj.get("name", ""),
            "filename": filename,
            "url": url,
        })
    # 同一 version 下 filename 冲突时追加序号
    used: Counter[tuple[str, str]] = Counter()
    for r in en:
        key = (r["version"], r["filename"])
        used[key] += 1
        if used[key] > 1:
            stem, ext = pathlib.Path(r["filename"]).stem, pathlib.Path(r["filename"]).suffix
            r["filename"] = f"{stem}_{used[key]}{ext}"
    with EN_PLAN.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["version", "product", "name", "filename", "url"])
        w.writeheader()
        w.writerows(en)

    print("ZH", len(zh), "ZIPs across", len(set(r["version"] for r in zh)), "versions")
    print(dict(Counter(r["version"] for r in zh)))
    print("EN", len(en), "PDFs across", len(set(r["version"] for r in en)), "versions")
    print(dict(Counter(r["version"] for r in en)))
    print("EN duplicate filename collisions resolved:", sum(1 for r in en if re.search(r"_\d+\.pdf$", r["filename"])))
    print("plans:", ZH_PLAN, EN_PLAN)


if __name__ == "__main__":
    main()
