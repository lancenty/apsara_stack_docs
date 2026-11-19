# Apsara Stack document archive

The archive scope is the current bilingual latest-document manifest in `data/apsara_latest_manifest.csv` (704 unique documents: 287 Chinese and 417 English). Older revisions are excluded; see `APSARA_LATEST_MANIFEST.md` for the collection and deduplication notes.

## Current verified download status — 2026-11-16

| Language | Manifest | Verified PDFs | Remaining |
|---|---:|---:|---:|
| Chinese | 287 | 287 | 0 |
| English | 417 | 417 | 0 |
| **Total** | **704** | **704** | **0** |

All manifest PDFs are present and were checked for the `%PDF-` signature; all 287 Chinese PDFs also match the manifest file sizes. Nineteen older English PDFs covered by the V3.18.6-2607 batch were removed; the file mapping, hashes, and restoration URLs are in `data/APSARA_2607_DEDUP_AUDIT.csv`. The broader historical URL list in `data/apsara_all_urls.txt` remains unchanged.

## Folders

- `docs/cn/`: 287 verified Chinese PDFs (two-level category/product layout).
- `docs/en/`: 417 verified English PDFs (two-level category/product layout).

The directories were previously named `Chinese/` and `English/` at the project root; they have been moved into `docs/` and renamed `cn` / `en`.

## Download or resume

Run from this project directory:

```powershell
python scripts/download_latest_bilingual.py --language en --workers 2
```

To download both languages or only Chinese:

```powershell
python scripts/download_latest_bilingual.py
python scripts/download_latest_bilingual.py --language zh
```

The downloader reads `data/apsara_latest_manifest.csv`, checks PDF signatures and known file sizes, keeps completed files, writes into `docs/cn` or `docs/en`, and writes any failures to `outputs/download_failures.txt`. Rerun the command to resume missing files.
