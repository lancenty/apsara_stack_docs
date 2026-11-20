Alibaba Cloud  
Apsara Stack  
VPN Gateway  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.VPN Gateway](#section-1)
    - [1.1. Features](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Features](#section-1-4)

<a id="section-1"></a>

# 1.VPN Gateway

VPN Gateway is an Internet-based service that securely and reliably connects enterprise data centers, office networks, and Internet clients to virtual private clouds (VPCs) through encrypted tunnels.

<a id="section-1-1"></a>

## 1.1. Features

VPN Gateway allows you to establish secure and reliable network connections between data centers, office networks, Internet clients, and virtual private clouds (VPCs) by using IPsec-VPN and SSL-VPN.

**IPsec-VPN**

IPsec-VPN is a route-based network connection technology that provides flexible traffic routing methods and allows you to configure and maintain VPN policies with ease.

You can use IPsec-VPN to establish connections between data centers, office networks, and VPCs. You can also use IPsec-VPN to establish connections between VPCs in different regions.

**SSL-VPN**

SSL-VPN is a network connection technology based on OpenVPN. After you deploy the required resources, you need to only load an SSL client certificate to an Internet client and initiate a connection to a VPC.

<a id="section-1-2"></a>

## 1.2. Benefits

VPN gateways are easy to configure and allow you to establish secure and stable connections in an efficient manner. Compared with Express Connect, VPN Gateway allows you to establish connections in a faster and more cost-effective manner.

**Security**

VPN Gateway uses the IPsec protocol or certificates in data transmission to ensure data security.

**Stability**

VPN Gateway adopts the hot-standby architecture to implement failover within a few seconds, session persistence, and zero service downtime.

**Ease-of-use**

A VPN gateway is ready-to-use and its configurations immediately take effect. You can deploy VPN gateways in a fast manner.

**Cost-effectiveness**

The encrypted and Internet-based connections provided by VPN Gateway are more cost-effective than Express Connect circuits.

<a id="section-1-3"></a>

## 1.3. Scenarios

You can use VPN Gateway to build hybrid cloud networks, connect cloud resources, and enable telecommuting.

**Build a hybrid cloud network**

You can use IPsec-VPN to establish encrypted connections between data centers and virtual private clouds (VPCs) to build a hybrid cloud network.

**Connect cloud resources**

You can use IPsec-VPN to establish encrypted connections between VPCs are that deployed in the same region or different regions. This enables the resources in different VPCs to communicate with each other.

**Enable telecommuting**

You can use SSL-VPN to connect Internet clients to VPCs through encrypted channels. This way, the clients can connect to VPCs in a secure manner anytime. This is an ideal feature for telecommuting scenarios.

<a id="section-1-4"></a>

## 1.4. Features

**Feature**

**Description**

Modify IPsec-VPN connections.

IPsec-VPN

Manage IPsec-VPN

configuration

Create IPsec-VPN connections.

connections

Delete IPsec-VPN connections.

Download SSL client certificates.

Manage SSL clients

Create SSL client certificates.

Delete SSL client certificates.

SSL-VPN configuration

Modify SSL servers.

Manage SSL servers

Create SSL servers.

Delete SSL servers.

Modify VPN gateways.

Create VPN gateways.

Create VPN gateways

View VPN gateways.

Instance management

Modify customer gateways.

Create customer gateways.

Customer gateway

Delete customer gateways.

View customer gateways.

Support for IPsec-VPN monitoring.

Monitoring capabilities

O&M capabilities

Support for SSL-VPN monitoring.

Support for VPN Gateway monitoring.

VPN supports multiple regions.

Multi-Region

Multi-data center deployment

Zone-disaster recovery

VPN Gateway supports zone-disaster recovery.

support

Encryption algorithm

aes, aes192, aes256, eds, 3des.

Encryption algorithm

Authentication algorithm

sha1, MD5.
