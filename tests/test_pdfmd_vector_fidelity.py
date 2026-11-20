from hashlib import sha256
from pathlib import Path
import sys
import tempfile
import unittest

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_body import render_body
from pdfmd_document import ASSET, page_events
from pdfmd_media import extract_figures, in_box
from pdfmd_structure import build_structure


class VectorFidelity(unittest.TestCase):
    def test_inline_code_is_text_and_genuine_images_keep_their_source_bytes(self):
        pdf = next((ROOT / "docs/cn/OpenTrek").rglob("*飞天助理 开发指南 20251205.pdf"))
        with pymupdf.open(pdf) as doc, tempfile.TemporaryDirectory() as temp:
            assets = Path(temp)
            state = build_structure(doc, "cn")
            state["_qt"] = True
            for number in (5, 7, 8, 11, 19, 22, 24):
                with self.subTest(page=number):
                    page = doc[number - 1]
                    events, urls = page_events(page, state, assets)
                    source = [b for b in page.get_text("dict")["blocks"] if b["type"] == 1]
                    # The other raster marks on these pages are notice-label decorations.
                    expected = {sha256(b["image"]).hexdigest() for b in source if not b.get("mask")}
                    actual = {sha256((assets / Path(u).name).read_bytes()).hexdigest() for u in urls}
                    self.assertEqual(actual, expected)
                    if number == 7:
                        self.assertTrue(any(e["kind"] == "line" and "GetOrganizationList" in e["text"]
                                            for e in events))
                        self.assertEqual(ASSET.findall(render_body(events, "cn")), list(urls) * 2)

    def test_wrapped_inline_code_has_square_corners_at_a_line_break(self):
        pdf = next((ROOT / "docs/en").rglob("* Alibaba Cloud Message Queue User Guide 20260828.pdf"))
        with pymupdf.open(pdf) as doc, tempfile.TemporaryDirectory() as temp:
            page = doc[377]
            blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT | pymupdf.TEXT_INHIBIT_SPACES)["blocks"]
            lines = [dict(line, text="".join(s["text"] for s in line["spans"]))
                     for b in blocks for line in b.get("lines", [])]
            figures, covered = extract_figures(page, blocks, lines, page.get_drawings(), [],
                                                page.rect, Path(temp), {"_qt": True})
            self.assertFalse(figures)
            self.assertFalse(covered)

    def test_unlabelled_vector_shapes_are_preserved(self):
        with pymupdf.open() as doc, tempfile.TemporaryDirectory() as temp:
            page = doc.new_page()
            gray = (238 / 255,) * 3
            page.draw_rect((60, 80, 160, 98), radius=.15, color=None, fill=gray)
            assets = Path(temp)
            events, covered = extract_figures(page, [], [], page.get_drawings(), [],
                                               page.rect, assets, {"_qt": True})
            self.assertFalse(covered)
            self.assertEqual(len(events), 1)
            self.assertEqual((assets / Path(events[0]["url"]).name).read_bytes(),
                             page.get_pixmap(matrix=pymupdf.Matrix(3, 3),
                                             clip=pymupdf.Rect(events[0]["bbox"])).tobytes("png"))

    def test_architecture_diagram_contains_every_component_in_its_pdf_viewport(self):
        pdf = next((ROOT / "docs/cn").rglob("*裸机管理服务 产品简介 20251205.pdf"))
        with pymupdf.open(pdf) as doc, tempfile.TemporaryDirectory() as temp:
            state = build_structure(doc, "cn")
            state["_qt"] = True
            page = doc[4]
            viewport = next(d["scissor"] for d in page.get_drawings(extended=True)
                            if d["type"] == "clip" and d["level"] == 1)
            events, urls = page_events(page, state, Path(temp))
            figures = [e for e in events if e["kind"] == "image"]
            self.assertEqual(len(urls), 1)
            self.assertEqual(len(figures), 1)
            self.assertTrue(in_box(viewport, figures[0]["bbox"], 0))
            self.assertTrue(in_box(figures[0]["bbox"], viewport, 2))
            self.assertFalse(any(e["kind"] == "line" and in_box(e["bbox"], viewport) for e in events))
