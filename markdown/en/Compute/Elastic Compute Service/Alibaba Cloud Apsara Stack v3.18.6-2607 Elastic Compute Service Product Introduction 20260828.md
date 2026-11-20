Alibaba Cloud  
Apsara Stack  
Elastic Compute Service  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.ECS](#section-1)
    - [1.1. ECS](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.ECS

Elastic Compute Service (ECS) is an IaaS offering on Alibaba Cloud that provides high-performance, stable, reliable, and scalable compute capacity in the cloud. You can create as many or as few ECS instances as needed to respond to changes in the requirements or popularity of your workloads.

<a id="section-1-1"></a>

## 1.1. ECS

Elastic Compute Service (ECS) is a computing service that provides scalable processing capabilities. It is easier to manage and more user-friendly than physical servers. You can create or release ECS instances and resize disks on demand anytime.

An ECS instance is a virtual computing environment that contains the basic components of computers such as the CPU, memory, and storage. Operations can be performed on ECS instances. Instances are core components of ECS. You can perform operations on instances in the ECS console. Other resources such as block storage devices, images, and snapshots can only be used after they are integrated into ECS instances.

**Instances**

An instance is the smallest computing service unit of ECS. Instance types comprise varying combinations of compute, memory, and storage capacity. An ECS instance is a virtual server that includes basic components such as CPUs, memory, an operating system (OS), network configurations, and disks. You can use management tools provided by Alibaba Cloud such as the ECS console and ECS API to create and manage ECS instances. You can manage the status of ECS instances and their deployed applications in the same manner as you would do with local servers. You can also upgrade compute, network, or storage resource specifications of your ECS instances as your requirements increase.

ECS provides a variety of instance families, such as shared instance families, dedicated instance families, instance families equipped with local HDDs, instance families equipped with local SSDs, and heterogeneous computing instance families. An instance family consists of one or more instance types that have similar attributes. ECS also provides innovative instance families that are developed based on state-of-the-art virtualization technology of Alibaba Cloud, such as ECS Bare Metal Instance families and super Computing Cluster (SCC) instance families.

- **ECS Bare Metal Instance**

  ECS Bare Metal Instance is an innovative cloud computing service developed by Alibaba Cloud on top of SHENLONG architecture that integrates hardware and software. ECS Bare Metal Instance combines virtual machine features (such as elasticity of resources, resource delivery within minutes, and automated O&M) and physical machine features (such as performance consistency, hardware feature sets, and strong hardware-level isolation). ECS Bare Metal Instance is compatible with services in the Alibaba Cloud ecosystem and can help enterprises migrate their critical and high-load applications to the cloud.

- **SCC**

  On top of ECS Bare Metal Instance families, SCC instance families use CPU-based devices and heterogeneously accelerated devices (such as GPU-accelerated devices) that are connected by high-speed InfiniBand (IB) networks to provide high-performance and highly parallel computing cluster services. SCC instance families are suitable for scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analysis, and audio and video processing.

**Block storage**

Block storage is a random block-level storage service that features low latency, high durability, and high reliability. Alibaba Cloud provides a variety of block storage devices, such as Elastic Block Storage (EBS) devices based on a distributed storage architecture and local storage located on the same physical machine that hosts the associated ECS instances.

- **EBS**

  EBS devices, also known as cloud disks, provide block-level random storage that features low latency and high performance, durability, and reliability for ECS instances. EBS devices use the triplicate distributed storage mechanism to ensure data durability for ECS instances. EBS devices can be created, released, and resized anytime.

- **Local storage**

  Local storage, also known as local disks, are temporary disks attached to physical machines that host ECS instances. Local storage is designed for business scenarios that require high storage I/O performance. Local storage provides block-level data access capabilities for instances and provide low latency, high random IOPS, and high throughput.

- **Disk resizing**

  You can resize disks to meet increasing storage requirements as your business and application data grow. You can resize the system disk or data disks of an instance online or offline. After you resize a disk of an instance offline, you must restart the instance for the resize operation to take effect.

- **Disk encryption**

  Disk encryption is a simple and secure method to encrypt new disks. Disk encryption eliminates the need to create or maintain your own key management infrastructure, to modify existing applications and maintenance procedures, and to perform additional encryption operations. Disk encryption does not have negative impacts on your business.

  Disk encryption can be used to encrypt the following types of data:

  - Data on disks.

  - Data transmitted between disks and instances. Data within instance operating systems is not encrypted.

  - All snapshots created from an encrypted disk.

**Images**

An image is a running environment template of ECS instances. An image includes an operating system and pre-installed applications.

An image is a copy of data from one or more disks. An instance image can contain data from only the system disk or from both system and data disks. You can use an image to create an ECS instance or replace the system disk of an ECS instance.

**Snapshots**

A snapshot is a point-in-time backup of a disk. The snapshot service is typically applied to scenarios such as environment replication and disaster recovery and backup.

- **Scenarios**

  - Environment replication

    When you write and store data on a disk, you can create a snapshot for the disk and use the snapshot to create a disk. The new disk contains all data that was present on the original disk when the snapshot was created.

  - Disaster recovery and backup

    Disks are a secure storage method that ensures no data is lost. If incorrect data is stored on a disk due to specific reasons (such as application errors or malicious read and write operations performed by hackers exploiting application vulnerabilities), you can create a snapshot for the disk on a regular basis to restore the disk to a desired state.

- **Snapshot-consistent groups**

  You can create a snapshot-consistent group to simultaneously create snapshots for one or more disks attached to an ECS instance. When a business system spans multiple disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data.

  - You can use snapshot-consistent groups to simultaneously create snapshots for multiple disks on an ECS instance.

  - Snapshot-consistent groups are applicable to cluster services.

  - After a snapshot-consistent group is created, you can use it to roll back one or more disks in the event of system failures or data errors caused by accidental operations.

- **Automatic snapshot policies**

  Automatic snapshot policies can be applied to system disks and data disks to create snapshots for the disks on a periodic basis. You can use automatic snapshot policies to improve data security and tolerance against accidental operations. Automatic snapshot policies can effectively eliminate risks associated with manual snapshots:

**Deployment sets**

Deployment Set is a service provided by ECS that allows you to view the physical topology of hosts, racks, and vSwitches. You can select deployment policies based on your business requirements to improve the reliability and performance of your business.

When you use multiple ECS instances in the same zone, you can use a deployment set to distribute the instances differently to improve business reliability or network performance.

- Improve business reliability

  To prevent the impacts caused by the failure of physical hosts, racks, or vSwitches, you can use deployment policies of deployment sets to distribute ECS instances that host identical applications across different physical hosts, racks, or vSwitches.

- Improve network performance

  In scenarios that involve frequent network interactions between ECS instances, you can use deployment policies of deployment sets to associate the instances with the same vSwitch to achieve low-latency and high-bandwidth communication between the instances.

**Networks**

- **VPCs**

  A virtual private cloud (VPC) is a custom private network that is established on Alibaba Cloud. VPCs are logically isolated from each other based on tunnels. You can create and manage cloud service instances in VPCs, such as ECS instances, and ApsaraDB RDS instances.

  Each new ECS instance in a VPC is assigned a private IP address based on the CIDR block of the VPC and the CIDR block of the vSwitch to which the instance is connected.

- **EIPs**

  An elastic IP address (EIP) is a public IP address that you can purchase and use as an independent resource. After an EIP is associated with an ECS instance, the instance can use the EIP to communicate with the Internet. EIPs can be associated with or disassociated from ECS instances. EIPs can also be deleted or have their public bandwidth modified.

- **ENIs**

  An elastic network interface (ENI) is a virtual network interface controller (NIC) that can be bound to an ECS instance. You can use ENIs to deploy high-availability clusters and perform low-cost failover and fine-grained network management.

**Security groups**

A security group acts as a virtual firewall to control the inbound and outbound traffic of ECS instances to improve security. Security groups provide Stateful Packet Inspection (SPI) and packet filtering capabilities. You can use security groups and security group rules to define security domains in the cloud.

- You can add or modify security group rules based on your business needs to implement finer-grained access control. Security group rules can be used to control access to or from specific IP addresses, CIDR blocks, security groups, or prefix lists.

- New and modified rules in each security group are automatically applied to all instances that are associated with the security group.

- If an instance belongs to multiple security groups, the rules of all the security groups are applied to the instance. When an access request destined for the instance is detected, the request is matched against applied security group rules one by one based on the rule attributes such as protocol, port range, and priority. No sessions are established until an Allow rule matches the request.

**Tags**

Tags are used to identify resources. Each tag consists of a key and a value. You can use tags to categorize ECS instances for easy search and management. When the number of ECS instances increases, you can use tags to manage, group, and categorize resources so that you can quickly search for and perform batch operations on the resources. For example, you can replace images to deploy applications, upgrade patches, and add security group rules to control network access based on tags.

**Dedicated hosts**

Dedicated Host (DDH) is a specialized solution that Alibaba Cloud provides for enterprise users. DDH offers highly cost-effective features, such as dedicated physical resources, flexible deployment, and rich configurations.

A dedicated host is a cloud host whose physical resources are exclusively reserved for a single tenant. As the only tenant of a host, you do not need to share the physical resources of the host with other tenants. You can obtain the physical attributes of the host, including the number of CPUs, the number of sockets, the number of physical CPU cores, and the memory size. You can also create ECS instances of an instance family on a dedicated host if only the instance family is compatible with the host type.

**Cloud Assistant**

Cloud Assistant is a native automated O&M tool developed for ECS. It allows you to batch maintain ECS instances and batch run commands on and send files to ECS instances in a password-free, logon-free manner without the use of jump servers. These commands can consist of shell, PowerShell, or batch scripts.

Typically, you can use Cloud Assistant to install and uninstall software, start and stop services, distribute configuration files, and run commonly used commands (scripts).

**Key pairs**

Key pairs are a secure and convenient authentication method provided by Alibaba Cloud for ECS instance logons. A key pair consists of a public key and a private key. Only Linux instances support logon based on key pairs.

A key pair is a pair of public and private keys that are generated based on an encryption algorithm. By default, 2048-bit RSA key pairs are used. If you want to log on to a Linux instance by using a key pair, you must first create the key pair. You can specify a key pair when you create an instance, or bind a key pair to an instance after the instance is created. Then, you can use the private key to connect to the instance.

<a id="section-1-2"></a>

## 1.2. Benefits

Compared with data centers or traditional servers, Elastic Compute Service (ECS) is easy to use and offers scalable, secure, and reliable computing capacity.

**High availability**

Compared with traditional servers that are limited by hardware, ECS instances raise the standard for operations and maintenance while integrating features of various cloud services to provide more efficient backup, disaster recovery, and fault recovery capabilities.

Additionally, ECS provides support in the following areas:

- Industry and ecosystem partners to help you build a more advanced and stable architecture.

- Diverse training services to help you implement high availability from the business end to the underlying basic service end.

**Security**

Security and stability are two primary concerns for cloud service users. Alibaba Cloud has received numerous international information security certifications that require strict confidentiality of user data and user privacy protection, including ISO27001 and MTCS Level-3.

- **A virtual private cloud (VPC) enables a wide range of business possibilities.** With a simple configuration, you can enhance the flexibility, stability, and scalability of your business.

- **You can connect your own data centers to Apsara Stack VPCs** using leased lines to build hybrid clouds. You can use a variety of hybrid cloud architectures and network services to provide robust networking.

- **VPCs are more stable and secure.**

  - VPCs allow you to divide, configure, and manage your networks at will.

  - VPCs provide traffic isolation and attack isolation to protect your services against cyberattacks. You can establish a first line of defense against malicious attacks and traffic by deploying your business in VPCs.

- **Comprehensive security protections** are provided for ECS and include security policies, security hardening, data security, monitoring, and alerts to improve the security of your business and defend against external attacks and unauthorized access.

VPCs provide a stable, secure, controllable, and fast-deliverable network environment. The capabilities and architecture of VPC hybrid clouds bring the technical advantages of cloud computing to enterprises in traditional industries that are not engaged in cloud computing.

**Scalability**

Elasticity is a key benefit of cloud computing.

- **Elastic computing**

  - **Vertical scaling**

    Vertical scaling is the process of changing the configurations of individual ECS instances. In a traditional data center, it is difficult to change the configurations of individual servers. However, in Apsara Stack, you can change the configurations of your ECS instances based on your business volume.

  - **Horizontal scaling**

    For sudden business peaks, traditional data centers cannot prepare resources for scaling at any time. The elasticity of cloud computing makes it possible to provide as many resources as required during peak hours. When the load returns to normal levels, you can release redundant resources to reduce operation costs.

    The combination of ECS vertical and horizontal elasticity and Auto Scaling enables you to scale resources up and down by specifying quantities as scheduled or based on business loads.

- **Elastic storage**

  Apsara Stack provides elastic storage. In a traditional data center, you need to upgrade server configurations or replace servers to increase storage space. In Apsara Stack, you can resize attached disks or attach more disks to instances to increase storage space.

- **Elastic network**

  Cloud networks offer great flexibility. You can deploy on demand in Apsara Stack VPCs and flexibly expand or contract network segments. All network configurations are similar to traditional data center configurations. At the same time, you can use physical networks to achieve interconnection between different data centers and security domain isolation between data centers, making VPC configuration and planning very flexible.

In conclusion, Apsara Stack provides elastic computing, storage, networking along with business architecture planning. You can use Apsara Stack to build your business portfolio in any way.

**Ease of use**

Apsara Stack provides an easy-to-use console for centralized management. You can use the console to perform operations on ECS instances and ECS-related services to create instances, activate related services, and modify the configurations of instances and services. Apsara Stack provides the following resources to help you use it easily:

- Diversified instance families such as shared instance families, dedicated instance families, and ECS Bare Metal Instance families.

- VPCs that serve various purposes. You can choose VPCs based on your needs and organization.

- Diversified storage types.

- Easy-to-use security group policies.

Apsara Stack also lets you use images, deploy clusters, use custom tags, migrate virtual machines, and modify configurations.

<a id="section-1-3"></a>

## 1.3. Scenarios

ECS instances can be used either independently as simple web servers or with other Apsara Stack services such as OSS and CDN to provide advanced multimedia solutions. The following sections describe the typical application scenarios of ECS instances:

**Official websites for enterprises and simple web applications**

Initially, official websites for enterprises do not have high volumes of traffic and only require low-configuration ECS instances to run applications and databases and store files. As your website develops, you can upgrade the configurations and increase the number of ECS instances at any time without the need to worry about insufficient resources during traffic spikes.

**Multimedia and high-traffic applications or websites**

When you use ECS instances together with OSS, you can store static images, videos, and downloaded packages in OSS to reduce storage costs. You can also use ECS in combination with CDN or SLB to shorten user response time, reduce bandwidth fees, and improve availability.

**Applications or websites that have large traffic fluctuations**

Some applications and websites may encounter large fluctuations in traffic within a short period of time. ECS provides elastic processing capabilities. The number of ECS instances automatically increases or decreases in response to changes in traffic to meet resource requirements and preserve cost efficiency. ECS can be used in combination with SLB to implement a high availability architecture.

**Databases**

Databases with high I/O requirements are supported. High-configuration I/O optimized ECS instances can be used together with standard SSDs to support high I/O concurrency and higher data reliability. Alternatively, multiple low-configuration I/O optimized ECS instances can be used in combination with SLB to implement a high availability architecture.

<a id="section-1-4"></a>

## 1.4. Features

**Instances**

| Feature | Description |
| --- | --- |

- Shared instance types

  - Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types

  - Suitable for business scenarios that require high performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large numbers of packets are received and transmitted.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

SHENLONG + Intel

- Network-enhanced instance types

  - Optimized for network-intensive scenarios and provide significantly higher network performance than other instance types of the same generation.

- Storage-enhanced instance types

  - Optimized for storage-intensive scenarios and provide optimized Elastic Block Storage (EBS)-related capabilities, such as disk bandwidth and disk IOPS.

- Bare metal

  - Provide robust compute, storage, and network capacities for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing.

  - Support shared block storage and the non-uniform memory access (NUMA) ON and NUMA OFF configurations.

- Shared instance types

  - Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types

  - Suitable for business scenarios that require high performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications,

SHENLONG + Hygon

and scenarios in which large numbers of packets are received and transmitted.

- CPU-to-memory ratios: 1:1, 1:2, 1:4, and 1:8.

- Storage-enhanced instance types

  - Optimized for storage-intensive scenarios and provide optimized Elastic Block Storage (EBS)-related capabilities, such as disk bandwidth and disk IOPS.

  - Bare metal

- Bare metal

  - Provide robust compute, storage, and network capacities for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing.

- GPU-accelerated ECS Bare Metal Instance types

  - Suitable for various deep learning training and development tasks, High-Performance Computing (HPC)-accelerated computing and simulation, image classification, autonomous driving, speech recognition, and other scenarios.

  - Supported GPUs: A10, T4, and V100.

- Pass-through GPU-accelerated instance types

  - Supported GPUs: A10 and T4.

SHENLONG + GPUs

- NVIDIA vGPU-accelerated instance types

  - Provide high-performance CPUs, memory, and GPUs and are suitable for concurrent AI inference tasks, such as image recognition, speech recognition, and behavior identification.

  - Suitable for compute-intensive graphics processing tasks that require high-performance 3D graphics virtualization capabilities, such as remote graphic design.

  - Supported GPUs: T4 and A10.

- Big data instance types (d series)

  - Suitable for big data computing and storage scenarios that involve services such as Hadoop MapReduce, Hadoop Distributed File System (HDFS), Hive, and HBase, and search and log data processing scenarios in which solutions such as Elasticsearch and Kafka are used.

  - CPU-to-memory ratio provided by certain instance types: 1:4.

SHENLONG + Local disks

- Instance types with local SSDs (i series)

  - Suitable for online transaction processing (OLTP) and high-performance relational databases, NoSQL databases such as Cassandra and MongoDB, search scenarios in which solutions such as Elasticsearch is used, and E-MapReduce big data scenarios such as storage and compute decoupling.

  - CPU-to-memory ratios: 1:4 and 1:8.

- Shared instance types

  - Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types

  - Suitable for business scenarios that require high performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large numbers of packets are received and transmitted.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Network-enhanced instance types

  - Applicable scenarios:

    - Network-intensive scenarios such as Network Functions Virtualization (NFV) or Software-defined Wide Area Network (SD-WAN), mobile Internet, live video commenting, and telecom data forwarding.

Instance type

- Small and medium-sized database systems, caches, and search clusters.

- Enterprise applications of various types and sizes.

- Provide ultra-high packet forwarding rates.

Intel

- CPU-to-memory ratios: 1:2 and 1:4.

- Burstable instance types

  - Provide baseline CPU performance with the ability to burst above the baseline by spending CPU credits. These instance types are suitable for business scenarios in which performance requirements are not high, such as web applications and small and medium-sized websites.

  - Support only Proof of Concept (PoC).

- Security-enhanced instance types

  - Provide enhanced data security protection based on technologies, such as trusted computing and confidential computing.

  - Implement trusted boot based on TCM or TPM chips. During a trusted boot, all modules in the boot chain from the underlying server to the guest operating system are measured and verified.

  - Applicable scenarios:

    - Scenarios that involve sensitive information such as personal identity information, healthcare information, financial information, and intellectual property data.

    - Scenarios in which confidential data is shared among multiple parties.

    - Blockchains.

    - Confidential machine learning.

    - Scenarios that require high security and trust, such as services for financial organizations, public service sectors, and enterprises.

    - Enterprise applications of various types and sizes.

- Shared instance types

  - Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types

  - Suitable for business scenarios that require high

Hygon

performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large numbers of packets are received and transmitted.

- CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Network-enhanced instance types

  - Optimized for network-intensive scenarios and provide significantly higher network performance than other instance types of the same generation.

- Shared instance types (Kunpeng)

  - Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types (Kunpeng)

  - Suitable for business scenarios that require high performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large numbers of packets are received and transmitted.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Shared instance types (Phytium)

ARM

- Suitable for business scenarios where low performance is acceptable, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and comprehensive application services.

- CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Dedicated instance types (Phytium)

  - Suitable for business scenarios that require high performance, such as frontend web servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large numbers of packets are received and transmitted.

  - CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8.

- Pass-through GPU-accelerated instance types

  - Supported GPUs: V100, A10, T4, A2, A16, MLU370, DCU Z100L, K100, Enflame I20, Atlas300I Pro, and Atlas300T GPUs.

- vGPU-accelerated instance types

GPU

- Suitable for real-time rendering of cloud games and AR and VR applications, AI (deep learning and machine learning) inference, Internet services involving AI inference, and educational environments and modeling experiment environments of deep learning.

- Supported GPUs: T4 and A10.

- Big data instance types (d series)

  - Suitable for big data computing and storage scenarios that involve services such as Hadoop MapReduce, Hadoop Distributed File System (HDFS), Hive, and HBase, and search and log data processing scenarios in which solutions such as Elasticsearch and Kafka are used.

Local disks

- Instance types with local SSDs (i series)

  - Suitable for online transaction processing (OLTP) and high-performance relational databases, NoSQL databases such as Cassandra and MongoDB, search scenarios in which solutions such as Elasticsearch is used, and E-MapReduce big data scenarios such as storage and compute decoupling.

Support up to 512 GB of

Instance types can provide up to 512 GB of memory.

memory

Enable or disable

You can enable or disable instance types in the Apsara

instance types

Uni-manager Operations Console.

You can disable HT for dedicated ECS clusters in the

Disable Hyper-

Apsara Uni-manager Operations Console to allow ECS

Threading (HT)

instances to exclusively occupy physical CPU cores for better performance.

ECS caches the system logs of instances at the time of the last startup, restart, or shutdown events, and lets you obtain the screenshots of your instances in real

View system logs and

time. You can use these features to analyze and

Instance type

screenshots

troubleshoot instance issues, such as unresponsive

management

operating systems, abnormal restart, or instance connection failures.

The format of a custom instance type is  `instance`

```text
family.c(number of CPU cores)m(memory 
```

Customize instance

`size).customize.XXX` , where  `XXX`  is a manually

specifications and

entered description of the custom instance type. You can

performance to create

set a custom name, the number of vCPUs, and the

custom instance types

memory size for an instance type. Parameters such as network bandwidth, packet forwarding rate, and multi-queue are automatically generated.

You can check the affinity of deployment sets in the Apsara Uni-manager Management Console. If ECS

Anti-affinity

instances breach the anti-affinity (strict dispersion)

visualization

constraints, the deployment set is marked red and can be restored with a few clicks.

Constraint relationship monitoring and reporting are supported. When ECS instances are not distributed as expected, the system can detect the issue, record it, and

Anti-affinity

Anti-affinity scheduling

notify the O&M administrator. O&M administrator can

and affinity scheduling

configure automatic hot or cold migration for ECS instances or manually migrate them to restore scheduling constraints.

If anti-affinity does not take effect, you can perform hot-migration scheduling based on the pre-configured anti-

Anti-affinity correction

affinity policy when physical resources become available.

You can add dedicated hosts to dedicated host groups to

Dedicated host group

simplify host management.

A dedicated host is a cloud host whose physical resources are reserved exclusively for a single tenant.

DDH

Dedicated host

ECS instances that are created on a dedicated host are physically isolated from ECS instances created on other dedicated hosts.

Share dedicated hosts

The account to which dedicated hosts belong can share

across level-1 accounts

the hosts with other level-1 accounts.

Classify ECS instances

You can classify ECS instances based on tags.

based on tags

You can view and modify the CPU topologies of ECS instances to improve performance and parallelism and

View and modify CPU

optimize resource allocation in various scenarios, such as

topologies

virtualization environments, multi-threaded programming, and HPC.

You can perform up to four consecutive hot configuration changes on a shared or dedicated instance to increase its memory size. This limit does not apply to the CPU

Perform hot upgrade

specifications. If you attempt to perform the fifth

for instance types

consecutive change, it will fail with an error reported. In this case, you must restart the instance to reset the hot configuration change count.

Hot expansion (online

You can resize the system disk and data disks of an ECS

resizing) of system

instance online without restarting the instance.

disks and data disks

Online resizing of

You can resize shared disks online.

shared disks

- Only disks that are based on Apsara Distributed File System 2.0 support configuration changes.

- The following online category changes are supported by disks:

Instance management

- Change standard SSDs to ultra disks, premium performance disks, or standard performance disks

Hot reconfiguration of

online.

I/O specifications for

- Change ultra disks standard SSDs, premium

disks

performance disks, or standard performance disks online.

- Change premium performance disks to standard performance disks online.

- Change standard performance disks to premium performance disks online.

Batch hot-upgrade of

You can hot-upgrade multiple ECS instances to a specific

ECS instances

instance type at a time.

Online cloning of ECS

You can use a CloudOps Orchestration Service (OOS)

instances

template to clone ECS instances online.

Batch clone ECS

You can clone an ECS instance online to create multiple

instances online

identical ECS instances.

Offline cloning of ECS

You can use an OOS template to clone ECS instances

instances

offline.

Mount CD-ROMs for

You can mount ISOs for system recovery.

system recovery

<table>
  <tr>
    <td rowspan="4">Recycle bin</td>
    <td>Recycle ECS instances</td>
    <td>The recycle bin protects ECS instances against accidental deletions to ensure business continuity and improve O&amp;M and production security. Deleted ECS instances can be retained in the recycle bin for a specific period of time. You can restore them from the recycle bin at any time before their retention period ends. After the retention period ends, they are permanently deleted and cannot be restored.</td>
  </tr>
  <tr>
    <td>Set the retention period</td>
    <td>When ECS instances are moved to the recycle bin, they enter a retention period.</td>
  </tr>
  <tr>
    <td>Restore ECS instances</td>
    <td>You can restore ECS instances within their retention period.</td>
  </tr>
  <tr>
    <td>Permanent deletion</td>
    <td>You can permanently delete ECS instances that you no longer need from the recycle bin.</td>
  </tr>
</table>

**Images**

| Feature | Description |
| --- | --- |
| Anolis | • Anolis OS 7.9 ANCK<br>• Anolis OS 7.9 ANCK (Level 3 of MLPS 2.0)<br>• Anolis OS 8.4 ANCK<br>• Anolis OS 8.4 ANCK (UEFI)<br>• Anolis OS 7.9 ANCK for Arm<br>• Anolis OS 7.9 ANCK for Arm (Level 3 of MLPS 2.0)<br>• Anolis OS 8.4 ANCK for Arm<br>• Anolis OS 8.6 ANCK for Arm (Level 3 of MLPS 2.0)<br>• Anolis OS 8.6 ANCK for Arm |
| Alibaba Cloud Linux | • Alibaba Cloud Linux2<br>• Alibaba Cloud Linux3 |

<table>
  <tr>
    <td>CentOS</td>
    <td>• CentOS 7.2<br>• CentOS 7.3<br>• CentOS 7.4<br>• CentOS 7.5<br>• CentOS 7.5 (SCC)<br>• CentOS 7.6<br>• CentOS 7.7<br>• CentOS 7.8 (Trusted)<br>• CentOS 7.9<br>• CentOS 7.9 (SCC)<br>• CentOS 7.9 (UEFI)<br>• CentOS 7.9 for Arm</td>
  </tr>
  <tr>
    <td>CentOS Stream</td>
    <td>CentOS Stream 8</td>
  </tr>
  <tr>
    <td>AlmaLinux</td>
    <td>• AlmaLinux 8.5<br>• AlmaLinux 8.6<br>• AlmaLinux 9</td>
  </tr>
  <tr>
    <td>Rocky Linux</td>
    <td>• Rocky Linux 8.5<br>• Rocky Linux 8.6<br>• Rocky Linux 9</td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>• Debian 9.6<br>• Debian 9.9<br>• Debian 9.13<br>• Debian 9.13 (UEFI)<br>• Debian 10.10 (UEFI)<br>• Debian 10.12<br>• Debian 10.12 (UEFI)<br>• Debian 11.4</td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>• Ubuntu 16.04<br>• Ubuntu 18.04<br>• Ubuntu 18.04 (UEFI)<br>• Ubuntu 22.04<br>• Ubuntu 20.04 (UEFI)</td>
  </tr>
  <tr>
    <td>OpenSUSE</td>
    <td>• OpenSUSE 15.3<br>• OpenSUSE 15.4</td>
  </tr>
</table>

- SUSE Linux Enterprise Server 11 SP4

- SUSE Linux Enterprise Server 12 SP4

SUSE Linux

- SUSE Linux Enterprise Server 12 SP5

- SUSE Linux Enterprise Server 15 SP2

- Windows Server Version 2004 Datacenter 64-bit (Simplified Chinese)

- Windows Server Version 2004 Datacenter 64-bit (English)

- Windows Server 2012 R2 Datacenter 64-bit (Simplified Chinese)

- Windows Server 2012 R2 Datacenter 64-bit (English)

- Windows Server 2016 Datacenter 64-bit (Simplified Chinese)

Windows Server

- Windows Server 2016 Datacenter 64-bit (English)

- Windows Server 2019 Datacenter 64-bit (Simplified Chinese)

- Windows Server 2019 Datacenter 64-bit (English)

- Windows Server 2022 Datacenter 64-bit (Simplified Chinese)

- Windows Server 2022 Datacenter 64-bit (English)

- Kylin V10 SP1 0518

- Kylin V10 SP1 (UEFI)

- Kylin V10 SP2 0524

Kylin

- Kylin V10 SP2 0524 (UEFI)

- Kylin V10 SP1 0518 for Arm

- Kylin V10 SP2 0524 for Arm

- UOS Server 20 1002a

- UOS Server 20 1040d

- UOS Server 20 1050d

- UOS Server 20 1050d (UEFI)

UOS

- UOS Server 20 1050a

- UOS Server 20 1002a for Arm

- UOS Server 20 1040d for Arm

- UOS Server 20 1050d for Arm

- UOS Server 20 1050a for Arm

NFS

Founder High-Trust Server Operating System V4

Public images

The public images provided by Alibaba Cloud in Apsara Stack support almost all Windows Server operating systems and mainstream Linux operating systems.

Enterprise public images are custom images globally shared by administrators in the Apsara Uni-manager Operations Console. Enterprise public images have the following characteristics:

Enterprise public images

- Enterprise public images appear in the list of globally shared images for each organization.

- Enterprise public images can be modified only by their sharers.

Encrypt public

You can encrypt public images using the SM2 and SM3 algorithms in

images

the Apsara Uni-manager Operations Console for integrity protection.

You can create ECS instances from encrypted custom images to meet

Encrypt custom

compliance requirements for data security. The system disks of the

images

created instances are automatically encrypted.

Support for UEFI

You can enable the Unified Extensible Firmware Interface (UEFI) boot

boot mode

mode for custom images.

You can use custom images to create ECS instances with identical configurations. This eliminates the need to make repeated

Custom Images

configurations. Custom images include images created based on ECS instances or snapshots and images imported from on-premises machines.

- You can deprecate public images in the Apsara Uni-manager Operations Console. After a public image is deprecated, the image

Publish and

can still be found based on its ID but is no longer included in the

deprecate

image list.

images

Image

- You can publish deprecated public images.

manage ment

You can import and export images in multiple formats, including RAW, VHD, and QCOW2. After you upload an image from your computer to an Object Storage Service (OSS) bucket, you can import the image as a custom image to ECS. You can also export a custom

Import and

image to an OSS bucket and then download the image to your

export images

computer.

When you export a custom image, you cannot change its format. For example, you can export RAW-formatted custom images only in the RAW format.

You can share a custom image with other organizations. The

Share and

organizations can use the shared image to create ECS instances with

unshare images

identical environments. You can also unshare a shared image.

You can update images for ECS instances by replacing the operating

Update images

systems of the instances.

Disable the ISO

- You can upload and mount ISOs in the Apsara Uni-manager

feature

Operations Console. After you mount an ISO to an ECS instance, you can start the instance from the ISO.

- You can unmount CD-ROMs from ECS instances in the Apsara Uni-manager Operations Console.

- You can import images in the VMDK format in the Apsara Uni-manager Management Console.

Import images in

- You can convert images from the VMDK format to the RAW format.

the VMDK format

- You can create ECS instances from imported custom images.

**Snapshots**

| Feature | Description |
| --- | --- |
| View and modify the name and description of a snapshot | You can view the information about created snapshots and modify their names and descriptions. |
| Instant access (IA) | Snapshots for which the IA feature is enabled can be used instantly after creation to create or restore cloud disks. Only premium performance disks support the IA feature. |
| Snapshot-consistent group | You can create a snapshot-consistent group to simultaneously take snapshots for multiple cloud disks on one or more ECS instances. If a business system involves multiple cloud disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data. |
| Cross-instance snapshot-consistent group | You can create a snapshot-consistent group to simultaneously take snapshots for multiple cloud disks on one or more ECS instances. If a business system involves multiple cloud disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data. |
| View snapshot chain information | You can view the information about a snapshot chain. |
| Share snapshots across tenants | • You can share snapshots with other accounts.<br>• The accounts can use the shared snapshots to create cloud disks. |

**Security groups**

| Feature | Description |
| --- | --- |
| Maximum number of security group rules | The maximum number of security group rules associated with an elastic network interface (ENI) can be increased to 1,000. |
| Import and export security group rules | • You can import security group rules to security groups. You can import a backup file of security group rules from your computer to a security group to create or restore security group rules.<br>• You can export security group rules as Excel files to your computer for on-premises backup. |
| Clone security group rules | You can clone a security group rule to quickly create a similar rule. |
| Aggregate security group rules | You can use parameter templates to create security group rules.Parameter templates are classified into IP address parameter templates and port parameter templates. |
| Support for port groups | You can configure port groups in security group rules. |
| Support for IP groups | You can configure IP groups in security group rules. |
| Managed security groups | Apsara Stack services can create managed security groups. You can view managed security groups but you cannot perform other operations. |
| Security group rule check | You can use the security group rule check feature to check whether a security group allows and denies access as expected. |
| Scheduled security group tasks | You can create a scheduled task for a security group to dynamically add ECS instances to or remove ECS instances from the security group at the specified effective time or expiration time. |
| Audit operation logs | You can view the operation logs of security groups. The operation logs include information about each operation performed on the security groups, such as the operation name, operator, execution status, operation source (console operation or API call), operation type, source IP address, and operation time. |
| Audit security group logs | You can view the historical operations performed in the Apsara Uni-manager Operations Console, historical POP API calls, and historical Server Controller API calls for security groups. |

**Self-service and O&M platforms**

**Feature**

**Description**

Workbench

You can log on to ECS instances using Workbench.

SSH key pair-based

You can log on to ECS instances using SSH key pairs.

logon

Logon

Termination of Virtual

management

When you delete or disable a VNC, the VNC logon

Network Computing

session is closed.

(VNC) logon sessions

When you create an ECS instance, you can create a non-

Create a non-

administrator account named ecs-user for the instance

administrator account

and specify a password for the account.

Create and run Cloud

You can run Cloud Assistant commands to perform

Assistant commands

routine tasks on ECS instances. The tasks include running automated O&M scripts, polling processes, resetting user passwords, installing or uninstalling software, updating applications, and installing patches. The Cloud Assistant commands can be batch or PowerShell commands for Windows instances and shell commands for Linux instances. You can specify custom parameters as variables in the Cloud Assistant

Cloud

commands.

Assistant

Upload files

You can upload files, such as configuration files and scripts, from on-premises machines to ECS instances.

Cloud Assistant plug-ins

You can use Cloud Assistant plug-ins to make complex configurations by running simple commands. This improves O&M efficiency.

You can change the CPU overcommit ratio of a shared

Super-

Customize the CPU

cluster or NC in the Apsara Uni-manager Operations

resolution

overcommit ratio

Console.

- Intelligently diagnoses issues with running ECS instances and analyzes their possible causes.

AI instance diagnosis

- Provides troubleshooting steps and repair suggestions.

Provides best practice configuration suggestions and

Instance type

ECS instance type recommendations for migrating your

recommendation

Compute AI

different services to the cloud.

Assistant

You can enter a resource ID to automatically query the

Intelligent resource

status and information of the resource and obtain

query

information about its associated resources.

If ECS instances are affected by updates, maintenance, or detected system failures, O&M submits an off-peak migration task. The task analyzes the off-peak business

Off-peak migration

O&M events

hours and informs users in advance of the impact on

events

their instances and the planned execution time. This allows users to prepare before the event is executed to reduce business losses.

**High availability (HA)**

**Feature**

**Description**

With specific configurations, service interruptions caused

Hot migration time

by a hot migration task last up to 100 milliseconds.

Uninterrupted persistent connections

Persistent connections are not interrupted when ECS

during the hot

instances that are associated as backend servers with

migration of ECS

SLB instances are being hot-migrated.

instances associated with Server Load Balancer (SLB) instances

- You can create a batch migration task to batch migrate multiple ECS instances.

Batch hot-migrate

- To improve the success rate of batch migration tasks,

multiple ECS instances

we recommend that you select ECS instances of the same instance family.

- You can create batch migration tasks to drain virtual machines in multiple hosts with one click.

- You can check whether all ECS instances are migrated from the specified hosts in real time.

Delete host

- After the batch machine migration task is completed, you can view the task logs for the task details, including the source and destination NCs, whether all ECS instances are migrated from the source NCs, the migration duration, and the reason why ECS instances fail to be migrated from a source NC.

- You can create a cluster migration task to drain VMs in a cluster.

- You can check whether all ECS instances are migrated from all hosts in the cluster in real time.

Migrate all ECS instances from all hosts

- After the cluster-level migration task is completed, you

in a cluster

can view the task logs for the task details, including the source and destination NCs, whether all ECS instances are migrated from the source NCs, the migration duration, and the reason why ECS instances fail to be migrated from a source NC.

Select and hot-migrate

You can select multiple ECS instances in the ECS

multiple ECS instances

instance list for batch migration.

at a time

Hot migration

Maximum migration

You can specify a maximum migration rate for ECS

rate for ECS instance

instance hot migration tasks.

hot migration tasks

- You can create a machine migration, also known as host-level or computing server-level migration task, to migrate all ECS instances from a host to other hosts.

Migrate all ECS

- Before you run the machine migration task, a pre-

instances from a host

migration check can be performed to check resource availability.

- You can set the migration rate and concurrency level for the migration task.

Cross-vendor hot

You can hot-migrate ECS instances with the same

migration of ECS

instruction set across CPUs of different vendors and

instances with the

mask or hot-add instruction sets.

same instruction set

- When you create a batch migration task, you can

In-batch, batch, and

enable in-batch migration and scheduled migration for

scheduled hot

the task.

migration of ECS

- You can create a batch migration task to batch

instances

migrate multiple ECS instances.

You can perform a precheck before migration to check the current traffic volume or whether the ECS instance memory refresh rate may cause migration failures. There-migration check lets you predict whether

Pre-migration check

migration tasks will be successful and provides suggestions for specific limits, such as scaling up NCs, repairing faulty NCs, or performing migration during off-peak periods.

- You can view the logs of an ECS instance migration task, cluster-level migration task, machine migration task, or batch machine migration task for the task

Migration logs

details, such as the task start time, the migration duration, and whether the task is successful.

- You can retain the logs permanently or as needed.

- You can view the progress, dirty page rate, and migration rate of hot migration tasks.

View the progress of hot migration tasks

- You can cancel hot migration tasks.

The interval between when a host failure is detected and

ECS instance downtime

when ECS instances are failed over to a different host is

less than 90 seconds

less than 90 seconds.

The failover capability is provided to achieve high availability in scenarios such as kernel crashes, system

Host memory leaks

hangs, and NICs repeatedly going up and down. The ECS instance restart time is less than 60 seconds.

The failover capability is provided to achieve high availability in scenarios such as VM GuestOS memory leaks, kernel crashes, system hangs, and NICs

VM GuestOS

repeatedly going up and down. The ECS instance restart time is less than 60 seconds.

Disable HA

You can disable the HA feature for ECS instances.

- You can export the details of physical machine events.

- The export file of non-downtime events includes the following fields: event ID, instance ID, instance name, affected physical machine IP address, cluster, tenant account ID, event type, affected GPUs, affected

Convergence and

memory size, occurrence time, and virtual private

visualization of

cloud (VPC).

downtime events

- The export file of downtime events includes the following fields in addition to the fields in the export

Cold migration

file of non-downtime events: migration result, migration status, destination physical machine IP address, and source physical machine ID.

When ECS instance crashes are detected, alerts are

ECS instance crash

generated.

alert (Windows blue screen detection)

- You can associate reserved CPU and memory resources with ECS instances on the relevant management page. When a host fails and triggers virtual machine HA, make sure that the computing clusters have sufficient idle resources.

Resource reservation

- The system ensures that computing clusters have

for minimizing

sufficient available resources to support virtual

downtime

machine HA when a host failure occurs. You can also configure a dedicated failover host on the relevant management page, so that when a host failure triggers virtual machine HA, the HA service can be started using the dedicated failover host.

Failover triggered by

When an OOM error is detected on an ECS instance,

out-of-memory (OOM)

failover is performed.

errors on ECS instances

Hot standby disk for ECS

Hot standby disk for

Hot standby disks are provided to replace damaged local

instances

ECS instances equipped

disks on ECS instances.

equipped with

with local disks

local disks

Repair of local

Repair of local disks on

disks on ECS

Local disks on ECS instances can be separately repaired.

ECS instances

instances
