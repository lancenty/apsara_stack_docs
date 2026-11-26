#!/usr/bin/env python3
"""按 PDF 封面字段统一文件名中的版本号（保守方案）。

只替换文件名里的「产品版本」和「文档版本」为封面值，其余部分（产品名、指南类型）
保持原样不动 —— 因为封面里产品名/指南类型常粘连或缺省，重建会引入错误。

封面字段（验证过 100% 与文件名一致）：
  中文: 产品版本:<ver> / 文档版本:<date>
  英文: Product Version: <ver> / Document Version: <date>

目标：目录内所有文件名使用封面原样的版本写法（如 v3.18.6 / v3.18.6-SP2607），
      大小写与 SP 后缀以封面为准，不再出现 V3.18.6 vs v3.18.6 混用。

默认 dry-run；--apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import unicodedata
from collections import Counter
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "outputs" / "rename_by_cover_manifest.csv"

# 文件名中旧版本写法（覆盖 3.18.1/2/3/6 全系列 + SP/2607 后缀）
VER_RE = re.compile(r"[Vv]?3\.18\.\d+(?:[-\s]?(?:SP)?\d{4})?", re.I)
DATE_RE = re.compile(r"(?<!\d)\d{8}(?!\d)")


def cover_fields(p: pathlib.Path, lang: str) -> tuple[str, str] | None:
    try:
        t = PdfReader(str(p)).pages[0].extract_text() or ""
    except Exception:
        return None
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"\s+", " ", t)
    if lang == "cn":
        m = re.search(r"产品版本\s*[:：]\s*([\w.\-]+)", t)
        d = re.search(r"文档版本\s*[:：]\s*(\d{8})", t)
    else:
        m = re.search(r"Product Version\s*[:：]\s*([\w.\-]+)", t, re.I)
        d = re.search(r"Document Version\s*[:：]\s*(\d{8})", t, re.I)
    if not m or not d:
        return None
    return m.group(1), d.group(1)


def make_name(old: str, ver: str, date: str) -> str:
    stem = pathlib.PurePath(old).stem
    # 用封面版本替换文件名中的版本（仅一个）
    stem, n1 = VER_RE.subn(ver, stem, count=1)
    # 用封面日期替换文件名中最后一组 8 位数字
    matches = list(DATE_RE.finditer(stem))
    if matches:
        last = matches[-1]
        stem = stem[:last.start()] + date + stem[last.end():]
    return stem + ".pdf"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    plan = []
    for lang in ["cn", "en"]:
        for p in sorted((ROOT / "docs" / lang).rglob("*.pdf")):
            fields = cover_fields(p, lang)
            if fields is None:
                plan.append((lang, p, "FAIL", p.name, "", ""))
                continue
            ver, date = fields
            new = make_name(p.name, ver, date)
            status = "SAME" if new == p.name else "RENAME"
            plan.append((lang, p, status, new, ver, date))

    print("总计", len(plan), dict(Counter(x[2] for x in plan)))
    print("\n解析失败:")
    for x in [x for x in plan if x[2] == "FAIL"][:10]:
        print("  ", x[1].relative_to(ROOT))
    print("\n将重命名样例:")
    for x in [x for x in plan if x[2] == "RENAME"][:20]:
        print("  旧:", x[1].name)
        print("  新:", x[3])

    with MANIFEST.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["lang", "status", "old_path", "new_name", "cover_version", "cover_date"])
        for lang, p, status, new, ver, date in plan:
            w.writerow([lang, status, str(p.relative_to(ROOT)), new, ver, date])

    if not args.apply:
        print("\n[DRY-RUN] 未改动。清单:", MANIFEST)
        return

    # 冲突检查
    targets = {}
    for lang, p, status, new, ver, date in plan:
        if status != "RENAME":
            continue
        t = p.parent / new
        if t in targets or (t.exists() and t != p):
            print("  冲突:", t)
            raise SystemExit(1)
        targets[t] = p

    renamed = 0
    for lang, p, status, new, ver, date in plan:
        if status != "RENAME":
            continue
        p.rename(p.parent / new)
        renamed += 1
    print(f"\n[APPLIED] 重命名 {renamed} 份，清单:", MANIFEST)


if __name__ == "__main__":
    main()
