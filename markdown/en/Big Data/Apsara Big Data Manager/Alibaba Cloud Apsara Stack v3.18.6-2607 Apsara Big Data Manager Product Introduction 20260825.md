Alibaba Cloud  
Apsara Stack  
Apsara Big Data Manager  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260825

**Table of Contents**

- [1.Apsara Big Data Manager](#section-1)
    - [1.1. Features](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.Apsara Big Data Manager

Apsara Big Data Manager (ABM) is an operations and maintenance (O&M) platform tailored for big data products. ABM supports monitoring, management, and O&M in multiple dimensions, such as business, services, clusters, and hosts. Customer O&M teams or on-site personnel can use ABM to perform O&M operations on big data products and manage the products in an efficient and centralized manner.

<a id="section-1-1"></a>

## 1.1. Features

Apsara Big Data Manager (ABM) provides the following functional modules for big data products: Monitor, O&M, and Management. The Monitor module helps you monitor the status of big data products in real time. The O&M and Management modules allow you to perform O&M and management operations by using a graphical user interface (GUI) based on multiple dimensions, such as business, services, clusters, and hosts.

**Monitor**

- **Dashboard**: allows you to view the overview of the key metrics of MaxCompute, DataWorks, Realtime Compute, and DataHub.

- **Repository**: allows you to view the resource usage of MaxCompute, DataWorks, and DataHub.

- **Health**: allows you to view the monitoring items of each big data service and the alerts of different levels of urgency and check the monitoring items and alerts again after the alerts are handled.

- **Reports**: allows you to view the inspection results of each big data service.

**O&M**

- **Business**: provides O&M features that are dedicated for big data products.

  - MaxCompute: allows you to manage and optimize projects and jobs.

  - DataHub: displays information about projects and topics in DataHub clusters.

  - Realtime Compute: displays information about projects, jobs, and queues in Realtime Compute clusters.

  - Elasticsearch: allows you to configure clusters and system settings.

  - MaxCompute and DataWorks: allows you to configure and manage geo-disaster recovery in the configuration center. You can configure protection groups, rehearsal plans, and failure plans.

- **Services**: displays O&M information about big data products. The information includes all service roles in a cluster and the resource usage trend of each service role. This tab also provides specific information about the following big data products:

  - MaxCompute: displays information about Control, Fuxi, Pangu, and Tunnel Service.

  - DataWorks: displays information about data warehouses.

  - DataWorks: displays information about data warehouses and data integration.

  - DataHub: displays information about Control, Fuxi, and Pangu.

  - Realtime Compute: displays information about Realtime Compute, Yarn, and Hadoop Distributed File System (HDFS).

- **Clusters**: displays O&M information about clusters. The information includes the overview and the health status of clusters.

- **Hosts**: displays O&M information about hosts. The information includes the overview of hosts.

**Management**

- **Jobs**: allows you to run jobs to perform O&M operations on big data products. Jobs are classified into cron jobs and common jobs. The system can automatically run cron jobs at a specified time on a schedule. You can also manually run cron jobs. Common jobs can only be manually run.

- **Health Checks**: includes Monitoring Configuration and Patrol Configuration.

  - The Monitoring Configuration tab provides various built-in check items for each big data service. The system automatically checks service faults and sends alerts based on the scheduling items and check items. If a check item does not meet the requirements, the system reports an alert. You can also configure custom scheduling intervals and modify the status of scheduling items and check items. The information displayed on this tab helps you identify and handle service faults at the earliest opportunity.

  - The Patrol Configuration tab allows you to manage inspection items and inspection scenarios. The system manages inspection items at a specified time on a schedule. You can also manually manage inspection items. This helps prevent potential risks of major issues or service faults.

- **Processes**: allows you to process manual tasks, define processes, and view process instances.

- **Operation Logs**: provides the records of all O&M operations that are performed in the ABM console and the details of each operation. You can identify the causes of service faults based on the operation records.

<a id="section-1-2"></a>

## 1.2. Benefits

Apsara Big Data Manager (ABM) allows you to perform O&M operations on big data products and manage the products in a centralized manner. ABM helps enhance the stability of big data products, reduce O&M costs, and improve the efficiency of O&M. ABM provides benefits in various aspects, such as cluster health monitoring, resource usage analysis, and a graphical user interface (GUI) for O&M and management operations.

**Cluster health monitoring**

Allows you to monitor and configure the devices, resources, and services of the clusters of big data products, and collects and displays performance metrics of the clusters in real time.

**Resource usage analysis**

Displays the status of devices, resources, and services of clusters in real time, provides the historical data of the devices, resources, and services, and supports data aggregation and analysis to help you evaluate the health status of a cluster. If the evaluation result indicates potential risks in the cluster, related engineers can be immediately notified.

**GUI for O&M and management operations**

Provides a GUI on which you can view performance metrics and perform common O&M operations.

<a id="section-1-3"></a>

## 1.3. Scenarios

If you are using Apsara Stack and have deployed one or more big data services, you need to use Apsara Big Data Manager (ABM) to perform operations and maintenance (O&M) on these big data services.

**Apsara Stack Enterprise and big data services**

If you are using Apsara Stack Enterprise and have deployed one or more big data services, such as MaxCompute or DataWorks, you need to use ABM to perform O&M operations on these big data services.

**Apsara Stack Agility SE and big data services**

If you are using Apsara Stack Agility SE and have deployed one or more big data services, such as MaxCompute or DataWorks, you need to use ABM to perform O&M operations on these big data services.

**Apsara Stack Agility PaaS and big data services**

If you are using Apsara Stack Agility PaaS and have deployed one or more big data services, such as Alibaba Cloud Realtime Compute for Apache Flink, you need to use ABM to perform O&M operations on these big data services.

<a id="section-1-4"></a>

## 1.4. Features

This topic describes the features that are provided in the Apsara Big Data Manager (ABM) console.

**Service**

**Module**

**Feature**

**Description**

Displays the key operation metrics of

Instrument

MaxCompute, DataWorks, StreamCompute, and

cluster

DataHub, including cluster resource usage, traffic, and the running overview of jobs and tasks.

Displays the resource usage in MaxCompute,

Resource Library

DataWorks, and DataHub.

Monitoring

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of ABM.

Provides in-depth health check of ABM services,

Report

businesses, and capacity details, and generates reports.

Allows you to view cron job statistics, specify geo-

Business

disaster recovery security configurations, manage

operation and

protection groups, and perform routine drills and

maintenance

Operation

ABM

failovers.

and maintenan ce

Environment

Allows you to view the basic components of a

operation and

single host.

maintenance

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Allows you to configure monitoring and scheduling

Health

items, inspection items, inspection scenarios, and

Management

scenario combinations.

Manageme nt

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of DataHub.

Monitoring

Provides in-depth health check of DataHub

Report

services, businesses, and capacity details, and generates reports.

Business

Allows you to view the information about DataHub

operation and

projects, log sources, hot machine analysis, and

maintenance

data archiving tasks.

Allows you to perform O&M operations on control,

Service operation

Job Scheduler, and Apsara Distributed File System

Operation

and maintenance

services, and displays the information about

and

service instances.

maintenan ce

Displays the overview, health, and machine list of

Cluster O&M

DataHub clusters, and supports node scaling.

DataHub

Allows you to view the host list and the overview

Host O&M

and server role information of specified hosts.

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Allows you to configure monitoring and scheduling

Health

items, inspection items, inspection scenarios, and

Management

scenario combinations.

Manageme nt

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of DataWorks.

Monitoring

Provides in-depth health check of DataWorks

Report

services, businesses, and capacity details, and generates reports.

Provides a task instance list and multi-dimensional

Service operation

analysis for data integration services, and provides

and maintenance

the slot management feature for data workshop services.

Operation and maintenan

Displays the overview, health, and machine list of

Cluster O&M

ce

DataWorks clusters, and supports node scaling.

DataWorks

Allows you to view the host list and the overview

Host O&M

and server role information of specified hosts.

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Allows you to configure monitoring and scheduling

Health

items, inspection items, inspection scenarios, and

Management

scenario combinations.

Manageme nt

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.

Operation and maintenan

Business

Displays the information about the Flink queue and

ce

operation and

the overall cluster resource inventory.

maintenance

Flink

Manageme

Allows you to run ordinary jobs and cron jobs, and

Job Services

nt

view the job execution history.

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of Hologres.

Monitoring

Provides in-depth health check of Hologres

Report

services, businesses, and capacity details, and generates reports.

Allows you to perform O&M operations on Job

Service operation

Scheduler and Apsara Distributed File System

and maintenance

services, and displays the overview, service roles, and node lists of these services.

Operation and

Displays the overview, health, and machine list of

maintenan

Cluster O&M

Hologres clusters, and supports the

ce

synchronization of region information.

Hologres

Allows you to view the host list and the overview

Host O&M

and server role information of specified hosts.

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Allows you to configure monitoring and scheduling

Health

items, inspection items, inspection scenarios, and

Management

scenario combinations.

Manageme nt

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of MaxCompute.

Monitoring

Provides in-depth health check of MaxCompute

Report

services, businesses, and capacity details, and generates reports.

Allows you to perform project management, quota

Business

group management, job management, and

operation and

business governance, including file merging, file

maintenance

archiving, and multi-dimensional resource analysis.

Allows you to perform O&M operations on control, Job Scheduler, Apsara Distributed File System,

Service operation

Lindorm Tunnel Service, and replication services,

and maintenance

Operation

displays service instances, and allows you to

and

modify service instance configurations.

maintenan ce

Displays the overview, health, and machine list of

MaxComp

Cluster O&M

MaxCompute clusters, and supports node scaling.

ute

Allows you to view the host list and the overview

Host O&M

and server role information of specified hosts.

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Recycling

Allows you to modify the rules for recycling custom

Management

chart data and default chart data.

Allows you to configure monitoring and scheduling

Manageme

Health

items, inspection items, inspection scenarios, and

nt

Management

scenario combinations.

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.

Provides diagnostic analysis of a single job and

Job Analysis

allows you to view the diagnostics history.

Analysis

Provides diagnostic analysis of a single queue in a

Queue Analysis

cluster and allows you to view the diagnostics history.

Provides built-in scheduling and monitoring items

Degree of health

and displays the monitoring items and alerts of StreamCompute.

Monitoring

Provides in-depth health check of StreamCompute

Report

services, businesses, and capacity details, and generates reports.

Business

Allows you to manage StreamCompute projects,

operation and

jobs, and queues.

maintenance

Service operation

Displays the overview of Blink, YARN, and Hadoop

and maintenance

Distributed File System (HDFS) services.

Stream

Operation

Compute

and

(Blink)

maintenan ce

Displays the overview, health, and machine list of

Cluster O&M

StreamCompute clusters, and supports node scaling.

Allows you to view the host list and the overview

Host O&M

and server role information of specified hosts.

Allows you to run ordinary jobs and cron jobs, and

Job Services

view the job execution history.

Allows you to configure monitoring and scheduling

Health

items, inspection items, inspection scenarios, and

Management

scenario combinations.

Manageme nt

Allows you to view details of manual tasks, process

Process Services

definitions, and process instances.

Records the history of O&M operations and the

Operational Audit

details of each operation.
