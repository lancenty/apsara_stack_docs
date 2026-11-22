import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "scripts" / "convert_pdf_to_md.py"
VERIFY = ROOT / "scripts" / "verify_pdf_md.py"


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

            expected_assets_dir = "zh-ahm-user-guide-v3.18.6-20250529.assets"
            self.assertIn(f"]({expected_assets_dir}/", text)
            self.assertNotIn("](assets/", text)
            self.assertNotIn('src="assets/', text)
            self.assertTrue((md.parent / expected_assets_dir).is_dir())
            self.assertFalse((md.parent / "assets").exists())

            records = json.loads((Path(folder) / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(records["format"], 2)
            doc = records["documents"][0]
            self.assertEqual(doc["document_id"], "zh-cn/v3.18.6/ahm/user-guide/20250529")
            self.assertEqual(doc["assets_dir"], expected_assets_dir)
            self.assertEqual(doc["id_status"], "ok")
            self.assertEqual(doc["pages"], 24)
            self.assertEqual(doc["headings"], 15)
            self.assertEqual(len(doc["assets"]), doc["images"])

            changed = md.stat().st_mtime_ns
            subprocess.run(args, check=True, stdout=subprocess.PIPE)
            self.assertEqual(changed, md.stat().st_mtime_ns)

            verify_proc = subprocess.run(
                [sys.executable, str(VERIFY), str(pdf), "--output", folder, "--render"],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            )
            verify_data = json.loads(verify_proc.stdout)
            self.assertEqual(verify_data["summary"]["failed_checks_documents"], 0)


if __name__ == "__main__":
    unittest.main()
