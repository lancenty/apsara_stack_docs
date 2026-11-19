#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apsara Stack 文档版本去重
==========================
同一文档在 V3.18.2 / V3.18.3 / V3.18.6 多个版本中会出现多次。
核心身份 = 文件名去掉「前缀(阿里云 专有云) + 版本号 + 日期」后剩余部分。
同一核心身份只保留最高版本（V3.18.6 > V3.18.3 > V3.18.2），删除低版本重复。

用法：
  python3 dedup.py            # 预览：列出会被删除的低版本项及数量
  python3 dedup.py --apply    # 确认后实际删除本地低版本 PDF
  python3 dedup.py --out /path/to/apsara_stack_docs
"""
import json
import os
import re
import argparse
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LINKS_JSON = os.path.join(ROOT, "data", "oss_links.json")

PREFIX_RE = re.compile(r"^阿里云\s*专有云\s*", re.IGNORECASE)
VER_RE = re.compile(r"[Vv]3\.18\.\d+")
DATE_RE = re.compile(r"\b\d{8}\b")


def core(filename):
    """提取文档核心身份（去掉前缀、版本号、日期、扩展名、空白）。"""
    name = os.path.splitext(filename)[0]
    name = PREFIX_RE.sub("", name)
    name = VER_RE.sub("", name)
    name = DATE_RE.sub("", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def ver_tuple(version):
    m = re.search(r"[Vv](\d+)\.(\d+)\.(\d+)", version or "")
    if not m:
        return (0, 0, 0)
    return tuple(int(x) for x in m.groups())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="实际删除低版本文件（默认仅预览）")
    ap.add_argument("--out", default=os.path.join(ROOT, "downloads"))
    args = ap.parse_args()

    with open(LINKS_JSON, encoding="utf-8") as f:
        links = json.load(f)

    groups = {}
    for it in links:
        if it.get("status") != "ok":
            continue
        key = core(it["filename"])
        groups.setdefault(key, []).append(it)

    keep, remove = [], []
    for key, items in groups.items():
        if len(items) == 1:
            keep.extend(items)
            continue
        items_sorted = sorted(items, key=lambda x: ver_tuple(x["version"]))
        best = items_sorted[-1]
        keep.append(best)
        remove.extend(items_sorted[:-1])

    print(f"核心身份组数: {len(groups)}")
    print(f"保留(最高版本): {len(keep)}  可删除(低版本重复): {len(remove)}")

    if not args.apply:
        print("\n[预览] 以下低版本将被删除（加 --apply 执行）：")
        for it in remove:
            print(f"  [{it['version']}] {it['filename'][:70]}")
        return

    deleted = 0
    for it in remove:
        path = os.path.join(args.out, it["version"], it["filename"])
        if os.path.exists(path):
            os.remove(path)
            deleted += 1
        else:
            print(f"  [缺失] {path}")
    print(f"\n[已完成] 实际删除 {deleted} 个低版本文件；保留 {len(keep)} 个唯一文档。")


if __name__ == "__main__":
    main()
