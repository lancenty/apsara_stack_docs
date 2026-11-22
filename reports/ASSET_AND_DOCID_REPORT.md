# 文档资产独立化与 Document ID 标准化报告

## 1. 总体统计

- 文档总数：704
- 唯一 Document ID 数：704
- 唯一独立 Assets 目录数：704
- 通过确定性规则生成：703
- 通过持久化 Override 解决：1
- 通过持久化 Registry 保持：0
- 异常文档数：0
- ID 冲突组数：0
- Assets 目录冲突组数：0
- 最长 Windows 资产完整路径长度：234 字符（限制 < 260）

## 2. 独立 Assets 迁移统计

- 含图片文档数：601
- 无图片文档数：103
- 迁移前共享目录图片文件总数：21936（约 1628.9 MB）
- 迁移后独立目录图片引用总数：25696（约 1894.7 MB）
- 取消跨文档去重后新增副本数：3760（约 265.9 MB）
- 清理的旧共享 `assets/` 目录数：142

## 3. Document ID 分布统计

### 按语言

| 语言 | 文档数 |
|---|---:|
| `en-us` | 417 |
| `zh-cn` | 287 |

### 按平台版本

| 平台版本 | 文档数 |
|---|---:|
| `v3.12.0` | 12 |
| `v3.14.0` | 2 |
| `v3.16.2` | 4 |
| `v3.18.1` | 2 |
| `v3.18.2` | 18 |
| `v3.18.3` | 48 |
| `v3.18.6` | 355 |
| `v3.18.6-2607` | 263 |

### 按一级分类

| 分类 | 文档数 |
|---|---:|
| `big-data` | 40 |
| `cloud-platform` | 56 |
| `compute` | 75 |
| `database` | 116 |
| `middleware` | 68 |
| `monitoring-ops` | 33 |
| `networking` | 79 |
| `opentrek` | 24 |
| `security` | 148 |
| `storage` | 65 |

### 按产品（共 83 个产品）

| 产品 Slug | 文档数 |
|---|---:|
| `ack` | 10 |
| `acr` | 8 |
| `ahm` | 9 |
| `aiops` | 6 |
| `alb` | 4 |
| `analyticdb` | 10 |
| `apfs` | 12 |
| `api-gateway` | 7 |
| `apsara-big-data-manager` | 6 |
| `apsara-copilot` | 9 |
| `apsara-stack-security` | 4 |
| `apsara-uni-manager` | 16 |
| `apsara-uni-manager-ops` | 13 |
| `arms` | 8 |
| `asr` | 30 |
| `bare-metal-computing` | 12 |
| `bare-metal-management` | 8 |
| `bastionhost` | 9 |
| `cds` | 8 |
| `cfw` | 14 |
| `cloud-gateway` | 8 |
| `cloud-monitor` | 6 |
| `cloud-native-gateway` | 2 |
| `cloud-security-center` | 12 |
| `cloud-security-scanner` | 11 |
| `cmh` | 4 |
| `container-security` | 15 |
| `cpfs` | 10 |
| `database-audit` | 8 |
| `datahub` | 8 |
| `dataworks` | 8 |
| `dbs` | 6 |
| `dcas` | 4 |
| `dms` | 6 |
| `dns` | 13 |
| `dts` | 8 |
| `ecs` | 11 |
| `edas` | 8 |
| `efs-nas` | 12 |
| `eip` | 6 |
| `elasticsearch` | 8 |
| `ess` | 8 |
| `express-connect` | 8 |
| `flink` | 10 |
| `idaas` | 8 |
| `ipv6-gateway` | 4 |
| `kafka` | 8 |
| `kms` | 11 |
| `lindorm` | 8 |
| `maxcompute` | 8 |
| `mongodb` | 8 |
| `mq` | 11 |
| `nas` | 12 |
| `nat` | 4 |
| `ndr` | 10 |
| `oos` | 8 |
| `openshift` | 1 |
| `opentrek-agent-runtime` | 2 |
| `opentrek-ai-gateway` | 4 |
| `opentrek-ai-studio` | 4 |
| `opentrek-dev` | 3 |
| `opentrek-ops` | 2 |
| `oss` | 3 |
| `polardb` | 28 |
| `prometheus` | 8 |
| `rds` | 18 |
| `redis` | 12 |
| `ros` | 8 |
| `schedulerx` | 8 |
| `server-guard` | 17 |
| `slb` | 8 |
| `sls` | 6 |
| `smc` | 2 |
| `soar` | 9 |
| `static-data-masking` | 6 |
| `tablestore` | 2 |
| `terraform` | 1 |
| `tracing-analysis` | 7 |
| `transit-router` | 8 |
| `tsdb` | 4 |
| `vpc` | 8 |
| `vpn` | 8 |
| `waf` | 14 |

## 4. Override 清单

| 源文件 | Document ID | 原因 |
|---|---|---|
| `en/Compute/Resource Orchestration Service/Alibaba Cloud Apsara Stack Terraform User Guide 20241115.pdf` | `en-us/v3.18.3/terraform/user-guide/20241115` | Cover and filename omit Apsara Stack version; official download URL in data/apsara_latest_manifest.json places it under 01_ApsaraStackEnterprise/3.18.3/. |

## 5. 异常与冲突清单

- 异常数：0
- Document ID 冲突数：0
- Assets 目录冲突数：0
