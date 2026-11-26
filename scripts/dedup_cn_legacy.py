#!/usr/bin/env python3
"""清理 docs/cn 中因版本正则缺陷漏检的重复老版本文档。

用更稳健的身份规则（去掉 3.18.1/2/3/6 全系列版本号 + 日期 + "版"字等）
找出同身份多版本组，保留最高版本，其余移到集中备份目录。

默认 dry-run；--apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import shutil
import unicodedata
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
CN = ROOT / "docs/cn"
BACKUP = ROOT / "outputs" / "legacy_duplicates_backup"
PLAN = ROOT / "outputs" / "legacy_duplicates_plan.csv"

VER = re.compile(r"[Vv]?3\.18\.\d+(?:[-\s]?(?:SP)?\d{4})?|[-_]?(?:SP)?\d{4}", re.I)
DATE = re.compile(r"\b\d{8}\b")
PREFIX = re.compile(r"^阿里云\s*专有云(?:\s*企业版)?\s*", re.I)
NOISE = re.compile(r"专有云基础服务|专有云平台企业版|企业版")


def core2(name: str) -> str:
    s = pathlib.PurePath(name).stem
    s = PREFIX.sub("", s)
    s = VER.sub("", s)
    s = DATE.sub("", s)
    s = NOISE.sub("", s)
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[\s\u3000（）()·\-—_版]", "", s).lower()


def ver_key(p: pathlib.Path) -> tuple[int, int, str]:
    m = re.search(r"[Vv]3\.18\.(\d+)", p.name)
    minor = int(m.group(1)) if m else 0
    sp = 1 if "SP2607" in p.name else 0
    return (minor, sp, p.name)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    groups: dict[str, list[pathlib.Path]] = defaultdict(list)
    for p in CN.rglob("*.pdf"):
        groups[core2(p.name)].append(p)

    dups = {k: sorted(v, key=ver_key) for k, v in groups.items() if len(v) > 1}
    plan = []
    for core, items in dups.items():
        keep = items[-1]
        for drop in items[:-1]:
            plan.append({"core": core, "keep": keep, "drop": drop})

    print(f"重复组 {len(dups)}，将移出 {len(plan)} 份老版本，保留 {len(dups)} 份最新版")

    with PLAN.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["core", "action", "path", "version", "keep_path"])
        for r in plan:
            w.writerow([r["core"], "MOVE_TO_BACKUP",
                        str(r["drop"].relative_to(ROOT)), ver_key(r["drop"])[:2],
                        str(r["keep"].relative_to(ROOT))])

    if not args.apply:
        print("\n[DRY-RUN] 未改动文件。清单:", PLAN)
        for r in plan:
            print("  移出", r["drop"].relative_to(CN))
        return

    moved = 0
    for r in plan:
        rel = r["drop"].relative_to(CN)
        dest = BACKUP / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(r["drop"]), str(dest))
        moved += 1
    # 清理空目录
    for d in sorted([p for p in CN.rglob("*") if p.is_dir()], reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass

    final = list(CN.rglob("*.pdf"))
    print(f"\n[APPLIED] 已移出 {moved} 份到 {BACKUP}")
    print("docs/cn 最终 PDF 数", len(final), "| 备份", len(list(BACKUP.rglob('*.pdf'))))


if __name__ == "__main__":
    main()
