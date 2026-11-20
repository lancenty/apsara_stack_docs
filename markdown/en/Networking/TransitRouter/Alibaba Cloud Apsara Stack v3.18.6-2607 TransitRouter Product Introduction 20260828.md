Alibaba Cloud  
Apsara Stack  
TransitRouter  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Transit router](#section-1)
    - [1.1. Product details](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Scenarios](#section-1-3)
    - [1.4. Functions and features](#section-1-4)

<a id="section-1"></a>

# 1.Transit router

TransitRouter (TR) is an enterprise-grade networking solution that enables you to quickly build high-speed, high-quality, and stable connections between virtual private clouds (VPCs) in the same region, along with between multiple VPCs and data centers.

<a id="section-1-1"></a>

## 1.1. Product details

Transit Router (TR) supports establishing private network communication channels between virtual private clouds (VPCs) in the same region and between VPCs and data centers. TR also provides rich network interconnection and routing management capabilities, such as forwarding association, route learning, custom route tables, and routing policies. These capabilities allow enterprises to customize network connectivity and help them build flexible, reliable, and large-scale enterprise interconnection networks.

**Network instance connections**

Transit Router supports connections to Virtual Private Cloud (VPC) instances and Virtual Border Router (VBR) instances.

- VPC instances in the same region can communicate with each other after they are connected to a transit router instance.

- After a transit router instance is connected to a VBR instance, the data center associated with the VBR instance can communicate with VPC instances connected to the transit router.

**Routing**

Transit Router supports various routing management features, such as forwarding association, route learning, custom route tables, custom route entries, and routing policies. These features help enterprises customize network connectivity.

- **Custom route tables**

  After a transit router is connected to a network instance, it stores the routes of the network instance in a route table. The transit router forwards traffic from the network instance by querying the route entries in the route table.

  Each transit router has a default route table and supports the creation of custom route tables. The default route table and custom route tables are isolated from each other, which allows you to implement access isolation.

- **Forwarding association**

  The forwarding association feature controls traffic forwarding for network instances. After a forwarding association is established between a network instance connection and a transit router route table, the transit router forwards traffic from the network instance by querying the route entries in the route table.

- **Route learning**

  The route learning feature controls route advertisement for network instances. After a route learning relationship is established between a network instance connection and a transit router route table, the routes of the network instance are allowed to be advertised to the transit router route table.

- **Custom route entries**

  Route tables of transit routers support custom route entries. You can add custom route entries to a transit router route table to help control traffic forwarding for network instances.

- **Routing policies** A routing policy controls route advertisement for the route table of a transit router. A routing policy can determine whether to advertise routes in a transit router route table to network instances. It can also modify the properties of routes in a transit router route table.

**Multicast**

- Transit Router supports multicast traffic forwarding by default. After VPC instances in the same region are connected to a transit router instance, you can establish a multicast network between the VPC instances.

- You can create a Connect connection under a transit router to connect to a data center. VPC instances under the transit router and the on-premises data center can transmit multicast traffic through the Connect connection to enable multicast network communication between cloud and on-premises environments.

**Health check**

VBRs can connect data centers to Alibaba Cloud through Express Connect circuits. After a VBR instance is connected to a transit router instance, you can use the health check feature to detect the connectivity of the Express Connect circuit.

<a id="section-1-2"></a>

## 1.2. Benefits

Transit routers are easy to configure and quickly establish secure, flexible, high-speed, high-quality, and stable communication channels between VPCs in the same region and between multiple VPCs and on-premises data centers. This helps enterprises build large-scale enterprise-class interconnection networks.

**Large-scale network interconnection**

Transit routers quickly connect multiple VPC-connected instances and on-premises networks in the same region to enable resource communication. A transit router in the same region supports VPC peering for up to 300 VPCs, meeting enterprise network expansion needs.

**Low latency and high speed**

Transit routers provide low-latency and high-speed network transmission capabilities. The maximum transmission rate between resources in the same region can reach the port forwarding rate of network devices.

**High reliability and high quality**

Transit routers provide primary and secondary nodes that automatically switch between each other to ensure uninterrupted service. Multiple sets of high-quality transmission links exist between any two nodes in the network. When underlying links are interrupted, the network automatically converges without affecting your services.

<a id="section-1-3"></a>

## 1.3. Scenarios

Transit Router is used for scenarios such as connecting VPCs in the same region, connecting on-premises and cloud networks in the same region, and enabling multicast network communication.

**Connect VPCs in the same region**

After VPC-connected instances in the same region are connected to a transit router, they can communicate with each other.

**Connect on-premises data centers and VPCs**

When an on-premises data center is connected to a transit router through a VBR instance, it can communicate with VPC-connected instances that are connected to the same transit router in the same region.

**Cloud multicast networks**

After VPC-connected instances in the same region are connected to a transit router, they can communicate with each other through multicast networks via the transit router.

**Connect on-premises and cloud multicast networks**

On-premises data centers can connect directly to a transit router through Connect connections, enabling multicast network communication with VPC instances under the transit router through these Connect connections.

<a id="section-1-4"></a>

## 1.4. Functions and features

<table>
  <tr>
    <th colspan="2">Operation</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Virtual private cloud (VPC) connections</td>
    <td>Connect transit routers to VPCs</td>
    <td>You can connect transit routers to VPCs.</td>
  </tr>
  <tr>
    <td>Virtual border router (VBR) connections</td>
    <td>Connect transit routers to VBRs</td>
    <td>You can connect transit routers to VBRs.</td>
  </tr>
  <tr>
    <td rowspan="5">Route tables of transit routers</td>
    <td>Create or delete route tables</td>
    <td>Multiple route tables may exist on one transit router to implement traffic control of different network partitions.</td>
  </tr>
  <tr>
    <td>Associated route tables</td>
    <td>Associated route tables are used to implement routing and forwarding for the network communication between transit routers and other network instances.</td>
  </tr>
  <tr>
    <td>Route learning</td>
    <td>You can specify the network instances from which transit routers automatically learns routes.</td>
  </tr>
  <tr>
    <td>Support for static routes</td>
    <td>Route tables of transit routers can be configured with static routes.</td>
  </tr>
  <tr>
    <td>Support for routing policies</td>
    <td>The route tables of transit routers can control the sending and receiving rules of routes based on routing policies.</td>
  </tr>
</table>

Multiple multicast groups can be created on one transit

Create or delete multicast groups

router, and each multicast group has one multicast IP address.

Multicast management

You can manage multicast

Add or delete multicast sources

sources in a multicast group.

You can manage multicast

Add or remove multicast members

members in a multicast group.

Multicast sources and members

Cloud multicast

are in the cloud.

The multicast sources or

On-premises and cloud multicast

multicast members are not in

Multicast

the cloud.

One network interface card (NIC) works as

The same NIC works as both a

both a multicast source and a multicast

multicast source and a

member

multicast member.

Traffic monitoring service connected to

The traffic between transit

VPCs

routers and VPCs is monitored.

Traffic monitoring service connected to

The traffic between transit

VRBs

routers and VBRs is monitored.

Transit routers are connected to CloudMonitor to implement tenant monitoring and

Service-level monitoring of transit routers

management.

O&M and Monitoring

Transit routers are connected to TianjiMon to implement

Cluster-level monitoring of transit routers

platform monitoring and management.

Transit routers are connected to TianjiMon to implement

Region-level monitoring of transit routers

platform-side region monitoring and management.

<table>
  <tr>
    <td rowspan="4">Health checks</td>
    <td>Cloud Enterprise Network (CEN) instances</td>
    <td>You can select CEN instances on which health check is performed.</td>
  </tr>
  <tr>
    <td>VBRs</td>
    <td>You can select VBRs on which health check is performed.</td>
  </tr>
  <tr>
    <td>Detection IP addresses for health checks</td>
    <td>You can specify the source and destination IP addresses.</td>
  </tr>
  <tr>
    <td>Probe interval and probe packets</td>
    <td>You can specify the probe interval and the number of probe packets.</td>
  </tr>
  <tr>
    <td>Multiple clusters</td>
    <td>Support for multiple clusters</td>
    <td>Transit routers support multi-cluster deployment solutions.</td>
  </tr>
  <tr>
    <td>Topology display</td>
    <td>Display of resource topologies</td>
    <td>The basic information about the topologies of cloud services associated with transit routers can be displayed.</td>
  </tr>
  <tr>
    <td>Quota management</td>
    <td>Quota management for transit routers</td>
    <td>You can perform quota management on transit routers.</td>
  </tr>
  <tr>
    <td>Security Protection</td>
    <td>Shared security policies for multiple VPCs</td>
    <td>Security policies are shared among multiple VPCs.</td>
  </tr>
  <tr>
    <td>Disaster recovery</td>
    <td>Support for zone-disaster recovery</td>
    <td>Transit routers support zone-disaster recovery.</td>
  </tr>
  <tr>
    <td rowspan="2">domestic software and hardware ecology</td>
    <td>Support for Intel chip architecture</td>
    <td>Transit routers support Intel chip architecture.</td>
  </tr>
  <tr>
    <td>Support for Hygon chip architecture</td>
    <td>Transit routers support Hygon chip architecture.</td>
  </tr>
</table>
