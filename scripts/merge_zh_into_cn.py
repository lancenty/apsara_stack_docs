#!/usr/bin/env python3
"""把 docs_zh 三个版本与现有 docs/cn 合并去重，保留最新版到 docs/cn。

策略：
1. 文档身份 core = 文件名去掉前缀/版本/批次/日期后的归一化文本
2. 同一 core 只保留最高优先级版本：1030 > SP2607 > 0430 > 现有 cn
3. 目录结构沿用 cn 的 <一级分类>/<二级产品>，产品名优先复用 cn 已有目录名
4. 备份被替换的 cn 原文件到 outputs/cn_merge_backup/

默认仅预览（--dry-run），加 --apply 执行。
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import shutil
import unicodedata
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
CN = ROOT / "docs/cn"
ZH = ROOT / "docs_zh"
BACKUP = ROOT / "outputs" / "cn_merge_backup"

SOURCE_RANK = {"cn": 0, "0430": 1, "SP2607": 2, "1030": 3}
BATCH_SHORT = {"v3.18.6-0430": "0430", "v3.18.6-SP2607": "SP2607", "v3.18.6-1030": "1030"}

# zh 一级分类 -> cn 一级分类
CAT_MAP = {
    "专有云云平台": "云平台",
    "统一运营平台": "云平台",
    "交付服务": "云平台",
    "监控与运维平台": "监控与运维服务",
    "计算服务": "计算",
    "云原生服务": "计算",
    "存储服务": "存储",
    "网络服务": "网络",
    "数据库服务": "数据库",
    "大数据服务": "大数据",
    "安全服务": "安全",
    "应用服务": "中间件",
    "人工智能": "OpenTrek",
    "其他": "云平台",
}

# zh 产品名 -> cn 二级产品目录名（仅列与 cn 现有目录不同的）
PRODUCT_MAP = {
    "容器服务Kubernetes版": "容器服务 Kubernetes",
    "容器镜像服务": "容器镜像服务 ACR",
    "资源编排": "资源编排 ROS",
    "运维编排": "运维编排 OOS",
    "专有网络VPC": "专有网络 VPC",
    "负载均衡": "负载均衡 SLB",
    "云数据库RDS": "云数据库 RDS",
    "云数据库MongoDB版": "云数据库 MongoDB",
    "云数据库 Tair（兼容 Redis）": "云数据库 Redis",
    "密钥管理服务": "密钥管理服务 KMS",
    "应用身份服务": "应用身份服务 IDaaS",
    "应用实时监控服务": "应用实时监控服务 ARMS",
    "日志服务": "日志服务 SLS",
    "对象存储": "云定义存储",
    "文件存储NAS": "文件存储 NAS",
    "弹性文件存储NAS": "弹性文件存储 EFS-NAS",
    "大数据计算服务": "大数据计算 MaxCompute",
    "DataWorks": "大数据开发治理平台 DataWorks",
    "Elasticsearch": "检索分析服务 Elasticsearch",
    "云盾云防火墙": "云防火墙",
    "云盾堡垒机": "堡垒机",
    "云安全中心（安骑士）": "安骑士",
    "云安全中心（态势感知）": "云安全中心（态势感知）",
    "云盾网络检测与响应": "网络流量检测与响应",
    # 灾备管理平台 / 混合云存储CDS / 对象存储 在 cn 无真正对应，保留原名新建目录
    "统一云管平台": "统一云管平台",
    "云迁移中心": "云迁移中心",
    "专有云运维平台": "专有云运维平台",
    "应用运维平台": "应用运维平台",
    "消息队列 RocketMQ 版": "消息队列 MQ",
    "云消息队列 RocketMQ 版": "消息队列 MQ",
    "消息队列Kafka版": "消息队列 Kafka版",
    "全栈云平台": "专有云云平台",
    "智能体工厂 OpenTrek": "飞天助理",
    # 以下 cn 无对应，保留原名（新建目录）
}

# 修正：对象存储不是"云定义存储"（cn 的云定义存储是另一产品族），保留原名
PRODUCT_MAP.pop("对象存储", None)
PRODUCT_MAP.pop("灾备管理平台", None)

PREFIX_RE = re.compile(r"^阿里云\s*专有云\s*", re.IGNORECASE)
VER_LONG_RE = re.compile(r"[Vv]_?3[_.]18[_.]6[_.]\d{8}", re.IGNORECASE)
VER_RE = re.compile(r"[Vv]?3\.18\.6(?:[-\s]?(?:SP)?\d{4})?|[-_]?(?:SP)?\d{4}", re.IGNORECASE)
DATE_RE = re.compile(r"\b\d{8}\b")
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
    name = re.sub(r"[（）()·\-—_]", "", name)
    return name.lower()


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"[\s\u3000（）()·\-—_]", "", s)


def collect() -> list[dict]:
    rows = []
    for p in CN.rglob("*.pdf"):
        rel = p.relative_to(CN)
        rows.append({"source": "cn", "cat": rel.parts[0], "product": rel.parts[1],
                     "file": p.name, "core": core_of(p.name), "path": p})
    for short, key in BATCH_SHORT.items():
        base = ZH / short
        for p in base.rglob("*.pdf"):
            rel = p.relative_to(base)
            zh_cat, zh_prod = rel.parts[0], rel.parts[1]
            cat = CAT_MAP.get(zh_cat, zh_cat)
            product = PRODUCT_MAP.get(zh_prod, zh_prod)
            rows.append({"source": key, "cat": cat, "product": product,
                         "file": p.name, "core": core_of(p.name), "path": p,
                         "zh_cat": zh_cat, "zh_product": zh_prod})
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    rows = collect()
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[r["core"]].append(r)

    keep = []
    for core, items in groups.items():
        best = max(items, key=lambda r: SOURCE_RANK[r["source"]])
        keep.append((core, best, items))

    print(f"总输入 {len(rows)}，唯一身份 {len(groups)}，最终保留 {len(keep)}")
    print("保留来源", dict(Counter(r["source"] for _, r, _ in keep)))

    # 目标路径冲突检查（同 core 内可能有多个文件映射后同名，极少）
    dest_map: dict[pathlib.Path, tuple] = {}
    conflicts = []
    for core, best, items in keep:
        dest = CN / best["cat"] / best["product"] / best["file"]
        if dest in dest_map:
            conflicts.append((dest, dest_map[dest], best))
        dest_map[dest] = (core, best)

    print("目标路径冲突", len(conflicts))
    for dest, a, b in conflicts[:10]:
        print("  ", dest.relative_to(ROOT), "|", a[1]["source"], a[1]["path"].name, "vs", b["source"], b["path"].name)

    # 变更统计
    to_add, to_replace, unchanged = [], [], []
    for core, best, items in keep:
        dest = CN / best["cat"] / best["product"] / best["file"]
        if best["source"] == "cn":
            unchanged.append((best, dest))
        elif dest.exists():
            to_replace.append((best, dest))
        else:
            to_add.append((best, dest))

    print(f"\n新增 {len(to_add)}，替换 {len(to_replace)}，保持 {len(unchanged)}")
    print("将被移除的 cn 旧文件数", sum(1 for _, best, items in keep for x in items if x["source"] == "cn" and x is not best))

    # 详细清单
    out = ROOT / "outputs" / "cn_merge_final_plan.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["core", "action", "keep_source", "keep_cat", "keep_product", "keep_file",
                    "keep_from", "dest", "all_sources", "all_products"])
        for core, best, items in sorted(keep, key=lambda x: (x[1]["cat"], x[1]["product"], x[1]["file"])):
            dest = CN / best["cat"] / best["product"] / best["file"]
            action = "KEEP" if best["source"] == "cn" else ("REPLACE" if dest.exists() else "ADD")
            w.writerow([core, action, best["source"], best["cat"], best["product"], best["file"],
                        str(best["path"].relative_to(ROOT)),
                        str(dest.relative_to(ROOT)),
                        ",".join(sorted(set(x["source"] for x in items))),
                        ",".join(sorted(set(x.get("zh_product", x["product"]) for x in items)))])
    print("方案清单", out)

    if not args.apply:
        print("\n[DRY-RUN] 未修改任何文件。加 --apply 执行。")
        return

    # 执行
    backup_count = 0
    # 1) 备份所有将被替换/移除的 cn 原文件
    for core, best, items in keep:
        for x in items:
            if x["source"] == "cn" and x is not best:
                rel = x["path"].relative_to(CN)
                bak = BACKUP / rel
                bak.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(x["path"], bak)
                backup_count += 1
    # 2) 复制保留文档到目标
    copied = 0
    for core, best, items in keep:
        if best["source"] == "cn":
            continue
        dest = CN / best["cat"] / best["product"] / best["file"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(best["path"], dest)
        copied += 1
    # 3) 删除被替换掉的旧 cn 文件（core 组内非 best 的 cn 文件，且目标路径不同）
    removed = 0
    for core, best, items in keep:
        for x in items:
            if x["source"] != "cn" or x is best:
                continue
            dest = CN / best["cat"] / best["product"] / best["file"]
            if x["path"] == dest:
                continue
            if x["path"].exists():
                x["path"].unlink()
                removed += 1
    # 4) 清理空目录
    for d in sorted([p for p in CN.rglob("*") if p.is_dir()], reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass

    print(f"\n[APPLIED] 备份 {backup_count}，复制 {copied}，删除旧文件 {removed}")
    final = list(CN.rglob("*.pdf"))
    print("docs/cn 最终 PDF 数", len(final))
    print("一级分类", dict(Counter(p.relative_to(CN).parts[0] for p in final)))


if __name__ == "__main__":
    main()
