Alibaba Cloud  
Apsara Stack  
Data Transmission Service  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260831

**Table of Contents**

- [1.What is DTS?](#section-1)
    - [1.1. Overview](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.What is DTS?

Data Transmission Service (DTS) is a data service that is provided by Alibaba Cloud. DTS supports data transmission between various types of data sources, such as relational databases and big data systems. Compared with traditional data migration or synchronization tools, DTS provides diverse features and high performance, security, reliability, and ease of use. DTS helps you simplify data transmission and focus on your application development.

<a id="section-1-1"></a>

## 1.1. Overview

This topic provides an overview of the features of Data Transmission Service (DTS), such as data synchronization, data migration, and change tracking.

**Data synchronization**

You can use DTS to synchronize data between data sources in real time.

The following table describes the capabilities supported by the data synchronization feature.

| Capability | Description |
| --- | --- |
| Add or remove the objects to be synchronized | You can add or remove the objects to be synchronized at any time when a data synchronization task is running. |
| View and analyze the synchronization performance | DTS provides trend charts that allow you to view and analyze the performance of your data synchronization tasks. The synchronization performance is measured based on bandwidth, records per second (RPS), and synchronization latency. |
| Monitor data synchronization tasks | DTS allows you to monitor the status of data synchronization tasks. If the threshold for synchronization latency is reached, the system sends an alert notification to you. You can set the alert threshold based on the sensitivity of your business to synchronization latency. |

**Data migration**

You can use DTS to migrate data between homogeneous or heterogeneous data sources. DTS provides the following extract, transform, and load (ETL) capabilities: object name mapping for columns, tables, and databases, and data filtering. These capabilities allow you to migrate data between various types of data sources with ease.

DTS uses online migration. You need to only configure the source instance, the destination instance, and the objects to be migrated. DTS automatically completes the entire data migration process. You can select all of the supported migration types to minimize the impact of online data migration on your services. However, you must ensure that DTS servers can connect to both the source and destination instances.

The following table describes the ETL capabilities supported by the data migration feature.

| Capability | Description |
| --- | --- |
| Enable object name mapping for columns, tables, and databases | You can migrate data between two columns, tables, or databases that have different names. |
| Filter the data to be migrated | You can set SQL conditions to filter the data to be migrated in a specific table. For example, you can specify a time range to migrate only the latest data. |

**Change tracking**

DTS allows you to track incremental data in databases in real time. You can consume the tracked data based on your business requirements.

The following table describes the capabilities supported by the change tracking feature.

| Capability | Description |
| --- | --- |
| Add or remove the objects for change tracking | You can add or remove the objects for change tracking at any time when a change tracking task is running. |
| View the tracked data | You can view the incremental data that is tracked by a change tracking task in the DTS console. |
| Modify the consumption checkpoint | You can modify the consumption checkpoint at any time. |
| Monitor change tracking tasks | DTS allows you to monitor the status of change tracking tasks. If the threshold for consumption latency is reached, the system sends an alert notification to you. You can set the alert threshold based on the sensitivity of your business to consumption latency. |

**ETL**

DTS provides the ETL feature. When you configure a data migration or synchronization task, you can rename databases, tables, and columns in the destination instance and set conditions to filter specific data.

The following table describes the capabilities supported by the ETL feature.

| Capability | Description |
| --- | --- |
| High computing effectiveness | Integrated with the powerful capabilities of DTS in collecting streaming data from databases, the ETL feature ensures data accuracy and provides high computing effectiveness in the industry. |
| Flexible task monitoring and management | You can monitor and manage ETL tasks in the DTS console. For example, you can start a task, stop a task, and view task details. |

**Data consistency**

DTS uses the data reading module, data loading module, data verification feature, and resumable transmission feature to ensure data consistency between the source and destination databases.

<a id="section-1-2"></a>

## 1.2. Benefits

Compared with third-party data migration or synchronization tools, Data Transmission Service (DTS) supports diverse data transmission scenarios and ensures high performance, security, and reliability. DTS allows you to create and manage tasks with high efficiency.

**Multiple transmission modes**

- DTS supports multiple data transmission modes, including data migration, data synchronization, and change tracking.

  > **Note**
  >
  > In the change tracking and data synchronization modes, data is
  >
  > transmitted in real time.

- In the data migration mode, data is migrated between databases without interrupting application operations. The application downtime during data migration is reduced to a few minutes.

**High performance**

- DTS uses servers with high specifications to ensure the performance of each data synchronization or migration instance.

- Compared with traditional data synchronization tools, DTS provides better synchronization performance. You can use DTS to concurrently synchronize transactions and the incremental data of a single table.

- DTS supports concurrent data capture and data write. The data capture and data write modules are decoupled to improve the overall throughput.

- To implement concurrent migration between tables and within tables, DTS applies a variety of intelligent sharding policies on the tables to be migrated. This ensures parallel data synchronization and improves the processing efficiency of a large number of databases and a large amount of data in a single table.

- DTS uses efficient network protocols and data compression technology to reduce the amount of data on long-distance connections and minimize data transmission latency. Multiple TCP connections are deployed to improve the synchronization performance and stability in abnormal network environments.

- DTS provides horizontal scaling capabilities. You can improve capacity by increasing the number of tasks.

- At the underlying layer of DTS, multiple measures are taken to improve performance.

**High security and reliability**

- DTS provides a 24 × 7 mechanism for validating data accuracy in some instances to discover and rectify inaccurate data. This helps ensure reliable data transmission.

- DTS is deployed based on clusters. If a node in a cluster is down or faulty, the control center moves all tasks from this node to another healthy node in the cluster within seconds.

- Secure transmission protocols and tokens are used for authentication across DTS modules to ensure reliable data transmission.

- DTS supports the deployment of multiple data centers in the same city or across cities. If one of the data centers fails, you can quickly switch your workloads to another data center.

**Ease of use**

- The DTS console is a GUI that provides a wizard-like process to assist you in creating tasks for various scenarios.

- To facilitate task management, the DTS console displays task information such as status, progress, and performance.

- DTS supports resumable transmission and monitors task status on a regular basis. If DTS detects a network failure or system error, DTS automatically fixes the failure or error and restarts the task. If the failure or error persists, you can manually troubleshoot and restart the task in the DTS console.

<a id="section-1-3"></a>

## 1.3. Scenarios

Data Transmission Service (DTS) is applicable to scenarios such as interruption-free data migration, accelerated access to global services, geo-disaster recovery, and active geo-redundancy.

**Interruption-free data migration**

Traditional migration tools have many disadvantages. For example, these tools cannot ensure data consistency, require that services be suspended for a long time, and even have a great impact on the business during data migration. DTS provides an interruption-free data migration solution that minimizes the service downtime to minutes.

The interruption-free data migration process involves schema migration, full data migration, and incremental data migration. In the incremental data migration phase, data is synchronized between the source and destination instances in real time. You can validate the services in the destination instance, and switch your services to the destination instance after the validation is complete. The entire system is then eventually migrated.

> **Note**
>
> Throughout the migration process, you may experience service interruptions
>
> only when the services are switched from the source instance to the destination instance.

**Accelerated access to global services**

In traditional architectures, if services with widely distributed users, such as global services, are deployed in only one region, users in other regions have to access the services remotely, resulting in high access latency and poor user experience. DTS synchronizes data from the center to various cells in real time. Read requests of users in different regions can be routed to the nearby cells to avoid remote access. This way, the access latency is reduced, and the access to global services is accelerated.

**Quick building of a custom BI system**

Self-managed business intelligence (BI) systems are difficult to manipulate and cannot meet increasing requirements for real-time capabilities. Alibaba Cloud provides comprehensive BI systems. DTS allows you to synchronize data in real time from self-managed databases to Alibaba Cloud BI storage systems, such as MaxCompute, AnalyticDB, and Realtime Compute for Apache Flink. DTS helps you build a custom BI system that meets your business requirements on Alibaba Cloud.

**Real-time data analysis**

To implement real-time data analysis without affecting online services, you need to synchronize service data to an analysis system in real time. For this reason, acquiring service data in real time becomes essential. The change tracking feature of DTS helps you acquire real-time incremental data without affecting online services and synchronize the data to the analysis system by using the SDK for real-time data analysis.

**Lightweight cache update policies**

DTS provides the change tracking feature that can be used to track the incremental data in databases in an asynchronous manner and update the cached data. This way, data integrity is ensured, and lightweight cache update policies are implemented.

Cache update policies offer the following benefits:

- Quick update with low latency

  Cache invalidation is an asynchronous process, and updated data is directly returned after the database update is complete. For this reason, you do not need to consider the cache invalidation process. The entire update process is quick with low latency.

- Simple and reliable applications The complex doublewrite logic is not required for your applications. You need to only start asynchronous threads to track incremental data and update cached data.

- Application updates without performance degradation

  DTS tracks incremental data by parsing incremental logs in databases. This does not affect the performance of your business and databases.

**Business decoupling with asynchronous communication between different types of business logic**

You can use the change tracking feature of DTS to decouple different types of business logic. This is achieved by means of real-time notifications and asynchronous communication between different types of business logic. This makes the core business logic simple and reliable.

**Horizontal scaling of the read capability**

A single database instance may not have sufficient resources to deal with a large number of read requests. To scale out the read capability and relieve the pressure on the database instance, you can use the real-time data synchronization feature of DTS to create read-only instances and distribute read requests across these read-only instances.

<a id="section-1-4"></a>

## 1.4. Features

This topic describes the features of Alibaba Cloud Data Transmission Service (DTS) to help you quickly understand the product capabilities.

**Feature category**

**Description**

Db2 for i migration to

Supports schema migration, full data migration, and

MySQL

incremental data migration.

Migrate data from

Supports schema migration, full data migration, and

Db2 for i to PolarDB

incremental data migration.

for MySQL

Db2 for LUW migration to

Supports schema migration, full data migration, and

AnalyticDB

incremental data migration.

PostgreSQL

Migrate data from

Supports schema migration, full data migration, and

Db2 for LUW to

incremental data migration.

PolarDB for PostgreSQL

Migrate data from

Supports schema migration, full data migration, and

Db2 for LUW to

incremental data migration.

PolarDB for MySQL

- Supports schema migration, full data migration, and

Migrate data from

incremental data migration.

PolarDB for MySQL to

- Supports self-managed MySQL versions 5.1, 5.5, 5.6, and

MySQL

5.7.

- Supports full data migration and incremental data

Migrate data from

migration.

PolarDB for MySQL to Kafka

- Supports self-managed Kafka versions 0.1 to 2.7.

MaxCompute

Supports schema migration and full data migration.

migration to MySQL

- Only self-managed MongoDB database instances are

Data migration

supported as source and destination.

between MongoDB instances

- Supported MongoDB database versions are 3.0, 3.2, 3.4, 3.6, 4.0, or 4.2.

- MySQL versions 5.1 to 5.7.

MySQL migration to

- RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

PolarDB-X 1.0

- Supports full data migration and incremental data migration, but does not support schema migration.

Migrate data from

Supports schema migration, full data migration, and

MySQL to PolarDB-X

incremental data migration.

2.0

- Self-managed MySQL versions 5.1 to 5.7, RDS MySQL

MySQL migration to

versions 5.5, 5.6, 5.7.

AnalyticDB

- Supports schema migration, full data migration, and

PostgreSQL

incremental data migration.

- Self-managed MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7.

- Supports schema migration, full data migration, and incremental data migration.

- Kafka requires public network or private network access, and must be able to communicate with DTS. Select the

MySQL migration to

public network access method and enter the public or

Kafka

private IP address.

- Self-managed Kafka versions 0.10 to 2.0 over public network.

- Self-managed MySQL versions 5.1 to 5.7, RDS MySQL

Data migration

versions 5.5, 5.6, 5.7.

between MySQL

- Supports schema migration, full data migration, and

instances

incremental data migration.

- Oracle versions 9i, 10g, 11g.

MySQL migration to

- MySQL versions 5.1 to 5.7.

Oracle

- Supports schema migration, full data migration, and incremental data migration.

- Supports MySQL versions 5.5, 5.6, 5.7, 8.0.

MySQL migration to

- Supports PostgreSQL versions 10.x, 11.x, 12.x, 13.x.

PostgreSQL

- PostgreSQL must be accessed as a self-managed database over public network.

- Oracle versions 9i, 10g, 11g.

Oracle migration to AnalyticDB MySQL

- Supports full data migration and incremental data

2.0

migration.

- Oracle versions 9i, 10g, 11g.

Oracle migration to AnalyticDB MySQL

- Supports schema migration, full data migration, and

3.0

incremental data migration.

- Oracle versions 9i, 10g, 11g.

Oracle migration to

- Supports schema migration, full data migration, and

AnalyticDB

incremental data migration.

PostgreSQL

- Oracle versions 9i, 10g, 11g.

Oracle migration to

- RDS MySQL versions 5.1 to 5.73 attached to PolarDB-X 1.0.

PolarDB-X 1.0

- Supports full data migration and incremental data migration, but does not support schema migration.

- Oracle versions 9i, 10g, 11g.

- MySQL versions 5.1 to 5.7.

Oracle migration to

- Supports schema migration, full data migration, and

MySQL

incremental data migration.

- Oracle versions 9i, 10g, 11g.

Data migration between Oracle

- Supports schema migration, full data migration, and

instances

incremental data migration.

- Oracle versions 9i, 10g, 11g.

Oracle migration to

- Supports schema migration, full data migration, and

PolarDB for

incremental data migration.

PostgreSQL (Compatible with

- PolarDB for PostgreSQL (Compatible with Oracle) requires

Oracle)

public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address.

- Oracle versions 9i, 10g, 11g.

Oracle migration to

- Supports schema migration, full data migration, and

PostgreSQL

incremental data migration.

- Oracle versions 9i, 10g, 11g.

Oracle migration to

- Supports schema migration, full data migration, and

PPAS

incremental data migration.

- Self-managed Kafka versions 0.10 to 2.0 over public network.

- Supports schema migration, full data migration, and incremental data migration.

Oracle migration to Kafka

- Oracle versions 9i, 10g, 11g, 12g, 18c, 19c.

- RAC access only supports public network method, and leased line access only supports configuring one of the VIPs.

- Oracle versions 9i, 10g, 11g.

- Supports schema migration, full data migration, and incremental data migration.

- PolarDB for PostgreSQL (Compatible with Oracle) requires public network or private network access, and must be

Oracle migration to

Data

able to communicate with DTS. Select the public network

PostgreSQL

migration

access method and enter the public or private IP address.

- PostgreSQL versions 10.x, 11.x, 12.x require public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address.

- Oracle versions 9i, 10g, 11g, 12c, 18c, 19c.

Oracle to CCB streaming collection

- Supports full data migration and incremental data

SDK

migration.

Migrate data from

Supports schema migration, full data migration, and

PolarDB for MySQL to

incremental data migration.

MySQL

- Self-managed Kafka versions 0.10 to 2.0 over public network.

PolarDB for PostgreSQL

- Only supports incremental data migration.

(Compatible with

- PolarDB for PostgreSQL (Compatible with Oracle) needs to

Oracle) migration to

be accessed as a self-managed database over public

Kafka

network, by entering the IP and Port of PolarDB for PostgreSQL (Compatible with Oracle) for connection.

- PolarDB for PostgreSQL (Compatible with Oracle) needs to be accessed as a self-managed database over public network, by entering the IP and Port of PolarDB for

PolarDB for

PostgreSQL (Compatible with Oracle) for connection.

PostgreSQL (Compatible with

- Self-managed Oracle versions 9i to 19c over public

Oracle) migration to

network.

Oracle

- Supports full and incremental data migration, but does not support schema migration.

- PolarDB for PostgreSQL (Compatible with Oracle) needs to

Data migration

be accessed as a self-managed database over public

between PolarDB for

network, by entering the IP and Port of PolarDB for

PostgreSQL

PostgreSQL (Compatible with Oracle) for connection.

(Compatible with

- Supports schema migration, full data migration, and

Oracle) instances

incremental data migration.

PolarDB-X 2.0 migration to

Supports schema migration, full data migration, and

AnalyticDB

incremental data migration.

PostgreSQL

PolarDB-X 2.0

Supports schema migration, full data migration, and

migration to Kafka

incremental data migration.

PolarDB-X 2.0

Supports schema migration, full data migration, and

migration to MySQL

incremental data migration.

Data migration

Supports schema migration, full data migration, and

between PolarDB-X

incremental data migration.

2.0 instances

PostgreSQL

Supports schema migration, full data migration, and

migration to PolarDB

incremental data migration.

for PostgreSQL

- Supports schema migration, full data migration, and incremental data migration.

PostgreSQL

- PolarDB for PostgreSQL (Compatible with Oracle) must be

migration to PolarDB

accessed as a self-managed database over public network.

for PostgreSQL (Compatible with

- PostgreSQL must be accessed as a self-managed database

Oracle)

over public network.

- PostgreSQL versions 10.x, 11.x, 12.x.

- PostgreSQL versions 9.x to 10.x.

Data migration

- Supports schema migration, full data migration, and

between PostgreSQL

incremental data migration.

instances

- For self-managed databases, incremental migration requires the installation of the ali_decoding plugin.

- Supports schema migration, full data migration, and incremental data migration.

- PPAS requires public network or private network access,

PPAS migration to

and must be able to communicate with DTS. Select the

PolarDB for

public network access method and enter the public or

PostgreSQL

private IP address.

(Compatible with Oracle)

- PolarDB for PostgreSQL (Compatible with Oracle) requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address.

- Supports only full and incremental data migration. Schema

Migrate data from

migration is not supported.

ApsaraDB for MongoDB to Kafka

- Supports self-managed Kafka versions 0.1 to 2.7.

- Only self-managed Redis over public network.

- Cluster architecture is not supported.

Data migration between Redis

- Supported self-managed Redis versions: 2.8, 3.0, 3.2, 4.0.

instances

- Supports full data migration and incremental data migration.

- Supported SQL Server versions: 2005 to 2017.

Data migration between SQL Server

- Supports schema migration, full data migration, and

instances

incremental data migration.

Data migration

Supports schema migration, full data migration, and

between PolarDB for

incremental data migration.

MySQL instances

Migrate data from

Supports schema migration, full data migration, and

PolarDB for MySQL to

incremental data migration.

PolarDB-X 2.0 Migrate data from PolarDB-X 2.0 to

Supports schema migration, full data migration, and

PolarDB for MySQL

incremental data migration.

Migrate data from RDS for PostgreSQL

Supports schema migration, full data migration, and

to PolarDB for

incremental data migration.

PostgreSQL

Data migration between PolarDB for

Supports schema migration, full data migration, and

PostgreSQL

incremental data migration.

instances

Self-managed MySQL (Public Network)

Supports schema migration, full data migration, and

migration to PolarDB-

incremental data migration.

X 2.0

RDS MySQL

Supports schema migration, full data migration, and

(Instance) migration

incremental data migration.

to PolarDB-X 2.0

RDS PostgreSQL

Supports schema migration, full data migration, and

migration to PolarDB

incremental data migration.

for PostgreSQL

- Supports schema migration, full data migration, and

PolarDB-X 1.0

incremental data migration.

migration to Kafka

- Kafka version 2.7.

Migrate data from OceanBase Database

Supports schema migration, full data migration, and

for MySQL to PolarDB

incremental data migration.

for MySQL

Incremental data subscription with

RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

PolarDB-X 1.0 as source

Incremental change tracking from a

Supports multi-stream change data capture (CDC).

PolarDB-X 2.0 source

Change tracking

Incremental data subscription with

MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7.

MySQL as source

Incremental data

- Oracle versions 9i, 10g, 11g.

subscription with

- Oracle RAC is not supported.

Oracle as source

Db2 for i

Supports schema synchronization, full data synchronization,

synchronization to

and incremental data synchronization.

MySQL

Synchronize data

Supports schema synchronization, full data synchronization,

from Db2 for i to

and incremental data synchronization.

PolarDB for MySQL

Db2 for LUW

- Supports schema synchronization, full data

synchronization to

synchronization, and incremental data synchronization.

AnalyticDB

- Db2 for LUW versions 10.1, 10.5, 11.5.

PostgreSQL

Synchronize data from Db2 for LUW to

Supports schema synchronization, full data synchronization,

PolarDB for

and incremental data synchronization.

PostgreSQL

Synchronize data

Supports schema synchronization, full data synchronization,

from Db2 for LUW to

and incremental data synchronization.

PolarDB for MySQL

- Supports schema synchronization, full data

Synchronize data

synchronization, and incremental data synchronization.

from PolarDB for

- Supports self-managed MySQL versions 5.1, 5.5, 5.6, and

MySQL to MySQL

5.7.

- Supports full data synchronization and incremental data

Synchronize data

synchronization.

from PolarDB for MySQL to Kafka

- Supports self-managed Kafka versions 0.1 to 2.7.

- RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

PolarDB-X 1.0

- Supports schema synchronization, full data

synchronization to

synchronization, and incremental data synchronization.

DataHub

- RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

Data synchronization between PolarDB-X

- Supports schema synchronization, full data

1.0 instances

synchronization, and incremental data synchronization.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6,

MySQL

5.7.

synchronization to AnalyticDB

- Supports schema synchronization, full data

PostgreSQL

synchronization, and incremental data synchronization.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6,

MySQL

5.7.

synchronization to AnalyticDB MySQL

- Supports schema synchronization, full data

2.0

synchronization, and incremental data synchronization.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6,

MySQL

5.7.

synchronization to AnalyticDB MySQL

- Supports schema synchronization, full data

3.0

synchronization, and incremental data synchronization.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7.

MySQL synchronization to

- Supports schema synchronization and incremental data

DataHub

synchronization, but does not support full data synchronization.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7.

MySQL

- Supports schema synchronization, full data

synchronization to

synchronization, and incremental data synchronization.

MaxCompute

- Supported DDL statements: ALTER TABLE, ADD COLUMN.

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6,

One-way

5.7.

synchronization between MySQL

- Supports schema synchronization, full data

instances

synchronization, and incremental data synchronization.

Data synchronizat ion

- MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6,

Two-way

5.7.

synchronization between MySQL

- Supports schema synchronization, full data

instances

synchronization, and incremental data synchronization.

Oracle

- Oracle versions 9i, 10g, 11g, 12c, 18c, 19c.

synchronization to

- Supports schema synchronization, full data

AnalyticDB

synchronization, and incremental data synchronization.

PostgreSQL

- Oracle versions 9i, 10g, 11g, 12c, 18c, 19c.

Oracle

- Supports schema synchronization and incremental data

synchronization to

synchronization.

DataHub PolarDB-X 1.0

- RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

synchronization to

- Supports schema synchronization, full data

AnalyticDB MySQL

synchronization, and incremental data synchronization.

3.0

- RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0.

PolarDB-X 1.0

- Supports full data synchronization and incremental data

synchronization to

synchronization, but does not support schema

PolarDB-X 2.0

synchronization.

Synchronize data

Supports full data synchronization and incremental data

from PolarDB-X 2.0

synchronization. Schema synchronization is not supported.

to PolarDB-X 1.0

Synchronize data from PolarDB-X 2.0

Supports schema synchronization, full data synchronization,

to AnalyticDB for

and incremental data synchronization.

MySQL 3.0

PolarDB-X 2.0 synchronization to

Supports schema synchronization, full data synchronization,

AnalyticDB

and incremental data synchronization.

PostgreSQL

PolarDB-X 2.0

Supports schema synchronization, full data synchronization,

synchronization to

and incremental data synchronization.

MySQL

Data synchronization

Supports schema synchronization, full data synchronization,

between PolarDB-X

and incremental data synchronization.

2.0 instances

- Only supports full and incremental data synchronization,

PostgreSQL

does not support schema synchronization.

synchronization to AnalyticDB

- DDL synchronization is not supported.

PostgreSQL

- One task only supports synchronization of one database.

- Supports only full and incremental data synchronization.

Synchronize data

Schema synchronization is not supported.

from ApsaraDB for MongoDB to Kafka

- Supports self-managed Kafka versions 0.1 to 2.7.

- Supported architectures: standard and cluster.

Data synchronization between Redis or

- Supported version: 5.0.

Tair Enterprise Edition instances

- Supports one-way and two-way synchronization.

Data synchronization

- Supported architectures: standard and cluster.

between Redis Community Edition

- Supported versions: 4.0, 5.0.

instances

- Supported SQL Server versions: 2005 to 2017.

Data synchronization between SQL Server

- Supports schema synchronization, full data

instances

synchronization, and incremental data synchronization.

Zone-disaster

Supports zone-disaster recovery.

recovery

Disaster recovery

Geo-disaster

Supports geo-disaster recovery.

recovery

HTTPS certificate

DTS Portal supports national cryptographic HTTPS access.

encryption

Resource isolation

Security

Integrates with ASCM to achieve resource isolation between

between different

different department accounts.

accounts

Security audit

Supports security audit.

Multi-region

Multi-region

Supports multi-region deployment.

deployment

deployment

Monitoring

Support for task

Supports configuration of task latency and task failure alerts.

and alerting

alerting configuration

Real-time conversion of Oracle, Db2, Teradata SQL to

Online SQL

multiple target databases such as PolarDB, AnalyticDB

conversion

PostgreSQL, and other mainstream open-source databases.

Java application profile information display.

Application profile

Application

Java application evaluation details, modification points, and

evaluation

modification suggestions.

Application data

Source database Oracle, Db2, Teradata, Java application data

collection

collection (business SQL).

Incremental data

Oracle, Db2, Teradata source database incremental

comparison

comparison.

Support for hot

Supports hot upgrades for subsequent assessment migration

upgrade functionality

function iterations.

Data and application migration assessment

Support for high

Supports multi-data center disaster recovery.

(ADAM)

availability

Source database

Oracle, Db2, Teradata source database structure comparison.

verification

Migration plan

Supports migration from mainstream open-source databases

generation

to PolarDB, AnalyticDB PostgreSQL.

Supports schema revision and modification suggestions for

Schema

migration from mainstream open-source databases to

migration/revision

PolarDB, AnalyticDB PostgreSQL.

Source database

Display of collected source database profile.

profile

Target database

Display of source database assessment details, compatibility

compatibility

details, incompatibility points and reasons.

assessment

Target database

Compatibility selection recommendations for multiple target

selection

databases.

recommendations

DTS data consistency

Data consistency

Supports creating data verification and correction tasks for

verification

verification and

database tables.

and

correction

correction

DTS periodic

Relies on DMS task orchestration and scheduling functions to

Periodic data

data

achieve periodic full data migration through orchestrated

integration

integration

periodic data integration tasks.

DTS data ETL, stream

DTS data ETL stream

Supports creating ETL tasks, stream and batch computing

and batch

and batch processing

tasks for data processing with DTS Pro.

processing basic package

Cross-cloud

One-way and two-

Supports only MySQL versions 5.1 to 5.7 and RDS MySQL

synchronizat

way synchronization

versions 5.5, 5.6, and 5.7.

ion

across two clouds

functionality
