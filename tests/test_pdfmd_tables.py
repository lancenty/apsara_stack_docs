"""Exercise extraction on Qt/Word manuals and merged cells with inline images."""

import sys
import unittest
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_tables import attach_image, merge_tables, render_table, tables_on_page


def extract(page):
    flags = (pymupdf.TEXTFLAGS_DICT | pymupdf.TEXT_INHIBIT_SPACES) & ~pymupdf.TEXT_PRESERVE_IMAGES
    lines = [dict(line, text="".join(s["text"] for s in line["spans"]))
             for block in page.get_text("dict", flags=flags)["blocks"] for line in block["lines"]]
    return tables_on_page(page, lines, page.get_drawings(), (0, 65, page.rect.width, page.rect.height - 65))


class TableTests(unittest.TestCase):
    def document(self, pattern):
        doc = pymupdf.open(next((ROOT / "docs").rglob(pattern)))
        self.addCleanup(doc.close)
        return doc

    def test_chinese_continuation_without_header(self):
        doc = self.document("*应用运维平台 用户指南 20250529.pdf")
        table, = extract(doc[6])
        continuation, other = extract(doc[7])
        self.assertFalse(continuation["header"])
        self.assertTrue(merge_tables(table, continuation))
        self.assertFalse(merge_tables(table, other))
        self.assertEqual(len(table["rows"]), 11)
        md = render_table(table)
        self.assertEqual(md.count("字段名称"), 1)
        self.assertIn("| 归属地域 | 是 | 选择准备部署应用的ACK集群所在地域。 |", md)
        self.assertIn("| 归属可用区 |", md)
        self.assertNotIn("| VPC |", md)

    def test_repeated_header_and_genuine_rowspan(self):
        doc = self.document("*Tablestore User Guide*.pdf")
        table, = extract(doc[5])
        continuation, = extract(doc[6])
        self.assertTrue(merge_tables(table, continuation))
        result = render_table(table)
        self.assertEqual(result.count("| Item | Limit | Description |"), 1)
        self.assertEqual(len(table["rows"]), 14)
        self.assertIn("| The data size of a row | Unlimited |", result)
        self.assertIn('rowspan="2"', render_table(extract(doc[10])[0]))

    def test_page_break_before_tall_rows(self):
        doc = self.document("*Tablestore Developer Guide*.pdf")
        table, = extract(doc[65])
        for page in (66, 67, 68, 69):
            continuation, = extract(doc[page])
            self.assertTrue(merge_tables(table, continuation), page + 1)
        self.assertEqual(len(table["rows"]), 5)
        self.assertEqual(render_table(table).count("| Parameter | Description |"), 1)

    def test_same_qt_cell_continues_beyond_both_paper_edges(self):
        doc = self.document("*V3.18.6 云迁移中心 用户指南 20251217.pdf")
        upper = extract(doc[78])[-1]
        lower = extract(doc[79])[0]
        self.assertTrue(merge_tables(upper, lower))
        self.assertFalse(upper["issues"])
        self.assertIn("开启LVM", render_table(upper))

    def test_header_at_page_foot_is_not_merged_into_first_data_row(self):
        doc = self.document("*V3.18.6 应用身份服务 开发指南 20251217.pdf")
        table = extract(doc[306])[-1]
        before = [p["text"] for c in table["rows"][0] for p in c["parts"]]
        self.assertTrue(merge_tables(table, extract(doc[307])[0]))
        after = [p["text"] for c in table["rows"][0] for p in c["parts"]]
        self.assertEqual(before, after)

    def test_words_across_rule_and_list_continuations(self):
        doc = self.document("*Red Hat OpenShift*.pdf")
        table, = extract(doc[7])
        self.assertTrue(merge_tables(table, extract(doc[8])[0]))
        result = render_table(table)
        self.assertIn("| SLB (Server Load Balancer) | SLB is an Alibaba Cloud service", result)
        self.assertFalse(table["issues"])
        table, = extract(doc[10])
        following = extract(doc[11])
        self.assertTrue(merge_tables(table, following[0]))
        self.assertEqual(len(table["rows"]), 2)
        self.assertIn("p.12:", table["issues"][0])
        self.assertIn("ARM.<br>★ Aspara Stack", render_table(table))
        table = following[-1]
        self.assertTrue(merge_tables(table, extract(doc[12])[0]))
        self.assertEqual(len(table["rows"]), 2)
        self.assertIn("<br>➔ DNS", render_table(table))

    def test_colspan_and_image_placement(self):
        with pymupdf.open() as doc:
            page = doc.new_page(width=300, height=400)
            for xs, y in [([35, 260], 100), ([35, 260], 130), ([35, 260], 180)]:
                page.draw_line((xs[0], y), (xs[1], y))
            for x, start in [(35, 100), (130, 130), (260, 100)]:
                page.draw_line((x, start), (x, 180))
            page.insert_text((39, 118), "Spanning title")
            page.insert_text((39, 151), "Diagram")
            page.insert_text((138, 151), "A < B")
            table, = extract(page)
            event = dict(page=1, bbox=(40, 154, 85, 170), md="![](assets/figure.png)", url="assets/figure.png")
            self.assertTrue(attach_image(table, event))
            self.assertFalse(attach_image(table, dict(event, bbox=(262, 110, 280, 145))))
            self.assertIn('<td colspan="2">Spanning title</td>', render_table(table))
            self.assertIn('<td>Diagram<br><img src="assets/figure.png" alt=""></td>', render_table(table))
            self.assertIn("A &lt; B", render_table(table))

    def test_headerless_new_table_with_different_columns(self):
        doc = self.document("*应用运维平台 用户指南 20250529.pdf")
        table, = extract(doc[6])
        continuation, _ = extract(doc[7])
        continuation["xs"][1] += 110
        self.assertFalse(merge_tables(table, continuation))
        continuation["xs"][1] -= 95
        self.assertTrue(merge_tables(table, continuation))


if __name__ == "__main__":
    unittest.main()
