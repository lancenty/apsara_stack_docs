#!/usr/bin/env python3
"""找出 docs/cn 与 docs/en 中「早期版本独有、没有 3.18.6 对应」的文档。

口径：
- 按文件名归一化身份（去前缀/版本/日期/标点）分组；
- 组内只要有一份 3.18.6（含 SP2607 / 2607）就视为已有新版；
- 文件名没有版本标记时，读取 PDF 封面确认是否为 3.18.6，避免误判；
- 每个身份只输出最高老版本的一份。

输出：outputs/legacy_only_docs.csv、reports/老版本独有文档清单.md
"""
from __future__ import annotations

import csv
import pathlib
import re
import unicodedata
from collections import defaultdict

from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CSV_OUT = ROOT / "outputs" / "legacy_only_docs.csv"
MD_OUT = ROOT / "reports" / "老版本独有文档清单.md"

VER = re.compile(r"[Vv]?3\.\d+\.\d+(?:[-\s]?(?:SP)?\d{4})?|[-_]?(?:SP)?\d{4}", re.I)
DATE = re.compile(r"(?<!\d)\d{8}(?!\d)")
CN_PREFIX = re.compile(r"^阿里云\s*专有云(?:\s*企业版)?\s*", re.I)
EN_PREFIX = re.compile(r"^Alibaba\s+Cloud\s+Apsara\s+Stack(?:\s+Enterprise)?\s*", re.I)
CN_NOISE = re.compile(r"专有云基础服务|专有云平台企业版|企业版")
PV = re.compile(r"Product\s+Version\s*[:：]\s*([\w.\-]+)", re.I)
ASTACK = re.compile(r"Apsara\s+Stack\s+(v?3\.\d+\.\d+(?:-[\w.]+)?)", re.I)


def long_path(p: pathlib.Path) -> str:
    return "\\\\?\\" + str(p.resolve())


def cover_text(p: pathlib.Path) -> str:
    try:
        t = PdfReader(long_path(p)).pages[0].extract_text() or ""
        return unicodedata.normalize("NFKC", re.sub(r"\s+", " ", t))
    except Exception:
        return ""


def core(p: pathlib.Path, lang: str) -> str:
    s = p.stem
    s = (CN_PREFIX if lang == "cn" else EN_PREFIX).sub("", s)
    s = VER.sub("", s)
    s = DATE.sub("", s)
    if lang == "cn":
        s = CN_NOISE.sub("", s)
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[\s\u3000（）()\[\]·\-—_版]", "", s).lower()


def ver_key(v: str) -> tuple[int, ...]:
    nums = [int(x) for x in re.findall(r"\d+", v)]
    return tuple(nums[:3]) if len(nums) >= 3 else (0, 0, 0)


GUIDE_PATTERNS = [
    ("开发指南", "dev"), ("用户指南", "user"), ("运维指南", "ops"), ("产品简介", "intro"),
    ("developer guide", "dev"), ("user guide", "user"),
    ("operations and maintenance guide", "ops"), ("product introduction", "intro"),
    # 个别老文档标题把 Guide 截掉，如 "... Developer 20241024.pdf"
    ("developer", "dev"), ("user", "user"),
    ("operations and maintenance", "ops"), ("introduction", "intro"),
]


def guide_type(name: str) -> str:
    n = name.lower()
    for pat, key in GUIDE_PATTERNS:
        if pat in n:
            return key
    return "other"


def main() -> None:
    rows = []
    caches: dict[str, str] = {}
    all_docs: list[dict] = []
    for lang in ("cn", "en"):
        for p in (DOCS / lang).rglob("*.pdf"):
            rel = p.relative_to(ROOT)
            all_docs.append({
                "lang": lang,
                "category": rel.parts[2],
                "product": rel.parts[3],
                "filename": p.name,
                "guide": guide_type(p.name),
                "is36": bool(re.search(r"3\.18\.6", p.name, re.I)),
            })

    for lang in ("cn", "en"):
        groups: dict[str, list[pathlib.Path]] = defaultdict(list)
        for p in (DOCS / lang).rglob("*.pdf"):
            groups[core(p, lang)].append(p)

        for _core, items in groups.items():
            has36 = False
            infos = []
            for p in items:
                cv = caches.setdefault(str(p), cover_text(p))
                v36 = bool(re.search(r"3\.18\.6", p.name, re.I) or re.search(r"3\.18\.6", cv, re.I))
                has36 = has36 or v36
                m = re.search(r"v?3\.\d+\.\d+(?:-(?:sp)?\d{4})?", p.name, re.I)
                if m:
                    ver = m.group(0)
                else:
                    ver = (PV.search(cv) or ASTACK.search(cv))
                    ver = ver.group(1) if ver else "(无版本标记)"
                rel = p.relative_to(ROOT)
                infos.append({
                    "language": "中文" if lang == "cn" else "英文",
                    "lang": lang,
                    "version": ver,
                    "category": rel.parts[2],
                    "product": rel.parts[3],
                    "filename": p.name,
                    "path": str(rel),
                    "core": _core,
                    "_v36": v36,
                })
            if has36:
                continue
            best = sorted(infos, key=lambda x: (ver_key(x["version"]), x["filename"]))[-1]
            best["version_count"] = len(infos)
            best["all_versions"] = " / ".join(sorted({i["version"] for i in infos}))
            # 二次复核：同一级分类/二级产品 + 同指南类型是否已有 3.18.6
            cand = [d for d in all_docs if d["is36"] and d["lang"] == lang
                    and d["product"] == best["product"] and d["guide"] == guide_type(best["filename"])]
            best["has_same_product_guide_36"] = bool(cand)
            best["candidate_36"] = cand[0]["filename"] if cand else ""
            rows.append(best)

    rows.sort(key=lambda r: (r["lang"], r["category"], r["product"], r["filename"]))

    with CSV_OUT.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=[
            "language", "version", "category", "product", "filename", "path", "all_versions",
            "has_same_product_guide_36", "candidate_36"
        ])
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in w.fieldnames})

    # Markdown 报告
    true_old = [r for r in rows if not r["has_same_product_guide_36"]]
    renamed = [r for r in rows if r["has_same_product_guide_36"]]

    lines = [
        "# 老版本独有文档清单",
        "",
        "> 口径一（严格身份）：文件名归一化后，组内**没有任何 3.18.6（含 SP2607 / 2607）文档**。",
        "> 口径二（复核后真正独有）：在严格身份独有中，再检查「同一级分类 + 同二级产品 + 同指南类型」是否已有 3.18.6；若已有一律不算独有（多为产品名/子名变化导致严格身份漏配）。",
        "> 文件名无版本标记时读取 PDF 封面判断；每个身份只列最高老版本一份。",
        "",
        "## 汇总",
        "",
        "| 语言 | 严格身份独有 | 复核后已有同产品同指南新版 | 真正老版本独有 |",
        "|---|---:|---:|---:|",
    ]
    for lang, label in (("cn", "中文"), ("en", "英文")):
        sub = [r for r in rows if r["lang"] == lang]
        t = [r for r in sub if not r["has_same_product_guide_36"]]
        m = [r for r in sub if r["has_same_product_guide_36"]]
        lines.append(f"| {label} | {len(sub)} | {len(m)} | {len(t)} |")
    lines += ["", f"严格身份独有 **{len(rows)}** 份；复核后真正老版本独有 **{len(true_old)}** 份（中文 {sum(1 for r in true_old if r['lang']=='cn')}、英文 {sum(1 for r in true_old if r['lang']=='en')}）。", ""]

    for title, subset in (("真正老版本独有", true_old), ("名称变化但已有同产品同指南新版", renamed)):
        lines += [f"## {title}（{len(subset)} 份）", ""]
        if not subset:
            lines += ["无。", ""]
            continue
        lines += ["| 语言 | 版本 | 一级分类 | 二级产品 | 文件名 |" + (" | 对应 3.18.6 文档 |" if subset is renamed else ""),
                  "|---|---|---|---|---|" + ("---|" if subset is renamed else "")]
        for r in subset:
            base = f"| {r['language']} | {r['version']} | {r['category']} | {r['product']} | `{r['filename']}` |"
            if subset is renamed:
                base += f" `{r['candidate_36']}` |"
            lines.append(base)
        lines.append("")

    lines += [
        "## 排除说明",
        "",
        "- `Database/ApsaraDB for POLARDB/Secondary Edition)...pdf` 三份文件名被截断，但封面 `Product Version: v3.18.6-2607`，已排除。",
        "- `Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack.pdf` 封面含 `Apsara Stack 3.18.6`，已排除。",
        "- `Alibaba Cloud Apsara Stack Terraform User Guide 20241115.pdf` 无产品版本字段，仅有文档版本 20241115，按早期文档列入，需人工确认是否应保留。",
        "",
        f"机器可读清单：`outputs/legacy_only_docs.csv`。",
        "",
    ]
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"严格身份独有 {len(rows)}；复核后真正独有 {len(true_old)}（中文 {sum(1 for r in true_old if r['lang']=='cn')}、英文 {sum(1 for r in true_old if r['lang']=='en')}）")
    print("CSV:", CSV_OUT)
    print("MD :", MD_OUT)


if __name__ == "__main__":
    main()
