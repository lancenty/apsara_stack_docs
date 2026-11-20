from pathlib import Path
import sys
import unittest

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_document import extract_blocks


def spans(page):
    return [span for block in extract_blocks(page, pymupdf.TEXTFLAGS_DICT | pymupdf.TEXT_INHIBIT_SPACES)
            for line in block.get("lines", []) for span in line["spans"]]


class TypesetText(unittest.TestCase):
    def test_open_trek_citations_use_a_sheared_upright_font(self):
        path = next((ROOT / "docs/cn/OpenTrek/飞天助理").glob("*开发指南 20251205.pdf"))
        with pymupdf.open(path) as pdf:
            runs = spans(pdf[6])
            italic = "".join(s["text"] for s in runs if s["flags"] & 2)
            self.assertIn("GetOrganizationList", italic)
            self.assertIn("ListResourceGroup", italic)
            self.assertNotIn("2019-05-10", italic)
            self.assertTrue(any("GetOrganizationList" in s["text"] and not s["flags"] & 2 for s in runs))

    def test_rotation_and_regular_horizontal_scaling_do_not_imply_italics(self):
        with pymupdf.open() as doc:
            page = doc.new_page()
            page.insert_text((72,100), "Rotated", rotate=90)
            page.insert_text((72,140), "Wide", morph=(pymupdf.Point(72,140), pymupdf.Matrix(1.4,1)))
            self.assertFalse(any(s["flags"] & 2 for s in spans(page)))
