from pathlib import Path
import sys
import tempfile
import unittest

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_document import page_events
from pdfmd_structure import build_structure


class MultiPageImage(unittest.TestCase):
    def test_tall_screenshot_is_extracted_once_at_native_dimensions(self):
        pdf = next((ROOT / "docs/cn").rglob("*飞天助理 用户指南 20251205.pdf"))
        with pymupdf.open(pdf) as doc, tempfile.TemporaryDirectory() as temp:
            state = build_structure(doc, "cn")
            state["_qt"] = True
            assets = Path(temp)
            for page in range(21,25):
                page_events(doc[page], state, assets)
            found = [p for p in assets.iterdir() if pymupdf.Pixmap(p.read_bytes()).height == 2677]
            self.assertEqual(len(found), 1)
            self.assertTrue({23,24}.issubset(state["continued_figures"]))
