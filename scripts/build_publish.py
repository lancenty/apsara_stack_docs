"""Build the curated `publish/` directory from read-only `downloads/` sources.

Copies and extracts whitelisted Apsara Stack 3.18.6 and legacy PDFs into
`publish/zh` and `publish/en` using 11 pure-name categories (Option A) and
writes an audit manifest to `reports/publish_manifest.csv`.
"""

from __future__ import annotations

import csv
import hashlib
import os
import pathlib
import re
import zipfile
from typing import Iterable

WORKSPACE_ROOT = pathlib.Path(r"C:\Users\Lancent\Documents\Workspace\apsara_stack_docs")
DOWNLOADS_ROOT = WORKSPACE_ROOT / "downloads"
ZH_ROOT = DOWNLOADS_ROOT / "zh_all_versions"
EN_ROOT = DOWNLOADS_ROOT / "en_all_versions"
PUBLISH_ROOT = WORKSPACE_ROOT / "publish"
MANIFEST_OUT = WORKSPACE_ROOT / "reports" / "publish_manifest.csv"

ZH_VERSIONS = ("v_3_18_6_20250430", "v_3_18_6_20260730", "v_3_18_6_20261030")
EN_VERSIONS = ("V3.18.6", "V3.18.6_2607")

CAT_ZH: dict[str, tuple[str, ...]] = {
    "云平台": ("apsarabase", "apsara_stack_platform"),
    "计算": ("ecs", "ecsgpu", "ess", "csk", "acr", "alinux", "dcaas", "ehpc", "ros"),
    "存储": ("hcs_hgw", "oss", "sls"),
    "网络": ("vpc", "slb", "apsara_stack_dns", "expressconnect", "cgw", "ntr", "vpn"),
    "数据库": ("polardb", "kvstore", "mongodb", "hdm", "dms", "dts", "cbs"),
    "中间件": ("rocketmq", "apigateway", "prometheus"),
    "大数据": ("odps", "dide", "hologram", "quickbi", "learn"),
    "安全": ("kms", "aegis", "sas", "sddp", "dbaudit", "ddos", "idaas"),
    "监控与运维服务": ("cms", "tongque", "oos"),
    "容灾与迁移": ("asr", "apds"),
    "OpenTrek": ("opentrek",),
}

ZH_CODE_TO_CAT: dict[str, str] = {
    code: cat for cat, codes in CAT_ZH.items() for code in codes
}

HCS_EXCLUDED_KEYWORDS = ("CPFS", "EFS-NAS", "APFS")

EN_TAG_MAP: dict[str, tuple[str, str]] = {
    "ApsaraUni-managerManagementConsole": ("Cloud Platform", "apsara_stack_platform"),
    "ApsaraCopilot": ("Cloud Platform", "apsara_stack_platform"),
    "ElasticComputeService": ("Compute", "ecs"),
    "AutoScaling": ("Compute", "ess"),
    "ContainerServiceforKubernetes": ("Compute", "csk"),
    "ContainerRegistry": ("Compute", "acr"),
    "BareMetalManagementService": ("Compute", "dcaas"),
    "ResourceOrchestrationService": ("Compute", "ros"),
    "HybridCloudStorage": ("Storage", "hcs_hgw"),
    "VirtualPrivateCloud": ("Network", "vpc"),
    "ServerLoadBalancer": ("Network", "slb"),
    "ApsaraStackDNS": ("Network", "apsara_stack_dns"),
    "ExpressConnect": ("Network", "expressconnect"),
    "CloudGateway": ("Network", "cgw"),
    "TransitRouter": ("Network", "ntr"),
    "VPNGateway": ("Network", "vpn"),
    "PolarDB": ("Database", "polardb"),
    "CloudNativeDistributedDatabasePolarDB-X": ("Database", "polardb"),
    "KVStoreforRedis": ("Database", "kvstore"),
    "ApsaraDBforMongoDB": ("Database", "mongodb"),
    "DataManagement": ("Database", "dms"),
    "DataTransmission": ("Database", "dts"),
    "DatabaseBackup": ("Database", "cbs"),
    "MessageQueueforApacheRocketMQ": ("Middleware", "rocketmq"),
    "APIGateway": ("Middleware", "apigateway"),
    "Cloud-nativeGateway": ("Middleware", "apigateway"),
    "ManagedServiceforPrometheus": ("Middleware", "prometheus"),
    "MaxCompute": ("Big Data", "odps"),
    "DataWorks": ("Big Data", "dide"),
    "BareMetalComputingPlatform": ("Big Data", "learn"),
    "KeyManagementService": ("Security", "kms"),
    "AlibabaCloudSecurity-ServerGuardAdvancedEdition": ("Security", "aegis"),
    "ContainerSecurityService(CSS)": ("Security", "aegis"),
    "AlibabaCloudSecurity-SituationAwareness": ("Security", "sas"),
    "AlibabaCloudSecurity-SituationAwarenessAlibabaCloudSecurity-SituationAwareness": (
        "Security",
        "sas",
    ),
    "DatabaseSecurityAudit": ("Security", "dbaudit"),
    "StaticDataMaskingandWatermarking": ("Security", "dbaudit"),
    "IDaaS": ("Security", "idaas"),
    "CloudMonitor": ("Monitoring and O&M", "cms"),
    "OperationOrchestrationService": ("Monitoring and O&M", "oos"),
    "ApsaraStackResilience": ("DR and Migration", "asr"),
    "ASRforZone-disasterRecovery": ("DR and Migration", "asr"),
    "ASRforGeo-disasterRecovery": ("DR and Migration", "asr"),
    "ASRforBackupandRecovery": ("DR and Migration", "asr"),
    "ASRforBackupandRecovery ": ("DR and Migration", "asr"),
    "CloudPlatformBackup": ("DR and Migration", "asr"),
    "CloudMigrationHub": ("DR and Migration", "apds"),
    "AIStudio": ("OpenTrek", "opentrek"),
    "AIGateway": ("OpenTrek", "opentrek"),
    "AgentRuntime": ("OpenTrek", "opentrek"),
    "OpenTrekDev": ("OpenTrek", "opentrek"),
    "OpenTrek-Ops": ("OpenTrek", "opentrek"),
}

SECONDARY_EDITION_RENAMES: dict[str, str] = {
    "Secondary Edition) Developer Guide 20260831.pdf": (
        "PolarDB for MySQL (Primary_Secondary Edition) Developer Guide 20260831.pdf"
    ),
    "Secondary Edition) Developer Guide 20260831_2.pdf": (
        "PolarDB for PostgreSQL (Primary_Secondary Edition) Developer Guide 20260831.pdf"
    ),
    "Secondary Edition) Operations and Maintenance Guide 20260828.pdf": (
        "PolarDB for MySQL (Primary_Secondary Edition) Operations and Maintenance Guide 20260828.pdf"
    ),
    "Secondary Edition) Operations and Maintenance Guide 20260831.pdf": (
        "PolarDB for PostgreSQL (Primary_Secondary Edition) Operations and Maintenance Guide 20260831.pdf"
    ),
    "Secondary Edition) User Guide 20260831.pdf": (
        "PolarDB for PostgreSQL (Primary_Secondary Edition) User Guide 20260831.pdf"
    ),
}

ZH_LEGACY_RULES: tuple[tuple[str, str], ...] = (
    ("弹性公网IP", "eip"),
    ("Terraform", "terraform"),
    ("灾备管理中心", "asr"),
)

EN_LEGACY_RULES: tuple[tuple[str, str], ...] = (
    ("Elastic IP Address", "eip"),
    ("Terraform", "terraform"),
    ("Object Storage Service", "oss"),
    ("Log Service", "sls"),
)

EN_PREFIX_RE = re.compile(r"^Alibaba Cloud Apsara Stack [Vv]3\.18\.6(?:-2607)?\s+")


def win_long_path(path: pathlib.Path | str) -> str:
    """Return a Windows extended-length path string (`\\\\?\\...`) for safe I/O."""
    s = str(path)
    if os.name == "nt" and not s.startswith("\\\\?\\"):
        return "\\\\?\\" + os.path.abspath(s)
    return s


def clean_filename(name: str, strip_en_prefix: bool = False) -> str:
    """Normalize NBSP and repeated whitespace, optionally stripping EN version prefix."""
    cleaned = re.sub(r" +", " ", name.replace("\xa0", " ")).strip()
    if strip_en_prefix:
        cleaned = EN_PREFIX_RE.sub("", cleaned).strip()
    return cleaned


def match_rule(name: str, rules: Iterable[tuple[str, str]]) -> str:
    """Match a filename against ordered `(substring, code)` rules or raise ValueError."""
    for needle, code in rules:
        if needle in name:
            return code
    raise ValueError(f"Unmatched legacy file: {name}")


def record_and_write(
    data: bytes,
    dest: pathlib.Path,
    seen_dests: set[str],
    rows: list[dict[str, object]],
    *,
    lang: str,
    version: str,
    category: str,
    product: str,
    source: str,
) -> None:
    """Validate PDF bytes, prevent destination collisions, write file, and append audit row."""
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Invalid PDF header from {source}")
    if len(str(dest)) >= 240:
        raise ValueError(f"Destination path too long ({len(str(dest))}): {dest}")
    dest_key = str(dest).lower()
    if dest_key in seen_dests:
        raise FileExistsError(f"Duplicate destination path: {dest}")
    seen_dests.add(dest_key)

    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data)

    rows.append(
        {
            "lang": lang,
            "version": version,
            "category": category,
            "product": product,
            "source": source,
            "dest_rel": dest.relative_to(PUBLISH_ROOT).as_posix(),
            "size_bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    )


def load_en_manifest() -> dict[tuple[str, str], set[str]]:
    """Load `(version, filename) -> set(product)` from the EN download manifest."""
    mapping: dict[tuple[str, str], set[str]] = {}
    manifest_path = EN_ROOT / "download_manifest.csv"
    with open(manifest_path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            fn = row.get("filename")
            ver = row.get("version")
            prod = row.get("product")
            if fn and ver in EN_VERSIONS and prod:
                mapping.setdefault((ver, fn), set()).add(prod)
    return mapping


def process_zh_3186(seen_dests: set[str], rows: list[dict[str, object]]) -> None:
    """Extract whitelisted ZH 3.18.6 PDFs from ZIP archives into `publish/zh`."""
    for version in ZH_VERSIONS:
        for code, category in sorted(ZH_CODE_TO_CAT.items()):
            zip_path = ZH_ROOT / version / f"{code}.zip"
            if not zip_path.exists():
                continue
            with zipfile.ZipFile(zip_path) as zf:
                for info in zf.infolist():
                    if info.is_dir():
                        continue
                    raw_name = info.filename.split("/")[-1]
                    if code == "hcs_hgw" and any(
                        kw in raw_name for kw in HCS_EXCLUDED_KEYWORDS
                    ):
                        continue
                    out_name = clean_filename(raw_name)
                    dest = PUBLISH_ROOT / "zh" / version / category / code / out_name
                    record_and_write(
                        zf.read(info.filename),
                        dest,
                        seen_dests,
                        rows,
                        lang="zh",
                        version=version,
                        category=category,
                        product=code,
                        source=f"{zip_path.relative_to(WORKSPACE_ROOT).as_posix()}::{info.filename}",
                    )


def process_zh_legacy(seen_dests: set[str], rows: list[dict[str, object]]) -> None:
    """Copy whitelisted ZH legacy PDFs into `publish/zh/legacy`."""
    legacy_dir = ZH_ROOT / "legacy"
    for src in sorted(legacy_dir.glob("*.pdf")):
        if "飞天基础运维平台" in src.name:
            continue
        code = match_rule(src.name, ZH_LEGACY_RULES)
        out_name = clean_filename(src.name)
        dest = PUBLISH_ROOT / "zh" / "legacy" / code / out_name
        record_and_write(
            src.read_bytes(),
            dest,
            seen_dests,
            rows,
            lang="zh",
            version="legacy",
            category="legacy",
            product=code,
            source=src.relative_to(WORKSPACE_ROOT).as_posix(),
        )


def process_en_3186(seen_dests: set[str], rows: list[dict[str, object]]) -> None:
    """Copy whitelisted EN 3.18.6 PDFs into `publish/en` with path/name fixes."""
    fn_to_prod = load_en_manifest()
    for version in EN_VERSIONS:
        src_dir = EN_ROOT / version
        for fn in sorted(os.listdir(win_long_path(src_dir))):
            if not fn.lower().endswith(".pdf"):
                continue
            if fn in SECONDARY_EDITION_RENAMES:
                mapped = {("Database", "polardb")}
                raw_out = SECONDARY_EDITION_RENAMES[fn]
                strip_prefix = False
            else:
                prods = fn_to_prod.get((version, fn), set())
                mapped = {EN_TAG_MAP[p] for p in prods if p in EN_TAG_MAP}
                if not mapped:
                    continue
                if len(mapped) != 1:
                    raise ValueError(f"Ambiguous EN mapping for {version}/{fn}: {mapped}")
                raw_out = fn
                strip_prefix = True

            category, code = next(iter(mapped))
            out_name = clean_filename(raw_out, strip_en_prefix=strip_prefix)
            dest = PUBLISH_ROOT / "en" / version / category / code / out_name
            src_lp = win_long_path(src_dir / fn)
            with open(src_lp, "rb") as fh:
                data = fh.read()
            record_and_write(
                data,
                dest,
                seen_dests,
                rows,
                lang="en",
                version=version,
                category=category,
                product=code,
                source=f"{src_dir.relative_to(WORKSPACE_ROOT).as_posix()}/{fn}",
            )


def process_en_legacy(seen_dests: set[str], rows: list[dict[str, object]]) -> None:
    """Copy all whitelisted EN legacy PDFs into `publish/en/legacy`."""
    legacy_dir = EN_ROOT / "legacy"
    for src in sorted(legacy_dir.glob("*.pdf")):
        code = match_rule(src.name, EN_LEGACY_RULES)
        out_name = clean_filename(src.name)
        dest = PUBLISH_ROOT / "en" / "legacy" / code / out_name
        record_and_write(
            src.read_bytes(),
            dest,
            seen_dests,
            rows,
            lang="en",
            version="legacy",
            category="legacy",
            product=code,
            source=src.relative_to(WORKSPACE_ROOT).as_posix(),
        )


def main() -> None:
    """Populate `publish/` from `downloads/` and emit `reports/publish_manifest.csv`."""
    if PUBLISH_ROOT.exists() and any(PUBLISH_ROOT.iterdir()):
        raise RuntimeError(f"{PUBLISH_ROOT} is not empty; clear it before re-running.")
    PUBLISH_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_OUT.parent.mkdir(parents=True, exist_ok=True)

    seen_dests: set[str] = set()
    rows: list[dict[str, object]] = []

    process_zh_3186(seen_dests, rows)
    process_zh_legacy(seen_dests, rows)
    process_en_3186(seen_dests, rows)
    process_en_legacy(seen_dests, rows)

    fieldnames = [
        "lang",
        "version",
        "category",
        "product",
        "source",
        "dest_rel",
        "size_bytes",
        "sha256",
    ]
    with open(MANIFEST_OUT, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Done: wrote {len(rows)} PDFs into {PUBLISH_ROOT}")


if __name__ == "__main__":
    main()
