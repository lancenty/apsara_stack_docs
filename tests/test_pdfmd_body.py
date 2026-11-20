import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_body import decorate_events, render_body


def line(text, x=70, y=100, page=1, font="DejaVuSans", size=10, **fields):
    box = (x, y - size, x + len(text) * size * .6, y + 2)
    span = dict(text=text, font=font, size=size, bbox=box, origin=(x, y))
    return dict(kind="line", text=text, spans=[span], page=page, bbox=box, **fields)


def page_lines(doc, number):
    page = doc[number-1]
    blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES)["blocks"]
    events = [dict(kind="line", bbox=l["bbox"], spans=l["spans"], page=number,
                   text="".join(s["text"] for s in l["spans"]))
              for block in blocks for l in block.get("lines", ())
              if 69 < (l["bbox"][1] + l["bbox"][3]) / 2 < 772]
    return decorate_events(page, sorted(events, key=lambda e: (e["bbox"][1], e["bbox"][0])))


class BodyTests(unittest.TestCase):
    def test_word_shaded_shell_example(self):
        source = next((ROOT / "docs/en").rglob("Red Hat OpenShift*.pdf"))
        with pymupdf.open(source) as pdf:
            text = render_body(page_lines(pdf, 39), "en")
            self.assertRegex(text, r"```bash\n\$ oc-mirror --v2 --help")

    def test_sample_policy_spans_pages_and_retains_literal_indentation(self):
        path = next((ROOT / "docs/cn").rglob("*应用运维平台 用户指南 20250529.pdf"))
        with pymupdf.open(path) as doc:
            events = [e for p in (10, 11) for e in page_lines(doc, p) if e.get("notice_rect")]
        text = render_body(events, "cn")
        self.assertEqual(text.count("```json"), 1)
        quote = "\n".join(re.sub(r"^> ?", "", l) for l in text.splitlines())
        code = quote.split("```json\n")[1].split("\n```")[0]
        policy = json.loads(code)
        self.assertEqual(len(policy["Statement"]), 2)
        self.assertEqual(policy["Statement"][0]["Action"].count("rds:ModifySecurityIps"), 1)
        self.assertIn('\n                "rds:CreateDBInstance",', code)
        self.assertIn('**说明**', text)
        self.assertEqual(text.count('<ol type="i">'), 1)
        self.assertEqual(text.count('<li>'), 3)

    def test_sample_cn_en_paragraphs_bullets_and_warning(self):
        sources = [("cn", "*应用运维平台 用户指南 20250529.pdf"), ("en", "*Application Hybrid Marketplace User Guide*")]
        for lang, filename in sources:
            with self.subTest(lang=lang), pymupdf.open(next((ROOT / "docs" / lang).rglob(filename))) as doc:
                events = page_lines(doc, 6)
                text = render_body(events, lang)
                if lang == "cn":
                    self.assertIn("各区域当前系统资源", text)
                    self.assertIn("   - **我的应用状态**", text)
                    self.assertIn("> **说明**", text)
                    self.assertIn("> - 在容器服务Kubernetes集群管理", text)
                    page19 = render_body(page_lines(doc, 19), lang)
                    self.assertIn("> **重要**", page19)
                    self.assertIn("且产生的应用数据将被删除", page19)
                else:
                    self.assertIn("Apsara Uni-manager Management Console. The homepage", text)
                    self.assertIn("**Products > Application > Hybrid Cloud Application Center**", text)
                    self.assertIn("   - **My Application Status**", text)
                    self.assertIn("kube-system from the Namespace", render_body(page_lines(doc, 7), lang))

    def test_roman_group_contains_figures_tables_and_numeric_children(self):
        events = [line("1. Parent", x=60, y=100),
                  line("i. First", x=75, y=118),
                  dict(kind="table", bbox=(90,130,250,142), page=1),
                  dict(kind="image", md="![setup](assets/setup.png)", bbox=(90,152,250,200), page=1),
                  line("1. Substep", x=91, y=220), line("ii. Second", x=70, y=240),
                  line("2. Next parent", x=60, y=260)]
        table = "| A | B |\n| --- | --- |\n| Q | R |"
        with patch("pdfmd_tables.render_table", return_value=table):
            text = render_body(events, "en")
        self.assertEqual(text.count('<ol type="i">'), 1)
        first, second = text.split("</li>", 1)
        self.assertIn("| Q | R |", first)
        self.assertIn("![setup](assets/setup.png)", first)
        self.assertIn("1. Substep", first)
        self.assertIn("<li>\n\n   Second", second)
        self.assertIn("</ol>\n\n2. Next parent", second)

    def test_native_fence_length_blank_lines_and_wrapped_command_token(self):
        # Text fills the last cell of a simulated PDF code panel before it wraps.
        first = "curl https://example.com/lo"
        rectangle = (70, 80, 76 + len(first) * 6 + 6, 220)
        events = [line(v, x=76, y=y, font="Courier", code_rect=rectangle)
                  for y, v in [(100, first), (115, "ng/path"), (145, "echo '```'"), (160, "    echo indented")]]
        text = render_body(events, "en")
        self.assertEqual(text, "````bash\ncurl https://example.com/long/path\n\necho '```'\n    echo indented\n````\n")

    def test_preserves_equal_code_lines_at_different_baselines(self):
        rect = (70, 80, 200, 150)
        result = render_body([line("echo test", y=y, font="Courier", code_rect=rect) for y in (100,115)], "en")
        self.assertEqual(result.count("echo test"), 2)


if __name__ == "__main__":
    unittest.main()
