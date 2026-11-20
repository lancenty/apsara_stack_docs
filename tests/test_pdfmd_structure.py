"""Selected real PDFs exercise both document generators used by the archive."""
from pathlib import Path
import sys
import unittest

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pdfmd_structure as structure


class StructureTests(unittest.TestCase):
    def examine(self, pattern, language):
        path, = list((ROOT / "docs").rglob(pattern))
        document = pymupdf.open(path)
        self.addCleanup(document.close)
        result = structure.build_structure(document, language)
        for number, expected in result["_by_page"].items():
            page = document[number - 1]
            lines = structure._lines(page)
            headings, claimed = structure.heading_events(page, lines, result)
            self.assertEqual([h["anchor"] for h in headings], [e["anchor"] for e in expected])
            self.assertGreaterEqual(len(claimed), len(headings))
        self.assertEqual(result["issues"], [])
        self.assertEqual(len({e["anchor"] for e in result["entries"]}), len(result["entries"]))
        return document, result

    def test_chinese_cover_contents_and_running_matter(self):
        doc, result = self.examine("*应用运维平台 用户指南 20250529.pdf", "cn")
        self.assertEqual(result["cover"], ["阿里云", "专有云", "应用运维平台", "用户指南",
                                           "产品版本：V3.18.6", "文档版本：20250529"])
        self.assertEqual(result["first_body"], 5)
        self.assertEqual(len(result["entries"]), 15)
        self.assertEqual(result["entries"][2]["title"], "2.1. 登录应用中心AHM控制台")
        self.assertEqual(result["entries"][2]["level"], 2)
        page = doc[4]
        lines = structure._lines(page)
        headings, used = structure.heading_events(page, lines, result)
        self.assertEqual(headings[0]["title"], "1.概述")
        self.assertLess(headings[0]["bbox"][1], 85)
        _, top, _, bottom = structure.body_box(page, result)
        body = [structure.normalize_text(l["text"]) for idx, l in enumerate(lines)
                if idx not in used and top < (l["bbox"][1] + l["bbox"][3]) / 2 < bottom]
        self.assertTrue(body[0].startswith("应用中心AHM"))
        self.assertFalse(any("文档版本" in t or "概述" in t for t in body))

    def test_english_guide(self):
        _, result = self.examine("*V3.18.6 Application Hybrid Marketplace User Guide 20260630.pdf", "en")
        self.assertEqual(result["first_body"], 5)
        self.assertEqual(len(result["entries"]), 19)
        self.assertEqual(result["entries"][0]["title"], "1.Overview")
        self.assertEqual(len(result["cover"]), 6)

    def test_old_qt_multilevel_index(self):
        _, result = self.examine("*Tablestore Developer Guide 20220928.pdf", "en")
        self.assertEqual(result["first_body"], 9)
        self.assertEqual(len(result["entries"]), 114)
        self.assertEqual([e["level"] for e in result["entries"][:4]], [1, 2, 3, 4])
        self.assertEqual(result["entries"][3]["title"], "1.1.1.1. GetRow")
        self.assertGreater(max(e["level"] for e in result["entries"]), 4)

    def test_word_printed_contents_and_wrapped_title(self):
        doc, result = self.examine("Red Hat OpenShift*.pdf", "en")
        self.assertEqual(doc.get_toc(), [])
        self.assertEqual(result["first_body"], 6)
        self.assertEqual(len(result["entries"]), 80)
        self.assertEqual(result["entries"][-1]["page"], 158)
        self.assertFalse(any("disclaimer" in e["title"].lower() for e in result["entries"]))
        page = doc[5]
        lines = structure._lines(page)
        headings, used = structure.heading_events(page, lines, result)
        self.assertEqual(headings[0]["title"], "1 Introduction of Red Hat Openshift Container Platform")
        self.assertEqual(len(used), 2)

    def test_overlapping_table_does_not_interrupt_multiline_title(self):
        _, result = self.examine(
            "*V3.18.6 Realtime Compute for Apache Flink (Compute-Storage Separation Edition)"
            " Operations and Maintenance Guide 20260701.pdf", "en")
        self.assertTrue(any(e["title"].endswith("Flink SQL optimization tips") for e in result["entries"]))

    def test_normalization_is_limited_to_extraction_artifacts(self):
        self.assertEqual(structure.normalize_text("⽬录，⽤户⻚⾯；⻔⻛"), "目录，用户页面；门风")
        self.assertEqual(structure.normalize_text("ＡＰＩ：① 12²"), "ＡＰＩ：① 12²")


if __name__ == "__main__":
    unittest.main()
