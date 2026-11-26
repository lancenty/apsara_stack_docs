"""Package curated `publish/` PDF version directories into ZIP bundles for GitHub Releases."""

from __future__ import annotations

import hashlib
import pathlib
import zipfile

WORKSPACE_ROOT = pathlib.Path(r"C:\Users\Lancent\Documents\Workspace\apsara_stack_docs")
PUBLISH_ROOT = WORKSPACE_ROOT / "publish"
RELEASES_ROOT = WORKSPACE_ROOT / "dist" / "releases"
MAX_GITHUB_ASSET_BYTES = 2 * 1024 * 1024 * 1024

BUNDLES: dict[str, tuple[tuple[str, str], ...]] = {
    "zh": (
        ("v_3_18_6_20250430", "apsara-docs-zh-v.3.18.6-20250430.zip"),
        ("v_3_18_6_20260730", "apsara-docs-zh-v.3.18.6-20260730.zip"),
        ("v_3_18_6_20261030", "apsara-docs-zh-v.3.18.6-20261030.zip"),
        ("legacy", "apsara-docs-zh-legacy.zip"),
    ),
    "en": (
        ("V3.18.6", "apsara-docs-en-V3.18.6.zip"),
        ("V3.18.6_2607", "apsara-docs-en-V3.18.6_2607.zip"),
        ("legacy", "apsara-docs-en-legacy.zip"),
    ),
}


def sha256_file(path: pathlib.Path) -> str:
    """Compute hex SHA256 digest of a file."""
    with open(path, "rb") as fh:
        return hashlib.file_digest(fh, "sha256").hexdigest()


def build_zip(src_dir: pathlib.Path, out_zip: pathlib.Path) -> tuple[int, int]:
    """Create and integrity-test a ZIP archive of all PDFs inside `src_dir`."""
    pdfs = sorted(p for p in src_dir.rglob("*.pdf") if p.is_file())
    if not pdfs:
        raise ValueError(f"No PDFs found in {src_dir}")
    out_zip.parent.mkdir(parents=True, exist_ok=True)
    tmp_zip = out_zip.with_suffix(".zip.tmp")
    with zipfile.ZipFile(tmp_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for pdf in pdfs:
            arcname = pdf.relative_to(src_dir).as_posix()
            zf.write(pdf, arcname=arcname)
    with zipfile.ZipFile(tmp_zip, "r") as zf:
        bad = zf.testzip()
        if bad is not None:
            raise RuntimeError(f"Corrupted ZIP entry {bad} in {tmp_zip}")
    tmp_zip.replace(out_zip)
    size = out_zip.stat().st_size
    if size >= MAX_GITHUB_ASSET_BYTES:
        raise RuntimeError(f"ZIP exceeds 2 GiB GitHub Release limit: {out_zip} ({size} bytes)")
    return len(pdfs), size


def main() -> None:
    """Build release ZIPs and SHA256SUMS files for ZH and EN."""
    RELEASES_ROOT.mkdir(parents=True, exist_ok=True)
    for lang, items in BUNDLES.items():
        sums: list[str] = []
        for ver_dir, zip_name in items:
            src_dir = PUBLISH_ROOT / lang / ver_dir
            out_zip = RELEASES_ROOT / zip_name
            count, size = build_zip(src_dir, out_zip)
            digest = sha256_file(out_zip)
            sums.append(f"{digest}  {zip_name}")
            print(f"[{lang}] {zip_name}: {count} PDFs, {size / 1024 / 1024:.2f} MiB, sha256={digest[:12]}")
        sums_path = RELEASES_ROOT / f"SHA256SUMS-{lang}.txt"
        sums_path.write_text("\n".join(sums) + "\n", encoding="utf-8")
        print(f"[{lang}] Wrote {sums_path}")


if __name__ == "__main__":
    main()
