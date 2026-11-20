import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "scripts" / "convert_pdf_to_md.py"


class ArchiveConversion(unittest.TestCase):
    def test_application_guide_and_resume(self):
        pdf = next((ROOT / "docs/cn").rglob("*应用运维平台 用户指南 20250529.pdf"))
        with tempfile.TemporaryDirectory() as folder:
            args = [sys.executable, str(TOOL), str(pdf), "--output", folder, "--jobs", "1"]
            subprocess.run(args, check=True, stdout=subprocess.PIPE)
            md = next(Path(folder).rglob("*.md"))
            text = md.read_text(encoding="utf-8")
            self.assertIn("## 2.1. 登录应用中心AHM控制台", text)
            self.assertIn("**操作步骤**", text)
            self.assertNotIn("法律声明", text)
            self.assertIn("rds:ModifySecurityIps", text)
            self.assertIn("归属可用区", text)
            self.assertIn("](assets/", text)
            records = json.loads((Path(folder) / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(records["documents"][0]["pages"], 24)
            self.assertEqual(records["documents"][0]["headings"], 15)
            changed = md.stat().st_mtime_ns
            subprocess.run(args, check=True, stdout=subprocess.PIPE)
            self.assertEqual(changed, md.stat().st_mtime_ns)


if __name__ == "__main__":
    unittest.main()
