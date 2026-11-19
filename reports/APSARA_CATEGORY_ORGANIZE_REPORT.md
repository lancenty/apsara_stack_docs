# Apsara Stack 产品文档 · 按云产品分类整理报告

**项目**：阿里云文档（项目盘根 `PmvqDlmWVrDJ`）
**父目录**：`ApsaraStack产品文档`（`PuINqmeKObuQ`）→ `按云产品分类`（`PaIoHTrpJjcp`）

## 整理方式

按用户要求，**不按版本分类，而是按云产品种类分类**。整理逻辑：

1. 对 287 个去重后的唯一 PDF，从其 OSS 直链路径中解析出产品目录名（共 118 个命名变体）。
2. 规范化命名变体（如 `ECS` / `云服务器ECS` → `云服务器ECS`），并按关键词优先级归入 **10 个云产品大类**。
3. 每个大类生成一个 `<品类>_docs.zip`，上传至资产盘对应子目录。

## 资产盘最终结构

`ApsaraStack产品文档 / 按云产品分类 /` 下共 **10 个子目录**，每个含 1 个压缩包：

| 云产品大类 | 文档数 | 大小 | 子目录 file_id | zip file_id |
|---|---:|---:|---|---|
| 专有云与运维平台 | 62 | 409.4 MB | `PsRdGunLBZAq` | `PNHndcgzAsCG` |
| 安全 | 58 | 77.6 MB | `PGsaBHwKxjbJ` | `PXpKQcNvFPgS` |
| 数据库 | 48 | 60.1 MB | `PeKPntpTvQaT` | `PaMNshLUsspx` |
| 网络与CDN | 40 | 57.6 MB | `PQSBcqXnXRMz` | `PLUWCZhEcmjP` |
| 大数据 | 22 | 116.5 MB | `PLsOfZXzqVME` | `PUuhxfcFFskk` |
| 存储 | 19 | 43.4 MB | `PJmZmYacGTFD` | `PDMLSvIbUQRT` |
| 计算 | 18 | 27.6 MB | `PcFazEeVJawl` | `PzcBBhoLAWZw` |
| 中间件 | 8 | 17.4 MB | `PMOwHVoApCrG` | `PmganYRMUorT` |
| 容器 | 8 | 14.4 MB | `PfOtwZxXhDtT` | `PoSkumShUgEu` |
| 人工智能 | 4 | 29.1 MB | `PklUKlZEdbjs` | `PWGNHMEWbmDy` |
| **合计** | **287** | **~853 MB** | — | — |

> 全部 287 个去重文档均已归类，0 个未分类；每个 zip 上传后在资产盘的字节数与本地完全一致（已抽样校验：专有云 429307180 B、大数据 122145305 B、容器 15067806 B 均吻合）。

## 说明

- 原始 7 个产物（oss_links.*、download_apsara.py、dedup.py、APSARA_DOWNLOAD_REPORT.md、apsara_stack_docs.zip）仍保留在 `ApsaraStack产品文档` 根目录。
- `按云产品分类` 目录是本次新增的、按品类组织的视图；如需把 287 个 PDF 以**解压后的散文件**形式按品类存放（而非 zip 包），可再追加一步解压上传。
- 上传过程中网盘对 `dir_create` / `file_upload` 有频控（error_code 406450），已通过分批 + 间隔重试规避；`大数据_docs.zip` 首次因安全令牌转写错误返回 403，重新申请凭证后成功。
