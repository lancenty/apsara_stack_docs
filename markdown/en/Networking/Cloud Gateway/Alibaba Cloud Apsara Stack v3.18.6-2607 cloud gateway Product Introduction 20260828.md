Alibaba Cloud  
Apsara Stack  
cloud gateway  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Cloud Gateway](#section-1)
- [2.Product Details](#section-2)
- [3.Product Value](#section-3)
- [4.Features](#section-4)

<a id="section-1"></a>

# 1.Cloud Gateway

Cloud Gateway (CGW) is designed to provide scenario-specific network services to help you efficiently build hybrid clouds and migrate workloads to the clouds. CGW is an ideal service for migrating your infrastructure from a public or private cloud to a hybrid cloud.

<a id="section-2"></a>

# 2.Product Details

The Cloud Access Gateway provides network services for specific scenarios. It helps customers quickly migrate to the cloud and flexibly build hybrid clouds. This service meets the diverse requirements that arise as cloud infrastructure evolves from private or public clouds to hybrid clouds.

**Open Network Service Platform**

This platform provides lifecycle management for third-party virtual network services, such as Server Load Balancer, firewall, and network performance management, based on network functions virtualization (NFV). The platform follows ETSI standards to standardize onboarding, ensure high availability (HA), enable rapid scaling, and support efficient O&M. It delivers virtual network and security services from Alibaba Cloud's ecosystem partners. Key features include the following:

- Initializes virtual network service sets.

- Manages virtual network service clusters.

- Manages network traffic steering policies.

- Monitors virtual network element health and isolates faults.

**Computing Power Platform Networking**

This feature diagnoses nodes in the Computing Power Network (CPN). It performs performance analysis, performance monitoring, network device management, and network monitoring. This provides O&M teams with the data required to help administrators better understand and manage network performance and faults.

**Intelligent Computing Server Access to VPC**

Intelligent computing servers connect to a VPC through the computing power platform access gateway, which is a dedicated CHSW device. This connection enables unified management of intelligent computing server resources. The system supports features such as instance management, operation history, bare metal networking, and O&M configuration. These features are used to perform daily O&M tasks for the computing power platform access gateway.

<a id="section-3"></a>

# 3.Product Value

The Cloud Access Gateway delivers comprehensive, efficient, secure, easy-to-use, and visual network services for Apsara Stack customers.

**Open Network Service Platform**

Provides an open network service platform that enables standard access, rapid deployment, and efficient operations and maintenance (O&M) support for ecosystem network elements.

- Automated Deployment: Supports automated deployment of ecosystem partner virtual network devices through standardization and modeling.

- High Reliability: Supports active/standby high availability cluster models for virtual network devices, with automatic traffic switching during failover.

- Centralized Management: Deploys partner virtual network devices centrally in an independent VPC to achieve centralized management and reduce deployment costs.

**Computing Power Platform Network**

Provides network access capabilities for intelligent computing scenarios, delivering high performance, simplified O&M, flexible access, strong compatibility, and security.

- High Performance: Supports RoCEv2-based RDMA networks, physical dual-plane and virtual multi-plane architectures, and multi-track deployment solutions.

- Easy O&M: Supports over 20 one-click inspection items on the host side, along with performance analysis and testing tools covering communication libraries, bandwidth, and latency. Comprehensive monitoring and alerting coverage on both host and network sides simplifies network operations and maintenance.

- Flexible Access: Supports dual-uplink access for computing nodes and storage nodes to the storage network, and single-uplink or dual-uplink access for computing nodes to the computing network. Supports current mainstream GPU network interface controller (NIC) access methods.

- Compatibility: Switches are compatible with H3C and Ruijie. GPUs support NVIDIA GPUs, Hygon DCUs, and Ascend NPUs.

- Security: Supports ACL-based tenant isolation and secure isolation for multi-tenant traffic.

**Intelligent Computing Server Access to VPC**

Enables intelligent computing server access to a virtual private cloud (VPC).

- Compatibility: Requires no modifications to intelligent computing servers. Supports connecting intelligent computing servers to the VPC network through a forward gateway. Enables reuse of existing servers to protect your investment.

- Unified Management: Integrates with Alibaba Cloud VPC products to connect ECS and intelligent computing servers and provide unified resource management.

- Ease of Use: Integrates with intelligent computing server management to enable unified management and on-demand allocation of intelligent computing server resources. Automatically configures tenant networks for intelligent computing servers when resources are allocated.

- Security: Supports multi-tenant isolation for intelligent computing server networks. Intelligent computing server networks are isolated from the underlying cloud platform network.

<a id="section-4"></a>

# 4.Features

Cloud Access Gateway provides network connectivity services for various scenarios to help enterprises quickly migrate to the cloud and flexibly build hybrid clouds.

**Hybrid Cloud Networking – Platform Side**

**Feature**

**Description**

Automates DNS forwarding and A record configuration for hybrid cloud scenarios.

Dynamic DNS

Includes a management page to improve efficiency when connecting hybrid cloud networks.

Provides network access capabilities for Alibaba Cloud services and VIP or DNS configuration. Enables service interconnection across

Cloud Service

multicloud, IDC, and Apsara Stack

Dynamic VIP

Connectivity

environments. Supports dynamic VIP creation and synchronizes changes with static VIP resources created in Tianji. Offers flexible external service exposure.

Generates specific access matrices for cloud instances using predefined metadata and rules.

Cross-Cloud Access

Provides accurate input for cloud service connectivity and improves hybrid cloud network connectivity efficiency.

Collects and displays IP address pool

IP Address Pool

information from Apsara Stack.

Dynamically collects network device interconnection data within a single Apsara

Hybrid Cloud

Physical Topology

Stack data center. Lets you manually add cross-

Resources

data-center interconnections and internal device interconnections in customer IDCs.

Network Element

Manages network devices in Apsara Stack and

Management

customer IDCs (limited support).

Maintains north-south security policies for the cloud platform. Includes system-default policies

Mitigation Policies (North-

and custom policies. Integrates with hardware

South)

firewalls deployed through “Border Default Security” to push and manage security policies.

North-South Security Policies

Manages NAT capabilities for outbound traffic from the classic network to external networks.

NAT Management

Supports IP address pool management and NAT policy management.

Manages hardware firewalls deployed through “Border Default Security”. Supports

Border Wall Management

passwordless login to the firewall’s native management interface.

**Network Open Platform**

**Feature**

**Description**

ONSP builds an open hybrid cloud networking

Network Element Lifecycle

platform. It delivers network function

Management

virtualization (NFV)-based lifecycle management for network services to ecosystem partners.

Core Features

Using ONSP, steer east-west traffic and some

Traffic Steering

north-south traffic to third-party network elements for processing.

Integrates with CloudMonitor Service (CMS) to

CMS Monitoring

report asynchronous tasks and network element anomaly alerts to CMS.

O&M Monitoring Capabilities

Integrates with Tianjimon to report ONSP

Tianjimon Monitoring

platform anomaly alerts to Tianjimon.

Allows network element administrators to share

Network Element Sharing

network elements with other tenants.

Supports multiple tenants managing their own network elements independently.

Multi-Tenant Support

ECS Instance Type

Filters ECS instance types.

Filtering

Advanced Features

Dynamic Refresh of VPC ID

Refreshes VPC IDs and vSwitch names

and vSwitch Name

dynamically.

One-Click Bypass

Enables one-click bypass.

Multi-VPC Security

Protects multiple VPCs.

Protection

Intel

Supports Intel processors.

Hygon

Supports Hygon processors.

Domestic Software and Hardware Ecosystem

Kunpeng

Supports Kunpeng processors.

Phytium

Supports Phytium processors.

**Bare Metal Networking**

**Feature**

**Description**

You can attach bare metal servers as backend

Service Reliability

servers to Server Load Balancer (SLB) instances in a VPC.

You can access bare metal servers from your office or an existing IDC over a leased line. The VPC connected to your leased line must be the

Deployment and

same as the VPC where the bare metal server

Maintenance of Bare Metal

resides. You can also log on to bare metal

Services

servers using ECS instances. The ECS instance and the bare metal server must be in the same VPC.

You can provision and release bare metal servers in a VPC. This feature enables communication between bare metal servers in

Bare Metal Server Access

different vSwitches within the same VPC,

to VPC

between bare metal servers and ECS instances in the same VPC, and between bare metal servers in different VPCs.

Core Features

You can access cloud services such as ops-dns,

Bare Metal Server Access

NTP servers, ApsaraDB RDS, OSS, and NAS from

to Cloud Services

bare metal servers.

You can use the Source Network Address

Bare Metal Server Access

Translation (SNAT) feature of NAT Gateway to

to the Internet

connect bare metal servers to the Internet.

You can attach bare metal servers as backend servers to Internet-facing SLB instances. You

Internet Access to Bare

can also use the Destination Network Address

Metal Servers

Translation (DNAT) feature of NAT Gateway to map public IP addresses to the IP addresses of bare metal servers.

This feature supports

Each license lets you manage one group of HSW

License

license-based

switches and up to 48 dual-NIC bare metal

Management

authorization.

servers.

This port is for 10-Gigabit servers and requires

10-Gigabit Optical Port

Link Aggregation Control Protocol (LACP) port aggregation support.

Bare Metal Server Port Types

This port is for 10-Gigabit or 25-Gigabit servers

25-Gigabit Optical Port

and requires LACP port aggregation support.

Multi-Zone Disaster Recovery Across Data Centers

Deployment Models

Multi-Region Deployment (Cell-Based Deployment)

HSW bare machine

Stacking Removal

managed switches support an unstacked architecture.

**Alibaba Cloud Networking Service Topology Visualization**

**Feature**

**Description**

Display Specified VPC Network Topology

Display Subnet

Displays ECS information in subnets.

Information in VPC

Display NAT Gateway

Displays NAT Gateway information in the VPC.

Information in VPC

Display Specified VPC Network Topology

Display Express Connect

Displays VPC peering connection information.

Information in VPC

Retrieve VPC Network

Retrieve VPC network topology information

Topology Information

using Open API.

Using Open API

VPC Peering

Displays count and supports navigation.

Attach a virtual border

Displays count and supports navigation.

router (VBR)

NAT Gateway

Displays count and supports navigation.

Displays count. Backends are ECS instances in

Display External

Internet-Facing SLB

this VPC.

Network Areas for VPC

Displays count. EIPs are bound to ECS instances

Elastic IP Address

in this VPC.

Displays count. Shows VPN Gateways

VPN Gateway

associated with this VPC.

Displays count. Shows IPv6 Gateways for this

IPv6 Gateway

VPC.

Displays VPC topology.

Display VPC Private

Lets you select different

Networks

VPC networks.

Route Table ID

Displays route table IDs.

Display Routers

Route Table Name

Displays route table names.

Router ID

Displays router IDs.

Display Full Router

Displays all routers.

Lists all routers vertically.

List

Displays vSwitch IDs.

vSwitch ID

vSwitch Name

Displays vSwitch names.

Zone for vSwitch

Displays the zone where the vSwitch resides.

Display vSwitches

IPv4 CIDR Block for

Displays the IPv4 CIDR block for the vSwitch.

vSwitch

IPv6 CIDR Block for

Displays the IPv6 CIDR block for the vSwitch.

vSwitch

Elastic Compute Service

Displays count and supports navigation.

(ECS)

ApsaraDB RDS

Displays count and supports navigation.

Display Cloud Resources Under vSwitches

Internal SLB

Displays count and supports navigation.

Display All vSwitches

Lists all vSwitches vertically.

**Hybrid Cloud Network Traffic Visualization**

**Feature**

**Description**

Traffic Trend

Shows top-N traffic rankings.

Supports statistics on Top-N application type distribution, traffic

Traffic Analysis

number of application types, mean traffic

Traffic Analysis

volume, and total traffic volume.

Supports switch port mirroring. Mirrors traffic in

Supported Data Sources

both inbound and outbound directions on switch ports.

Multi-zone disaster

Lowers traffic priority for low-priority

recovery supports

applications consuming large bandwidth.

emergency traffic

Traffic Rerouting

Ensures bandwidth for high-priority applications.

rerouting

(Version 317 supports only ODPS.)

Add Analyzer

Add a NIS Traffic Analyzer device.

Edit Analyzer

Edit a NIS Traffic Analyzer device.

Delete Analyzer

Delete a NIS Traffic Analyzer device.

Analyzer

View Analyzer

You can view NIS Traffic Analyzer devices.

Management

Add Analyzer Port

Add analysis port information for an analyzer.

Edit Analyzer Port

Edit analysis port information for an analyzer.

Delete Analyzer Port

Delete an analyzer’s analysis port.

View Analyzer Port

View an analyzer’s analysis port.

Add Rule

Add a traffic analysis rule.

Edit Rule

Edit a traffic analysis rule.

Rule Management

Delete Rule

Delete a traffic analysis rule.

View Rule

View a traffic analysis rule.

Add Scenario

Add a traffic analysis scenario.

Edit Scenario

Edit a traffic analysis scenario.

Scenario Management

Delete Scenario

Delete a traffic analysis scenario.

View Scenario

View a traffic analysis scenario.

Traffic visualization

Multi-Data Center

supports multi-AZ

Support

deployment.

Traffic visualization

Network Asset

supports network asset analysis.

Traffic visualization

Security Integration

Exports data to third parties.

supports Galaxy Gateway.
