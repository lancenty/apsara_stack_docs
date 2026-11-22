"""Deterministic Document ID and per-document assets directory resolution."""
from __future__ import annotations

from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
RULES_PATH = CONFIG_DIR / "doc_id_rules.json"
OVERRIDES_PATH = CONFIG_DIR / "doc_id_overrides.json"
REGISTRY_PATH = CONFIG_DIR / "doc_id_registry.json"

DOC_ID_RE = re.compile(
    r"^(zh-cn|en-us)/v\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*/[a-z0-9]+(?:-[a-z0-9]+)*/\d{8}$"
)
ASSETS_DIR_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*\.assets$")
MAX_ASSETS_DIR_LEN = 72

_BRAND_LINES = {
    "阿里云",
    "专有云",
    "专有云企业版",
    "Alibaba Cloud",
    "Apsara Stack",
    "Apsara Stack Enterprise",
}
_VERSION_LINE_RE = re.compile(
    r"^(?:产品版本|文档版本|Product\s*Version|Document\s*Version|Apsara\s+Stack\s+\d)",
    re.I,
)
_CJK_RE = re.compile(r"[\u4e00-\u9fff]+")
_COVER_PVER_RE = re.compile(
    r"(?:产品版本|Product\s*Version)\s*[:：]\s*(v?\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?)",
    re.I,
)
_COVER_AS_PVER_RE = re.compile(
    r"Apsara\s+Stack(?:\s+Enterprise)?\s+(v?\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?)",
    re.I,
)
_FILE_PVER_RE = re.compile(r"\b(v\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?)\b", re.I)
_COVER_DVER_RE = re.compile(r"(?:文档版本|Document\s*Version)\s*[:：]\s*(\d{8})", re.I)
_FILE_DVER_RE = re.compile(r"\b(20\d{6})\b")


def _atomic_write_json(path: Path, data: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    with NamedTemporaryFile(dir=path.parent, prefix=".docid-", delete=False) as handle:
        tmp = Path(handle.name)
        try:
            handle.write(payload)
        except BaseException:
            handle.close()
            tmp.unlink(missing_ok=True)
            raise
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def normalize_text(value: str) -> str:
    """Normalize Unicode width and non-breaking spaces without losing case."""
    text = unicodedata.normalize("NFKC", value).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def load_rules(path: Path | None = None) -> dict:
    target = Path(path) if path is not None else RULES_PATH
    return json.loads(target.read_text(encoding="utf-8"))


def load_overrides(path: Path | None = None) -> dict:
    target = Path(path) if path is not None else OVERRIDES_PATH
    if not target.exists():
        return {"format": 1, "overrides": []}
    return json.loads(target.read_text(encoding="utf-8"))


def load_registry(path: Path | None = None) -> dict:
    target = Path(path) if path is not None else REGISTRY_PATH
    if not target.exists():
        return {"format": 1, "documents": {}}
    return json.loads(target.read_text(encoding="utf-8"))


def save_registry(documents: dict, path: Path | None = None) -> None:
    target = Path(path) if path is not None else REGISTRY_PATH
    ordered = {k: documents[k] for k in sorted(documents)}
    _atomic_write_json(target, {"format": 1, "documents": ordered})


def extract_cover_from_markdown(md_text: str) -> list[str]:
    """Extract clean cover lines preceding the generated Table of Contents."""
    head = md_text[:4000]
    toc = re.search(r"\n\n\*\*(?:目录|Table of Contents)\*\*", head)
    if toc:
        cover_raw = head[:toc.start()]
    else:
        body = re.search(r'\n\n(?:<a\s+id="section-|# )', head)
        cover_raw = head[:body.start()] if body else head.split("\n\n", 1)[0]
    return [line.strip().rstrip("  ").strip() for line in cover_raw.splitlines() if line.strip()]


def join_cover_lines(lines: list[str]) -> str:
    """Join wrapped cover title lines without inserting spurious breaks inside wrapped words."""
    out = ""
    for raw in lines:
        line = normalize_text(raw)
        if not line:
            continue
        if not out:
            out = line
        elif out.endswith("-") and re.match(r"^[A-Za-z]", line):
            out += line
        elif out.endswith("Servic") and line == "e":
            out += line
        elif (
            re.search(r"(?:产|开|用|运|产品简|开发指|用户指|运维指|本地盘)$", out)
            and re.match(r"^(?:品简介|发指南|户指南|维指南|介|南|版(?:\s|$))", line)
        ):
            out += line
        else:
            out += " " + line
    return normalize_text(out)


def _normalize_lang_hint(lang: str) -> str:
    val = (lang or "").strip().lower()
    if val in ("cn", "zh", "zh-cn"):
        return "zh-cn"
    if val in ("en", "en-us"):
        return "en-us"
    return ""


def extract_language(source_key: str, cover_lines: list[str], lang_hint: str = "") -> tuple[str, list[str]]:
    anomalies = []
    parts = Path(source_key).parts
    path_lang = next((_normalize_lang_hint(p) for p in parts if p.lower() in ("cn", "zh", "en")), "")
    hint_lang = _normalize_lang_hint(lang_hint)
    joined = "\n".join(normalize_text(line) for line in cover_lines)

    cover_lang = ""
    if any(tok in joined for tok in ("阿里云", "专有云", "产品版本", "文档版本")) or _CJK_RE.search(joined):
        cover_lang = "zh-cn"
    elif any(tok in joined.lower() for tok in ("alibaba cloud", "apsara stack", "product version", "document version")):
        cover_lang = "en-us"

    chosen = path_lang or hint_lang or cover_lang
    if path_lang and cover_lang and path_lang != cover_lang:
        anomalies.append(f"language_mismatch(path={path_lang},cover={cover_lang})")
    if not chosen:
        anomalies.append("missing_language")
    return chosen, anomalies


def _norm_pver(raw: str) -> str:
    val = raw.strip().lower()
    if val and not val.startswith("v"):
        val = "v" + val
    return val


def extract_platform_version(cover_lines: list[str], filename: str) -> tuple[str, list[str]]:
    anomalies = []
    joined = "\n".join(normalize_text(line) for line in cover_lines)
    cover_ver = ""
    m = _COVER_PVER_RE.search(joined)
    if m:
        cover_ver = _norm_pver(m.group(1))
    else:
        m2 = _COVER_AS_PVER_RE.search(joined)
        if m2:
            cover_ver = _norm_pver(m2.group(1))

    m_file = _FILE_PVER_RE.search(normalize_text(filename))
    file_ver = _norm_pver(m_file.group(1)) if m_file else ""

    if cover_ver and file_ver and cover_ver != file_ver:
        anomalies.append(f"platform_version_mismatch(cover={cover_ver},filename={file_ver})")

    chosen = cover_ver or file_ver
    if not chosen:
        anomalies.append("missing_platform_version")
    return chosen, anomalies


def _valid_date(yyyymmdd: str) -> bool:
    if not re.fullmatch(r"\d{8}", yyyymmdd or ""):
        return False
    try:
        datetime.strptime(yyyymmdd, "%Y%m%d")
        return True
    except ValueError:
        return False


def extract_document_version(cover_lines: list[str], filename: str) -> tuple[str, list[str]]:
    anomalies = []
    joined = "\n".join(normalize_text(line) for line in cover_lines)
    m_cov = _COVER_DVER_RE.search(joined)
    cover_ver = m_cov.group(1) if m_cov else ""

    m_file = _FILE_DVER_RE.search(normalize_text(filename))
    file_ver = m_file.group(1) if m_file else ""

    if cover_ver and file_ver and cover_ver != file_ver:
        anomalies.append(f"document_version_mismatch(cover={cover_ver},filename={file_ver})")

    chosen = cover_ver or file_ver
    if not chosen:
        anomalies.append("missing_document_version")
    elif not _valid_date(chosen):
        anomalies.append(f"invalid_document_version_date({chosen})")
    return chosen, anomalies


def _strip_pattern(text: str, pattern: str) -> str:
    prefix = r"(?<![A-Za-z0-9])" if re.match(r"^[A-Za-z0-9]", pattern) else ""
    suffix = r"(?![A-Za-z0-9])" if re.search(r"[A-Za-z0-9]$", pattern) else ""
    return re.sub(prefix + pattern + suffix, " ", text, flags=re.I)


def _slugify(token: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", token.lower()).strip("-")


def _clean_filename_title(filename: str) -> str:
    stem = Path(filename).stem
    stem = normalize_text(stem)
    stem = re.sub(r"\(\d+\)$", "", stem).strip()
    stem = re.sub(r"^(?:阿里云\s+专有云(?:企业版)?|Alibaba\s+Cloud\s+Apsara\s+Stack(?:\s+Enterprise)?)\s+", "", stem, flags=re.I)
    stem = re.sub(r"\bv\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?\b", " ", stem, flags=re.I)
    stem = re.sub(r"\b20\d{6}\b", " ", stem)
    return normalize_text(stem)


def extract_product_and_key(
    cover_lines: list[str], filename: str, prod_dir: str, rules: dict
) -> tuple[str, str, str, str, list[str]]:
    anomalies = []
    title_lines = []
    for raw in cover_lines:
        line = normalize_text(raw)
        if not line or line in _BRAND_LINES or _VERSION_LINE_RE.match(line):
            continue
        title_lines.append(line)

    full_title = join_cover_lines(title_lines)
    clean_file = _clean_filename_title(filename)
    products = rules.get("products", [])

    matched = None
    title_cf = full_title.casefold()
    file_cf = normalize_text(filename).casefold()
    for prod in products:
        if any(kw.casefold() in title_cf for kw in prod["title_keywords"]):
            matched = prod
            break
    if matched is None:
        for prod in products:
            if any(kw.casefold() in file_cf for kw in prod["title_keywords"]):
                matched = prod
                break
    if matched is None and prod_dir:
        for prod in products:
            if prod_dir in prod.get("dir_aliases", ()):
                matched = prod
                break

    if matched is None:
        anomalies.append("unknown_product")
        return "", "", "", full_title or clean_file, anomalies

    subject = full_title or clean_file
    for _ in range(4):
        prev = subject
        for pat in matched.get("strip_patterns", ()):
            subject = normalize_text(_strip_pattern(subject, pat))
        if subject == prev:
            break

    for pat, rep in rules.get("topic_replacements", ()):
        subject = re.sub(pat, f" {rep} ", subject, flags=re.I)
    subject = normalize_text(subject)

    cjk_leftovers = _CJK_RE.findall(subject)
    if cjk_leftovers:
        anomalies.append(f"untranslated_cjk_in_document_key({','.join(cjk_leftovers)})")

    doc_type_set = set(rules.get("doc_type_suffixes", ()))
    tokens = [_slugify(tok) for tok in subject.split() if _slugify(tok)]
    dedup = []
    for tok in tokens:
        if not dedup or dedup[-1] != tok:
            dedup.append(tok)
    others = [tok for tok in dedup if tok not in doc_type_set]
    types = [tok for tok in dedup if tok in doc_type_set]
    document_key = "-".join(others + types)
    if not document_key:
        anomalies.append("empty_document_key")

    return matched["slug"], matched["category"], document_key, full_title or clean_file, anomalies


def build_assets_dir(document_id: str, fallback_key: str, language: str = "") -> str:
    """Compute a concise, deterministic, Windows-safe sibling directory name (<72 chars)."""
    short_lang = "zh" if language == "zh-cn" else ("en" if language == "en-us" else "doc")
    if document_id and DOC_ID_RE.fullmatch(document_id):
        lang, pver, prod, dkey, dver = document_id.split("/")
        short_lang = "zh" if lang == "zh-cn" else "en"
        candidate = f"{short_lang}-{prod}-{dkey}-{pver}-{dver}.assets"
        if len(candidate) <= MAX_ASSETS_DIR_LEN:
            return candidate
        digest = hashlib.sha256(document_id.encode("utf-8")).hexdigest()[:8]
        tail = f"-{digest}-{pver}-{dver}.assets"
        prefix = f"{short_lang}-{prod}-"
        avail = MAX_ASSETS_DIR_LEN - len(prefix) - len(tail)
        if avail >= 4:
            dkey_part = dkey[:avail].rstrip("-") or dkey[:avail]
            return f"{prefix}{dkey_part}{tail}"
        rem = MAX_ASSETS_DIR_LEN - len(f"{short_lang}-") - len(tail)
        prod_part = prod[: max(1, rem)].rstrip("-") or prod[: max(1, rem)]
        return f"{short_lang}-{prod_part}{tail}"

    slug = re.sub(r"[^a-z0-9]+", "-", (fallback_key or "doc").lower()).strip("-")[:32] or "doc"
    digest = hashlib.sha256((fallback_key or "doc").encode("utf-8")).hexdigest()[:8]
    return f"{short_lang}-{slug}-{digest}.assets"


def _match_override(ov: dict, source_key: str, pdf_sha256: str) -> bool:
    ov_sha = ov.get("sha256")
    ov_src = ov.get("source")
    if pdf_sha256 and ov_sha:
        return ov_sha == pdf_sha256
    return bool(ov_src and ov_src == source_key)


def _category_for_product(product_slug: str, rules: dict) -> str:
    for prod in rules.get("products", ()):
        if prod["slug"] == product_slug:
            return prod["category"]
    return ""


def _filter_overridden_anomalies(anomalies: list[str], overridden_fields: dict) -> list[str]:
    drop_prefixes = []
    if overridden_fields.get("language"):
        drop_prefixes.extend(("missing_language", "language_mismatch"))
    if overridden_fields.get("platform_version"):
        drop_prefixes.extend(("missing_platform_version", "platform_version_mismatch"))
    if overridden_fields.get("document_version"):
        drop_prefixes.extend(("missing_document_version", "invalid_document_version_date", "document_version_mismatch"))
    if overridden_fields.get("product"):
        drop_prefixes.append("unknown_product")
    if overridden_fields.get("document_key"):
        drop_prefixes.extend(("empty_document_key", "untranslated_cjk_in_document_key"))
    return [a for a in anomalies if not any(a.startswith(p) for p in drop_prefixes)]


def resolve_identity(
    source_key: str,
    cover_lines: list[str],
    pdf_sha256: str = "",
    lang_hint: str = "",
    rules: dict | None = None,
    overrides: dict | None = None,
    registry: dict | None = None,
) -> dict:
    """Resolve standardized Document ID and assets directory deterministically."""
    rules = rules if rules is not None else load_rules()
    overrides = overrides if overrides is not None else load_overrides()
    registry = registry if registry is not None else load_registry()

    parts = Path(source_key).parts
    filename = parts[-1] if parts else source_key
    prod_dir = parts[-2] if len(parts) >= 2 else ""

    language, lang_anomalies = extract_language(source_key, cover_lines, lang_hint)
    platform_version, pver_anomalies = extract_platform_version(cover_lines, filename)
    document_version, dver_anomalies = extract_document_version(cover_lines, filename)
    product, category, document_key, title, prod_anomalies = extract_product_and_key(
        cover_lines, filename, prod_dir, rules
    )
    anomalies = [*lang_anomalies, *pver_anomalies, *dver_anomalies, *prod_anomalies]

    id_source = "rules"
    override_reason = ""
    registry_note = ""

    matched_ov = next(
        (ov for ov in overrides.get("overrides", ()) if _match_override(ov, source_key, pdf_sha256)),
        None,
    )
    if matched_ov:
        fields = matched_ov.get("fields", {})
        language = fields.get("language", language)
        platform_version = fields.get("platform_version", platform_version)
        product = fields.get("product", product)
        document_key = fields.get("document_key", document_key)
        document_version = fields.get("document_version", document_version)
        category = fields.get("category") or _category_for_product(product, rules) or category
        title = fields.get("title", title)
        anomalies = _filter_overridden_anomalies(anomalies, fields)
        id_source = "override"
        override_reason = matched_ov.get("reason", "")
    elif pdf_sha256 and pdf_sha256 in registry.get("documents", {}):
        reg = registry["documents"][pdf_sha256]
        reg_id = reg.get("document_id", "")
        if DOC_ID_RE.fullmatch(reg_id):
            computed_id = (
                f"{language}/{platform_version}/{product}/{document_key}/{document_version}"
                if all((language, platform_version, product, document_key, document_version))
                else ""
            )
            if computed_id != reg_id:
                registry_note = (
                    f"Computed rule ID '{computed_id}' differs from registered ID '{reg_id}'; "
                    "preserving registered ID."
                )
            language = reg.get("language") or language
            platform_version = reg.get("platform_version") or platform_version
            product = reg.get("product") or product
            document_key = reg.get("document_key") or document_key
            document_version = reg.get("document_version") or document_version
            category = reg.get("category") or _category_for_product(product, rules) or category
            anomalies = []
            if reg.get("source") != source_key:
                id_source = "registry"

    document_id = ""
    if all((language, platform_version, product, document_key, document_version)):
        candidate = f"{language}/{platform_version}/{product}/{document_key}/{document_version}"
        if DOC_ID_RE.fullmatch(candidate) and _valid_date(document_version):
            document_id = candidate
        elif not any("invalid_document_version_date" in a for a in anomalies):
            anomalies.append(f"invalid_document_id_format({candidate})")

    id_status = "ok" if (document_id and not anomalies) else "anomaly"
    assets_dir = build_assets_dir(document_id if id_status == "ok" else "", source_key, language)

    result = {
        "document_id": document_id,
        "language": language,
        "platform_version": platform_version,
        "product": product,
        "document_key": document_key,
        "document_version": document_version,
        "category": category,
        "title": title,
        "id_status": id_status,
        "id_source": id_source,
        "id_anomalies": anomalies,
        "assets_dir": assets_dir,
    }
    if override_reason:
        result["override_reason"] = override_reason
    if registry_note:
        result["registry_note"] = registry_note
    return result


def validate_document_id_fields(record: dict) -> list[str]:
    """Validate Document ID structure, component consistency, and anomaly status on a manifest record."""
    issues = []
    doc_id = record.get("document_id", "")
    if not doc_id or not DOC_ID_RE.fullmatch(doc_id):
        issues.append(f"Invalid or missing document_id: {doc_id!r}")
        return issues
    parts = doc_id.split("/")
    fields = (
        ("language", parts[0]),
        ("platform_version", parts[1]),
        ("product", parts[2]),
        ("document_key", parts[3]),
        ("document_version", parts[4]),
    )
    for name, expected in fields:
        if record.get(name) != expected:
            issues.append(f"Field {name}={record.get(name)!r} does not match document_id segment {expected!r}")
    if not _valid_date(parts[4]):
        issues.append(f"Invalid calendar date in document_version: {parts[4]!r}")
    if record.get("id_status") != "ok":
        issues.append(f"id_status is {record.get('id_status')!r}")
    if record.get("id_anomalies"):
        issues.append(f"Document has id_anomalies: {record['id_anomalies']}")
    return issues
