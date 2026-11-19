#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二级分类：在每个一级分类目录下，按具体产品建立二级子目录并移动文件。

图中每个一级分类下列出的二级产品优先采用图中名称；
图中未列出的产品，按文件名中的实际产品名建立二级目录。

用法:
    python classify_docs_v2.py --dry-run
    python classify_docs_v2.py --apply
"""

import argparse
import csv
import os
import re
import shutil
import unicodedata
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 一级目录名 -> 规则 key
DIR_TO_KEY = {
    "云平台": "cloud", "计算": "compute", "存储": "storage", "网络": "network",
    "数据库": "database", "中间件": "middleware", "大数据": "bigdata",
    "安全": "security", "监控与运维服务": "monitor", "OpenTrek": "opentrek",
    "Cloud Platform": "cloud", "Compute": "compute", "Storage": "storage",
    "Networking": "network", "Database": "database", "Middleware": "middleware",
    "Big Data": "bigdata", "Security": "security",
    "Monitoring and Ops": "monitor", "OpenTrek_en": "opentrek",
}
# key -> 中文二级名映射中用于英文目录的后缀判断（见规则元组本身）
OTHER = ("其他产品", "Other Products")

# 产品规则: key -> [(中文二级名, 英文二级名, [关键词...]), ...]
# 顺序即优先级，越具体越靠前。
PRODUCT_RULES = {
    "cloud": [
        ("备份管理平台", "Backup Management Platform", ["备份管理平台", "backup and recovery", "cloud platform backup", "云平台备份"]),
        ("云迁移中心", "Cloud Migration Hub", ["云迁移中心", "cloud migration hub", "server migration center"]),
        ("数据中心即服务", "Data Center as a Service", ["data center as a service"]),
        ("灾备管理中心", "Disaster Recovery Center", ["灾备管理中心", "灾备", "容灾", "resilience", "asr", "geo-disaster", "zone-disaster"]),
        ("统一云管平台", "Apsara Uni-manager", ["统一云管平台", "uni-manager", "management console"]),
    ],
    "compute": [
        ("容器服务 Kubernetes", "Container Service for Kubernetes", ["容器服务kubernetes", "container service for kubernetes", "kubernetes", "ack one", "openshift"]),
        ("容器镜像服务 ACR", "Container Registry", ["容器镜像服务", "container registry"]),
        ("云服务器 ECS", "Elastic Compute Service", ["云服务器ecs", "云服务器 ecs", "elastic compute service"]),
        ("弹性伸缩", "Auto Scaling", ["弹性伸缩", "auto scaling"]),
        ("资源编排 ROS", "Resource Orchestration Service", ["资源编排", "resource orchestration service", "terraform"]),
        ("运维编排 OOS", "Operation Orchestration Service", ["运维编排", "operation orchestration service"]),
        ("裸金属算力平台", "Bare Metal Computing Platform", ["裸金属算力平台", "bare metal computing platform", "machine learning platform for ai"]),
        ("裸机管理服务", "BareMetal Management Service", ["裸机管理服务", "baremetal"]),
    ],
    "storage": [
        ("高性能并行文件存储 APFS", "ApsaraStack Parallel File System", ["apfs", "parallel file system"]),
        ("文件存储 CPFS", "Cloud Parallel File Storage", ["cpfs", "cloud parallel file storage"]),
        ("弹性文件存储 EFS-NAS", "Elastic File System NAS", ["efs-nas", "elastic file system nas", "阿里云弹性文件存储"]),
        ("文件存储 NAS", "File Storage NAS", ["文件存储nas", "file storage nas", "apsara file storage nas"]),
        ("对象存储 OSS", "Object Storage Service", ["对象存储", "object storage service"]),
        ("日志服务 SLS", "Log Service", ["日志服务", "log service"]),
        ("表格存储 Tablestore", "Tablestore", ["表格存储", "tablestore"]),
        ("云定义存储", "Cloud Defined Storage", ["定义存储", "cloud defined storage"]),
    ],
    "network": [
        ("IPv6网关", "IPv6 Gateway", ["ipv6网关", "ipv6 gateway"]),
        ("NAT网关", "NAT Gateway", ["nat网关", "nat gateway"]),
        ("VPN网关", "VPN Gateway", ["vpn网关", "vpn gateway"]),
        ("弹性公网IP", "Elastic IP Address", ["弹性公网ip", "elastic ip address"]),
        ("转发路由器", "TransitRouter", ["转发路由器", "transitrouter"]),
        ("高速通道", "Express Connect", ["高速通道", "express connect"]),
        ("专有云DNS", "Apsara Stack DNS", ["dns"]),
        ("云接入网关", "Cloud Gateway", ["云接入网关", "cloud gateway"]),
        ("专有网络 VPC", "Virtual Private Cloud", ["专有网络vpc", "virtual private cloud"]),
        ("负载均衡 SLB", "Server Load Balancer", ["负载均衡", "server load balancer", "application load balancer"]),
    ],
    "database": [
        ("云原生数据仓库 AnalyticDB", "AnalyticDB", ["analyticdb", "云原生数据仓库"]),
        ("云原生多模数据库 Lindorm", "Lindorm", ["lindorm"]),
        ("时序时空数据库", "Time Series and Spatial-Temporal Database", ["time series and spatial-temporal"]),
        ("数据总线 DataHub", "DataHub", ["datahub", "数据总线"]),
        ("数据库备份", "Database Backup", ["数据库备份", "database backup"]),
        ("数据传输服务 DTS", "Data Transmission Service", ["数据传输", "data transmission service", "dts"]),
        ("数据管理 DMS", "Data Management", ["数据管理", "data management", "dms"]),
        ("云数据库 MongoDB", "ApsaraDB for MongoDB", ["mongodb"]),
        ("云数据库 Redis", "ApsaraDB for Redis", ["redis", "tair"]),
        ("云数据库 RDS", "ApsaraDB for RDS", ["rds"]),
        ("云原生关系型数据库 PolarDB", "ApsaraDB for POLARDB", ["polardb", "secondary edition)"]),
    ],
    "middleware": [
        ("SchedulerX 2.0", "SchedulerX 2.0", ["schedulerx"]),
        ("消息队列 Kafka版", "Message Queue for Apache Kafka", ["消息队列kafka", "kafka"]),
        ("消息队列 MQ", "Alibaba Cloud Message Queue", ["消息队列", "message queue", "rocketmq"]),
        ("链路追踪", "Tracing Analysis", ["链路追踪", "tracing analysis"]),
        ("Prometheus 监控服务", "Prometheus Service", ["prometheus", "可观测监控"]),
        ("API 网关", "API Gateway", ["api 网关", "api gateway"]),
        ("云原生网关", "Cloud-native Gateway", ["cloud-native gateway"]),
        ("应用市场", "Application Hybrid Marketplace", ["application hybrid marketplace"]),
        ("应用运维平台", "Application Operation Platform", ["应用运维平台", "application operation platform"]),
        ("企业级分布式应用服务 EDAS", "Enterprise Distributed Application Service", ["企业级分布式应用服务", "enterprise distributed application service", "edas"]),
    ],
    "bigdata": [
        ("实时计算 Flink", "Realtime Compute for Apache Flink", ["realtime compute", "flink", "实时计算"]),
        ("检索分析服务 Elasticsearch", "Elasticsearch", ["elasticsearch", "检索分析"]),
        ("大数据管家", "Apsara Big Data Manager", ["大数据管家", "apsara big data manager"]),
        ("大数据开发治理平台 DataWorks", "DataWorks", ["dataworks", "大数据开发"]),
        ("大数据计算 MaxCompute", "MaxCompute", ["maxcompute", "大数据计算"]),
    ],
    "security": [
        ("容器安全", "Container Security Service", ["容器安全", "container security service"]),
        ("云安全中心（态势感知）", "Cloud Security Management Center", ["态势感知", "situation awareness", "云安全管理中心", "cloud security management center", "漏洞扫描", "cloud security scanner", "安全编排", "security orchestration automation and response", "soar"]),
        ("Web应用防火墙", "Web Application Firewall", ["web应用防火墙", "web application firewall", "waf"]),
        ("云防火墙", "Cloud Security Firewall", ["云防火墙", "cloud security firewall", "nfv cloud firewall"]),
        ("堡垒机", "Bastionhost", ["堡垒机", "bastionhost"]),
        ("数据库审计", "Database Security Audit", ["数据库审计", "database security audit"]),
        ("静态数据脱敏", "Static Data Masking and Watermarking", ["静态数据脱敏", "static data masking"]),
        ("应用身份服务 IDaaS", "IDaaS", ["应用身份服务", "idaas"]),
        ("网络流量检测与响应", "Network Detection and Response", ["网络检测与响应", "network detection and response"]),
        ("密钥管理服务 KMS", "Key Management Service", ["密钥管理", "key management service", "kms"]),
        ("安骑士", "Server Guard Advanced Edition", ["安骑士", "server guard"]),
        ("云盾", "Apsara Stack Security", ["云盾", "apsara stack security", "security administrator"]),
    ],
    "monitor": [
        ("应用实时监控服务 ARMS", "Application Real-time Monitoring Service", ["arms", "应用实时监控服务", "application real-time monitoring service"]),
        ("Apsara AIOps", "Apsara AIOps", ["aiops"]),
        ("专有云运维平台", "Apsara Uni-manager Operations Console", ["专有云运维平台", "operations console"]),
        ("云监控", "CloudMonitor", ["云监控", "cloudmonitor"]),
    ],
    "opentrek": [
        ("OpenTrek Dev", "OpenTrek Dev", ["opentrek dev"]),
        ("OpenTrek Ops", "OpenTrek Ops", ["opentrek-ops", "opentrek ops"]),
        ("OpenTrek AI Gateway", "OpenTrek AI Gateway", ["ai 网关", "ai gateway"]),
        ("OpenTrek AI Studio", "OpenTrek AI Studio", ["ai studio"]),
        ("OpenTrek AgentRuntime", "OpenTrek AgentRuntime", ["agentruntime"]),
        ("Apsara Copilot", "Apsara Copilot", ["copilot"]),
        ("飞天助理", "Feitian Assistant", ["飞天助理"]),
    ],
}


def normalize(name: str) -> str:
    s = unicodedata.normalize("NFKC", name).lower()
    s = s.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()


def match_product(key, filename):
    n = normalize(filename)
    for zh, en, kws in PRODUCT_RULES.get(key, []):
        for kw in kws:
            if kw in n:
                return zh, en, kw
    return OTHER[0], OTHER[1], ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not (args.dry_run or args.apply):
        parser.error("请指定 --dry-run 或 --apply")

    mapping = []
    stats = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    # 语言标签 -> 文档实际目录（docs/cn 中文、docs/en 英文）
    doc_dirs = {"Chinese": os.path.join("docs", "cn"), "English": os.path.join("docs", "en")}
    for folder, lang in (("Chinese", "zh"), ("English", "en")):
        root = os.path.join(BASE, doc_dirs[folder])
        for first in sorted(os.listdir(root)):
            first_path = os.path.join(root, first)
            if not os.path.isdir(first_path):
                continue
            key = DIR_TO_KEY.get(first)
            if key is None:
                print(f"[警告] 未知一级目录: {first}")
                continue
            for name in sorted(os.listdir(first_path)):
                src = os.path.join(first_path, name)
                if not os.path.isfile(src):
                    continue
                zh, en, kw = match_product(key, name)
                second = zh if lang == "zh" else en
                dst = os.path.join(first_path, second, name)
                mapping.append({
                    "language": folder, "first": first, "second": second,
                    "filename": name, "matched_keyword": kw,
                    "source": src, "destination": dst,
                })
                stats[folder][first][second] += 1

    print("=" * 70)
    print("二级分类预演" if args.dry_run else "二级分类执行结果")
    print("=" * 70)
    for folder in ("Chinese", "English"):
        total = sum(sum(v.values()) for v in stats[folder].values())
        print(f"\n【{folder}】共 {total} 个文件")
        for first, seconds in sorted(stats[folder].items()):
            print(f"  ▼ {first} ({sum(seconds.values())})")
            for sec, cnt in sorted(seconds.items(), key=lambda x: (-x[1], x[0])):
                print(f"      {sec:<38} {cnt:>3}")

    other = [m for m in mapping if m["second"] in (OTHER[0], OTHER[1])]
    if other:
        print(f"\n[!] 未匹配到具体产品 {len(other)} 个:")
        for m in other:
            print(f"  - [{m['first']}] {m['filename']}")

    csv_path = os.path.join(BASE, "outputs", "classification_map_v2.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=[
            "language", "first", "second", "filename", "matched_keyword", "source", "destination",
        ])
        w.writeheader()
        w.writerows(mapping)
    print(f"\n映射明细已写入: {csv_path}")

    if args.apply:
        moved = 0
        for m in mapping:
            dst_dir = os.path.dirname(m["destination"])
            os.makedirs(dst_dir, exist_ok=True)
            if os.path.exists(m["destination"]):
                print(f"[警告] 目标已存在，跳过: {m['destination']}")
                continue
            src, dst = m["source"], m["destination"]
            # Windows 下启用长路径支持（>260 字符）
            if os.name == "nt":
                src = "\\\\?\\" + os.path.abspath(src)
                dst = "\\\\?\\" + os.path.abspath(dst)
            shutil.move(src, dst)
            moved += 1
        print(f"\n已移动 {moved} 个文件。")


if __name__ == "__main__":
    main()
