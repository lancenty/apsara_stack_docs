import importlib.util
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
        pdf = ROOT / "publish/zh/v_3_18_6_20250430/中间件/apigateway/阿里云 专有云 V3.18.6 API 网关 用户指南 20260528.pdf"
        self.assertTrue(pdf.is_file(), pdf)
        with tempfile.TemporaryDirectory() as folder:
            args = [sys.executable, str(TOOL), str(pdf), "--output", folder, "--jobs", "1"]
            subprocess.run(args, check=True, stdout=subprocess.PIPE)
            md = next(Path(folder).rglob("*.md"))
            text = md.read_text(encoding="utf-8")
            self.assertIn("## 4.1. 通过路由访问EDAS中的应用", text)
            self.assertIn("**操作步骤**", text)
            self.assertNotIn("法律声明", text)
            self.assertIn("网关实例", text)

            expected_assets_dir = "zh-api-gateway-user-guide-v3.18.6-20260528.assets"
            self.assertIn(f"]({expected_assets_dir}/", text)
            self.assertNotIn("](assets/", text)
            self.assertNotIn('src="assets/', text)
            self.assertTrue((md.parent / expected_assets_dir).is_dir())
            self.assertFalse((md.parent / "assets").exists())

            records = json.loads((Path(folder) / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(records["format"], 3)
            doc = records["documents"][0]
            self.assertEqual(
                doc["document_id"], "zh-cn/3.18.6_20250430/middleware/apigateway/api-gateway-user-guide/20260528"
            )
            self.assertEqual(doc["package_version"], "3.18.6_20250430")
            self.assertEqual(doc["product_code"], "apigateway")
            self.assertEqual(doc["assets_dir"], expected_assets_dir)
            self.assertEqual(doc["id_status"], "ok")
            self.assertEqual(doc["pages"], 173)
            self.assertEqual(doc["headings"], 80)
            self.assertEqual(len(doc["assets"]), doc["images"])

            changed = md.stat().st_mtime_ns
            subprocess.run(args, check=True, stdout=subprocess.PIPE)
            self.assertEqual(changed, md.stat().st_mtime_ns)

            verify_cmd = [sys.executable, str(VERIFY), str(pdf), "--output", folder]
            if importlib.util.find_spec("markdown_it"):
                verify_cmd.append("--render")
            verify_proc = subprocess.run(
                verify_cmd,
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            )
            verify_data = json.loads(verify_proc.stdout)
            self.assertEqual(verify_data["summary"]["failed_checks_documents"], 0)


if __name__ == "__main__":
    unittest.main()
