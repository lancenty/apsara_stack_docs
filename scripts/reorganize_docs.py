#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reorganize docs/cn/ and docs/en/ PDFs into a clean two-level hierarchy:
    docs/<lang>/<一级分类>/<二级产品>/<file>.pdf

Rules:
1. Primary source: uploaded console screenshot (10 categories, 39 products;
   overrides Help Center where they differ, e.g., 日志服务 SLS -> 存储,
   链路追踪 & Prometheus监控服务 -> 中间件).
2. Fallback source: Aliyun Apsara Stack Enterprise Help Center taxonomy
   (outputs/products_v_3_18_6_*.json & outputs/中文三版本PDF清单.csv) for
   products and categories absent from the screenshot.

Usage:
    python scripts/reorganize_docs.py --dry-run
    python scripts/reorganize_docs.py --apply
"""
from __future__ import annotations

import argparse
import csv
import os
import pathlib
import re
import shutil
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
ZH_MANIFEST_CSV = ROOT / "outputs" / "中文三版本PDF清单.csv"
PLAN_CSV = ROOT / "outputs" / "reorganize_plan.csv"

# 12 canonical categories: key -> (CN folder name, EN folder name)
CATEGORIES: dict[str, tuple[str, str]] = {
    "cloud": ("云平台", "Cloud Platform"),
    "compute": ("计算", "Compute"),
    "storage": ("存储", "Storage"),
    "network": ("网络", "Networking"),
    "database": ("数据库", "Database"),
    "middleware": ("中间件", "Middleware"),
    "bigdata": ("大数据", "Big Data"),
    "security": ("安全", "Security"),
    "monitor": ("监控与运维服务", "Monitoring and Ops"),
    "opentrek": ("OpenTrek", "OpenTrek"),
    "delivery": ("交付服务", "Delivery Services"),
    "other": ("其他", "Other"),
}

# Canonical product registry: code -> (category_key, cn_product_dir, en_product_dir, basis)
PRODUCTS: dict[str, tuple[str, str, str, str]] = {
    # 1. 云平台 / Cloud Platform
    "apsara_stack_platform": ("cloud", "统一云管平台", "Apsara Uni-manager", "screenshot+helpcenter"),
    "asr": ("cloud", "灾备管理平台", "Disaster Recovery Platform", "screenshot+helpcenter"),
    "apsarabase": ("cloud", "全栈云平台", "Apsara Base", "helpcenter"),
    "apds": ("cloud", "云迁移中心", "Cloud Migration Hub", "helpcenter"),
    # 2. 计算 / Compute
    "acr": ("compute", "容器镜像服务 ACR", "Container Registry", "screenshot"),
    "csk": ("compute", "容器服务 Kubernetes", "Container Service for Kubernetes", "screenshot"),
    "ecs": ("compute", "云服务器 ECS", "Elastic Compute Service", "screenshot"),
    "ess": ("compute", "弹性伸缩", "Auto Scaling", "screenshot"),
    "ros": ("compute", "资源编排 ROS", "Resource Orchestration Service", "screenshot"),
    "oos": ("compute", "运维编排 OOS", "Operation Orchestration Service", "screenshot"),
    "alinux": ("compute", "Alibaba Cloud Linux", "Alibaba Cloud Linux", "helpcenter"),
    "ecsgpu": ("compute", "GPU云服务器", "GPU Elastic Compute Service", "helpcenter"),
    "ehpc": ("compute", "弹性高性能计算", "Elastic High Performance Computing", "helpcenter"),
    "dcaas": ("compute", "裸机管理 BMS", "BareMetal Management Service", "helpcenter"),
    # 3. 存储 / Storage
    "hcs_hgw": ("storage", "云定义存储", "Cloud Defined Storage", "screenshot+helpcenter"),
    "oss": ("storage", "对象存储 OSS", "Object Storage Service", "screenshot"),
    "sls": ("storage", "日志服务 SLS", "Log Service", "screenshot"),
    "ots": ("storage", "表格存储 Tablestore", "Tablestore", "screenshot"),
    "nas": ("storage", "文件存储 NAS", "File Storage NAS", "helpcenter"),
    # 4. 网络 / Networking
    "slb": ("network", "负载均衡 SLB", "Server Load Balancer", "screenshot"),
    "vpc": ("network", "专有网络 VPC", "Virtual Private Cloud", "screenshot"),
    "cgw": ("network", "云接入网关", "Cloud Gateway", "screenshot"),
    "apsara_stack_dns": ("network", "专有云DNS", "Apsara Stack DNS", "screenshot"),
    "expressconnect": ("network", "高速通道", "Express Connect", "screenshot"),
    "ntr": ("network", "转发路由器", "TransitRouter", "helpcenter"),
    "vpn": ("network", "VPN网关", "VPN Gateway", "helpcenter"),
    "eip": ("network", "弹性公网IP", "Elastic IP Address", "helpcenter"),
    "nat": ("network", "NAT网关", "NAT Gateway", "helpcenter"),
    "ipv6": ("network", "IPv6网关", "IPv6 Gateway", "helpcenter"),
    # 5. 数据库 / Database
    "polardb": ("database", "云原生关系型数据库 PolarDB", "ApsaraDB for POLARDB", "screenshot"),
    "rds": ("database", "云数据库 RDS", "ApsaraDB for RDS", "screenshot"),
    "kvstore": ("database", "云数据库 Redis", "ApsaraDB for Redis", "screenshot"),
    "dms": ("database", "数据管理 DMS", "Data Management", "screenshot"),
    "dts": ("database", "数据传输服务 DTS", "Data Transmission Service", "screenshot"),
    "mongodb": ("database", "云数据库 MongoDB", "ApsaraDB for MongoDB", "screenshot"),
    "hdm": ("database", "数据库自治服务", "Database Autonomy Service", "screenshot"),
    "adb": ("database", "云原生数据仓库 AnalyticDB", "AnalyticDB", "helpcenter"),
    "cbs": ("database", "数据库备份 DBS", "Database Backup", "helpcenter"),
    "hitsdb": ("database", "云原生多模数据库 Lindorm", "Lindorm", "helpcenter"),
    "oceanbase": ("database", "云数据库 OceanBase", "ApsaraDB for OceanBase", "helpcenter"),
    # 6. 中间件 / Middleware
    "rocketmq": ("middleware", "消息队列 MQ", "Alibaba Cloud Message Queue", "screenshot"),
    "edas": ("middleware", "企业级分布式应用服务 EDAS", "Enterprise Distributed Application Service", "screenshot"),
    "txc": ("middleware", "全局事务服务", "Global Transaction Service", "screenshot"),
    "xtrace": ("middleware", "链路追踪", "Tracing Analysis", "screenshot"),
    "prometheus": ("middleware", "Prometheus监控服务", "Prometheus Service", "screenshot"),
    "apigateway": ("middleware", "API 网关", "API Gateway", "screenshot"),
    "alikafka": ("middleware", "消息队列 Kafka版", "Message Queue for Apache Kafka", "helpcenter"),
    "msha": ("middleware", "多活容灾 MSHA", "Multi-Site High Availability", "helpcenter"),
    "csb": ("middleware", "云服务总线 CSB", "Cloud Service Bus", "helpcenter"),
    "ahas": ("middleware", "应用高可用服务", "Application High Availability Service", "helpcenter"),
    # 7. 大数据 / Big Data
    "odps": ("bigdata", "大数据计算 MaxCompute", "MaxCompute", "screenshot"),
    "dide": ("bigdata", "大数据开发治理平台 DataWorks", "DataWorks", "screenshot"),
    "hologram": ("bigdata", "交互式分析 Hologres", "Hologres", "screenshot"),
    "bcc": ("bigdata", "大数据管家", "Apsara Big Data Manager", "helpcenter"),
    "sc": ("bigdata", "实时计算（流计算）", "Realtime Compute for Apache Flink", "helpcenter"),
    "datahub": ("bigdata", "数据总线 DataHub", "DataHub", "helpcenter"),
    "elasticsearch": ("bigdata", "检索分析服务 Elasticsearch", "Elasticsearch", "helpcenter"),
    "learn": ("bigdata", "机器学习", "Machine Learning Platform for AI", "helpcenter"),
    "dataphin": ("bigdata", "智能数据构建与管理 Dataphin", "Dataphin", "helpcenter"),
    "drp": ("bigdata", "数据资源平台 DataQ", "DataQ", "helpcenter"),
    "datav": ("bigdata", "DataV数据可视化", "DataV", "helpcenter"),
    "quickbi": ("bigdata", "Quick BI", "Quick BI", "helpcenter"),
    # 8. 安全 / Security
    "kms": ("security", "密钥管理服务 KMS", "Key Management Service", "screenshot"),
    "beaver": ("security", "网络流量检测与响应", "Network Detection and Response", "screenshot"),
    "aegis": ("security", "云安全中心（安骑士）", "Cloud Security Center (Server Guard)", "screenshot"),
    "bastionhost": ("security", "堡垒机", "Bastionhost", "screenshot"),
    "sas": ("security", "云安全管理中心", "Cloud Security Management Center", "screenshot"),
    "sddp": ("security", "敏感数据保护", "Sensitive Data Discovery and Protection", "screenshot"),
    "dbaudit": ("security", "数据库审计", "Database Security Audit", "screenshot"),
    "ddos": ("security", "DDoS防护", "Anti-DDoS", "screenshot"),
    "idaas": ("security", "应用身份服务", "IDaaS", "screenshot"),
    "cas": ("security", "SSL证书（CA证书服务、数据安全）", "SSL Certificates Service", "helpcenter"),
    "waf": ("security", "Web应用防火墙", "Web Application Firewall", "helpcenter"),
    "cloudfw": ("security", "云防火墙", "Cloud Security Firewall", "helpcenter"),
    "yundun": ("security", "云盾", "Apsara Stack Security", "helpcenter"),
    "lvwang": ("security", "内容安全", "Content Moderation", "helpcenter"),
    "hsm": ("security", "加密服务", "Hardware Security Module", "helpcenter"),
    # 9. 监控与运维服务 / Monitoring and Ops
    "cms": ("monitor", "云监控", "CloudMonitor", "screenshot"),
    "aso": ("monitor", "专有云运维平台", "Apsara Stack Operation", "helpcenter"),
    "asm": ("monitor", "应用运维平台", "Application Operation Platform", "helpcenter"),
    "arms": ("monitor", "应用实时监控服务 ARMS", "Application Real-time Monitoring Service", "helpcenter"),
    "tongque": ("monitor", "SRE技术保障平台", "SRE Platform", "helpcenter"),
    "tianji": ("monitor", "飞天基础运维平台", "Apsara Infrastructure Management Framework", "helpcenter"),
    # 10. OpenTrek
    "opentrek": ("opentrek", "智能体工厂 OpenTrek", "OpenTrek", "screenshot+helpcenter"),
    # 11. 交付服务
    "asdelivery": ("delivery", "专有云部署服务", "Apsara Stack Delivery", "helpcenter"),
    # 12. 其他
    "appstreaming": ("other", "无影", "Wuying", "helpcenter"),
}

# Ordered fallback rules for EN files and legacy CN files not in 中文三版本PDF清单.csv.
# Order is critical to avoid substring collisions!
FALLBACK_RULES: list[tuple[str, list[str]]] = [
    # 1. Operations Console / AIOps BEFORE Uni-manager
    ("aso", ["运维控制台", "专有云运维平台", "operations console", "apsara stack operation", "aiops"]),
    ("apsara_stack_platform", ["飞天助理", "copilot", "统一云管平台", "uni-manager"]),
    # 2. OpenTrek BEFORE API Gateway (AI Gateway vs API Gateway)
    ("opentrek", ["opentrek", "ai 网关", "ai gateway", "ai studio", "agentruntime"]),
    # 3. Security: specific products BEFORE generic 云盾 and BEFORE 容器服务
    ("aegis", ["容器安全", "container security", "安骑士", "server guard"]),
    ("sas", [
        "云安全管理中心", "cloud security management center",
        "态势感知", "situation awareness",
        "漏洞扫描", "cloud security scanner",
        "安全编排", "soar", "security orchestration",
    ]),
    ("dbaudit", ["数据库审计", "database security audit", "database audit", "静态数据脱敏", "static data masking"]),
    ("waf", ["web应用防火墙", "web application firewall", "waf"]),
    ("cloudfw", ["云防火墙", "cloud security firewall", "nfv cloud firewall"]),
    ("bastionhost", ["堡垒机", "bastionhost"]),
    ("beaver", ["网络检测与响应", "网络流量检测与响应", "network detection and response"]),
    ("kms", ["密钥管理", "key management service", "kms"]),
    ("idaas", ["应用身份服务", "idaas"]),
    ("ddos", ["ddos"]),
    ("cas", ["ssl证书", "数字证书管理"]),
    ("lvwang", ["内容安全", "ai安全护栏"]),
    ("sddp", ["敏感数据保护"]),
    ("hsm", ["加密服务"]),
    ("yundun", ["apsara stack security", "云盾"]),
    # 4. Bare Metal Computing Platform (MLPAI) BEFORE BareMetal Management Service
    ("learn", ["裸金属算力平台", "bare metal computing platform", "machine learning platform for ai", "机器学习", "人工智能平台pai"]),
    ("dcaas", ["data center as a service", "裸机管理", "baremetal", "bare metal", "专有云弹性数据中心"]),
    # 5. Monitoring & Middleware observability
    ("asm", ["应用运维平台", "application operation platform", "application hybrid marketplace"]),
    ("arms", ["应用实时监控服务", "application real-time monitoring service", "arms"]),
    ("cms", ["云监控", "cloudmonitor"]),
    ("prometheus", ["prometheus", "可观测监控"]),
    ("xtrace", ["链路追踪", "tracing analysis"]),
    # 6. Database: RDS BEFORE PolarDB (so RDS for PolarDB stays in rds); OceanBase BEFORE Log Service
    ("adb", ["云原生数据仓库", "analyticdb"]),
    ("rds", ["云数据库rds", "云数据库 rds", "apsaradb for rds", "apsaradb rds"]),
    ("polardb", ["polardb", "secondary edition)"]),
    ("oceanbase", ["oceanbase"]),
    ("mongodb", ["mongodb"]),
    ("kvstore", ["redis", "tair"]),
    ("hitsdb", ["lindorm", "time series and spatial-temporal"]),
    ("cbs", ["数据库备份", "database backup"]),
    ("dts", ["数据传输", "data transmission service", "dts"]),
    ("dms", ["数据管理", "data management", "dms"]),
    ("hdm", ["数据库自治服务"]),
    ("datahub", ["datahub", "数据总线"]),
    # 7. Cloud Platform
    ("asr", ["备份管理平台", "backup and recovery", "cloud platform backup", "灾备", "容灾", "resilience"]),
    ("apds", ["云迁移中心", "cloud migration hub", "server migration center"]),
    ("apsarabase", ["专有云基础服务", "全栈云平台", "云平台 专有云license", "云平台 多region", "云平台 数据中心机房"]),
    # 8. Storage: CDS sub-products BEFORE generic File Storage NAS
    ("hcs_hgw", [
        "弹性文件存储", "elastic file system nas",
        "cpfs", "cloud parallel file storage",
        "apfs", "parallel file system",
        "定义存储", "cloud defined storage",
        "混合云存储cds",
    ]),
    ("nas", ["文件存储", "file storage nas"]),
    ("oss", ["对象存储", "object storage service"]),
    ("sls", ["日志服务", "log service"]),
    ("ots", ["表格存储", "tablestore"]),
    # 9. Compute
    ("acr", ["容器镜像服务", "container registry"]),
    ("csk", ["容器服务", "kubernetes", "ack one", "openshift"]),
    ("ecs", ["云服务器", "elastic compute service"]),
    ("ess", ["弹性伸缩", "auto scaling"]),
    ("ros", ["资源编排", "resource orchestration service", "terraform"]),
    ("oos", ["运维编排", "operation orchestration service"]),
    ("alinux", ["alibaba cloud linux"]),
    ("ecsgpu", ["gpu云服务器"]),
    ("ehpc", ["弹性高性能计算"]),
    # 10. Middleware: Kafka BEFORE generic Message Queue
    ("alikafka", ["消息队列kafka", "kafka"]),
    ("rocketmq", ["消息队列", "message queue", "rocketmq"]),
    ("edas", ["schedulerx", "企业级分布式应用服务", "enterprise distributed application service", "edas"]),
    ("apigateway", ["api 网关", "api gateway", "cloud-native gateway"]),
    ("txc", ["全局事务"]),
    ("msha", ["多活容灾", "异地多活", "msha"]),
    ("csb", ["云服务总线", "csb"]),
    ("ahas", ["应用高可用服务"]),
    # 11. Networking
    ("ipv6", ["ipv6网关", "ipv6 gateway"]),
    ("nat", ["nat网关", "nat gateway"]),
    ("vpn", ["vpn网关", "vpn gateway"]),
    ("eip", ["弹性公网ip", "elastic ip address"]),
    ("ntr", ["转发路由器", "transitrouter"]),
    ("expressconnect", ["高速通道", "express connect"]),
    ("cgw", ["云接入网关", "cloud gateway"]),
    ("vpc", ["专有网络", "virtual private cloud"]),
    ("slb", ["负载均衡", "server load balancer", "application load balancer"]),
    ("apsara_stack_dns", ["dns"]),
    # 12. Big Data
    ("sc", ["realtime compute", "flink", "实时计算"]),
    ("elasticsearch", ["elasticsearch", "检索分析"]),
    ("bcc", ["大数据管家", "apsara big data manager"]),
    ("dide", ["dataworks", "大数据开发"]),
    ("odps", ["maxcompute", "大数据计算"]),
    ("hologram", ["hologres", "交互式分析"]),
    ("dataphin", ["dataphin"]),
    ("drp", ["dataq", "数据资源平台"]),
    ("datav", ["datav"]),
    ("quickbi", ["quick bi"]),
    # 13. Other / Delivery / Monitor
    ("tongque", ["sre技术保障平台"]),
    ("tianji", ["飞天基础运维平台"]),
    ("asdelivery", ["专有云部署服务"]),
    ("appstreaming", ["无影"]),
]


def normalize_name(name: str) -> str:
    s = unicodedata.normalize("NFKC", name).replace("\u00a0", " ").lower()
    return re.sub(r"\s+", " ", s).strip()


def win_long_path(path: pathlib.Path) -> str:
    abs_path = os.path.abspath(str(path))
    if os.name == "nt" and not abs_path.startswith("\\\\?\\"):
        if abs_path.startswith("\\\\"):
            return "\\\\?\\UNC\\" + abs_path[2:]
        return "\\\\?\\" + abs_path
    return abs_path


def load_zh_manifest_codes(csv_path: pathlib.Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing manifest CSV: {csv_path}")
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            fn = row["file"]
            code = row["code"]
            if fn in mapping and mapping[fn] != code:
                raise ValueError(f"Conflicting codes for {fn}: {mapping[fn]} vs {code}")
            mapping[fn] = code
    return mapping


def resolve_code(lang: str, filename: str, zh_manifest_codes: dict[str, str]) -> tuple[str | None, str, str]:
    if lang == "cn" and filename in zh_manifest_codes:
        return zh_manifest_codes[filename], "manifest", filename
    n = normalize_name(filename)
    for code, keywords in FALLBACK_RULES:
        for kw in keywords:
            if kw in n:
                return code, "keyword", kw
    return None, "", ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Reorganize docs/cn and docs/en PDFs.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview changes without moving files (default)")
    mode.add_argument("--apply", action="store_true", help="Apply file moves and prune empty directories")
    args = parser.parse_args()
    apply_changes = bool(args.apply)

    zh_manifest_codes = load_zh_manifest_codes(ZH_MANIFEST_CSV)

    plan_rows: list[dict[str, str]] = []
    unclassified: list[tuple[str, pathlib.Path]] = []
    dest_seen: dict[pathlib.Path, pathlib.Path] = {}
    collisions: list[tuple[pathlib.Path, pathlib.Path, pathlib.Path]] = []

    stats: dict[str, dict[str, dict[str, int]]] = {
        "cn": defaultdict(lambda: defaultdict(int)),
        "en": defaultdict(lambda: defaultdict(int)),
    }

    for lang in ("cn", "en"):
        lang_root = DOCS_DIR / lang
        if not lang_root.is_dir():
            print(f"[ERROR] Missing directory: {lang_root}", file=sys.stderr)
            return 2
        pdfs = sorted(lang_root.rglob("*.pdf"))
        for src in pdfs:
            code, match_source, matched_key = resolve_code(lang, src.name, zh_manifest_codes)
            if code is None or code not in PRODUCTS:
                unclassified.append((lang, src))
                continue
            cat_key, cn_prod, en_prod, basis = PRODUCTS[code]
            cn_cat, en_cat = CATEGORIES[cat_key]
            target_cat = cn_cat if lang == "cn" else en_cat
            target_prod = cn_prod if lang == "cn" else en_prod
            dst = lang_root / target_cat / target_prod / src.name

            if dst in dest_seen:
                collisions.append((dst, dest_seen[dst], src))
            dest_seen[dst] = src

            src_rel = str(src.relative_to(DOCS_DIR)).replace("\\", "/")
            dst_rel = str(dst.relative_to(DOCS_DIR)).replace("\\", "/")
            changed = "YES" if src != dst else "NO"

            plan_rows.append({
                "language": lang,
                "code": code,
                "basis": basis,
                "match_source": match_source,
                "matched_key": matched_key,
                "target_category": target_cat,
                "target_product": target_prod,
                "filename": src.name,
                "changed": changed,
                "source_rel": src_rel,
                "dest_rel": dst_rel,
            })
            stats[lang][target_cat][target_prod] += 1

    PLAN_CSV.parent.mkdir(parents=True, exist_ok=True)
    with PLAN_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "language",
                "code",
                "basis",
                "match_source",
                "matched_key",
                "target_category",
                "target_product",
                "filename",
                "changed",
                "source_rel",
                "dest_rel",
            ],
        )
        writer.writeheader()
        writer.writerows(plan_rows)

    total_cn = sum(sum(prods.values()) for prods in stats["cn"].values())
    total_en = sum(sum(prods.values()) for prods in stats["en"].values())
    changed_count = sum(1 for r in plan_rows if r["changed"] == "YES")

    print("=" * 72)
    print("REORGANIZE PLAN SUMMARY" if not apply_changes else "REORGANIZE EXECUTION SUMMARY")
    print("=" * 72)
    print(f"Total scanned: {total_cn + total_en} (cn: {total_cn}, en: {total_en})")
    print(f"Unclassified:  {len(unclassified)}")
    print(f"Collisions:    {len(collisions)}")
    print(f"Moves needed:  {changed_count}")
    print(f"Plan CSV:      {PLAN_CSV}")

    for lang in ("cn", "en"):
        lang_total = sum(sum(prods.values()) for prods in stats[lang].values())
        cat_count = len(stats[lang])
        prod_count = sum(len(prods) for prods in stats[lang].values())
        print(f"\n[{lang.upper()}] {lang_total} files across {cat_count} categories / {prod_count} products")
        for cat, prods in sorted(stats[lang].items(), key=lambda x: (-sum(x[1].values()), x[0])):
            print(f"  - {cat} ({sum(prods.values())})")
            for prod, cnt in sorted(prods.items(), key=lambda x: (-x[1], x[0])):
                print(f"      {prod:<42} {cnt:>4}")

    if unclassified:
        print("\n[ERROR] Unclassified files detected:", file=sys.stderr)
        for lang, p in unclassified:
            print(f"  [{lang}] {p}", file=sys.stderr)
        return 1

    if collisions:
        print("\n[ERROR] Destination collisions detected:", file=sys.stderr)
        for dst, a, b in collisions:
            print(f"  {dst} <- {a} AND {b}", file=sys.stderr)
        return 1

    if not apply_changes:
        print("\n[DRY-RUN] No files were modified. Pass --apply to execute.")
        return 0

    moved = 0
    for row in plan_rows:
        if row["changed"] != "YES":
            continue
        src = DOCS_DIR / pathlib.PurePosixPath(row["source_rel"])
        dst = DOCS_DIR / pathlib.PurePosixPath(row["dest_rel"])
        os.makedirs(win_long_path(dst.parent), exist_ok=True)
        if os.path.exists(win_long_path(dst)):
            raise FileExistsError(f"Destination already exists: {dst}")
        shutil.move(win_long_path(src), win_long_path(dst))
        moved += 1

    # Prune empty directories bottom-up under docs/cn and docs/en
    removed_dirs = 0
    for lang in ("cn", "en"):
        lang_root = DOCS_DIR / lang
        dirs = sorted(
            [p for p in lang_root.rglob("*") if p.is_dir()],
            key=lambda p: len(p.parts),
            reverse=True,
        )
        for d in dirs:
            lp = win_long_path(d)
            if not os.listdir(lp):
                os.rmdir(lp)
                removed_dirs += 1

    print(f"\n[APPLIED] Moved {moved} files, removed {removed_dirs} empty directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
