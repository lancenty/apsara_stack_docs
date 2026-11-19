# 阿里云专有云文档分类报告

依据图片中的产品分类体系，按文件名对 `docs/cn/` 与 `docs/en/` 文件夹中的 PDF 进行了**两级分类**。共处理 **704 个文件**（中文 287、英文 417），一级/二级目录均无残留、无遗漏、无重复。

目录结构：`docs/cn/<一级分类>/<二级产品>/xxxx.pdf`（中文）、`docs/en/<一级分类>/<二级产品>/xxxx.pdf`（英文）。此前文档位于根目录的 `Chinese/`、`English/`，现已移入 `docs/` 并分别改名为 `cn`、`en`。

## 一级分类与数量对照

| 图中分类 | cn 目录（中文） | 数量 | en 目录（英文） | 数量 |
|---|---|---:|---|---:|
| 云平台 | 云平台 | 29 | Cloud Platform | 29 |
| 计算 | 计算 | 34 | Compute | 41 |
| 存储 | 存储 | 22 | Storage | 43 |
| 网络 | 网络 | 37 | Networking | 42 |
| 数据库 | 数据库 | 52 | Database | 64 |
| 中间件 | 中间件 | 21 | Middleware | 47 |
| 大数据 | 大数据 | 15 | Big Data | 25 |
| 安全 | 安全 | 58 | Security | 90 |
| 监控与运维服务 | 监控与运维服务 | 12 | Monitoring and Ops | 19 |
| OpenTrek | OpenTrek | 7 | OpenTrek | 17 |
| **合计** | | **287** | | **417** |

## 二级产品目录

图中明确列出的二级产品按原名称建目录（如计算下的容器镜像服务 ACR、容器服务 Kubernetes、云服务器 ECS、弹性伸缩、资源编排 ROS、运维编排 OOS）；图中未列出但实际存在的产品按产品名建目录。共生成中文 64 个、英文 78 个二级目录。各一级分类下的二级产品如下：

- **云平台**：统一云管平台、灾备管理中心、备份管理平台、云迁移中心（英：Apsara Uni-manager、Disaster Recovery Center、Backup Management Platform、Cloud Migration Hub、Data Center as a Service）
- **计算**：云服务器 ECS、容器服务 Kubernetes、容器镜像服务 ACR、弹性伸缩、资源编排 ROS、运维编排 OOS、裸金属算力平台、裸机管理服务
- **存储**：云定义存储、对象存储 OSS、日志服务 SLS、表格存储 Tablestore、文件存储 NAS/CPFS、弹性文件存储 EFS-NAS、高性能并行文件存储 APFS
- **网络**：负载均衡 SLB、专有网络 VPC、云接入网关、专有云DNS、高速通道，以及 VPN网关、NAT网关、弹性公网IP、转发路由器、IPv6网关
- **数据库**：云原生关系型数据库 PolarDB、云数据库 RDS/Redis/MongoDB、数据管理 DMS、数据传输服务 DTS，以及 Lindorm、AnalyticDB、时序时空数据库、DataHub、数据库备份
- **中间件**：消息队列 MQ、企业级分布式应用服务 EDAS、链路追踪、Prometheus 监控服务、API 网关，以及 Kafka、SchedulerX、云原生网关、应用运维平台/应用市场
- **大数据**：大数据计算 MaxCompute、大数据开发治理平台 DataWorks、检索分析服务 Elasticsearch、大数据管家、实时计算 Flink
- **安全**：密钥管理服务 KMS、网络流量检测与响应、云安全中心（态势感知）、堡垒机、数据库审计、应用身份服务 IDaaS，以及安骑士、容器安全、Web应用防火墙、云防火墙、静态数据脱敏、Apsara Stack Security
  - 说明：安全编排（SOAR）、漏洞扫描在图中属于"云安全中心（态势感知）"之下，故与其合并为一个二级目录，中英文保持一致。
- **监控与运维服务**：云监控、应用实时监控服务 ARMS、专有云运维平台、Apsara AIOps
- **OpenTrek**：AI Studio、AI 网关、AgentRuntime、Apsara Copilot、飞天助理、OpenTrek Dev、OpenTrek-Ops

## 归类说明

- 采用产品名关键词匹配，规则按特异性排序（如"容器安全"先于"安骑士"，避免误归）。
- 图中只列部分二级产品，未列出的按文件名中的实际产品名建目录，保证 100% 覆盖。
- Windows 路径超过 260 字符的文件通过长路径方式完成移动。

## 回溯

- `outputs/classification_map.csv`：一级分类的原始映射（原路径 → 一级目录）。
- `outputs/classification_map_v2.csv`：二级分类的完整映射（原路径 → 一级/二级目录、命中关键词），可用于核对或回退；路径字段已按 `docs/cn`、`docs/en` 更新。
- `scripts/classify_docs.py` / `scripts/classify_docs_v2.py`：一级 / 二级分类脚本，支持 `--dry-run` 预演与 `--apply` 执行，文档目录已指向 `docs/cn`、`docs/en`。
- `scripts/rebuild_map.py`：从当前两级目录结构重建二级映射表，文档目录已指向 `docs/cn`、`docs/en`。
