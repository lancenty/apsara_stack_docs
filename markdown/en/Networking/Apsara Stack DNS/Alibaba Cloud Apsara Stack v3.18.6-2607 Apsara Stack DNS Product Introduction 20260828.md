Alibaba Cloud  
Apsara Stack  
Apsara Stack DNS  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Apsara Stack DNS](#section-1)
    - [1.1. Overview](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.Apsara Stack DNS

<a id="section-1-1"></a>

## 1.1. Overview

Apsara Stack DNS is a service that is encapsulated based on the DNS protocol and runs on Apsara Stack to resolve domain names over internal networks, such as virtual private clouds (VPCs), networks of self-managed data centers, and the classic network. You can configure rules and policies to map domain names to IP addresses. Apsara Stack DNS then distributes the DNS requests from clients to cloud resources, self-managed business applications, business systems on your internal networks, or the service resources of Internet service providers (ISPs).

**Category**

**Feature**

**Supported**

Global basic DNS resolution

Yes

Yes

Global load balancing (weight)

Global domain names

Global domain name forwarding

Yes

in Apsara Stack

Global default forwarding

Yes

Internet recursive resolution

Yes

Global line

Scheduling domain management

Yes

Tenant-specific basic DNS resolution

Yes

Tenant-specific load balancing (weight)

Yes

Private domain names

VPC association and disassociation

Yes

for VPCs

Tenant-specific domain name forwarding

Yes

Tenant-specific default forwarding

Yes

Private lines

Scheduling domain management

Yes

Scheduling instance management (multi-

Yes

cloud)

Global scheduling

Address pool management (multi-cloud)

Yes

Cross-cloud shared

Global basic DNS resolution (multi-cloud)

Yes

domain names

ISP line

ISP line management (multi-cloud)

Yes

Synchronization cluster management (multi-

Node management

Yes

cloud)

Log management (multi-cloud)

Log management

Yes

**DNS**

DNS is a distributed database used for TCP/IP applications. It translates domain names into IP addresses and selects paths for emails.

**Domain name resolution**

Domain name resolution maps domain names to IP addresses by using DNS. It includes both authoritative resolution and recursive resolution.

**Recursive resolution**

Recursive resolution queries domain names cached on the local DNS server or sends a request to the authoritative DNS system to obtain the corresponding IP addresses. You can use recursive resolution to resolve Internet domain names.

**DNS forwarding**

DNS forwarding uses two DNS servers to provide DNS resolution services. The local DNS server is used to configure and manage the domain name resolution data. The other DNS server is used to resolve domain names.

**Default forwarding**

If DNS queries for authoritative domain names are not resolved by the local DNS server, they are forwarded to another DNS server for resolution.

<a id="section-1-2"></a>

## 1.2. Benefits

Apsara Stack DNS is a key network service that controls data traffic for Apsara Stack. This service resolves domain names, balances and schedules server loads, and connects Apsara Stack with self-managed data centers. Apsara Stack DNS provides a complete suite of solutions to deploy a cloud environment, achieve high availability and disaster recovery for data centers, and balance server loads to secure your IT services.

You can perform the following operations by using Apsara Stack DNS in enterprise intranets:

- Access other Elastic Compute Service (ECS) instances deployed in the current virtual private cloud (VPC).

- Access other cloud service instances on Apsara Stack.

- Access the custom business systems of your enterprise.

- Access services over the Internet.

- Use the global server load balancing (GSLB) feature to implement multi-active solutions and disaster recovery, such as local active-active disaster recovery, active zone-redundancy, remote active-active disaster recovery, active geo-redundancy, and geo-disaster recovery.

- Connect to Apsara Stack DNS with your own DNS servers over a leased line.

**Enterprise domain name management**

Apsara Stack DNS provides management and resolution services for your enterprise domain names. It supports the following operations:

- Perform forward and reverse DNS lookups for domain names of cloud service instances, such as ECS instances.

- Perform forward and reverse DNS lookups for your internal domain names.

- Add, modify, and delete DNS records of the following types: A, AAAA, CNAME, MX, PTR, TXT, SRV, NAPTR, CAA, and NS.

- Add multiple A, AAAA, and PTR records for a hostname of a domain name. The system returns all record values by default through random round-robin to achieve load balancing.

- Add multiple A, AAAA, and CNAME records for a hostname of a domain name. The system returns a record value based on the weights configured for the record values of these records to achieve load balancing.

**Flexible integration with data centers**

Apsara Stack DNS can forward enterprise domain names and provide the following services for you to flexibly build your network and cascade Apsara Stack DNS servers with the DNS servers that you create:

- Global default forwarding

- Query forwarding for specific domain names

**Internet access from enterprise servers**

Apsara Stack DNS supports recursive resolution for Internet domain names, which allows your servers to access the Internet.

**Tenant isolation**

Apsara Stack DNS allows you to manage private zones in VPCs, resolve internal domain names, and isolate DNS records and resolution based on tenants. You can use Apsara Stack DNS to isolate data by VPC without the need to build your own DNS system. This helps reduce server and O&M costs.

> **Note**
>
> This feature is available only in Apsara Stack DNS Standard Edition.

**GTM-based management**

Global Traffic Manager (GTM) achieves nearby access to application services and load balancing in high-concurrency scenarios. GTM can implement traffic switchover based on health check results. This allows you to build active zone-redundancy and geo-disaster recovery services in a flexible and efficient manner. GSLB provides the following features in enterprise intranets:

- Allows you to add multiple records for a hostname of a domain name. The system returns a record value based on the weights configured for the record values of these records to achieve load balancing.

- Supports scheduling line management. You can customize lines and their priorities to allow clients to access the nearest nodes and implement intelligent traffic scheduling based on geographical locations and application groups. This accelerates access to applications.

- Synchronizes DNS configuration data among multiple clusters for which GTM is activated. This feature is supported in multi-cloud scenarios.

- Supports address pool management. You can manage your applications in a centralized manner by application service cluster.

- Supports custom global scheduling domains. You can manage and code global scheduling instances in a centralized manner based on your naming conventions.

**Unified management platform**

You can access DNS and any other cloud services on the Apsara Uni-manager Management Console with one account. This provides the following benefits:

- Apsara Stack DNS supports web operations for data and service management, which facilitates your use of the DNS service.

- Apsara Stack DNS is deployed on clusters. You can add more clusters based on your needs.

- You can deploy Apsara Stack DNS in multiple zones. Apsara Stack DNS supports local active-active and zone-disaster recovery.

- Apsara Stack DNS is deployed in anycast mode, which delivers high availability and disaster recovery.

**API operations**

Apsara Stack DNS provides API operations so that you can integrate it with other systems.

<a id="section-1-3"></a>

## 1.3. Scenarios

Apsara Stack DNS is a key network service that controls data traffic for Apsara Stack. This service resolves domain names, balances and schedules server loads, and connects Apsara Stack with self-managed data centers and Alibaba Cloud. Apsara Stack DNS provides a complete suite of solutions to deploy a cloud environment, achieve high availability and disaster recovery for data centers, and balance server loads to secure your IT services.

**Basic DNS resolution**

**Access cloud resource instances in a VPC**

You can use Apsara Stack DNS to access ApsaraDB RDS, Server Load Balancer (SLB), and Object Storage Service (OSS) instances from the Elastic Compute Service (ECS) instances or Docker instances in a virtual private cloud (VPC).

**Access ECS instances or Docker instances by using hostnames in a VPC**

You can create hostnames for the ECS instances or Docker instances in a VPC based on the rules that you define, and access and manage these instances by using the hostnames.

**Access the domain names of internal services in a VPC**

You can develop your own Platform as a Service (PaaS) or Software as a Service (SaaS) services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions. Tenants can access the deployed services by using domain names in the relevant VPC.

**Schedule the requests to internal services on Apsara Stack by using the round-robin algorithm**

You can use Apsara Stack DNS to access a deployed SaaS service and evenly distribute requests to different nodes in a VPC.

**Access Internet services from a VPC or the classic network**

You can use Apsara Stack DNS to access Internet services from a VPC or the classic network.

**Establish connections between Apsara Stack and other networks**

You can use Apsara Stack DNS to connect your internal network, a public cloud network, or other external networks to Apsara Stack to implement DNS resolution.

**Tenant isolation**

**Isolate tenant resources on Apsara Stack**

You can use Apsara Stack DNS to isolate tenant resources on Apsara Stack. The internal DNS records and the default forwarding configurations of each tenant are isolated from those of other tenants. Tenants can configure their own private DNS records to complete service addressing and scheduling.

**Establish connections among global resources on Apsara Stack**

If you want to allow all tenants to share global resources and configurations on Apsara Stack, system administrators can configure global DNS records and settings to complete service addressing and scheduling.

**Perform VPC-based intelligent scheduling on Apsara Stack**

You can use Apsara Stack DNS to provide different resolution results for different VPCs of a tenant based on the same hostname.

**Global scheduling**

You can develop your own PaaS or SaaS services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions.

**Schedule the traffic loads of internal network services on Apsara Stack based on weights**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and distribute requests to different nodes in backend service clusters based on the weights of these nodes.

**Schedule the traffic loads of internal network services on Apsara Stack based on the geographical locations of request sources or the application groups to which request sources belong**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and distribute requests to different nodes based on the geographical locations or application groups of the request sources.

**Enterprise disaster recovery**

You can develop your own PaaS or SaaS services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions.

**Schedule the traffic loads of internal network services on Apsara Stack to achieve disaster recovery**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and switch the access traffic of internal services from backend service cluster A (primary data center) to backend service cluster B (secondary data center) in a disaster recovery scenario.

<a id="section-1-4"></a>

## 1.4. Features

Apsara Stack DNS provides the DNS resolution and Global Server Load Balancer (GSLB) services in VPCs, networks of self-managed data centers, and the classic network.

**Global Traffic Manager (GTM)**

**Feature**

**Description**

The health check for address pools using

Health check

protocols such as TCP, UDP, HTTP, HTTPS, and ICMP is supported.

You can add, modify, comment, and delete address pools at a time. You can also perform fuzzy search based on keywords to manage

Address pool management

application service clusters.

The supported addresses can be IPv4 addresses, IPv6 addresses, or domain names.

Address pool

This meets the configuration requirements of

Address Type

common application services.

The system supports the following load balancing policies for DNS records, each of which can contain multiple IP addresses: round-

Load Balancing Policy

robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications.

Real-time synchronization of scheduling configuration data, such as scheduling instances, address pools, IP address

GTM data synchronization

configurations, and scheduling domains, among multiple GTM nodes. The cluster can work normally when less than half of the nodes fail.

You can merge multiple GTM clusters to form a

GTM cluster management

large GTM cluster

Data synchronization

Clusters can be rebuilt in single-data center or

management

Rebuild a GTM cluster

multi-data center failure scenarios to ensure business continuity.

You can merge multiple GTM clusters to form a

Merge GTM Control

large GTM cluster

Domain

Clusters can be rebuilt in single-data center or

Emergency group

multi-data center failure scenarios to ensure business continuity.

You can add, modify, comment, and delete

Scheduling domain

scheduling domains at a time. You can also

Scheduling domains

management

perform fuzzy search based on keywords to customize private scheduling domains.

Each scheduling instance supports a custom

CNAME Settings

CNAME access domain name to resolve configuration records.

You can configure primary and secondary address pools for scheduling instances to

Address pool switchover

achieve automatic switchover between the primary and secondary address pools based on their health check results.

You can configure multiple access policy for each scheduling instance. Separate access

Scheduling

IP address-based Access

policy can be configured for different lines

instances

Policy

(corresponding to the DNS request source) to implement intelligent traffic scheduling.

You can add, modify, comment, and delete scheduling instances at a time. You can also

Scheduling instance

perform fuzzy query based on keywords to

management

manage scheduling instances.

<table>
  <tr>
    <td>Resolution line management</td>
    <td>IP address line configuration</td>
    <td>Lines can be created based on client IP addresses and more than one route can be configured for each source CIDR block. In addition, priorities can be configured for routes that belong to the same source CIDR block.</td>
  </tr>
</table>

**Management and resolution of authoritative domain names**

**Feature**

**Note**

Apsara Stack DNS allows you to add, modify, remove, or batch delete authoritative domain

Authoritative domain

names or add remarks. Fuzzy match based on

name management

keywords is also supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation.

Apsara Stack DNS allows you to add, modify, remove, and batch delete DNS records of the

Internal DNS

DNS record management

following types: A, AAAA, CNAME, NS, MX, TXT,

resolution

SRV, PTR, NAPTR, CAA, and SOA. Fuzzy search

management

is supported by keyword.

Each of the following types of DNS records can contain multiple IP addresses: A, AAAA, and CNAME. The system supports the following load balancing policies for DNS records, each of

Load balancing policy

which can contain multiple IP addresses: round-robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications.

Users can associate DNS query forwarding rules

Custom DNS authoritative

with VPCs or disassociate DNS query forwarding

DNS resolution service for

rules from VPCs. Users can also query

VPC

associations between authoritative domain names and VPCs.

You can add, modify, remove, or batch delete authoritative domain names or add remarks.

Authoritative domain

Fuzzy match based on keywords is also

name management

supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation.

PrivateZone (DNS Standard Edition

Apsara Stack DNS allows you to add, modify,

only)

and delete DNS records of the following types:

DNS record management

A, AAAA, CNAME, NS, MX, TXT, SRV, PTR, NAPTR, CAA, and SOA. Fuzzy search is supported by keyword.

Each of the following types of DNS records can contain multiple IP addresses: A, AAAA, and CNAME. The system supports the following load

Load Balancing Policy

balancing policies for DNS records, each of

(Among Addresses)

which can contain multiple IP addresses: round-robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications.

**Forwarding and recursion configuration management and resolution**

**Feature**

**Note**

You can add, modify, comment, remove, and delete forwarding configurations based on

Domain name forwarding

domain names. You can also perform fuzzy

configuration

search based on keywords to perform

management

undifferentiated global forwarding DNS resolution services over all VPCs and classic network.

Apsara Stack DNS can forward requests with or without recursion. In non-recursive forwarding

Global internal

mode, only the specified DNS server is used to

network forwarding

resolve domain names. If the resolution fails or

configuration

times out, a message is returned to the DNS

Default forwarding mode

client to indicate that the current request fails. In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used.

You can enable, modify, and disable the default

Default forwarding

forwarding configuration. This way, you can

configuration

forward the DNS resolution over all VPCs and

management

classic network.

Users can associate DNS query forwarding rules with VPCs or disassociate DNS query forwarding

VPC-based custom DNS

rules from VPCs. Users can also query

forwarding service

associations between authoritative domain names and VPCs.

You can add, modify, remove, or batch delete authoritative domain names or add remarks.

Domain name forwarding

Fuzzy match based on keywords is also

configuration

supported. This allows users to customize a DNS

management

resolution service for each VPC to implement VPC-level tenant isolation.

Tenant forwarding

Public DNS can forward requests with or without

configurations

recursion. In non-recursive forwarding mode, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails. In the mode of forwarding with recursion, the specified

Forwarding mode

DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used.

You can add, modify, remove, or batch delete authoritative domain names or add remarks.

Default forwarding

Fuzzy match based on keywords is also

configuration

supported. This allows users to customize a DNS

management

resolution service for each VPC to implement VPC-level tenant isolation.

**Characteristics**

<table>
  <tr>
    <th colspan="2">Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Low latency</td>
    <td>Low-latency DNS services</td>
    <td>Apsara Stack DNS supports Anycast IP addresses and provides seamless data center service switchover in disaster recovery scenarios.</td>
  </tr>
  <tr>
    <td>Hybrid cloud</td>
    <td>System cascade</td>
    <td>Supports interconnection with external DNS systems and interconnection between hybrid clouds through domain name forwarding.</td>
  </tr>
  <tr>
    <td>Quick update</td>
    <td>The time when data delivery takes effect.</td>
    <td>The changes for domain names take effect within 5 seconds. The effective time for changes in domain names within a VPC is not affected by TTL.</td>
  </tr>
  <tr>
    <td>Access Control</td>
    <td>Traffic throttling for individual requests</td>
    <td>The throttling for DNS requests is supported for VPCs. By default, the Throttling Threshold is set to 50,000 QPS for a single VPC and 3,000QPS for a single source IP address in a single VPC.</td>
  </tr>
  <tr>
    <td rowspan="2">High availability</td>
    <td>High-availability resolution service</td>
    <td>Apsara Stack DNS supports Anycast IP addresses and provides seamless data center service switchover in disaster recovery scenarios.</td>
  </tr>
  <tr>
    <td>Multi-region Architecture 2.0</td>
    <td>DNS supports the multi-region 2.0 solution.</td>
  </tr>
</table>

**O&M and monitoring**

<table>
  <tr>
    <th colspan="2">Feature</th>
    <th>Note</th>
  </tr>
  <tr>
    <td>O&amp;M logs</td>
    <td>DNS Logs</td>
    <td>Supports DNS resolution logs to facilitate DNS tracing and troubleshooting.</td>
  </tr>
  <tr>
    <td rowspan="3">Statistical monitoring</td>
    <td>QPS Statistics</td>
    <td>QPS(Query Per Second) statistics are supported to measure the performance of the DNS resolution service.</td>
  </tr>
  <tr>
    <td>Success Rate</td>
    <td>Supports statistics on the success rate of DNS resolution to determine the quality of DNS resolution in the current network. When the resolution success rate decreases, a large number of domain names fail to be accessed and administrator intervention is required.</td>
  </tr>
  <tr>
    <td>Average Resolution Latency</td>
    <td>The average DNS resolution latency is supported. If the resolution latency is high, a large number of external domain names are accessed. In this case, a random domain name attack may occur and administrator intervention is required.</td>
  </tr>
</table>

**Other features**

<table>
  <tr>
    <th colspan="2">Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>OpenAPI</td>
    <td>API service capabilities</td>
    <td>Apsara Stack DNS provides API operations so that you can integrate it with other systems.</td>
  </tr>
  <tr>
    <td>Resolution line management</td>
    <td>IP address line configuration</td>
    <td>Lines can be created based on client IP addresses and more than one route can be configured for each source CIDR block. In addition, priorities can be configured for routes that belong to the same source CIDR block. The lines can be used by global domain names on Apasara Stack, private domain names of VPCs, and GTM instances to implement line-based intelligent resolution.</td>
  </tr>
  <tr>
    <td>Global recursive resolution service</td>
    <td>Recursive resolution service configuration</td>
    <td>The recursive resolution service can be enabled and disabled on demand. You can enable this service to resolve public domain names for servers and terminals deployed in VPCs or classic networks. This allows these servers or terminals to access the Internet.</td>
  </tr>
  <tr>
    <td>Cache</td>
    <td>Support for cache management</td>
    <td>Supports cache management.</td>
  </tr>
  <tr>
    <td>Support for the xfer protocol</td>
    <td>Resolve the original primary domain name of a website.</td>
    <td>Forwarding mode: has high requirements on network connectivity.</td>
  </tr>
  <tr>
    <td>Multi-IDC Deployment</td>
    <td>Three-zone disaster recovery is supported.</td>
    <td>Support physical machine-based deployment.</td>
  </tr>
</table>
