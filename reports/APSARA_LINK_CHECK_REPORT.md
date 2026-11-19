# 下载路径核查报告

核查时间：2026-11-15 · 核查对象：7 月保存的 421 条 OSS 直链及官方当前状态

## 结论速览

| 问题 | 结论 |
|---|---|
| 之前的下载路径还可用吗？ | ✅ **可用**。抽样 19 条，17 条正常返回 PDF，2 条仍是已知 404；完整下载 1 份实测成功 |
| 为什么有 agent 说需要登录？ | ⚠️ **误解**，详见第 2 节——OSS 直链本身公开读，不需登录 |
| 还有更新吗？ | 🆕 **有**。发现 265 份全新英文版 `V3.18.6-2607` 文档（2026-07~09），我们清单里没有 |
| 能下载到本地吗？ | ✅ 能。本地已有 287 份完整副本；新批次链接也已整理好 |

---

## 1. 旧直链当前可用性

- 链接来源：`/workspace/oss_links.json` / `.txt` / `.csv`，域名 `apsarastackdocument.oss-cn-hangzhou.aliyuncs.com`（OSS 公开读）。
- 抽样 19 条（覆盖 V3.18.2 / V3.18.3 / V3.18.6）：
  - **17 条** → `206 application/pdf`，响应体以 `%PDF-1.4` 开头，无重定向、无登录页、无 403。
  - **2 条** → `404`，正是 7 月报告里已记录的源站删除对象：V3.18.6「数据传输 用户指南 20250925」「大数据计算服务 用户指南 20250728」。状态未变。
- 完整下载验证：HTTP 200，323,929 字节，0.24 秒，`%PDF` 头 + `%%EOF` 尾齐全，是有效 PDF。
- `Last-Modified` 抽样多为 2024–2025，个别对象在 2026-07 被重新上传；未发现大规模替换。

## 2. 「需要登录」说法的来源（实测澄清）

真实原因是**把几种不同的「被拒」混为一谈**：

1. **bucket 不允许列举，但允许读取已知对象**。访问
   `https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/?prefix=...` 返回
   `AccessDenied: Access denied by bucket policy`。这是 OSS 的 bucket policy 只放行「按对象名 GET」，
   不放行 `ListObjects`。agent 若去列目录就会看到 AccessDenied，容易误判为「要登录/要鉴权」。
2. **主站页面里的 `login` 字样与下载无关**。主站下载页 HTML 有 11 处 `login`，逐条查过语境，全是
   埋点脚本读的 cookie 名（`login_aliyunid`、`login_current_pk`），以及页面底部「Post a Suggestion」
   跳转 `account.alibabacloud.com/login/login.htm` —— 是**提建议**要登录，不是下载要登录。
3. **主站风控而非登录墙**。7 月报告记录主站对 `curl` 直抓有 x5sec 验证码，需真实浏览器绕过；
   被拦截时容易被笼统描述成「需要登录」。本次带浏览器 UA 直抓主站返回 200、1.8 MB，无拦截。
4. **另一条下载路径确实要会话授权**：WorkBuddy 项目资产盘（tdrive）的 `file_download` 需要当前账号会话。
   如果 agent 指的是从**云端资产盘**下载，那确实要登录——但这与 OSS 直链是两回事。
5. 中文帮助中心 `apsara-stack.aliyun.com` 的企业版在线手册部分可能需账号，也易被泛化。

> 简言之：**按已知 URL 直连 OSS 不需要任何登录**；需要登录的是「账户相关操作」和「WorkBuddy 资产盘会话」。

## 3. 更新情况

### 3.1 新批次（重要）

国际站下载页出现全新目录 `国际版文档/3816 2607/pdf 3/`：

| 项目 | 值 |
|---|---|
| 文件数 | **265 份** |
| 版本标识 | `V3.18.6-2607` |
| 文件标注日期 | **2026-07-31 ~ 2026-09-11**（集中在 08-28、08-31） |
| 语言 | 英文版（`Alibaba Cloud Apsara Stack ...`），我们已有 287 份是中文版 |
| 涉及产品 | 54 个（CDS、OpenTrek、PolarDB、云安全中心、EDAS、RocketMQ 等） |
| 与本地 421 条交集 | **0**，完全是新批次 |
| 可下载性 | 抽样 8 条全部 `206 application/pdf` + `%PDF` 头 |

清单已导出：`/workspace/apsara_stack_new_batch_2607.json`（含 version / filename / date / product / url）。

### 3.2 其他发现

- 中文专有云帮助中心 `apsara-stack.aliyun.com/notice/product` 的版本选择里有
  `v_3_18_6_20261030`、`v_3_18_6_20260730`（2026 年 10 月 / 7 月批次），比 7 月抓取晚，属另一套在线产品手册体系。
- 下载页还包含更多历史版本（`V3.12` / `V3.14.0` / `V3.16.2` / `V3.18.1` / `01_ApsaraStackEnterprise` 英文版），
  7 月用 `tags=,V3.18.6,V3.18.3,V3.18.2` 过滤掉了，不在我们清单范围内。
- **未发现**比 V3.18.6 更高的版本号（无 V3.18.7 / V3.19）。

## 4. 下载到本地

**可以，已实测。** 现有本地副本（沙箱 `/workspace`）：

| 内容 | 路径 |
|---|---|
| 287 份去重 PDF（按 10 个分类） | `/workspace/apsara_by_category/` |
| 287 份去重 PDF（按版本） | `/workspace/apsara_stack_docs/` |
| 完整 zip（分类目录，853 MB） | `/workspace/apsara_stack_by_category.zip` |
| 421 条直链清单 | `/workspace/oss_links.txt` / `.json` / `.csv` |
| 265 条新批次链接 | `/workspace/apsara_stack_new_batch_2607.json` |

复用方式：

```bash
# 重下旧清单（脚本自带断点续传、跳过 404）
cd /workspace && python3 download_apsara.py
# 或
wget -i oss_links.txt -P apsara_stack_docs/ -U "Mozilla/5.0" -nc
```

若要下载到**自己的电脑**：在 WorkBuddy 项目资产盘下载 `apsara_stack_by_category.zip`（853 MB），
或直接用浏览器打开 `oss_links.txt` 里的 URL 单份另存。

> ⚠️ 若要下载新的 265 份、或把它们补进项目资产盘，属于新的写入操作，需先确认再执行。

---

## 5. 英文版本核查（补充，2026-11-15）

**结论：有，而且官方下载页当前列出的 952 份 PDF 全部是英文版。**

### 5.1 现状对比

| 位置 | 语言 | 数量 |
|---|---|---|
| 本地 `/workspace/apsara_by_category/`、云端资产盘 10 个分类 | 中文（`阿里云 专有云 ...`） | 287 |
| 本地英文命名 PDF | — | **0** |
| 官方下载页当前列表 | 英文（`Alibaba Cloud Apsara Stack ...`） | **952** |

即：我们手上和资产盘里**只有中文版**；OSS 上另有一整套英文版，且中文直链与英文直链互不冲突、都可公开读取。

### 5.2 英文版构成（按 OSS 版本目录）

| 版本目录 | 份数 | 说明 |
|---|---:|---|
| `v3.18.6版本文档` | 287 | 与中文 287 份数量一致，是对应英文版；含 2026 年新日期，更新更频繁 |
| `3816 2607`（`v3.18.6-2607`） | 265 | 2026-07~09 新批次（见第 3 节） |
| `V3.18.3` | 123 | |
| `v3.18.2版本文档` | 57 | |
| `V3.12` / `v3.14.0` / `3.18.1版本文档` | 54 / 49 / 49 | 历史版本 |
| `v3.16.2_intl_en` / `v3.16.2版本文档` | 38 / 14 | 历史英文版 |
| 其余零散目录 | ~16 | 含 1 份 Red Hat OpenShift on Apsara Stack |
| **合计** | **952** | 日期跨度 2022-06-28 ~ 2026-09-11 |

- 其中 **506 份**是 2026 年及以后的文档。
- 文档类型词频对照（中文 287 vs 英文 V3.18.6 287）：产品简介 58 / Product Introduction 72、用户指南 88 / User Guide 79、开发指南 71 / Developer Guide 65、运维指南 66 / O&M Guide 67 —— 大体对应，但并非严格 1:1，英文版含部分独有文档。
- 抽样验证 6 份 `v3.18.6版本文档` 英文 PDF：全部 `206 application/pdf` + `%PDF` 头，可直接下载。

### 5.3 英文版清单

已导出 `/workspace/apsara_stack_en_links.json`（952 条，字段：version / product / filename / date / url）。
`apsara_stack_new_batch_2607.json`（265 条）是其中 `3816 2607` 批次的子集。

> 若要下载英文版到本地、或补进项目资产盘，属于新的写入操作，需先确认再执行。
