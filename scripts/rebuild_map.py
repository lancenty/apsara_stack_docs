#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从当前两级目录结构重建完整的二级分类映射表（产物修复工具）。"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    rows = []
    # 语言标签 -> 文档实际目录（docs/cn 中文、docs/en 英文）
    doc_dirs = {"Chinese": os.path.join("docs", "cn"), "English": os.path.join("docs", "en")}
    for lang in ("Chinese", "English"):
        root = os.path.join(ROOT, doc_dirs[lang])
        for dp, _, fn in os.walk(root):
            for name in sorted(fn):
                full = os.path.join(dp, name)
                rel = os.path.relpath(full, root)
                parts = rel.split(os.sep)
                if len(parts) != 3:
                    print(f"[警告] 非标准层级: {rel}")
                    continue
                first, second, _ = parts
                rows.append({
                    "language": lang,
                    "first": first,
                    "second": second,
                    "filename": name,
                    "matched_keyword": "(按当前目录结构生成)",
                    "source": "",
                    "destination": full.replace("\\", "/"),
                })

    out = os.path.join(ROOT, "outputs", "classification_map_v2.csv")
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=[
            "language", "first", "second", "filename",
            "matched_keyword", "source", "destination",
        ])
        w.writeheader()
        w.writerows(rows)

    print(f"重建完成: {out}")
    print(f"  总计 {len(rows)} 行")
    print(f"  Chinese: {sum(1 for r in rows if r['language'] == 'Chinese')}")
    print(f"  English: {sum(1 for r in rows if r['language'] == 'English')}")


if __name__ == "__main__":
    main()
