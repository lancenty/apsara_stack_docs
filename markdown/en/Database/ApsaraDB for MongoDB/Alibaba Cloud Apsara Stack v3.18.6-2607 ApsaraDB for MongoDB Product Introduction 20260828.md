Alibaba Cloud  
Apsara Stack  
ApsaraDB for MongoDB  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.ApsaraDB for MongoDB](#section-1)
    - [1.1. What is ApsaraDB for MongoDB?](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Functions and features](#section-1-4)

<a id="section-1"></a>

# 1.ApsaraDB for MongoDB

ApsaraDB for MongoDB is a high-performance document database service that is fully compatible with the MongoDB protocol. Based on the Apsara distributed system and a highly reliable storage engine, ApsaraDB for MongoDB provides features such as high availability, elastic scaling, read/write splitting, high data security, backup and restoration, intelligent O&M, and online database management.

<a id="section-1-1"></a>

## 1.1. What is ApsaraDB for MongoDB?

ApsaraDB for MongoDB is a MongoDB-compatible document-oriented database service that is developed based on the Apsara system and a high-reliability storage engine. ApsaraDB for MongoDB uses a multi-node architecture to ensure high availability and supports elastic scaling, disaster recovery, backup and restoration, and performance optimization.

**Data structure**

MongoDB is a document-oriented NoSQL database. MongoDB stores data in JSON-like documents that consist of field-value pairs. Example:

```text
{
    name:"John",
    sex:"male",
    age:30
}
```

**Storage structure**

The storage structure of MongoDB is different from that of conventional relational databases. Data in MongoDB is organized at the following levels:

- Document

  Documents are the basic unit of data in MongoDB. A document consists of BSON key-value pairs and is equivalent to a row in a relational database.

- Collection

  A collection can contain multiple documents. Collections are equivalent to tables in a relational database.

- Database

  A database can contain multiple collections. You can create multiple databases in MongoDB. Databases are equivalent to relational databases.

**Instance architectures**

ApsaraDB for MongoDB provides the following instance architectures:

- Replica set instances An ApsaraDB for MongoDB replica set instance consists of a primary node, one or more secondary nodes, and a hidden node.

  - Primary node: processes all read and write operations.

  - Secondary node: synchronizes data from the primary node. If the primary node fails, a secondary node becomes the new primary node to ensure high availability.

  - Hidden node: ensures high availability of the instance. If a secondary node fails, the hidden node becomes the secondary node.

    > **Note**
    >
    > The hidden node is used only to ensure high availability. It is invisible to
    >
    > users.

- Sharded cluster instances An ApsaraDB for MongoDB sharded cluster instance consists of mongos, shard, and Configserver nodes.

  - Mongos node: routes queries and write operations to the corresponding shard node.

  - Shard node: stores database data.

  - Configserver node: stores data of shard nodes.

**Deployment suggestions**

When you deploy an ApsaraDB for MongoDB instance, you can consider the following aspects:

- Regions and zones You can select a region and zone based on your location, the availability of Alibaba Cloud services, your application availability requirements, and whether internal network communication is required.

  > **Note**
  >
  > A region is an Alibaba Cloud data center. A zone is a physical area within a
  >
  > region that has its own independent power supply and network.

  For example, if your application is deployed on an Elastic Compute Service (ECS) instance and requires an ApsaraDB for MongoDB instance to serve as its database, you must select the same region and zone as the ECS instance when you create your ApsaraDB for MongoDB instance.

  > **Note**
  >
  > - An ECS instance and an ApsaraDB for MongoDB instance within the same zone can be connected by using an internal network with minimal network latency.
  >
  > - The region and zone determine the physical location of an ApsaraDB for MongoDB instance. You cannot change the region of an ApsaraDB for MongoDB instance after the instance is created.

- Network planning

  A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways within a VPC. We recommend that you select VPC for improved security.

- Security policies

  ApsaraDB for MongoDB provides comprehensive security measures to improve data security. You can ensure database security by means of zone-disaster recovery, audit logs, network isolation, whitelists, password authentication, SSL encryption, and Transparent Data Encryption (TDE).

<a id="section-1-2"></a>

## 1.2. Benefits

ApsaraDB for MongoDB is a MongoDB-compatible document-oriented database service that is developed based on the Apsara system and a high-reliability storage engine. ApsaraDB for MongoDB ensures high availability, supports elastic scaling, and delivers security.

**High availability**

- High-availability architecture, zone-disaster recovery, and automatic backup to ensure business availability

  - ApsaraDB for MongoDB provides the three-node replica set and sharded cluster architectures. Multiple data nodes are deployed on various physical servers. When a node in an instance fails, other nodes automatically synchronize data to ensure the high availability of the instance.

  - ApsaraDB for MongoDB allows you to create dual-zone instances. When a zone for a dual-zone instance becomes unavailable due to unexpected events, the data in the instance can be synchronized in the other zone to ensure the continued availability of the instance.

  - ApsaraDB for MongoDB provides the automatic backup feature. The system automatically backs up data and uploads the data to Object Storage Service (OSS) during the specified time period. This improves disaster recovery capabilities and reduces consumed disk capacity. Backup files can be used to restore instance data to their source instance and prevent irreversible effects on business data caused by accidental changes and other errors.

- Primary/secondary failover to ensure service availability

  ApsaraDB for MongoDB provides the primary/secondary failover feature. When a node of an instance fails, the system triggers a primary/secondary failover to ensure availability of the instance.

**Elastic scaling**

- Flexible configuration changes to meet business requirements

  ApsaraDB for MongoDB allows you to change instance configurations. Multiple instance types are available for configuration change. You can change instance configurations as your business needs change.

- Multiple chip architectures for hybrid deployment

  ApsaraDB for MongoDB provides a variety of chip architectures such as x86 and ARM. You can select a chip architecture based on your needs for scenarios such as scale-out events, disaster recovery, and hybrid deployment.

**Security**

- Pre-protection

  ApsaraDB for MongoDB provides the DDoS mitigation feature. ApsaraDB for MongoDB monitors inbound traffic in real time, filters source IP addresses to scrub large amounts of malicious traffic, and triggers blackhole filtering if traffic scrubbing becomes ineffective.

- In-event protection

  - Configuration of IP address whitelists for enhanced database access security

    IP addresses or CIDR blocks used to access databases can be added to a whitelist of the instance to ensure security and stability of databases.

  - SSL encryption for enhanced link security

    SSL encryption can encrypt network connections at the transport layer to improve data security and ensure data integrity. After SSL encryption is enabled, you can install SSL certificates issued by certification authorities (CAs) on your application to improve link security.

  - TDE for improved data security

    Transparent Data Encryption (TDE) is used to encrypt data before the data is written from data files to a disk and decrypt data before the data is read from a disk and written to the memory. TDE does not increase the sizes of data files. You can use TDE without the need to modify the configuration data of your application. You can enable TDE for an instance to encrypt instance data and improve data security.

- Post-auditing

  ApsaraDB for MongoDB automatically stores audit logs in Log Service and allows you to download these logs from Log Service. This facilitates the long-term storage and management of audit logs.

**Intelligent O&M**

- Comprehensive monitoring to help O&M personnel understand the running status of instances

  ApsaraDB for MongoDB provides a variety of performance monitoring metrics such as CPU utilization, memory usage, and disk usage for you to view the running status of your instances in real time.

- Performance optimization to ensure stability, security, and efficiency of databases

  ApsaraDB for MongoDB allows you to view and customize instance performance trends and view performance, storage, and slow query logs of instances in real time. This helps you eliminate service failures caused by manual operations and ensure the stability, security, and efficiency of databases.

**Network isolation**

ApsaraDB for MongoDB uses Virtual Private Cloud (VPC) to implement advanced network access control. VPC and IP address whitelists greatly improve the security of ApsaraDB for MongoDB instances.

A VPC can help you build an isolated network environment by using underlying network protocols. You can resolve resource conflicts by customizing route tables, IP addresses, and gateways in VPCs.

By default, ApsaraDB for MongoDB instances deployed in a VPC can be accessed only by the Elastic Compute Service (ECS) instances in the same VPC. If necessary, you can apply for a public IP address to allow access requests from the Internet (not recommended). Before you apply for a public IP address, you must configure a whitelist. For example, you can allow access requests from elastic IP addresses (EIPs) of ECS instances and the Internet egress of your data center.

**Online management of databases**

Data Management (DMS) is an integrated and visualized database solution that offers data management, structure management, user authorization, security auditing, data trend analysis, data tracking, business intelligence (BI) charts, performance optimization, and server management. You can use DMS to log on to the ApsaraDB for MongoDB console and obtain a list of ApsaraDB for MongoDB instances for remote access and online management.

<a id="section-1-3"></a>

## 1.3. Scenarios

ApsaraDB for MongoDB is a MongoDB-compatible document-oriented database service that can store large amounts of data and provides features such as security auditing and backup and restoration. It is widely used in scenarios such as IoT and gaming.

**Read/write splitting**

ApsaraDB for MongoDB uses a three-node replica set architecture to ensure high availability. Three data nodes are deployed on different physical servers and automatically synchronize data. The primary and secondary nodes are configured with different endpoints. MongoDB drivers allocate read/write requests to these nodes.

**Flexible business scenarios**

ApsaraDB for MongoDB has no schema and is suitable for startups that do not want to go through the hassles of changing table schemas. You can store structured data that has a fixed schema in ApsaraDB RDS, data that has flexible schemas in ApsaraDB for MongoDB, and hot data in ApsaraDB for Redis or ApsaraDB for Memcache. This ensures that business data can be stored and retrieved in an efficient manner to reduce data storage costs.

**Mobile apps**

ApsaraDB for MongoDB supports two-dimensional spatial indexes. Therefore, ApsaraDB for MongoDB can provide support for location-based apps. ApsaraDB for MongoDB uses a dynamic storage method, which is suitable for storing heterogeneous data from multiple systems and meets the needs of mobile apps.

**IoT scenarios**

- ApsaraDB for MongoDB provides high performance and allows data to be asynchronously written.

- Three types of components are available in ApsaraDB for MongoDB sharded cluster instances: mongos, shard, and Configserver nodes. You can configure the number and specifications of mongos and shard nodes when you create sharded cluster instances to provide different levels of performance. This makes ApsaraDB for MongoDB suitable for IoT scenarios that involve highly concurrent write operations.

- ApsaraDB for MongoDB provides the secondary index feature for dynamic queries. It can use the MapReduce aggregation framework of MongoDB to conduct multidimensional data analysis.

**Applications in various fields**

- Gaming

  ApsaraDB for MongoDB can be used as a database service for game servers to store user information. The in-game equipment and credits of players are directly stored in the form of an embedded document to facilitate queries and updates.

- Logistics

  ApsaraDB for MongoDB can store order information. The order status is constantly updated during the shipping process and is stored in the form of an embedded array in ApsaraDB for MongoDB. You can read all the changes in an order in a straightforward manner by performing a single query.

- Social networking

  - ApsaraDB for MongoDB can store the information of users and their published WeChat moments. Geographical location indexes can be used to search nearby people and places.

  - Additionally, ApsaraDB for MongoDB is suitable for storing chat history because ApsaraDB for MongoDB provides rich query abilities and is fast in both writing and reading.

- Live video streaming

  ApsaraDB for MongoDB can store user information and gift information.

<a id="section-1-4"></a>

## 1.4. Functions and features

This topic describes the features of ApsaraDB for MongoDB.

| Feature | Description |
| --- | --- |

Create an instance

You can create a replica set or sharded cluster instance.

Restart an instance

You can restart an instance to quickly restore its status.

If the current instance configuration does not meet

Change

application requirements, or is too high or too low,

configurations

change the instance configuration, such as the specification or storage capacity.

Release an

After you delete all databases under the instance, release

instance

the instance to reclaim resources.

Instance

Upgrade the

You can upgrade the database version.

management

database version

Migrate an

You can migrate an instance to another zone within the

instance to another

same region. After migration, all instance attributes,

zone

specifications, and endpoints remain unchanged.

You can create tags and bind them to instances for

Tag management

classification, and then filter instances by tag.

If a node fails, the high-availability system of ApsaraDB for MongoDB automatically triggers a switchover to

Primary/secondary

ensure overall availability. ApsaraDB for MongoDB also

switchover

allows you to manually trigger switchovers in scenarios such as disaster recovery drills.

Create an account

You can create a database account.

Delete an account

You can delete obsolete accounts.

Account management

Modify permissions

You can modify account permissions.

Reset a password

You can reset the password of an account.

Modify the

You can modify the endpoint and port of an instance on

endpoint and port

the ApsaraDB for MongoDB console.

Log in to an ApsaraDB for

You can log in to an ApsaraDB for MongoDB database

MongoDB database

through Alibaba Cloud Data Management Service (DMS).

through DMS Connect to an

Mongo Shell is a built-in database management tool of

ApsaraDB for

MongoDB. You can install MongoDB on your client and

MongoDB instance

use Mongo Shell to connect to an ApsaraDB for MongoDB

through Mongo

instance.

Shell

Database

Apply for a public

You can apply for a public endpoint for scenarios that

connection

endpoint

require connecting to an instance over the Internet.

Release a public

To ensure data security, if you no longer need a public

endpoint

endpoint, release it on the console.

A sharded cluster instance consists of Mongos nodes, shard nodes, and ConfigServer nodes. In most cases,

Apply for the

business read/write operations only need to connect to

endpoint of a shard

Mongos nodes. In specific scenarios, such as data

or ConfigServer

synchronization between clusters, you may need to read

node

the oplog of Shard nodes or configuration information of ConfigServer nodes. You can apply for the endpoint of the corresponding node to meet business requirements.

Release the endpoint of a shard

When you no longer need to connect to Shard nodes or

or ConfigServer

ConfigServer nodes, release their endpoints.

node

To help you monitor and understand instance status,

Monitoring

View monitoring

ApsaraDB for MongoDB provides various performance

information

information

monitoring items. You can view instance monitoring data on the ApsaraDB for MongoDB console.

View a monitoring

You can view CMS metrics to quickly locate O&M issues.

dashboard

You can create alert rules. Then CMS triggers alerts based

Cloud Monitor

Set alert rules

on specified cloud service monitoring metric thresholds

(CMS)

and notifies relevant users promptly.

You can view alert history by cloud product, cloud service

View alert history

instance, or alert level. You can export and download alert history for local data analysis.

Configure an

You can configure an allowlist to enhance database

allowlist

security and stability.

You can assign IPv4-only or dual-stack IPv4/IPv6

IP type and

addresses to meet different network environment

allowlist

requirements. In dual-stack mode, you can configure independent IPv6 allowlists for precise access control.

Configure Secure

You can enable SSL encryption and install the SSL CA

Data security

Sockets Layer

certificate on required application services to improve link

(SSL) encryption

security.

Configure

TDE performs real-time I/O encryption and decryption on

Transparent Data

data files. Data is encrypted before written to disks and

Encryption (TDE)

decrypted when read into memory.

You can query execution statement logs, operation logs,

Audit logs

and error logs of an instance to help you troubleshoot and analyze failures.

Based on business deployment, you can switch node roles

Service

Switch node roles

of ApsaraDB for MongoDB instances through the console

availability

to meet application proximity connection requirements.

Backup mode

Manual backup and automatic backup are supported.

Download backup

Backup and

You can download backup files to restore databases.

files

restoration

Full restoration supports two methods: restore from

Restore databases

backup set and restore to a point in time.

The one-click diagnosis feature diagnoses instances and

One-click diagnosis

provides visualized diagnostic results.

Session

The instance session feature allows you to view and

management

manage sessions of target instances.

You can view real-time performance metrics such as

Real-time

read/write latency, QPS, operation statistics, and

performance

connection statistics to understand database performance in real time.

Autonomy service

The storage analysis feature helps you promptly detect

Storage analysis

storage anomalies in databases to avoid affecting database stability.

You can use different methods to view performance

Performance trend

trends, including viewing by interval, comparison viewing, and custom viewing.

The feature allows you to view slow query log trends,

Slow query log

statistics, and details to help you discover, analyze,

analysis

diagnose, optimize, and track slow queries.

<table>
  <tr>
    <td>Log management</td>
    <td>Slow query log</td>
    <td>You can query slow query log details of an instance to help with troubleshooting and analysis.</td>
  </tr>
  <tr>
    <td rowspan="2">Parameter management</td>
    <td>Configure instance parameters</td>
    <td>You can view and modify values of some parameters, and trace parameter change history.</td>
  </tr>
  <tr>
    <td>Use parameter templates</td>
    <td>You can centrally manage identical or partially identical parameter configurations across multiple instances through parameter templates, and quickly apply them to target instances to improve parameter management and instance configuration efficiency.</td>
  </tr>
  <tr>
    <td rowspan="2">Recycle bin</td>
    <td>Restore an instance</td>
    <td>The instance-level recycle bin allows you to restore deleted instances. You can also modify the retention period of instances in the recycle bin.</td>
  </tr>
  <tr>
    <td>Destroy an instance</td>
    <td>Destroying an instance also destroys all backups except cross-region backups, including regular data backups, log backups, and permanent backups.</td>
  </tr>
  <tr>
    <td rowspan="2">AI capabilities</td>
    <td>Intelligent migration</td>
    <td>After creating an ApsaraDB for MongoDB instance, migrate data through DTS and switch endpoints after migration.</td>
  </tr>
  <tr>
    <td>AI-native interface MCP service</td>
    <td>The MongoDB AI-native interface Model Context Protocol (MCP) service provides standardized, secure, and efficient database access capabilities for large models. Through MCP, AI applications can directly query, execute SQL statements, or manage database instances without writing complex code, enabling rapid implementation of AI-native scenarios such as Retrieval-Augmented Generation (RAG), intelligent O&amp;M, and data Q&amp;A.</td>
  </tr>
</table>
