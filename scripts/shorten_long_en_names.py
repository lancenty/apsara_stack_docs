#!/usr/bin/env python3
"""修复 docs/en 中因文件名过长超过 Windows MAX_PATH 而无法打开的文档。

用长路径前缀 (\\\\?\\) 读取封面，按封面字段重构精简文件名：
  <Product Version> <简短产品名> <Guide Type> <Document Version>.pdf

简短产品名由目录名 + 文件名中的子产品推导，去掉重复与冗余前缀。
默认 dry-run；--apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import unicodedata
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "docs/en"
MANIFEST = ROOT / "outputs" / "long_en_names_fix.csv"
MAX_NAME = 110


def long_path(p: pathlib.Path) -> str:
    return "\\\\?\\" + str(p.resolve())


def cover(p: pathlib.Path) -> tuple[str, str]:
    t = unicodedata.normalize("NFKC", PdfReader(long_path(p)).pages[0].extract_text() or "")
    t = re.sub(r"\s+", " ", t)
    pv = re.search(r"Product Version\s*[:：]\s*([\w.\-]+)", t, re.I)
    dv = re.search(r"Document Version\s*[:：]\s*(\d{8})", t, re.I)
    if not pv or not dv:
        raise ValueError("封面无字段")
    return pv.group(1), dv.group(1)


GUIDES = ["Developer Guide", "User Guide", "Operations and Maintenance Guide", "Product Introduction"]

# 已知长产品名 -> 稳定简称。保留最有辨识度的子产品，避免按字符截断成 "Mar"/"Serv"/"Ins"。
ALIASES = {
    "Enterprise Distributed Application Service SchedulerX 2.0": "EDAS SchedulerX",
    "Enterprise Distributed Application Service SchedulerX": "EDAS SchedulerX",
    "Realtime Compute Realtime Compute for Apache Flink": "Realtime Compute for Apache Flink",
    "Application Operation Platform Application Hybrid Marketplace": "Application Hybrid Marketplace",
    "Server Guard Advanced Edition Container Security Service": "Server Guard Container Security",
    "Situation Awareness Cloud Security Management Center": "Cloud Security Management Center",
    "Web Application Firewall Web Application Firewall-Instance": "WAF Instance",
}


def short_product(dir_name: str, stem: str) -> str:
    # 从文件名中提取产品段（版本之后、指南类型之前），去掉与目录重复的专家
    m = re.search(r"Stack\s+(?:V?v?3\.18\.[\d.\-SP]+)\s+(.*?)(?:\s+(?:Developer Guide|User Guide|Operations and Maintenance Guide|Product Introduction)\b)", stem)
    seg = m.group(1) if m else dir_name
    # 去掉冗余前缀
    seg = re.sub(r"^Alibaba Cloud Security-", "", seg)
    seg = re.sub(r"\s*\([^)]*\)", "", seg)  # 去 (EDAS)/(Compute-Storage...) 等括号
    # 去掉完全重复的前后两半（如 "EDAS EDAS"），仅当整个字符串严格由两段相同词组构成
    words = seg.split()
    n = len(words)
    if n % 2 == 0 and words[:n // 2] == words[n // 2:]:
        seg = " ".join(words[:n // 2])
    seg = re.sub(r"\s+", " ", seg).strip(" -")
    # 长产品名使用稳定简称；保留尾随的版本号等补充信息
    for old, new in ALIASES.items():
        if seg == old or seg.startswith(old + " "):
            rest = seg[len(old):].strip()
            seg = new + (" " + rest if rest else "")
            break
    return seg.strip(" -")


def fit_product(prod: str, ver: str, gtype: str, date: str) -> str:
    # 文件名格式: <ver> <prod> <gtype> <date>.pdf
    # 固定开销 = 3 个空格 + ".pdf"(4)，共 7；用总上限反推产品段预算。
    budget = MAX_NAME - len(ver) - len(gtype) - len(date) - 7
    if budget <= 0:
        raise ValueError(f"版本/指南/日期过长，无法控制在 {MAX_NAME} 字符内")
    if len(prod) <= budget:
        return prod
    # 优先保留尾部词组（通常是子产品名），按词边界截断，不产生半个单词。
    kept: list[str] = []
    for word in reversed(prod.split()):
        candidate = " ".join([word] + kept)
        if len(candidate) <= budget:
            kept.insert(0, word)
        else:
            break
    if kept:
        return " ".join(kept)
    return prod[:budget].rstrip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    bad = []
    for p in EN.rglob("*.pdf"):
        try:
            with open(p, "rb") as f:
                f.read(4)
        except (FileNotFoundError, OSError):
            bad.append(p)

    plan = []
    for p in sorted(bad):
        try:
            ver, date = cover(p)
            stem = p.stem
            gtype = next((g for g in GUIDES if g in stem), "Guide")
            prod = fit_product(short_product(p.parent.name, stem), ver, gtype, date)
            new = f"{ver} {prod} {gtype} {date}.pdf"
            if len(new) > MAX_NAME:
                raise ValueError(f"生成文件名仍超过 {MAX_NAME}: {new}")
            plan.append((p, new, ver, date, prod, gtype, len(p.name)))
        except Exception as e:
            print("封面解析失败", p.name[:50], repr(e)[:80])

    print(f"待修复 {len(plan)} 份")
    for p, new, ver, date, prod, gtype, oldlen in plan:
        print(f"\n  {oldlen} -> {len(new)} 字符")
        print("  旧:", p.name)
        print("  新:", new)

    if plan or not MANIFEST.exists():
        with MANIFEST.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["old_name", "new_name", "old_len", "new_len", "product_version", "doc_version", "short_product", "guide_type", "dir"])
            for p, new, ver, date, prod, gtype, oldlen in plan:
                w.writerow([p.name, new, oldlen, len(new), ver, date, prod, gtype, str(p.parent.relative_to(ROOT))])
    else:
        # 验证阶段 plan 为空时，不要覆盖已生成的修复清单。
        print("  清单保持不变:", MANIFEST)

    if not args.apply:
        print("\n[DRY-RUN] 未改动。清单:", MANIFEST)
        return

    # 冲突检查
    targets = {}
    for p, new, *_ in plan:
        t = p.parent / new
        if t in targets or (t.exists() and t != p):
            print("  冲突:", t)
            raise SystemExit(1)
        targets[t] = p

    renamed = 0
    for p, new, *_ in plan:
        lp = long_path(p)
        dest = p.parent / new
        import os
        os.rename(lp, long_path(dest))
        renamed += 1

    print(f"\n[APPLIED] 重命名 {renamed} 份")
    # 验证
    ok = 0
    for p, new, *_ in plan:
        dest = p.parent / new
        try:
            with open(dest, "rb") as f:
                if f.read(4) == b"%PDF":
                    ok += 1
        except Exception:
            pass
    print(f"验证可打开: {ok}/{len(plan)}")
    print("清单:", MANIFEST)


if __name__ == "__main__":
    main()
