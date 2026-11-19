# Apsara Stack 产品文档 — 资产盘点上架完成报告

更新时间：2026-07-27

## 交付说明

按最新要求，资产盘点的交付物为两部分（不再按分类打包成多个 zip）：

1. **一个完整 zip 包**：`apsara_stack_by_category.zip`（约 853 MB），顶层为 10 个云产品分类文件夹，内含全部 287 份未打包 PDF。
   - 位于资产目录 `ApsaraStack产品文档`（`PuINqmeKObuQ`），file_id `PDaidiQbdved`。
2. **资产内未打包 PDF 按分类存放**：在 `按云产品分类`（`PaIoHTrpJjcp`）下建 10 个分类子目录，每个目录直接放对应分类的 PDF（未打包）。

> 注：网盘对文件名做了「扩展名剥离」展示（列表里 `name` 不带 `.pdf`，但 `ext=pdf`），文件本身均为 PDF，下载后即为正常 PDF。

## 资产目录结构

```
ApsaraStack产品文档 (PuINqmeKObuQ)
├── apsara_stack_by_category.zip        ← 完整 zip（287 份，853 MB）
└── 按云产品分类 (PaIoHTrpJjcp)
    ├── 专有云与运维平台  PsRdGunLBZAq   71 份
    ├── 安全              PGsaBHwKxjbJ   54 份
    ├── 数据库            PeKPntpTvQaT   48 份
    ├── 网络与CDN         PQSBcqXnXRMz   40 份
    ├── 中间件            PMOwHVoApCrG   19 份
    ├── 大数据            PLsOfZXzqVME   18 份
    ├── 存储              PJmZmYacGTFD   15 份
    ├── 计算              PcFazEeVJawl   10 份
    ├── 容器              PfOtwZxXhDtT    8 份
    └── 人工智能          PklUKlZEdbjs    4 份
```

## 校验结果（dir_list 实测）

| 分类 | dir_id | 网盘文件数 | 与本地一致 |
|---|---|---|---|
| 专有云与运维平台 | `PsRdGunLBZAq` | 71 | ✅ |
| 安全 | `PGsaBHwKxjbJ` | 54 | ✅ |
| 数据库 | `PeKPntpTvQaT` | 48 | ✅ |
| 网络与CDN | `PQSBcqXnXRMz` | 40 | ✅ |
| 中间件 | `PMOwHVoApCrG` | 19 | ✅ |
| 大数据 | `PLsOfZXzqVME` | 18 | ✅ |
| 存储 | `PJmZmYacGTFD` | 15 | ✅ |
| 计算 | `PcFazEeVJawl` | 10 | ✅ |
| 容器 | `PfOtwZxXhDtT` | 8 | ✅ |
| 人工智能 | `PklUKlZEdbjs` | 4 | ✅ |
| **合计** | | **287** | ✅ |

全部 10 个分类目录的 `total_num` 与本地源文件数逐一吻合，无缺失、无重复（上传过程中已自动清理个别重名副本）。

## 关于 Higress

在 421 条 OSS 直链 / 287 份去重 PDF 中**未发现任何 Higress 文档**。当前专有云产品文档里与「网关」相关的仅有「云接入网关」和「AI 网关」两类，Higress（开源 Envoy 系网关）未纳入本批文档范围。

## 源数据规模

- 原始 OSS 直链：421 条 → 去重后唯一 PDF：287 份
- 版本分布：V3.18.2 含 13 份、V3.18.3 含 35 份、V3.18.6 含 239 份
- 本地整理目录：`/workspace/apsara_by_category/`（10 个分类子目录，共 287 份）
