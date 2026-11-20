Alibaba Cloud  
Apsara Stack  
Time Series and Spatial-  
Temporal Database  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260827

**Table of Contents**

- [1.Lindorm](#section-1)
    - [1.1. Product details](#section-1-1)
    - [1.2. Product value](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.Lindorm

Lindorm is a cloud-native, multi-model, and hyper-converged database built for scenarios such as the Internet of Things (IoT), the Internet, and the Internet of Vehicles (IoV). It provides unified access to and converged processing of various data types, such as wide table, time series, text, object, stream, and spatial data. Lindorm is compatible with multiple open-standard interfaces and integrates with third-party ecosystem tools.

<a id="section-1-1"></a>

## 1.1. Product details

Lindorm is a cloud-native database service that supports multiple data models. You can use the Alibaba Cloud console to create Lindorm instances, upgrade engine versions, scale nodes, or release instances as needed.

**Instance**

An instance is the smallest unit of service that Lindorm provides. Different instance types offer different computing and storage capabilities. A single Lindorm instance can store and compute data for multiple models, such as wide table, time series, text, object, stream, and spatial data.

**Storage engines**

Lindorm supports storage engines such as the wide table engine, time series engine, search engine, and file engine. It is compatible with multiple open standard interfaces, such as HBase, Cassandra, S3, OpenTSDB, Solr, Hadoop Distributed File System (HDFS), and Kafka. Lindorm also provides capabilities such as SQL queries, time series processing, and text search and analysis.

**Network**

- Virtual private cloud

  A virtual private cloud (VPC) is a private network on the cloud. Different VPCs are logically isolated at Layer 2 to provide high security and performance. If Lindorm-cli is deployed on an ECS instance, you can connect to your Lindorm instance over a VPC for higher security and lower network latency.

- The Internet

  If an on-premises device needs to connect to a Lindorm instance, you can request a public endpoint to connect over the Internet. Connecting over the Internet may pose security risks. For higher security, connect over a VPC.

**Auto Scaling**

Lindorm supports Auto Scaling. This service automatically adjusts your computing and storage resources based on defined policies to help reduce infrastructure and operations and maintenance (O&M) costs.

- Lindorm storage resources support online scaling within seconds. Computing resources for the wide table, time series, and search engines support online scaling within minutes.

- Lindorm supports node upgrades and downgrades for each engine. This allows for rapid elastic scaling to efficiently handle peak workloads.

**Unified multi-model processing**

- Lindorm allows data to be shared between different models. For example, the search engine can act as an index for the wide table and time series engines, which speeds up multi-dimensional searches and analysis.

- Lindorm provides integrated processing capabilities, including data ingestion, storage, retrieval, computation, and analysis.

- Lindorm supports unified SQL access for cross-engine queries on multiple data models.

**Cold storage**

Lindorm supports a cold storage feature to reduce storage costs by storing cold data from your database. You can set a boundary between hot and cold data to automatically archive data from your tables into the appropriate storage tier.

**Secondary indexes**

The Lindorm wide table engine supports a high-performance native secondary index feature. This feature lets you create multiple index tables for a single primary table. Each index table can have a different storage policy, such as a specific compression algorithm or a hot and cold data separation policy. Lindorm ensures data consistency between the primary and index tables. Data in the index tables is updated automatically, which improves write efficiency.

**Data ecosystem service**

Lindorm uses Lindorm Tunnel Service (LTS) to import and migrate data. LTS is a data ecosystem service customized for Lindorm scenarios. It supports use cases such as data migration, real-time subscriptions, data lake offloading, data loading into data warehouses, active-active deployments, and backup and recovery.

**Cluster management system**

- The Lindorm wide table engine provides a cluster management system for intelligent operations and maintenance (O&M) of instances. This includes the following capabilities:

  - View information about an instance, such as capacity in each zone, server lists, table properties, and table sizes.

  - Manage database tables and namespaces.

  - Manage database accounts and permissions.

  - Run simple SQL statements to query data in the database.

  - View real-time monitoring metrics at multiple levels, including instances, groups, nodes, namespaces, and tables.

  - Perform health checks on instances and view inspection reports to quickly analyze and locate issues.

- The Lindorm search engine provides a cluster management system to manage index tables. This includes operations such as creating, deleting, and updating configurations.

<a id="section-1-2"></a>

## 1.2. Product value

Lindorm is built on a cloud-native architecture. It provides elastic scaling, low cost, high performance, ease of use, high availability, high reliability, and an open ecosystem.

**Elastic scaling**

- The fully distributed architecture decouples storage and compute. This allows for the independent elastic scaling of computing and storage resources.

- You can scale storage resources online within seconds. Computing resources, such as LindormTable, LindormTSDB, and the search engine, can be scaled online within minutes.

**Low cost**

- Offers multiple storage specifications, such as compute-optimized, standard, and storage-optimized, to provide cost-effective solutions for various scenarios.

- Multiple engines share a unified storage pool, which reduces storage fragmentation and lowers usage costs.

- The built-in, deeply optimized compression algorithms provide a data compression ratio of over 10:1, which is an improvement of more than 50% compared to Snappy.

- Built-in adaptive encoding is tailored for different data types, allowing for fast data queries without decoding.

- Supports intelligent hot and cold data separation, allowing you to use a mix of storage specifications to significantly reduce overall data storage costs.

**High performance**

- LindormTable: Supports a throughput of tens of millions of concurrent operations and storage of hundreds of petabytes. Its performance is 3 to 7 times higher than open-source HBase, and its P99 latency is one-tenth that of open-source HBase.

- LindormTSDB offers write and query performance that is 1.3 times that of InfluxDB and 5 to 10 times that of OpenTSDB.

- The search engine is deeply optimized based on the Lucene engine, and its overall performance is 30% better than open-source Solr or ES.

**Ease of use**

- Compatible with multiple open standard interfaces, such as HBase, Cassandra, Phoenix, OpenTSDB, and Solr, allowing for seamless service migration.

- Provides a fully managed cloud service that requires no Operations and Maintenance (O&M).

- You can use the graphical user interface (GUI) for simple system administration and data access.

**High availability**

- The distributed, multi-replica architecture enables clusters to automatically recover from disasters.

- Supports cross-zone disaster recovery with strong consistency and meets financial-grade availability standards.

- Supports Global Distributed Cache deployments.

**High reliability**

- Multi-replica storage at the underlying layer ensures high data reliability.

- Provides enterprise-grade backup capabilities.

**Open ecosystem**

- Supports smooth online data migration from systems such as MySQL, HBase, and Cassandra.

- Seamlessly integrates with compute engines such as Spark, Flink, Data Lake Analytics (DLA), and MaxCompute.

- Seamlessly subscribes to data from log channels, such as Kafka and Simple Log Service (SLS), and provides fast data processing.

- You can use Lindorm Stream to subscribe to incremental data changes in Lindorm in real time for custom consumption.

<a id="section-1-3"></a>

## 1.3. Scenarios

Lindorm is a cloud-native multi-model database developed by Alibaba Cloud. It is designed for low-cost storage and analysis of massive multi-model data and serves as a data foundation for the Internet of Everything. Lindorm provides single-millisecond response times and supports horizontal scaling to petabytes of storage and tens of millions of queries per second (QPS). It is a key component of Alibaba's core services and is used in scenarios such as big data, finance, the Internet of Vehicles, and Internet services.

**Best practices within Alibaba Group**

Lindorm is widely used in core business operations within Alibaba Group. It stores and analyzes real-time data for applications such as Taobao messages, Alipay bills, and Cainiao logistics information. Lindorm offers Alibaba Group low cost, high concurrency, and elastic scaling.

**Big data scenarios**

Lindorm supports low-cost storage, fast batch imports, and real-time access to massive amounts of data. It provides efficient channels for both incremental and full data. Lindorm easily integrates with big data platforms, such as Spark and MaxCompute, to perform large-scale offline analysis. These capabilities provide businesses with advantages such as low cost, fast imports, and elastic scaling.

**Finance and retail**

Lindorm stores massive order records from financial transactions and important data for financial risk control, such as user events, profiles, rule models, and device fingerprints. It provides a low-cost, high-concurrency, flexible, and reliable solution that meets the real-time data storage requirements of financial transaction and risk control scenarios.

**Internet of Vehicles**

Lindorm stores important data for the Internet of Vehicles, such as driving trajectories, vehicle status, and precise location information. It provides a low-cost, elastic, flexible, and reliable solution for data storage and processing in scenarios such as ride-hailing, logistics transportation, and new energy vehicle monitoring.

**Internet and social media**

Lindorm stores important data for social media applications, such as chats, comments, posts, and likes. By offering ease of development, high availability, and low latency, Lindorm significantly reduces user access wait times and provides a stable and reliable social feed system.

<a id="section-1-4"></a>

## 1.4. Features

**Feature**

**Feature**

**Description**

**category**

Create an

A base platform can have only one instance. The instance is created with

instance

the platform.

Scale-out

Lets you scale out instances using scale-out packages.

Upgrade the minor engine

Upgrade packages are provided by the product and released as hotfixes.

version

Instance managem

Upgrade

ent

or

Lets you change instance types, including upgrades and downgrades, and

downgrad

modify storage capacity.

e an instance

Release an

Lets you release existing instances.

instance

View basic instance

View detailed information for an instance in the console. This includes

informatio

basic information, running status, and detailed configuration.

n

Instance

Displays basic instance information in a list. The list includes the instance

list

name, status, and network operation entries.

Create an

Lets you create privileged and standard accounts.

account

Modify account

Lets you modify the permissions of existing accounts.

permissio ns

Service authorizat

Authorize a service account to let helpdesk staff provide technical support.

ion

Account

account

managem ent

Reset a

Lets you reset account passwords.

password

Reset a privileged

Lets you reset privileged accounts.

account

Delete an

Lets you delete specified accounts.

account

Full

Perform full backups of your data. This requires manual deployment and

backup

can be managed from the console.

Data

Increment

Perform incremental backups of your data. This requires manual

backup

al backup

deployment and can be managed from the console.

<table>
  <tr>
    <td rowspan="2">Database managem ent</td>
    <td>Create a namespac e</td>
    <td>Lets you create namespaces.</td>
  </tr>
  <tr>
    <td>Delete a namespac e</td>
    <td>Lets you delete existing namespaces.</td>
  </tr>
  <tr>
    <td>Monitorin g and alerting</td>
    <td>View metrics</td>
    <td>View monitoring metrics in the console. Metrics include the number of timelines, data points written per second, and disk usage (Master disk usage). You can also set alert rules for these metrics.</td>
  </tr>
  <tr>
    <td>Data migration</td>
    <td>HBase data migration</td>
    <td>Migrate data from a self-managed HBase cluster to Alibaba Cloud HBase.Both full and incremental migration are supported.</td>
  </tr>
  <tr>
    <td rowspan="2">Import and export</td>
    <td>Write data using Blink</td>
    <td>Lets you write data using Blink.</td>
  </tr>
  <tr>
    <td>Export data to MaxComp ute</td>
    <td>Lets you export data to MaxCompute.</td>
  </tr>
  <tr>
    <td>Disaster recovery</td>
    <td>Cross-data center disaster recovery</td>
    <td>Provides high availability (HA) disaster recovery across data centers.</td>
  </tr>
  <tr>
    <td>Data security</td>
    <td>Configure a whitelist</td>
    <td>Configure a whitelist for an instance to allow access from external devices.</td>
  </tr>
  <tr>
    <td rowspan="2">Kernel features</td>
    <td>Dynamic columns</td>
    <td>The LindormTable engine supports dynamic columns. This means you can write data to and query columns that were not explicitly defined when the table was created.</td>
  </tr>
  <tr>
    <td>Secondary index</td>
    <td>Provides native support for secondary indexes.</td>
  </tr>
  <tr>
    <td>Hardware support</td>
    <td>Support for domestic hardware</td>
    <td>• Supports Hygon 2, 3, and 4 chips.<br>• Supports Kunpeng chips.<br>• Supports Phytium chips.<br>• Supports Yitian chips.<br>• Supports mixed deployment with the x86 instruction set.<br>• Supports mixed deployment with the Arm instruction set.</td>
  </tr>
</table>
