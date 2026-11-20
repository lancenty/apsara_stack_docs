"""Check column layout, inline icons and emphasis in the generated tables."""

import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from markdown_it import MarkdownIt
import pymupdf

from test_pdfmd_tables import ROOT, extract

sys.path.insert(0, str(ROOT / "scripts"))
from pdfmd_tables import attach_image, render_table


class TableFidelity(unittest.TestCase):
    def feature_table(self):
        pdf = next((ROOT / "docs/cn/OpenTrek/飞天助理").glob("*产品简介 20251205.pdf"))
        with pymupdf.open(pdf) as doc:
            table, = extract(doc[7])
        # The source sets each of the nine labels on one physical line.
        labels = [row[0]["parts"][0]["text"] for row in table["rows"][1:]]
        self.assertEqual(len(labels), 9)
        self.assertTrue(all(len(row[0]["parts"]) == 1 for row in table["rows"]))
        return render_table(table), labels

    def test_cjk_feature_column_has_room_and_preserves_plain_labels(self):
        md, labels = self.feature_table()
        html = MarkdownIt("commonmark", {"html": True}).enable("table").render(md)
        self.assertRegex(html, r'<th width="[0-9]+">功能</th>')
        for label in labels:
            self.assertIn(f"<td>{label}</td>", html)

    @unittest.skipUnless(os.environ.get("PDFMD_CHROMIUM"), "set PDFMD_CHROMIUM to a local Chromium executable")
    def test_each_feature_name_renders_on_one_line_in_chromium(self):
        md, labels = self.feature_table()
        table = MarkdownIt("commonmark", {"html": True}).enable("table").render(md)
        # Measure actual text line boxes at common reader widths, including mobile.
        with tempfile.TemporaryDirectory() as temp:
            page = Path(temp) / "width-test.html"
            page.write_text("""<!doctype html><meta charset=utf-8><style>
                body{font:16px/1.5 "Microsoft YaHei",sans-serif}
                table{border-collapse:collapse;display:block;width:max-content;max-width:100%;overflow:auto}
                th,td{border:1px solid;padding:6px 13px}
                </style>""" + table + """<output></output><script>
                const results = [];
                for (const width of [375, 640, 900]) {
                    document.body.style.width = width + 'px';
                    const counts = Array.from(document.querySelectorAll('td:first-child'), cell => {
                        const range = new Range(); range.selectNodeContents(cell);
                        return new Set(Array.from(range.getClientRects(), rect => rect.top)).size;
                    });
                    results.push(counts.join(','));
                }
                document.querySelector('output').textContent = results.join('/');
                </script>""", encoding="utf-8")
            output = subprocess.run(
                [os.environ["PDFMD_CHROMIUM"], "--headless", "--disable-gpu", "--no-first-run",
                 "--disable-background-networking", f"--user-data-dir={temp}/profile", "--dump-dom", page.as_uri()],
                check=True, capture_output=True, timeout=45,
            ).stdout.decode("utf-8")
            self.assertEqual(re.search(r"<output>([^<]+)</output>", output)[1],
                             "/".join([",".join(["1"] * len(labels))] * 3))

    def test_mixed_italic_and_sized_icon_inside_cell(self):
        with pymupdf.open() as doc:
            page = doc.new_page(width=300, height=400)
            for y in (90, 120, 165):
                page.draw_line((30, y), (270, y))
            for x in (30, 108, 270):
                page.draw_line((x, 90), (x, 165))
            for x, title in ((35, "Item"), (113, "Description")):
                page.insert_text((x, 108), title)
            page.insert_text((35, 143), "Save")
            page.insert_text((113, 143), "Press ")
            x = 113 + pymupdf.get_text_length("Press ")
            page.insert_text((x, 143), "Ctrl", fontname="heit")
            x += pymupdf.get_text_length("Ctrl", fontname="heit")
            page.insert_text((x, 143), " then")
            table, = extract(page)
            icon = dict(page=1, bbox=(x+26, 133, x+35, 144),
                        md="![](assets/icon.png)", url="assets/icon.png")
            self.assertTrue(attach_image(table, icon))
            for as_html in (False, True):
                table["header"] = not as_html
                html = MarkdownIt("commonmark", {"html": True}).enable("table").render(render_table(table))
                self.assertRegex(html, r'Press <em>Ctrl</em> then\s*<img src="assets/icon.png" width="12"')
                self.assertNotIn("<br>", html)


if __name__ == "__main__":
    unittest.main()
