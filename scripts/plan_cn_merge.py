#!/usr/bin/env python3
"""分析 docs/cn 与 docs_zh 三批文档的合并去重方案（只读，不改文件）。

文档身份 core = 文件名去掉「阿里云 专有云 + 版本 + 日期」后的关键词归一化文本。
同一 core 视为同一份文档的不同版本，只保留最高优先级版本。

版本优先级（高→低）：1030 > SP2607 > 0430 > 现有 docs/cn
"""
from __future__ import annotations

import csv
import pathlib
import re
import unicodedata
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]

# 优先级：数字越大越优先
SOURCE_RANK = {
    "cn": 0,           # 现有 docs/cn
    "0430": 1,
    "SP2607": 2,
    "1030": 3,
}

PREFIX_RE = re.compile(r"^阿里云\s*专有云\s*", re.IGNORECASE)
VER_RE = re.compile(r"[Vv]?3\.18\.6(?:[-\s]?(?:SP)?\d{4})?|[-_]?(?:SP)?\d{4}", re.IGNORECASE)
# 先去掉长版本（v_3_18_6_20250430 之类下划线写法）
VER_LONG_RE = re.compile(r"[Vv]_?3[_.]18[_.]6[_.]\d{8}", re.IGNORECASE)
DATE_RE = re.compile(r"\b\d{8}\b")
# 噪音词：批次日期目录名里的"专有云基础服务"等修饰，文档身份去掉
NOISE = re.compile(r"专有云基础服务|专有云平台企业版|企业版")


def core_of(filename: str) -> str:
    name = pathlib.PurePath(filename).stem
    name = PREFIX_RE.sub("", name)
    name = VER_LONG_RE.sub("", name)
    name = VER_RE.sub("", name)
    name = DATE_RE.sub("", name)
    name = NOISE.sub("", name)
    name = unicodedata.normalize("NFKC", name)
    name = re.sub(r"[\s\u3000]+", "", name)
    # 标点归一化
    name = re.sub(r"[（）()·\-—_]", "", name)
    return name.lower()


def collect() -> list[dict]:
    rows = []
    # 现有 docs/cn
    for p in pathlib.Path(ROOT / "docs/cn").rglob("*.pdf"):
        rel = p.relative_to(ROOT / "docs/cn")
        rows.append({
            "source": "cn",
            "cat": rel.parts[0], "product": rel.parts[1],
            "file": p.name, "core": core_of(p.name), "path": p,
        })
    # docs_zh 三批
    for short in ["v3.18.6-0430", "v3.18.6-SP2607", "v3.18.6-1030"]:
        key = "SP2607" if "SP2607" in short else ("0430" if "0430" in short else "1030")
        for p in (ROOT / "docs_zh" / short).rglob("*.pdf"):
            rel = p.relative_to(ROOT / "docs_zh" / short)
            rows.append({
                "source": key,
                "cat": rel.parts[0], "product": rel.parts[1],
                "file": p.name, "core": core_of(p.name), "path": p,
            })
    return rows


def main() -> None:
    rows = collect()
    print("总文档数", len(rows))
    by_src = Counter(r["source"] for r in rows)
    print("按来源", dict(by_src))

    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[r["core"]].append(r)
    print("唯一文档身份", len(groups))

    multi = {k: v for k, v in groups.items() if len(v) > 1}
    print("有多版本的身份数", len(multi))

    # 每个身份保留最高优先级
    keep, replace = [], []
    for core, items in groups.items():
        best = max(items, key=lambda r: SOURCE_RANK[r["source"]])
        keep.append(best)
        for it in items:
            if it is not best:
                replace.append((it, best))

    print(f"\n最终保留 {len(keep)} 份；被替换/去重 {len(replace)} 份")
    print("\n被替换来源分布", dict(Counter(r["source"] for r, _ in replace)))
    print("保留来源分布", dict(Counter(r["source"] for r in keep)))

    # 分类映射：新文档(cn 之外)的目标一级分类
    # cn 现有产品 -> 一级分类
    cn_prod2cat = {}
    for r in rows:
        if r["source"] == "cn":
            cn_prod2cat.setdefault(r["product"], r["cat"])
    print("\ncn 产品数", len(cn_prod2cat))
    zh_prods = set(r["product"] for r in rows if r["source"] != "cn")
    print("zh 产品数", len(zh_prods))
    matched = zh_prods & set(cn_prod2cat)
    print("产品名直接匹配上的", len(matched))
    print("未匹配的 zh 产品样例:", sorted(zh_prods - set(cn_prod2cat))[:25])

    # 是否存在"同一身份不同产品名"(需人工判断改名)
    name_conflict = 0
    for core, items in groups.items():
        if len(set(r["product"] for r in items)) > 1:
            name_conflict += 1
    print("\n同身份跨产品名(疑似改名)身份数", name_conflict)
    for core, items in list((k, v) for k, v in groups.items() if len(set(r["product"] for r in items)) > 1)[:15]:
        print("  ", core[:50], "=>", sorted(set(r["product"] for r in items)))

    # 输出完整方案 CSV
    out = ROOT / "outputs" / "cn_merge_plan.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["core", "action", "src_source", "src_cat", "src_product", "src_file", "src_path",
                    "keep_source", "keep_cat", "keep_product", "keep_file", "keep_path"])
        for core, items in groups.items():
            best = max(items, key=lambda r: SOURCE_RANK[r["source"]])
            for it in items:
                w.writerow([core, "KEEP" if it is best else "DROP", it["source"], it["cat"], it["product"],
                            it["file"], str(it["path"].relative_to(ROOT)),
                            best["source"], best["cat"], best["product"], best["file"],
                            str(best["path"].relative_to(ROOT))])
    print("\n方案已写入", out)


if __name__ == "__main__":
    main()
