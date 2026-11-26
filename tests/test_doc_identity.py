import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from convert_pdf_to_md import _find_conflicts
from doc_identity import (
    ASSETS_DIR_RE,
    DOC_ID_RE,
    MAX_ASSETS_DIR_LEN,
    build_assets_dir,
    load_overrides,
    load_rules,
    resolve_identity,
    validate_document_id_fields,
)


class DocumentIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()
        cls.overrides = load_overrides()
        cls.empty_overrides = {"format": 1, "overrides": []}
        cls.empty_registry = {"format": 1, "documents": {}}

    def test_prompt_example_document_ids_and_repeatability(self):
        cases = [
            (
                "cn/计算/云服务器 ECS/阿里云 专有云 V3.18.6 云服务器ECS 用户指南 20251230.pdf",
                ["阿里云", "专有云", "云服务器ECS", "用户指南", "产品版本：V3.18.6", "文档版本：20251230"],
                "zh-cn/3.18.6/compute/ecs/user-guide/20251230",
            ),
            (
                "cn/数据库/云数据库 RDS/阿里云 专有云 V3.18.3 云数据库RDS 用户指南（RDS PostgreSQL） 20250320.pdf",
                ["阿里云", "专有云", "云数据库RDS", "用户指南（RDS PostgreSQL）", "产品版本：V3.18.3", "文档版本：20250320"],
                "zh-cn/3.18.3/database/rds/rds-postgresql-user-guide/20250320",
            ),
            (
                "en/Database/ApsaraDB for POLARDB/"
                "Alibaba Cloud Apsara Stack V3.18.6-2607 ApsaraDB for POLARDB "
                "PolarDB for PostgreSQL (Primary_Secondary Edition) User Guide 20260831.pdf",
                [
                    "Alibaba Cloud",
                    "Apsara Stack",
                    "ApsaraDB for POLARDB",
                    "PolarDB for PostgreSQL",
                    "(Primary/Secondary Edition)",
                    "User Guide",
                    "Product Version: v3.18.6-2607",
                    "Document Version: 20260831",
                ],
                "en-us/3.18.6_2607/database/polardb/postgresql-primary-secondary-user-guide/20260831",
            ),
        ]
        for source_key, cover, expected_id in cases:
            with self.subTest(expected_id=expected_id):
                first = resolve_identity(
                    source_key, cover, rules=self.rules, overrides=self.empty_overrides, registry=self.empty_registry
                )
                second = resolve_identity(
                    source_key, cover, rules=self.rules, overrides=self.empty_overrides, registry=self.empty_registry
                )
                self.assertEqual(first, second)
                self.assertEqual(first["id_status"], "ok")
                self.assertEqual(first["document_id"], expected_id)
                self.assertRegex(first["document_id"], DOC_ID_RE)
                self.assertRegex(first["assets_dir"], ASSETS_DIR_RE)
                self.assertLessEqual(len(first["assets_dir"]), MAX_ASSETS_DIR_LEN)
                self.assertEqual(validate_document_id_fields(first), [])

    def test_publish_layout_drives_package_category_and_product_code(self):
        source = (
            "v_3_18_6_20250430/OpenTrek/opentrek/"
            "阿里云 专有云 V3.18.6 智能体工厂 OpenTrek AI Gateway 产品简介 20260528.pdf"
        )
        cover = [
            "阿里云",
            "专有云",
            "智能体工厂",
            "OpenTrek AI Gateway",
            "产品简介",
            "产品版本：V3.18.6",
            "文档版本：20260528",
        ]
        ident = resolve_identity(
            source,
            cover,
            pdf_sha256="",
            lang_hint="zh-cn",
            rules=self.rules,
            overrides=self.empty_overrides,
            registry=self.empty_registry,
        )
        self.assertEqual(ident["id_status"], "ok")
        self.assertEqual(ident["package_version"], "3.18.6_20250430")
        self.assertEqual(ident["category"], "opentrek")
        self.assertEqual(ident["product_code"], "opentrek")
        self.assertEqual(
            ident["document_id"],
            "zh-cn/3.18.6_20250430/opentrek/opentrek/ai-gateway-product-introduction/20260528",
        )

    def test_openshift_platform_version_from_cover(self):
        source = (
            "en/Compute/Container Service for Kubernetes/"
            "Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack.pdf"
        )
        cover = [
            "Red Hat OpenShift",
            "Container Platform 4.18 on",
            "Alibaba Cloud Apsara Stack",
            "Product version：OpenShift 4.18",
            "Apsara Stack 3.18.6",
            "Document version：20260703",
        ]
        ident = resolve_identity(
            source, cover, rules=self.rules, overrides=self.empty_overrides, registry=self.empty_registry
        )
        self.assertEqual(ident["id_status"], "ok")
        self.assertEqual(
            ident["document_id"],
            "en-us/3.18.6/compute/openshift/container-platform-4-18-on-apsara-stack/20260703",
        )

    def test_missing_platform_version_anomaly_and_override_resolution(self):
        source = (
            "en/Compute/Resource Orchestration Service/"
            "Alibaba Cloud Apsara Stack Terraform User Guide 20241115.pdf"
        )
        cover = ["Alibaba Cloud", "Terraform", "User Guide", "Document Version: 20241115"]
        without_ov = resolve_identity(
            source, cover, rules=self.rules, overrides=self.empty_overrides, registry=self.empty_registry
        )
        self.assertEqual(without_ov["id_status"], "anomaly")
        self.assertEqual(without_ov["document_id"], "")
        self.assertIn("missing_platform_version", without_ov["id_anomalies"])
        self.assertIn("missing_package_version", without_ov["id_anomalies"])

        with_ov = resolve_identity(
            source,
            cover,
            pdf_sha256="cac1868da4995053203e416f218121225ac1708f410357f62e03465bcc0b3be1",
            rules=self.rules,
            overrides=self.overrides,
            registry=self.empty_registry,
        )
        self.assertEqual(with_ov["id_status"], "ok")
        self.assertEqual(with_ov["id_source"], "override")
        self.assertEqual(with_ov["document_id"], "en-us/3.18.3/compute/terraform/user-guide/20241115")

    def test_untranslated_cjk_produces_anomaly(self):
        source = "cn/计算/云服务器 ECS/阿里云 专有云 V3.18.6 云服务器ECS 未知专题指南 20251230.pdf"
        cover = ["阿里云", "专有云", "云服务器ECS", "未知专题指南", "产品版本：V3.18.6", "文档版本：20251230"]
        ident = resolve_identity(
            source, cover, rules=self.rules, overrides=self.empty_overrides, registry=self.empty_registry
        )
        self.assertEqual(ident["id_status"], "anomaly")
        self.assertTrue(any(a.startswith("untranslated_cjk_in_document_key(") for a in ident["id_anomalies"]))

    def test_registry_preserves_identity_across_rename_and_move(self):
        sha = "deadbeef" * 8
        registry = {
            "format": 1,
            "documents": {
                sha: {
                    "document_id": "zh-cn/3.18.6/compute/ecs/user-guide/20251230",
                    "source": "cn/计算/云服务器 ECS/阿里云 专有云 V3.18.6 云服务器ECS 用户指南 20251230.pdf",
                    "assets_dir": "zh-ecs-user-guide-v3.18.6-20251230.assets",
                    "language": "zh-cn",
                    "package_version": "3.18.6",
                    "platform_version": "v3.18.6",
                    "category": "compute",
                    "product_code": "ecs",
                    "product": "ecs",
                    "document_key": "user-guide",
                    "base_document_key": "user-guide",
                    "document_version": "20251230",
                    "id_source": "rules",
                }
            },
        }
        moved = resolve_identity(
            "cn/计算/新目录/renamed_ecs_manual.pdf",
            ["阿里云", "专有云", "云服务器ECS", "用户指南", "产品版本：V3.18.6", "文档版本：20251230"],
            pdf_sha256=sha,
            rules=self.rules,
            overrides=self.empty_overrides,
            registry=registry,
        )
        self.assertEqual(moved["id_status"], "ok")
        self.assertEqual(moved["id_source"], "registry")
        self.assertEqual(moved["document_id"], "zh-cn/3.18.6/compute/ecs/user-guide/20251230")
        self.assertEqual(moved["assets_dir"], "zh-ecs-user-guide-v3.18.6-20251230.assets")

    def test_assets_dir_cap_and_conflict_detection(self):
        adir = build_assets_dir(
            "en-us",
            "apsara-uni-manager",
            "management-console-operations-and-maintenance-guide",
            "v3.18.6-2607",
            "20260831",
        )
        self.assertLessEqual(len(adir), MAX_ASSETS_DIR_LEN)
        self.assertRegex(adir, ASSETS_DIR_RE)
        self.assertTrue(adir.endswith("-v3.18.6-2607-20260831.assets"))

        id_conflicts, asset_conflicts = _find_conflicts(
            {
                "a.pdf": {"source": "a.pdf", "document_id": "zh-cn/3.18.6/compute/ecs/user-guide/20251230", "assets_path": "cn/a.assets"},
                "b.pdf": {"source": "b.pdf", "document_id": "zh-cn/3.18.6/compute/ecs/user-guide/20251230", "assets_path": "cn/a.assets"},
            }
        )
        self.assertIn("zh-cn/3.18.6/compute/ecs/user-guide/20251230", id_conflicts)
        self.assertIn("cn/a.assets", asset_conflicts)

    def test_independent_assets_isolation_in_same_product_directory(self):
        product_dir = ROOT / "publish/zh/v_3_18_6_20250430/安全/aegis"
        pdf_a = product_dir / "阿里云 专有云 V3.18.6 安骑士 运维指南 20260528.pdf"
        pdf_b = product_dir / "阿里云 专有云 V3.18.6 容器安全 运维指南 20260528.pdf"
        self.assertTrue(pdf_a.is_file(), pdf_a)
        self.assertTrue(pdf_b.is_file(), pdf_b)
        tool = ROOT / "scripts" / "convert_pdf_to_md.py"
        verify = ROOT / "scripts" / "verify_pdf_md.py"

        with tempfile.TemporaryDirectory() as folder:
            subprocess.run(
                [sys.executable, str(tool), str(pdf_a), str(pdf_b), "--output", folder, "--jobs", "2"],
                check=True,
                stdout=subprocess.PIPE,
            )
            out = Path(folder)
            self.assertFalse((out / "assets").exists())
            dir_a = out / "zh-server-guard-operations-guide-v3.18.6-20260528.assets"
            dir_b = out / "zh-container-security-operations-guide-v3.18.6-20260528.assets"
            self.assertTrue(dir_a.is_dir(), sorted(p.name for p in out.iterdir()))
            self.assertTrue(dir_b.is_dir(), sorted(p.name for p in out.iterdir()))
            self.assertTrue(any(path.stat().st_size for path in dir_a.iterdir()))
            self.assertTrue(any(path.stat().st_size for path in dir_b.iterdir()))

            md_a = (out / (pdf_a.stem + ".md")).read_text(encoding="utf-8")
            md_b = (out / (pdf_b.stem + ".md")).read_text(encoding="utf-8")
            self.assertIn(f"{dir_a.name}/", md_a)
            self.assertNotIn(dir_b.name, md_a)
            self.assertIn(f"{dir_b.name}/", md_b)
            self.assertNotIn(dir_a.name, md_b)

            verify_proc = subprocess.run(
                [sys.executable, str(verify), str(pdf_a), str(pdf_b), "--output", folder],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            )
            self.assertEqual(json.loads(verify_proc.stdout)["summary"]["failed_checks_documents"], 0)


if __name__ == "__main__":
    unittest.main()
