#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
按图片中的阿里云专有云产品分类体系，对 docs/cn/ 和 docs/en/ 下的 PDF 按文件名分类。

用法:
    python classify_docs.py --dry-run   # 仅预演，输出统计与未分类清单，不改动文件
    python classify_docs.py --apply     # 创建分类目录并移动文件

分类顺序即优先级：越靠前的规则越先匹配（用于处理"容器安全"这类易混淆名称）。
"""

import argparse
import csv
import os
import re
import shutil
import unicodedata
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 分类 key -> (中文目录名, 英文目录名)
CATEGORIES = {
    "security":   ("安全", "Security"),
    "opentrek":   ("OpenTrek", "OpenTrek"),
    "monitor":    ("监控与运维服务", "Monitoring and Ops"),
    "cloud":      ("云平台", "Cloud Platform"),
    "compute":    ("计算", "Compute"),
    "storage":    ("存储", "Storage"),
    "network":    ("网络", "Networking"),
    "database":   ("数据库", "Database"),
    "middleware": ("中间件", "Middleware"),
    "bigdata":    ("大数据", "Big Data"),
}
UNCATEGORIZED = ("未分类", "Unclassified")

# 规则列表：(分类 key, 关键词列表)。关键词统一用小写，匹配时对文件名做 NFKC + 小写规范化。
RULES = [
    # 1. 安全（优先于计算，避免"容器安全"被"容器"误归计算）
    ("security", [
        "密钥管理服务", "key management service", "kms",
        "网络检测与响应", "network detection and response",
        "态势感知", "situation awareness", "云安全中心", "cloud security management center",
        "堡垒机", "bastionhost", "运维安全中心",
        "数据库审计", "database security audit",
        "ddos",
        "应用身份服务", "idaas",
        "安骑士", "server guard",
        "容器安全", "container security service",
        "web应用防火墙", "web application firewall", "waf",
        "云防火墙", "cloud security firewall", "nfv cloud firewall",
        "漏洞扫描", "cloud security scanner",
        "安全编排", "security orchestration automation and response", "soar",
        "静态数据脱敏", "static data masking",
        "apsara stack security", "云盾", "security administrator",
    ]),
    # 2. OpenTrek / AI
    ("opentrek", [
        "opentrek", "ai studio", "ai 网关", "ai gateway",
        "agentruntime", "copilot", "飞天助理",
    ]),
    # 3. 监控与运维服务（放在云平台之前，避免 Uni-manager Operations Console 被云平台抢走）
    ("monitor", [
        "云监控", "cloudmonitor", "cloud monitor",
        "应用实时监控服务", "application real-time monitoring service", "arms",
        "aiops",
        "专有云运维平台", "operations console",
    ]),
    # 4. 云平台
    ("cloud", [
        "统一云管平台", "uni-manager management console", "apsara uni-manager",
        "灾备", "容灾", "resilience", "backup and recovery", "cloud platform backup",
        "备份管理平台",
        "云迁移中心", "cloud migration hub", "server migration center",
        "data center as a service",
    ]),
    # 5. 计算
    ("compute", [
        "容器镜像服务", "container registry",
        "容器服务kubernetes", "container service for kubernetes", "kubernetes", "ack one", "openshift",
        "云服务器ecs", "云服务器 ecs", "elastic compute service",
        "弹性伸缩", "auto scaling",
        "资源编排", "resource orchestration service",
        "运维编排", "operation orchestration service",
        "裸金属", "裸机", "bare metal", "baremetal", "machine learning platform for ai",
        "terraform",
    ]),
    # 6. 存储
    ("storage", [
        "定义存储", "cloud defined storage",
        "对象存储", "object storage service",
        "日志服务", "log service",
        "表格存储", "tablestore",
        "文件存储", "file storage",
        "cpfs", "cloud parallel file storage",
        "apfs", "parallel file system",
        "efs", "elastic file system",
    ]),
    # 7. 网络
    ("network", [
        "负载均衡", "server load balancer", "application load balancer",
        "专有网络vpc", "virtual private cloud",
        "云接入网关", "cloud gateway",
        "dns",
        "高速通道", "express connect",
        "nat gateway", "nat网关",
        "vpn gateway", "vpn网关",
        "弹性公网ip", "elastic ip address",
        "转发路由器", "transitrouter",
        "ipv6 gateway", "ipv6网关",
    ]),
    # 8. 数据库
    ("database", [
        "polardb",
        "rds",
        "redis", "tair",
        "mongodb",
        "lindorm",
        "analyticdb", "云原生数据仓库",
        "time series and spatial-temporal",
        "数据管理", "data management", "dms",
        "数据传输", "data transmission service", "dts",
        "datahub", "数据总线",
        "数据库备份", "database backup",
        "secondary edition)",  # 文件名被截断的 PolarDB 主备版文档
    ]),
    # 9. 中间件
    ("middleware", [
        "消息队列", "message queue", "kafka", "rocketmq",
        "企业级分布式应用服务", "enterprise distributed application service", "edas",
        "schedulerx",
        "全局事务",
        "链路追踪", "tracing analysis",
        "prometheus", "可观测监控",
        "api 网关", "api gateway", "cloud-native gateway",
        "应用运维平台", "application operation platform", "application hybrid marketplace",
    ]),
    # 10. 大数据
    ("bigdata", [
        "maxcompute", "大数据计算",
        "dataworks", "大数据开发",
        "hologres", "交互式分析",
        "realtime compute", "flink", "实时计算",
        "elasticsearch", "检索分析",
        "大数据管家", "apsara big data manager",
    ]),
]


def normalize(name: str) -> str:
    """NFKC 规范化（统一全角/半角及 NBSP），转小写并压缩空白。"""
    s = unicodedata.normalize("NFKC", name).lower()
    s = s.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()


def classify(filename: str):
    n = normalize(filename)
    for key, keywords in RULES:
        for kw in keywords:
            if kw in n:
                return key, kw
    return None, None


def dirname_for(key, lang):
    pair = CATEGORIES.get(key, UNCATEGORIZED)
    return pair[0] if lang == "zh" else pair[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="仅预演，不移动文件")
    parser.add_argument("--apply", action="store_true", help="实际创建目录并移动文件")
    args = parser.parse_args()
    if not (args.dry_run or args.apply):
        parser.error("请指定 --dry-run 或 --apply")

    mapping = []
    stats = defaultdict(lambda: defaultdict(int))

    # 语言标签 -> 文档实际目录（docs/cn 中文、docs/en 英文）
    doc_dirs = {"Chinese": os.path.join("docs", "cn"), "English": os.path.join("docs", "en")}
    for folder, lang in (("Chinese", "zh"), ("English", "en")):
        root = os.path.join(BASE, doc_dirs[folder])
        if not os.path.isdir(root):
            print(f"[跳过] 目录不存在: {root}")
            continue
        for name in sorted(os.listdir(root)):
            src = os.path.join(root, name)
            if not os.path.isfile(src):
                continue
            key, kw = classify(name)
            target_dir = os.path.join(root, dirname_for(key, lang))
            dst = os.path.join(target_dir, name)
            mapping.append({
                "language": folder,
                "filename": name,
                "category_key": key or "",
                "category": dirname_for(key, lang),
                "matched_keyword": kw or "",
                "source": src,
                "destination": dst,
            })
            stats[folder][dirname_for(key, lang)] += 1

    # 输出统计
    print("=" * 60)
    print("分类预演统计" if args.dry_run else "分类执行结果")
    print("=" * 60)
    grand = 0
    for folder in ("Chinese", "English"):
        total = sum(stats[folder].values())
        grand += total
        print(f"\n【{folder}】共 {total} 个文件")
        for cat, cnt in sorted(stats[folder].items(), key=lambda x: (-x[1], x[0])):
            print(f"  {cat:<20} {cnt:>4}")
    print(f"\n总计: {grand} 个文件")

    # 未分类清单
    un = [m for m in mapping if not m["category_key"]]
    if un:
        print(f"\n[!] 未分类文件 {len(un)} 个:")
        for m in un:
            print(f"  - {m['filename']}")

    # 写出映射 CSV
    csv_path = os.path.join(BASE, "outputs", "classification_map.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "language", "filename", "category_key", "category",
            "matched_keyword", "source", "destination",
        ])
        writer.writeheader()
        writer.writerows(mapping)
    print(f"\n映射明细已写入: {csv_path}")

    if args.apply:
        moved = 0
        for m in mapping:
            os.makedirs(os.path.dirname(m["destination"]), exist_ok=True)
            if os.path.abspath(m["source"]) == os.path.abspath(m["destination"]):
                continue
            if os.path.exists(m["destination"]):
                print(f"[警告] 目标已存在，跳过: {m['destination']}")
                continue
            shutil.move(m["source"], m["destination"])
            moved += 1
        print(f"\n已移动 {moved} 个文件。")


if __name__ == "__main__":
    main()
