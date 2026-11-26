"""Restamp `document_id` in the published `dist/` manifests with the six-segment scheme.

Document IDs follow the `publish/` package layout:

    {language}/{package_version}/{category}/{product_code}/{document_key}/{document_version}

e.g. `zh-cn/3.18.6_20250430/opentrek/opentrek/ai-gateway-product-introduction/20260528`
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from doc_identity import (  # noqa: E402
    _atomic_write_json,
    extract_cover_from_markdown,
    load_overrides,
    load_rules,
    resolve_identity,
    save_registry,
    validate_document_id_fields,
)

SITES = {
    "zh": ROOT / "dist" / "apsara-docs-zh",
    "en": ROOT / "dist" / "apsara-docs-en",
}
REGISTRY_PATH = ROOT / "config" / "doc_id_registry.json"
REPORT_PATH = ROOT / "reports" / "document-id-retag.json"
ID_FIELDS = (
    "document_id",
    "language",
    "package_version",
    "platform_version",
    "category",
    "product_code",
    "product",
    "document_key",
    "base_document_key",
    "document_version",
    "title",
    "id_status",
    "id_source",
    "id_anomalies",
)


def retag_site(
    site: str, root: Path, rules: dict, overrides: dict, apply: bool, rules_stamp: str = ""
) -> tuple[dict, list[dict]]:
    """Recompute identity for every record of one site and optionally rewrite its manifest."""
    manifest_path = root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    documents = data["documents"]
    registry: dict = {}
    changes: list[dict] = []
    problems: list[dict] = []
    drift = 0

    for record in documents:
        markdown = (root / record["output"]).read_text(encoding="utf-8")
        identity = resolve_identity(
            source_key=record["source"],
            cover_lines=extract_cover_from_markdown(markdown),
            pdf_sha256=record["sha256"],
            lang_hint=record["language"],
            rules=rules,
            overrides=overrides,
            registry={"format": 1, "documents": {}},
        )
        if identity["assets_dir"] != record.get("assets_dir"):
            drift += 1
            problems.append(
                {
                    "source": record["source"],
                    "problem": "assets_dir_drift",
                    "manifest": record.get("assets_dir"),
                    "computed": identity["assets_dir"],
                }
            )
        if identity["document_id"] != record.get("document_id"):
            changes.append(
                {
                    "source": record["source"],
                    "from": record.get("document_id"),
                    "to": identity["document_id"],
                }
            )
        record.update({name: identity[name] for name in ID_FIELDS})
        record["assets_dir"] = record.get("assets_dir") or identity["assets_dir"]
        if rules_stamp:
            record["rules"] = rules_stamp
        if identity["id_status"] == "ok":
            registry[record["sha256"]] = {
                "document_id": record["document_id"],
                "source": record["source"],
                "assets_dir": record["assets_dir"],
                "language": record["language"],
                "package_version": record["package_version"],
                "platform_version": record["platform_version"],
                "category": record["category"],
                "product_code": record["product_code"],
                "product": record["product"],
                "document_key": record["document_key"],
                "base_document_key": record["base_document_key"],
                "document_version": record["document_version"],
                "id_source": record["id_source"],
            }

    ids = Counter(r["document_id"] for r in documents if r.get("document_id"))
    duplicates = {k: v for k, v in ids.items() if v > 1}
    invalid = [
        {"source": r["source"], "issues": validate_document_id_fields(r)}
        for r in documents
        if validate_document_id_fields(r)
    ]

    summary = {
        "site": site,
        "documents": len(documents),
        "unique_document_ids": len(ids),
        "ids_changed": len(changes),
        "assets_dir_drift": drift,
        "duplicate_document_ids": len(duplicates),
        "invalid_records": len(invalid),
        "package_versions": dict(sorted(Counter(r["package_version"] for r in documents).items())),
        "categories": dict(sorted(Counter(r["category"] for r in documents).items())),
        "product_codes": len({r["product_code"] for r in documents}),
    }

    if apply:
        summary_manifest = {
            "ok": sum(r["status"] == "ok" for r in documents),
            "review": sum(r["status"] == "review" for r in documents),
            "failed": sum(r["status"] == "failed" for r in documents),
            "documents": len(documents),
            "pages": sum(r.get("pages", 0) for r in documents),
            "images": sum(r.get("images", 0) for r in documents),
            "unique_document_ids": len(ids),
            "id_ok": sum(r.get("id_status") == "ok" for r in documents),
            "id_overrides": sum(r.get("id_source") == "override" for r in documents),
            "id_anomalies": sum(r.get("id_status") != "ok" for r in documents),
            "id_conflicts": len(duplicates),
            "package_versions": len({r["package_version"] for r in documents}),
            "product_codes": len({r["product_code"] for r in documents}),
        }
        payload = dict(format=3, summary=summary_manifest, documents=documents)
        _atomic_write_json(manifest_path, payload)

    problems.extend({"source": k, "problem": "duplicate_document_id", "count": v} for k, v in duplicates.items())
    problems.extend(invalid)
    return {"summary": summary, "registry": registry}, problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Rewrite dist manifests with six-segment document IDs.")
    parser.add_argument("--apply", action="store_true", help="write manifests and registry")
    parser.add_argument(
        "--refresh-rules",
        action="store_true",
        help="stamp the current converter rules fingerprint (only identity metadata changed)",
    )
    args = parser.parse_args()

    rules = load_rules()
    overrides = load_overrides()
    rules_stamp = ""
    if args.refresh_rules:
        from convert_pdf_to_md import rule_version

        rules_stamp = rule_version()
    report: dict = {"format": 1, "applied": args.apply, "sites": {}, "problems": []}
    registry: dict = {}

    for site, root in SITES.items():
        result, problems = retag_site(site, root, rules, overrides, args.apply, rules_stamp)
        report["sites"][site] = result["summary"]
        report["problems"].extend({"site": site, **p} for p in problems)
        registry.update(result["registry"])
        print(json.dumps(result["summary"], ensure_ascii=False), flush=True)

    report["registry_documents"] = len(registry)
    _atomic_write_json(REPORT_PATH, report)
    if args.apply:
        save_registry(registry)
        print(f"Wrote {len(registry)} registry entries and {REPORT_PATH}", flush=True)
    else:
        print(f"Dry run; report at {REPORT_PATH}", flush=True)
    return int(bool(report["problems"]))


if __name__ == "__main__":
    raise SystemExit(main())
