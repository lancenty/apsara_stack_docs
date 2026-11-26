"""Migrate shared product-level assets to per-document independent directories and standardize Document IDs."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from convert_pdf_to_md import (
    _LEGACY_ASSET_REF,
    native,
    rule_version,
    run_lock,
    save_manifest,
)
from doc_identity import (
    ASSETS_DIR_RE,
    extract_cover_from_markdown,
    load_overrides,
    load_registry,
    load_rules,
    resolve_identity,
    save_registry,
)
from pdfmd_media import atomic_write


IMAGE_REF_RE = re.compile(
    r'(?P<prefix>!\[[^\]\n]*\]\(|<img\b[^>]*?\bsrc=["\'])'
    r'(?P<dir>assets|[a-z0-9][a-z0-9._-]*\.assets)/(?P<name>[a-f0-9]{32}\.[a-z0-9]+)'
)


def _rewrite_markdown_images(md_text: str, new_assets_dir: str) -> tuple[str, list[tuple[str, str]]]:
    """Rewrite image directory prefixes while preserving every other byte of Markdown."""
    refs_found = []
    out = []
    last = 0
    for match in IMAGE_REF_RE.finditer(md_text):
        refs_found.append((match.group("dir"), match.group("name")))
        out.append(md_text[last : match.start("dir")])
        out.append(new_assets_dir)
        last = match.end("dir")
    out.append(md_text[last:])
    rewritten = "".join(out)

    # Round-trip check: restoring each replaced span to its original directory must equal md_text.
    rebuilt = []
    last = 0
    idx = 0
    for match in IMAGE_REF_RE.finditer(rewritten):
        orig_dir, orig_name = refs_found[idx]
        if match.group("name") != orig_name:
            raise ValueError(f"Image name mismatch during rewrite verification: {match.group('name')} != {orig_name}")
        rebuilt.append(rewritten[last : match.start("dir")])
        rebuilt.append(orig_dir)
        last = match.end("dir")
        idx += 1
    rebuilt.append(rewritten[last:])
    if idx != len(refs_found) or "".join(rebuilt) != md_text:
        raise ValueError("Markdown round-trip verification failed during asset rewrite")
    return rewritten, refs_found


def _copy_if_needed(src: Path, dst: Path, expected_stem: str) -> tuple[int, bool]:
    """Verify hash of source image and write to independent destination if absent or different."""
    data = src.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if not digest.startswith(expected_stem):
        raise ValueError(f"Asset hash mismatch for {src}: sha256={digest}")
    if src == dst:
        return len(data), False
    try:
        already = dst.is_file() and dst.stat().st_size == len(data) and dst.read_bytes() == data
    except OSError:
        already = False
    if not already:
        atomic_write(dst, data)
        return len(data), True
    return len(data), False


def _build_markdown_report(summary: dict) -> str:
    lines = [
        "# 文档资产独立化与 Document ID 标准化报告",
        "",
        "## 1. 总体统计",
        "",
        f"- 文档总数：{summary['total_documents']}",
        f"- 唯一 Document ID 数：{summary['unique_document_ids']}",
        f"- 唯一独立 Assets 目录数：{summary['unique_assets_paths']}",
        f"- 通过确定性规则生成：{summary['by_id_source'].get('rules', 0)}",
        f"- 通过持久化 Override 解决：{summary['by_id_source'].get('override', 0)}",
        f"- 通过持久化 Registry 保持：{summary['by_id_source'].get('registry', 0)}",
        f"- 异常文档数：{len(summary['anomalies'])}",
        f"- ID 冲突组数：{len(summary['id_conflicts'])}",
        f"- Assets 目录冲突组数：{len(summary['assets_conflicts'])}",
        f"- 最长 Windows 资产完整路径长度：{summary['max_asset_path_len']} 字符（限制 < 260）",
        "",
        "## 2. 独立 Assets 迁移统计",
        "",
        f"- 含图片文档数：{summary['assets_stats']['docs_with_images']}",
        f"- 无图片文档数：{summary['assets_stats']['docs_without_images']}",
        f"- 迁移前共享目录图片文件总数：{summary['assets_stats']['legacy_unique_files']}（约 {summary['assets_stats']['legacy_total_mb']} MB）",
        f"- 迁移后独立目录图片引用总数：{summary['assets_stats']['per_doc_unique_images']}（约 {summary['assets_stats']['per_doc_total_mb']} MB）",
        f"- 取消跨文档去重后新增副本数：{summary['assets_stats']['duplicated_copies']}（约 {summary['assets_stats']['duplicated_mb']} MB）",
        f"- 清理的旧共享 `assets/` 目录数：{summary['assets_stats']['removed_shared_dirs']}",
        "",
        "## 3. Document ID 分布统计",
        "",
        "### 按语言",
        "",
        "| 语言 | 文档数 |",
        "|---|---:|",
    ]
    for k, v in sorted(summary["by_language"].items()):
        lines.append(f"| `{k}` | {v} |")
    lines.extend(["", "### 按发布包版本", "", "| 包版本 | 文档数 |", "|---|---:|"])
    for k, v in sorted(summary["by_package_version"].items()):
        lines.append(f"| `{k}` | {v} |")
    lines.extend(["", "### 按一级分类", "", "| 分类 | 文档数 |", "|---|---:|"])
    for k, v in sorted(summary["by_category"].items()):
        lines.append(f"| `{k}` | {v} |")
    lines.extend(["", f"### 按产品代码（共 {len(summary['by_product_code'])} 个）", "", "| 产品代码 | 文档数 |", "|---|---:|"])
    for k, v in sorted(summary["by_product_code"].items()):
        lines.append(f"| `{k}` | {v} |")

    lines.extend(["", "## 4. Override 清单", ""])
    if summary["overrides_applied"]:
        lines.extend(["| 源文件 | Document ID | 原因 |", "|---|---|---|"])
        for ov in summary["overrides_applied"]:
            lines.append(f"| `{ov['source']}` | `{ov['document_id']}` | {ov['reason']} |")
    else:
        lines.append("- 无")

    lines.extend(["", "## 5. 异常与冲突清单", ""])
    if not summary["anomalies"] and not summary["id_conflicts"] and not summary["assets_conflicts"]:
        lines.append("- 异常数：0")
        lines.append("- Document ID 冲突数：0")
        lines.append("- Assets 目录冲突数：0")
    else:
        for item in summary["anomalies"]:
            lines.append(f"- [异常] `{item['source']}`: {item['anomalies']} (candidate: `{item['document_id']}`)")
        for doc_id, srcs in sorted(summary["id_conflicts"].items()):
            lines.append(f"- [ID 冲突] `{doc_id}` -> {srcs}")
        for apath, srcs in sorted(summary["assets_conflicts"].items()):
            lines.append(f"- [Assets 冲突] `{apath}` -> {srcs}")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="将共享产品级 assets 迁移为每文档独立目录，并标准化 Document ID。")
    ap.add_argument("--dry-run", action="store_true", help="仅分析与校验，不修改文件")
    ap.add_argument("--apply", action="store_true", help="执行迁移与 Manifest 更新")
    ap.add_argument("--output", type=Path, default=ROOT / "markdown", help="Markdown 输出根目录")
    ap.add_argument("--report-json", type=Path, help="JSON 报告输出路径")
    ap.add_argument("--report-md", type=Path, help="Markdown 报告输出路径")
    ap.add_argument("--allow-anomalies", action="store_true", help="允许存在异常时继续迁移（仅用于调试）")
    args = ap.parse_args()
    if args.dry_run == args.apply:
        ap.error("请指定 --dry-run 或 --apply 中的一个")

    root = native(args.output)
    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"找不到 manifest.json: {manifest_path}")

    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    documents = manifest_data["documents"]
    rules = load_rules()
    overrides = load_overrides()
    registry = load_registry()
    version = rule_version()

    plans = []
    by_id = defaultdict(list)
    by_assets_path = defaultdict(list)
    anomalies = []
    overrides_applied = []
    registry_notes = []
    max_asset_path_len = 0
    max_asset_path_sample = ""

    legacy_files_seen = {}
    per_doc_unique_images = 0
    per_doc_total_bytes = 0
    docs_with_images = 0

    for rec in documents:
        md_rel = Path(rec["output"])
        md_path = native(root / md_rel)
        if not md_path.is_file():
            raise SystemExit(f"找不到 Markdown 文件: {md_path}")
        md_text = md_path.read_text(encoding="utf-8")
        cover = extract_cover_from_markdown(md_text)
        ident = resolve_identity(
            source_key=rec["source"],
            cover_lines=cover,
            pdf_sha256=rec.get("sha256", ""),
            rules=rules,
            overrides=overrides,
            registry=registry,
        )
        assets_dir = ident["assets_dir"]
        if not ASSETS_DIR_RE.fullmatch(assets_dir):
            raise ValueError(f"非法的独立目录名称: {assets_dir}")
        assets_path = (md_rel.parent / assets_dir).as_posix()

        rewritten_md, refs_found = _rewrite_markdown_images(md_text, assets_dir)
        unique_refs = sorted(set(refs_found))
        unique_names = sorted({name for _, name in unique_refs})
        if unique_names:
            docs_with_images += 1
        per_doc_unique_images += len(unique_names)

        # Verify source image existence and collect byte stats
        for old_dir, name in unique_refs:
            src_img = native(md_path.parent / old_dir / name)
            if not src_img.is_file():
                raise SystemExit(f"缺失图片文件 {src_img} (被 {rec['output']} 引用)")
            sz = src_img.stat().st_size
            legacy_files_seen[str(src_img)] = sz
            per_doc_total_bytes += sz
            dst_sample = str((args.output / md_rel.parent / assets_dir / name).resolve())
            if len(dst_sample) > max_asset_path_len:
                max_asset_path_len = len(dst_sample)
                max_asset_path_sample = dst_sample

        if ident["document_id"]:
            by_id[ident["document_id"]].append(rec["source"])
        by_assets_path[assets_path].append(rec["source"])
        if ident["id_status"] != "ok":
            anomalies.append(
                {
                    "source": rec["source"],
                    "document_id": ident["document_id"],
                    "anomalies": ident["id_anomalies"],
                }
            )
        if ident["id_source"] == "override":
            overrides_applied.append(
                {
                    "source": rec["source"],
                    "document_id": ident["document_id"],
                    "reason": ident.get("override_reason", ""),
                }
            )
        if ident.get("registry_note"):
            registry_notes.append({"source": rec["source"], "note": ident["registry_note"]})

        plans.append(
            {
                "record": rec,
                "md_path": md_path,
                "orig_md": md_text,
                "rewritten_md": rewritten_md,
                "unique_refs": unique_refs,
                "unique_names": unique_names,
                "identity": ident,
                "assets_dir": assets_dir,
                "assets_path": assets_path,
            }
        )

    id_conflicts = {k: v for k, v in by_id.items() if len(v) > 1}
    assets_conflicts = {k: v for k, v in by_assets_path.items() if len(v) > 1}
    legacy_dirs = sorted(
        {str(p) for p in root.rglob("assets") if p.is_dir()}
    )
    legacy_total_bytes = sum(legacy_files_seen.values())
    dup_bytes = per_doc_total_bytes - legacy_total_bytes

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "rules_version": version,
        "total_documents": len(plans),
        "unique_document_ids": len(by_id),
        "unique_assets_paths": len(by_assets_path),
        "by_language": dict(Counter(p["identity"]["language"] for p in plans)),
        "by_package_version": dict(Counter(p["identity"]["package_version"] for p in plans)),
        "by_category": dict(Counter(p["identity"]["category"] for p in plans)),
        "by_product_code": dict(Counter(p["identity"]["product_code"] for p in plans)),
        "by_id_source": dict(Counter(p["identity"]["id_source"] for p in plans)),
        "overrides_applied": overrides_applied,
        "registry_notes": registry_notes,
        "anomalies": anomalies,
        "id_conflicts": id_conflicts,
        "assets_conflicts": assets_conflicts,
        "max_asset_path_len": max_asset_path_len,
        "max_asset_path_sample": max_asset_path_sample,
        "assets_stats": {
            "docs_with_images": docs_with_images,
            "docs_without_images": len(plans) - docs_with_images,
            "legacy_unique_files": len(legacy_files_seen),
            "legacy_total_mb": round(legacy_total_bytes / 1048576, 1),
            "per_doc_unique_images": per_doc_unique_images,
            "per_doc_total_mb": round(per_doc_total_bytes / 1048576, 1),
            "duplicated_copies": per_doc_unique_images - len(legacy_files_seen),
            "duplicated_mb": round(dup_bytes / 1048576, 1),
            "legacy_shared_dirs_found": len(legacy_dirs),
            "removed_shared_dirs": 0,
        },
    }

    if args.apply:
        if (anomalies and not args.allow_anomalies) or id_conflicts or assets_conflicts:
            if args.report_json:
                atomic_write(native(args.report_json), (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
            raise SystemExit(
                f"中止迁移：发现 anomalies={len(anomalies)}, id_conflicts={len(id_conflicts)}, "
                f"assets_conflicts={len(assets_conflicts)}。"
            )

        with run_lock(root):
            new_records = {}
            superseded_dirs = set()
            for item in plans:
                rec = dict(item["record"])
                ident = item["identity"]
                md_path = item["md_path"]
                assets_dir = item["assets_dir"]
                target_asset_dir = native(md_path.parent / assets_dir)

                # Copy images into this document's own assets directory
                for old_dir, name in item["unique_refs"]:
                    src_img = native(md_path.parent / old_dir / name)
                    dst_img = native(target_asset_dir / name)
                    _copy_if_needed(src_img, dst_img, Path(name).stem)
                    if old_dir != assets_dir and old_dir.endswith(".assets"):
                        superseded_dirs.add(md_path.parent / old_dir)

                # Clean stale files inside the document's dedicated directory
                expected_names = set(item["unique_names"])
                if target_asset_dir.is_dir():
                    for leftover in list(target_asset_dir.iterdir()):
                        if leftover.is_file() and leftover.name not in expected_names:
                            leftover.unlink()
                    if not expected_names and not any(target_asset_dir.iterdir()):
                        target_asset_dir.rmdir()

                new_bytes = item["rewritten_md"].encode("utf-8")
                if not md_path.is_file() or md_path.read_bytes() != new_bytes:
                    atomic_write(md_path, new_bytes)

                rec["rules"] = version
                rec["bytes"] = len(new_bytes)
                rec["md_sha256"] = hashlib.sha256(new_bytes).hexdigest()
                rec["images"] = len(item["unique_names"])
                rec["assets_dir"] = assets_dir
                rec["assets_path"] = item["assets_path"]
                rec["assets"] = item["unique_names"]
                rec["document_id"] = ident["document_id"]
                rec["language"] = ident["language"]
                rec["package_version"] = ident["package_version"]
                rec["platform_version"] = ident["platform_version"]
                rec["product_code"] = ident["product_code"]
                rec["product"] = ident["product"]
                rec["document_key"] = ident["document_key"]
                rec["base_document_key"] = ident["base_document_key"]
                rec["document_version"] = ident["document_version"]
                rec["category"] = ident["category"]
                rec["title"] = ident["title"]
                rec["id_status"] = ident["id_status"]
                rec["id_source"] = ident["id_source"]
                rec["id_anomalies"] = ident["id_anomalies"]
                new_records[rec["source"]] = rec

            # Clean superseded per-document directories (if any document's slug/assets_dir changed)
            for sdir in sorted(superseded_dirs):
                if sdir.is_dir():
                    shutil.rmtree(native(sdir))

            # Verify no .md in a product directory still uses legacy assets/, then remove shared assets/ dirs
            removed_dirs = 0
            for d_str in legacy_dirs:
                shared_dir = Path(d_str)
                if not shared_dir.is_dir():
                    continue
                prod_dir = shared_dir.parent
                for md_file in prod_dir.glob("*.md"):
                    if _LEGACY_ASSET_REF.search(native(md_file).read_text(encoding="utf-8")):
                        raise SystemExit(f"迁移失败：{md_file} 仍引用旧版共享 assets/")
                shutil.rmtree(native(shared_dir))
                removed_dirs += 1

            summary["assets_stats"]["removed_shared_dirs"] = removed_dirs
            save_manifest(manifest_path, new_records)

            if root == native(ROOT / "markdown"):
                reg_docs = dict(registry.get("documents", {}))
                for rec in new_records.values():
                    if rec["id_status"] == "ok" and rec.get("sha256"):
                        reg_docs[rec["sha256"]] = {
                            "document_id": rec["document_id"],
                            "source": rec["source"],
                            "assets_dir": rec["assets_dir"],
                            "language": rec["language"],
                            "package_version": rec["package_version"],
                            "platform_version": rec["platform_version"],
                            "category": rec["category"],
                            "product_code": rec["product_code"],
                            "product": rec["product"],
                            "document_key": rec["document_key"],
                            "base_document_key": rec["base_document_key"],
                            "document_version": rec["document_version"],
                            "id_source": rec["id_source"],
                        }
                save_registry(reg_docs)

    report_json_path = args.report_json or (ROOT / "reports" / "document-id-report.json" if args.apply else None)
    report_md_path = args.report_md or (ROOT / "reports" / "ASSET_AND_DOCID_REPORT.md" if args.apply else None)
    if report_json_path:
        atomic_write(
            native(report_json_path),
            (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        )
    if report_md_path:
        atomic_write(native(report_md_path), _build_markdown_report(summary).encode("utf-8"))

    print(
        json.dumps(
            {
                "mode": summary["mode"],
                "total_documents": summary["total_documents"],
                "unique_document_ids": summary["unique_document_ids"],
                "unique_assets_paths": summary["unique_assets_paths"],
                "anomalies": len(summary["anomalies"]),
                "id_conflicts": len(summary["id_conflicts"]),
                "assets_conflicts": len(summary["assets_conflicts"]),
                "overrides": len(summary["overrides_applied"]),
                "max_asset_path_len": summary["max_asset_path_len"],
                "assets_stats": summary["assets_stats"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if anomalies or id_conflicts or assets_conflicts:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
