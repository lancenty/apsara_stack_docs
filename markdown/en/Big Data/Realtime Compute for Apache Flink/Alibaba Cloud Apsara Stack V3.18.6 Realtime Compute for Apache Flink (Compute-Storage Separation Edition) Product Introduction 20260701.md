Alibaba Cloud  
Apsara Stack  
Realtime Compute for Apache  
Flink (Compute-Storage  
Separation Edition) Product  
Introduction  
Product Version: V3.18.6  
Document Version: 20260701

**Table of Contents**

- [1.Product details](#section-1)
- [2.Benefits](#section-2)
- [3.Scenarios](#section-3)
- [4.Features](#section-4)

<a id="section-1"></a>

# 1.Product details

Alibaba Cloud Realtime Compute for Apache Flink supports features including data ingestion and storage, data development, data O&M, and automatic tuning.

**Data ingestion and storage**

A prerequisite for any big data analysis system is that data must be ingested into the big data system. To maximize compatibility with customers' existing streaming storage systems, Alibaba Cloud Realtime Compute for Apache Flink integrates with multiple upstream streaming storage services, such as DataHub, Log Service, Tablestore, and Message Queue. Customers can leverage their existing streaming data storage without needing to perform separate data ingestion or data integration tasks.

**Data development**

- Integrated SQL assistance features

  - Flink SQL syntax checking

    After modifying text in the IDE, click **Validate** to trigger SQL syntax checking. If errors are found, the IDE displays the line number, column number, and reason for each error.

  - Flink SQL code hinting

    When writing Flink SQL, the IDE provides hints for keywords, built-in functions, and SQL auto-completion.

  - Flink SQL syntax highlighting

    The IDE applies distinct colors to Flink SQL keywords to visually differentiate structural elements of the SQL statement.

- DDL generation assistance

  Generating DDL statements for Realtime Compute typically involves mechanical translation — manually converting the DDL of a target data store into Realtime Compute-compatible

  <ol type="I" start="1050">

  <li>

  Realtime Compute provides tools to assist with DDL generation, reducing the

  </li>

  </ol>

  complexity of manually writing streaming jobs, lowering the error rate in SQL authoring, and ultimately improving productivity for real-time computing tasks. Users can select a template on the development page to auto-generate DDL statements. Running the template then generates and displays the corresponding table schema in the Schema view.

- Support for standard SQL

  Use standard SQL to perform real-time data cleansing, statistical aggregation, and data analysis. The system supports common aggregate functions and enables join queries between streaming and static data.

**Data O&M**

Alibaba Cloud Realtime Compute provides O&M and monitoring capabilities including job status, data throughput curves, failover events, checkpoints, JobManager metrics, TaskExecutor metrics, lineage tracking, and property parameter inspection.

**Automatic tuning**

This feature helps users optimize job parallelism and resource allocation more effectively, provided that all operators and upstream/downstream components of the streaming job meet performance and stability requirements. It globally optimizes job performance to resolve tuning issues such as insufficient throughput, end-to-end backpressure, and resource waste.

**High availability and high security**

Built on a compute-storage separation architecture, the system support same-city high availability disaster recovery and highly secure multi-tenant isolation.

<a id="section-2"></a>

# 2.Benefits

Compared with other realtime compute products, Alibaba Cloud Realtime Compute for Apache Flink offers strong competitiveness. You can leverage the following advantages to solve your business challenges in realtime big data analysis.

**Powerful realtime processing capabilities**

Alibaba Cloud Realtime Compute integrates multiple end-to-end features to simplify end-to-end realtime computing development for users:

- Powerful realtime compute engine:

  - Alibaba Cloud Realtime Compute provides standard Flink SQL and supports automatic recovery in various failure scenarios to ensure data processing accuracy during failures.

  - Supports multiple built-in functions for strings, time, statistics, and other types.

  - Enables precise control of computing resources to fully guarantee job isolation.

  - Provides compute engines for Flink 1.17, Flink 1.15, and Flink 1.13. Python jobs (ARM) support only Flink 1.17.

- Key performance metrics exceed those of open-source Flink by 3 to 4 times. Data compute latency is optimized to the second or even millisecond level. A single job can achieve throughput at the million level, and a single cluster can scale to thousands of nodes.

- Deeply integrates with various cloud data storage systems, including DataHub, Simple Log Service, ApsaraDB RDS, Tablestore, AnalyticDB for MySQL. No additional data integration work is required. Alibaba Cloud Realtime Compute for Apache Flink can directly read from and write to these products.

**Excellent streaming development experience**

- Supports standard Flink SQL.

  Realtime Compute uses built-in functions for strings, time, statistics, and other calculations to replace inefficient and complex Flink Java APIs with simple Flink SQL, enabling more BI and operations personnel to perform realtime big data analysis and processing using basic Flink SQL, thus democratizing realtime big data processing.

  The current external interface of Realtime Compute is defined as Flink SQL/UDF. It provides an all-in-one development tool for streaming data analysis, statistics, and processing. The target users are primarily data warehouse developers and data analysts who prefer not to engage deeply in low-level code development and instead wish to write simple realtime SQL to fulfill their streaming data analysis tasks.

- Provides an end-to-end streaming data processing solution

  Includes auxiliary suites for different stages such as data development, data O&M, and monitoring and alerting.

- Supports automatic fault tolerance for server hard disk failures within the cluster

  Supports hot-swappable hard disks. Business recovery time for failed disks is less than two minutes.

- The platform adopts a multi-node cluster architecture

  Management nodes within the platform support high availability. Routine O&M management node failures do not affect normal business operations.

**Low labor and cluster costs**

The highly optimized SQL execution engine generates compute tasks that are more efficient and cost-effective than manually written native Storm tasks. Whether in development cost or runtime cost, Alibaba Cloud Realtime Compute is significantly lower than open-source streaming frameworks. By using it, you can focus entirely on your business and rapidly achieve market goals without needing to write complex Java code for Storm tasks. Alibaba Cloud assumes all costs related to debugging, testing, tuning, deployment, and subsequent O&M of open-source software such as Storm and Zookeeper.

Without affecting runtime performance, the system supports inconsistent CPU, hard disk, memory, and NIC specifications within a single component cluster, maximizing compatibility with existing equipment.

<a id="section-3"></a>

# 3.Scenarios

Alibaba Cloud Realtime Compute for Flink is suitable for scenarios such as real-time extract, transform, and load (ETL) and index building, real-time statistics and analytics, real-time machine learning platforms, and real-time event processing.

**Real-time ETL & index building**

Realtime Compute uses its various data tunnels and flexible SQL processing capabilities to clean, merge, and structure streaming data in real time. Realtime Compute effectively supplements and optimizes offline data warehouses by providing a channel for real-time data transmission.

**Real-time statistics & analytics**

Realtime Compute collects and processes streaming data sources, and monitors and displays various metrics in real time. This enables real-time, data-driven operations. For example:

- Real-time statistics for page views (PVs) and unique visitors (UVs).

- Statistics on the average traffic flow through a checkpoint every 5 minutes.

- Statistics and display of dam pressure data.

**Real-time machine learning platform**

This platform helps data analysts and application developers complete the end-to-end process, from data processing and feature engineering to model training and prediction.

**Real-time event processing**

You can detect and analyze system, user, and business behavior in real time to identify malicious activities. For example:

- Display user behavior dashboards, such as transaction and user dashboards.

- A site-wide transaction curve graph helps operations and technical staff understand the current transaction status. If transactions fluctuate abnormally, such as with a sudden drop, an alert is triggered immediately. This allows staff to investigate the issue and reduce the business impact.

- Monitor major sales promotions, such as Double 11 and 618, in real time. Operations staff can use real-time metrics to quickly decide whether to change the promotion strategy.

- Set up rule-based alerts to detect specific patterns of financial theft in online payments.

<a id="section-4"></a>

# 4.Features

This topic describes the features of Real-time Compute for Apache Flink.

**Feature**

**Sub-**

**Feature**

**Description**

**category**

**feature**

DataStream

Supports DataStream jobs.

job

SQL job

Supports SQL jobs.

SQL editor

Provides an SQL editor.

UDF

Supports user-defined functions (UDFs).

Peak job

A single job in a single cluster can reach a peak

throughput

throughput of up to 8 million records per second.

Supports manual and intelligent tuning for job resources and parallelism:

- **Manual tuning:** Provides operator-level settings to

Job resource

adjust resources such as CPU, memory, and

and

parallelism.

parallelism tuning

- **Intelligent tuning:** You can adjust global job resources, and a backend AI system automatically optimizes resource allocation based on the job's real-time operational status.

Job

StreamSQL

Provides a comprehensive StreamSQL development

manageme

developmen

kit with auto-complete, syntax highlighting, and

nt

t kit

syntax checking.

Console

Concurrent

A single cluster supports at least 2,400 concurrent

job capacity

jobs.

Complex

Complex Event Processing (CEP) with dynamic rules

event

decouples developers from policy analysts by

processing

separating the application framework from business

(CEP) with

rules. Flink automatically loads updated rules to

dynamic

ensure business continuity.

rules

Fast recovery

Jobs recover quickly from a single checkpoint after a

from single-

failure.

point failures

Job runtime

Runtime parameters for stream jobs let you configure

parameters

the Time to Live (TTL) for state data.

Metadata

Built-in

Supports Apache Paimon table creation through the

manageme

catalog for

built-in catalog.

nt

Paimon

Built-in

Built-in

Provides more than 30 built-in connectors for a wide

connectors

connectors

range of data sources.

User-

Custom

Users can upload custom connectors for specific data

defined

connectors

sources.

connectors

Log-based automatic

Supports automatic metadata discovery and

Change

metadata

management through a catalog. Combined with the

data

discovery

Create Table As Select (CTAS) syntax, you can

capture

and

synchronize data and automatically propagate

(CDC)

managemen

schema changes with a single line of SQL.

t

Incremental synchroniza

Supports incremental data synchronization.

tion

Breakpoint

Supports resuming data synchronization from

resume

breakpoints.

Full

Connectors

synchroniza

Supports full data synchronization.

tion

Full and incremental

Enables unified data synchronization for both full and

integrated

incremental reads.

reads

Flink CDC

CTAS for database

Use CTAS syntax with regular expressions to merge

and table

and synchronize data from sharded databases and

sharding

tables into a downstream data warehouse.

synchroniza tion Dynamic

Dynamically add new source tables to a

table

synchronization job without affecting existing table

addition

states or requiring a full resynchronization.

CDAS for full

Enables full database synchronization using CDAS

database

syntax and a catalog.

synchroniza tion

Leverages a distributed computing framework to

Compute

Cluster

provide stream processing services that can be scaled

cluster

scaling

on demand. A compute cluster can scale up to 2,400

scale

capability

nodes.

Mixed x86

Supports mixed deployments of Intel and Hygon CPUs

deployment

within the same cluster.

Scalability

Cross-chip architecture

Heterogene ous cross-

Supports mixed deployments of heterogeneous x86

chip

and ARM architectures within the same cluster.

deployment

Supports on-demand hot scaling (scaling up or down)

Hot scaling

Scaling

of resources within a single cluster without affecting

support

online services.

Resource-level fault detection

Fault

Provides fault detection and automatic job migration

and

detection

for high CPU, I/O, memory, and disk utilization.

automatic job migration

Non-

Online job

disruptive

Provides online debugging for stream computing jobs

debugging

online job

without disrupting the production environment.

debugging

O&M and monitoring

The job O&M dashboard displays underlying metrics,

Job O&M

Job O&M

such as traffic and resource usage, for you to monitor

dashboard

dashboard

job health.

Capacity level

Capacity

monitoring

Supports capacity usage monitoring and

monitoring

and

management.

managemen t

<table>
  <tr>
    <td rowspan="3">Security</td>
    <td>Secret manageme nt</td>
    <td>Secret managemen t for SQL jobs</td>
    <td>Supports secret management for SQL jobs.</td>
  </tr>
  <tr>
    <td>Access control</td>
    <td>IP address range for allowlist</td>
    <td>Lets you configure access control allowlist using IP address ranges.</td>
  </tr>
  <tr>
    <td>Log auditing</td>
    <td>Search operation logs</td>
    <td>Search operation logs through the visual interface in the log center.</td>
  </tr>
  <tr>
    <td>High availability</td>
    <td>Disaster recovery</td>
    <td>Intra-city disaster recovery</td>
    <td>Supports namespace-level intra-city disaster recovery.You can also create non-disaster recovery instances in the secondary data center.</td>
  </tr>
  <tr>
    <td>Network</td>
    <td>Service IP address</td>
    <td>Dual-stack support for service virtual IP (VIP) addresses</td>
    <td>Supports IPv6 and IPv4 in dual-stack mode for service virtual IP (VIP) addresses.</td>
  </tr>
</table>
