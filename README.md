# Apsara Stack 文档归档项目

阿里云专有云（Apsara Stack）产品文档的抓取、去重、下载与分类归档工程。共收录 **704 份最新文档**（中文 287、英文 417，约 2.7 GB），已按「一级分类 / 二级产品」两级目录归类。

## 目录结构

```
apsara_stack_docs/
├── README.md                 本说明
├── .gitignore                版本库忽略规则
│
├── scripts/                  【代码】抓取 / 去重 / 下载 / 分类脚本
│   ├── download_apsara.py         从 oss_links.json 下载（旧版全量）
│   ├── download_latest_bilingual.py  按 manifest 下载中英最新文档
│   ├── dedup.py                   按版本去重
│   ├── classify_docs.py           一级分类（10 大类）
│   ├── classify_docs_v2.py        二级分类（按产品）
│   └── rebuild_map.py             从当前目录结构重建二级映射表（产物修复）
│
├── data/                     【数据】URL 清单 / 链接 / manifest / 审计数据
│   ├── apsara_all_urls.txt         全量 URL
│   ├── apsara_latest_urls.txt      中英最新 URL
│   ├── apsara_zh_latest_urls.txt   中文最新 URL
│   ├── apsara_en_latest_urls.txt   英文最新 URL
│   ├── apsara_stack_en_links.json  英文链接
│   ├── apsara_stack_new_batch_2607.json  2607 批次数据
│   ├── apsara_latest_manifest.csv  最新清单（下载脚本输入）
│   ├── apsara_latest_manifest.json 最新清单 JSON
│   ├── oss_links.csv / .json / .txt  OSS 直链（三种格式）
│   └── APSARA_2607_DEDUP_AUDIT.csv  2607 去重审计
│
├── reports/                  【报告】采集 / 核查 / 去重 / 分类报告
│   ├── DOWNLOAD_README.md          下载说明
│   ├── APSARA_LATEST_MANIFEST.md   最新清单说明
│   ├── APSARA_DOWNLOAD_REPORT.md   采集总结
│   ├── APSARA_LINK_CHECK_REPORT.md 链接核查
│   ├── APSARA_2607_DEDUP_REPORT.md 2607 去重记录
│   ├── APSARA_ASSET_FINAL_REPORT.md 资产盘点
│   ├── APSARA_CATEGORY_ORGANIZE_REPORT.md 分类整理记录
│   └── CLASSIFICATION_REPORT.md    两级分类报告（最新）
│
├── outputs/                  【产物】分类映射表等生成物
│   ├── classification_map.csv      一级分类映射
│   ├── classification_map_v2.csv   二级分类映射
│   └── product_candidates.txt      产品名候选清单
│
├── docs/                     【文档】两级分类归档（cn 中文 / en 英文）
│   ├── cn/                        中文 287 份：<一级分类>/<二级产品>/xxx.pdf
│   └── en/                        英文 417 份：<一级分类>/<二级产品>/xxx.pdf
├── downloads/                （可选）下载脚本的默认输出目录
└── .workbuddy/               工作区内部数据（记忆等）
```

## 常用操作

所有脚本均从项目根目录运行，路径基于脚本位置自动解析：

```bash
# 下载中英最新文档（按 manifest）
python scripts/download_latest_bilingual.py

# 仅下载中文 / 英文
python scripts/download_latest_bilingual.py --language zh
python scripts/download_latest_bilingual.py --language en

# 全量下载（旧版，从 oss_links.json）与去重
python scripts/download_apsara.py
python scripts/dedup.py

# 分类（先一级、再二级）
python scripts/classify_docs.py --dry-run    # 预演
python scripts/classify_docs.py --apply      # 执行
python scripts/classify_docs_v2.py --dry-run
python scripts/classify_docs_v2.py --apply
```

> 依赖：下载类脚本需要 `requests`（`pip install requests`）；分类脚本仅需标准库。

## 分类体系

一级分类 10 类：云平台、计算、存储、网络、数据库、中间件、大数据、安全、监控与运维服务、OpenTrek。每类下按二级产品建目录，详见 `reports/CLASSIFICATION_REPORT.md`。

分类映射记录在 `outputs/`，可用于核对或回退。

## 将 PDF 转为带图 Markdown

转换器在本地读取 PDF。使用 Python 3.11 或更高版本，在项目根目录运行以下命令。

```powershell
python -m pip install -r requirements-pdfmd.txt

# 试转单份文档
python scripts/convert_pdf_to_md.py "docs/cn/中间件/应用运维平台/阿里云 专有云 V3.18.6 应用运维平台 用户指南 20250529.pdf"

# 转换全部中文和英文 PDF
python scripts/convert_pdf_to_md.py

# 选择语言、产品目录、输出位置或并行处理数
python scripts/convert_pdf_to_md.py --language en --jobs 4
python scripts/convert_pdf_to_md.py "docs/cn/中间件/应用运维平台" --output "preview"

# 重建指定范围，包括已有结果
python scripts/convert_pdf_to_md.py "docs/cn/中间件/应用运维平台" --force
```

每份 PDF 对应一份同名 MD，位于 `markdown/<语言>/<分类>/<产品>/`。每份文档拥有独立的同级资源目录（`<assets_dir>/`，如 `zh-ecs-user-guide-v3.18.6-20251230.assets/`），与其它文档完全解耦，可直接打包单份 MD 及其 `.assets` 目录离线阅读或独立发布。建议使用支持表格和内嵌 HTML 的 Markdown 阅读器，合并单元格及罗马数字子步骤使用 HTML 表达。

文档从纯文字封面和可跳转的多级目录开始。正文保留编号标题、加粗标签、分层步骤、提示和代码。工具按表格列线、单元格边界及分页位置识别续表。嵌入的截图优先按原始像素提取，组合图按版面截取。

[飞天助理开发指南](<markdown/cn/OpenTrek/飞天助理/阿里云 专有云 V3.18.6 飞天助理 开发指南 20251205.md>)展示了行内按钮、可复制的 API 名称和斜体引用。转换器按原 PDF 的字形倾斜与按钮坐标还原这些内容。[飞天助理产品简介](<markdown/cn/OpenTrek/飞天助理/阿里云 专有云 V3.18.6 飞天助理 产品简介 20251205.md#section-4>)中的“功能特性”表为短名称预留列宽，长说明可随阅读窗口换行。

### 标准化 Document ID 与独立 Assets

每份文档按确定性本地规则（无模型调用）生成唯一结构化 `document_id`：`{language}/{platform_version}/{product}/{document_key}/{document_version}`（如 `zh-cn/v3.18.6/ecs/user-guide/20251230`）：

- 规则词典与产品映射：`config/doc_id_rules.json`
- 人工确认覆盖规则：`config/doc_id_overrides.json`
- 持久化身份注册表：`config/doc_id_registry.json`（按源 PDF 指纹保持已有文档 ID 稳定）
- 迁移与审计脚本：`python scripts/migrate_assets_and_ids.py --dry-run` / `--apply`（输出报告至 `reports/ASSET_AND_DOCID_REPORT.md` 与 `reports/document-id-report.json`）

### 续跑和核验

转换器逐份更新输出目录中的 `manifest.json`（`format: 2`），记录 `document_id`、标准化语言/平台版本/产品/文档主题/文档版本、独立 `assets_dir` / `assets_path` / `assets` 清单，以及源/目标文件指纹与转换质量统计。重新运行相同命令会跳过源 PDF 指纹、转换规则、Document ID 及独立资源均匹配的文档，重试失败项。默认最多同时处理 6 份，内存紧张时可用 `--jobs 2`。同一输出目录一次运行一个转换任务。

清单的 `source` 和 `output` 分别给出相对于源文档根目录和输出目录的路径。`ok` 表示已生成且通过转换内置检查，`review` 表示已生成并有版面问题需要复核，`failed` 表示本次转换失败。`issues` 中的页码从 PDF 封面计为第 1 页。清单另列正文起页、空白页、跨页长图所占的续页、目录项数和跨页表格合并次数。

```powershell
# 核对源文件、MD、图片内容指纹、目录锚点、代码围栏和正文页数
python scripts/verify_pdf_md.py

# 实际渲染全库，核对 HTML 中的图片、目录链接、表格和代码块，并保存结果
python scripts/verify_pdf_md.py --render --jobs 4 --report reports/markdown-verification.json

# 核验自定义输出目录中的单个产品
python scripts/verify_pdf_md.py "docs/cn/中间件/应用运维平台" --output preview --render

# 运行针对实际 PDF 样本的回归测试
python -m unittest discover -s tests -v
```

要测量“功能特性”表在窄窗口中的实际行数，可将环境变量 `PDFMD_CHROMIUM` 设为本机 Chrome 或 Chromium 可执行文件的路径，再运行上述测试。布局用例分别在 375、640 和 900 像素宽的阅读区测量每个标签。其余样本测试直接对照 PDF 的图片字节、字形和坐标。

核验程序发现错误时返回非零退出码。核验通过后，清单中的 `review` 项仍可按页对照原 PDF，检查需要人工判断的排版细节。

本次归档的 704 份 MD 均已通过离线渲染核验。[全库核验结果](reports/markdown-verification.json)记录了正文页、标题、表格和代码块统计。[中文应用运维指南](<markdown/cn/中间件/应用运维平台/阿里云 专有云 V3.18.6 应用运维平台 用户指南 20250529.md>)可用于查看嵌套步骤、跨页参数表和 JSON 的实际效果。

[转换清单](markdown/manifest.json)保留了 OpenShift 指南的两条自动复核提示。已对照原 PDF 第 11–13 页和渲染后的表格确认，第 12 页延续“Cluster resources”表右列的 ECS 规格和 ISO 镜像说明，第 13 页延续“DNS”表左列的 DNS 记录要求，两处均已接入对应单元格。
