from html.parser import HTMLParser
from pathlib import Path
import sys
import tempfile
import unittest

from markdown_it import MarkdownIt
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_body import decorate_events, render_body
from pdfmd_document import page_events
from pdfmd_structure import build_structure


class RenderedBody(HTMLParser):
    """Record text and image leaves together with their actual HTML ancestors."""

    def __init__(self, md):
        super().__init__()
        self.stack = []
        self.leaves = []
        self.feed(MarkdownIt("commonmark").render(md))

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.leaves.append((tuple(self.stack), dict(attrs)["src"]))
        elif tag not in ("br", "hr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, text):
        if text.strip():
            self.leaves.append((tuple(self.stack), text))


def event(spans, box):
    return dict(kind="line", bbox=box, page=1, spans=spans)


def text_span(text, x, x1, y, **extra):
    return dict(text=text, size=10, bbox=(x, y-10, x1, y+2), origin=(x,y), **extra)


def icon(url, box):
    return dict(kind="image", page=1, bbox=box, url=url, md=f'<img src="{url}" width="10" alt="">')


class InlineFidelity(unittest.TestCase):
    def test_real_buttons_and_sheared_references_stay_inside_their_own_steps(self):
        source = next((ROOT / "docs/cn/OpenTrek").rglob("*开发指南 20251205.pdf"))
        with pymupdf.open(source) as pdf, tempfile.TemporaryDirectory() as temp:
            state = build_structure(pdf, "cn")
            state["_qt"] = True
            events, urls = page_events(pdf[6], state, Path(temp))
            md = render_body(events, "cn")
            url = "assets/2bce3a89ad44b21dc8bfe2999bf3ef06.png"
            self.assertIn(url, urls)
            self.assertTrue((Path(temp) / Path(url).name).is_file())
        leaves = RenderedBody(md).leaves
        icons = [i for i, (_, value) in enumerate(leaves) if value == url]
        self.assertEqual(len(icons), 2)
        for idx in icons:
            step = leaves[idx][0]
            self.assertIn("li", step)
            self.assertEqual(leaves[idx-1:idx+6], [
                (step, "单击 "), (step, url), (step, " 按钮，选择"),
                (step+("strong",), "云平台"), (step, " > "),
                (step+("strong",), "统一云管平台"), (step, "，")])
        self.assertEqual(md.count('4. 单击 <img'), 2)
        references = [text for parents, text in leaves if "li" in parents and "em" in parents]
        self.assertEqual(references, ["Apsara Uni-manager运营控制台开发指南", "GetOrganizationList",
                                      "Apsara Uni-manager运营控制台开发指南", "ListResourceGroup"])

    def test_embedded_icon_within_one_homogeneous_font_run_uses_glyph_positions(self):
        with pymupdf.open() as pdf:
            page = pdf.new_page()
            page.insert_text((72,100), "left    right", fontsize=10)
            line = page.get_text("dict")["blocks"][0]["lines"][0]
            chars = page.get_text("rawdict")["blocks"][0]["lines"][0]["spans"][0]["chars"]
            image = icon("assets/button.png", (chars[4]["bbox"][0],92,chars[7]["bbox"][2],101))
            self.assertEqual(len(line["spans"]), 1)
            events = [image, event(line["spans"], line["bbox"])]
            decorate_events(page, events, [])
            dom = RenderedBody(render_body(events, "en"))
        self.assertEqual(dom.leaves, [(("p",), "left "), (("p",), "assets/button.png"), (("p",), " right")])

    def test_right_aligned_prose_two_icons_and_separate_columns(self):
        with pymupdf.open() as pdf:
            page = pdf.new_page()
            spans = [text_span("A", 300,305,100), text_span("B", 313,318,100), text_span("C", 326,331,100)]
            col = text_span("Column", 440,480,100)
            below = text_span("Next", 300,327,132)
            events = [event([col], col["bbox"]), icon("assets/2.png", (318,92,326,102)),
                      event(spans, (300,90,331,102)), icon("assets/1.png", (305,92,313,102)),
                      icon("assets/separate.png", (70,130,270,180)), event([below], below["bbox"])]
            decorate_events(page, events, [])
            md = render_body(events, "en")
        self.assertEqual(md.count("<img"), 3)
        expected = ["A ", "assets/1.png", " B ", "assets/2.png", " C"]
        dom = [text for _, text in RenderedBody(md).leaves]
        self.assertEqual(dom[dom.index("A "):dom.index("A ")+5], expected)
        self.assertIn("Column\n\n", md)
        self.assertIn("\n\nNext", md)

    def test_wide_native_bitmap_keeps_its_printed_inline_size(self):
        with pymupdf.open() as pdf:
            page = pdf.new_page()
            left = text_span("Click", 100,122,100)
            right = text_span("to continue.", 161,230,100)
            button = dict(kind="image", page=1, bbox=(123,91,159,102), url="assets/retina.png",
                          md="![](assets/retina.png)")
            events = [event([left], left["bbox"]), button, event([right], right["bbox"])]
            decorate_events(page, events, [])
            md = render_body(events, "en")
        self.assertIn('Click <img src="assets/retina.png" width="48" alt=""> to continue.', md)
        self.assertEqual([v for _,v in RenderedBody(md).leaves], ["Click ", "assets/retina.png", " to continue."])

    def test_punctuation_and_adjacent_styles_render_correctly_without_added_spaces(self):
        spans = [text_span(text,i*10,i*10+10,100,**style) for i,(text,style) in enumerate([
            ("请", {}), ("《标题》", {"flags":2}), ("阅读", {"font":"Sans-BoldOblique"}),
            ("A", {"flags":18}), ("然后", {}), ("[OK]", {"flags":16}), ("继续", {})])]
        md = render_body([event(spans, (0,90,70,102))], "cn")
        dom = RenderedBody(md).leaves
        self.assertEqual(dom, [(("p",), "请"), (("p","em"), "《标题》"),
                               (("p","em","strong"), "阅读A"), (("p",), "然后"),
                               (("p","strong"), "[OK]"), (("p",), "继续")])


if __name__ == "__main__":
    unittest.main()
