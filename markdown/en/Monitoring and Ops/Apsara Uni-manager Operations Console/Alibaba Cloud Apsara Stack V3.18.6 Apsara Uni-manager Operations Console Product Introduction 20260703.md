Alibaba Cloud  
Apsara Stack  
Apsara Uni-manager  
Operations Console  
Product Introduction  
Product Version: V3.18.6  
Document Version: 20260703

**Table of Contents**

- [1.Product details](#section-1)
- [2.Product value](#section-2)
- [3.Use cases](#section-3)
- [4.Functions and features](#section-4)

<a id="section-1"></a>

# 1.Product details

Apsara Uni-manager provides a unified operations portal with general O&M capabilities, such as monitoring and alerting, inspection management, and resource management, alongsode dedicated O&M consoles for computing, networking, and storage. The platform reduces O&M costs for your cloud environment and ensures its secure and stable operation.

- **Monitor&Alert**

  Cloud platform O&M is carried out through the following modules: Monitor Management, Alert Management, Event Center, Inspections, Diagnosis Center, and Self Healing.

- **Platform Operation**

  Cloud platform basic O&M is performed through the following modules: Apsara Infrastructure Management, Capacity, Log Center, O&M Services, Disaster recovery management, O&M Change, Reports Center, Task Center, and Management and Control Service O&M.

- **Product Operation**

  Modules such as Computing, Networking, Storage, Databases, Middleware, and Big Data are integrated through standardized access methods to assist O&M personnel in performing in-depth product O&M.

- **Security Management**

  Secure and compliant management of O&M operations are carried out through the following modules: Security Audit, Security Operations, Host Security, Network Security, Account Security, Access Control, Security Compliance Center, and Data Security.

- **System Config**

  You can configure the system through Personalized configuration, Document Management, Card management, Authorization information, Notification Management, Region coordinate management, Third-party Authentication, and Platform Backup Management.

- **User Authorities**

  A redesigned ASO permission system implements a separation of duties for platform operations through hierarchical role management. This includes managing users, user groups, roles, departments, menus, and more.

<a id="section-2"></a>

# 2.Product value

Apsara Stack O&M Platform automates operational workflows to provide proactive monitoring and alerting, root cause analysis, and automated fault remediation. This reduces operational costs and ensures the security and stability of your cloud environment.

**Unified portal**

- Unifies monitoring and alerting across products.

- Unifies capacity monitoring and management across products.

- Provides a single entry point to the O&M consoles for compute, network, and storage.

**Flexible permissions**

- Provides multiple built-in roles, including System Management, Security Management, Security Auditing, Role Management, and Authorized Administrator, that are ready to use out of the box.

- Allows you to create a custom role and define fine-grained permissions for the ASO console, product consoles, and menus.

- Enforces separation of duties for platform operations through hierarchical role management.

**Intelligent analysis**

- Synchronizes global data in real time for unified resource scheduling.

- Monitors and analyzes resource usage trends to optimize resource allocation and utilization.

**Open integration**

- Provides a visual API portal that simplifies and accelerates development.

- Provides standard northbound APIs and multi-language SDKs.

- Supports page-level integration and custom configurations for fast integration with third-party systems.

**Centralized operations**

- Provides comprehensive, centralized monitoring of resources, inventory levels, and alerts to track operational status and identify potential risks.

- Automatically updates the resource dependency topology in real time. Its built-in algorithm engine then identifies probable root causes, narrowing the scope of investigation and accelerating fault isolation.

- Lets you encapsulate atomic operational scripts and perform visual orchestration. The platform also provides automated remediation for various failure scenarios, reducing manual intervention.

- Dynamically analyzes and automatically calculates optimal scale-out strategies to optimize cloud costs and minimize resource waste.

<a id="section-3"></a>

# 3.Use cases

**Routine O&M**

- The O&M workbench provides operations staff with a centralized view of risk data, pending items, and tasks that require attention and provides quick access to frequently used tools, improving operational efficiency.

- alert management aggregates alerts from all modules on the cloud platform by receiving actively reported alerts or by matching monitoring data against alert rules, helping you efficiently locate and resolve faults to ensure service availability.

- Inspection management enables quick health checks for various scenarios to maintain your system and cloud product integrity.

- The diagnosis center, which includes product diagnosis and hardware diagnosis, provides a clear overview of your Apsara Stack platform's health. It helps operations staff quickly detect and isolate cloud platform issues through topology visualization, status checks, root cause analysis, and fault troubleshooting.

- The event center is a unified event management platform for Apsara Stack that centrally manages and prioritizes alerts from both **cloud infrastructure and applications**. By layering, aggregating, and classifying various types of alerts, it reduces alert noise and consolidates alerts into actionable events that require manual intervention, significantly improving O&M efficiency for the Apsara Stack platform.

- capacity management analyzes usage data and patterns to forecast capacity trends for your products, helping you plan for scaling and other operations.

**Automated O&M**

- The platform provides one-click scaling. The entire scaling process is fully automated, integrating server provisioning, network expansion, and cloud product deployment. You can define custom pre-checks and post-checks to reduce change complexity and improve O&M efficiency.

- O&M service provides a unified entry point for common change operations, including orchestration-based automated services and hyperlink-guided services. The Service Catalog acts as a centralized portal for recommended O&M activities, integrating automated workflow entry points and frequently used change services. By using a graphical orchestration framework, you can import templates to quickly update local O&M services, improving the efficiency of automated O&M.

**Security O&M**

- security audit allows you to query activity logs for user operations from the console or CLI.

- security policy allows you to configure security policies for platform accounts and passwords.

- The platform supports two-factor authentication (2FA). When users log in, they must enter both a password and a dynamic verification code generated by an authenticator app. This dual-verification mechanism effectively prevents account compromise.

**Remote O&M**

- remote O&M: Tongque uses a dual-center O&M model that combines remote and local operations. This model enables the sharing of core resources and capabilities, allowing a remote center to uniformly manage and collaboratively support local sites.

- Incident response: During a major failure, the platform provides graceful service degradation, diagnostics, and contingency plans. This improves your response to critical incidents.

- fault drill: This feature provides practical drill plans based on your platform's business architecture and incident response system. These drills identify stability weaknesses, help refine response procedures, and improve business continuity.

<a id="section-4"></a>

# 4.Functions and features

This topic describes the functions and features of Apsara Uni-manager.

**Operation Platform**

| Module | Description |
| --- | --- |
| Operation Platform | 1. You can customize the section to be displayed in the console.<br>2. You can view the overview data of events, alerts, and inspections from the last seven days.<br>3. You can view the asset data and Bare Metal Management Service (BMS) asset overview.<br>4. You can view messages pending approval or action.<br>5. You can view information such as cloud product capacity, security risks, and the distribution of multi-core servers within a single cloud.<br>6. You can perform global search and show your favorites.<br>7. If you are a platform O&amp;M administrator, you can view overview data such as unhealthy products, alerts, capacity, assets, and security risks. |

**Monitor&Alert**

| Module | Description |
| --- | --- |

<table>
  <tr>
    <td>Monitor Management</td>
    <td>1. You can view basic monitoring and business metric information for all cloud products.<br>2. You can configure business metrics for cloud products, and view, copy, edit, import, export, and delete configurations.<br>3. You can view monitoring templates and alert rules of all cloud products. You can import, export, and edit monitoring templates, as well as modify and export alert rules.<br>4. You can view all alerts for cloud product monitoring, including clusters and services.<br>5. API Monitoring Dashboard allows you to monitor metrics such as API requests, average visists, average total time, availability, and success rate for APIs registered with gateways. You can query metrics by time range (up to 31 days).<br>6. You can view and manage alarm rules and alarm history for cloud product API monitoring. You can modify, copy, disable, enable, or delete alarm rules.<br>7. You can view core metrics of networking products to monitor product and device status in real time.<br>8. Site monitoring provides preset monitoring tasks. These tasks use TianjiMon black box container nodes to remotely probe virtual IP addresses (VIPs), Domain Name Resolution (DNS) entries, and hostnames exposed by any cloud product, component, or cluster to check connectivity and performance. You can also create and manage site monitoring tasks.<br>9. You can view basic information and monitoring charts of each cloud product instance to monitor the operational status of your resources.<br>10. You can configure alert rules for cloud service instances and view generated alerts that are displayed in an aggregated manner. You can view, modify, copy, disable, enable, or delete alert rules.<br>11. You can view the impact and utilization information about cloud product metrics (accessed via CMS/TianjiMon) on OTS capacity, as well as the control policies on metrics.<br>12. You can customize a dashboard to display the metrics for business monitoring and application monitoring on the same page. You can drag elements to customize a dashboard in a visualized manner. You can also specify multiple conditions to query data and display the queried data in multiple types of charts.<br>13. You can visually manage the data sources of APIs.<br>14. You can extend monitoring capabilities by using custom scripts or executable commands, achieving rapid enhancement of monitoring capabilities after inspections or fault reviews.</td>
  </tr>
</table>

<table>
  <tr>
    <td>Alert Management</td>
    <td>1. You can view the number of alerts at different levels by region, alert sources, total number of alerts, alert trends, highest-level alerts, all alerts, and alert distribution across cloud products.<br>2. You can view lists of real-time alerts and dumped alerts, export alerts, and search for alerts by alert content, level, source, resource owner, time, and status.<br>3. You can view alert details, such as alert information, impact scope, and handling suggestions. You can handle or close alerts.<br>4. You can view monitoring templates of all services and alert rules of cloud products. You can import, export, and edit monitoring templates, and modify and export alert rules.<br>5. You can search for, add, modify, and delete alert contacts and alert contact groups.<br>6. You can configure the retention period and maximum data size of alert data.<br>7. You can configure alert notification channels and push alerts to alert contacts.<br>8. You can mute alerts during a specific period of time and mute alerts by product, cluster, service, and machine. You can also mute a single alert and unmute alerts.<br>9. You can upload the latest alert list data package. By default, only the latest data package takes effect.</td>
  </tr>
  <tr>
    <td>Inspections</td>
    <td>1. You can run inspections for multiple inspection scenarios with a few clicks.<br>2. You can create custom inspection scenarios and add different inspection items.<br>3. You can configure an inspection to run as scheduled or manually start an inspection.<br>4. You can view recent inspection status, data overview, anomaly distribution and overall trends of inspection items, inspection task records, inspection findings, and the latest inspection reports.<br>5. You can view the following information in an inspection report: inspection scenario, inspection start time, inspection end time, initiator, and suggestions; overall pass rate, total number of inspection items, number of normal items, number of warnings, number of errors, and inspection details in a specific scenario; and details of each inspection item, including the name, content, and results.<br>6. You can search for inspection records and manually terminate an inspection.<br>7. You can download inspection reports and email inspection results.</td>
  </tr>
  <tr>
    <td>Self Healing</td>
    <td>1. You can view details of each auto-recovery rule, including trigger conditions, associated plans, and execution method.<br>2. You can manage diagnosis and recovery plans, while also configuring plan templates and risk levels.<br>3. You can view the execution history of self-healing rules and track the status and results of diagnosis and recovery plans.</td>
  </tr>
  <tr>
    <td>Diagnosis Center</td>
    <td>1. You can view the health status of platform products, including analyzing the product deployment final states, checking for critical alerts, and performing eBFP network diagnostics to comprehensively assess product status.<br>2. You can view the health status of networks and hardware by data center.<br>3. You can view the dependency relationships among products with a few clicks to quickly assess fault impact.<br>4. You can view product diagnostic records.</td>
  </tr>
  <tr>
    <td>Event Center</td>
    <td>1. You can view multi-dimensional statistics on events and specify filter conditions as needed to flexibly view information about key events.<br>2. You can obtain and manage events at all levels. For example, you can view details of an event and handle the event.<br>3. You can configure event severity grading policies for cloud platform events.<br>4. The system provides a portal that allows you to quickly handle events on the <strong>My</strong> <strong>Pending Events</strong> and <strong>My Participated Events</strong> tabs.<br>5. You can centrally manage attributes and enumerations. You can also customize configurations based on business needs.<br>6. Notification management enables you to manage alert and event message notification channels, groups, and strategies to meet notification requirements across different stages and scenarios.</td>
  </tr>
</table>

**Platform Operation**

| Module | Description |
| --- | --- |
| Capacity | 1. You can view the average available capacity, trends, and utilization rates for core products, view the available capacity forecasts of products by day, week, or month, and export capacity details by individual product.<br>2. You can view the capacity information about Elastic Compute Service (ECS) and Container Service for Kubernetes.<br>3. You can view the capacity information about Server Load Balancer (SLB) instances, elastic IP addresses (EIPs), and other networking services.<br>4. You can view the capacity information about storage services, such as Elastic Block Storage (EBS), File Storage NAS (NAS), Object Storage Service (OSS), and Tablestore. You can view the capacity usage trends by cluster.<br>5. You can view the capacity usage trends of database products and view capacity information by database type and date.<br>6. You can configure capacity alert rules to trigger alerts when the product capacity thresholds are met.<br>7. You can view capacity data of base, middleware, big data, and other product categories. |
| O&amp;M Services | 1. A unified portal for service execution changes is provided.<br>2. You can manage the lifecycle of services.<br>3. Visual orchestration enables you to orchestrate different types of components into templates to meet the needs of various O&amp;M scenarios.<br>4. You can manage classification and permissions in Service Catalog.<br>5. You can use automated O&amp;M capabilities to perform operations on multiple hosts or Docker containers in batches.<br>6. Preconfigured common scripts are provided. You can create custom Shell and Python scripts. You can also create, import, view, modify, export, and delete scripts.<br>7. With software repositories, you can manage software, including uploading, viewing, downloading, and deleting software.<br>8. You can manage O&amp;M jobs. Each O&amp;M job performs a specific task, such as distributing software or executing a script. You can create, import, view, export, modify, execute, and delete O&amp;M jobs.<br>9. You can search for O&amp;M jobs and view their details, such as the job name, start time, end time, execution method, and execution result.<br>10. You can configure service notification settings.<br>11. You can view details of various types of execution flows. |
| Log Cleanup | 1. You can clean logs in specific log files for designated containers or physical machines.<br>2. You can modify, import, and export cleanup rules and configure thresholds for log cleanup.<br>3. You can view the usage of a specific log file for a designated container or physical server.<br>4. You can manually trigger log cleanup or configure automated log cleanup.<br>5. You can view log cleanup records. |
| Version Management | 1. You can manage versions of product packages, component atches, and compressed packages.<br>2. You can configure the system to display and analyze versions of deployed products, including product versions and component versions.<br>3. You can view all change tasks, view the information and phases of specific change tasks, and perform operations on them. |
| Task Center | 1. You can centrally manage platform tasks (pending tasks requiring manual intervention, including but not limited to exception handling, approvals, and manual confirmations).<br>2. You can view the list of your own tasks. |
| Reports Center | 1. You can manage your reports and public reports, including their scenarios and lifecycle.<br>2. You can create report download tasks to download reports in formats such as Excel and HTML.<br>3. You can schedule periodic report delivery. |

**Product Operation**

| Module | Description |
| --- | --- |
| Compute Operations Console | 1. You can view core product metrics for IaaS O&amp;M, including data migration, high availability monitoring, top five proactive O&amp;M events, service check, resource data, capacity allocation rate, and health status of services. You can search for a resource with a few clicks.<br>2. You can view the list of computing clusters and their details. The details include the number of physical servers, number of vCPUs, and memory; the number and status distribution of hosts and ECS instances; as well as vCPU utilization, memory usage, and GPU utilization. You can log in to the control server of a computing cluster with a few clicks and modify the overprovisioning ratio of the cluster.<br>3. You can view the following information about a computing server, including IP address, model, CPU cores, memory, architecture type, service status, and acluster.<br>i. You can lock, unlock, activate, and migrate computing servers.<br>ii. You can audit the operations on computing servers, including operations performed in the console and by calling APIs.<br>iii. You can perform quick diagnostics on a single computing server and view exception information, such as exceptions in cloud computing, hosts, control services or devices, hardware, data center infrastructure, and switches.<br>4. You can view the ECS instance list, the physical host where an ECS instance resides, and cluster details. You can search for an ECS instance by instance ID, private IP address, or public IP address.<br>i. You can start, stop, restart, log in to, or migrate ECS instances.<br>ii. You can modify internal bandwidth settings for ECS instances.<br>iii. You can audit the operations on ECS instances, including operations performed in the console and by calling API operations.<br>5. You can query and view cloud disk details, detach cloud disks from an ECS instance, view audited operations, create snapshots, and view snapshots.<br>6. You can view image details, including operating system, capacity, status, region, and type.<br>i. You can unpublish public images. Once unpublished, a public image remains accessible by its ID but is no longer listed in the image list. You can also publish previously unpublished public images<br>ii. You can convert VMDK images to the RAW format.<br>7. You can view and delete snapshots, view audited operations, create images from snapshots, and query and view information about target snapshots.<br>8. You can view basic information about all elastic network interfaces (ENIs).<br>9. You can view information about security groups, including the region, network type, virtual private cloud (VPC) ID, associated instances, and creation time. You can view details of a security group, including the basic information, inbound rules and outbound rules, and details of ECS instances associated with the security group.<br>10. You can query the inventory of ECS instance types to check their vCPU and memory usage trends.<br>11. You can customize the ECS instance types available for sale.<br>12. You can associate reserved CPU and memory with ECS instances on the relevant management page. The system ensures that computing clusters maintain sufficient available resources to support virtual machine HA in the event of a host failure. You can also configure a dedicated failover host on the relevant management page, allowing the HA service to leverage it when a host failure triggers a failover.<br>13. You can initiate, view, and configure migration tasks, including ECS migration tasks, machine migration tasks, batch ECS migration tasks, batch machine migration tasks, and cluster-level migration tasks.<br>i. When creating a batch migration task, you can enable in-batch migration and scheduled migration for the task.<br>ii. You can perform prechecks before ECS hot migration to assess the feasibility of the operation.<br>iii. You can cancel, pause, or resume migration tasks.<br>iv. You can customize constraints for migration tasks.<br>14. You can search for ECS instance events using filters like date, event ID, instance ID, physical machine IP address, disk ID, and host ID. This helps you monitor the status of your ECS instances.<br>15. You can view monitoring information of computing services, including databases, scheduled task execution status, abnormal workflows, and workflow queues.<br>16. You can view the impact analysis of host failures. When a host fails, you can view the specific ECS instances that are migrated as a result. |

<table>
  <tr>
    <td>Network Operations Console</td>
    <td>1. You can view a network service overview, including port usage, port error packet statistics, network device alerts, traffic dashboard, device vendor distribution, automatic configuration backup status, and configuration baseline synchronization status.<br>2. You can view the physical network topology and alerts reported for devices and the connections between devices.<br>3. You can create a custom view to display specific sets of monitoring data based on your needs. By simply configuring the display content and rules, you can centralize and visualize the monitoring metrics that matter most to you.<br>4. You can view the following information in the physical network device list, including management IP address, serial number (SN), vendor, model, role, online duration, operational status, and last update time. You can also view the details of a physical network device, including port status, aggregate port status, port traffic, CPU usage, memory usage, and alerts.<br>5. You can view syslogs of physical network devices and manage passwords of physical switches.<br>6. You can view traffic metrics of gateway clusters, gateways, SLB clusters, and SLB instances.<br>7. You can view alerts for physical network devices. You can customize monitoring rules and alert templates, specify monitoring metrics for different network products, and configure alert notifications or suppression.<br>8. You can view all network assets, including physical devices, VPCs, gateways, SLB instances, elastic network interfaces, and more.<br>9. You can manage IP CIDR blocks, view details and distribution for all public/private and IPv4/IPv6 CIDR blocks, and manually verify whether a CIDR block conflicts with existing ones.<br>10. You can manage gateway adaptation and monitoring for Computing Network Platform (CPN) network O&amp;M in intelligent computing scenarios.<br>11. You can perform end-to-end path analysis with just a few clicks. A network path topology includes ECS instances, hosts, vSwitches, physical switches, and other network products and services. You can view packet loss and latency information of each hop.<br>12. You can analyze network instances such as DNS or SLB instances with a few clicks to check whether they are running as expected. The system provides visualized and automated diagnostic capabilities.<br>13. You can view the topology of network instances, including IP addresses, listeners, and their corresponding backend servers. You can view diagnostic details, including the item name, description, result, and other detailed information returned by the system.</td>
  </tr>
</table>

**Security Management**

| Module | Description |
| --- | --- |
| ActionTrail | You can audit operation logs, including all operations performed by all users on the platform.<br>1. You can query records of console operations performed by users.<br>2. You can query CLI-based O&amp;M operations performed on servers or containers.<br>3. Intelligent analysis and summarization of audit logs are supported. |
| Container Image Management | You can enforce security controls for container images using built-in and custom policies. This prevents unauthorized images from running on platform resources and mitigates potential risks to the cloud platform. |
| Network Security Management Center | 1. You can manage cross-boundary network access of cloud platform products in both single-region and cross-region scenarios.<br>2. You can isolate individual products and services on the cloud platform by configuring settings such as IP allowlists/blocklists and specifying exempt products.<br>3. You can enable host network isolation to control external access to the internal host network.<br>4. You can manage device network access to Apsara Stack. |
| Account Security | 1. You can manage server passwords, such as periodically or manually updating passwords and viewing previous passwords.<br>2. You can view and manage boundary interaction policies between the cloud platform and external systems, including products, services, IP addresses, and ports used for interactions. You can also apply boundary protection policies to boundary devices to ensure they take effect.<br>3. You can configure and monitor the Platform Credential Management (PCM) service, and perform emergency response actions. |
| Access Control | 1. Security Policy allows you to change the account policy, password policy, change policy, and data masking policy.<br>2. You can configure login policies, including IP address allowlist/blocklist settings and policy effective time.<br>3. You can configure two-factor authentication for login.<br>4. You can configure the privacy policy content. |
| Security Compliance Center | 1. You can use the cipher insight platform to quickly obtain information such as the status of enabled cryptographic features, cryptographic application configurations, and encrypted message analysis results. This provides a rapid overview of the cloud platform's cryptographic capabilities.<br>2. You can collect compliance evidence chains for various cryptographic application scenarios by running cryptographic application detection tasks, which supports the cloud platform in passing commercial cryptographic evaluations.<br>3. You can configure encryption algorithms used for storage encryption and integrity protection.<br>4. You can use SM algorithms (Chinese commercial cryptographic algorithms) to encrypt metadatabase data at rest. Additionally, you can enable encryption at rest for logs, enable OSS server-side encryption for ECS snapshots, encrypt platform access and transmission, and enable full-state encryption for sensitive data.<br>5. You can verify the Chinese cryptographic signature of ECS public images to implement integrity checks. |
| Platform Cert Manager | 1. You can manage and view platform certificate assets, including those managed by tianji and those detected through network asset scanning.<br>2. You can manage certificate update tasks to handle operations such as certificate issuance, binding, and distribution.<br>3. You can view and download certificate chains within the platform. |

**System Config**

| Module | Description |
| --- | --- |
| System Config | 1. You can change the platform language, switch between light and dark modes, enable page watermarks, and customize the browser icon, platform logo, login page, version information, and copyright notice.<br>2. You can manage the coverage of internationalized texts for products and applications.<br>3. You can manage built-in cards and your own cards.<br>4. You can view the cloud platform's authorization information.<br>5. You can manage message notifications for the cloud platform, including configuring channels for message notifications and viewing message push records.<br>6. You can configure latitude and longitude coordinates for multiple regions in a multi-region scenario.<br>7. You can configure third-party authentication settings to implement login authorization for the cloud management platform acting as a Service Provider (SP). In this case, the SAML 2.0 protocol is supported.<br>8. You can back up Apsara Stack metadata to enable quick recovery from Apsara Stack failures. |

**User Authorities**

| Module | Description |
| --- | --- |
| User Authorities | 1. User Management allows you to create, modify, and delete users, associate login policies with users, view basic information about users, and extend account validity period.<br>2. User Group Management allows you to add multiple users to a single user group and assign identical roles to them for unified management. You can create, edit, and delete user groups, manage group membership by adding or removing users, and assign or modify roles for existing user groups.<br>3. Role Management allows you to create, modify, and delete roles, while also viewing the platform's built-in basic roles.<br>4. Department Management allows you to create, modify, delete, and search for departments. You can also create users and user groups under specific departments.<br>5. In multi-region scenarios, system administrators can associate departments with specific regions. Once associated, users in the department can perform O&amp;M operations on resources within that region.<br>6. Menu Management allows you to add, hide, modify, or delete menus. |
