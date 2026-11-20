Alibaba Cloud  
Apsara Stack  
Express Connect  
User Guide  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Log on to the Express Connect console](#section-1)
- [2.Getting started](#section-2)
    - [2.1. What is Express Connect?](#section-2-1)
    - [2.2. Peering connections](#section-2-2)
    - [2.3. Overview of Express Connect](#section-2-3)
    - [2.4. VBRs](#section-2-4)
    - [2.5. Connect a data center to a VPC by using an Express Connect circuit](#section-2-5)
- [3.Overview](#section-3)
- [4.VPC peering](#section-4)
    - [4.1. Create and manage VPC peering connections](#section-4-1)
    - [4.2. Configure routes](#section-4-2)
- [5.VBR-to-VPC connections](#section-5)
- [6.Physical connections](#section-6)
    - [6.1. Create and manage connections over Express Connect circuits](#section-6-1)
    - [6.2. Modify an Express Connect circuit](#section-6-2)
    - [6.3. Delete a connection over an Express Connect circuit](#section-6-3)
    - [6.4. Manage a VBR](#section-6-4)
- [7.VBRs](#section-7)
    - [7.1. Create and manage a VBR](#section-7-1)
    - [7.2. Manage Express Connect circuits](#section-7-2)
    - [7.3. Add and manage routes](#section-7-3)
    - [7.4. Configure and manage BGP](#section-7-4)
    - [7.5. Manage VBR-to-VPC connections](#section-7-5)
    - [7.6. Configure a failover group](#section-7-6)
    - [7.7. Attach a VBR to a CEN instance across accounts](#section-7-7)
- [8.Manage operation logs](#section-8)
- [9.Manage tags](#section-9)

<a id="section-1"></a>

# 1.Log on to the Express Connect console

This topic describes how to log on to the Express Connect console from the Apsara Uni-manager Management Console.

**Prerequisites**

- The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers.

- A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.

   ![](assets/687f6d006b35a4552292b1f7b3755914.jpeg)

   > **Note**
   >
   > - You can select a language from the drop-down list in the upper-right corner of the page.
   >
   > - 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Uni-manager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。

2. Enter the correct username and password.

   Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

   > **Note**
   >
   > - **First logon**
   >
   >   The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
   >
   > - **Forgot password**
   >
   >   If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.

4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following operations based on your scenario:

   - Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator.

     <ol type="a">

     <li>

     On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device.

     </li>

     <li>

     Re-enter your username and password as described in Step 2, and click **Log On**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Enter the 6-digit MFA code and click **Authenticate**.

     </li>

     </ol>

   - Scenario 2: You have enabled MFA and bound an MFA device.

     Enter the 6-digit MFA code and click **Authenticate**.

     > **Note**
     >
     > For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

5. In the top navigation bar, choose **Products > Networking > Express Connect**.

6. In the top navigation bar, select the region.

<a id="section-2"></a>

# 2.Getting started

<a id="section-2-1"></a>

## 2.1. What is Express Connect?

This topic provides an overview of Express Connect. Express Connect allows you to establish private connections to enable fast, stable, and secure communication between different networking environments. You can use Express Connect to ensure network stability and prevent data breaches.

**Features**

You can use a leased line provided by an Internet Service Provider (ISP) to establish a physical connection between your data center and an Alibaba Cloud access point. After the physical connection is established, you can create a virtual border router (VBR) to connect your data center with Alibaba Cloud to build a hybrid cloud.

The physical connections of Express Connect do not traverse the Internet, and therefore feature faster speeds, lower latency, greater security, and higher reliability compared with Internet connections.

Express Connect enables you to create a peering connection between two Virtual Private Clouds (VPCs) as a channel for private communication.

**Benefits**

Express Connect provides the following benefits:

- High-speed interconnections

  Powered by the network virtualization technology of Alibaba Cloud, Express Connect allows networks to connect and exchange traffic at high speeds within internal networks without carrying traffic across the Internet. The impact of distance on network performance is minimized to ensure low-latency and high-bandwidth communication.

- Stability and reliability

  Built on the state-of-the-art infrastructure of Alibaba Cloud, Express Connect guarantees stable and reliable communication between networks.

- Security

  Express Connect implements cross-network communication at the network virtualization layer, where data is transmitted over separate and private channels within the infrastructure of Alibaba Cloud, mitigating the risks of data breaches.

- Buy-as-you-need service

  Express Connect delivers connectivity with a wide range of bandwidth options. You can choose based on the needs of your business to get the best value for your purchase.

<a id="section-2-2"></a>

## 2.2. Peering connections

You can create a peering connection between two virtual private clouds (VPCs) or between a VPC and a virtual border router (VBR).

**Initiator and acceptor**

One end of a peering connection functions as the initiator and the other end functions as the acceptor. Only the initiator can initiate the peering connection. The acceptor must wait for the initiator to initiate the peering connection. The concepts of initiator and acceptor are used only to control how a peering connection is established. Data transmission between the initiator and acceptor is bidirectional. Therefore, after a peering connection is established, both the initiator and acceptor can send and receive data.

If you create a peering connection for two VPCs within the same account, the system of Express Connect automatically creates the initiator and acceptor. You do not need to manually initiate the connection. The system automatically sends the connection request and enables the connection. If you create a peering connection for two VPCs that belong to different accounts, you must manually initiate the connection.

The following table describes the differences between an initiator and acceptor.

| Item | Initiator | Acceptor |
| --- | --- | --- |
| Whether the configuration of the peer is required before the connection is initiated | Yes | Yes |
| Initiate the connection | Supported | Not supported |
| Send messages to the peer after the connection is established | Supported | Supported |

**Connection process and status**

In the peering connection process, the initiator initiates a connection. The acceptor then receives the connection, after which the connection is established successfully.

During different stages of the connection process, the status of a peering connection is also different, as shown in the following table.

> **Note**
>
> If you choose to create both ends at the same time when establishing a
>
> peering connection, the system automatically initiates and establishes a connection. In this case, the initiator and the acceptor become activated after being created.

| Connection process | Initiator status | Acceptor status |
| --- | --- | --- |
| The initiator initiates a connection. | Connecting | Accepting |
| The connection is established. | Activated | Activated |
| The connection is suspended. | Suspending | Suspending |
| The connection is broken. | Suspended | Suspended |
| A connection is re-initiated. | Activating | Activating |
| The connection is established. | Activated | Activated |

<a id="section-2-3"></a>

## 2.3. Overview of Express Connect

Express Connect offers a secure, reliable, and high-performance solution for connecting your data centers to Apsara Stack. You can lease an Express Connect circuit from a connectivity provider and use the Express Connect circuit to connect a data center to an Apsara Stack access point. Connections over Express Connect circuits are not exposed to the Internet. Compared with Internet connections, connections over Express Connect circuits are safer, faster, and more reliable with lower network latency.

**Connection methods**

You can apply for an Express Connect circuit to establish a connection.

You can lease an Express Connect circuit to connect your data center to an access point of Apsara Stack. The Express Connect circuit is dedicated to you. You can apply for dedicated connections over Express Connect circuits. For more information, see Apply for an Express Connect circuit.

<a id="section-2-4"></a>

## 2.4. VBRs

Virtual border routers (VBRs) are an abstraction of Express Connect circuits that are isolated and virtualized by using the Layer 3 overlay and vSwitch technologies in the Software Defined Network (SDN) architecture. A VBR is deployed between the customer-premises equipment (CPE) and a virtual private cloud (VPC) and is used to exchange data between the VPC and data center.

> **Note**
>
> Similar to VPC routers, each VBR manages a route table. You can add routes
>
> to the route table of a VBR to control network traffic forwarding.

**Features**

A VBR provides the following features:

- Exchanges data between a VPC and a data center.

- Determines the type of virtual interface of an Express Connect circuit: Layer 3 router interface or Layer 3 Virtual Local Area Network (VLAN) subinterface.

- Adds or identifies VLAN tags if a Layer 3 VLAN subinterface is used.

- Supports Border Gateway Protocol (BGP) routing.

  - BGP is a dynamic routing protocol based on Transmission Control Protocol (TCP). BGP is used to exchange routing and network accessibility information across autonomous systems. When you create a connection over an Express Connect circuit, you can configure BGP routing between your data center and the associated VBR. This way, the data center and the VBR can communicate with each other through a private connection. This helps you to set up a hybrid cloud with higher efficiency, flexibility, and security.

  - VBRs support BGP dynamic routing in both IPv4 and IPv6 networks.

**Limits**

- VBRs do not support source address-specific policy-based routes.

- Each VBR has one and only one route table.

- VBRs support only BGP-4.

- You can create at most eight BGP peers for each VBR.

- Each BGP peer supports at most 110 dynamic routes. Routes are denied when the upper limit is exceeded.

- To configure BGP when you connect to a VPC, you must specify an Autonomous System Number (ASN) for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

<a id="section-2-5"></a>

## 2.5. Connect a data center to a VPC by using an Express Connect circuit

You can connect a data center to a virtual private cloud (VPC) on Alibaba Cloud by using an Express Connect circuit. This way, the data center and the VPC can exchange data by using private connections.

**Step 1: Confirm the access point**

Before you apply for an Express Connect circuit, you must choose an access point, check the inventory, and contact a connectivity provider for a pre-installation site survey.

An access point is where network services are provided and supports multiple types of connections between a data center and Apsara Stack. When you choose an access point, take note of factors such as the region, connectivity provider, and port.

**Step 2: Apply for an Express Connect circuit**

> **Note**
>
> To apply for an Express Connect circuit, you need to log on to the Apsara Uni-manager Operations Console.

1. Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.

3. On the **Physical Connection** page, click **Apply for Physical Connection**.

4. Go to the Apsara Uni-manager Operations Console to configure an Express Connect circuit as prompted.

**Step 3: Enable the connection over the Express Connect circuit**

The Express Connect circuit interface requested in Step 2 is in the **Allocating Resources** state. After resources are allocated, refresh the **Physical Connection** page. After the Express Connect circuit enters the **Pending Confirmation** state. Perform the following steps to enable the Express Connect circuit:

1. On the **Physical Connection** page, find the Express Connect circuit in the **Disabled** state and click **Enable Connection** in the **Actions** column.

2. In the **Enable Connection** message, click **OK**.

**Step 4: Create a virtual border router (VBR)**

After the Express Connect circuit is enabled, the Express Connect circuit enters the **Enabled** state on the **Physical Connection** page. You need to create a VBR to enable communication between the data center and the VPC. After a VBR is created and enters the **Normal** state, run the **ping** command to check the connectivity between the on-premises gateway in the data center and the Alibaba Cloud gateway of the VBR.

1. On the **Physical Connection** page, find the **Enabled** Express Connect circuit and click its ID in the **ID/Name** column.

2. On the details page of the Express Connect circuit, click **Create VBR** in the **Connected VBRs** section.

3. In the **Create VBR** dialog box, specify the following parameters and click **OK**.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">Basic Information</td>
     </tr>
     <tr>
       <td>Account Type</td>
       <td>• <strong>Current Organization</strong>: creates a VBR for the current organization.<br>• <strong>Another Organization</strong>: creates a VBR for another organization.<br>In this example, <strong>Current Organization</strong> is selected.</td>
     </tr>
     <tr>
       <td>Organization</td>
       <td>Select an organization for the VBR.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Resource Set</td>
       <td>Select the resource set to which the VBR belongs.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Name</td>
       <td>Enter a name for the VBR.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Organization UID</td>
       <td>Enter the UID of another organization.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Another</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td colspan="2">Physical Connection Configurations</td>
     </tr>
     <tr>
       <td>Physical Connection</td>
       <td>Select an Express Connect circuit that is enabled and works as expected.</td>
     </tr>
     <tr>
       <td>VLAN ID</td>
       <td>Enter a VLAN ID for the VBR. Valid values: 0 to 3999.<br>• If the VLAN ID is set to 0, VLAN is not enabled and the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface.<br>When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR.<br>• If the VLAN ID is set to a value from 1 to 3999, the switch port on the VBR is a Layer 3 VLAN subinterface.<br>When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2.<br>Important<br>The VLAN ID that you specify for the VBR and that of the customer-premises device must be the same.</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center.</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Customer Side</td>
       <td>Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv4 Address)</td>
       <td>Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center.</td>
     </tr>
     <tr>
       <td>IPv6 Support</td>
       <td>Specify whether to enable IPv6.<br>• <strong>Disable</strong>: disables IPv6.<br>• <strong>Enable (You cannot disable this feature after it is enabled.)</strong>: If IPv6 is enabled, the VPC and data center can use IPv6 addresses.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Customer Side</td>
       <td>Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv6 Address)</td>
       <td>Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
   </table>

   > **Note**
   >
   > Specify the IP addresses based on your network plan. The IP addresses must be in the same CIDR block. We recommend that:
   >
   > 1. The specified IP addresses do not conflict with IP addresses in the cloud or on-
   >
   > premises IP addresses.
   >
   > 2. Use private IP addresses.
   >
   > Example:
   >
   > IPv4 address of the gateway at the Alibaba Cloud side: 10.0.0.1
   >
   > IPv4 address of the gateway at the customer side: 10.0.0.2
   >
   > IPv4 subnet mask: 255.255.255.252
   >
   > Set IPv6 Address of Gateway at Alibaba Cloud Side to 2408:4004:cc:400::1 (GUA address).
   >
   > Set IPv6 Address of Gateway at Customer Side to 2408:4004:cc:400::2 (GUA address).
   >
   > Set Subnet Mask (IPv6 Address) to 2408:4004:cc:400::/56.

**Step 5: Create a peering connection between the VBR and the VPC**

After a connection over the Express Connect circuit is established between the data center and Apsara Stack, you must create a VBR-to-VPC peering connection between the VBR and a VPC. This way, the VPC can communicate with the data center over the private network.

1. In the left-side navigation pane, click **VBR-to-VPC Connection**.

2. On the **VBR-to-VPC Connection** page, click **Create Peering Connection**.

3. On the **Create Peering Connection** page, set the following parameters.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">VBR-side configuration</td>
     </tr>
     <tr>
       <td>Organization/Resou rce set</td>
       <td>Select the organization and resource set to which the VBR belongs.</td>
     </tr>
     <tr>
       <td>Region</td>
       <td>Select the region where the VBR is located.</td>
     </tr>
   </table>

   <table>
     <tr>
       <th>Router type</th>
       <th>Select the router type on the VBR side. Currently, only the default <strong>Virtual</strong> <strong>Border Router</strong> type is supported.</th>
     </tr>
     <tr>
       <td>Access point</td>
       <td>Select an access point.</td>
     </tr>
     <tr>
       <td>VBR</td>
       <td>Select the VBR ID.</td>
     </tr>
     <tr>
       <td>Router interface specification</td>
       <td>Select the router interface specification on the VBR side.<br>• 1000 Mbps<br>• 2000 Mbps<br>• 5000 Mbps<br>• 10000 Mbps</td>
     </tr>
     <tr>
       <td>Router interface name</td>
       <td>Enter a name for the router interface on the VBR side.<br>The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-), but cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Description</td>
       <td>Enter a description for the VBR side.<br>The description must be 2 to 256 characters in length, start with a letter or a Chinese character, and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td colspan="2">VPC-side configuration</td>
     </tr>
     <tr>
       <td>Organization/Resou rce set</td>
       <td>Select the organization and resource set to which the VPC belongs.<br>Note<br>If the acceptor VPC belongs to a different organization, the other organization must confirm the connection.</td>
     </tr>
     <tr>
       <td>Region/Availability zone</td>
       <td>Select the region and availability zone where the VPC is located.</td>
     </tr>
     <tr>
       <td>Router type</td>
       <td>Select the router type on the VPC side. Currently, only the default <strong>VPC</strong> <strong>router</strong> type is supported.</td>
     </tr>
     <tr>
       <td>VPC</td>
       <td>Select a VPC.</td>
     </tr>
     <tr>
       <td>Router interface name</td>
       <td>Enter a name for the router interface on the VPC side.<br>The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-), but cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Description</td>
       <td>Enter a description for the VPC side.<br>The description must be 2 to 256 characters in length, start with a letter or a Chinese character, and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Health check source IP</td>
       <td>Enter the source IP address for the health check.<br>Note<br>The health check source IP address must be an available IP address within the CIDR block of a VSwitch in the local VPC.</td>
     </tr>
     <tr>
       <td>Health check destination IP</td>
       <td>Enter the destination IP address for the health check.<br>Note<br>The health check destination IP address must be the IP address of the port on the on-premises device at the other end of the leased line associated with the VBR.</td>
     </tr>
   </table>

   > **Note**
   >
   > Before you create the instance, you can view and verify the configuration in the **Configuration Overview** pane on the right side of the page.
   >
   > - Click a field to go to the corresponding parameter and modify it as needed.
   >
   > - Click **Quota Management** (if the organization/resource set has no quota) or click **Manage** in the **Quota** section (if the organization/resource set has a quota) to manage quotas for cloud products.
   >
   >   For more information about quota management, see the **Quota Management** chapter in the **Apsara Uni-manager Operations Console User Guide**.

<a id="section-3"></a>

# 3.Overview

The Express Connect console provides an overview of your resources, such as connections and instances.

**Procedure**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Overview**.

3. On the Overview page, you can view the connections and instances. You can analyze the trends of resource usage to better manage your resources.

<a id="section-4"></a>

# 4.VPC peering

<a id="section-4-1"></a>

## 4.1. Create and manage VPC peering connections

This topic describes how to create a peering connection between two virtual private clouds (VPCs).

**Create a peering connection**

1. Log in to the Express Connect console.

2. In the left-side navigation pane, click **VPC-to-VPC**.

3. On the **VPC-to-VPC** page, click **Create Peering Connection**.

4. On the **Create Peering Connection** page, configure the parameters described in the following table.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">Local Configurations</td>
     </tr>
     <tr>
       <td>Requester Organization/Requester Resource Set</td>
       <td>The organization and resource set to which the requester VPC belongs.</td>
     </tr>
     <tr>
       <td>Requester Region</td>
       <td>The region in which the requester VPC resides.</td>
     </tr>
     <tr>
       <td>Router Type</td>
       <td>The requester router type. Only <strong>vRouter</strong> is supported.</td>
     </tr>
     <tr>
       <td>Local VPC ID</td>
       <td>The ID of the requester VPC.</td>
     </tr>
     <tr>
       <td colspan="2">Peer Configurations</td>
     </tr>
     <tr>
       <td>Acceptor Organization/Acceptor Resource Set</td>
       <td>The organization and resource set to which the acceptor VPC belongs.<br>Note<br>If the acceptor VPC belongs to another organization, confirm with the organization.</td>
     </tr>
     <tr>
       <td>Acceptor Region</td>
       <td>The region in which the acceptor VPC resides.</td>
     </tr>
     <tr>
       <td>Router Type</td>
       <td>The acceptor router type. Only <strong>vRouter</strong> is supported.</td>
     </tr>
     <tr>
       <td>Peer VPC ID</td>
       <td>The ID of the acceptor VPC.</td>
     </tr>
     <tr>
       <td colspan="2">Basic Configurations</td>
     </tr>
     <tr>
       <td>Bandwidth</td>
       <td>The maximum bandwidth for the private connections. Only <strong>10000Mbps</strong> is supported.</td>
     </tr>
   </table>

   > **Note**
   >
   > Before you click submit to create the instance, you can view and check the configurations of the instance in the **Configuration overview** section on the right side.
   >
   > - You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
   >
   > - You can click **Quota Management** (the organization/resource set does not have quotas) or click **Quota Management** (the organization/resource set has quotas) in the **Quota** section to manage quotas for the cloud service.
   >
   >   For more information about quota management, see the **Quota management** topic in **Apsara Uni-manager Management Console User Guide**.

5. Create the peering connection.

   - Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created and **Router Interface (VPC-to-VPC)** is displayed in the **Cloud resources** column of the service.

   - If the service whose **Cloud resources** value is **Router Interface (VPC-to-VPC)** does not exist on the Service Management page, confirm the parameters and click **Submit**.

   For more information about service management, see the **Manage services** topic in **Apsara Uni-manager Management Console User Guide**.

**Create a requester or an acceptor**

The following section describes the procedure to create a requester or an acceptor.

1. Log in to the Express Connect console.

2. In the left-side navigation pane, click **VPC-to-VPC**.

3. On the **VPC-to-VPC** page, click **Create Requester/Acceptor**.

4. On the **Create Requester/Acceptor** page, configure the parameters described in the following table.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">Local Settings</td>
     </tr>
     <tr>
       <td>Organization</td>
       <td>Select the organization to which the requester VPC belongs.</td>
     </tr>
     <tr>
       <td>Resource Set</td>
       <td>Select the resource set to which the requester VPC belongs.</td>
     </tr>
     <tr>
       <td>Region</td>
       <td>Select the region of the requester VPC.</td>
     </tr>
     <tr>
       <td>Router Type</td>
       <td>Select the requester router type. Only <strong>vRouter</strong> is supported.</td>
     </tr>
     <tr>
       <td>Role</td>
       <td>Select a role. Valid values:<br>• Requester<br>• Acceptor</td>
     </tr>
     <tr>
       <td>VPC ID</td>
       <td>Select the ID of the requester VPC.</td>
     </tr>
     <tr>
       <td>Name</td>
       <td>Enter a name for the requester VPC.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td colspan="2">Peer Settings</td>
     </tr>
     <tr>
       <td>Peer Region</td>
       <td>Select the region of the peer VPC.</td>
     </tr>
     <tr>
       <td>Peer Router Type</td>
       <td>Select the peer router type. Only <strong>vRouter</strong> is supported.</td>
     </tr>
     <tr>
       <td colspan="2">Specifications</td>
     </tr>
     <tr>
       <td>Bandwidth</td>
       <td>Specify the maximum bandwidth for the private connections.<br>• If you set <strong>Role</strong> to <strong>Requester</strong>, you can select only <strong>10000Mbps</strong>.<br>• If you set <strong>Role</strong> to <strong>Acceptor</strong>, you can select only <strong>Negative</strong>.</td>
     </tr>
   </table>

5. Create the requester or acceptor.

   - Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created and **Router Interface (VPC-to-VPC)** is displayed in the **Cloud resources** column of the service.

   - If the service whose **Cloud resources** value is **Router Interface (VPC-to-VPC)** does not exist on the Service Management page, confirm the parameters and click **Submit**.

   For more information about service management, see the **Manage services** topic in **Apsara Uni-manager Management Console User Guide**.

**What to do next**

**VPC-to-VPC connection list**

On the **VPC-to-VPC** page, you can view the created peering connections.

> **Note**
>
> At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

- You can use a keyword or a specific filter condition to filter peering connections.

- Click the <img src="assets/362fdc387951132f8acc618f76230478.png" width="18" alt=""> icon in the upper-right corner of the peering connection list to select the

  columns that you want to show or hide. You can also drag a column name to adjust its order.

- Click the ID in the **Requester** column to view the details of the requester.

- Click **Route Settings** in the **Requester** column to manage the route configurations of the requester.

- Click the ID in the **Acceptor** column to view the details of the acceptor.

- Click **Route Settings** in the **Acceptor** column to manage the route configurations of the acceptor.

- Click the <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> icon next to the value in the **Requester** or **Acceptor** column to modify the

  name of the requester or acceptor.

**Tag management**

You can manage tags of peering connections on the **VPC-to-VPC** page. For more information, see Manage tags.

**Modify peer information**

You can modify the peer information when a peering connection is not active.

1. On the **VPC-to-VPC** page, find the peering connection that you want to modify and click **Modify Peer Info** in the **Actions** column.

2. In the **Modify Peer Info** dialog box, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Peer Router Interface Organization UID | Enter the UID of the organization to which the peer router belongs. |
   | Peer Router Interface ID | Enter the ID of the peer router interface. |
   | Peer Router ID | Enter the ID of the peer router. |

**Initiate a connection**

> **Note**
>
> If you create a peering connection for two VPCs within the same account, the system of Express Connect automatically creates the requester and acceptor. You do not need to manually initiate the connection. The system automatically sends the connection request and establishes the connection.
>
> If you create a peering connection for two VPCs that belong to different accounts, you must manually initiate the connection. Only the requester can initiate the peering connection. The acceptor must wait for the requester to initiate the peering connection.

1. On the **VPC-to-VPC** page, find the peering connection and click **Initiate Connection** in the **Actions** column.

2. In the **Initiate Connection** message, click **OK**.

**Disable a peering connection**

You can disable a requester VPC or acceptor VPC of a peering connection. After a peering connection is disabled, data is no longer transmitted between the VPCs.

1. On the **VPC-to-VPC** page, find the peering connection and click **Disable Requester** or **Disable Acceptor** in the **Actions** column.

2. In the message that appears, click **OK**.

**Enable a peering connection**

You can enable a disabled peering connection. After a peering connection is enabled, data is transmitted between the VPCs.

1. On the **VPC-to-VPC** page, find the peering connection and click **Enable Requester** or **Enable Acceptor** in the **Actions** column.

2. In the message that appears, click **OK**.

**Delete a peering connection**

1. On the **VPC-to-VPC** page, find the peering connection and click **Delete** in the **Actions** column.

2. In the **Delete** message, click **OK**.

<a id="section-4-2"></a>

## 4.2. Configure routes

This topic describes how to configure route tables for a virtual private cloud (VPC) peering connection.

**Add peer routes to the requester**

> **Note**
>
> In this example, you can manage only operating system route tables. To manage custom route tables, go to the Route Tables page in the VPC console.

1. Log in to the Express Connect console.

2. In the left-side navigation pane, click **VPC-to-VPC**.

3. On the **VPC-to-VPC** page, find the peering connection that you want to manage and click **Route Settings** in the **Requester** column.

4. In the panel that appears, view the basic information about the route table and the list of added routes.

   - In the **Basic Information**section, the route table ID, router ID, whether IPv6 is supported, and the time when the route table was created are displayed.

   - In the route list, you can search for route entries by destination CIDR block.

5. Click **Add Peer Route**.

6. In the **Add Route** dialog box, configure the parameters described in the following table and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Destination CIDR Block | The type of the destination CIDR block. Valid values:<br>• IPv4 CIDR Block<br>• IPv6 CIDR Block |
   | <strong>IPv4 CIDR Block</strong> or IPv6 CIDR Block | After you configure the <strong>Destination CIDR Block</strong> parameter, specify a CIDR block of the selected type.<br>If you set the <strong>Destination CIDR Block</strong> parameter to <strong>IPv4 CIDR Block</strong>, you can click <strong>Add CIDR Block</strong> to enter multiple destination CIDR blocks. |
   | Next Hop Type | The type of the next hop. Be default, <strong>Router Interface (to VPC)</strong> is selected.<br><strong>Router Interface (to VPC)</strong>: routes the traffic destined for the specified CIDR block to the specified VPC. |
   | VPC | The VPC instance used to receive traffic. |
   | Description | The description of the route.<br>The description must be 2 to 256 characters in length and cannot start with <code> http:// </code> or <code> https:// </code>. |

7. In the **Add Peer Route** message that appears, wait until all CIDR blocks are in the **Successful** state and click **OK**.

**Add peer routes to the acceptor**

> **Note**
>
> In this example, you can manage only operating system route tables. To manage custom routing tables, go to the Route Tables page in the VPC console.

1. Log in to the Express Connect console.

2. In the left-side navigation pane, click **VPC-to-VPC**.

3. On the **VPC-to-VPC** page, find the peering connection that you want to manage and click **Route Settings** in the **Acceptor** column.

4. In the panel that appears, view the basic information about the route table and the list of added routes.

   - In the **Basic Information**section, the route table ID, router ID, whether IPv6 is supported, and the time when the route table was created are displayed.

   - In the route list, you can search for route entries by destination CIDR block.

5. Click **Add Peer Route**.

6. In the **Add Route** dialog box, configure the parameters described in the following table and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Destination CIDR Block | The type of the destination CIDR block. Valid values:<br>• IPv4 CIDR Block<br>• IPv6 CIDR Block |
   | <strong>IPv4 CIDR Block</strong> or IPv6 CIDR Block | After you configure the <strong>Destination CIDR Block</strong> parameter, specify a CIDR block of the selected type.<br>If you set the <strong>Destination CIDR Block</strong> parameter to <strong>IPv4 CIDR Block</strong>, you can click <strong>Add CIDR Block</strong> to enter multiple destination CIDR blocks. |
   | Next Hop Type | The type of the next hop. Be default, <strong>Router Interface (to VPC)</strong> is selected.<br><strong>Router Interface (to VPC)</strong>: routes the traffic destined for the specified CIDR block to the specified VPC. |
   | VPC | The VPC instance used to receive traffic. |
   | Description | The description of the route.<br>The description must be 2 to 256 characters in length and cannot start with <code> http:// </code> or <code> https:// </code>. |

7. In the **Add Peer Route** message that appears, wait until all CIDR blocks are in the **Successful** state and click **OK**.

<a id="section-5"></a>

# 5.VBR-to-VPC connections

You can create a peering connection to enable communication between a Virtual Private Cloud (VPC) and a Virtual Border Router (VBR). This topic describes how to establish a peering connection by using a VBR-to-VPC connection.

**Prerequisites**

You have created the VPC instance that you want to connect. For more information, see the **Create and manage a VPC** chapter in the **Virtual Private Cloud User Guide**.

You have created the VBR instance that you want to connect. For more information, see Create a Virtual Border Router.

**Create a peering connection**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **VBR-to-VPC Connection**.

3. On the **VBR-to-VPC Connection** page, click **Create Peering Connection**.

4. On the **Create Peering Connection** page, set the following parameters.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">VBR-side configuration</td>
     </tr>
     <tr>
       <td>Organization/Resou rce set</td>
       <td>Select the organization and resource set to which the VBR belongs.</td>
     </tr>
     <tr>
       <td>Region</td>
       <td>Select the region where the VBR is located.</td>
     </tr>
     <tr>
       <td>Router type</td>
       <td>Select the router type on the VBR side. Currently, only the default <strong>Virtual</strong> <strong>Border Router</strong> type is supported.</td>
     </tr>
     <tr>
       <td>Access point</td>
       <td>Select an access point.</td>
     </tr>
     <tr>
       <td>VBR</td>
       <td>Select the VBR ID.</td>
     </tr>
     <tr>
       <td>Router interface specification</td>
       <td>Select the router interface specification on the VBR side.<br>• 1000 Mbps<br>• 2000 Mbps<br>• 5000 Mbps<br>• 10000 Mbps</td>
     </tr>
     <tr>
       <td>Router interface name</td>
       <td>Enter a name for the router interface on the VBR side.<br>The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-), but cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Description</td>
       <td>Enter a description for the VBR side.<br>The description must be 2 to 256 characters in length, start with a letter or a Chinese character, and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td colspan="2">VPC-side configuration</td>
     </tr>
     <tr>
       <td>Organization/Resou rce set</td>
       <td>Select the organization and resource set to which the VPC belongs.<br>Note<br>If the acceptor VPC belongs to a different organization, the other organization must confirm the connection.</td>
     </tr>
     <tr>
       <td>Region/Availability zone</td>
       <td>Select the region and availability zone where the VPC is located.</td>
     </tr>
     <tr>
       <td>Router type</td>
       <td>Select the router type on the VPC side. Currently, only the default <strong>VPC</strong> <strong>router</strong> type is supported.</td>
     </tr>
     <tr>
       <td>VPC</td>
       <td>Select a VPC.</td>
     </tr>
     <tr>
       <td>Router interface name</td>
       <td>Enter a name for the router interface on the VPC side.<br>The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-), but cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Description</td>
       <td>Enter a description for the VPC side.<br>The description must be 2 to 256 characters in length, start with a letter or a Chinese character, and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
     </tr>
     <tr>
       <td>Health check source IP</td>
       <td>Enter the source IP address for the health check.<br>Note<br>The health check source IP address must be an available IP address within the CIDR block of a VSwitch in the local VPC.</td>
     </tr>
     <tr>
       <td>Health check destination IP</td>
       <td>Enter the destination IP address for the health check.<br>Note<br>The health check destination IP address must be the IP address of the port on the on-premises device at the other end of the leased line associated with the VBR.</td>
     </tr>
   </table>

   > **Note**
   >
   > Before you create the instance, you can view and verify the configuration in the **Configuration Overview** pane on the right side of the page.
   >
   > - Click a field to go to the corresponding parameter and modify it as needed.
   >
   > - Click **Quota Management** (if the organization/resource set has no quota) or click **Manage** in the **Quota** section (if the organization/resource set has a quota) to manage quotas for cloud products.
   >
   >   For more information about quota management, see the **Quota Management** chapter in the **Apsara Uni-manager Operations Console User Guide**.

5. Create the peering connection.

   - If a service exists in Service Management where **Cloud Resource** is set to **Router Interface (VBR Interconnection)**: confirm the configuration parameters and click **Confirm Order**.

   - If no service exists in Service Management where **Cloud Resource** is set to **Router Interface (VBR Interconnection)**: confirm the configuration parameters and click **Submit**.

   For more information about service management, see the **Manage services** topic in **Apsara Uni-manager Management Console User Guide**.

**More operations**

**VBR-to-VPC connection list**

The **VBR-to-VPC Connection** page lists the details of created peering connections.

> **Note**
>
> The list is limited to 100 pages and can display a maximum of 10,000 entries. To view data beyond this limit, use the filter feature.

- You can search for a specific peering connection by entering a keyword or using advanced filters.

- Click an instance ID in the **Initiator Instance** column to view the configuration information of the initiator instance.

- Click an instance ID in the **Acceptor Instance** column to view the configuration information of the acceptor instance.

- Click the <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> icon next to the name in the **Initiator Instance** column to modify the initiator

  router interface name.

  The name must be 2 to 128 characters in length, must start with a letter or a Chinese character, and can contain digits, underscores (_), and hyphens (-).

**Tag management**

On the **VBR-to-VPC Connection** page, you can use tags to mark and group peering connections. For more information, see Manage tags.

**Initiate a connection**

1. On the **VBR-to-VPC Connection** page, find the target peering connection, and in the **Actions** column, click **Initiate Connection**.

2. In the dialog box that appears, click **OK**.

**Deactivate a connection**

You can deactivate either the initiator or acceptor instance of an active peering connection. After you deactivate an instance, data forwarding stops.

1. On the **VBR-to-VPC Connection** page, find the target peering connection, and in the **Actions** column, click **Deactivate Initiator** or **Deactivate Acceptor**.

2. In the dialog box that appears, click **OK**.

**Activate a connection**

If you need to use a deactivated peering connection again, you can reactivate the instance. After you activate the instance, data forwarding resumes.

1. On the **VBR-to-VPC Connection** page, find the target peering connection, and in the **Actions** column, click **Activate Initiator** or **Activate Acceptor**.

2. In the dialog box that appears, click **OK**.

**Health check**

> **Note**
>
> - Health checks are supported when both the source and destination are IPv6 addresses.
>
> - Health checks are not supported when the source is an IPv4 address and the destination is an IPv6 address. An "invalid address" error occurs.
>
> - Health checks are not supported when the source is an IPv6 address and the destination is an IPv4 address. An "invalid address" error occurs.
>
> - Health checks are supported when both the source and destination are IPv4 addresses.

1. On the **VBR-to-VPC Connection** page, find the target peering connection, and in the **Actions** column, click **Health Check**.

2. In the **Health Check** dialog box, configure the following parameters, select **I have read and understood the risks**, and then click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Health check source IP | Enter the source IP address for the health check. |
   | Health check destination IP | Enter the destination IP address for the health check. |
   | Probe interval | The interval at which health check probe packets are sent. Unit: seconds.<br>Default: 2. Valid values: 1 to 10.<br>Important<br>Setting the probe interval to a very short value may cause frequent service switchovers. |
   | Number of probes | The number of probe packets sent for each health check. Unit: packets.<br>Default: 8. Valid values: 3 to 8. |

**Delete a connection**

> **Warning**
>
> Before you delete a VBR-to-VPC connection, you must verify whether any bare-metal resources exist in the peer VPC.

1. On the **VBR-to-VPC Connection** page, find the target peering connection, and in the **Actions** column, click **Delete**.

2. (Optional) If bare-metal resources exist in the peer VPC, follow the prompts in the dialog box to confirm that you want to delete the connection, and then click **OK**.

3. In the **Delete** dialog box, click **OK**.

<a id="section-6"></a>

# 6.Physical connections

<a id="section-6-1"></a>

## 6.1. Create and manage connections over Express Connect circuits

To create a dedicated connection, you must apply for an Express Connect circuit in the console, complete the installation, and then enable the connection.

**Apply for an Express Connect circuit**

> **Note**
>
> To apply for an Express Connect circuit, you need to log on to the Apsara Uni-manager Operations Console.

1. Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.

3. On the **Physical Connection** page, click **Apply for Physical Connection**.

4. Go to the Apsara Uni-manager Operations Console to configure an Express Connect circuit as prompted.

**Related operations**

**The list of Express Connect circuits**

On the **Express Connect circuit** page, you can view the created Express Connect circuit in the list.

> **Note**
>
> At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

- You can use a keyword or a specific filter condition to filter Express Connect circuits.

- Click <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> next to the name of an Express Connect circuit in the **ID/Name** column to modify

  the name.

  The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter and cannot start with  `http://` or  `https://` .

**Tag management**

On the **Physical Connection** page, you can manage tags of Express Connect circuits. For more information, see Manage tags.

**Enable an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit in the **Disabled** state and click **Enable Connection** in the **Actions** column.

2. In the **Enable Connection** message, click **OK**.

**Cancel an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit and click **Cancel Connection** in the **Actions** column.

2. In the **Cancel Connection** message, click **OK**.

**Disable an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit and click **Disable Connection** in the **Actions** column.

2. In the **Disable Connection** message, click **OK**.

**Delete a connection over an Express Connect circuit**

For more information, see Delete a connection over an Express Connect circuit.

**Manage Express Connect circuits**

1. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the **ID/Name** column.

2. You can manage an Express Connect circuit on the details page.

   - You can view the basic information in the **Basic Information** section.

     - Click **Modify** in the upper-right corner to modify the information. For more information, see Modify the information about an Express Connect circuit.

     - Click <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> next to **Description** to modify the description.

       The description must be 2 to 256 characters in length and cannot start with  `http://` or  `https://` .

   - You can manage VBRs associated with the Express Connect circuit in the **Connected VBRs** section. For more information, see Create and manage a VBR.

   - In the **Operation Log** section, you can view all operations logs of the Express Connect circuit. For more information, see Manage operation logs.

<a id="section-6-2"></a>

## 6.2. Modify an Express Connect circuit

You can modify the following information about an Express Connect circuit: the name, bandwidth, and the location of the customer data center.

**Procedure**

1. Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.

3. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the **ID/Name** column.

4. In the **Basic Information** section of the Express Connect circuit details page, click **Modify** in the upper-right corner.

5. In the dialog box that appears, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Name | Enter a name for the Express Connect circuit. |
   | Bandwidth | Enter a maximum bandwidth value for the Express Connect circuit. Unit: Mbit/s. |
   | Data Center Location | Specify the location of the data center. |

<a id="section-6-3"></a>

## 6.3. Delete a connection over an Express Connect circuit

You can delete a connection over an Express Connect circuit that is in the Disabled state.

**Background information**

To delete a connection over an Express Connect circuit, perform the following operations in order:

1. Delete the routes on the router of the virtual private cloud (VPC) and routes on the virtual border router (VBR).

2. If Border Gateway Protocol (BGP) routing is configured, delete the BGP peers and BGP groups.

3. Delete a peering connection.

4. Delete the associated VBRs.

5. If the connection is not disabled, disable the connection.

6. Delete the connection over the Express Connect circuit.

**Step 1: Delete routes**

Delete routes on the VPC and the VBR.

1. Delete the routes in custom route tables in the VPC. For more information, see **Manage custom routes** in **VPC User Guide**.

2. Delete the routes on the VBR. For more information, see Delete routes.

**Step 2: Delete BGP peers and BGP groups**

If BGP is configured, you must delete the BGP settings. For more information, see Delete a BGP group and Delete a BGP peer.

**Step 3: Delete peering connections**

Delete the peering connection between the VPC and the VBR. For more information, see Delete a VBR-to-VPC connection.

**Step 4: Delete the associated VBRs**

Delete the VBRs. For more information, see Delete a VBR.

**Step 5: Disable the connection over the Express Connect circuit**

1. Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.

3. On the **Physical Connection** page, find the Express Connect circuit and click **Disable Connection** in the **Actions** column.

4. In the **Disable Connection** message, click **OK**.

**Step 6: Delete the connection over the Express Connect circuit**

1. On the **Physical Connection** page, find the **Disabled** connection and click **Delete** in the **Actions** column.

2. In the **Delete** message, click **OK**.

<a id="section-6-4"></a>

## 6.4. Manage a VBR

After you enable an Express Connect circuit, you must create a virtual border router (VBR) for the Express Connect circuit. The VBR is used to route traffic between the virtual private cloud (VPC) and your data center.

**Add a VBR for a connection over an Express Connect circuit**

1. Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.

3. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the **ID/Name** column.

4. On the details page of the Express Connect circuit, click **Create VBR** in the **Connected VBRs** section. For more information, see Create a VBR.

**What to do next**

**Modify a VBR**

On the details page of the Express Connect circuit, find the VBR in the **Connected VBRs** section and click **Modify** in the **Actions** column. For more information, see Modify a VBR.

**Disable a VBR**

1. On the details page of the Express Connect circuit, find the VBR in the **Connected VBRs** section and click **Disable Connection** in the **Actions** column.

2. In the **Disable Connection** message, click **OK**.

<a id="section-7"></a>

# 7.VBRs

<a id="section-7-1"></a>

## 7.1. Create and manage a VBR

A VBR is a router between a customer-premises equipment (CPE) in a data center and a VPC. This topic describes how to create and manage a VBR.

**Create a VBR**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, click **Create VBR**.

4. In the **Create VBR** dialog box, specify the following parameters and click **OK**.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">Basic Information</td>
     </tr>
     <tr>
       <td>Account Type</td>
       <td>• <strong>Current Organization</strong>: creates a VBR for the current organization.<br>• <strong>Another Organization</strong>: creates a VBR for another organization.<br>In this example, <strong>Current Organization</strong> is selected.</td>
     </tr>
     <tr>
       <td>Organization</td>
       <td>Select an organization for the VBR.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Resource Set</td>
       <td>Select the resource set to which the VBR belongs.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Name</td>
       <td>Enter a name for the VBR.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Current</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td>Organization UID</td>
       <td>Enter the UID of another organization.<br>Note<br>This parameter is required if you set <strong>Account Type</strong> to <strong>Another</strong> <strong>Organization</strong>.</td>
     </tr>
     <tr>
       <td colspan="2">Physical Connection Configurations</td>
     </tr>
     <tr>
       <td>Physical Connection</td>
       <td>Select an Express Connect circuit that is enabled and works as expected.</td>
     </tr>
     <tr>
       <td>VLAN ID</td>
       <td>Enter a VLAN ID for the VBR. Valid values: 0 to 3999.<br>• If the VLAN ID is set to 0, VLAN is not enabled and the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface.<br>When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR.<br>• If the VLAN ID is set to a value from 1 to 3999, the switch port on the VBR is a Layer 3 VLAN subinterface.<br>When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2.<br>Important<br>The VLAN ID that you specify for the VBR and that of the customer-premises device must be the same.</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center.</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Customer Side</td>
       <td>Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv4 Address)</td>
       <td>Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center.</td>
     </tr>
     <tr>
       <td>IPv6 Support</td>
       <td>Specify whether to enable IPv6.<br>• <strong>Disable</strong>: disables IPv6.<br>• <strong>Enable (You cannot disable this feature after it is enabled.)</strong>: If IPv6 is enabled, the VPC and data center can use IPv6 addresses.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Customer Side</td>
       <td>Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv6 Address)</td>
       <td>Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
   </table>

   > **Note**
   >
   > Specify the IP addresses based on your network plan. The IP addresses must be in the same CIDR block. We recommend that:
   >
   > 1. The specified IP addresses do not conflict with IP addresses in the cloud or on-
   >
   > premises IP addresses.
   >
   > 2. Use private IP addresses.
   >
   > Example:
   >
   > IPv4 address of the gateway at the Alibaba Cloud side: 10.0.0.1
   >
   > IPv4 address of the gateway at the customer side: 10.0.0.2
   >
   > IPv4 subnet mask: 255.255.255.252
   >
   > Set IPv6 Address of Gateway at Alibaba Cloud Side to 2408:4004:cc:400::1 (GUA address).
   >
   > Set IPv6 Address of Gateway at Customer Side to 2408:4004:cc:400::2 (GUA address).
   >
   > Set Subnet Mask (IPv6 Address) to 2408:4004:cc:400::/56.

**Related operations**

**VBR list**

On the **Virtual Border Router** page, you can view the created VBRs in the list.

> **Note**
>
> At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

- You can use a keyword or a specific filter condition to filter VBRs.

- Click <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> next to the name in the **ID/Name** column to modify the name of the VBR.

**Manage tags**

On the **Virtual Border Router** page, you can use tags to group VBRs. For more information, see Manage tags.

**Modify a VBR**

1. On the **Virtual Border Router** page, find the VBR that you want to modify and click **Edit** in the **Actions** column.

2. In the **Modify VBR** dialog box, specify the following parameters and click **OK**.

   <table>
     <tr>
       <th>Parameter</th>
       <th>Description</th>
     </tr>
     <tr>
       <td colspan="2">Physical Connection Configurations</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center.</td>
     </tr>
     <tr>
       <td>IPv4 Address of Gateway at Customer Side</td>
       <td>Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv4 Address)</td>
       <td>Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center.</td>
     </tr>
     <tr>
       <td>IPv6 Support</td>
       <td>Specify whether to enable IPv6.<br>• <strong>Disable</strong>: disables IPv6.<br>• <strong>Enable (You cannot disable this feature after it is enabled.)</strong>: If IPv6 is enabled, the VPC and data center can use IPv6 addresses.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Alibaba Cloud Side</td>
       <td>Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>IPv6 Address of Gateway at Customer Side</td>
       <td>Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td>Subnet Mask (IPv6 Address)</td>
       <td>Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center.<br>Note<br>This parameter is required if <strong>Enable</strong> is selected for the <strong>IPv6 Support</strong> parameter.</td>
     </tr>
     <tr>
       <td colspan="2">BFD Detection Mode (Applicable to BFD Single-hop Scenarios)</td>
     </tr>
     <tr>
       <td>Sending Interval</td>
       <td>Enter the sending interval. Unit: milliseconds.<br>Sending interval range: 200 to 1000 milliseconds. You can only enter an integer.</td>
     </tr>
     <tr>
       <td>Reception Interval</td>
       <td>Enter the reception interval. Unit: milliseconds.<br>Reception interval range: 200 to 1000 milliseconds. You can only enter an integer.</td>
     </tr>
     <tr>
       <td>Number of Probes</td>
       <td>Enter the number of probes. Unit: times.<br>Valid values: 3 to 10.</td>
     </tr>
   </table>

**Delete a VBR**

Before you delete a VBR, you must delete the Border Gateway Protocol (BGP) groups, BGP peers, and BGP routes that are configured on the VBR. For more information, see Delete a BGP group, Delete a BGP peer, and Delete routes.

1. On the **Virtual Border Routers** page, find the VBR that you want to delete and click **Delete** in the **Actions** column.

2. In the **Delete** message, click **OK**.

**Manage a VBR**

1. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

2. On the details page of the VBR, you can manage the VBR.

   - In the **Basic Information** section, you can view the basic information about the VBR. You can manage routes, configure routes, manage BGP, manage VBR-to-VPC connections, and configure failover groups.

   - Click the **Physical Connection** tab to manage Express Connect circuits connected to the VBR. For more information, see Manage Express Connect circuits.

   - Click the **Route Entries** tab to manage routes on the VBR. For more information, see Add and manage routes.

   - Click the **BGP CIDR Blocks** tab to manage the BGP CIDR blocks. For more information, see Configure and manage BGP.

   - Click the **BGP Groups** tab to manage the BGP groups. For more information, see Configure and manage BGP.

   - Click the **BGP Peers** tab to manage the BGP peers related to the VBR. For more information, see Configure and manage BGP.

   - Click the **VBR-to-VPC** tab to manage VBR-to-VPC connections. For more information, see Manage VBR-to-VPC connections.

   - Click the **Failover Groups** tab to manage failover groups. For more information, see Configure failover groups.

   - Click the **CEN Cross-Account Authorization** tab to manage cross-account authorization. For more information, see CEN cross-account authorization.

   - On the **Operation Log** tab, you can view all operations logs of the VBR. For more information, see Manage operation logs.

<a id="section-7-2"></a>

## 7.2. Manage Express Connect circuits

After you create a virtual border router, you can associate an Express Connect circuit with the VBR or modify the Express Connect circuits that are already associated with the VBR.

**Add an Express Connect circuit**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Physical Connection** tab.

5. Click **Add Physical Connection**.

6. In the **Add Physical Connection** dialog box, specify the parameters. For more information, see Create a peering connection.

**Modify an Express Connect circuit**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Physical Connection** tab.

5. In the Physical Connection list, find the Express Connect circuit and click **Modify** in the **Actions** column.

6. In the **Modify Physical Connection** dialog box, specify the parameters. For more information, see Modify a VBR.

<a id="section-7-3"></a>

## 7.3. Add and manage routes

You can add routes to the route table of a virtual border router (VBR) to manage where network traffic is forwarded. This topic describes how to add and manage routes.

**Background information**

After you create a VBR, you must add routes that point to the Express Connect circuit and the virtual private cloud (VPC) to route network traffic to the data center and the VPC. You can also configure Border Gateway Protocol (BGP) routing for a VBR. For more information, see Configure and manage BGP.

**Add a route**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Route Entry** tab.

5. Click **Add Route Entry**.

6. In the **Add Route Entry** dialog box, configure the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Next Hop Type | Select the type of next hop. Valid values:<br>• <strong>VPC</strong>: The VBR routes network traffic to a VPC.<br>• <strong>Physical Connection</strong>: The VBR routes network traffic to an Express Connect circuit. |
   | Destination CIDR Block | Enter the destination CIDR block. |
   | Next Hop | The next hop. |

**Delete a route**

> **Important**
>
> - Before you delete a route, make sure that the **Status** of the route is **Available**.
>
> - Before you delete a route whose **Next Hop Type** is **VPC**, check whether bare metal resources exist in the peer VPC.

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Route Entry** tab.

5. In the route list, find the route that you want to delete and click **Delete** in the **Actions** column.

6. Optional. If **Next Hop Type** of the route is **VPC**, delete the route as prompted in the dialog box that appears and click **OK**

7. In the **Delete** message, click **OK**.

<a id="section-7-4"></a>

## 7.4. Configure and manage BGP

You can configure Border Gateway Protocol (BGP) routing to enable communication between a data center and a virtual border router (VBR). You must add the BGP peer that communicates with the VBR to a BGP group, and then advertise the BGP CIDR block on the VBR. This topic describes how to configure and manage BGP.

**Background information**

BGP is a dynamic routing protocol based on TCP. BGP is used to exchange routing information and network accessibility information in different autonomous systems. If you use an Express Connect circuit to connect to Apsara Stack, you can configure BGP routing to enable communication between your data center and the virtual border router (VBR) that is associated with the Express Connect circuit. BGP allows you to build hybrid clouds in a more efficient, flexible, and reliable way.

Before you configure BGP routing, you must create a BGP group. BGP groups are used to simplify BGP configurations. You can add BGP peers with the same configurations to one BGP group. You need to only create a BGP group with an autonomous system number (ASN) and add BGP peers that meet your requirements to the BGP group. After you add the BGP peers to the BGP group, the BGP peers share the configurations of the BGP group. You do not need to configure each BGP peer separately.

**Limits**

Before you configure BGP routing, take note of the following limits:

- You can specify only the data center as the BGP peer of a VBR. The data center is connected to the VBR by using an Express Connect circuit. Static routing is required between a VBR and a virtual private cloud (VPC).

- VBRs support only BGP-4.

- You can create up to eight BGP peers for each VBR.

- Each BGP peer supports up to 110 dynamic routes. Routes are denied when the upper limit is exceeded.

- To configure BGP routing when you connect to a VPC, you must specify an ASN for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

**Configure BGP**

**Step 1: Create a BGP group**

Before you configure BGP routing, you must create a BGP group with the requested ASN.

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **BGP Groups** tab.

5. Click **Create BGP Group**.

6. In the **Create BGP Group** dialog box, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | IPv6 Support | Specify whether to enable IPv6.<br>• <strong>Yes</strong>: enables IPv6. After you enable IPv6, the endpoints of VPC and your data center can be IPv6 addresses.<br>• <strong>No</strong>: disables IPv6. |
   | Name | Enter a name for the BGP group.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>. |
   | Peer ASN | Enter the ASN of the data center.<br>Valid values for ASN: 1 to 65534 and 4200000000 to 4294967294. |
   | BGP Key | The key of the BGP group. |
   | Description | Enter the description of the BGP group.<br>The description must be 2 to 256 characters in length and cannot start with <code> http:// </code> or <code> https:// </code>. |
   | Local ASN | The local ASN.<br>Valid values for ASN: 1 to 65534 and 4200000000 to 4294967294. |

**Step 2: Create a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.

2. Click **Create BGP Peer**.

3. In the **Create BGP Peer** dialog box, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | BGP Group | The BGP group to which you want to add the BGP peer. |
   | BGP Peer IP Address | Enter the IP address of the BGP peer. |
   | Enable BFD | Specify whether to enable BFD. |
   | BFD Hop Count | Enter the number of BFD hops.<br>Note<br>This parameter is required only if you enable BFD. |

**Step 3: Advertise the BGP CIDR block**

After you create the BGP peer, you must advertise the CIDR block of the VPC. After the BGP session is established, the VBR automatically learns the CIDR block of the data center.

1. On the details page of the VBR, click the **Advertise BGP Subnet** tab.

2. Click **Advertise BGP Subnet**.

3. In the **Advertise BGP Subnet** dialog box, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Advertised Subnet | Enter the BGP CIDR block to be advertised. |

**What to do next**

**Modify a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.

2. Find the BGP peer and click **Edit** in the **Actions** column.

3. In the **Modify BGP Peer** dialog box, modify the **BGP Peer IP**, **Enable BFD**, and **BFD Hop Count** parameters, and click **OK**.

**Delete a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.

2. Find the BGP peer and click **Delete** in the **Actions** column.

3. In the dialog box that appears, click **OK**.

**Modify a BGP group**

1. On the details page of the VBR, click the **BGP Groups** tab.

2. Find the BGP group and click **Edit** in the **Actions** column.

3. In the **Modify BGP Group** dialog box, modify the **Name**, **Peer ASN**, **BFD Hop Count**, **Description**, and **Local ASN**, and click **OK**.

**Delete a BGP group**

1. On the details page of the VBR, click the **BGP Groups** tab.

2. Find the BGP group and click **Delete** in the **Actions** column.

3. In the dialog box that appears, click **OK**.

**Delete a BGP CIDR block**

1. On the details page of the VBR, click the **Advertise BGP Subnet** tab.

2. Find the BGP CIDR block and click **Delete** in the **Actions** column.

3. In the dialog box that appears, click **OK**.

<a id="section-7-5"></a>

## 7.5. Manage VBR-to-VPC connections

This topic describes how to create a peering connection. After you create a virtual border router (VBR), you must create a peering connection between the VBR and a virtual private cloud (VPC). This way, the VBR can route traffic between the VPC and the data center that is connected to the VBR.

**Create a peering connection**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **VBR-to-VPC** tab.

5. Click **Create Peering Connection**.

6. On the **Create BGP Group** page, create a peering connection. For more information, see Create a peering connection.

**Manage a peering connection**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **VBR-to-VPC** tab.

5. On the Virtual Border Router page, you can manage peering connections. For more information, see What to do next.

<a id="section-7-6"></a>

## 7.6. Configure a failover group

When the system detects a failure in an Express Connect circuit, the system performs a failover within a few seconds. To accelerate failovers, you can add virtual border routers (VBRs) to a failover group. After the system detects failures on a VBR by using Bidirectional Forwarding Detection (BDF), the system can seamlessly switch workloads to the standby VBR in the failover group within one second. This accelerates route convergence.

**Limits**

- You can add only VBRs that have BFD enabled to failover groups.

- Each failover group can contain only two VBRs and each VBR can be added to only one failover group.

- The two VBRs in the same failover group must belong to the same region.

- You must configure the VBRs in a failover group as active and standby VBRs and configure load balancing for the VBRs.

**Prerequisites**

- Two VBRs are created in the same region and each VBR is connected to your data center over an Express Connect circuit. For more information, see Create a VBR and Add routes.

- BFD is configured for the VBRs. For more information, see Configure BGP.

**Create a failover group**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Failover Groups** tab.

5. Click **Configure Backup Next Hop**.

6. In the **Configure Backup Next Hop** dialog box, set the following parameters and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Region | The system automatically displays the region where the VBR is deployed. |
   | Failover Group Name | Enter a name for the failover group.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>. |
   | Description | Enter a description for the failover group.<br>The description must be 2 to 256 characters in length and cannot start with <code> http:// </code> or <code> https:// </code>. |
   | Failover Group VBRs | Select a standby VBR from the drop-down list.<br>The system lists all VBRs that are in the same region as the current VBR. |

   After you complete the preceding steps, the **status** of the failover group changes to **Normal**.

   > **Note**
   >
   > - You cannot modify the configuration of a failover group after the failover group is created.
   >
   > - If the configuration does not meet your requirements, you can delete the failover group and create one again. For more information, see Delete a failover group.

**Delete a failover group**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **Failover Groups** tab.

5. In the failover group list, find the failover group that you want to delete and click **Delete** in the **Actions** column.

6. In the dialog box that appears, click **OK**.

<a id="section-7-7"></a>

## 7.7. Attach a VBR to a CEN instance across accounts

You can attach a virtual border router (VBR) to a Cloud Enterprise Network (CEN) instance that belongs to another account. You need to log on to the VBR that belongs to Account A and then grant permissions to the CEN instance that belongs to Account B. After the authorization is complete, the VBR can be attached to the CEN instance.

**CEN authorization**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **CEN Cross-Account Authorization** tab.

5. Click **CEN Authorization**.

6. In the **CEN Authorization** dialog box, specify **Peer Level-1 Organization UID** and **Peer CEN Instance ID**, and then click **OK**.

**Revoke CEN authorization**

You can revoke the CEN authorization based on your business requirements. Revoking the CEN authorization does not disconnect the VBR that corresponds to the CEN instance.

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click **Virtual Border Router**.

3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.

4. On the details page of the VBR, click the **CEN Cross-Account Authorization** tab.

5. In the list of authorized CEN instances, find the CEN instance and click **Delete** in the **Actions** column.

6. In the **Cancel Authorization** dialog box, confirm the account ID and CEN instance ID, and click **OK**.

<a id="section-8"></a>

# 8.Manage operation logs

Express Connect allows you to view the operation logs of related resources. The operation logs record the instance status, operation source, operation time, and API call details. You can analyze and trace historical operations based on the operation logs.

**View operation logs**

1. Log in to the Express Connect console.

2. In the left-side navigation pane, click **Operation Logs**.

3. On the Operation Logs page, view the operation logs.

   > **Note**
   >
   > - Operation logs are retained for seven days. To adjust the retention period, modify the log storage settings as an administrator.
   >
   > - If you extend the retention period by modifying the log storage settings, the log data before the new retention period is not recorded.
   >
   > - Up to 100 pages of records can be displayed on the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records.

4. Click **Advanced Filter** to search for operation logs by specifying filter conditions. The following table describes the filter conditions.

   | Filter condition | Description |
   | --- | --- |
   | Resource Type | The resource type. Valid values: <strong>Router Interface</strong>, <strong>VBR</strong>, and <strong>Express</strong> <strong>Connect Circuit</strong>. |
   | Event Type | The event type. Valid values: <strong>Delete Events</strong>, <strong>Create Events</strong>, and <strong>Query</strong> <strong>Events</strong>. |
   | Starting and ending time | The time range that you want to query. By default, the current month is selected. |
   | Resource ID | The ID of the resource. |
   | IP Address | The IP address of the operation. |
   | Read/Write Type | The type of the operation. Valid values: <strong>Read Operation </strong>and <strong>Write</strong> <strong>Operation</strong>. |
   | Operation Result | The result of the operation. Valid values: <strong>Success</strong> and <strong>Failed</strong>. |
   | Keywords | The keyword. You can enter an event ID, a resource ID, an operation source IP address, or an operation name. |

5. **Optional.** Find the operation that you want to manage and click **View** in the **Details** column. In the **View Operation Details** panel, view information in the **Basic Information** and **Instance Details** sections.

**View operation logs on the instance details page**

1. Log in to the Express Connect console.

2. View the operation logs of a single instance on the instance details page.

   <ol type="i">

   <li>

   In the left-side navigation pane, click **Physical Connection** or **Virtual Border Router**.

   </li>

   <li>

   On the page that appears, find the instance that you want to manage and click its ID.

   </li>

   <li>

   On the instance details page, click the **Operation Logs** tab.

   </li>

   </ol>

   > **Note**
   >
   > - Operation logs are retained for seven days. To adjust the retention period, modify the log storage settings as an administrator.
   >
   > - If you extend the retention period by modifying the log storage settings, the log data before the new retention period is not recorded.
   >
   > - Up to 100 pages of records can be displayed on the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records.

3. **Optional.** Search for operation logs by specifying filter conditions, such as **Operation Name** and **Operator**. The following table describes the filter conditions.

   | Filter condition | Description |
   | --- | --- |
   | Operator | The user who performs the operation. |
   | Operation Name | The name of the operation. This is the API operation name. |
   | Execution Status | The execution status. Valid values: <strong>Success</strong> and <strong>Failed</strong>. |
   | Operation Source IP | The source IP address of the operation. |
   | Operation Time | The time range that you want to query. |

4. **Optional.** Find the operation that you want to manage and click **Operation Details** in the **Actions** column. In the **Operation Details** panel, view information in the **Basic Information** and **API Call Details** sections.

<a id="section-9"></a>

# 9.Manage tags

Express Connect allows you to search for and filter resources by tag. You can use tags to mark and classify the following resources: virtual border routers (VBRs), VPC-to-VPC connections, VBR-to-VPC connections, and connections over Express Connect circuits. This topic describes how to manage and use tags.

**Tag overview**

As the number of instances increases, it becomes more difficult to manage instances. You can use tags to group instances to help you search for and filter instances.

Tags are used to mark instances. Each tag consists of a key and a value. Before you use tags, take note of the following items:

- You can manage tags for VPC peering connections, VBR-to-VPC connections, Express Connect circuits, and VBRs.

- The keys of tags that are added to the same instance must be unique.

- The keys and values of tags can be modified or deleted at any time. If you delete an instance, all tags added to the instance are deleted. This operation does not affect the tags added to other instances.

- You can add up to 20 tags to an instance. This quota cannot be increased.

**Add tags**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click the menu item corresponding to the type of the resources that you want to manage.

3. Add tags to instances based on the following information.

   - Add a tag to a single resource

     <ol type="a">

     <li>

     On the instances page, find the instance, move the pointer over <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> in the **Tag** column,

     and click **Edit** in the pop-up message.

     </li>

     <li>

     In the **Edit Tags** dialog box, set the following parameters, click **Add** to add multiple tags, and then click **OK**.

     | Parameter | Description |
     | --- | --- |
     | Tag Key | Select or enter a tag key.<br>The tag key can be up to 64 characters in length and cannot start with <code> aliyun </code> or <code> acs: </code>. The tag key cannot contain <code> http:// </code> or <code> https:// </code>. |
     | Tag Value | Select or enter a tag value.<br>The tag value can be up to 128 characters in length and cannot start with <code> aliyun </code> or <code> acs: </code>. The tag value cannot contain <code> http:// </code> or <code> https:// </code>. |

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     In the **Edited** message, check the tag information and click **Close**.

     </li>

     </ol>

   - Add a tag to multiple resources

     <ol type="a">

     <li>

     On the instances page, select the instances to which you want to add tags and click **Batch Add Tags** in the lower-left corner.

     </li>

     <li>

     In the **Batch Add Tags** dialog box, configure the **Tag Key** and **Tag Value** parameters and click **OK**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     In the **Edited** message, check the tag information and click **Close**.

     </li>

     </ol>

**Remove tags**

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click the menu item corresponding to the type of the resources that you want to manage.

3. Remove tags based on the following information.

   - Remove tags from an instance

     <ol type="a">

     <li>

     On the instances page, find the instance, move the pointer over <img src="assets/54b23d43f206646e4fae66cdb08f6c90.png" width="13" alt=""> in the **Tag** column,

     and click **Edit** in the pop-up message.

     </li>

     <li>

     In the **Edit Tags** dialog box, click <img src="assets/60ac6eaaddc532a75dda41677b0a867f.png" width="16" alt=""> next to the tags that you want to delete, and then

     click **OK**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     In the **Edited** message, check the tag information and click **Close**.

     </li>

     </ol>

   - Remove tags from multiple instances

     <ol type="a">

     <li>

     On the instances page, select the instances from which you want to remove tags and click **Batch Remove Tags** in the lower-left corner.

     </li>

     <li>

     In the **Batch Remove Tags** dialog box, select the tags that you want to remove under **Tags to Remove**, and then click **OK**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     In the **Edited** message, check the tag information and click **Close**.

     </li>

     </ol>

**Search for instances by tag**

After you add tags to instances, you can quickly filter the instances by tag.

1. Log on to the Express Connect console.

2. In the left-side navigation pane, click the menu item corresponding to the type of the resources that you want to manage.

3. On the instances page, choose **Advanced Filter > Filter by Tag**.

4. In the dialog box that appears, specify **Tag Key** and **Tag Value**, and then click **Search**. The instances that have the specified tag keys and tag values are displayed.
