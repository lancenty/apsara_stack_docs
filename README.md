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
