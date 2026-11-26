# 阿里云专有云文档分类报告

依据「控制台分类截图优先、官方专有云帮助中心（飞天企业版）补全」的双原则，对 `docs/cn/` 与 `docs/en/` 下的全部 **1,322 份 PDF**（中文 **905** 份、英文 **417** 份）完成了两级目录重新梳理，零文件丢失、零重复、零空目录、零路径冲突。

目录结构：`docs/cn/<一级分类>/<二级产品>/<file>.pdf`（中文 12 大类 / 86 产品）、`docs/en/<一级分类>/<二级产品>/<file>.pdf`（英文 10 大类 / 62 产品）。

## 分类原则

1. **第一优先级（控制台截图为准）**：严格遵循截图中的 10 个一级分类与 39 个二级产品归属及命名（包括截图与帮助中心口径不同之处，如 `日志服务 SLS` 归入 `存储`、`链路追踪` 与 `Prometheus监控服务` 归入 `中间件`）。
2. **第二优先级（专有云帮助中心补全）**：对于截图中未列出的产品与一级分类，严格依据[阿里云专有云帮助中心（飞天企业版）](https://help.aliyun.com/apsara/enterprise.html?tab=enterprise)官方接口清单（`outputs/products_v_3_18_6_20261030.json`、`outputs/products_v_3_18_6_20260730.json`、`outputs/products_v_3_18_6_20250430.json`、`outputs/中文三版本PDF清单.csv`）归类：
   - 帮助中心 `专有云云平台`、`统一运营平台` → `云平台`（`Cloud Platform`）
   - 帮助中心 `计算服务` → `计算`（`Compute`）
   - 帮助中心 `存储服务` → `存储`（`Storage`）
   - 帮助中心 `网络服务` → `网络`（`Networking`）
   - 帮助中心 `数据库服务` → `数据库`（`Database`）
   - 帮助中心 `云原生服务` → `中间件`（`Middleware`）
   - 帮助中心 `大数据服务` → `大数据`（`Big Data`）
   - 帮助中心 `安全服务` → `安全`（`Security`）
   - 帮助中心 `监控与运维平台`（除截图中已归入中间件的 `链路追踪` 与 `Prometheus监控服务`）→ `监控与运维服务`（`Monitoring and Ops`）
   - 帮助中心 `人工智能` → `OpenTrek`
   - 帮助中心独有且截图未覆盖的一级分类：`交付服务`（`专有云部署服务`）、`其他`（`无影`），目前仅中文文档包含该两类，英文未建空目录。

## 一级分类汇总

| 序号 | 中文目录（`docs/cn`） | 中文份数 | 英文目录（`docs/en`） | 英文份数 | 合计 |
|---|---|---:|---|---:|---:|
| 1 | 云平台 | 56 | Cloud Platform | 31 | 87 |
| 2 | 计算 | 62 | Compute | 37 | 99 |
| 3 | 存储 | 52 | Storage | 43 | 95 |
| 4 | 网络 | 44 | Networking | 42 | 86 |
| 5 | 数据库 | 168 | Database | 60 | 228 |
| 6 | 中间件 | 96 | Middleware | 41 | 137 |
| 7 | 大数据 | 106 | Big Data | 37 | 143 |
| 8 | 安全 | 228 | Security | 90 | 318 |
| 9 | 监控与运维服务 | 46 | Monitoring and Ops | 25 | 71 |
| 10 | OpenTrek | 29 | OpenTrek | 11 | 40 |
| 11 | 交付服务 | 15 | — | 0 | 15 |
| 12 | 其他 | 3 | — | 0 | 3 |
| **合计** | **12 个大类 / 86 个产品** | **905** | **10 个大类 / 62 个产品** | **417** | **1,322** |

## 完整中英文二级产品明细

| 一级分类（CN / EN） | 产品代号 | 中文二级目录 | CN | 英文二级目录 | EN | 归属依据 |
|---|---|---|---:|---|---:|---|
| 云平台 / Cloud Platform | `apsara_stack_platform` | 统一云管平台 | 14 | Apsara Uni-manager | 15 | 截图 + 帮助中心 |
| 云平台 / Cloud Platform | `asr` | 灾备管理平台 | 29 | Disaster Recovery Platform | 12 | 截图 + 帮助中心 |
| 云平台 / Cloud Platform | `apsarabase` | 全栈云平台 | 10 | — | 0 | 帮助中心 |
| 云平台 / Cloud Platform | `apds` | 云迁移中心 | 3 | Cloud Migration Hub | 4 | 帮助中心 |
| 计算 / Compute | `acr` | 容器镜像服务 ACR | 4 | Container Registry | 4 | 截图 |
| 计算 / Compute | `csk` | 容器服务 Kubernetes | 10 | Container Service for Kubernetes | 7 | 截图 |
| 计算 / Compute | `ecs` | 云服务器 ECS | 10 | Elastic Compute Service | 5 | 截图 |
| 计算 / Compute | `ess` | 弹性伸缩 | 8 | Auto Scaling | 4 | 截图 |
| 计算 / Compute | `ros` | 资源编排 ROS | 4 | Resource Orchestration Service | 5 | 截图 |
| 计算 / Compute | `oos` | 运维编排 OOS | 4 | Operation Orchestration Service | 4 | 截图 |
| 计算 / Compute | `alinux` | Alibaba Cloud Linux | 6 | — | 0 | 帮助中心 |
| 计算 / Compute | `ecsgpu` | GPU云服务器 | 1 | — | 0 | 帮助中心 |
| 计算 / Compute | `ehpc` | 弹性高性能计算 | 4 | — | 0 | 帮助中心 |
| 计算 / Compute | `dcaas` | 裸机管理 BMS | 11 | BareMetal Management Service | 8 | 帮助中心 |
| 存储 / Storage | `hcs_hgw` | 云定义存储 | 26 | Cloud Defined Storage | 27 | 截图 + 帮助中心 |
| 存储 / Storage | `oss` | 对象存储 OSS | 4 | Object Storage Service | 3 | 截图 |
| 存储 / Storage | `sls` | 日志服务 SLS | 7 | Log Service | 3 | 截图 |
| 存储 / Storage | `ots` | 表格存储 Tablestore | 8 | Tablestore | 2 | 截图 |
| 存储 / Storage | `nas` | 文件存储 NAS | 7 | File Storage NAS | 8 | 帮助中心 |
| 网络 / Networking | `slb` | 负载均衡 SLB | 9 | Server Load Balancer | 8 | 截图 |
| 网络 / Networking | `vpc` | 专有网络 VPC | 4 | Virtual Private Cloud | 4 | 截图 |
| 网络 / Networking | `cgw` | 云接入网关 | 4 | Cloud Gateway | 4 | 截图 |
| 网络 / Networking | `apsara_stack_dns` | 专有云DNS | 7 | Apsara Stack DNS | 8 | 截图 |
| 网络 / Networking | `expressconnect` | 高速通道 | 4 | Express Connect | 4 | 截图 |
| 网络 / Networking | `ntr` | 转发路由器 | 4 | TransitRouter | 4 | 帮助中心 |
| 网络 / Networking | `vpn` | VPN网关 | 4 | VPN Gateway | 4 | 帮助中心 |
| 网络 / Networking | `eip` | 弹性公网IP | 4 | Elastic IP Address | 2 | 帮助中心（历史版本） |
| 网络 / Networking | `nat` | NAT网关 | 2 | NAT Gateway | 2 | 帮助中心（历史版本） |
| 网络 / Networking | `ipv6` | IPv6网关 | 2 | IPv6 Gateway | 2 | 帮助中心（历史版本） |
| 数据库 / Database | `polardb` | 云原生关系型数据库 PolarDB | 47 | ApsaraDB for POLARDB | 16 | 截图 |
| 数据库 / Database | `rds` | 云数据库 RDS | 14 | ApsaraDB for RDS | 7 | 截图 |
| 数据库 / Database | `kvstore` | 云数据库 Redis | 12 | ApsaraDB for Redis | 8 | 截图 |
| 数据库 / Database | `dms` | 数据管理 DMS | 3 | Data Management | 3 | 截图 |
| 数据库 / Database | `dts` | 数据传输服务 DTS | 5 | Data Transmission Service | 4 | 截图 |
| 数据库 / Database | `mongodb` | 云数据库 MongoDB | 4 | ApsaraDB for MongoDB | 4 | 截图 |
| 数据库 / Database | `hdm` | 数据库自治服务 | 4 | — | 0 | 截图 |
| 数据库 / Database | `adb` | 云原生数据仓库 AnalyticDB | 21 | AnalyticDB | 7 | 帮助中心 |
| 数据库 / Database | `cbs` | 数据库备份 DBS | 4 | Database Backup | 3 | 帮助中心 |
| 数据库 / Database | `hitsdb` | 云原生多模数据库 Lindorm | 7 | Lindorm | 8 | 帮助中心 |
| 数据库 / Database | `oceanbase` | 云数据库 OceanBase | 47 | — | 0 | 帮助中心 |
| 中间件 / Middleware | `rocketmq` | 消息队列 MQ | 32 | Alibaba Cloud Message Queue | 7 | 截图 |
| 中间件 / Middleware | `edas` | 企业级分布式应用服务 EDAS | 14 | Enterprise Distributed Application Service | 16 | 截图 |
| 中间件 / Middleware | `txc` | 全局事务服务 | 8 | — | 0 | 截图 |
| 中间件 / Middleware | `xtrace` | 链路追踪 | 7 | Tracing Analysis | 4 | 截图 |
| 中间件 / Middleware | `prometheus` | Prometheus监控服务 | 7 | Prometheus Service | 4 | 截图 |
| 中间件 / Middleware | `apigateway` | API 网关 | 10 | API Gateway | 6 | 截图 |
| 中间件 / Middleware | `alikafka` | 消息队列 Kafka版 | 4 | Message Queue for Apache Kafka | 4 | 帮助中心 |
| 中间件 / Middleware | `msha` | 多活容灾 MSHA | 7 | — | 0 | 帮助中心 |
| 中间件 / Middleware | `csb` | 云服务总线 CSB | 4 | — | 0 | 帮助中心 |
| 中间件 / Middleware | `ahas` | 应用高可用服务 | 3 | — | 0 | 帮助中心 |
| 大数据 / Big Data | `odps` | 大数据计算 MaxCompute | 5 | MaxCompute | 4 | 截图 |
| 大数据 / Big Data | `dide` | 大数据开发治理平台 DataWorks | 8 | DataWorks | 4 | 截图 |
| 大数据 / Big Data | `hologram` | 交互式分析 Hologres | 5 | — | 0 | 截图 |
| 大数据 / Big Data | `bcc` | 大数据管家 | 4 | Apsara Big Data Manager | 3 | 帮助中心 |
| 大数据 / Big Data | `sc` | 实时计算（流计算） | 29 | Realtime Compute for Apache Flink | 10 | 帮助中心 |
| 大数据 / Big Data | `datahub` | 数据总线 DataHub | 8 | DataHub | 4 | 帮助中心 |
| 大数据 / Big Data | `elasticsearch` | 检索分析服务 Elasticsearch | 5 | Elasticsearch | 4 | 帮助中心 |
| 大数据 / Big Data | `learn` | 机器学习 | 24 | Machine Learning Platform for AI | 8 | 帮助中心 |
| 大数据 / Big Data | `dataphin` | 智能数据构建与管理 Dataphin | 4 | — | 0 | 帮助中心 |
| 大数据 / Big Data | `drp` | 数据资源平台 DataQ | 2 | — | 0 | 帮助中心 |
| 大数据 / Big Data | `datav` | DataV数据可视化 | 8 | — | 0 | 帮助中心 |
| 大数据 / Big Data | `quickbi` | Quick BI | 4 | — | 0 | 帮助中心 |
| 安全 / Security | `kms` | 密钥管理服务 KMS | 16 | Key Management Service | 4 | 截图 |
| 安全 / Security | `beaver` | 网络流量检测与响应 | 15 | Network Detection and Response | 5 | 截图 |
| 安全 / Security | `aegis` | 云安全中心（安骑士） | 22 | Cloud Security Center (Server Guard) | 16 | 截图 |
| 安全 / Security | `bastionhost` | 堡垒机 | 47 | Bastionhost | 6 | 截图 |
| 安全 / Security | `sas` | 云安全管理中心 | 26 | Cloud Security Management Center | 20 | 截图 |
| 安全 / Security | `sddp` | 敏感数据保护 | 7 | — | 0 | 截图 |
| 安全 / Security | `dbaudit` | 数据库审计 | 19 | Database Security Audit | 14 | 截图 |
| 安全 / Security | `ddos` | DDoS防护 | 2 | — | 0 | 截图 |
| 安全 / Security | `idaas` | 应用身份服务 | 18 | IDaaS | 4 | 截图 |
| 安全 / Security | `cas` | SSL证书（CA证书服务、数据安全） | 5 | — | 0 | 帮助中心 |
| 安全 / Security | `waf` | Web应用防火墙 | 15 | Web Application Firewall | 8 | 帮助中心 |
| 安全 / Security | `cloudfw` | 云防火墙 | 24 | Cloud Security Firewall | 10 | 帮助中心 |
| 安全 / Security | `yundun` | 云盾 | 2 | Apsara Stack Security | 3 | 帮助中心 |
| 安全 / Security | `lvwang` | 内容安全 | 3 | — | 0 | 帮助中心 |
| 安全 / Security | `hsm` | 加密服务 | 7 | — | 0 | 帮助中心 |
| 监控与运维服务 / Monitoring and Ops | `cms` | 云监控 | 4 | CloudMonitor | 3 | 截图 |
| 监控与运维服务 / Monitoring and Ops | `aso` | 专有云运维平台 | 16 | Apsara Stack Operation | 12 | 帮助中心 |
| 监控与运维服务 / Monitoring and Ops | `asm` | 应用运维平台 | 13 | Application Operation Platform | 6 | 帮助中心 |
| 监控与运维服务 / Monitoring and Ops | `arms` | 应用实时监控服务 ARMS | 7 | Application Real-time Monitoring Service | 4 | 帮助中心 |
| 监控与运维服务 / Monitoring and Ops | `tongque` | SRE技术保障平台 | 5 | — | 0 | 帮助中心 |
| 监控与运维服务 / Monitoring and Ops | `tianji` | 飞天基础运维平台 | 1 | — | 0 | 帮助中心 |
| OpenTrek / OpenTrek | `opentrek` | 智能体工厂 OpenTrek | 29 | OpenTrek | 11 | 截图 + 帮助中心 |
| 交付服务 | `asdelivery` | 专有云部署服务 | 15 | — | 0 | 帮助中心 |
| 其他 | `appstreaming` | 无影 | 3 | — | 0 | 帮助中心 |

## 本次主要修正（共移动 477 份文件、清理 61 个空目录）

- **错入一级分类修复**：
  - 将此前误放在 `计算/` 下的 8 个云原生中间件产品全部迁回 `中间件/`：`消息队列 MQ`（28）、`企业级分布式应用服务 EDAS`（14）、`API 网关`（10）、`全局事务服务`（8）、`多活容灾 MSHA`（7）、`云服务总线 CSB`（4）、`消息队列 Kafka版`（4）、`应用高可用服务`（3）；英文同步将 `Middleware/Application Hybrid Marketplace`（6）迁入 `Monitoring and Ops/Application Operation Platform`。
  - 将误放在 `计算/裸金属算力平台`（4）与 `Compute/Bare Metal Computing Platform`（8）的机器学习算力平台文档合并至 `大数据/机器学习`（`Big Data/Machine Learning Platform for AI`）。
  - 英文 `Database/DataHub`（4）移至 `Big Data/DataHub`；`OpenTrek/Apsara Copilot`（6）按帮助中心归属移至 `Cloud Platform/Apsara Uni-manager`；`Cloud Platform/Data Center as a Service`（4）合并至 `Compute/BareMetal Management Service`。
  - 按截图与帮助中心规则拆分原本挤在 `云平台/` 下的产品：`专有云部署服务`（15）→ `交付服务/专有云部署服务`；`无影`（3）→ `其他/无影`；`统一云管平台` 下 2 份 `Apsara Uni-manager运维控制台` → `监控与运维服务/专有云运维平台`。
- **同产品目录裂分合并与命名统一**：
  - **日志/监控类按截图归位并合并**：`中间件/日志服务 SLS`（4）并入 `存储/日志服务 SLS`（共 7 份）；`监控与运维服务/Prometheus监控服务`（3）与 `中间件/Prometheus 监控服务`（4）合并为 `中间件/Prometheus监控服务`（7）；`监控与运维服务/链路追踪`（4）与 `中间件/链路追踪`（3）合并为 `中间件/链路追踪`（7）；`中间件/应用运维平台`（1）并入 `监控与运维服务/应用运维平台`（共 13 份）。
  - **灾备与云定义存储合并**：中文 `灾备管理平台`（18）+ `灾备管理中心`（8）+ `备份管理平台`（3）统一为 `云平台/灾备管理平台`（29），英文合并 `Disaster Recovery Center`（7）+ `Backup Management Platform`（5）为 `Cloud Platform/Disaster Recovery Platform`（12）；中文 `混合云存储CDS`（26）改名为截图名称 `存储/云定义存储`，英文将 `Cloud Defined Storage`（4）+ `Cloud Parallel File Storage`（7）+ `Elastic File System NAS`（8）+ `ApsaraStack Parallel File System`（8）统一并入 `Storage/Cloud Defined Storage`（27）。
  - **安骑士 / 数据库 / 裸机 / OpenTrek 合并**：中文 `安骑士`（19）+ `容器安全`（3）合并为 `安全/云安全中心（安骑士）`（22），英文对应合并为 `Security/Cloud Security Center (Server Guard)`（16）；中文 `云安全中心（态势感知）`（26）改名为截图名称 `云安全管理中心`；`数据传输服务 DTS`（1）+ `数据传输服务DTS`（4）合并为 `数据传输服务 DTS`（5）；`裸机管理BMS`（7）+ `裸机管理服务`（4）合并为 `计算/裸机管理 BMS`（11）；中文 `OpenTrek/飞天助理`（25）+ `OpenTrek AI Gateway`（2）+ `OpenTrek AI Studio`（2）合并为 `OpenTrek/智能体工厂 OpenTrek`（29），英文对应 5 个子目录合并为 `OpenTrek/OpenTrek`（11）。
  - **其余规范化更名**：`对象存储` → `对象存储 OSS`、`表格存储` → `表格存储 Tablestore`、`专有云云平台` → `全栈云平台`、`实时数仓 Hologres` → `交互式分析 Hologres`、`应用身份服务 IDaaS` → `应用身份服务`，以及补齐空格风格（如 `数据管理 DMS`、`数据库备份 DBS`、`云原生多模数据库 Lindorm`、`云数据库 OceanBase`、`数据资源平台 DataQ`）。英文侧同时将 `Time Series and Spatial-Temporal Database`（4）并入 `Database/Lindorm`（8）、`Static Data Masking and Watermarking`（6）并入 `Security/Database Security Audit`（14）、`SchedulerX 2.0`（8）并入 `Middleware/Enterprise Distributed Application Service`（16）、`Cloud-native Gateway`（2）并入 `Middleware/API Gateway`（6）、`Apsara AIOps`（6）并入 `Monitoring and Ops/Apsara Stack Operation`（12）。

## 工具与产物

- `scripts/reorganize_docs.py`：双原则重整脚本，支持 `--dry-run` 预演与 `--apply` 执行（重复执行幂等，0 变更）。
- `outputs/reorganize_plan.csv`：全部 1,322 份文档重整前后的完整审计映射（含产品代号、归属依据、匹配来源、原路径与目标路径）。
- `outputs/classification_map_v2.csv`：由 `scripts/rebuild_map.py` 按当前目录结构重建的 1,322 行全量二级分类映射表。
