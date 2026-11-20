Alibaba Cloud  
Apsara Stack  
TransitRouter  
Developer Guide  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.API References](#section-1)
    - [1.1. List of operations by function](#section-1-1)
    - [1.2. CEN instances](#section-1-2)
        - [1.2.1. ModifyCenAttribute](#section-1-2-1)
        - [1.2.2. DescribeCenAttachedChildInstances](#section-1-2-2)
        - [1.2.3. DescribeCenAttachedChildInstanceAttribute](#section-1-2-3)
        - [1.2.4. DeleteCen](#section-1-2-4)
        - [1.2.5. DescribeCens](#section-1-2-5)
        - [1.2.6. CreateCen](#section-1-2-6)
        - [1.2.7. DescribeChildInstanceRegions](#section-1-2-7)
    - [1.3. Transit routers](#section-1-3)
        - [1.3.1. CreateTransitRouter](#section-1-3-1)
        - [1.3.2. DeleteTransitRouter](#section-1-3-2)
        - [1.3.3. UpdateTransitRouter](#section-1-3-3)
        - [1.3.4. ListTransitRouters](#section-1-3-4)
        - [1.3.5. ListTransitRouterAvailableResource](#section-1-3-5)
    - [1.4. Transit router CIDR blocks](#section-1-4)
        - [1.4.1. CreateTransitRouterCidr](#section-1-4-1)
        - [1.4.2. ModifyTransitRouterCidr](#section-1-4-2)
        - [1.4.3. ListTransitRouterCidr](#section-1-4-3)
        - [1.4.4. ListTransitRouterCidrAllocation](#section-1-4-4)
        - [1.4.5. DeleteTransitRouterCidr](#section-1-4-5)
    - [1.5. VPC connections](#section-1-5)
        - [1.5.1. CreateTransitRouterVpcAttachment](#section-1-5-1)
        - [1.5.2. UpdateTransitRouterVpcAttachmentAttribute](#section-1-5-2)
        - [1.5.3. ListTransitRouterVpcAttachments](#section-1-5-3)
        - [1.5.4. DeleteTransitRouterVpcAttachment](#section-1-5-4)
        - [1.5.5. UpdateTransitRouterVpcAttachmentZones](#section-1-5-5)
        - [1.5.6. ListGrantVSwitchesToCen](#section-1-5-6)
    - [1.6. VBR connections](#section-1-6)
        - [1.6.1. CreateTransitRouterVbrAttachment](#section-1-6-1)
        - [1.6.2. ListTransitRouterVbrAttachments](#section-1-6-2)
        - [1.6.3. UpdateTransitRouterVbrAttachmentAttribute](#section-1-6-3)
        - [1.6.4. DeleteTransitRouterVbrAttachment](#section-1-6-4)
    - [1.7. Connect attachments](#section-1-7)
        - [1.7.1. CreateTransitRouterConnectAttachment](#section-1-7-1)
        - [1.7.2. UpdateTransitRouterConnectAttachmentAttribute](#section-1-7-2)
        - [1.7.3. ListTransitRouterConnectAttachments](#section-1-7-3)
        - [1.7.4. CreateTransitRouterConnectPeer](#section-1-7-4)
        - [1.7.5. ListTransitRouterConnectPeers](#section-1-7-5)
        - [1.7.6. DeleteTransitRouterConnectPeer](#section-1-7-6)
        - [1.7.7. DeleteTransitRouterConnectAttachment](#section-1-7-7)
    - [1.8. Cross-account authorization](#section-1-8)
        - [1.8.1. GrantInstanceToTransitRouter](#section-1-8-1)
        - [1.8.2. RevokeInstanceFromTransitRouter](#section-1-8-2)
        - [1.8.3. DescribeGrantRulesToCen](#section-1-8-3)
        - [1.8.4. DescribeGrantRulesToResource](#section-1-8-4)
    - [1.9. Custom routes](#section-1-9)
        - [1.9.1. CreateTransitRouterRouteEntry](#section-1-9-1)
        - [1.9.2. UpdateTransitRouterRouteEntry](#section-1-9-2)
        - [1.9.3. ListTransitRouterRouteEntries](#section-1-9-3)
        - [1.9.4. DeleteTransitRouterRouteEntry](#section-1-9-4)
    - [1.10. Routing](#section-1-10)
        - [1.10.1. ListCenChildInstanceRouteEntriesToAttachment](#section-1-10-1)
        - [1.10.2. DescribeRouteConflict](#section-1-10-2)
        - [1.10.3. DescribeCenRegionDomainRouteEntries](#section-1-10-3)
        - [1.10.4. DescribeCenChildInstanceRouteEntries](#section-1-10-4)
    - [1.11. Custom route tables](#section-1-11)
        - [1.11.1. UpdateTransitRouterRouteTable](#section-1-11-1)
        - [1.11.2. DeleteTransitRouterRouteTable](#section-1-11-2)
        - [1.11.3. ListTransitRouterRouteTables](#section-1-11-3)
        - [1.11.4. CreateTransitRouterRouteTable](#section-1-11-4)
    - [1.12. Route learning](#section-1-12)
        - [1.12.1. DisableTransitRouterRouteTablePropagation](#section-1-12-1)
        - [1.12.2. ListTransitRouterRouteTablePropagations](#section-1-12-2)
        - [1.12.3. EnableTransitRouterRouteTablePropagation](#section-1-12-3)
    - [1.13. Associated forwarding](#section-1-13)
        - [1.13.1. DissociateTransitRouterAttachmentFromRouteTable](#section-1-13-1)
        - [1.13.2. ListTransitRouterRouteTableAssociations](#section-1-13-2)
        - [1.13.3. AssociateTransitRouterAttachmentWithRouteTable](#section-1-13-3)
    - [1.14. Multicast](#section-1-14)
        - [1.14.1. CreateTransitRouterMulticastDomain](#section-1-14-1)
        - [1.14.2. ModifyTransitRouterMulticastDomain](#section-1-14-2)
        - [1.14.3. ListTransitRouterMulticastDomains](#section-1-14-3)
        - [1.14.4. DeleteTransitRouterMulticastDomain](#section-1-14-4)
        - [1.14.5. AssociateTransitRouterMulticastDomain](#section-1-14-5)
        - [1.14.6. DisassociateTransitRouterMulticastDomain](#section-1-14-6)
        - [1.14.7. ListTransitRouterMulticastDomainAssociations](#section-1-14-7)
        - [1.14.8. RegisterTransitRouterMulticastGroupSources](#section-1-14-8)
        - [1.14.9. DeregisterTransitRouterMulticastGroupSources](#section-1-14-9)
        - [1.14.10. RegisterTransitRouterMulticastGroupMembers](#section-1-14-10)
        - [1.14.11. DeregisterTransitRouterMulticastGroupMembers](#section-1-14-11)
        - [1.14.12. ListTransitRouterMulticastGroups](#section-1-14-12)
        - [1.14.13. ListGrantVSwitchEnis](#section-1-14-13)
        - [1.14.14. ListTransitRouterMulticastDomainVSwitches](#section-1-14-14)
    - [1.15. Routing policies](#section-1-15)
        - [1.15.1. CreateCenRouteMap](#section-1-15-1)
        - [1.15.2. ModifyCenRouteMap](#section-1-15-2)
        - [1.15.3. DescribeCenRouteMaps](#section-1-15-3)
        - [1.15.4. DeleteCenRouteMap](#section-1-15-4)
    - [1.16. Health checks](#section-1-16)
        - [1.16.1. EnableCenVbrHealthCheck](#section-1-16-1)
        - [1.16.2. DisableCenVbrHealthCheck](#section-1-16-2)
        - [1.16.3. DescribeCenVbrHealthCheck](#section-1-16-3)

<a id="section-1"></a>

# 1.API References

<a id="section-1-1"></a>

## 1.1. List of operations by function

This topic provides a list of the APIs for transit routers.

**CEN Instances**

| API operation | Description |
| --- | --- |
| CreateCen | Creates a Cloud Enterprise Network (CEN) instance. |
| ModifyCenAttribute | Modifies the name and description of a specified CEN instance. |
| DescribeCens | Queries the information about CEN instances. |
| DescribeChildInstanceRegions | Queries the regions of network instance connections on a transit router. |
| DescribeCenAttachedChildInstanceAttr ibute | Queries the details about network instances such as virtual private clouds (VPCs) and virtual border routers (VBRs) attached to a CEN instance. |
| DescribeCenAttachedChildInstances | Queries the network instances that are attached to a CEN instance. |
| DeleteCen | Deletes a CEN instance. |

**Transit routers**

| API operation | Description |
| --- | --- |
| CreateTransitRouter | Creates a transit router. |
| UpdateTransitRouter | Modifies the name and description of a transit router. |
| ListTransitRouters | Queries the information about transit routers that are connected to a CEN instance. |
| ListTransitRouterAvailableResource | Queries the zones that support transit routers in a specified region. |
| DeleteTransitRouter | Deletes a transit router. |

**Transit router CIDR blocks**

| API operation | Description |
| --- | --- |
| CreateTransitRouterCidr | Creates a CIDR block for a transit router. |
| ModifyTransitRouterCidr | Modify the CIDR block of a transit router. |
| ListTransitRouterCidr | Queries the CIDR blocks of a transit router. |
| ListTransitRouterCidrAllocation | Queries how IP addresses within the CIDR block of a transit router are allocated. |
| DeleteTransitRouterCidr | Deletes a CIDR block from a transit router. |

**VPC connections**

| API operation | Description |
| --- | --- |
| CreateTransitRouterVpcAttachment | Creates a VPC connection on a transit router. |
| UpdateTransitRouterVpcAttachmentAtt ribute | Modifies the name and description of a VPC connection on a transit router. |
| ListTransitRouterVpcAttachments | Queries VPC connections on a transit router. |
| DeleteTransitRouterVpcAttachment | Deletes a VPC connection from a transit router. |
| UpdateTransitRouterVpcAttachmentZo nes | Modifies the zones and vSwitches of a VPC connection. |
| ListGrantVSwitchesToCen | Queries the vSwitches in a VPC that belongs to another Alibaba Cloud account and is attached to a CEN instance. |

**VBR connections**

| API operation | Description |
| --- | --- |
| CreateTransitRouterVbrAttachment | Create a VBR connection on a transit router. |
| UpdateTransitRouterVbrAttachmentAtt ribute | Modifies the name and description of a VBR connection that is created on a transit router. |
| ListTransitRouterVbrAttachments | Queries the information about VBR connection on a transit router. |
| DeleteTransitRouterVbrAttachment | Deletes a VBR connection from a transit router. |

**Connect attachments**

| API operation | Description |
| --- | --- |
| CreateTransitRouterConnectAttachme nt | Creates a Connect attachment. |
| UpdateTransitRouterConnectAttachme ntAttribute | Modifies the configurations of a Connect attachment. |
| ListTransitRouterConnectAttachments | Queries the information about a Connect attachment. |
| CreateTransitRouterConnectPeer | Adds a Connect peer. |
| ListTransitRouterConnectPeers | Queries the information about a Connect peer. |
| DeleteTransitRouterConnectPeer | Deletes a Connect peer. |
| DeleteTransitRouterConnectAttachme nt | Deletes a Connect attachment. |

**Cross-account authorization**

| API operation | Description |
| --- | --- |
| DescribeGrantRulesToCen | Queries the network instances within a different Alibaba Cloud account that CEN has the permissions to access. |
| DescribeGrantRulesToResource | Queries permissions granted to Cloud Enterprise Network (CEN) instances that belong to another Alibaba Cloud account. |
| RevokeInstanceFromTransitRouter | Revokes the permissions that a transit router uses to connect to network instances that belong to another Alibaba Cloud account. |
| GrantInstanceToTransitRouter | Grants a transit router the permissions to connect to a network instance that belongs to another Alibaba Cloud account. |

**Custom routes**

| API operation | Description |
| --- | --- |
| CreateTransitRouterRouteEntry | Adds a route to a route table of a transit router. |
| UpdateTransitRouterRouteEntry | Modifies the name and description of a route in a route table of a transit router. |
| DeleteTransitRouterRouteEntry | Deletes a static route from a route table of a transit router. |
| ListTransitRouterRouteEntries | Queries the information about routes in a route table of a transit router. |

**Routes**

| API operation | Description |
| --- | --- |
| ListCenChildInstanceRouteEntriesToAtt achment | Queries routes in route tables of network instances that point to network instance connections. |
| DescribeRouteConflict | Queries overlapping routes of a network instance. |
| DescribeCenRegionDomainRouteEntrie s | Queries the routes of a CEN instance. |
| DescribeCenChildInstanceRouteEntries | Queries the routes of a network instance that is attached to a CEN instance. |

**Custom route tables**

| API operation | Description |
| --- | --- |
| CreateTransitRouterRouteTable | Creates a custom route table for a transit router. |
| UpdateTransitRouterRouteTable | Modifies the name and description of a route table that belongs to a transit router. |
| ListTransitRouterRouteTables | Queries the route tables of a transit router. |
| DeleteTransitRouterRouteTable | Deletes a custom route table from a transit router. |

**Route learning**

| API operation | Description |
| --- | --- |
| EnableTransitRouterRouteTablePropag ation | Creates a route learning correlation. |
| DisableTransitRouterRouteTablePropa gation | Deletes a route learning correlation. |
| ListTransitRouterRouteTablePropagatio ns | Queries the route learning correlations of a route table that belongs to a transit router. |

**Associated forwarding**

| API operation | Description |
| --- | --- |
| AssociateTransitRouterAttachmentWit hRouteTable | Creates an associated forwarding correlation. |
| DissociateTransitRouterAttachmentFro mRouteTable | Deletes an associated forwarding correlation. |
| ListTransitRouterRouteTableAssociatio ns | Queries the associated forwarding correlations that are created for a route table of a transit router or a network instance connection. |

**Multicast**

| API operation | Description |
| --- | --- |
| CreateTransitRouterMulticastDomain | Creates a multicast domain. |
| ModifyTransitRouterMulticastDomain | Modifies the name and description of a multicast domain. |
| ListTransitRouterMulticastDomains | Queries the information about multicast domains. |
| DeleteTransitRouterMulticastDomain | Deletes a multicast domain. |
| AssociateTransitRouterMulticastDomai n | Associates a vSwitch in a VPC to a multicast domain. |
| DisassociateTransitRouterMulticastDo main | Disassociates vSwitches from a multicast domain. |
| ListTransitRouterMulticastDomainAsso ciations | Queries whether vSwitches in VPCs are associated with a multicast domain |
| RegisterTransitRouterMulticastGroupS ources | Creates a multicast source. |
| DeregisterTransitRouterMulticastGroup Sources | Deletes multicast sources. |
| RegisterTransitRouterMulticastGroupM embers | Adds multicast members to a multicast group. |
| DeregisterTransitRouterMulticastGroup Members | Removes multicast members from a multicast group. |
| ListTransitRouterMulticastGroups | Queries the multicast sources and members in a multicast domain. |
| ListGrantVSwitchEnis | Queries the elastic network interfaces (ENIs) that can be used as multicast sources or members in a VPC. |
| ListTransitRouterMulticastDomainVSwi tches | Queries VPC vSwitches that are associated with multicast domains. |

**Routing policies**

| API operation | Description |
| --- | --- |
| CreateCenRouteMap | Creates a routing policy. |
| ModifyCenRouteMap | Modifies a routing policy of a CEN instance. |
| DescribeCenRouteMaps | Queries information about routing policies. |
| DeleteCenRouteMap | Deletes a routing policy. |

**Health checks**

| API operation | Description |
| --- | --- |
| EnableCenVbrHealthCheck | Enables the health check feature for a VBR to detect anomalies on Express Connect circuits. You can modify the health check configuration of a VBR based on business requirements. |
| DescribeCenVbrHealthCheck | Queries the health check configuration of a VBR in a region. |
| DisableCenVbrHealthCheck | Disables the health check feature for a VBR. |

<a id="section-1-2"></a>

## 1.2. CEN instances

<a id="section-1-2-1"></a>

### 1.2.1. ModifyCenAttribute

Modifies the name and description of a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| CenId | String | Query | Yes | cen-7qthudw0ll6jmc\*\*\*\* | The ID of the CEN instance. |

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Name | String | Query | No | test | The name of the CEN instance.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>. |
| Description | String | Query | No | cen | The description of the CEN instance.<br>The description must be 2 to 256 characters in length.It must start with a letter or Chinese character and cannot start with <code> http:// </code> or <code> https:// </code>. |
| ProtectionL evel | String | Query | No | REDUCED | The level of CIDR block overlapping.<br>Set the value to REDUCED (default). This value specifies that CIDR blocks can overlap but cannot be the same. |
| Action | String | Query | No | ModifyCenAttribute | The operation that you want to perform. Set the value to ModifyCenAttribute. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 13526224-5780-4426-8BDF-BC8B08700F22 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyCenAttribute
&CenId=cen-7qthudw0ll6jmc****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"13526224-5780-4426-8BDF-BC8B08700F22"
}
```

`XML`  format

```xml
<RequestId>13526224-5780-4426-8BDF-BC8B08700F22</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_ENHANCE_PROTECTIO N_LEVEL | InvalidOperation.EnhanceProtectio nLevel | Your request to enhance CBN protection level cannot be processed. Please contact customer support to continue this operation. |

<a id="section-1-2-2"></a>

### 1.2.2. DescribeCenAttachedChildInstances

Queries the network instances that are attached to a Cloud Enterprise Network (CEN) instance.

**Usage notes**

You can use one of the following methods to query the information about the network instances that are attached to a CEN instance:

- You can query all the network instances that are attached to a CEN instance by setting the **CenId** parameter.

- You can query the network instances that are attached to a CEN instance in a specified region by setting the **CenId** and **ChildInstanceRegionId** parameters.

- You can query a specified type of network instances that are attached to a CEN instance by setting the **CenId** and **ChildInstanceType** parameters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenAttachedChildIns tances | The operation that you want to perform. The operation that you want to perform. Set the value to DescribeCenAttachedChild <strong>Instances</strong>. |
| PageNumber | Integ er | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: <strong>10</strong>. Valid values: <strong>1</strong> to <strong>50</strong>. |
| CenId | String | Query | Yes | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| ChildInstanc eType | String | Query | No | VPC | The type of network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| ChildInstanc eRegionId | String | Query | No | cn-qingdao-env66-d01 | The region ID of the network instance.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ChildInstances | Array |  | The information about the network instances. |
| -CenId | String | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| -ChildInstanceId | String | vpc-8vb1lu55yt9rlwgxl\*\*\* \* | The ID of the network instance. |
| -ChildInstanceTyp e | String | VPC | The type of network instance. Valid values:<br>• VPC<br>• VBR |
| -ChildInstanceRe gionId | String | cn-qingdao-env66-d01 | The region ID of the network instance. |
| -ChildInstanceOw nerId | Long | 1688000000000000 | The UID of the level-1 organization to which the network instance belongs. |
| -Status | String | Attached | The status of the network instance. Valid values:<br>• <strong>Attaching</strong>: The network instance is being attached to the CEN instance.<br>• <strong>Attached</strong>: The network instance is attached to the CEN instance.<br>• <strong>Detaching</strong>: The network instance is being detached from the CEN instance. |
| -ChildInstanceAtt achTime | String | 2021-08-10T06:27Z | The time when the network instance was attached to the CEN instance.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC). |
| RequestId | String | B2063B16-852B-5B66-B73D-4ED4D1A5E5C2 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenAttachedChildInstances
&CenId=cen-j3jzhw1zpau2km****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"B2063B16-852B-5B66-B73D-4ED4D1A5E5C2",
 "PageNumber":1,
 "ChildInstances":{
  "Status":"Attached",
  "ChildInstanceType":"VPC",
  "CenId":"cen-j3jzhw1zpau2km****",
  "ChildInstanceAttachTime":"2021-08-10T06:27Z",
  "ChildInstanceOwnerId":1688000000000000,
  "ChildInstanceId":"vpc-8vb1lu55yt9rlwgxl****",
  "ChildInstanceRegionId":"cn-qingdao-env66-d01"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<PageSize>10</PageSize>
<RequestId>B2063B16-852B-5B66-B73D-4ED4D1A5E5C2</RequestId>
<PageNumber>1</PageNumber>
<ChildInstances>
 <Status>Attached</Status>
 <ChildInstanceType>VPC</ChildInstanceType>
 <CenId>cen-j3jzhw1zpau2km****</CenId>
 <ChildInstanceAttachTime>2021-08-10T06:27Z</ChildInstanceAttachTime>
 <ChildInstanceOwnerId>1688000000000000</ChildInstanceOwnerId>
 <ChildInstanceId>vpc-8vb1lu55yt9rlwgxl****</ChildInstanceId>
 <ChildInstanceRegionId>cn-qingdao-env66-d01</ChildInstanceRegionId>
</ChildInstances>
```

<a id="section-1-2-3"></a>

### 1.2.3. DescribeCenAttachedChildInstanceAttribute

Queries the information about a network instance, such as a virtual private cloud (VPC) or a virtual border router (VBR), that is attached to a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenAttachedChildIns tanceAttribute | The operation that you want to perform. Set the value to DescribeCenAttachedChild <strong>InstanceAttribute</strong>. |
| CenId | String | Query | Yes | cen-5mv960yjhja0dh\*\*\*\* | The ID of the CEN instance. |
| ChildInstanc eId | String | Query | Yes | vpc-2zebdboka7d7t37vo\*\*\*\* | The ID of the network instance that is attached to the CEN instance. |
| ChildInstanc eType | String | Query | Yes | VPC | The type of network instance. Valid values:<br>• VPC<br>• VBR |
| ChildInstanc eRegionId | String | Query | Yes | cn-qingdao-env66-d01 | The region ID of the network instance.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | ADD98358-D265-4060-87CB-A2427F5A8944 | The request ID. |
| CenId | String | cen-5mv960yjhja0dh\*\*\*\* | The ID of the CEN instance. |
| ChildInstanceId | String | vpc-2zebdboka7d7t37vo\* \*\*\* | The network instance ID. |
| ChildInstanceTyp e | String | VPC | The type of network instance. Valid values:<br>• VPC<br>• VBR |
| ChildInstanceRe gionId | String | cn-qingdao-env66-d01 | The region ID of the network instance. |
| ChildInstanceOw nerId | Long | 1688000000000000 | The UID of the level-1 organization to which the network instance belongs. |
| Status | String | Attached | Indicates whether the network instance is attached to the CEN instance.<br>• <strong>Attaching</strong>: The network instance is being attached to the CEN instance.<br>• <strong>Attached</strong>: The network instance is attached to the CEN instance.<br>• <strong>Detaching</strong>: The network instance is being detached from the CEN instance. |
| ChildInstanceNa me | String | defaultvpc | The name of the network instance. |
| ChildInstanceAtt achTime | String | 2018-07-30T07:53Z | The time when the network instance was attached to the CEN instance.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC). |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenAttachedChildInstanceAttribute
&CenId=cen-5mv960yjhja0dh****
&ChildInstanceId=vpc-2zebdboka7d7t37vo****
&ChildInstanceType=VPC
&ChildInstanceRegionId=cn-qingdao-env66-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "Status":"Attached",
 "ChildInstanceType":"VPC",
 "RequestId":"ADD98358-D265-4060-87CB-A2427F5A8944",
 "CenId":"cen-5mv960yjhja0dh****",
 "ChildInstanceAttachTime":"2018-07-30T07:53Z",
 "ChildInstanceOwnerId":1688000000000000,
 "ChildInstanceName":"defaultvpc",
 "ChildInstanceId":"vpc-2zebdboka7d7t37vo****",
 "ChildInstanceRegionId":"cn-qingdao-env66-d01"
}
```

`XML`  format

```xml
<Status>Attached</Status>
<ChildInstanceType>VPC</ChildInstanceType>
<RequestId>ADD98358-D265-4060-87CB-A2427F5A8944</RequestId>
<CenId>cen-5mv960yjhja0dh****</CenId>
<ChildInstanceAttachTime>2018-07-30T07:53Z</ChildInstanceAttachTime>
<ChildInstanceOwnerId>1688000000000000</ChildInstanceOwnerId>
<ChildInstanceName>defaultvpc</ChildInstanceName>
<ChildInstanceId>vpc-2zebdboka7d7t37vo****</ChildInstanceId>
<ChildInstanceRegionId>cn-qingdao-env66-d01</ChildInstanceRegionId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | INSTANCE_NOT_EXIST | ParameterError | The parameter is error. |
| 400 |  | SystemBusy | The system is busy. Please try again later. |

<a id="section-1-2-4"></a>

### 1.2.4. DeleteCen

Deletes a Cloud Enterprise Network (CEN) instance.

**Usage notes**

Before you delete a CEN instance, make sure that the following resources are not attached to the CEN instance:

- No network instance connections are created on the transit router. To delete network instance connections, you can call the DeleteTransitRouterVpcAttachmen, DeleteTransitRouterVbrAttachment, and DeleteTransitRouterConnectAttachment operations.

- The transit router does not contain custom route tables. To delete custom route tables, call the DeleteTransitRouterRouteTable operation.

- The default route table of the transit router does not contain custom route entries. To delete custom route entries, call the DeleteTransitRouterRouteEntry operation.

- The transit router is not associated with a multicast domain. To disassociate a transit router from a multicast domain, call the DeleteTransitRouterMulticastDomain operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| CenId | String | Query | Yes | cen-7qthudw0ll6jmc\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| Action | String | Query | No | DeleteCen | The operation that you want to perform. Set the value to <strong>DeleteCen</strong>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 5903EE99-D542-4E14-BC65-AAC1CB2D3D03 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteCen
&CenId=cen-7qthudw0ll6jmc****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"5903EE99-D542-4E14-BC65-AAC1CB2D3D03"
}
```

`XML`  format

```xml
<RequestId>5903EE99-D542-4E14-BC65-AAC1CB2D3D03</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationFailed.Delet eCenWithCustomRout eTable | OperationFailed.DeleteCenWithCus tomRouteTable | Operation failed because you are not allowed to delete the CEN with the custom transit router route table. |
| 400 | OperationFailed.Delet eCenWithRouteEntry | OperationFailed.DeleteCenWithRou teEntry | Operation failed because you are not allowed to delete the CEN with the transit router route entry. |

<a id="section-1-2-5"></a>

### 1.2.5. DescribeCens

Queries the information about a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| PageNumber | Integ er | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page. Valid values: <strong>1</strong> to <strong>50</strong>. Default value: <strong>10</strong>. |
| Filter | Repea tList | Query | No |  | The filter conditions.<br>You can specify at most five filter conditions in each call. |
| -Key | String |  | No | CenId | The filter key. Valid values:<br>• <strong>CenId</strong>: the ID of a CEN instance.<br>• <strong>Name</strong>: the name of a CEN instance.<br>By default, the logical operator among filter conditions is <strong>AND</strong>.Information about a CEN instance is returned only if the CEN instance matches all filter conditions.<br>You can specify at most five filter conditions in each request. |

<table>
  <tr>
    <td>-Value</td>
    <td>Repea tList</td>
    <td></td>
    <td>No</td>
    <td>cen-0xyeagctz5sfg9****</td>
    <td>The value of the filter condition.<br>This parameter sets the value of a filter <strong>key</strong>. You can specify multiple values for a filter <strong>key</strong>. The logical operator among multiple filter values is <strong>OR</strong>. If a CEN instance matches one or more of the values that you specify, the CEN instance matches the filter condition.<br>You can specify at most five values in each filter condition.</td>
  </tr>
  <tr>
    <td>Tag</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td></td>
    <td>The information about the tag.<br>You can specify up to 20 tags in each call.</td>
  </tr>
  <tr>
    <td>-Key</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>tagtest</td>
    <td>The tag keys.<br>The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>.It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys.</td>
  </tr>
  <tr>
    <td>-Value</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>tagtest</td>
    <td>The tag values.<br>The tag values can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call.</td>
  </tr>
  <tr>
    <td>Action</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>DescribeCens</td>
    <td>The operation that you want to perform. Set the value to <strong>DescribeCens</strong>.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 2BFA6822-240E-4E27-B4C8-AA400EF7474D | The request ID. |
| PageNumber | Integer | 1 | The number of the page returned. |
| Cens | Array |  | The information about the CEN instance. |
| -Tags | Array |  | The IDs of the tags that are added to the CEN instance. |
| --Key | String | tagkey | The label key. |
| --Value | String | tagvalue | The tag value. |
| -Status | String | Active | The status of the CEN instance.<br>• <strong>Creating</strong>: The CEN instance is being created.<br>• <strong>Active</strong>: The CEN instance is running.<br>• <strong>Deleting</strong>: The CEN instance is being deleted. |
| -CreationTime | String | 2019-10-22T07:44Z | The time when the CEN instance was created.<br>The time follows the ISO8601 standard in the <code> YYYY-MM-DDThh:mmZ </code> format. The time is displayed in UTC. |
| -Ipv6Level | String | DISABLED | Indicates whether IPv6 is enabled for the CEN instance. Valid values:<br>• ENABLE<br>• DISABLED |
| -Description | String | desctest | The description of the CEN instance. |
| -CenId | String | cen-0xyeagctz5sfg9\*\*\*\* | The ID of the CEN instance. |
| -ProtectionLevel | String | REDUCED | The level of CIDR block overlapping.<br><strong>REDUCED</strong>: Overlapped CIDR blocks are allowed. This value specifies that CIDR blocks can overlap but CIDR blocks cannot be duplicates. |
| -Name | String | nametest | The name of the CEN instance. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCens
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"2BFA6822-240E-4E27-B4C8-AA400EF7474D",
 "PageNumber":1,
 "Cens":{
  "Status":"Active",
  "ProtectionLevel":"REDUCED",
  "Description":"desctest",
  "-Tags":{
   "Value":"tagvalue",
   "Key":"tagkey"
  },
  "Ipv6Level":"DISABLED",
  "CreationTime":"2019-10-22T07:44Z",
  "CenId":"cen-0xyeagctz5sfg9****",
  "Name":"nametest"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<PageSize>10</PageSize>
<RequestId>2BFA6822-240E-4E27-B4C8-AA400EF7474D</RequestId>
<PageNumber>1</PageNumber>
<Cens>
 <Status>Active</Status>
 <ProtectionLevel>REDUCED</ProtectionLevel>
 <Description>desctest</Description>
 <-Tags>
  <Value>tagvalue</Value>
  <Key>tagkey</Key>
 </-Tags>
 <Ipv6Level>DISABLED</Ipv6Level>
 <CreationTime>2019-10-22T07:44Z</CreationTime>
 <CenId>cen-0xyeagctz5sfg9****</CenId>
 <Name>nametest</Name>
</Cens>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_TAG_KEY | InvalidTagKey | The tag keys are not valid. |
| 400 | INVALID_TAG_VALUE | InvalidTagValue | The tag values are not valid. |

<a id="section-1-2-6"></a>

### 1.2.6. CreateCen

Creates a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| Name | String | Query | No | testname | The name of the CEN instance.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>. |
| Description | String | Query | No | testdesc | The description of the CEN instance.<br>The description must be 2 to 256 characters in length. It must start with a letter and cannot start with <code> http:// </code>or <code> https:// </code>. |
| ProtectionLe vel | String | Query | No | REDUCED | The level of CIDR block overlapping.<br>Set the value to <strong>REDUCED</strong> (default). This value specifies that CIDR blocks can overlap but cannot be the same. |
| Tag | Repea tList | Query | No |  | The information about the tag.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | tagtest | The tag keys.<br>The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>.It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |
| -Value | String |  | No | tagtest | The tag values.<br>The tag values can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call. |
| Action | String | Query | Yes | CreateCen | The operation that you want to perform. Set the value to <strong>CreateCen</strong>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50 | The request ID. |
| CenId | String | cen-dc4vwznpwbobrl\*\*\*\* | The ID of the CEN instance. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateCen
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50",
 "CenId":"cen-dc4vwznpwbobrl****"
}
```

`XML`  format

```xml
<RequestId>0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50</RequestId>
<CenId>cen-dc4vwznpwbobrl****</CenId>
```

<a id="section-1-2-7"></a>

### 1.2.7. DescribeChildInstanceRegions

Queries the regions of network instances connected to a transit routers.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ProductType | String | Query | No | VPC | The type of the network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| Action | String | Query | No | DescribeChildInstanceRegion s | The operation that you want to perform. The operation that you want to perform. Set the value to DescribeChildInstanceReg <strong>ions</strong>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | D5CEED59-36AA-47CC-9D81-16F71C46BD80 | The request ID. |
| Regions | Array |  | The regions. |
| -RegionId | String | cn-qingdao-env17e-d01 | The region ID. |
| -LocalName | String | cn-qingdao-env17e-d01 | The region name. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeChildInstanceRegions
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"D5CEED59-36AA-47CC-9D81-16F71C46BD80",
 "Regions":{
  "RegionId":"cn-qingdao-env17e-d01",
  "LocalName":"cn-qingdao-env17e-d01"
 }
}
```

`XML`  format

```xml
<RequestId>D5CEED59-36AA-47CC-9D81-16F71C46BD80</RequestId>
<Regions>
 <RegionId>cn-qingdao-env17e-d01</RegionId>
 <LocalName>cn-qingdao-env17e-d01</LocalName>
</Regions>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | Abs.MissingOwnerIdOr OwnerAccount | MissingParameter.OwnerIdOrOwne rAccount | The input parameter OwnerAccount or OwnerId that is mandatory for processing this request is not supplied |

<a id="section-1-3"></a>

## 1.3. Transit routers

<a id="section-1-3-1"></a>

### 1.3.1. CreateTransitRouter

Creates a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouter | The operation that you want to perform. Set the value to CreateTransitRouter. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| CenId | String | Query | Yes | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| RegionId | String | Query | Yes | cn-qingdao-env66-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| TransitRout erName | String | Query | No | testname | The name of the transit router.<br>The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| TransitRout erDescriptio n | String | Query | No | testdesc | The description of the transit router.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned. |
| SupportMult icast | Boolea n | Query | No | false | Specifies whether to enable the multicast feature for the transit router. Valid values:<br>• false (default): disables multicast.<br>• true: enables multicast. |
| Tag | Repeat List | Query | No |  | The tags.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | tagtest | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify at most 20 tag keys. |
| -Value | String |  | No | TagValue | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify at most 20 tag values in each call. |
| TransitRout erCidrList | Repeat List | Query | No |  | The CIDR blocks of the transit router.<br>You can specify at most five CIDR blocks in each call. |
| -Cidr | String |  | No | 192.168.10.0/24 | The CIDR block of the transit router. |
| -Name | String |  | No | nametest | The name of the transit router CIDR block.<br>The name must be 1 to 128 characters in length. |
| -Description | String |  | No | desctest | The description of the transit router CIDR block.<br>The description must be 1 to 256 characters in length. |
| -PublishCidr Route | Boolea n |  | No | true | Specifies whether to allow the system to automatically add a route that points to the CIDR block to the route table of the transit router.<br>• true (default): yes<br>• false: no |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterId | String | tr-uf6llz2286805i44g\*\*\* \* | The ID of the transit router. |
| RequestId | String | 404DA7EC-F495-44B5-B543-6EDCDF90F3D1 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouter
&CenId=cen-j3jzhw1zpau2km****
&RegionId=cn-qingdao-env66-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"404DA7EC-F495-44B5-B543-6EDCDF90F3D1",
 "TransitRouterId":"tr-uf6llz2286805i44g****"
}
```

`XML`  format

```xml
<RequestId>404DA7EC-F495-44B5-B543-6EDCDF90F3D1</RequestId>
<TransitRouterId>tr-uf6llz2286805i44g****</TransitRouterId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationUnsupporte d.RegionId | OperationUnsupported.RegionId | The specified Region is not supported. |
| 400 | InstanceExist.TransitR outerInstance | InstanceExist.TransitRouterInstanc e | The instance already exists. |
| 400 | USER_NOT_OPEN_TR_SERVICE | Forbbiden.TransitRouterServiceNot Open | The user has not open transit router service. |
| 400 | OperationUnsupporte d.SupportMulticast | OperationUnsupported.SupportMul ticast | The multicast is not supported in the specified region. |
| 400 | PARAMETER_ILLEGAL_TRANSITROUTER_REGI ONID | OperationUnsupported.RegionId | The specified Region is not supported. |
| 400 | CEN_FULL_LEVEL_NOT _SUPPORT_TR | OperationUnsupported.CenFullLev el | CEN full level does not support TransitRouter. |
| 400 | IllegalParam.Cidr | IllegalParam.Cidr | Cidr is illegal. |
| 400 | Illegal.TrType | Illegal.TrType | The TransitRouter type is illegal. |
| 400 | OperationUnsupporte d.TransitRouterCidrLis t | OperationUnsupported.TransitRout erCidrList | The TransitRouterCidrList is not support in the specified Region. |
| 400 | CIDR_CONFLICT | OperationFailed.CidrConflict | Operation is invalid because the cidr conflict. |
| 400 | IllegalParam.RegionId | IllegalParam.Region | The specified region is invalid. |

<a id="section-1-3-2"></a>

### 1.3.2. DeleteTransitRouter

Deletes a transit router.

**Usage notes**

You can delete transit routers that you no longer use. To delete a transit router, make sure that the following requirements are met:

- No network instance connections are created on the transit router. For more information, see DeleteTransitRouterVpcAttachment, DeleteTransitRouterConnectAttachment, and DeleteTransitRouterVbrAttachment.

- The transit router does not contain custom route tables. For more information, see DeleteTransitRouterRouteTable.

- The default route table of the transit router does not contain custom routes. For more information, see DeleteTransitRouterRouteEntry.

- The transit router is not associated with a multicast domain. For more information, see DeleteTransitRouterMulticastDomain.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouter | The operation that you want to perform. Set the value to DeleteTransitRouter. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and performs the request.<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned. |
| TransitRout erId | String | Query | Yes | tr-uf654ttymmljlvh2x\*\*\*\* | The ID of the transit router. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6DE3EE92-39C8-4BBD-A3AD-F568D74741BB | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouter
&TransitRouterId=tr-uf654ttymmljlvh2x****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"6DE3EE92-39C8-4BBD-A3AD-F568D74741BB"
}
```

`XML`  format

```xml
<RequestId>6DE3EE92-39C8-4BBD-A3AD-F568D74741BB</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationFailed.Delet eTransitRouter | OperationFailed.DeleteTransitRout er | Operation failed because TransitRouterRouteEntry exists |
| 400 | OperationFailed.Delet eTransitRouter | OperationFailed.DeleteTransitRout er | Operation failed because TransitRouterRouteTable exists |
| 400 | IncorrectStatus.Transi tRouterInstance | IncorrectStatus.TransitRouterInsta nce | The status of TransitRouter is incorrect. |
| 400 | INVALID_OPERATION_CCN_ATTACHED | OperationFailed.CCNAttached | Can not delete transit router because CCN still attached. |
| 400 | INVALID_OPERATION_BANDWIDTH_LIMIT_EX IST | OperationFailed.BandwidthLimitExi st | Operation is invalid because a bandwidth limit exist. |

<a id="section-1-3-3"></a>

### 1.3.3. UpdateTransitRouter

Modifies the name and description of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | UpdateTransitRouter | The operation that you want to perform. Set the value to UpdateTransitRouter. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the system returns the ID of the request. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeRegions operation to query the most recent region list. |
| TransitRout erId | String | Query | Yes | tr-uf654ttymmljlvh2x\*\*\*\* | The ID of the transit router. |
| TransitRout erName | String | Query | No | testname | The name of the transit router.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| TransitRout erDescriptio n | String | Query | No | testdesc | The description of the transit router.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | E9963DD7-998B-4F92-892D-8293CB49EE81 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouter
&RegionId=cn-qingdao-env17e-d01
&TransitRouterId=tr-uf654ttymmljlvh2x****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"E9963DD7-998B-4F92-892D-8293CB49EE81"
}
```

`XML`  format

```xml
<RequestId>E9963DD7-998B-4F92-892D-8293CB49EE81</RequestId>
```

**Error code**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationUnsupporte d.RegionId | OperationUnsupported.RegionId | The specified region ID is not supported. |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouterInsta nce | The status of TransitRouter is incorrect. |

<a id="section-1-3-4"></a>

### 1.3.4. ListTransitRouters

Queries the information about transit routers that are connected to a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouters | The operation that you want to perform. Set the value to ListTransitRouters. |
| PageNumbe r | Integer | Query | No | 1 | The page number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integer | Query | No | 10 | The number of entries per page. Valid values: <strong>1</strong> to 50. Default value: <strong>10</strong>. |
| CenId | String | Query | No | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| TransitRout erId | String | Query | No | tr-uf654ttymmljlvh2x\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | No | cn-qingdao-env66-d01 | The region ID of the transit router.<br>You can call the DescribeRegions operation to query the most recent region list. |
| Tag | Repeat List | Query | No |  | The tags.<br>You can specify at most 20 tags in each call. |
| -Key | String |  | No | TagKey | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify at most 20 tag keys in each call. |
| -Value | String |  | No | TagValue | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify at most 20 tag values in each call. |
| FeatureFilte r | Repeat List | Query | No |  | The field that is used to enable or disable a feature of the transit router. |
| -Key | String |  | No | Multicast | The value of the field that is used to enable or disable a feature of the transit router.Only the <strong>Multicast</strong> field is supported, which specifies the multicast feature. |
| -Value | Repeat List |  | No | Enabled | The field values. The Multicast field supports only one value. Valid values:<br>• Enabled: enables multicast.<br>• Disabled: disables multicast. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouters | Array |  | The list of transit routers. |
| -TransitRouterCid rList | Array |  | The CIDR blocks of the transit routers. |
| --Cidr | String | 192.168.1.0/24 | The CIDR block of the transit router. |
| --Name | String | CIDRname | The name of the transit router CIDR block. |
| --Description | String | CIDRdesc | The description of the transit router CIDR block. |
| --TransitRouterCid rId | String | cidr-46p5ceg21e8152\*\*\*\* | The ID of the transit router CIDR block. |
| --PublishCidrRoute | Boolean | true | Indicates whether the system is allowed to automatically add routes that point to the CIDR block to the route table of the transit router.<br>• true: yes<br>• false: no |
| -Tags | Array |  | The tags. |
| --Key | String | TagKey | The tag key. |
| --Value | String | TagValue | The tag value. |
| -CreationTime | String | 2021-03-15T09:39Z | The time when the transit router was created.<br>The time follows the ISO8601 standard in the <code> YYYY-MM-DDThh:mmZ </code> format. The time is displayed in UTC. |
| -Type | String | Enterprise | The edition of the transit router. Valid values:<br>Only the <strong>Enterprise</strong> value is returned, which indicates the enterprise edition. |
| -Status | String | Active | The status of the transit router. Valid values:<br>• Creating: The transit router is being created.<br>• Active: The transit router is available.<br>• Modifying: The transit router is being modified.<br>• Deleting: The transit router is being deleted.<br>• Upgrading: The transit router is being upgraded. |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl\*\*\* \* | The ID of the transit router. |
| -TransitRouterDe scription | String | testdesc | The description of the transit router. |
| -TransitRouterNa me | String | testname | The name of the transit router. |
| -CenId | String | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| -AliUid | Long | 1210123456123456 | The UID of the level-1 organization to which the CEN instance belongs. |
| -RegionId | String | cn-qingdao-env66-d01 | The region ID of the transit router. |
| -SupportMulticast | Boolean | false | Indicates whether multicast is enabled for the transit router. Valid values:<br>• true: enabled<br>• false: disabled |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 68521297-5FA6-46CB-B4EB-658F1C68C8CC | The request ID. |
| PageNumber | Integer | 1 | The number of the returned page. |
| TotalCount | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouters
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"68521297-5FA6-46CB-B4EB-658F1C68C8CC",
 "PageNumber":1,
 "TransitRouters":{
  "Status":"Active",
  "Type":"Enterprise",
  "SupportMulticast":false,
  "-Tags":{
   "Value":"TagValue",
   "Key":"TagKey"
  },
  "CreationTime":"2021-03-15T09:39Z",
  "CenId":"cen-j3jzhw1zpau2km****",
  "TransitRouterDescription":"testdesc",
  "TransitRouterName":"testname",
  "RegionId":"cn-qingdao-env66-d01",
  "-TransitRouterCidrList":{
   "Description":"CIDRdesc",
   "Cidr":"192.168.1.0/24",
   "TransitRouterCidrId":"cidr-46p5ceg21e8152****",
   "PublishCidrRoute":true,
   "Name":"CIDRname"
  },
  "TransitRouterId":"tr-bp1su1ytdxtataupl****",
  "AliUid":1210123456123456
 }
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_PARAMETER_COMBINATION_TRASN IT_ROUTER | InvalidParameterCombination.Tran sitRouter | Region ID is required if no TransitRouterId or CenId specified. |
| 400 | FILTER_VALUE_NOT_S UPPORT | InvalidOperation.UnsupportFilterVa lue | The specified FeatureFilter Value is not supported by this operation. |
| 400 | InvalidParameter.Feat ureFilter | InvalidOperation.UnsupportFilter | The specified FeatureFilter is not supported by this operation. |

<a id="section-1-3-5"></a>

### 1.3.5. ListTransitRouterAvailableResource

Queries the zones that support transit routers in a region.

**Usage notes**

You can call the ListTransitRouterAvailableResource operation to query the zones that support transit routers in a region.

- If you do not set **SupportMulticast**

  to **true**

  , general-purpose zones that support transit routers

  are queried.

- If you set **SupportMulticast**

  to **true**

  , zones in which transit routers support multicast are queried.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterAvailableR esource | The operation that you want to perform. Set the value to ListTransitRouterAvailab leResource. |
| RegionId | String | Query | No | cn-qingdao-env66-d01 | The ID of the region where the transit router is deployed.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| SupportMult icast | Boolea n | Query | No | false | Specifies whether to query only the zones in which the multicast feature is supported. Valid values:<br>• true: yes<br>After you call ListTransitRouterAvail ableResource, if no zone is returned, it indicates that the transit router does not support the multicast feature.<br>• false:: no |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| SlaveZones | String | cn-qingdao-env17e-amtest17001-a | A list of secondary zone IDs. |
| MasterZones | String | cn-qingdao-env17e-amtest17001-a | A list of primary zone IDs. |
| AvailableZones | String | cn-qingdao-env17e-amtest17001-a | A list of zone IDs. |
| RequestId | String | B4F480E0-4E76-5E43-9966-8322C28A158A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterAvailableResource
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"B4F480E0-4E76-5E43-9966-8322C28A158A",
 "AvailableZones":"cn-qingdao-env17e-amtest17001-a"
}
```

`XML`  format

```xml
<SlaveZones>cn-qingdao-env17e-amtest17001-a</SlaveZones>
<RequestId>B4F480E0-4E76-5E43-9966-8322C28A158A</RequestId>
<MasterZones>cn-qingdao-env17e-amtest17001-a</MasterZones>
<AvailableZones>cn-qingdao-env17e-amtest17001-a</AvailableZones>
```

<a id="section-1-4"></a>

## 1.4. Transit router CIDR blocks

<a id="section-1-4-1"></a>

### 1.4.1. CreateTransitRouterCidr

Creates a transit router CIDR block.

**Usage notes**

Custom CIDR blocks for transit routers are supported. The CIDR block of a transit router is similar to the CIDR block of the loopback interface of a router. IP addresses within the CIDR blocks can be allocated to Connect peers. For more information, see **Instance management** > **Transit router CIDR blocks** in Transit Router User Guide.

The CreateTransitRouterCidr operation can be used to create a CIDR block only after you create a transit router.

The CIDR block must meet the following requirements:

- Each transit router supports at most five CIDR blocks.

- The subnet mask of the CIDR block of a transit router must be 16 bits to 24 bits in length.

- You cannot specify 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, 169.254.0.0/16, or their subnets as the CIDR blocks of transit routers.

- The CIDR blocks of each transit router cannot overlap with the CIDR blocks of the network instances that need to communicate with each other by using the Cloud Enterprise Network (CEN) instance. The CIDR block of each transit router on the same CEN instance must be unique.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterCidr | The operation that you want to perform. Set the value to <strong>CreateTransitRouterCidr</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <em>request ID as the client</em> <em>token. The request ID</em> <em>may be different for</em> <em>each request.</em> |
| TransitRoute rId | String | Query | Yes | tr-p0w3x8c9em72a40nw\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| Name | String | Query | No | nametest | The name of the transit router CIDR block.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter but cannot start with <code> http:// </code>or <code> https:// </code>. |
| Description | String | Query | No | desctest | The description of the transit router CIDR block.<br>The description must be 2 to 256 characters in length. It must start with a letter but cannot start with <code> http:// </code>or <code> https:// </code>. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |
| Cidr | String | Query | Yes | 192.168.10.0/24 | The CIDR block of the transit router. |
| PublishCidrR oute | Boole an | Query | No | true | Specifies whether to allow the system to automatically add a route that points to the CIDR block to the route table of the transit router.<br>• <strong>true</strong> (default): yes<br>• <strong>false</strong>: no. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterCid rId | String | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block. |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterCidr
&TransitRouterId=tr-p0w3x8c9em72a40nw****
&RegionId=cn-qingdao-env17e-d01
&Cidr=192.168.10.0/24
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A",
 "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****"
}
```

`XML`  format

```xml
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
<TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OverLappingExist.Cidr | OverLappingExist.Cidr | The cidr overlapping exist. |
| 400 | OperationUnsupporte d.TransitRouterCidr | OperationUnsupported.TransitRout erCidr | Transit region does not support the operation. |
| 400 | IllegalParam.Cidr | IllegalParam.Cidr | The specified cidr is invalid. |

<a id="section-1-4-2"></a>

### 1.4.2. ModifyTransitRouterCidr

Modifies the CIDR block of a transit router.

**Usage notes**

- Before you modify the CIDR block of a transit router, we recommend that you read the limits on transit router CIDR blocks. For more information, refer to Instance management > Transit router CIDR blocks in Transit Router User Guide.

- If IP addresses within the CIDR block have been allocated to network instances, you cannot modify the CIDR block.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ModifyTransitRouterCidr | The operation that you want to perform. Set the value to ModifyTransitRouterCid r. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| TransitRout erId | String | Query | Yes | tr-gw8ergozrv77rtbjd\*\*\*\* | The ID of the transit router. |
| TransitRout erCidrId | String | Query | Yes | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block.<br>You can call the ListTransitRouterCidr operation to query the ID of a CIDR block. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| Name | String | Query | No | nametest | The new name of the transit router CIDR block.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| Description | String | Query | No | desctest | The new description of the transit router CIDR block.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| Cidr | String | Query | No | 192.168.10.0/24 | The new CIDR block of the transit router. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without sending the actual request.Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false: performs a dry run and performs the actual request. If the request passes the dry run, the CIDR block of the transit router is modified. |
| PublishCidr Route | Boolea n | Query | No | true | Specifies whether to allow the system to automatically add routes that point to the CIDR block to the route table of the transit router.<br>• true: yes<br>• false: no |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyTransitRouterCidr
&TransitRouterId=tr-gw8ergozrv77rtbjd****
&TransitRouterCidrId=cidr-0zv0q9crqpntzz****
&RegionId=cn-qingdao-env17e-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A"
}
```

`XML`  format

```xml
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
```

<a id="section-1-4-3"></a>

### 1.4.3. ListTransitRouterCidr

Queries the CIDR blocks of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterCidr | The operation that you want to perform. Set the value to ListTransitRouterCidr. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| TransitRout erId | String | Query | Yes | tr-p0w3x8c9em72a40nw\*\*\*\* | The ID of the transit router. |
| TransitRout erCidrId | String | Query | No | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without sending the actual request.Valid values:<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CidrLists | Array |  | The CIDR blocks of the transit router. |
| -TransitRouterCid rId | String | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block. |
| -Family | String | IPv4 | The type of the CIDR block.<br>The value is <strong>IPv4</strong>, which indicates that the CIDR block is of the IPv4 type. |
| -Name | String | nametest | The name of the transit router CIDR block. |
| -Description | String | desctest | The description of the transit router CIDR block. |
| -Cidr | String | 192.168.10.0/24 | The CIDR block of the transit router. |
| -PublishCidrRoute | Boolean | true | Indicates whether the system is allowed to automatically add routes that point to the CIDR block to the route table of the transit router.<br>• true: yes<br>• false: no |
| -TransitRouterId | String | tr-p0w3x8c9em72a40n w\*\*\*\* | The ID of the transit router. |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterCidr
&TransitRouterId=tr-p0w3x8c9em72a40nw****
&RegionId=cn-qingdao-env17e-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A",
 "CidrLists":{
  "Description":"desctest",
  "Cidr":"192.168.10.0/24",
  "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****",
  "Family":"IPv4",
  "PublishCidrRoute":true,
  "Name":"nametest",
  "TransitRouterId":"tr-p0w3x8c9em72a40nw****"
 }
}
```

`XML`  format

```xml
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
<CidrLists>
 <Description>desctest</Description>
 <Cidr>192.168.10.0/24</Cidr>
 <TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId>
 <Family>IPv4</Family>
 <PublishCidrRoute>true</PublishCidrRoute>
 <Name>nametest</Name>
 <TransitRouterId>tr-p0w3x8c9em72a40nw****</TransitRouterId>
</CidrLists>
```

<a id="section-1-4-4"></a>

### 1.4.4. ListTransitRouterCidrAllocation

Queries how IP addresses within the CIDR block of a transit router are allocated.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterCidrAllocat ion | The operation that you want to perform. Set the value to ListTransitRouterCidrAll ocation. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| TransitRout erId | String | Query | Yes | tr-p0w3x8c9em72a40nw\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| TransitRout erCidrId | String | Query | No | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block.<br>You can call the ListTransitRouterCidr operation to query the ID of a transit router CIDR block. |
| CidrBlock | String | Query | No | 192.168.10.0/28 | The CIDR block that has been allocated to network instances. |
| Cidr | String | Query | No | 192.168.10.0/24 | The CIDR block of the transit router. |
| DedicatedO wnerId | String | Query | No | VPN | The CIDR block that is for exclusive use.<br>Set the value to <strong>VPN</strong>, which specifies the CIDR block that is reserved for VPN connections. |
| AttachmentI d | String | Query | No | tr-attach-2nalp6yksc805w\*\*\*\* | The ID of the network instance connection. |
| Attachment Name | String | Query | No | nametest | The name of the network instance connection. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without sending the actual request.Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |
| MaxResults | Integer | Query | No | 20 | The number of entries per page.<br>• If you do not set MaxResults, it indicates that you do not need to query results in batches. The value of MaxResults indicates the total number of entries.<br>• If a value is specified for MaxResults, it indicates that you need to query results in batches. Valid values: 1 to <strong>100</strong>. We recommend that you set MaxResults to <strong>20</strong>.<br>The value of <strong>MaxResults</strong> in the response indicates the number of entries in the current batch. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the NextToken parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterCid rAllocations | Array |  | The information about the CIDR blocks that have IP addresses allocated to network instances. |
| -TransitRouterCid rId | String | cidr-0zv0q9crqpntzz\*\*\*\* | The ID of the transit router CIDR block. |
| -AllocatedCidrBlo ck | String | 192.168.10.0/28 | The CIDR blocks that have been allocated to network instances. |
| -AttachmentId | String | tr-attach-2nalp6yksc805w\*\*\*\* | The ID of the network instance connection. |
| -Cidr | String | 192.168.10.0/24 | The CIDR block of the transit router. |
| -AttachmentNam e | String | nametest | The name of the network instance connection. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 1 | The number of entries per page.<br>• If no value is specified for <strong>MaxResults</strong>, query results are returned in one batch. The value of <strong>MaxResults</strong> indicates the total number of entries.<br>• If a value is specified for <strong>MaxResults</strong>, query results are returned in batches. The value of <strong>MaxResults</strong> in the response indicates the number of entries in the current batch. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterCidrAllocation
&TransitRouterId=tr-p0w3x8c9em72a40nw****
&RegionId=cn-qingdao-env17e-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A",
 "MaxResults":1,
 "TransitRouterCidrAllocations":{
  "Cidr":"192.168.10.0/24",
  "AttachmentName":"nametest",
  "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****",
  "AllocatedCidrBlock":"192.168.10.0/28",
  "AttachmentId":"tr-attach-2nalp6yksc805w****"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
<MaxResults>1</MaxResults>
<TransitRouterCidrAllocations>
 <Cidr>192.168.10.0/24</Cidr>
 <AttachmentName>nametest</AttachmentName>
 <TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId>
 <AllocatedCidrBlock>192.168.10.0/28</AllocatedCidrBlock>
 <AttachmentId>tr-attach-2nalp6yksc805w****</AttachmentId>
</TransitRouterCidrAllocations>
```

<a id="section-1-4-5"></a>

### 1.4.5. DeleteTransitRouterCidr

Deletes a transit router CIDR block.

**Usage notes**

If IP addresses within the CIDR block have been allocated to network instances, the CIDR block cannot be deleted.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterCidr | The operation that you want to perform. Set the value to DeleteTransitRouterCid r. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| TransitRout erId | String | Query | Yes | tr-p0w3x8c9em72a40nwXXXX | The ID of the transit router. |
| TransitRout erCidrId | String | Query | Yes | cidr-0zv0q9crqpntzzXXXX | The ID of the transit router CIDR block.<br>You can call the ListTransitRouterCidr operation to query the ID of a transit router CIDR block. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without sending the actual request.Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterCidr
&TransitRouterId=tr-p0w3x8c9em72a40nwXXXX
&TransitRouterCidrId=cidr-0zv0q9crqpntzzXXXX
&RegionId=cn-qingdao-env17e-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A"
}
```

`XML`  format

```xml
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | CIDR_BLOCK_ALLOCA TED | OperationFailed.CidrBlockAllocated | Cidr blocks are allocated from the cidr, which should be released first. |

<a id="section-1-5"></a>

## 1.5. VPC connections

<a id="section-1-5-1"></a>

### 1.5.1. CreateTransitRouterVpcAttachment

Creates a virtual private cloud (VPC) connection on a transit router.

**Usage notes**

- By default, route learning and associated forwarding are disabled between transit router route tables and VPC connections.

- Before you call this operation, make sure that the following requirements are met:

  - To connect to a network instance that belongs to another Alibaba Cloud account, you must first acquire the required permissions from the account. For more information, see GrantInstanceToTransitRouter.

  - If the region of a transit router contains only one zone, before you connect the transit router to a VPC, make sure that the VPC in the preceding zone has at least one vSwitch. In addition, make sure that the vSwitch has at least one idle IP address.

  - If the region of a transit router contains multiple regions, before you connect the transit router to a VPC, make sure that the VPC has at least two vSwitches residing in different zones. In addition, make sure that each vSwitch has at least one idle IP address. This way, the two vSwitches can conduct zone-disaster recovery to ensure uninterrupted data transmission between the VPC and the transit router.

    *If your transit router is deployed in a region that contains multiple zones, we recommend that you create a vSwitch in each zone to support VPC connections. Make sure that each vSwitch has at least one idle IP address. This reduces the network latency and data transmission distance.*

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterVpcAttac hment | The operation that you want to perform. Set the value to CreateTransitRouterVpcAt <strong>tachment</strong>. |

<table>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>02fb3da4-130e-11e9-8e44-001****</td>
    <td>The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <em>request ID as the client</em> <em>token. The request ID</em> <em>may be different for</em> <em>each request.</em></td>
  </tr>
  <tr>
    <td>CenId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>cen-j3jzhw1zpau2km****</td>
    <td>The ID of the Cloud Enterprise Network (CEN) instance.</td>
  </tr>
  <tr>
    <td>TransitRoute rId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>tr-bp1su1ytdxtataupl****</td>
    <td>The ID of the transit router.</td>
  </tr>
  <tr>
    <td>RegionId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>cn-qingdao-env17e-d01</td>
    <td>The region ID of the VPC.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list.</td>
  </tr>
  <tr>
    <td>TransitRoute rAttachment Name</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>testname</td>
    <td>The name of the VPC connection.<br>The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter.</td>
  </tr>
  <tr>
    <td>TransitRoute rAttachment Description</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>testname</td>
    <td>The description of the VPC connection.<br>The description must be 2 to 256 characters in length. It must start with a letter but cannot start with <code> http:// </code>or <code> https:// </code>.</td>
  </tr>
  <tr>
    <td>VpcId</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>vpc-bp1kbjcre9vtsebo1****</td>
    <td>The VPC ID.</td>
  </tr>
  <tr>
    <td>VpcOwnerId</td>
    <td>Long</td>
    <td>Query</td>
    <td>No</td>
    <td>1250123456123456</td>
    <td>The UID of the level-1 organization to which the VPC belongs. By default, the UID of the current level-1 organization is specified.<br><em>If you want to connect to</em> <em>a network instance that</em> <em>belongs to a different</em> <em>account, this parameter</em> <em>is required.</em></td>
  </tr>
  <tr>
    <td>ChargeType</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.</td>
  </tr>
  <tr>
    <td>ZoneMappin gs</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>Yes</td>
    <td></td>
    <td>A vSwitch that is deployed in a zone supported by transit routers.<br>You can specify at most 10 vSwitches in each call.</td>
  </tr>
  <tr>
    <td>-VSwitchId</td>
    <td>String</td>
    <td></td>
    <td>Yes</td>
    <td>vsw-bp1a214sbus8z3b54****</td>
    <td>A vSwitch that is deployed in a zone supported by transit routers.<br>You can specify at most 10 vSwitches in each call.</td>
  </tr>
  <tr>
    <td>-ZoneId</td>
    <td>String</td>
    <td></td>
    <td>Yes</td>
    <td>cn-qingdao-env17e-amtest17001-a</td>
    <td>The ID of the zone that supports transit routers.<br>You can call the DescribeZones operation to query the most recent zone list.<br>You can specify at most 10 zones in each call.</td>
  </tr>
  <tr>
    <td>Tag</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td></td>
    <td>The tags.<br>You can specify at most 20 tags in each call.</td>
  </tr>
  <tr>
    <td>-Key</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>tagtest</td>
    <td>The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify at most 20 tag keys.</td>
  </tr>
  <tr>
    <td>-Value</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>tagtest</td>
    <td>The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Limit |
| --- | --- | --- | --- |
| TransitRouterAtt achmentId | String | tr-attach-ia340z7xis7t5s\*\*\*\* | The ID of the VPC connection. |
| RequestId | String | C087A369-82B9-43EF-91F4-4B63A9C6E6B6 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterVpcAttachment
&VpcId=vpc-bp1kbjcre9vtsebo1****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TransitRouterAttachmentId":"tr-attach-ia340z7xis7t5s****",
 "RequestId":"C087A369-82B9-43EF-91F4-4B63A9C6E6B6"
}
```

`XML`  format

```xml
<TransitRouterAttachmentId>tr-attach-ia340z7xis7t5s****</TransitRouterAttachmentId>
<RequestId>C087A369-82B9-43EF-91F4-4B63A9C6E6B6</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_ALREADY_ATTACHED_CEN_PROTECTION_LE VEL_FULL | InvalidStatus.VpcAttachedFullMode Cen | Operation is invalid because the instance has already attached to other cen with protection level FULL |
| 400 | ATTACH_ACROSS_BID _FORBIDDEN | Forbbiden.AttachChildInstanceAcro ssBid | Operation is invalid, please apply for cross-bid attaching. |
| 400 | OperationUnsupporte d.TransitRouterRegion Id | OperationUnsupported.TransitRout erRegionId | The specified TransitRouterRegion does not support the operation. |
| 400 | NoPermission.AliyunS erviceRoleForCEN | NoPermission.AliyunServiceRoleFor CEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForCEN. Service Name: cen.aliyuncs.com. Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
| 400 | PARAMETER_ILLEGAL_RESOURCE_REGIONID | IllegalParam.RegionId | The Specified Parameter RegionId is illegal |
| 400 | MissingParam.CenId or RegionId | MissingParam.CenIdOrRegionId | Either CenId or RegionId must be specified. |
| 400 | IllegalParam.ZoneId | IllegalParam.ZoneId | The specified ZoneId is illegal. |
| 400 | IllegalParam.ChargeTy pe | IllegalParam.ChargeType | The specified ChargeType is illegal. |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | The specified TransitRouterId is not found. |
| 400 | INVALID_OPERATION_RESOURCE_ATTACHM ENT_STATUS | IncorrectStatus.Attachment | The resource is not in a valid state for the attachment operation. |
| 400 | INVALID_VPC_STATUS | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
| 400 | UNESPECTED_VPC_RE SULT | IncorrectStatus.VpcOrVswitch | The Vpc Or Vswith is not in a valid state for the attachment operation. |
| 400 | NOT_SUPPORT_VPC_A UTO_PUBLISH_ROUTE | OperationNotSupport.VpcAutoRout esPublish | Auto publish vpc routes is not supported in this region. |
| 400 | INVALID_OPERATION_CEN_ALREADY_AUTO_PUBLISH_ROUTE_TO_I NSTANCE | InvalidOperation.VpcAutoRoutesPu blishInOtherCEN | The operation is not supported because the VPC is already set autoRoutesPublish in other CEN. |
| 400 | QUOTA_FULL_PER_TR_VPC_AUTO_ROUTE | QuotaExceeded.VpcAutoRoutesPub lishPerTransitRouter | The count of VPC instance which set autoRoutesPublish in transitRouter is over limit. |
| 400 | VPN_ASSOCIATED | InvalidOperation.VpnAssociated | The operation is not supported because the VPC is associated with VPN. |
| 400 | USER_NOT_OPEN_TR_SERVICE | Forbbiden.TransitRouterServiceNot Open | The user has not open transit router service. |
| 400 | PARAMETER_ILLEGAL_ZONE_MAPPINGS | IllegalParam.ZoneMappings | The Specified Parameter ZoneMappings is illegal |
| 400 | OperationUnsupporte d.TransitRouterType | OperationUnsupported.TransitRout erType | The specified TransitRouterType does not support the operation. |
| 400 | InvalidCenId.NotFoun d | InvalidCenId.NotFound | CenId is not found. |
| 400 | IllegalParam.VSwitchI d | IllegalParam.VSwitchId | VSwitchId is illegal. |
| 400 | InvalidVSwitchId.NotF ound | InvalidVSwitchId.NotFound | VSwitchId is not found. |
| 400 | IllegalParam.RegionId | IllegalParam.RegionId | RegionId is illegal. |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouterInsta nce | The status of TransitRouter is incorrect. |
| 400 | CEN_FULL_LEVEL_NOT _SUPPORT_TR | OperationUnsupported.CenFullLev el | CEN full level does not support TransitRouter |

<a id="section-1-5-2"></a>

### 1.5.2. UpdateTransitRouterVpcAttachmentAttribute

Modifies the name and description of a virtual private cloud (VPC) connection on a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | UpdateTransitRouterVpcAtt achmentAttribute | The operation that you want to perform. Set the value to UpdateTransitRouterVpc AttachmentAttribute. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the VPC connection. |
| TransitRout erAttachme ntName | String | Query | No | testname | The name of the VPC connection.<br>The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter. |
| TransitRout erAttachme ntDescriptio n | String | Query | No | testdesc | The description of the VPC connection.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and performs the actual request.<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the system returns the ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E61D334-4025-41EF-9145-FC327B35301D | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterVpcAttachmentAttribute
&TransitRouterAttachmentId=tr-attach-nls9fzkfat8934****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"7E61D334-4025-41EF-9145-FC327B35301D"
}
```

`XML`  format

```xml
<RequestId>7E61D334-4025-41EF-9145-FC327B35301D</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IncorrectStatus.Transi tRouterAttachmentId | IncorrectStatus.TransitRouterAttac hmentId | TransitRouterAttachmentId status is invalid. |
| 400 | InvalidTransitRouterAt tachmentId.NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | NOT_SUPPORT_VPC_A UTO_PUBLISH_ROUTE | InvalidOperation.RegionNotSupport | The operation is not supported in this region. |
| 400 | INVALID_OPERATION_CEN_ALREADY_AUTO_PUBLISH_ROUTE_TO_I NSTANCE | InvalidOperation.VpcAutoRoutesPu blishInOtherCEN | The operation is not supported because the VPC is already set autoRoutesPublish in other CEN. |
| 400 | QUOTA_FULL_PER_TR_VPC_AUTO_ROUTE | QuotaExceeded.VpcAutoRoutesPub lishPerTransitRouter | The count of VPC instance which set autoRoutesPublish in transitRouter is over limit. |
| 400 | VPN_ASSOCIATED | InvalidOperation.VpnAssociated | The operation is not supported because the VPC is associated with VPN. |

<a id="section-1-5-3"></a>

### 1.5.3. ListTransitRouterVpcAttachments

Queries the virtual private cloud (VPC) connections on a transit router.

**Usage notes**

You can use the following methods to query VPC connections on a transit router:

- Query all VPC connections on a transit router by specifying the ID of the transit router.

- Query all VPC connections on a transit router by specifying the ID of the Cloud Enterprise Network (CEN) instance and the ID of the region where the transit router is deployed.

- Query all VPC connections in the region where the transit router is deployed by specifying the ID of the region.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterVpcAttachm ents | The operation that you want to perform. Set the value to ListTransitRouterVpcAtta <strong>chments</strong>. |
| CenId | String | Query | No | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| RegionId | String | Query | No | cn-qingdao-env66-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| TransitRoute rAttachment Id | String | Query | No | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the VPC connection. |
| TransitRoute rId | String | Query | No | tr-bp1su1ytdxtataupl\*\*\*\* | The ID of the transit router. |
| MaxResults | Integ er | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGK Pd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first query and no subsequent queries are to be sent, ignore this parameter.<br>• If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results. |
| VpcId | String | Query | No | vpc-bp1kbjcre9vtsebo1\*\*\*\* | The VPC ID. |
| Tag | Repea tList | Query | No |  | The tags.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | tagtest | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |
| -Value | String |  | No | tagtest | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterAtt achments | Array |  | The information about the VPC connection. |
| -ZoneMappings | Array |  | The primary and secondary zones of the VPC connection and the vSwitches and elastic network interfaces (ENIs) of the VPC. |
| --ZoneId | String | cn-qingdao-env17e-amtest17001-a | The zone ID of the vSwitch. |
| --VSwitchId | String | vsw-bp1a214sbus8z3b54\* \*\*\* | The vSwitch ID. |
| --NetworkInterface Id | String | eni-bp149hmyaqegerml\*\* \*\* | The ID of the ENI created in the vSwitch of the transit router. |
| -Tags | Array |  | The tags. |
| --Key | String | tagtest | The tag key. |
| --Value | String | tagtest | The tag value. |
| -CreationTime | String | 2021-06-15T02:14Z | The time when the VPC connection was created.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC). |
| -Status | String | Attached | The status of the VPC connection.<br>• <strong>Attached</strong>: The VPC connection is created on the transit router.<br>• <strong>Attaching</strong>: The VPC connection is being created on the transit router.<br>• <strong>Detaching</strong>: The VPC connection is being deleted from the transit router. |
| -VpcId | String | vpc-bp1h8vbrbcgohcju5\*\* \*\* | The VPC ID. |
| -TransitRouterAtt achmentId | String | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the VPC connection. |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl\*\*\* \* | The ID of the transit router. |
| -ResourceType | String | VPC | The type of resource to which the transit router is connected.<br>The value is <strong>VPC</strong>. |
| -TransitRouterAtt achmentDescript ion | String | testdesc | The description of the VPC connection. |
| -VpcOwnerId | Long | 1250123456123456 | The UID of the level-1 organization to which the VPC belongs. |
| -VpcRegionId | String | cn-qingdao-env17e-d01 | The region ID of the VPC. |
| -TransitRouterAtt achmentName | String | testname | The name of the VPC connection. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | C97FF53F-3EF8-4883-B459-60E171924B23 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterVpcAttachments
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"C97FF53F-3EF8-4883-B459-60E171924B23",
 "MaxResults":20,
 "TransitRouterAttachments":{
  "Status":"Attached",
  "TransitRouterAttachmentId":"tr-attach-nls9fzkfat8934****",
  "-Tags":{
   "Value":"tagtest",
   "Key":"tagtest"
  },
  "TransitRouterAttachmentName":"testname",
  "ResourceType":"VPC",
  "VpcOwnerId":1250123456123456,
  "VpcId":"vpc-bp1h8vbrbcgohcju5****",
  "CreationTime":"2021-06-15T02:14Z",
  "VpcRegionId":"cn-qingdao-env17e-d01",
  "-ZoneMappings":{
   "ZoneId":"cn-qingdao-env17e-amtest17001-a",
   "VSwitchId":"vsw-bp1a214sbus8z3b54****",
   "NetworkInterfaceId":"eni-bp149hmyaqegerml****"
  },
  "TransitRouterAttachmentDescription":"testdesc",
  "TransitRouterId":"tr-bp1su1ytdxtataupl****"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>C97FF53F-3EF8-4883-B459-60E171924B23</RequestId>
<MaxResults>20</MaxResults>
<TransitRouterAttachments>
 <Status>Attached</Status>
 <TransitRouterAttachmentId>tr-attach-nls9fzkfat8934****</TransitRouterAttachmentId>
 <-Tags>
  <Value>tagtest</Value>
  <Key>tagtest</Key>
 </-Tags>
 <TransitRouterAttachmentName>testname</TransitRouterAttachmentName>
 <ResourceType>VPC</ResourceType>
 <VpcOwnerId>1250123456123456</VpcOwnerId>
 <VpcId>vpc-bp1h8vbrbcgohcju5****</VpcId>
 <CreationTime>2021-06-15T02:14Z</CreationTime>
 <VpcRegionId>cn-qingdao-env17e-d01</VpcRegionId>
 <-ZoneMappings>
  <ZoneId>cn-qingdao-env17e-amtest17001-a</ZoneId>
  <VSwitchId>vsw-bp1a214sbus8z3b54****</VSwitchId>
  <NetworkInterfaceId>eni-bp149hmyaqegerml****</NetworkInterfaceId>
 </-ZoneMappings>
 <TransitRouterAttachmentDescription>testdesc</TransitRouterAttachmentDescription>
 <TransitRouterId>tr-bp1su1ytdxtataupl****</TransitRouterId>
</TransitRouterAttachments>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstanc e | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | IllegalParam.TransitRo uterId | IllegalParam.TransitRouterId | The specified TransitRouterId is invalid. |
| 400 | IllegalParam.CenId Or RegionId | IllegalParam.CenIdOrRegionId | The specified CenId or RegionId is invalid. |

<a id="section-1-5-4"></a>

### 1.5.4. DeleteTransitRouterVpcAttachment

Deletes a virtual private cloud (VPC) connection from a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-ia340z7xis7t5s\*\*\*\* | The ID of the VPC connection. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and sends the request.<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request. |
| Force | Boolea n | Query | No | false | Specifies whether to forcefully delete the VPC connection. Valid values:<br>• false (default): checks resources such as associated forwarding correlations and route learning policies that are related to the VPC connection before it is deleted. If such resources exist, the VPC connection is not deleted and an error message is returned.<br>• true: deletes the VPC connection and all resources that are related to the VPC connection. |
| Action | String | Query | No | DeleteTransitRouterVpcAtta chment | The operation that you want to perform. Set the value to DeleteTransitRouterVpc Attachment. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E61D334-4025-41EF-9145-FC327B35301D | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterVpcAttachment
&TransitRouterAttachmentId=tr-attach-ia340z7xis7t5s****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"7E61D334-4025-41EF-9145-FC327B35301D"
}
```

`XML`  format

```xml
<RequestId>7E61D334-4025-41EF-9145-FC327B35301D</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | ATTACHMENT_REFERE NCED_BY_VPC_ROUTE _ENTRY | OperationFailed.AttachmentRefere ncedVpcRouteEntryExisted | Operation is failed because there is at least one route entry which next hop is the specified attachment. |
| 400 | OperationFailed.Route TableAssociationExist | OperationFailed.RouteTableAssocia tionExist | Operation failed because TransitRouterRouteTable exists |
| 400 | OperationFailed.Route TablePropagationExist | OperationFailed.RouteTablePropag ationExist | The specified TransitRouterAttachment has configured RouteTablePropagation.Please remove the configuration first. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_EXIST | OperationFailed.MulticastDomainA ssociationExist | The specified TransitRouterAttachment has configured MulticastDomainAssociation.Please remove the configuration first. |
| 400 | OperationUnsupporte d.TransitRouterType | OperationUnsupported.TransitRout erType | The specified TransitRouterType does not support the operation. |
| 400 | INVALID_OPERATION_PREFIXLIST_EXIST | OperationFailed.PrefixListExist | Operation failed because PrefixList exists. |
| 400 | InvalidTrAttachmentId.NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | VPC_ROUTE_ENTRY_S TATUS_ERROR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPC_SWITCH_STATUS _ERROR | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 400 | VPC_ROUTE_ENTRY_S TATUS_ERROR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPC_SWITCH_STATUS _ERROR | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 400 | UNESPECTED_VPC_RE SULT | IncorrectStatus.Vpc | The resource is not in a valid state for the operation. |
| 400 | OperationFailed.Route EntryExist | OperationFailed.RouteEntryExist | Operation failed because the TransitRouterAttachment exists in RouteTable. |

<a id="section-1-5-5"></a>

### 1.5.5. UpdateTransitRouterVpcAttachmentZones

Modifies the zones and vSwitches that are associated with a virtual private cloud (VPC) connection.

**Usage notes**

When you associate a zone and a vSwitch with a VPC connection, make sure that the vSwitch has at least one idle IP address. When you connect a transit router to the VPC, the transit router creates an elastic network interface (ENI) in the vSwitch. The ENI occupies one IP address in the vSwitch to forward traffic between the VPC and transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No |  | The operation that you want to perform. Set the value to UpdateTransitRouterVpc AttachmentZones. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without performing the actual request. Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the zones and vSwitches of the VPC connection are modified. |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-9bbqyygouv4cpn\*\*\*\* | The ID of the VPC connection. |
| AddZoneMa ppings | Repeat List | Query | No |  | The zones and vSwitches that you want to associate with the VPC connection. |
| -VSwitchId | String |  | No | vsw-wz9f5izl6wshndmta\*\*\*\* | The ID of the vSwitch that you want to associate with the VPC connection.<br>You can specify at most 10 vSwitches in each call.<br>• If the VPC belongs to the current organization, you can call the DescribeVSwitches operation to query the IDs of vSwitches and zones in the VPC.<br>• If the VPC does not belong to the current organization, you can call the ListGrantVSwitchesToCen operation to query the IDs of vSwitches and zones in the VPC. |
| -ZoneId | String |  | No | cn-qingdao-env17e-amtest17001-a | The ID of the zone where the vSwitch that you want to associate with the VPC connection is deployed.<br>You can specify at most 10 vSwitches in each call. |
| RemoveZon eMappings | Repeat List | Query | No |  | The zones and vSwitches that you want to disassociate from the VPC connection. |
| -VSwitchId | String |  | No | vsw-wz9f5izl6wshndmta\*\*\*\* | The ID of the vSwitch that you want to disassociate from the VPC connection.<br>You can specify at most 10 vSwitches in each call. |
| -ZoneId | String |  | No | cn-qingdao-env17e-amtest17001-a | The ID of the zone where the vSwitch that you want to disassociate from the VPC connection is deployed.<br>You can specify at most 10 vSwitches in each call. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 595AE52F-49FF-5788-A677-0DD1467941A1 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterVpcAttachmentZones
&TransitRouterAttachmentId=tr-attach-9bbqyygouv4cpn****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"595AE52F-49FF-5788-A677-0DD1467941A1"
}
```

`XML`  format

```xml
<RequestId>595AE52F-49FF-5788-A677-0DD1467941A1</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.ZoneId | IllegalParam.ZoneId | The specified ZoneId is illegal. |
| 400 | IncorrectStatus.Transi tRouterAttachmentId | IncorrectStatus.TransitRouterAttac hment | The status of TransitRouterAttachment is incorrect. |
| 400 | IllegalParam.VSwitchI d | IllegalParam.VSwitchId | VSwitchId is illegal. |
| 400 | InvalidTransitRouterAt tachmentId.NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | OperationUnsupporte d.ServiceMode | OperationUnsupported.ServiceMod e | The specified TransitRouter does not support the operation. |
| 400 | IllegalParam.AddZone Mappings Or RemoveZoneMapping s | IllegalParam.AddOrRemoveZoneMa ppings | The specified AddZoneMappings or RemoveZoneMappings are illegal. |
| 400 | IncorrectStatus.VpcCb nStatus | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
| 400 | OperationDenied.Rout eEntryOnEni | OperationDenied.RouteEntryOnEni | Operation is failed because there is at least one route entry which next hop is the specified eni. |
| 400 | VPC_ROUTE_ENTRY_S TATUS_ERROR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPC_SWITCH_STATUS _ERROR | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 404 | InvalidZoneId.NotFoun d | IllegalParam.ZoneId | The specified ZoneId is illegal. |

<a id="section-1-5-6"></a>

### 1.5.6. ListGrantVSwitchesToCen

Queries the information about vSwitches in virtual private clouds (VPCs) that belong to a different Alibaba Cloud account than the Cloud Enterprise Network (CEN) instance.

**Usage notes**

Before you can call the ListGrantVSwitchesToCen operation, you must obtain the required permissions from the Alibaba Cloud account to which the VPC belongs. For more information, see GrantInstanceToCen.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListGrantVSwitchesToCen | The operation that you want to perform. Set the value to ListGrantVSwitchesToCe n. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the VPC.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| CenId | String | Query | Yes | cen-44m0p68spvlrqq\*\*\*\* | The ID of the CEN instance. |
| VpcId | String | Query | Yes | vpc-bp12ge2tq5gzdc915\*\*\*\* | The VPC ID. |
| PageNumbe r | Integer | Query | No | 1 | The page number. Default value: <strong>1</strong>. |
| PageSize | Integer | Query | No | 10 | The number of entries per page. Valid values: <strong>1</strong> to 50. Default value: <strong>10</strong>. |
| ZoneId | String | Query | No | cn-qingdao-env17e-amtest17001-a | The zone ID of the vSwitch.<br>• If you specify a zone ID, the system queries the information about the vSwitches in the specified zone.<br>• If you do not specify a zone ID, the system queries the information about the vSwitches in all zones.<br>You can call the DescribeZones operation to query the most recent zone list. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| VSwitches | Array |  | The information about the vSwitch. |
| -VpcId | String | vpc-bp12ge2tq5gzdc915\* \*\*\* | The ID of the VPC to which the vSwitch belongs. |
| -ZoneId | String | cn-qingdao-env17e-amtest17001-a | The zone ID of the vSwitch. |
| -VSwitchId | String | vsw-bp1194lh263wx1gsk\* \*\*\* | The vSwitch ID. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | A9288C78-881A-5D30-A8A9-68E05EE0A086 | The request ID. |
| PageNumber | Integer | 1 | The page number. |
| TotalCount | Integer | 2 | The total number of entries returned. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListGrantVSwitchesToCen
&RegionId=cn-qingdao-env17e-d01
&CenId=cen-44m0p68spvlrqq****
&VpcId=vpc-bp12ge2tq5gzdc915****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":2,
 "PageSize":10,
 "RequestId":"A9288C78-881A-5D30-A8A9-68E05EE0A086",
 "PageNumber":1,
 "VSwitches":{
  "VpcId":"vpc-bp12ge2tq5gzdc915****",
  "ZoneId":"cn-qingdao-env17e-amtest17001-a",
  "VSwitchId":"vsw-bp1194lh263wx1gsk****"
 }
}
```

`XML`  format

```xml
<TotalCount>2</TotalCount>
<PageSize>10</PageSize>
<RequestId>A9288C78-881A-5D30-A8A9-68E05EE0A086</RequestId>
<PageNumber>1</PageNumber>
<VSwitches>
 <VpcId>vpc-bp12ge2tq5gzdc915****</VpcId>
 <ZoneId>cn-qingdao-env17e-amtest17001-a</ZoneId>
 <VSwitchId>vsw-bp1194lh263wx1gsk****</VSwitchId>
</VSwitches>
```

<a id="section-1-6"></a>

## 1.6. VBR connections

<a id="section-1-6-1"></a>

### 1.6.1. CreateTransitRouterVbrAttachment

Connects a virtual border router (VBR) to a transit router.

**Usage notes**

After you create a VBR connection, it is not in route learning or associated forwarding relationship with transit router route tables by default.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterVbrAttac hment | The operation that you want to perform. Set the value to CreateTransitRouterVbrAt <strong>tachment</strong>. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| CenId | String | Query | No | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| TransitRoute rId | String | Query | No | tr-bp1su1ytdxtataupl\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | No | cn-qingdao-env17e-d01 | The region ID of the VBR.<br>You can call the DescribeRegions operation to query the most recent region list. |
| TransitRoute rAttachment Name | String | Query | No | testname | The name of the VBR connection.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter. |
| TransitRoute rAttachment Description | String | Query | No | testdesc | The description of the VBR connection.<br>The description must be 2 to 256 characters in length. It must start with a letter but cannot start with <code> http:// </code>or <code> https:// </code>. |
| VbrId | String | Query | Yes | vbr-bp1svadp4lq38janc\*\*\*\* | The VBR ID. |
| VbrOwnerId | Long | Query | No | 1250123456123456 | The UID of the level-1 organization to which the VBR belongs. By default, the UID of the current level-1 organization is specified.<br><em>If you want to connect to</em> <em>a network instance that</em> <em>belongs to another</em> <em>account, this parameter</em> <em>is required.</em> |
| AutoPublish RouteEnable d | Boole an | Query | No | false | Specifies whether to enable the transit router to automatically advertise routes to the VBR. Valid values:<br>• <strong>false</strong> (default)<br>• true |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and sends the request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the system returns the ID of the request. |
| Tag | Repea tList | Query | No |  | The information about the tag.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | TagKey | The tag key of the VPN connection.<br>The tag keys cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |
| -Value | String |  | No | TagValue | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterAtt achmentId | String | tr-attach-ia340z7xis7t5s\*\*\*\* | The ID of the VBR connection. |
| RequestId | String | C087A369-82B9-43EF-91F4-4B63A9C6E6B6 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterVbrAttachment
&VbrId=vbr-bp1svadp4lq38janc****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TransitRouterAttachmentId":"tr-attach-ia340z7xis7t5s****",
 "RequestId":"C087A369-82B9-43EF-91F4-4B63A9C6E6B6"
}
```

`XML`  format

```xml
<TransitRouterAttachmentId>tr-attach-ia340z7xis7t5s****</TransitRouterAttachmentId>
<RequestId>C087A369-82B9-43EF-91F4-4B63A9C6E6B6</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | NoPermission.AliyunS erviceRolePolicyForCE N | NoPermission.AliyunServiceRolePol icyForCEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRolePolicyForCEN.Service Name: cen.aliyuncs.com.Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
| 400 | OperationUnsupporte d.TransitRouterRegion Id | OperationUnsupported.TransitRout erRegionId | The specified TransitRouterRegion does not support the operation. |
| 400 | InvalidCenId.NotFoun d | InvalidCenId.NotFound | CenId is not found. |
| 400 | INVALID_OPERATION_RESOURCE_ATTACHM ENT_STATUS | InvalidStatus.ResourceStatus | The resource is not in a valid state for the attachment operation. |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found. |
| 400 | USER_NOT_OPEN_TR_SERVICE | Forbbiden.TransitRouterServiceNot Open | The user has not open transit router service. |
| 400 | OperationUnsupporte d.TransitRouterType | OperationUnsupported.TransitRout erType | The specified TransitRouterType does not support the operation. |
| 400 | MissingParam.CenId or RegionId | MissingParam.CenIdOrRegionId | Either CenId or RegionId must be specified. |
| 400 | INVALID_VPC_STATUS | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
| 400 | DEVICE_MODEL_FORB IDDEN | Forbidden.VbrDeviceModel | Attach VBR on some access device models are forbidden. |
| 403 | INVALID_OPERATION_DEVICE_MODEL_FORB IDDEN | Forbidden.VbrDeviceModel | The attached VBR on some access device models are not supported.Please submit a ticket to continue using this VBR on CEN. |

<a id="section-1-6-2"></a>

### 1.6.2. ListTransitRouterVbrAttachments

Queries virtual border router (VBR) connections on a transit router.

**Usage notes**

You can use the following methods to query VBR connection information:

- Query all VBR connections on a transit router by specifying the ID of the transit router.

- Query all VBR connections on a transit router by specifying the ID of an Cloud Enterprise Network (CEN) instance and the ID of the region in which the transit router is deployed.

- Configure the **TransitRouterAttachmentId**

  parameter to specify the VBR connection that you want

  to query.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| CenId | String | Query | No | cen-j3jzhw1zpau2km\*\*\*\* | The ID of the CEN instance. |
| RegionId | String | Query | No | cn-qingdao-env66-d01 | The region ID of the transit router.<br>You can call the DescribeRegions operation to query the most recent region list. |
| TransitRout erAttachme ntId | String | Query | No | tr-attach-oyf70wfuorwx87\*\*\*\* | The ID of the VBR connection. |
| TransitRout erId | String | Query | No | tr-bp1su1ytdxtataupl\*\*\*\* | The ID of the transit router. |
| MaxResults | Integer | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | dd20\*\*\*\* | The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. |
| Tag | Repeat List | Query | No |  | The tags.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | tagtest | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |
| -Value | String |  | No | tagtest | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call. |
| Action | String | Query | No | ListTransitRouterVbrAttach ments | The operation that you want to perform. Set the value to ListTransitRouterVbrAtta chments. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TotalCount | Integer | 1 | The total number of entries returned. |
| NextToken | String | dd20\*\*\*\* | The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. |
| RequestId | String | F42D9616-29EB-4E75-8CA8-9654D4E07501 | The request ID. |
| MaxResults | Integer | 20 | The number of entries per page. |
| TransitRouterAtt achments | Array |  | A list of VBR connections. |
| -Tags | Array |  | The tags. |
| --Key | String | tagtest | The tag key. |
| --Value | String | tagtest | The tag value. |
| -CreationTime | String | 2021-06-15T15:20Z | The time when the VBR connection was established.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC). |
| -Status | String | Attached | The status of the VBR connection. Valid values:<br>• Attached: The VBR connection is created on the transit router.<br>• Attaching: The VBR connection is being created on the transit router.<br>• Detaching: The VBR connection is being deleted from the transit router. |
| -TransitRouterAtt achmentId | String | tr-attach-oyf70wfuorwx87\*\*\*\* | The ID of the VBR connection. |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl\*\*\* \* | The ID of the transit router. |
| -ResourceType | String | VBR | The type of resource to which the transit router is connected. Valid values:<br>The value is <strong>VBR</strong>. |
| -VbrRegionId | String | cn-qingdao-env66-d01 | The region ID of the VBR. |
| -TransitRouterAtt achmentDescript ion | String | testdesc | The description of the VBR connection. |
| -VbrOwnerId | Long | 1250123456123456 | The UID of the level-1 organization to which the VBR belongs. |
| -AutoPublishRout eEnabled | Boolean | false | Indicates whether the transit router is allowed to automatically advertise routes to the VBR. Valid values:<br>• false: (default): no<br>• true: yes |
| -VbrId | String | vbr-bp1svadp4lq38janc\*\* \*\* | The VBR ID. |
| -TransitRouterAtt achmentName | String | testa | The name of the VBR connection. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterVbrAttachments
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"dd20****",
 "RequestId":"F42D9616-29EB-4E75-8CA8-9654D4E07501",
 "MaxResults":20,
 "TransitRouterAttachments":{
  "Status":"Attached",
  "TransitRouterAttachmentId":"tr-attach-oyf70wfuorwx87****",
  "AutoPublishRouteEnabled":false,
  "-Tags":{
   "Value":"tagtest",
   "Key":"tagtest"
  },
  "VbrOwnerId":1250123456123456,
  "CreationTime":"2021-06-15T15:20Z",
  "TransitRouterAttachmentName":"testa",
  "ResourceType":"VBR",
  "VbrRegionId":"cn-qingdao-env66-d01",
  "VbrId":"vbr-bp1svadp4lq38janc****",
  "TransitRouterAttachmentDescription":"testdesc",
  "TransitRouterId":"tr-bp1su1ytdxtataupl****"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>dd20****</NextToken>
<RequestId>F42D9616-29EB-4E75-8CA8-9654D4E07501</RequestId>
<MaxResults>20</MaxResults>
<TransitRouterAttachments>
 <Status>Attached</Status>
 <TransitRouterAttachmentId>tr-attach-oyf70wfuorwx87****</TransitRouterAttachmentId>
 <AutoPublishRouteEnabled>false</AutoPublishRouteEnabled>
 <-Tags>
  <Value>tagtest</Value>
  <Key>tagtest</Key>
 </-Tags>
 <VbrOwnerId>1250123456123456</VbrOwnerId>
 <CreationTime>2021-06-15T15:20Z</CreationTime>
 <TransitRouterAttachmentName>testa</TransitRouterAttachmentName>
 <ResourceType>VBR</ResourceType>
 <VbrRegionId>cn-qingdao-env66-d01</VbrRegionId>
 <VbrId>vbr-bp1svadp4lq38janc****</VbrId>
 <TransitRouterAttachmentDescription>testdesc</TransitRouterAttachmentDescription>
 <TransitRouterId>tr-bp1su1ytdxtataupl****</TransitRouterId>
</TransitRouterAttachments>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstanc e | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | IllegalParam.TransitRo uterId | IllegalParam.TransitRouterId | The specified TransitRouterId is invalid. |
| 400 | IllegalParam.CenId Or RegionId | IllegalParam.CenIdOrRegionId | The specified CenId or RegionId is invalid. |

<a id="section-1-6-3"></a>

### 1.6.3. UpdateTransitRouterVbrAttachmentAttribute

Modifies the name and description of a virtual border router (VBR) connection that is created on a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | UpdateTransitRouterVbrAtta chmentAttribute | The operation that you want to perform. Set the value to UpdateTransitRouterVbr AttachmentAttribute. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-oyf70wfuorwx87\*\*\*\* | The ID of the VBR connection. |
| TransitRout erAttachme ntName | String | Query | No | testname | The new name of the VBR connection.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter. |
| TransitRout erAttachme ntDescriptio n | String | Query | No | testdesc | The new description of the VBR connection.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| AutoPublish RouteEnabl ed | Boolea n | Query | No | true | Specifies whether to allow the transit router to automatically advertise routes to the VBR. Valid values:<br>• true<br>• false |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 91B36DC3-FF8A-45C3-AC1E-456B1789136D | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterVbrAttachmentAttribute
&TransitRouterAttachmentId=tr-attach-oyf70wfuorwx87****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"91B36DC3-FF8A-45C3-AC1E-456B1789136D"
}
```

`XML`  format

```xml
<RequestId>91B36DC3-FF8A-45C3-AC1E-456B1789136D</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterAt tachmentId.NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | IncorrectStatus.Transi tRouterAttachmentId | IncorrectStatus.TransitRouterAttac hment | The status of TransitRouterAttachment is incorrect. |

<a id="section-1-6-4"></a>

### 1.6.4. DeleteTransitRouterVbrAttachment

Deletes a virtual border router (VBR) connection from an Enterprise Edition transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterVbrAtta chment | The operation that you want to perform. Set the value to DeleteTransitRouterVbrA ttachment. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the </em><strong><em>request ID</em></strong> <em>as the </em><strong><em>client token</em></strong><em>.</em><em>The </em><strong><em>request ID</em></strong> <em> may</em> <em>be different for each</em> <em>request.</em> |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-9nlnjv7by7n7a\*\*\*\* | The ID of the VBR connection. |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• false (default): performs a dry run and sends the request.<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the system returns the ID of the request. |
| Force | Boolea n | Query | No | false | Specifies whether to forcefully delete the VBR connection. Valid values:<br>• false (default): checks for resources related to the VBR connection, such as associated forwarding and route learning policies. If such resources exist, the ECR connection is not deleted and an error message is returned.<br>• true: deletes the VBR connection and related resources. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3EDA94DE-0AE5-41FC-A91E-7170E408E0FD | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterVbrAttachment
&TransitRouterAttachmentId=tr-attach-9nlnjv7by7n7a****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"3EDA94DE-0AE5-41FC-A91E-7170E408E0FD"
}
```

`XML`  format

```xml
<RequestId>3EDA94DE-0AE5-41FC-A91E-7170E408E0FD</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationFailed.Route TableAssociationExist | OperationFailed.RouteTableAssocia tionExist | Operation failed because TransitRouterRouteTable exists |
| 400 | OperationFailed.Route EntryExist | OperationFailed.RouteEntryExist | Operation failed because the TransitRouterAttachment exists in RouteTable. |
| 400 | OperationFailed.Route TablePropagationExist | OperationFailed.RouteTablePropag ationExist | The specified TransitRouterAttachment has configured RouteTablePropagation.Please remove the configuration first. |
| 400 | VBR_ATTACHED_VBR_HA | OperationFailed.VbrAttachedVbrHa | The operation is failed because of VbrAttachedVbrHa. |
| 400 | OperationFailed.FlowL ogExistOrNisOpened | OperationFailed.FlowLogExistOrNis Opened | Operation failed because FlowLog exists or Nis opened. |
| 400 | OperationUnsupporte d.TransitRouterType | OperationUnsupported.TransitRout erType | The specified TransitRouterType does not support the operation. |
| 400 | ATTACHMENT_REFERE NCED_BY_VPC_ROUTE _ENTRY | InstanceReferenced.VpcRouteEntry | The specified attachment is referenced by vpc route entry. |

<a id="section-1-7"></a>

## 1.7. Connect attachments

<a id="section-1-7-1"></a>

### 1.7.1. CreateTransitRouterConnectAttachment

Creates a Connect attachment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterConnec tAttachment | The operation that you want to perform. Set the value to CreateTransitRouterCon nectAttachment. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the request. |
| CenId | String | Query | No | cen-a7syd349kne38g\*\*\*\* | The ID of the CEN instance. |
| TransitRout erId | String | Query | No | tr-p0wr9p28r92d598y6\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | No | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| TransitRout erAttachme ntName | String | Query | No | nametest | The name of the Connect attachment.<br>The name must be 2 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter. |
| TransitRout erAttachme ntDescriptio n | String | Query | No | desctest | The description of the Connect attachment.<br>The description must be 2 to 256 characters in length.It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| ResourceId | String | Query | No | vbr-group-iz5egnzmcm7wwv\*\*\*\* | The ID of the resource that is associated with the tunnel.<br><em>This parameter is</em> <em>unavailable. By default,</em> <em>the system transmits</em> <em>data over the VBR</em> <em>connections for the</em> <em>Connect attachment.</em> |
| ResourceO wnerUid | Long | Query | No | 1250123456123456 | The UID of the level-1 organization to which the resource associated with the tunnel belongs.<br><em>This parameter is</em> <em>unavailable. By default,</em> <em>all VBRs attached to</em> <em>the transit routers are</em> <em>connected to the</em> <em>Connect attachment.</em> |
| Protocol | String | Query | No | gre | The protocol that is used to encapsulate data packets in the tunnel. Set the value to gre. |
| TransportTy pe | String | Query | No | AllVbr | The type of the tunnel. Set the value to <strong>AllVbr</strong>, which specifies that all VBRs attached to the transit router are connected to the Connect attachment to transmit data. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterAtt achmentId | String | tr-attach-8b586cj3ugv12r\*\*\*\* | The ID of the Connect attachment. |
| RequestId | String | 8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterConnectAttachment
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TransitRouterAttachmentId":"tr-attach-8b586cj3ugv12r****",
 "RequestId":"8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893"
}
```

`XML`  format

```xml
<TransitRouterAttachmentId>tr-attach-8b586cj3ugv12r****</TransitRouterAttachmentId>
<RequestId>8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893</RequestId>
```

<a id="section-1-7-2"></a>

### 1.7.2. UpdateTransitRouterConnectAttachmentAttribute

Modifies the configurations of a Connect attachment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | UpdateTransitRouterConnec tAttachmentAttribute | The operation that you want to perform. Set the value to UpdateTransitRouterCon nectAttachmentAttribut e. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without sending the actual request.Valid values:<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-8b586cj3ugv12r\*\*\*\* | The ID of the Connect attachment. |
| TransitRout erAttachme ntName | String | Query | No | nametest | The new name of the Connect attachment.<br>The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter. |
| TransitRout erAttachme ntDescriptio n | String | Query | No | desctest | The new description of the Connect attachment.<br>The description must be 2 to 256 characters in length.The description must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0876E54E-3E36-5C31-89F0-9EE8A9266F9A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterConnectAttachmentAttribute
&TransitRouterAttachmentId=tr-attach-8b586cj3ugv12r****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A"
}
```

`XML`  format

```xml
<RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId>
```

<a id="section-1-7-3"></a>

### 1.7.3. ListTransitRouterConnectAttachments

Queries the information about Connect attachments.

**Usage notes**

To query the information about Connect attachments, specify the following parameters:

- To query the information about all Connect attachments in a region, specify the **CenId**

  and

  **RegionId**

  parameters.

- To query the information about all Connect attachments on an Enterprise Edition transit router, specify the **TransitRouterId**

  parameter.

- To query the information about a specific Connect attachment, specify the **TransitRouterAttachmentId**

  parameter.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterConnectAtt achments | The operation that you want to perform. Set the value to ListTransitRouterConnec tAttachments. |
| CenId | String | Query | No | cen-a7syd349kne38g\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| RegionId | String | Query | No | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeRegions operation to query the most recent region list. |
| TransitRout erAttachme ntId | String | Query | No | tr-attach-8b586cj3ugv12r\*\*\*\* | The ID of the Connect attachment. |
| TransitRout erId | String | Query | No | tr-p0wr9p28r92d598y6\*\*\*\* | The ID of the transit router. |
| MaxResults | Integer | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the NextToken parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterAtt achments | Array |  | The information about the Connect attachments. |
| -CreationTime | String | 2022-12-12T07:31Z | The time when the Connect attachment was created.<br>The time follows the ISO8601 standard in the <code> YYYY-MM-DDThh:mmZ </code> format. The time is displayed in UTC. |
| -Status | String | Attached | The status of the Connect attachment. Valid values:<br>• Attaching<br>• Attached<br>• Modifying<br>• Detaching |
| -TransitRouterAtt achmentId | String | tr-attach-8b586cj3ugv12r\*\*\*\* | The ID of the Connect attachment. |
| -TransitRouterId | String | tr-p0wr9p28r92d598y6\* \*\*\* | The ID of the transit router. |
| -ResourceOwnerI d | Long | 1250123456123456 | The UID of the level-1 organization to which the resource associated with the channel belongs. |
| -ResourceType | Integer | Connect | The type of transmission channel.<br>Only <strong>Connect</strong> may be returned, which indicates Connect attachments. |
| -TransitRouterAtt achmentDescript ion | String | desctest | The description of the Connect attachment. |
| -ResourceRegionI d | String | cn-qingdao-env17e-d01 | The region ID of the resource associated with the transmission channel. |
| -ResourceId | String | vbr-group-iz5egnzmcm7wwv\*\*\*\* | The ID of the resource that is associated with the channel. |
| -TransitRouterAtt achmentName | String | nametest | The name of the Connect attachment. |
| -Protocol | String | gre | The protocol that is used to encapsulate data packets in the tunnel. |
| -TransportType | String | AllVbr | The type of the tunnel.<br>Only <strong>AllVbr</strong> may be returned, which indicates that all VBRs attached to the transit router are connected to the Connect attachment to transmit data. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | 0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterConnectAttachments
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50",
 "MaxResults":20,
 "TransitRouterAttachments":{
  "Status":"Attached",
  "TransitRouterAttachmentId":"tr-attach-8b586cj3ugv12r****",
  "ResourceRegionId":"cn-qingdao-env17e-d01",
  "ResourceId":"vbr-group-iz5egnzmcm7wwv****",
  "CreationTime":"2022-12-12T07:31Z",
  "TransitRouterAttachmentName":"nametest",
  "ResourceType":Connect,
  "TransportType":"AllVbr",
  "Protocol":"gre",
  "ResourceOwnerId":1250123456123456,
  "TransitRouterAttachmentDescription":"desctest",
  "TransitRouterId":"tr-p0wr9p28r92d598y6****"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50</RequestId>
<MaxResults>20</MaxResults>
<TransitRouterAttachments>
 <Status>Attached</Status>
 <TransitRouterAttachmentId>tr-attach-8b586cj3ugv12r****</TransitRouterAttachmentId>
 <ResourceRegionId>cn-qingdao-env17e-d01</ResourceRegionId>
 <ResourceId>vbr-group-iz5egnzmcm7wwv****</ResourceId>
 <CreationTime>2022-12-12T07:31Z</CreationTime>
 <TransitRouterAttachmentName>nametest</TransitRouterAttachmentName>
 <ResourceType>Connect</ResourceType>
 <TransportType>AllVbr</TransportType>
 <Protocol>gre</Protocol>
 <ResourceOwnerId>1250123456123456</ResourceOwnerId>
 <TransitRouterAttachmentDescription>desctest</TransitRouterAttachmentDescription>
 <TransitRouterId>tr-p0wr9p28r92d598y6****</TransitRouterId>
</TransitRouterAttachments>
```

<a id="section-1-7-4"></a>

### 1.7.4. CreateTransitRouterConnectPeer

Adds a Connect peer.

**Usage notes**

Before you add a Connect peer to a transit router, make sure that a CIDR block is added to the transit router. For more information, see CreateTransitRouterCidr.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterConnec tPeer | The operation that you want to perform. Set the value to CreateTransitRouterCon nectPeer. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and sends the request. |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-y89r3j7a51xeec\*\*\*\* | The ID of the Connect attachment. |
| TransitRout erConnectP eerName | String | Query | No | nametest | The name of the Connect peer. |
| TransitRout erConnectP eerLocalIp | String | Query | No | 192.168.0.1 | The local address of the transit router. |
| TransitRout erConnectP eerPeerIp | String | Query | Yes | 10.0.0.1 | The IP address of the Connect peer. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterCo nnectPeerId | String | tr-connect-peer-ax66ixf6ubbajw\*\*\*\* | The ID of the Connect peer. |
| RequestId | String | BCF96FD3-17C1-58DA-B9D6-2CC347A71D79 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterConnectPeer
&TransitRouterAttachmentId=tr-attach-y89r3j7a51xeec****
&TransitRouterConnectPeerPeerIp=10.0.0.1
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TransitRouterConnectPeerId":"tr-connect-peer-ax66ixf6ubbajw****",
 "RequestId":"BCF96FD3-17C1-58DA-B9D6-2CC347A71D79"
}
```

`XML`  format

```xml
<TransitRouterConnectPeerId>tr-connect-peer-ax66ixf6ubbajw****</TransitRouterConnectPeerId>
<RequestId>BCF96FD3-17C1-58DA-B9D6-2CC347A71D79</RequestId>
```

<a id="section-1-7-5"></a>

### 1.7.5. ListTransitRouterConnectPeers

Queries the information about a Connect peer.

**Usage notes**

When you call the ListTransitRouterConnectPeers operation, you must specify at least one of the **TransitRouterAttachmentId**

and **TransitRouterConnectPeerId**

parameters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterConnectPe ers | The operation that you want to perform. Set the value to ListTransitRouterConnec tPeers. |
| TransitRout erAttachme ntId | String | Query | No | tr-attach-k4x7usyt7hj719\*\*\*\* | The ID of the Connect attachment. |
| TransitRout erConnectP eerId | String | Query | No | tr-connect-peer-anr505utij7pvr\*\*\*\* | The ID of the Connect peer. |
| MaxResults | Integer | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the NextToken parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterCo nnectPeers | Array |  | The information about the Connect peer. |
| -CreationTime | String | 2022-12-12T07:31Z | The time when the Connect peer was created.<br>The time follows the ISO8601 standard in the <code> YYYY-MM-DDThh:mmZ </code> format. The time is displayed in UTC. |
| -Status | String | Active | The status of the Connect peer. Valid values:<br>• Creating: The Connect peer is being created.<br>• Active: The Connect peer is available.<br>• Deleting: The Connect peer is being deleted. |
| -TransitRouterCo nnectPeerId | String | tr-connect-peer-anr505utij7pvr\*\*\*\* | The ID of the Connect peer. |
| -TransitRouterAtt achmentId | String | tr-attach-k4x7usyt7hj719\*\*\*\* | The ID of the Connect attachment. |
| -TransitRouterCo nnectPeerName | String | nametest | The name of the Connect peer. |
| -TransitRouterId | Long | tr-p0wa3m41xs8806q2n \*\*\*\* | The ID of the transit router. |
| -TransitRouterCo nnectPeerLocalIp | String | 192.168.0.1 | The local address of the transit router. |
| -CenId | String | cen-wc1026dke30j67\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| -TransitRouterCo nnectPeerPeerIp | String | 10.0.0.1 | The IP address of the Connect peer. |
| -TransitRouterRe gionId | String | ap-southeast-2 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegions operation to query the most recent region list. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | 23CC4215-69A5-5635-8249-65AD25B02E91 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page.<br>The value of <strong>MaxResults</strong> indicates the number of entries returned on the current page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterConnectPeers
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"23CC4215-69A5-5635-8249-65AD25B02E91",
 "MaxResults":20,
 "TransitRouterConnectPeers":{
  "Status":"Active",
  "TransitRouterAttachmentId":"tr-attach-k4x7usyt7hj719****",
  "TransitRouterConnectPeerId":"tr-connect-peer-anr505utij7pvr****",
  "TransitRouterConnectPeerName":"nametest",
  "TransitRouterConnectPeerLocalIp":"192.168.0.1",
  "CreationTime":"2022-12-12T07:31Z",
  "CenId":"cen-wc1026dke30j67****",
  "TransitRouterRegionId":"ap-southeast-2",
  "TransitRouterId":tr-p0wa3m41xs8806q2n****,
  "TransitRouterConnectPeerPeerIp":"10.0.0.1"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>23CC4215-69A5-5635-8249-65AD25B02E91</RequestId>
<MaxResults>20</MaxResults>
<TransitRouterConnectPeers>
 <Status>Active</Status>
 <TransitRouterAttachmentId>tr-attach-k4x7usyt7hj719****</TransitRouterAttachmentId>
 <TransitRouterConnectPeerId>tr-connect-peer-anr505utij7pvr****</TransitRouterConnectPeerId>
 <TransitRouterConnectPeerName>nametest</TransitRouterConnectPeerName>
 <TransitRouterConnectPeerLocalIp>192.168.0.1</TransitRouterConnectPeerLocalIp>
 <CreationTime>2022-12-12T07:31Z</CreationTime>
 <CenId>cen-wc1026dke30j67****</CenId>
 <TransitRouterRegionId>ap-southeast-2</TransitRouterRegionId>
 <TransitRouterId>tr-p0wa3m41xs8806q2n****</TransitRouterId>
 <TransitRouterConnectPeerPeerIp>10.0.0.1</TransitRouterConnectPeerPeerIp>
</TransitRouterConnectPeers>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | MissingParam.TrConn ectPeerId Or TrAttachmentId | MissingParam.TrConnectPeerIdOrTr AttachmentId | The parameter TrConnectPeerId Or TrAttachmentId is mandatory. |

<a id="section-1-7-6"></a>

### 1.7.6. DeleteTransitRouterConnectPeer

Deletes a Connect peer.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterConnect Peer | The operation that you want to perform. Set the value to DeleteTransitRouterCon nectPeer. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform a dry run, without performing the actual request. Valid values:<br>• true: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed. |
| TransitRout erConnectP eerId | String | Query | No | tr-connect-peer-y5osf8cbw1d75e\*\*\*\* | The ID of the Connect peer. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterConnectPeer
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893"
}
```

`XML`  format

```xml
<RequestId>8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_MULTICAST_GROUP_E XIST | OperationFailed.MulticastGroupExi st | Operation is failed because connect peer exists in multicast groups. |

<a id="section-1-7-7"></a>

### 1.7.7. DeleteTransitRouterConnectAttachment

Deletes a Connect attachment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterConnect Attachment | The operation that you want to perform. Set the value to DeleteTransitRouterCon nectAttachment. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-42665544\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify</em> <em>this parameter, the</em> <em>system automatically</em> <em>uses the request ID as</em> <em>the client token. The</em> <em>request ID may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boolea n | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code>DryRunOperation</code> error code is returned.<br>• false (default): performs a dry run and performs the actual request. |
| TransitRout erAttachme ntId | String | Query | No | tr-attach-r6g0m3epjehw57\*\*\*\* | The ID of the Connect attachment. |
| Force | Boolea n | Query | No | false | Specifies whether to forcefully delete the Connect attachment. Valid values:<br>• false (default): Check resource dependencies such as Connect peers and multicast groups before deleting the Connect attachment. If a resource dependency exists, the Connect attachment is not deleted and an error message is returned.<br>• true: Delete the Connect attachment and all resource dependencies. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 9878790A-5C16-5A59-A6CB-79B28C04637D | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterConnectAttachment
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"9878790A-5C16-5A59-A6CB-79B28C04637D"
}
```

`XML`  format

```xml
<RequestId>9878790A-5C16-5A59-A6CB-79B28C04637D</RequestId>
```

<a id="section-1-8"></a>

## 1.8. Cross-account authorization

<a id="section-1-8-1"></a>

### 1.8.1. GrantInstanceToTransitRouter

Grants a transit router the permissions to connect to a network instance that belongs to another Alibaba Cloud account.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | GrantInstanceToTransitRoute r | The operation that you want to perform. Set the value to GrantInstanceToTransitRo <strong>uter</strong>. |
| CenId | String | Query | Yes | cen-44m0p68spvlrqq\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance to which the transit router belongs. |
| InstanceId | String | Query | Yes | vpc-bp1h8vbrbcgohcju5\*\*\*\* | The network instance ID. |
| InstanceTyp e | String | Query | Yes | VPC | The type of the network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>ExpressConnect</strong>: virtual border router (VBR) |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The ID of the region where the network instance is deployed.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| CenOwnerId | Long | Query | Yes | 1250123456123456 | The UID of the level-1 organization to which the CEN instance belongs. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RequestId | String | C6E5992C-A57B-5A6C-9B26-568074DC68BA | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=GrantInstanceToTransitRouter
&CenId=cen-44m0p68spvlrqq****
&InstanceId=vpc-bp1h8vbrbcgohcju5****
&InstanceType=VPC
&RegionId=cn-qingdao-env17e-d01
&CenOwnerId=1250123456123456
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"C6E5992C-A57B-5A6C-9B26-568074DC68BA"
}
```

`XML`  format

```xml
<RequestId>C6E5992C-A57B-5A6C-9B26-568074DC68BA</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | USER_NOT_OPEN_TR_SERVICE | Forbbiden.TransitRouterServiceNot Open | The user has not open transit router service. |
| 400 | NoPermission.AliyunS erviceRolePolicyForCE N | NoPermission.AliyunServiceRoleFor CEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForCEN. Service Name: cen.aliyuncs.com. Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
| 400 | IllegalParam.CenInsta nceId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | TaskConflict | OperationFailed.TaskConflict | The operation is too frequent, please wait a moment and try again. |
| 400 | InvalidVbr.NotFound | InvalidVbr.NotFound | vbr is not found. |
| 404 | INSTANCE_NOT_EXIST | InvalidInstanceId.NotFound | InstanceId is not found. |

<a id="section-1-8-2"></a>

### 1.8.2. RevokeInstanceFromTransitRouter

Revokes the permissions that a transit router requires to connect to network instances that belong to another Alibaba Cloud account.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | RevokeInstanceFromTransitR outer | The operation that you want to perform. Set the value to RevokeInstanceFromTran <strong>sitRouter</strong>. |
| CenId | String | Query | Yes | cen-44m0p68spvlrqq\*\*\*\* | The ID of the CEN instance to which the transit router belongs. |
| InstanceId | String | Query | Yes | vpc-bp1h8vbrbcgohcju5\*\*\*\* | The network instance ID. |
| InstanceTyp e | String | Query | Yes | VPC | The type of the network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>ExpressConnect</strong>: virtual border router (VBR) |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The ID of the region where the network instance is deployed.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| CenOwnerId | Long | Query | Yes | 1250123456123456 | The UID of the level-1 organization to which the Cloud Enterprise Network (CEN) instance belongs. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RequestId | String | AA4BFFD1-5090-5896-935F-4B353557F1A8 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=RevokeInstanceFromTransitRouter
&CenId=cen-44m0p68spvlrqq****
&InstanceId=vpc-bp1h8vbrbcgohcju5****
&InstanceType=VPC
&RegionId=cn-qingdao-env17e-d01
&CenOwnerId=1250123456123456
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"AA4BFFD1-5090-5896-935F-4B353557F1A8"
}
```

`XML`  format

```xml
<RequestId>AA4BFFD1-5090-5896-935F-4B353557F1A8</RequestId>
```

<a id="section-1-8-3"></a>

### 1.8.3. DescribeGrantRulesToCen

Queries the network instances within a different Alibaba Cloud account that Cloud Enterprise Network (CEN) has the permissions to access.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeGrantRulesToCen | The operation that you want to perform. Set the value to DescribeGrantRulesToCen. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the network instance.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| CenId | String | Query | Yes | cen-nye53d7p3hzyu4\*\*\*\* | The ID of the CEN instance. |
| ProductType | String | Query | Yes | VPC | The type of network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| MaxResults | Long | Query | No | 20 | • If you do not set <strong>MaxResults</strong>, it indicates that you do not need to query results in batches.The value of <strong>MaxResults</strong> in the response indicates the total number of entries returned.<br>• If you specify a value for <strong>MaxResults</strong>, it indicates that you need to query results in batches. The value of <strong>MaxResults</strong> indicates the number of entries to return in each batch. Valid values: <strong>1</strong> to<br><strong>100</strong>. The value of <strong>MaxResults</strong> in the response indicates the number of entries in the current batch. We recommend that you set <strong>MaxResults</strong> to <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGK Pd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the <strong>NextToken</strong> parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| GrantRules | Array |  | The permissions that are granted to the CEN instance. |
| -ChildInstanceTyp e | String | VPC | The type of network instance. Valid values:<br>• <strong>VPC</strong>: VPC<br>• <strong>VBR</strong>: VBR |
| -ChildInstanceRe gionId | String | cn-qingdao-env17e-d01 | The region ID of the network instance. |
| -ChildInstanceOw nerId | Long | 1250123456123456 | The UID of the level-1 organization to which the network instance belongs. |
| -ChildInstanceId | String | vpc-bp1rgeww9mdstuuar\* \*\*\* | The ID of the network instance. |
| -CenId | String | cen-nye53d7p3hzyu4\*\*\*\* | The ID of the CEN instance. |
| -CenOwnerId | Long | 1210123456123456 | The UID of the level-1 organization to which the CEN instance belongs. |
| RequestId | String | 4906B209-8613-5C19-9CC9-B7A3FFDA731C | The request ID. |
| TotalCount | Long | 1 | The total number of entries returned. |
| MaxResults | Long | 20 | • If no value is specified for <strong>MaxResults</strong>, query results are returned in one batch. The value of <strong>MaxResults</strong> indicates the total number of entries.<br>• If a value is specified for <strong>MaxResults</strong>, query results are returned in batches. The value of <strong>MaxResults</strong> in the response indicates the number of entries in the current batch. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If a value is returned for <strong>NextToken</strong>, the value indicates the token that is used for the next request to retrieve a new page of results. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeGrantRulesToCen
&RegionId=cn-qingdao-env17e-d01
&CenId=cen-nye53d7p3hzyu4****
&ProductType=VPC
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "RequestId":"4906B209-8613-5C19-9CC9-B7A3FFDA731C",
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "MaxResults":20,
 "GrantRules":{
  "ChildInstanceType":"VPC",
  "OrderType":"",
  "CenOwnerId":1210123456123456,
  "CenId":"cen-nye53d7p3hzyu4****",
  "ChildInstanceOwnerId":1250123456123456,
  "ChildInstanceId":"vpc-bp1rgeww9mdstuuar****",
  "ChildInstanceRegionId":"cn-qingdao-env17e-d01"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<RequestId>4906B209-8613-5C19-9CC9-B7A3FFDA731C</RequestId>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<MaxResults>20</MaxResults>
<GrantRules>
 <ChildInstanceType>VPC</ChildInstanceType>
 <OrderType  />
 <CenOwnerId>1210123456123456</CenOwnerId>
 <CenId>cen-nye53d7p3hzyu4****</CenId>
 <ChildInstanceOwnerId>1250123456123456</ChildInstanceOwnerId>
 <ChildInstanceId>vpc-bp1rgeww9mdstuuar****</ChildInstanceId>
 <ChildInstanceRegionId>cn-qingdao-env17e-d01</ChildInstanceRegionId>
</GrantRules>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | MissingParameter | MissingParameter | Missing parameter. |
| 400 | SDK.InvalidRegionId : Can not find endpoint to access. | InvalidParameter.RegionId | The specified Region Id is invalid. |

<a id="section-1-8-4"></a>

### 1.8.4. DescribeGrantRulesToResource

Queries permissions granted to Cloud Enterprise Network (CEN) instances that belong to another Alibaba Cloud account.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeGrantRulesToResou rce | The operation that you want to perform. Set the value to DescribeGrantRulesToRe source. |
| RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the network instance.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| ResourceId | String | Query | Yes | vpc-p0wfut1iqauelpdpb\*\*\*\* | The ID of the network instance. |
| ProductTyp e | String | Query | Yes | VPC | The type of network instance. Valid values:<br>• VPC: virtual private cloud (VPC)<br>• ExpressConnect: virtual border router (VBR) |
| MaxResults | Integer | Query | No | 20 | • If you do not set MaxResults, it indicates that you do not need to query results in batches. The value of MaxResults indicates the total number of entries.<br>• If you specify a value for MaxResults, it indicates that you need to query results in batches. The value of MaxResults indicates the number of entries to return in each batch.Valid values: <strong>1</strong> to 100. The value of MaxResults in the response indicates the number of entries in the current batch. We recommend that you set MaxResults to <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the NextToken parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| GrantRules | Array |  | The permissions that are granted to the CEN instance. |
| -CenOwnerId | Long | 1250123456123456 | The UID of the level-1 organization to which the CEN instance belongs. |
| -CenId | String | cen-44m0p68spvlrqq\*\*\*\* | The ID of the CEN instance. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | C6E5992C-A57B-5A6C-9B26-568074DC68BA | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 1 | • If no value is specified for <strong>MaxResults</strong>, query results are returned in one batch. The value of <strong>MaxResults</strong> indicates the total number of entries.<br>• If a value is specified for <strong>MaxResults</strong>, query results are returned in batches. The value of <strong>MaxResults</strong> in the response indicates the number of entries in the current batch. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeGrantRulesToResource
&RegionId=cn-qingdao-env17e-d01
&ResourceId=vpc-p0wfut1iqauelpdpb****
&ProductType=VPC
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"C6E5992C-A57B-5A6C-9B26-568074DC68BA",
 "MaxResults":1,
 "GrantRules":{
  "CenOwnerId":1250123456123456,
  "CenId":"cen-44m0p68spvlrqq****"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>C6E5992C-A57B-5A6C-9B26-568074DC68BA</RequestId>
<MaxResults>1</MaxResults>
<GrantRules>
 <CenOwnerId>1250123456123456</CenOwnerId>
 <CenId>cen-44m0p68spvlrqq****</CenId>
</GrantRules>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | MissingParameter | MissingParameter | Missing parameter. |
| 400 | SDK.InvalidRegionId : Can not find endpoint to access. | InvalidParameter.RegionId | The specified Region Id is invalid. |

<a id="section-1-9"></a>

## 1.9. Custom routes

<a id="section-1-9-1"></a>

### 1.9.1. CreateTransitRouterRouteEntry

Adds a route to a route table of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterRouteEnt ry | The operation that you want to perform. Set the value to CreateTransitRouterRoute <strong>Entry</strong>. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| TransitRoute rRouteEntry Name | String | Query | No | testname | The name of the route.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. |
| TransitRoute rRouteEntry Description | String | Query | No | testdesc | The description of the route.<br>The description must be 2 to 256 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. You can also leave the description empty. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |

<table>
  <tr>
    <td>TransitRoute rRouteEntry NextHopTyp e</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>BlackHole</td>
    <td>The next hop type. Valid values:<br>• <strong>BlackHole</strong>: routes network traffic to a black hole. All packets that match this route are dropped. If you select this option, you do not need to specify the next hop information.<br>• <strong>Attachment</strong>: routes network traffic to a network instance connection. If you select this option, you must specify the ID of the network instance connection. All packets that match this route are routed to the specified network instance connection.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntry DestinationC idrBlock</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>192.168.0.0/24</td>
    <td>The destination CIDR block of the route.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntry NextHopId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>tr-attach-nls9fzkfat8934****</td>
    <td>The ID of the network instance connection that you want to specify as the next hop.</td>
  </tr>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterRo uteEntryId | String | rte-75eg4jprkvk0pw\*\*\*\* | The route ID. |
| RequestId | String | 835E7F4B-B380-4E0F-96A5-6EA572388047 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterRouteEntry
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&TransitRouterRouteEntryNextHopType=BlackHole
&TransitRouterRouteEntryDestinationCidrBlock=192.168.0.0/24
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"835E7F4B-B380-4E0F-96A5-6EA572388047",
 "TransitRouterRouteEntryId":"rte-75eg4jprkvk0pw****"
}
```

`XML`  format

```xml
<RequestId>835E7F4B-B380-4E0F-96A5-6EA572388047</RequestId>
<TransitRouterRouteEntryId>rte-75eg4jprkvk0pw****</TransitRouterRouteEntryId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | InvalidTransitRouterR outeTableId.NotFound | InvalidTransitRouterRouteTableId.N otFound | TransitRouterRouteTableId is not found. |
| 400 | TransitRouterRouteEn tryNextHopId.NotFoun d | TransitRouterRouteEntryNextHopId.NotFound | TransitRouterRouteEntryNextHopId is not found. |
| 400 | OperationFailed.Creat eRouteEntryWithCCN Attachment | OperationFailed.CreateRouteEntry WithCCNAttachment | Operation failed because Create RouteEntry to CCN Attachment does not support. |
| 400 | QuotaExceeded.Transi tRouterRoutEntry | QuotaExceeded.TransitRouterRout Entry | TransitRouterRoutEntry quota exceeded. |
| 400 | IllegalParam.TransitRo uterDestinationCidrBl ock | IllegalParam.TransitRouterDestinati onCidrBlock | TransitRouterDestinationCidrBlock is illegal. |
| 400 | InstanceExist.TransitR outerRouteEntry | InstanceExist.TransitRouterRouteE ntry | The instance TransitRouterRouteEntry already exists. |
| 400 | IncorrectStatus.Transi tRouterRouteTable | IncorrectStatus.TransitRouterRoute Table | TransitRouterRouteTable status is invalid. |
| 400 | ParamExclusive.Route EntryIdAndRouteTable IdOrDestCidrBlock | ParamExclusive.RouteEntryIdAndTr ansitRouterRouteTableIdOrDestCid rBlock | RouteEntryId and TransitRouterRouteTableIdOrDestC idrBlock is mutually exclusive. |
| 400 | InvalidDescription | InvalidDescription | Description is invalid. |
| 400 | InvalidName | InvalidName | Name is invalid. |
| 400 | IllegalParam.NextHop Type | IllegalParam.NextHopType | The NextHopType is illegal. |
| 400 | MissingParam.Transit RouterRouteEntryNext HopId | MissingParam.TransitRouterRouteE ntryNextHopId | The parameter TransitRouterRouteEntryNextHopId is mandatory |
| 400 | InvalidTransitRouterR outeEntryNextHopId.N otFound | InvalidTransitRouterRouteEntryNex tHopId.NotFound | TransitRouterRouteEntryNextHopId is not found |
| 400 | ROUTE_CONFLICT | OperationFailed.CreateRouteEntry WithSameDestinationCidrBlock | Operation failed because Create RouteEntry with same destination cidrblock does not support. |
| 400 | InvalidDestinationCidr Block.NotFound | InvalidDestinationCidrBlock.NotFou nd | DestinationCidrBlock is not found. |

<a id="section-1-9-2"></a>

### 1.9.2. UpdateTransitRouterRouteEntry

Modifies the name and description of a route that belongs to a route table of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | UpdateTransitRouterRouteEn try | The operation that you want to perform. Set the value to UpdateTransitRouterRout <strong>eEntry</strong>. |
| TransitRoute rRouteEntryI d | String | Query | Yes | rte-ksssq7kto4wfdx\*\*\*\* | The route ID. |
| TransitRoute rRouteEntry Name | String | Query | No | testname | The new name of the route.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. |
| TransitRoute rRouteEntry Description | String | Query | No | testdesc | The new description of the route.<br>The description must be 2 to 256 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. You can also leave the description empty. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and sends the request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RequestId | String | 2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterRouteEntry
&TransitRouterRouteEntryId=rte-ksssq7kto4wfdx****
&Action=UpdateTransitRouterRouteEntry
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E"
}
```

`XML`  format

```xml
<RequestId>2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterR outeEntryId.NotFound | IllegalParam.TransitRouterRouteEn tryId | TransitRouterRouteEntryId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | InvalidName | InvalidName | Name is invalid. |
| 400 | InvalidDescription | InvalidDescription | Description is invalid. |

<a id="section-1-9-3"></a>

### 1.9.3. ListTransitRouterRouteEntries

Queries the information about routes that belong to a route table of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListTransitRouterRouteEntrie s | The operation that you want to perform. Set the value to ListTransitRouterRouteEn <strong>tries</strong>. |
| MaxResults | Integ er | Query | No | 20 | The number of entries per page. Valid values: <strong>1</strong> to <strong>100</strong>.Default value: <strong>20</strong>. |
| TransitRoute rRouteEntry DestinationC idrBlock | String | Query | No | 192.168.0.0/24 | The destination CIDR block of the route. <strong>This parameter</strong> is to be deprecated. We recommend that you use the RouteFilter <strong>parameter</strong>. |
| TransitRoute rRouteEntry Status | String | Query | No | Active | The route status. Valid values:<br>• <strong>All</strong>: all routes<br>• <strong>Active</strong> (default): available routes<br>• <strong>Rejected</strong>: rejected routes<br>• <strong>Prohibited</strong>: prohibited routes<br>• <strong>Standby</strong>: standby routes<br>• <strong>Candidate</strong>: candidate routes<br>If you do not specify a value, routes in the Active state are queried. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| NextToken | String | Query | No | fce19\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the <strong>NextToken</strong> parameter. |
| TransitRoute rRouteEntry Names | Repea tList | Query | No | testname | The name of the route.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -.<br><em>You can use this</em> <em>parameter to query only</em> <em>static routes in the</em> <em>specified route table.</em><em>This parameter conflicts</em> <em>with other query</em> <em>conditions except for</em> <em>TransitRouterRouteEntry</em> <em>Ids.</em> |
| TransitRoute rRouteEntryI ds | Repea tList | Query | No | rte-oklkgwmj97z6dn\*\*\*\* | The route ID.<br><em>You can use this</em> <em>parameter to query only</em> <em>static routes in the</em> <em>specified route table.</em><em>This parameter conflicts</em> <em>with other query</em> <em>conditions except for</em> <em>TransitRouterRouteEntry</em> <em>Names.</em> |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterRo uteEntries | Array |  | A list of routes. |
| -TransitRouterRo uteEntryId | String | rte-oklkgwmj97z6dn\*\*\*\* | The route ID.<br><em>This parameter is returned only for static</em> <em>routes.</em> |
| -TransitRouterRo uteEntryDestinat ionCidrBlock | String | 192.168.0.0/24 | The destination CIDR block of the route. |
| -TransitRouterRo uteEntryType | String | Static | The type of the route. Valid values:<br>• <strong>Static</strong>: static route.<br>• <strong>Propagated</strong>: route automatically learned by the route table. |
| -CreateTime | String | 2021-06-15T07:01Z | The time when the route was created.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC).<br><em>This parameter is returned only for static</em> <em>routes.</em> |
| -TransitRouterRo uteEntryName | String | testname | The name of the route.<br><em>This parameter is returned only for static</em> <em>routes.</em> |
| -TransitRouterRo uteEntryStatus | String | Active | The route status. Valid values:<br>• <strong>Active</strong>: Available route.<br>• <strong>Rejected</strong>: Rejected route.<br>• <strong>Prohibited</strong>: Prohibited route.<br>• <strong>Standby</strong>: Standby route.<br>• <strong>Candidate</strong>: Candidate route.<br>• <strong>Creating</strong>: The route is being added.<br>• <strong>Deleting</strong>: The route is being deleted. |
| -TransitRouterRo uteEntryNextHop Type | String | BlackHole | The next hop type. Valid values:<br>• <strong>BlackHole</strong>: a blackhole route. Packets destined for the destination CIDR block of the route are dropped.<br>• <strong>Attachment</strong>: a network instance connection.Packets destined for the destination CIDR block of the route are forwarded to the specified network instance connection. |
| -TransitRouterRo uteEntryNextHop Id | String | tr-attach-vx6iwhjr1x1j78\*\*\*\* | The next hop ID. This parameter is not returned if the route is a blackhole route. |
| -TransitRouterRo uteEntryDescript ion | String | CidrRoute | The description of the route.<br><em>This parameter is returned only for static</em> <em>routes.</em> |
| -OperationalMode | Boolean | false | Indicates whether the route can be managed.Valid values:<br>• <strong>true</strong>: The route can be managed. You can delete the route.<br>• <strong>false</strong>: The route cannot be managed because it is automatically generated by the system. |
| -Tag | String | PermitVbr | The route tag.<br>Valid value: <strong>PermitVbr</strong>, which indicates that the route is advertised only to the route table of the virtual border router (VBR) that is connected to the transit router.<br><em>This parameter is returned only for routes</em> <em>that are automatically generated by the</em> <em>system and use IP addresses from the CIDR</em> <em>block of the transit router.</em> |
| NextToken | String | fce19\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | C3835E5E-1504-4344-B1BB-98A4110F1079 | The request ID. |
| TotalCount | Integer | 6 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterRouteEntries
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":6,
 "NextToken":"fce19****",
 "RequestId":"C3835E5E-1504-4344-B1BB-98A4110F1079",
 "MaxResults":20,
 "TransitRouterRouteEntries":{
  "TransitRouterRouteEntryDestinationCidrBlock":"192.168.0.0/24",
  "TransitRouterRouteEntryNextHopId":"tr-attach-vx6iwhjr1x1j78****",
  "TransitRouterRouteEntryType":"Static",
  "TransitRouterRouteEntryDescription":"CidrRoute",
  "CreateTime":"2021-06-15T07:01Z",
  "TransitRouterRouteEntryNextHopType":"BlackHole",
  "TransitRouterRouteEntryName":"testname",
  "Tag":"PermitVbr",
  "OperationalMode":false,
  "TransitRouterRouteEntryId":"rte-oklkgwmj97z6dn****",
  "TransitRouterRouteEntryStatus":"Active"
 }
}
```

`XML`  format

```xml
<TotalCount>6</TotalCount>
<NextToken>fce19****</NextToken>
<RequestId>C3835E5E-1504-4344-B1BB-98A4110F1079</RequestId>
<MaxResults>20</MaxResults>
<TransitRouterRouteEntries>
 
<TransitRouterRouteEntryDestinationCidrBlock>192.168.0.0/24</TransitRouterRouteEntryDestinationCidrB
k>
 <TransitRouterRouteEntryNextHopId>tr-attach-vx6iwhjr1x1j78****</TransitRouterRouteEntryNextHopId>
 <TransitRouterRouteEntryType>Static</TransitRouterRouteEntryType>
 <TransitRouterRouteEntryDescription>CidrRoute</TransitRouterRouteEntryDescription>
 <CreateTime>2021-06-15T07:01Z</CreateTime>
 <TransitRouterRouteEntryNextHopType>BlackHole</TransitRouterRouteEntryNextHopType>
 <TransitRouterRouteEntryName>testname</TransitRouterRouteEntryName>
 <Tag>PermitVbr</Tag>
 <OperationalMode>false</OperationalMode>
 <TransitRouterRouteEntryId>rte-oklkgwmj97z6dn****</TransitRouterRouteEntryId>
 <TransitRouterRouteEntryStatus>Active</TransitRouterRouteEntryStatus>
</TransitRouterRouteEntries>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.TransitRo uterRouteTableId | IllegalParam.TransitRouterRouteTa bleId | TransitRouterRouteTableId is illegal. |
| 400 | IllegalParam.TransitRo uterRouteEntryStatus | IllegalParam.TransitRouterRouteEn tryStatus | TransitRouterRouteEntryStatus is illegal. |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | NextToken is illegal. |
| 400 | ParamExclusive.Transi tRouterRouteEntryIds AndTransitRouterRout eEntryStatus | ParamExclusive.RouteEntryIdsAnd Status | TransitRouterRouteEntryIds and TransitRouterRouteEntryStatus is mutually exclusive. |
| 400 | InvalidTransitRouterR outeTableId.NotFound | InvalidTransitRouterRouteTableId.N otFound | TransitRouterRouteTableId is not found. |
| 404 | ROUTE_TABLE_NOT_F OUND | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |

<a id="section-1-9-4"></a>

### 1.9.4. DeleteTransitRouterRouteEntry

Deletes a static route from a route table of a transit router.

**Usage notes**

You can call this operation to delete only static routes. Automatically learned routes are not supported. You can call the ListTransitRouterRouteEntries operation to query route types.

Before you call this operation, take note of the following items:

- If **TransitRouterRouteEntryId** is set, you must not set **TransitRouterRouteTableId** or **TransitRouterRouteEntryDestinationCidrBlock**. Otherwise, parameter conflicts will occur.

- If **TransitRouterRouteEntryId** is not set, you must set the following parameters based on the type of the next hop:

  - To delete a blackhole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, and **TransitRouterRouteEntryNextHopType**.

  - If the route that you want to delete is not a blackhole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, **TransitRouterRouteEntryNextHopType**, and **TransitRouterRouteEntryNextHopId**.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterRouteEnt ry | The operation that you want to perform. Set the value to DeleteTransitRouterRoute <strong>Entry</strong>. |

<table>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>02fb3da4-130e-11e9-8e44-001****</td>
    <td>The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em></td>
  </tr>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. If the request passes the dry run, the route is deleted.<br>• <strong>true</strong>: performs only a dry run. The route is not deleted after the request passes the dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntryI d</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>rte-75eg4jprkvk0pw****</td>
    <td>The route ID.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntry NextHopTyp e</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>BlackHole</td>
    <td>The next hop type. Valid values:<br>• <strong>BlackHole</strong>: a blackhole route. You do not need to specify a next hop.<br>• <strong>Attachment</strong>: a network instance connection. You must specify a network instance connection as the next hop.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntry DestinationC idrBlock</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>192.168.0.0/24</td>
    <td>The destination CIDR block.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteEntry NextHopId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>tr-attach-nls9fzkfat8934****</td>
    <td>The ID of the network instance connection that you want to specify as the next hop.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteTableI d</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-bp1dudbh2d5na6b50****</td>
    <td>The ID of the route table of the transit router.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterRouteEntry
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E"
}
```

`XML`  format

```xml
<RequestId>2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | InvalidTransitRouterR outeEntryId.NotFound | IllegalParam.TransitRouterRouteEn tryId | TransitRouterRouteEntryId is not found. |
| 400 | ParamExclusive.Route EntryIdAndTransitRou terRouteTableIdOrDes tCidrBlock | ParamExclusive.RouteEntryIdAndR outeTableIdOrDestCidrBlock | RouteEntryId and TransitRouterRouteTableIdOrDestC idrBlock is mutually exclusive. |
| 400 | InvalidTransitRouterR outeEntry.NotFound | IllegalParam.TransitRouterRouteEn tryId | TransitRouterRouteEntryId is not found. |

<a id="section-1-10"></a>

## 1.10. Routing

<a id="section-1-10-1"></a>

### 1.10.1. ListCenChildInstanceRouteEntriesToAttachment

Queries routes in route tables of network instances that point to network instance connections.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListCenChildInstanceRouteE ntriesToAttachment | The operation that you want to perform. Set the value to ListCenChildInstanceRou teEntriesToAttachment. |
| MaxResults | Integer | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first query and no subsequent queries are to be sent, ignore this parameter.<br>• If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results. |
| CenId | String | Query | No | cen-dc4vwznpwbobrl\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| ChildInstanc eRouteTabl eId | String | Query | Yes | vtb-bp174d1gje79u1g4t\*\*\*\* | The ID of the route table of the network instance. |
| TransitRout erAttachme ntId | String | Query | Yes | tr-attach-r6g0m3epjehw57\*\*\*\* | The ID of the network instance connection. |
| ServiceType | String | Query | No | TR | Specifies whether the route is hosted. If the parameter is empty, the route is not hosted. A value of TR indicates that the route is hosted on a transit router. |
| RouteFilter | Repeat List | Query | No |  | The filter condition for the destination CIDR block. |
| -Key | String |  | No | prefix-exact-match | The match mode of the route. Set the value to prefix-exact-match, which specifies exact match. |
| -Value | Repeat List |  | No | 10.0.0.0/8 | The destination CIDR blocks. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RouteEntry | Array |  | Detailed information about the route. |
| -CenId | String | cen-9adwg6ghpq8oq4dp7 q | The ID of the CEN instance. |
| -TransitRouterAtt achmentId | String | tr-attach-y463sghkkv1loe\*\*\*\* | The ID of the network instance connection. |
| -Status | String | Available | The route status. Valid values:<br>• Available: The route is available.<br>• Pending: The route is being configured.<br>• Modifying: the route is being modified. |
| -ServiceType | String | TR | Indicates whether the route is hosted. If the parameter is empty, the route is not hosted. A value of TR indicates that the route is hosted on a transit router. |
| -DestinationCidrB lock | String | 10.0.0.0/8 | The destination CIDR block of the route. |
| -ChildInstanceRo uteTableId | String | vtb-bp1tlaj1c4nxr2t3e\*\*\*\* | The ID of the route table of the network instance. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | 530BC816-F575-412A-AAB2-435125D26328 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListCenChildInstanceRouteEntriesToAttachment
&ChildInstanceRouteTableId=vtb-bp174d1gje79u1g4t****
&TransitRouterAttachmentId=tr-attach-r6g0m3epjehw57****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RouteEntry":{
  "TransitRouterAttachmentId":"tr-attach-y463sghkkv1loe****",
  "Status":"Available",
  "ServiceType":"TR",
  "CenId":"cen-9adwg6ghpq8oq4dp7q",
  "DestinationCidrBlock":"10.0.0.0/8",
  "ChildInstanceRouteTableId":"vtb-bp1tlaj1c4nxr2t3e****"
 },
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"530BC816-F575-412A-AAB2-435125D26328"
}
```

`XML`  format

```xml
<RouteEntry>
 <TransitRouterAttachmentId>tr-attach-y463sghkkv1loe****</TransitRouterAttachmentId>
 <Status>Available</Status>
 <ServiceType>TR</ServiceType>
 <CenId>cen-9adwg6ghpq8oq4dp7q</CenId>
 <DestinationCidrBlock>10.0.0.0/8</DestinationCidrBlock>
 <ChildInstanceRouteTableId>vtb-bp1tlaj1c4nxr2t3e****</ChildInstanceRouteTableId>
</RouteEntry>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>530BC816-F575-412A-AAB2-435125D26328</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The parameter NextToken is invalid. |
| 400 | MissingParameter.Tra nsitRouterAttachment Id | MissingParam.TransitRouterAttach mentId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | MissingParameter.Chil dInstanceRouteTableI d | MissingParam.ChildInstanceRouteT ableId | The parameter ChildInstanceRouteTableId is Missing. |
| 400 | MissingParam.Transit RouterAttachmentId | MissingParam.TransitRouterAttach mentId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | MissingParam.ChildIns tanceRouteTableId | MissingParam.ChildInstanceRouteT ableId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | InvalidParameter | InvalidParam.RouteFilter | The parameter RouteFilter is invalid. |
| 400 | InvalidTrAttachment.N otFound | ResourceNotFound.TransitRouterAt tachment | The specified TransitRouterAttachment does not exist. |
| 400 | INVALID_ROUTE_FILTE R_KEY | InvalidParam.RoutFilterKey | The specified Key of RouteFilter is invalid. |
| 400 | PARAMETER_CBN_INS TANCE_ID | InvalidParam.CenId | The specified CEN does not exist. |
| 400 | INVALID_OPERATION_CBN_INSTANCE_STAT US | OperationFailed.CenInstanceStatus | The CEN instance is not in a valid state for the operation. |
| 400 | ATTACHMENT_NOT_F OUND | ResourceNotFound.TransitRouterAt tachment | The specified TransitRouterAttachment does not exist. |

<a id="section-1-10-2"></a>

### 1.10.2. DescribeRouteConflict

Queries overlapping routes of a network instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeRouteConflict | The operation that you want to perform. Set the value to <strong>DescribeRouteConflict</strong>. |
| PageNumber | Integ er | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: <strong>10</strong>. Valid values: <strong>1</strong> to <strong>50</strong>. |
| ChildInstanc eId | String | Query | Yes | vpc-rj9gt5nll27onu\*\*\*\* | The ID of the network instance that you want to query. |
| ChildInstanc eType | String | Query | Yes | VPC | The type of the network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| ChildInstanc eRegionId | String | Query | Yes | cn-qingdao-env66-d01 | The ID of the region where the network instance is deployed.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| ChildInstanc eRouteTable Id | String | Query | Yes | vtb-bp174d1gje79u1g4t\*\*\*\* | The ID of the route table that you want to query. |
| DestinationC idrBlock | String | Query | No | 172.16.0.0/16 | The destination CIDR block of the overlapping route. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RouteConflicts | Array |  | A list of overlapping routes. |
| -DestinationCidrB lock | String | 172.16.0.0/16 | The destination CIDR block of the overlapping route. |
| -RegionId | String | cn-qingdao-env66-d01 | The region ID of the peer network instance on which the overlapping routes are found. |
| -InstanceId | String | vpc-rj9gt5nll27onu\*\*\*\* | The ID of the peer network instance on which the overlapping routes are found. |
| -InstanceType | String | VPC | The type of the peer network instance on which the conflicting routes are found. Valid values:<br>• VPC<br>• VBR |
| -Status | String | conflict | The cause of overlapping routes. Valid values:<br>• <strong>conflict</strong>: Routes have the same destination CIDR block.<br>• <strong>overflow</strong>: The number of routes in the route table configured on another network instance has reached the upper limit. |
| RequestId | String | EE3A2CC7-41F1-58DB-8306-CFC99D9C747B | The request ID. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeRouteConflict
&ChildInstanceId=vpc-rj9gt5nll27onu****
&ChildInstanceType=VPC
&ChildInstanceRegionId=cn-qingdao-env66-d01
&ChildInstanceRouteTableId=vtb-bp174d1gje79u1g4t****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"EE3A2CC7-41F1-58DB-8306-CFC99D9C747B",
 "PageNumber":1,
 "RouteConflicts":{
  "Status":"conflict",
  "InstanceId":"vpc-rj9gt5nll27onu****",
  "DestinationCidrBlock":"172.16.0.0/16",
  "RegionId":"cn-qingdao-env66-d01",
  "InstanceType":"VPC"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<PageSize>10</PageSize>
<RequestId>EE3A2CC7-41F1-58DB-8306-CFC99D9C747B</RequestId>
<PageNumber>1</PageNumber>
<RouteConflicts>
 <Status>conflict</Status>
 <InstanceId>vpc-rj9gt5nll27onu****</InstanceId>
 <DestinationCidrBlock>172.16.0.0/16</DestinationCidrBlock>
 <RegionId>cn-qingdao-env66-d01</RegionId>
 <InstanceType>VPC</InstanceType>
</RouteConflicts>
```

<a id="section-1-10-3"></a>

### 1.10.3. DescribeCenRegionDomainRouteEntries

Queries the routes of a Cloud Enterprise Network (CEN) instance in a region.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenRegionDomainR outeEntries | The operation that you want to perform. Set the value to DescribeCenRegionDomai <strong>nRouteEntries</strong>. |
| CenId | String | Query | Yes | cen-7qthudw0ll6j\*\*\*\* | The ID of the CEN instance. |
| CenRegionId | String | Query | Yes | cn-qingdao-env66-d01 | The region ID.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| PageNumber | Integ er | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: <strong>10</strong>. Valid values: <strong>1</strong> to <strong>50</strong>. |

<table>
  <tr>
    <td>Status</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>Active</td>
    <td>The route status. Valid values:<br>• <strong>Active</strong> (default): available routes<br>• <strong>Candidate</strong>: candidate routes<br>• <strong>Standby</strong>: standby routes<br>• <strong>Rejected</strong>: rejected routes<br>• <strong>Prohibited</strong>: prohibited routes<br>• <strong>All</strong> (default value): all routes in the current region</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CenRouteEntries | Array |  | A list of routes. |
| -AsPaths | Normal | 65501 | The AS path of the route. |
| -Communities | Normal | 65501:1 | The community attributes of the route. |
| -CenRouteMapRe cords | Array |  | The routing policy that the route matches in the inbound direction. |
| --RegionId | String | cn-qingdao-env66-d01 | The region ID of the routing policy. |
| --RouteMapId | String | cenrmap-dbarzidzp7ek4k\*\*\*\* | The routing policy ID. |
| -CenOutRouteMa pRecords | Array |  | The routing policy that the route matches in the outbound direction. |
| --RegionId | String | cn-qingdao-env66-d01 | The region ID of the routing policy. |
| --RouteMapId | String | cenrmap-dbarzidzp7ek4k\*\*\*\* | The routing policy ID. |
| -DestinationCidrB lock | String | 192.168.1.0/24 | The destination CIDR block of the route. |
| -Type | String | CEN | The route type. Valid values:<br>• <strong>CEN</strong>: the route that is advertised by CEN<br>• <strong>Custom</strong>: a custom route<br>• <strong>System</strong>: a system route |
| -NextHopInstance Id | String | vpc-bp1j8728mm6pweeod \*\*\*\* | The ID of the instance specified as the next hop in the route. |
| -NextHopType | String | VPC | The type of the instance specified as the next hop in the route. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC).<br>• <strong>VBR</strong>: virtual border router (VBR).<br>• <strong>local_service</strong>: No next hop is specified because the route is a system route. |
| -NextHopRegionI d | String | cn-qingdao-env66-d01 | The ID of the region where the network instance that is specified as the next hop in the route resides. |
| -Status | String | Active | The route status. Valid values:<br>• <strong>Active</strong>: available routes<br>• <strong>Candidate</strong>: candidate routes<br>• <strong>Standby</strong>: standby routes<br>• <strong>Rejected</strong>: rejected routes<br>• <strong>Prohibited</strong>: prohibited routes |
| -ToOtherRegionSt atus | String | Active | Indicates whether the route can be advertised to other regions. Valid values:<br>• <strong>Active</strong>: The route can be advertised to other regions.<br>• <strong>Prohibited</strong>: The route cannot be advertised to other regions. |
| -Preference | Integer | 50 | The priority of the route.<br>A smaller value indicates a higher priority. |
| RequestId | String | 004E99FB-E996-5777-888E-BA1D8F215407 | The request ID. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 4 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenRegionDomainRouteEntries
&CenId=cen-7qthudw0ll6j****
&CenRegionId=cn-qingdao-env66-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":4,
 "PageSize":10,
 "RequestId":"004E99FB-E996-5777-888E-BA1D8F215407",
 "PageNumber":1,
 "CenRouteEntries":{
  "Status":"Active",
  "ToOtherRegionStatus":"Active",
  "NextHopType":"VPC",
  "NextHopRegionId":"cn-qingdao-env66-d01",
  "Type":"CEN",
  "Communities":"65501:1",
  "Preference":50,
  "-CenRouteMapRecords":{
   "RegionId":"cn-qingdao-env66-d01",
   "RouteMapId":"cenrmap-cz5axczdxb7yfu****"
  },
  "AsPaths":"65501",
  "DestinationCidrBlock":"192.168.1.0/24",
  "NextHopInstanceId":"vpc-bp1j8728mm6pweeod****",
  "-CenOutRouteMapRecords":{
   "RegionId":"cn-qingdao-env66-d01",
   "RouteMapId":"cenrmap-dbarzidzp7ek4k****"
  }
 }
}
```

`XML`  format

```xml
<TotalCount>4</TotalCount>
<PageSize>10</PageSize>
<RequestId>004E99FB-E996-5777-888E-BA1D8F215407</RequestId>
<PageNumber>1</PageNumber>
<CenRouteEntries>
 <Status>Active</Status>
 <ToOtherRegionStatus>Active</ToOtherRegionStatus>
 <NextHopType>VPC</NextHopType>
 <NextHopRegionId>cn-qingdao-env66-d01</NextHopRegionId>
 <Type>CEN</Type>
 <Communities>65501:1</Communities>
 <Preference>50</Preference>
 <-CenRouteMapRecords>
  <RegionId>cn-qingdao-env66-d01</RegionId>
  <RouteMapId>cenrmap-cz5axczdxb7yfu****</RouteMapId>
 </-CenRouteMapRecords>
 <AsPaths>65501</AsPaths>
 <DestinationCidrBlock>192.168.1.0/24</DestinationCidrBlock>
 <NextHopInstanceId>vpc-bp1j8728mm6pweeod****</NextHopInstanceId>
 <-CenOutRouteMapRecords>
  <RegionId>cn-qingdao-env66-d01</RegionId>
  <RouteMapId>cenrmap-dbarzidzp7ek4k****</RouteMapId>
 </-CenOutRouteMapRecords>
</CenRouteEntries>
```

<a id="section-1-10-4"></a>

### 1.10.4. DescribeCenChildInstanceRouteEntries

Queries the routes of a network instance that is attached to a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenChildInstanceRo uteEntries | The operation that you want to perform. Set the value to DescribeCenChildInstance <strong>RouteEntries</strong>. |
| CenId | String | Query | Yes | cen-7qthudw0ll6jmc\*\*\*\* | The ID of the CEN instance. |
| ChildInstanc eId | String | Query | Yes | vpc-bp18sth14qii3pnvo\*\*\*\* | The ID of the network instance. |
| ChildInstanc eType | String | Query | Yes | VPC | The type of the network instance. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| Status | String | Query | No | Active | The route status. Valid values:<br>• <strong>Active</strong>: available routes<br>• <strong>Candidate</strong>: candidate routes<br>• <strong>Standby</strong>: standby routes<br>• <strong>Rejected</strong>: rejected routes<br>• <strong>Prohibited</strong>: prohibited routes<br>• <strong>All</strong> (default value): all routes |
| PageNumber | Integ er | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: <strong>10</strong>. Valid values: <strong>1</strong> to <strong>50</strong>. |
| ChildInstanc eRegionId | String | Query | No | cn-qingdao-env66-d01 | The ID of the region where the network instance is deployed.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CenRouteEntries | Array |  | The information about the routes. |
| -Communities | Normal | 65501:1 | The community attributes of the routes. |
| -AsPaths | Normal | 65501 | The AS path of the routes. |
| -CenRouteMapRe cords | Array |  | The routing policy that the routes match. |
| --RouteMapId | String | cenrmap-w4yf7toozfol3q\*\*\*\* | The routing policy ID. |
| --RegionId | String | cn-qingdao-env66-d01 | The region ID of the peer network instance on which the overlapping routes are found. |
| -Conflicts | Array |  | A list of overlapping routes. |
| --Status | String | conflict | The cause of the overlapping routes. Valid values:<br>• <strong>conflict</strong>: The routes have the same destination CIDR block.<br>• <strong>overflow</strong>: The number of routes in the route table configured on another network instance has reached the upper limit. |
| --DestinationCidrB lock | String | 192.168.1.0/24 | The destination CIDR block of the overlapping routes. |
| --InstanceId | String | vbr-bp1svadp4lq38janc\*\* \*\* | The ID of the peer network instance on which the overlapping routes are found. |
| --InstanceType | String | VBR | The type of the peer network instance on which the overlapping routes are found. Valid values:<br>• VPC<br>• VBR |
| --RegionId | String | cn-qingdao-env66-d01 | The region ID of the peer network instance on which the overlapping routes are found. |
| -Status | String | Active | The route status. Valid values:<br>• <strong>Active</strong>: available routes<br>• <strong>Candidate</strong>: candidate routes<br>• <strong>Standby</strong>: standby routes<br>• <strong>Rejected</strong>: rejected routes<br>• <strong>Prohibited</strong>: prohibited routes |
| -Type | String | CEN | The route type. Valid values:<br>• <strong>CEN</strong>: route advertised by CEN<br>• <strong>System</strong>: system route<br>• <strong>Custom</strong>: custom route |
| -PublishStatus | String | Published | Indicates whether the route is advertised to the CEN instance. Valid values:<br>• <strong>Published</strong>: The route is advertised to the CEN instance.<br>• <strong>NonPublished</strong>: The route is not advertised to the CEN instance. |
| -NextHopType | String | VBR | The type of the instance specified as the next hop in the route. Valid values:<br>• <strong>Instance</strong>: Elastic Compute Service (ECS) instance.<br>• <strong>HaVip</strong>: high-availability virtual IP address (HAVIP).<br>• <strong>RouterInterface</strong>: router interface.<br>• <strong>NetworkInterface</strong>: elastic network interface (ENI).<br>• <strong>VpnGateway</strong>: VPN gateway.<br>• <strong>IPv6Gateway</strong>: IPv6 gateway.<br>• <strong>NatGateway</strong>: NAT gateway.<br>• <strong>Attachment</strong>: network instance connection<br>• <strong>service</strong>: cloud service<br>• <strong>VBR</strong>: VBR<br>• <strong>CCN</strong>: Cloud Connect Network (CCN) instance<br>• <strong>VPC</strong>: VPC<br>• <strong>local</strong>: system route (no next hop is specified)<br>• <strong>TR</strong>: transit router<br>• <strong>BlackHole</strong>: blackhole route (no next hop is specified)<br>• <strong>EcRouterInterface</strong>: router interface for Express Connect<br>• <strong>HealthCheck</strong>: health check<br>• <strong>AS</strong>: access gateway for CCN<br>• <strong>classic</strong>: classic network-type instance<br>• <strong>GatewayEndpoint</strong>: gateway endpoint<br>• <strong>CPE</strong>: data center connected to a VBR |
| -OperationalMode | Boolean | true | Indicates whether the route is allowed to be advertised to or withdrawn from the CEN instance. Valid values:<br>• <strong>true</strong>: yes<br>• <strong>false</strong>: no |
| -NextHopRegionI d | String | cn-qingdao-env66-d01 | The region ID of the instance specified as the next hop in the route. |
| -NextHopInstance Id | String | vbr-bp13gtbhdp0pfqg6s\*\* \*\* | The ID of the instance specified as the next hop in the route. |
| -DestinationCidrB lock | String | 10.0.0.0/24 | The destination CIDR block of the route. |
| -RouteTableId | String | vtb-bp1r9pvl4xen8s9ju\*\*\* \* | The ID of the route table. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 17A57456-EF48-419D-9AE6-9B03D9996018 | The request ID. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 4 | The total number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenChildInstanceRouteEntries
&CenId=cen-7qthudw0ll6jmc****
&ChildInstanceId=vpc-bp18sth14qii3pnvo****
&ChildInstanceType=VPC
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":4,
 "PageSize":10,
 "RequestId":"17A57456-EF48-419D-9AE6-9B03D9996018",
 "PageNumber":1,
 "CenRouteEntries":{
  "Status":"Active",
  "RouteTableId":"vtb-bp1r9pvl4xen8s9ju****",
  "Communities":"65501:1",
  "-Conflicts":{
   "Status":"conflict",
   "InstanceId":"vbr-bp1svadp4lq38janc****",
   "DestinationCidrBlock":"192.168.1.0/24",
   "RegionId":"cn-qingdao-env66-d01",
   "InstanceType":"VBR"
  },
  "DestinationCidrBlock":"10.0.0.0/24",
  "OperationalMode":true,
  "NextHopInstanceId":"vbr-bp13gtbhdp0pfqg6s****",
  "NextHopType":"VBR",
  "NextHopRegionId":"cn-qingdao-env66-d01",
  "Type":"CEN",
  "-CenRouteMapRecords":{
   "RegionId":"cn-qingdao-env66-d01",
   "RouteMapId":"cenrmap-w4yf7toozfol3q****"
  },
  "AsPaths":"65501",
  "PublishStatus":"Published"
 }
}
```

`XML`  format

```xml
<TotalCount>4</TotalCount>
<PageSize>10</PageSize>
<RequestId>17A57456-EF48-419D-9AE6-9B03D9996018</RequestId>
<PageNumber>1</PageNumber>
<CenRouteEntries>
 <Status>Active</Status>
 <RouteTableId>vtb-bp1r9pvl4xen8s9ju****</RouteTableId>
 <Communities>65501:1</Communities>
 <-Conflicts>
  <Status>conflict</Status>
  <InstanceId>vbr-bp1svadp4lq38janc****</InstanceId>
  <DestinationCidrBlock>192.168.1.0/24</DestinationCidrBlock>
  <RegionId>cn-qingdao-env66-d01</RegionId>
  <InstanceType>VBR</InstanceType>
 </-Conflicts>
 <DestinationCidrBlock>10.0.0.0/24</DestinationCidrBlock>
 <OperationalMode>true</OperationalMode>
 <NextHopInstanceId>vbr-bp13gtbhdp0pfqg6s****</NextHopInstanceId>
 <NextHopType>VBR</NextHopType>
 <NextHopRegionId>cn-qingdao-env66-d01</NextHopRegionId>
 <Type>CEN</Type>
 <-CenRouteMapRecords>
  <RegionId>cn-qingdao-env66-d01</RegionId>
  <RouteMapId>cenrmap-w4yf7toozfol3q****</RouteMapId>
 </-CenRouteMapRecords>
 <AsPaths>65501</AsPaths>
 <PublishStatus>Published</PublishStatus>
</CenRouteEntries>
```

<a id="section-1-11"></a>

## 1.11. Custom route tables

<a id="section-1-11-1"></a>

### 1.11.1. UpdateTransitRouterRouteTable

Modifies the name and description of a route table that belongs to a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | UpdateTransitRouterRouteTa ble | The operation that you want to perform. Set the value to UpdateTransitRouterRout <strong>eTable</strong>. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| TransitRoute rRouteTable Name | String | Query | No | testname | The new name of the route table.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ - |
| TransitRoute rRouteTable Description | String | Query | No | testdesc | The new description of the route table.<br>The description must be 2 to 256 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. You can also leave the description empty. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 9D6D5548-F271-41C4-AA9F-A62F5599085B | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UpdateTransitRouterRouteTable
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"9D6D5548-F271-41C4-AA9F-A62F5599085B"
}
```

`XML`  format

```xml
<RequestId>9D6D5548-F271-41C4-AA9F-A62F5599085B</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterR outeTableId.NotFound | InvalidTransitRouterRouteTableId.N otFound | TransitRouterRouteTableId is not found. |
| 400 | InvalidName | InvalidName | Name is invalid. |
| 400 | InvalidDescription | InvalidDescription | Description is invalid. |

<a id="section-1-11-2"></a>

### 1.11.2. DeleteTransitRouterRouteTable

Deletes a custom route table of a transit router.

**Usage notes**

- You cannot delete the default route table of a transit router.

- Before you delete a custom route table, make sure that the following requirements are met:

  - The route table is not associated with an associated forwarding correlation. For more information about how to delete an associated forwarding correlation, see DissociateTransitRouterAttachmentFromRouteTable.

  - The route table is not associated with a route learning policy. For more information about how to delete a route learning correlation, see DisableTransitRouterRouteTablePropagation.

  - The route table does not contain a custom route. For more information about how to delete a custom route, see DeleteTransitRouterRouteEntry.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteTransitRouterRouteTa ble | The operation that you want to perform. Set the value to DeleteTransitRouterRoute <strong>Table</strong>. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1xbcgpgcz9axl9m\*\*\*\* | The ID of the custom route table. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | EAB2F133-8556-4D7C-9E91-7EE4FE9CC7D2 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterRouteTable
&TransitRouterRouteTableId=vtb-bp1xbcgpgcz9axl9m****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"EAB2F133-8556-4D7C-9E91-7EE4FE9CC7D2"
}
```

`XML`  format

```xml
<RequestId>EAB2F133-8556-4D7C-9E91-7EE4FE9CC7D2</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | OperationFailed.Delet eSystemRouteTable | OperationFailed.DeleteSystemRout eTable | Operation failed because You are not allowed to Delete System Transit Route Table. |
| 400 | InvalidTransitRouterR outeTableId.NotFound | InvalidTransitRouterRouteTableId.N otFound | TransitRouterRouteTableId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | MissingParam.Transit RouterRouteTableId | MissingParam.TransitRouterRouteT ableId | The parameter TransitRouterRouteTableId is mandatory. |
| 400 | IncorrectStatus.Transi tRouterRouteTable | IncorrectStatus.TransitRouterRoute Table | TransitRouterRouteTable status is invalid. |
| 400 | OperationFailed.Delet eRouteTableWithAsso ciation | OperationFailed.DeleteRouteTable WithAssociation | Operation failed because you are not allowed to delete TransitRouterRouteTable with association |
| 400 | OperationFailed.Delet eRouteTableWithProp agation | OperationFailed.DeleteRouteTable WithPropagation | Operation failed because you are not allowed to delete transit router route table with propagation |
| 400 | OperationFailed.Delet eRouteTableWithRout eEntry | OperationFailed.DeleteRouteTable WithRouteEntry | Operation failed because you are not allowed to delete transit touter route table with route entry |

<a id="section-1-11-3"></a>

### 1.11.3. ListTransitRouterRouteTables

Queries the route tables of a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListTransitRouterRouteTables | The operation that you want to perform. Set the value to ListTransitRouterRouteTa <strong>bles</strong>. |
| MaxResults | Integ er | Query | No | 20 | The number of entries per page. Valid values: <strong>1</strong> to <strong>100</strong>.Default value: <strong>20</strong>. |
| NextToken | String | Query | No | dd20\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the <strong>NextToken</strong> parameter. |
| TransitRoute rRouteTable Type | String | Query | No | Custom | The type of route table. Valid values:<br>• <strong>Custom</strong>: custom route table<br>• <strong>System</strong>: default route table |
| TransitRoute rId | String | Query | Yes | tr-uf654ttymmljlvh2x\*\*\*\* | The ID of the transit router. |
| TransitRoute rRouteTable Status | String | Query | No | Active | The state of the route table.Valid values: Valid values:<br>• <strong>Creating</strong>: The route table is being created.<br>• <strong>Deleting</strong>: The route table is being deleted.<br>• <strong>Active</strong>: The route table is available. |
| TransitRoute rRouteTable Names | Repea tList | Query | No | testname | The name of the route table.<br>You can query at most 20 route tables in each call.<br><em>If you specify both the</em> <strong><em>TransitRouterRouteT</em></strong> <strong><em>ableNames</em></strong><em> and</em> <strong><em>TransitRouterRouteT</em></strong> <strong><em>ableIds</em></strong><em> parameters,</em> <em>make sure that the</em> <em>specified name and ID</em> <em>belong to the same</em> <em>route table.</em> |
| TransitRoute rRouteTableI ds | Repea tList | Query | No | vtb-bp1l8awdb4iuo9uwu\*\*\*\* | The ID of the route table.<br>You can query at most 20 route tables in each call. |
| Tag | Repea tList | Query | No |  | The tags.<br>You can specify at most 20 tags in each call. |
| -Key | String |  | No | test | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify at most 20 tag keys. |

<table>
  <tr>
    <td>-Value</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>test</td>
    <td>The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterRo uteTables | Array |  | A list of route tables. |
| -Tags | Array |  | The tags. |
| --Key | String | test | The tag key. |
| --Value | String | test | The tag value. |
| -TransitRouterRo uteTableStatus | String | Active | The state of the route table. Valid values:<br>• <strong>Creating</strong>: The route table is being created.<br>• <strong>Deleting</strong>: The route table is being deleted.<br>• <strong>Active</strong>: The route table is available. |
| -TransitRouterRo uteTableType | String | System | The type of route table. Valid values:<br>• <strong>Custom</strong>: custom route table<br>• <strong>System</strong>: default route table |
| -CreateTime | String | 2021-03-15T09:39Z | The time when the route table was created.<br>The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in Coordinated Universal Time (UTC). |
| -TransitRouterRo uteTableId | String | vtb-bp1dudbh2d5na6b50 \*\*\*\* | The ID of the route table. |
| -TransitRouterRo uteTableName | String | testname | The name of the route table. |
| -TransitRouterRo uteTableDescript ion | String | testdesc | The description of the route table. |
| NextToken | String | dd20\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | 82678F4A-C9F7-4CC1-8BF0-D619A63BFC57 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTables
&TransitRouterId=tr-uf654ttymmljlvh2x****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"dd20****",
 "RequestId":"82678F4A-C9F7-4CC1-8BF0-D619A63BFC57",
 "TransitRouterRouteTables":{
  "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****",
  "TransitRouterRouteTableStatus":"Active",
  "TransitRouterRouteTableType":"System",
  "TransitRouterRouteTableDescription":"testdesc",
  "-Tags":{
   "Value":"test",
   "Key":"test"
  },
  "CreateTime":"2021-03-15T09:39Z",
  "TransitRouterRouteTableName":"testname"
 },
 "MaxResults":20
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>dd20****</NextToken>
<RequestId>82678F4A-C9F7-4CC1-8BF0-D619A63BFC57</RequestId>
<TransitRouterRouteTables>
 <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId>
 <TransitRouterRouteTableStatus>Active</TransitRouterRouteTableStatus>
 <TransitRouterRouteTableType>System</TransitRouterRouteTableType>
 <TransitRouterRouteTableDescription>testdesc</TransitRouterRouteTableDescription>
 <-Tags>
  <Value>test</Value>
  <Key>test</Key>
 </-Tags>
 <CreateTime>2021-03-15T09:39Z</CreateTime>
 <TransitRouterRouteTableName>testname</TransitRouterRouteTableName>
</TransitRouterRouteTables>
<MaxResults>20</MaxResults>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | NextToken is illegal |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found. |

<a id="section-1-11-4"></a>

### 1.11.4. CreateTransitRouterRouteTable

Creates a custom route table for a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateTransitRouterRouteTa ble | The operation that you want to perform. Set the value to CreateTransitRouterRoute <strong>Table</strong>. |

<table>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>02fb3da4-130e-11e9-8e44-001****</td>
    <td>The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em></td>
  </tr>
  <tr>
    <td>TransitRoute rRouteTable Name</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>testname</td>
    <td>The name of the custom route table.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteTable Description</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>testdesc</td>
    <td>The description of the custom route table.<br>The description must be 2 to 256 characters in length, and can contain letters, digits, and the following special characters: , . ; / @ _ -. You can also leave the description empty.</td>
  </tr>
  <tr>
    <td>TransitRoute rId</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>tr-bp1su1ytdxtataupl****</td>
    <td>The ID of the transit router.</td>
  </tr>
</table>

<table>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform a dry run. Valid values:<br>• <strong>false</strong> (default): performs a dry run and sends the request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request.</td>
  </tr>
  <tr>
    <td>Tag</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td></td>
    <td>The tags.<br>You can specify up to 20 tags in each call.</td>
  </tr>
  <tr>
    <td>-Key</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>test</td>
    <td>The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys.</td>
  </tr>
  <tr>
    <td>-Value</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>tagtest</td>
    <td>The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterRo uteTableId | String | vtb-bp1xbcgpgcz9axl9m\* \*\*\* | The ID of the custom route table. |
| RequestId | String | 599904C8-A3DA-4E5F-83B6-D5364E664247 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterRouteTable
&TransitRouterId=tr-bp1su1ytdxtataupl****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TransitRouterRouteTableId":"vtb-bp1xbcgpgcz9axl9m****",
 "RequestId":"599904C8-A3DA-4E5F-83B6-D5364E664247"
}
```

`XML`  format

```xml
<TransitRouterRouteTableId>vtb-bp1xbcgpgcz9axl9m****</TransitRouterRouteTableId>
<RequestId>599904C8-A3DA-4E5F-83B6-D5364E664247</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found |
| 400 | OperationFailed.CCNT rNotSupport | OperationFailed.CCNTrNotSupport | Operation failed because the CCN transit router does not support route table. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | MissingParam.Transit RouterId | MissingParam.TransitRouterId | The parameter TransitrouterId is mandatory. |
| 400 | OperationFailed.Basic TrNotSupport | OperationFailed.BasicTrNotSupport | Operation failed because the Basic TransitRouter does not support RouteTable |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouter | TransitRouter status is invalid. |
| 400 | QuotaExceeded.Transi tRouterRoutTable | QuotaExceeded.TransitRouterRout Table | TransitRouterRoutTable quota exceeded. |

<a id="section-1-12"></a>

## 1.12. Route learning

<a id="section-1-12-1"></a>

### 1.12.1. DisableTransitRouterRouteTablePropagation

Deletes a route learning correlation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DisableTransitRouterRouteTa blePropagation | The operation that you want to perform. Set the value to DisableTransitRouterRout <strong>eTablePropagation</strong>. |
| TransitRoute rAttachment Id | String | Query | Yes | tr-attach-vx6iwhjr1x1j78\*\*\*\* | The ID of the network instance connection. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | A7C43F99-B1E5-4A53-AB64-4BAE8AF4484E | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DisableTransitRouterRouteTablePropagation
&TransitRouterAttachmentId=tr-attach-vx6iwhjr1x1j78****
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"A7C43F99-B1E5-4A53-AB64-4BAE8AF4484E"
}
```

`XML`  format

```xml
<RequestId>A7C43F99-B1E5-4A53-AB64-4BAE8AF4484E</RequestId>
```

**Error codes**

<table>
  <tr>
    <td>HttpCode</td>
    <td>Error code</td>
    <td>Error message</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>400</td>
    <td>InvalidAttachmentId.N otFound</td>
    <td>InvalidAttachmentId.NotFound</td>
    <td>The specified AttachmentId is not found.</td>
  </tr>
  <tr>
    <td>404</td>
    <td>InvalidRouteTableId.N otFound</td>
    <td>InvalidRouteTableId.NotFound</td>
    <td>The specified RouteTableId is not found.</td>
  </tr>
</table>

<a id="section-1-12-2"></a>

### 1.12.2. ListTransitRouterRouteTablePropagations

Queries the route learning correlations of a route table that belongs to a transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterRouteTableP ropagations | The operation that you want to perform. Set the value to ListTransitRouterRouteTa <strong>blePropagations</strong>. |
| MaxResults | Integ er | Query | No | 50 | The number of entries per page. Default value: <strong>50</strong>. |
| NextToken | String | Query | No | dd20\*\*\*\* | The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| TransitRoute rAttachment Id | String | Query | No | tr-attach-vx6iwhjr1x1j78\*\*\*\* | The ID of the network instance connection. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterPro pagations | Array |  | A list of route learning correlations. |
| -Status | String | Active | The status of the route learning correlation.Valid values:<br>• Enabling<br>• Disabling<br>• Active |
| -TransitRouterAtt achmentId | String | tr-attach-vx6iwhjr1x1j78\*\*\*\* | The ID of the network instance connection. |
| -TransitRouterRo uteTableId | String | vtb-bp1dudbh2d5na6b50 \*\*\*\* | The ID of the route table of the transit router. |
| -ResourceId | String | vpc-bp1h8vbrbcgohcju5\*\* \*\* | The ID of the next hop. |
| -ResourceType | String | VPC | The type of next hop. Valid values:<br>• VPC<br>• VBR |
| RequestId | String | 04C81E0D-945E-4D61-A561-3DEA322F243B | The request ID. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| MaxResults | Integer | 50 | The number of entries per page. |
| NextToken | String | dd20\*\*\*\* | The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTablePropagations
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":2,
 "NextToken":"dd20****",
 "RequestId":"04C81E0D-945E-4D61-A561-3DEA322F243B",
 "MaxResults":50,
 "TransitRouterPropagations":{
  "Status":"Active",
  "TransitRouterAttachmentId":"tr-attach-vx6iwhjr1x1j78****",
  "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****",
  "ResourceId":"vpc-bp1h8vbrbcgohcju5****",
  "ResourceType":"VPC"
 }
}
```

`XML`  format

```xml
<TotalCount>2</TotalCount>
<NextToken>dd20****</NextToken>
<RequestId>04C81E0D-945E-4D61-A561-3DEA322F243B</RequestId>
<MaxResults>50</MaxResults>
<TransitRouterPropagations>
 <Status>Active</Status>
 <TransitRouterAttachmentId>tr-attach-vx6iwhjr1x1j78****</TransitRouterAttachmentId>
 <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId>
 <ResourceId>vpc-bp1h8vbrbcgohcju5****</ResourceId>
 <ResourceType>VPC</ResourceType>
</TransitRouterPropagations>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The parameter NextToken is invalid. |

<a id="section-1-12-3"></a>

### 1.12.3. EnableTransitRouterRouteTablePropagation

Creates a route learning correlation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | EnableTransitRouterRouteTa blePropagation | The operation that you want to perform. Set the value to EnableTransitRouterRout <strong>eTablePropagation</strong>. |
| TransitRoute rAttachment Id | String | Query | Yes | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the network instance connection. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 59CF8BF9-DE61-421E-B903-D56AF46A303C | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=EnableTransitRouterRouteTablePropagation
&TransitRouterAttachmentId=tr-attach-nls9fzkfat8934****
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"59CF8BF9-DE61-421E-B903-D56AF46A303C"
}
```

`XML`  format

```xml
<RequestId>59CF8BF9-DE61-421E-B903-D56AF46A303C</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | InvalidRouteTableId.N otFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |
| 404 | InvalidAttachmentId.N otFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |

<a id="section-1-13"></a>

## 1.13. Associated forwarding

<a id="section-1-13-1"></a>

### 1.13.1. DissociateTransitRouterAttachmentFromRouteTable

Deletes an associated forwarding correlation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DissociateTransitRouterAttac hmentFromRouteTable | The operation that you want to perform. Set the value to DissociateTransitRouterAt tachmentFromRouteTable. |
| TransitRoute rAttachment Id | String | Query | Yes | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the network instance connection. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and sends the request.<br>• <strong>true</strong>: performs a dry run.The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the system returns the ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DissociateTransitRouterAttachmentFromRouteTable
&TransitRouterAttachmentId=tr-attach-nls9fzkfat8934****
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"4EC47282-1B74-4534-BD0E-403F3EE64CAF"
}
```

`XML`  format

```xml
<RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IncorrectStatus.Status | IncorrectStatus.Status | RouteTableAssociation status is invalid. |
| 404 | InvalidAttachmentId.N otFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 404 | InvalidRouteTableId.N otFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |

<a id="section-1-13-2"></a>

### 1.13.2. ListTransitRouterRouteTableAssociations

Queries the associated forwarding correlations that are created for a route table of a transit router or a network instance connection.

**Usage notes**

When you call ListTransitRouterRouteTableAssociations, you must set at least one of the **TransitRouterRouteTableId** and **TransitRouterAttachmentId** parameters.

- To query the network instance connections that are in an associated forwarding relationship with a transit router route table, specify only the **TransitRouterRouteTableId** parameter.

- To query the transit router route table that is in an associated forwarding relationship with a network instance connection, specify only the **TransitRouterAttachmentId** parameter.

- To query the associated forwarding correlations between network instance connections and transit router route tables, specify both the **TransitRouterRouteTableId** and **TransitRouterAttachmentId** parameters.

  - If an associated forwarding correlation is created between the network instance connection and the route table of the Enterprise Edition transit router, the information about the associated forwarding correlation is returned.

  - If no associated forwarding correlation is created between the network instance connection and the route table of the Enterprise Edition transit router, **TransitRouterAssociations** in the response is empty.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterRouteTable Associations | The operation that you want to perform. Set the value to ListTransitRouterRouteTa <strong>bleAssociations</strong>. |
| MaxResults | Integ er | Query | No | 50 | The number of entries per page. Default value: <strong>50</strong>. |
| NextToken | String | Query | No | a415\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the <strong>NextToken</strong> parameter. |
| TransitRoute rRouteTableI d | String | Query | No | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| TransitRoute rAttachment Id | String | Query | No | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the network instance connection. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterAss ociations | Array |  | A list of associated forwarding correlations. |
| -TransitRouterAtt achmentId | String | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the network instance connection. |
| -Status | String | Associating | The status of the associated forwarding correlation. Valid values:<br>• Active<br>• Associating<br>• Dissociating |
| -ResourceType | String | VPC | The type of next hop. Valid values:<br>• <strong>VPC</strong>: virtual private cloud (VPC)<br>• <strong>VBR</strong>: virtual border router (VBR) |
| -ResourceId | String | vpc-bp1h8vbrbcgohcju5\*\* \*\* | The ID of the next hop. |
| -TransitRouterRo uteTableId | String | vtb-bp1dudbh2d5na6b50 \*\*\*\* | The ID of the route table of the transit router. |
| NextToken | String | a415\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | F6B1D9AB-176D-4399-801D-8BC576F4EB0D | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 50 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTableAssociations
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "NextToken":"a415****",
 "RequestId":"F6B1D9AB-176D-4399-801D-8BC576F4EB0D",
 "MaxResults":50,
 "TransitRouterAssociations":{
  "TransitRouterAttachmentId":"tr-attach-nls9fzkfat8934****",
  "Status":"Associating",
  "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****",
  "ResourceId":"vpc-bp1h8vbrbcgohcju5****",
  "ResourceType":"VPC"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<NextToken>a415****</NextToken>
<RequestId>F6B1D9AB-176D-4399-801D-8BC576F4EB0D</RequestId>
<MaxResults>50</MaxResults>
<TransitRouterAssociations>
 <TransitRouterAttachmentId>tr-attach-nls9fzkfat8934****</TransitRouterAttachmentId>
 <Status>Associating</Status>
 <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId>
 <ResourceId>vpc-bp1h8vbrbcgohcju5****</ResourceId>
 <ResourceType>VPC</ResourceType>
</TransitRouterAssociations>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The parameter NextToken is invalid. |

<a id="section-1-13-3"></a>

### 1.13.3. AssociateTransitRouterAttachmentWithRouteTable

Creates an associated forwarding correlation.

**Usage notes**

Each network instance connection can have an associated forwarding correlation with only one route table of only one transit router.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | AssociateTransitRouterAttach mentWithRouteTable | The operation that you want to perform. Set the value to AssociateTransitRouterAt <strong>tachmentWithRouteTable</strong>. |
| TransitRoute rAttachment Id | String | Query | Yes | tr-attach-nls9fzkfat8934\*\*\*\* | The ID of the network instance connection. |
| TransitRoute rRouteTableI d | String | Query | Yes | vtb-bp1dudbh2d5na6b50\*\*\*\* | The ID of the route table of the transit router. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44-001\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <strong><em>request ID</em></strong><em> as the</em> <strong><em>client token</em></strong><em>. The</em> <strong><em>request ID</em></strong><em> may be</em> <em>different for each</em> <em>request.</em> |
| DryRun | Boole an | Query | No | false | Specifies whether to perform only a dry run, without performing the actual request. Valid values:<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.<br>• <strong>true</strong>: performs only a dry run. If you use this value, the system checks whether the required parameters are set, and whether the request syntax is valid. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=AssociateTransitRouterAttachmentWithRouteTable
&TransitRouterAttachmentId=tr-attach-nls9fzkfat8934****
&TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"4EC47282-1B74-4534-BD0E-403F3EE64CAF"
}
```

`XML`  format

```xml
<RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | AssociationExist.Trans itRouterTable | AssociationExist.TransitRouterTabl e | The specified association already exists. |
| 404 | InvalidRouteTableId.N otFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |
| 404 | InvalidAttachmentId.N otFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |

<a id="section-1-14"></a>

## 1.14. Multicast

<a id="section-1-14-1"></a>

### 1.14.1. CreateTransitRouterMulticastDomain

A multicast domain is created.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | CreateTransitRouterMulticast Domain | The operation that you want to perform. Set the value to CreateTransitRouterMulti <strong>castDomain</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-4266\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| CenId | String | Query | No | cen-a7syd349kne38g\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| TransitRoute rId | String | Query | No | tr-p0wr9p28r92d598y6\*\*\*\* | The ID of the transit router. |
| RegionId | String | Query | No | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| TransitRoute rMulticastDo mainName | String | Query | No | nametest | The name of the multicast domain.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-). |
| TransitRoute rMulticastDo mainDescrip tion | String | Query | No | desctest | The description of the multicast domain.<br>The description must be 0 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-). |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a dry run, without performing the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code> DryRunOperation </code> error message is returned.<br>• <strong>false</strong> (default): performs a dry run and sends the request. |
| Tag | Repea tList | Query | No |  | The information about the tag.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | TagKey | The tag key.<br>The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |
| -Value | String |  | No | TagValue | The tag value.<br>The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterMul ticastDomainId | String | tr-mcast-domain-40cwj0rgzgdtam\*\*\*\* | The ID of the multicast domain. |
| RequestId | String | 94E19C6F-206F-5223-9A63-64B85851BC04 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateTransitRouterMulticastDomain
&Action=CreateTransitRouterMulticastDomain
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"94E19C6F-206F-5223-9A63-64B85851BC04",
 "TransitRouterMulticastDomainId":"tr-mcast-domain-40cwj0rgzgdtam****"
}
```

`XML`  format

```xml
<RequestId>94E19C6F-206F-5223-9A63-64B85851BC04</RequestId>
<TransitRouterMulticastDomainId>tr-mcast-domain-40cwj0rgzgdtam****
</TransitRouterMulticastDomainId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | The specified TransitRouterId is not found. |
| 400 | IllegalParam.TransitRo uterId | IllegalParam.TransitRouterId | The specified TransitRouterId is illegal. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is illegal. |
| 400 | IllegalParam.RegionId | IllegalParam.RegionId | The specified RegionId is illegal. |
| 400 | InvalidCenId.NotFoun d | InvalidCenId.NotFound | The specified CenId is not found. |
| 400 | INVALID_OPERATION_TRANSITROUTER_NOT _EXIST | InvalidOperation.TransitRouterNotE xist | Operation is invalid because the transit router not exist. |
| 400 | INVALID_OPERATION_CBN_INSTANCE_STAT US | InvalidOperation.CENInstanceStatu s | The CEN instance is not in a valid state for the operation. |
| 400 | IncorrectStatus.Transi tRouterInstance | IncorrectStatus.TransitRouterInsta nce | The status of TransitRouter is incorrect. |
| 400 | OperationUnsupporte d.TransitRouterType | OperationUnsupported.TransitRout erType | The specified TransitRouterType does not support the operation. |
| 400 | OperationUnsupporte d.ServiceMode | OperationUnsupported.ServiceMod e | The specified ServiceMode does not support the operation. |
| 400 | OperationUnsupporte d.TransitRouterSuppor tMulticast | OperationUnsupported.TransitRout erSupportMulticast | The specified TransitRouterSupportMulticast does not support the operation. |
| 400 | OperationUnsupporte d.RegionId | OperationUnsupported.RegionId | The specified RegionId does not support the operation. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouter | The status of TransitRouter is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-2"></a>

### 1.14.2. ModifyTransitRouterMulticastDomain

Modifies the name and description of a multicast domain.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ModifyTransitRouterMulticast Domain | The operation that you want to perform. Set the value to ModifyTransitRouterMulti <strong>castDomain</strong>. |

<table>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>123e4567-e89b-12d3-a456-4266****</td>
    <td>The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.</td>
  </tr>
  <tr>
    <td>TransitRoute rMulticastDo mainId</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>tr-mcast-domain-40cwj0rgzgdtam****</td>
    <td>The ID of the multicast domain.</td>
  </tr>
  <tr>
    <td>TransitRoute rMulticastDo mainName</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>nametest</td>
    <td>The new name of the multicast domain.<br>The name must be 0 to 128 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).</td>
  </tr>
  <tr>
    <td>TransitRoute rMulticastDo mainDescrip tion</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>desctest</td>
    <td>The new description of the multicast domain.<br>The description must be 0 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).</td>
  </tr>
</table>

<table>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.<br><em>This parameter is not in</em> <em>use.</em></td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 26273D23-5CB0-5EFC-AF5F-78A5448084C9 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyTransitRouterMulticastDomain
&TransitRouterMulticastDomainId=tr-mcast-domain-40cwj0rgzgdtam****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"26273D23-5CB0-5EFC-AF5F-78A5448084C9"
}
```

`XML`  format

```xml
<RequestId>26273D23-5CB0-5EFC-AF5F-78A5448084C9</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | NAME_ILLEGAL | Illegal.Name | Name is illegal. |
| 400 | DESCRIPTION_ILLEGAL | Illegal.Description | Description is illegal. |
| 400 | InvalidTransitRouterM ulticastDomainId.NotF ound | InvalidMulticastDomainId.NotFound | The specified MulticastDomainId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-3"></a>

### 1.14.3. ListTransitRouterMulticastDomains

Queries the information about multicast domains.

**Usage notes**

If you configure one of the **RegionId** and **CenId** parameters, you must configure the other parameter. Otherwise, no information about the multicast domain is returned. You can configure only one of the **TransitRouterId** and **TransitRouterMulticastDomainId** parameters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListTransitRouterMulticastDo mains | The operation that you want to perform. Set the value to ListTransitRouterMulticastDo mains. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426655440000 | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| CenId | String | Query | No | cen-a7syd349kne38g\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| TransitRoute rId | String | Query | No | tr-p0wr9p28r92d598y6\*\*\*\* | The ID of the transit router. |
| TransitRoute rMulticastDo mainId | String | Query | No | tr-mcast-domain-3r3bvbypxqheej\*\*\*\* | The ID of the multicast domain. |
| RegionId | String | Query | No | cn-qingdao-env17e-d01 | The region ID of the transit router.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| MaxResults | Long | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGK Pd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first query and no subsequent queries are to be sent, ignore this parameter.<br>• If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results. |
| Tag | Repea tList | Query | No |  | The information about the tag.<br>You can specify up to 20 tags in each call. |
| -Key | String |  | No | TagKey | The tag keys.<br>The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length, and cannot contain <code> http:// </code> or <code> https:// </code>.It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>You can specify up to 20 tag keys. |

<table>
  <tr>
    <td>-Value</td>
    <td>String</td>
    <td></td>
    <td>No</td>
    <td>TagValue</td>
    <td>The tag values.<br>The tag values can be an empty string. It can be up to 128 characters in length, and cannot contain <code> http:// </code>or <code> https:// </code>. It cannot start with <code> aliyun </code> or <code> acs: </code>.<br>Each tag key must have a unique tag value. You can specify up to 20 tag values in each call.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterMul ticastDomains | Array |  | The information about the multicast domain. |
| -Tags | Array |  | The tags. |
| --Key | String | TagKey | The tag key. |
| --Value | String | TagValue | The tag value. |
| -TransitRouterMul ticastDomainId | String | tr-mcast-domain-3r3bvbypxqheej\*\*\*\* | The ID of the multicast domain. |
| -TransitRouterMul ticastDomainNa me | String | nametest | The name of the multicast domain. |
| -TransitRouterMul ticastDomainDes cription | String | desctest | The description of the multicast domain. |
| -Status | String | Active | The status of the multicast domain.<br>The valid value is <strong>Active</strong>, which indicates that the multicast domain is available. |
| -TransitRouterId | String | tr-bp1c23ijrl6d6c226h\*\* \* | The ID of the transit router. |
| RequestId | String | 8A0F93D1-FD6C-56FC-B6D2-668FC92D12D2 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If a value is returned for <strong>NextToken</strong>, the value indicates the token that is used for the next request to retrieve a new page of results. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomains
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "RequestId":"8A0F93D1-FD6C-56FC-B6D2-668FC92D12D2",
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "MaxResults":20,
 "TransitRouterMulticastDomains":{
  "Status":"Active",
  "-Tags":{
   "Value":"TagValue",
   "Key":"TagKey"
  },
  "TransitRouterMulticastDomainId":"tr-mcast-domain-3r3bvbypxqheej****",
  "TransitRouterMulticastDomainName":"nametest",
  "TransitRouterMulticastDomainDescription":"desctest",
  "TransitRouterId":"tr-bp1c23ijrl6d6c226h***"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<RequestId>8A0F93D1-FD6C-56FC-B6D2-668FC92D12D2</RequestId>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<MaxResults>20</MaxResults>
<TransitRouterMulticastDomains>
 <Status>Active</Status>
 <-Tags>
  <Value>TagValue</Value>
  <Key>TagKey</Key>
 </-Tags>
 <TransitRouterMulticastDomainId>tr-mcast-domain-3r3bvbypxqheej****
</TransitRouterMulticastDomainId>
 <TransitRouterMulticastDomainName>nametest</TransitRouterMulticastDomainName>
 <TransitRouterMulticastDomainDescription>desctest</TransitRouterMulticastDomainDescription>
 <TransitRouterId>tr-bp1c23ijrl6d6c226h***</TransitRouterId>
</TransitRouterMulticastDomains>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TrInstanc e | IllegalParam.TrInstance | The specified TrInstance is illegal. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is illegal. |

<a id="section-1-14-4"></a>

### 1.14.4. DeleteTransitRouterMulticastDomain

Deletes a multicast domain.

**Usage notes**

Before you delete a multicast domain, make sure that the following requirements are met:

- The multicast domain is disassociated from all vSwitches. For more information, see DisassociateTransitRouterMulticastDomain.

- All multicast sources and members are removed from the multicast domain. For more information, see DeregisterTransitRouterMulticastGroupSources and DeregisterTransitRouterMulticastGroupMembers.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | DeleteTransitRouterMulticast Domain | The operation that you want to perform. Set the value to DeleteTransitRouterMulti <strong>castDomain</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-4266\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-40cwj0rgzgdtam\*\*\*\* | The ID of the multicast domain. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a only dry run, without performing the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and sends the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 40194E53-2484-5831-BB53-E11D123C1A32 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTransitRouterMulticastDomain
&TransitRouterMulticastDomainId=tr-mcast-domain-40cwj0rgzgdtam****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"40194E53-2484-5831-BB53-E11D123C1A32"
}
```

`XML`  format

```xml
<RequestId>40194E53-2484-5831-BB53-E11D123C1A32</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IncorrectStatus.Multic astDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | INSTANCE_NOT_EXIST | InstanceNotExist | The instance is not exist. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouter | The status of TransitRouter is incorrect. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_EXIST | InvalidOperation.MulticastDomainA ssociationExist | Operation is invalid because multicast domain associations exist. |
| 400 | INVALID_OPERATION_MULTICAST_GROUP_E XIST | InvalidOperation.MulticastGroupExi st | Operation is invalid because multicast groups exist. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_I N_GROUP | InvalidOperation.MulticastDomainI nGroup | Operation is invalid because multicast domain has registered as multicast group member. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-5"></a>

### 1.14.5. AssociateTransitRouterMulticastDomain

Associates the vSwitch of a virtual private cloud (VPC) with a multicast domain.

**Usage notes**

- A vSwitch can be associated with only one multicast domain. Make sure that the vSwitch is not associated with other multicast domains. For more information about how to disassociate a vSwitch from a multicast domain, see DisassociateTransitRouterMulticastDomain.

- The VPC of the vSwitch must be associated with a transit router. For more information, see CreateTransitRouterVpcAttachment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | AssociateTransitRouterMultic astDomain | The operation that you want to perform. Set the value to AssociateTransitRouterM <strong>ulticastDomain</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426655440000 | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast domain. |
| TransitRoute rAttachment Id | String | Query | Yes | tr-attach-g3kz2k3u76amsk\*\*\*\* | The ID of the VPC connection. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a dry run, without performing the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code> DryRunOperation </code> error message is returned.<br>• <strong>false</strong> (default): performs a dry run and sends the request. |
| VSwitchIds | Repea tList | Query | No | vsw-p0wxk12u6okfkr8xy\*\*\*\* | The IDs of the vSwitches.<br>You can specify at most five vSwitches in each call. A multicast domain can be associated with at most 10 vSwitches. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F88AC12C-943B-50E9-A344-4F8820BB07A7 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=AssociateTransitRouterMulticastDomain
&TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq****
&TransitRouterAttachmentId=tr-attach-g3kz2k3u76amsk****
&Action=AssociateTransitRouterMulticastDomain
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"F88AC12C-943B-50E9-A344-4F8820BB07A7"
}
```

`XML`  format

```xml
<RequestId>F88AC12C-943B-50E9-A344-4F8820BB07A7</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidMulticastDomai n.NotFound | InvalidMulticastDomain.NotFound | The specified MulticastDomain is not found. |
| 400 | IncorrectStatus.Multic astDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | InvalidAttachmentId.N otFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 400 | IllegalParam.Attachm entId | IllegalParam.AttachmentId | The specified AttachmentId is illegal. |
| 400 | IncorrectStatus.Attach ment | IncorrectStatus.Attachment | The status of Attachment is incorrect. |
| 400 | MissingParam.VSwitch Ids | MissingParam.VSwitchIds | The parameter VSwitchIds is mandatory. |
| 400 | INSTANCE_NOT_EXIST | InstanceNotExist | The instance is not exist. |
| 400 | OperationUnsupporte d.CLOUD_BOX_VPC_N OT_SUPPORT | OperationUnsupported.CloudBoxVp c | The specified CloudBoxVpc does not support the operation. |
| 400 | AssociationExist.VSwit chIds | AssociationExist.VSwitchIds | The association already exists. |
| 400 | QUOTA_FULL_MULTIC AST_VSWITCH_PER_D OMAIN | QuotaFull.VswitchPerMulticastDom ain | The number of vswitch associated with multicast domain has exceed the maximum value that can be created. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | OperationFailed.-100118 | OperationUnsupported.VpcRegion | The specified Region is not support for this operation. |

<a id="section-1-14-6"></a>

### 1.14.6. DisassociateTransitRouterMulticastDomain

Disassociates vSwitches from a multicast domain.

**Usage notes**

Before you delete a vSwitch from a multicast domain, make sure that the vSwitch does not contain a multicast source or a multicast member. For more information about how to remove a multicast source or member from a vSwitch, see DeregisterTransitRouterMulticastGroupSources and DeregisterTransitRouterMulticastGroupMembers.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | DisassociateTransitRouterMul ticastDomain | The operation that you want to perform. Set the value to DisassociateTransitRouter <strong>MulticastDomain</strong>. |

<table>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>123e4567-e89b-12d3-a456-426655440000</td>
    <td>The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.</td>
  </tr>
  <tr>
    <td>TransitRoute rMulticastDo mainId</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>tr-mcast-domain-91wpg6wbhchjeq****</td>
    <td>The ID of the multicast domain.</td>
  </tr>
  <tr>
    <td>TransitRoute rAttachment Id</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>tr-attach-g3kz2k3u76amsk****</td>
    <td>The ID of the virtual private cloud (VPC) connection.<br>A connection ID is generated after a VPC to which the vSwitch belongs is connected to a transit router.</td>
  </tr>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.</td>
  </tr>
  <tr>
    <td>VSwitchIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vsw-p0w9s2ig1jnwgrbzl****</td>
    <td>The vSwitch IDs.<br>You can specify at most five vSwitch IDs in each call.<br><em>This parameter is</em> <em>required.</em></td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6F6B3FF0-45D1-5416-B189-C45A42A0222B | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DisassociateTransitRouterMulticastDomain
&TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq****
&TransitRouterAttachmentId=tr-attach-g3kz2k3u76amsk****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"6F6B3FF0-45D1-5416-B189-C45A42A0222B"
}
```

`XML`  format

```xml
<RequestId>6F6B3FF0-45D1-5416-B189-C45A42A0222B</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidMulticastDomai nId.NotFound | InvalidMulticastDomainId.NotFound | The specified MulticastDomainId is not found. |
| 400 | IncorrectStatus.Multic astDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | INSTANCE_STATUS_N OT_SUPPORT | InstanceStatusNotSupport | The status of instance not support the operation. |
| 400 | InvalidAttachmentId.N otFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 400 | IncorrectStatus.Attach ment | IncorrectStatus.Attachment | The status of Attachment is incorrect. |
| 400 | IllegalParam.Attachm entId | IllegalParam.AttachmentId | The specified AttachmentId is illegal. |
| 400 | INVALID_OPERATION_MULTICAST_GROUP_E XIST | InvalidOperation.MulticastGroupExi st | Operation is invalid because multicast groups exist. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-7"></a>

### 1.14.7. ListTransitRouterMulticastDomainAssociations

Queries whether vSwitches in virtual private clouds (VPCs) are associated with a multicast domain.

**Usage notes**

You must specify at least one of the **TransitRouterMulticastDomainId**

and

**TransitRouterAttachmentId**

parameters.

- To query the information about the vSwitches in a VPC that are associated with a multicast domain, specify the **TransitRouterAttachmentId**

  parameter.

- To query the information about the vSwitches that are associated with a multicast domain, specify the **TransitRouterMulticastDomainId**

  parameter.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListTransitRouterMulticastD omainAssociations | The operation that you want to perform. Set the value to ListTransitRouterMultica stDomainAssociations. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-4266\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRout erMulticast DomainId | String | Query | No | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast domain. |
| TransitRout erAttachme ntId | String | Query | No | tr-attach-p90y3ymbbwuvy5\*\*\*\* | The ID of the network instance connection. |
| ResourceTy pe | String | Query | No | VPC | The type of resource associated with the multicast domain.<br>Valid value: <strong>VPC</strong>. |
| ResourceId | String | Query | No | vpc-p0w9alkte4w2htrqe\*\*\*\* | The ID of the resource associated with the multicast domain. |
| MaxResults | Long | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXG KPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the NextToken parameter. |
| VSwitchIds | Repeat List | Query | No | vsw-p0w9s2ig1jnwgrbzl\*\*\*\* | The vSwitch IDs.<br>You can specify at most 20 vSwitch IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| TransitRouterMul ticastAssociation s | Array |  | The information about the resource associated with the multicast domain. |
| -TransitRouterMul ticastDomainId | String | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast domain. |
| -TransitRouterAtt achmentId | String | tr-attach-p90y3ymbbwuvy5\*\*\*\* | The ID of the network instance connection. |
| -VSwitchId | String | vsw-p0wxk12u6okfkr8xy\*\* \*\* | The vSwitch ID. |
| -Status | String | Dissociating | The status of the associated resource. Valid values:<br>• Associated: The resource is associated with the multicast domain.<br>• Associating: The resource is being associated with the multicast domain.<br>• Dissociating: The resource is being disassociated from the multicast domain. |
| -ResourceType | String | VPC | The type of resource associated with the multicast domain.<br>Valid value: <strong>VPC</strong>. |
| -ResourceOwnerI d | Long | 1210123456123456 | The UID of the level -1 organization to which the resource associated with the multicast domain belongs. |
| -ResourceId | String | vpc-p0w9b7g9l90yofr0n\*\* \*\* | The ID of the resource associated with the multicast domain. |
| RequestId | String | 1CD0969B-A605-5D2D-BFF0-699FD182FB7F | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If a value is returned for <strong>NextToken</strong>, the value indicates the token that is used for the next request to retrieve a new page of results. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomainAssociations
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "TransitRouterMulticastAssociations":{
  "TransitRouterAttachmentId":"tr-attach-p90y3ymbbwuvy5****",
  "Status":"Dissociating",
  "ResourceId":"vpc-p0w9b7g9l90yofr0n****",
  "TransitRouterMulticastDomainId":"tr-mcast-domain-91wpg6wbhchjeq****",
  "VSwitchId":"vsw-p0wxk12u6okfkr8xy****",
  "ResourceType":"VPC",
  "ResourceOwnerId":1210123456123456
 },
 "RequestId":"1CD0969B-A605-5D2D-BFF0-699FD182FB7F",
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "MaxResults":20
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<TransitRouterMulticastAssociations>
 <TransitRouterAttachmentId>tr-attach-p90y3ymbbwuvy5****</TransitRouterAttachmentId>
 <Status>Dissociating</Status>
 <ResourceId>vpc-p0w9b7g9l90yofr0n****</ResourceId>
 <TransitRouterMulticastDomainId>tr-mcast-domain-91wpg6wbhchjeq****
</TransitRouterMulticastDomainId>
 <VSwitchId>vsw-p0wxk12u6okfkr8xy****</VSwitchId>
 <ResourceType>VPC</ResourceType>
 <ResourceOwnerId>1210123456123456</ResourceOwnerId>
</TransitRouterMulticastAssociations>
<RequestId>1CD0969B-A605-5D2D-BFF0-699FD182FB7F</RequestId>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<MaxResults>20</MaxResults>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TransitRo uterMulticastDomainI d | IllegalParam.TransitRouterMulticas tDomainId | The specified TransitRouterMulticastDomainId is illegal. |

<a id="section-1-14-8"></a>

### 1.14.8. RegisterTransitRouterMulticastGroupSources

Creates a multicast source.

**Usage notes**

- You can specify only elastic network interfaces (ENIs) as multicast sources.

- Before you call RegisterTransitRouterMulticastGroupSources, make sure that the vSwitch on which the ENI is created is associated with the multicast domain. For more information, see AssociateTransitRouterMulticastDomain.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | RegisterTransitRouterMultica stGroupSources | The operation that you want to perform. Set the value to RegisterTransitRouterMul <strong>ticastGroupSources</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-4266\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <em>request ID as the client</em> <em>token. The request ID</em> <em>may be different for</em> <em>each request.</em> |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-5mjb5gjb6dgu98\*\*\*\* | The ID of the multicast group to which the multicast source belongs. |
| GroupIpAddr ess | String | Query | Yes | 239.XX.XX.2 | The IP address of the multicast group to which the multicast source belongs.Valid values: <strong>224.0.0.1</strong> to <strong>239.255.255.254</strong>.<br>If the multicast group does not exist in the multicast domain, the system automatically creates the multicast group in the multicast domain. |

<table>
  <tr>
    <td>DryRun</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request.</td>
  </tr>
  <tr>
    <td>VpcId</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>vpc-wz9fusm6zq8uy7cfa****</td>
    <td>The ID of the VPC to which the ENI belongs.<br>• If the ENI belongs to the current Alibaba Cloud account, ignore this parameter.<br>• If the ENI belongs to a different Alibaba Cloud account, you must set this parameter.</td>
  </tr>
  <tr>
    <td>NetworkInter faceIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>eni-p0w92o2wupc3c05t****</td>
    <td>The ENI IDs.<br><em>This parameter is</em> <em>required.</em></td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 9C5D5D70-0AFF-5E5C-8D8A-E92C90C8FB08 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=RegisterTransitRouterMulticastGroupSources
&TransitRouterMulticastDomainId=tr-mcast-domain-5mjb5gjb6dgu98****
&GroupIpAddress=239.XX.XX.2
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"9C5D5D70-0AFF-5E5C-8D8A-E92C90C8FB08"
}
```

`XML`  format

```xml
<RequestId>9C5D5D70-0AFF-5E5C-8D8A-E92C90C8FB08</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_PEER_MULTICAST_DO MAIN_SOURCE | InvalidOperation.PeerMulticastDom ainSource | Operation is invalid because peer multicast domain can not be group source. |
| 400 | IllegalParam.GroupIpA ddress | IllegalParam.GroupIpAddress | The specified GroupIpAddress is illegal. |
| 400 | InvalidMulticastDomai nId.NotFound | InvalidMulticastDomainId.NotFound | The specified AttachmentId is not found. |
| 400 | IncorrectStatus.Multic astDomainId | IncorrectStatus.MulticastDomainId | The status of MulticastDomainId is incorrect. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | INSTANCE_EXIST | InstanceExist | The instance already exists. |
| 400 | INVALID_OPERATION_NETWORKINTERFACE_NOT_EXIST | InvalidOperation.NetworkInterface NotExist | Operation is invalid bacause network interface not exist. |
| 400 | INVALID_OPERATION_NTR_NETWORKINTERF ACE_NOT_SUPPORT | InvalidOperation.NTRNetworkInterf aceNotSupport | Operation is invalid, due to ntr eni not support. |
| 400 | INSTANCE_NOT_EXIST | InstanceNotExist | The instance is not exist. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_NOT_EX IST | InvalidOperation.MulticastDomainA ssociationNotExist | Operation is invalid because multicast association domain association not exist. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_STATUS | InvalidOperation.MulticastDomainA ssociationStatus | Operation is invalid, due to multicast domain association not Active. |
| 400 | QUOTA_FULL_MULTIC AST_GROUP_PER_DO MAIN | QuotaFull.MulticastGroupPerDomai n | The number of multicast group has exceed the maximum value that can be created. |
| 400 | QUOTA_FULL_MULTIC AST_SOURCE_PER_GR OUP | QuotaFull.MulticastSourcePerGroup | The number of multicast group source has exceed the maximum value that can be created. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-9"></a>

### 1.14.9. DeregisterTransitRouterMulticastGroupSources

Deletes multicast sources.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | DeregisterTransitRouterMulti castGroupSources | The operation that you want to perform. Set the value to DeregisterTransitRouterM <strong>ulticastGroupSources</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-4266\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast group to which the multicast source belongs. |
| GroupIpAddr ess | String | Query | Yes | 239.XX.XX.2 | The IP address of the multicast group to which the multicast source belongs. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. |
| NetworkInter faceIds | Repea tList | Query | No | eni-p0weuda3lszwzjly\*\*\*\* | The IDs of the multicast sources that you want to delete.<br>You can delete at most five multicast sources from a multicast group in each call.<br><em>This parameter is</em> <em>required.</em> |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 53E7E8BE-7F4E-5458-ACCA-9B5C1D6A642D | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeregisterTransitRouterMulticastGroupSources
&TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq****
&GroupIpAddress=239.XX.XX.2
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"53E7E8BE-7F4E-5458-ACCA-9B5C1D6A642D"
}
```

`XML`  format

```xml
<RequestId>53E7E8BE-7F4E-5458-ACCA-9B5C1D6A642D</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterM ulticastDomainId.NotF ound | InvalidTransitRouterMulticastDoma inId.NotFound | The specified TransitRouterMulticastDomainId is not found. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_STATUS | InvalidOperation.MulticastDomainS tatus | Operation is invalid, due to multicast domain not Active. |
| 400 | IncorrectStatus.Multic astGroup | IncorrectStatus.MulticastGroup | The status of MulticastGroup is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-10"></a>

### 1.14.10. RegisterTransitRouterMulticastGroupMembers

Adds multicast members to a multicast group.

**Usage notes**

Transit routers support only elastic network interfaces (ENIs) as multicast members. Make sure that the vSwitches of the ENIs are associated with the multicast domain. For more information, see AssociateTransitRouterMulticastDomain.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | RegisterTransitRouterMultica stGroupMembers | The operation that you want to perform. Set the value to RegisterTransitRouterMul <strong>ticastGroupMembers</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426655440000 | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.<br><em>If you do not specify this</em> <em>parameter, the system</em> <em>automatically uses the</em> <em>request ID as the client</em> <em>token. The request ID</em> <em>may be different for</em> <em>each request.</em> |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast domain to which the multicast members belong. |
| GroupIpAddr ess | String | Query | Yes | 239.XX.XX.2 | The IP address of the multicast group to which the multicast members belong.Valid values: 224.0.0.1 to 239.255.255.254.<br>If the multicast group does not exist in the specified multicast domain, the system automatically creates the multicast group in the multicast domain. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a dry run, without sending the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned.If the request passes the dry run, the <strong>DryRunOperation</strong> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. |
| VpcId | String | Query | No | vpc-wz9fusm6zq8uy7cfa\*\*\*\* | The ID of the VPC to which the ENI belongs.<br>• If the level-1 organization of the ENI is the same as the current organization, you can skip this parameter.<br>• If the level-1 organization of the ENI is different than the current organization, you must specify this parameter. |
| NetworkInter faceIds | Repea tList | Query | No | eni-p0weuda3lszwzjly\*\*\*\* | The ENI ID.<br>You can specify multiple ENIs in each call. Make sure that the total number of specified ENIs and multicast domains does not exceed five. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | EB985B7E-2CF8-5EC9-A7DB-F7C82ABD3ACE | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=RegisterTransitRouterMulticastGroupMembers
&TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq****
&GroupIpAddress=239.XX.XX.2
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"EB985B7E-2CF8-5EC9-A7DB-F7C82ABD3ACE"
}
```

`XML`  format

```xml
<RequestId>EB985B7E-2CF8-5EC9-A7DB-F7C82ABD3ACE</RequestId>
```

**Error codes**

<table>
  <tr>
    <td>HttpCode</td>
    <td>Error code</td>
    <td>Error message</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IllegalParam.GroupIpA ddress</td>
    <td>IllegalParam.GroupIpAddress</td>
    <td>The specified GroupIpAddress is illegal.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>InvalidMulticastDomai nId.NotFound</td>
    <td>InvalidMulticastDomainId.NotFound</td>
    <td>The specified AttachmentId is not found.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IncorrectStatus.Multic astDomainId</td>
    <td>IncorrectStatus.MulticastDomainId</td>
    <td>The status of MulticastDomainId is incorrect.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IncorrectStatus.Cen</td>
    <td>IncorrectStatus.Cen</td>
    <td>The status of Cen is incorrect.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INSTANCE_NOT_EXIST</td>
    <td>InstanceNotExist</td>
    <td>The instance is not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_PEER_MULTICAST_DO MAIN_REGION</td>
    <td>InvalidOperation.PeerMulticastDom ainRegion</td>
    <td>Operation is invalid because to peer multicast domain in the same region with multicast domain.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_MULTICAST_DOMAIN_STATUS</td>
    <td>InvalidOperation.MulticastDomainS tatus</td>
    <td>Operation is invalid, due to multicast domain not Active.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_BANDWIDTH_LIMIT_N OT_EXIST</td>
    <td>InvalidOperation.BandwidthLimitNo tExist</td>
    <td>Operation is invalid because a bandwidth limit not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>ATTACHMENT_NOT_F OUND</td>
    <td>AttachmentNotFound</td>
    <td>"The attachment does not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IncorrectStatus.Attach mentId</td>
    <td>IncorrectStatus.AttachmentId</td>
    <td>The status of AttachmentId is incorrect.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INSTANCE_EXIST</td>
    <td>InstanceExist</td>
    <td>The instance already exists.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_NETWORKINTERFACE_NOT_EXIST</td>
    <td>InvalidOperation.NetworkInterface NotExist</td>
    <td>Operation is invalid bacause network interface not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_NTR_NETWORKINTERF ACE_NOT_SUPPORT</td>
    <td>InvalidOperation.NTRNetworkInterf aceNotSupport</td>
    <td>Operation is invalid, due to ntr eni not support.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INSTANCE_NOT_EXIST</td>
    <td>InstanceNotExist</td>
    <td>The instance is not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_NOT_EX IST</td>
    <td>InvalidOperation.MulticastDomainA ssociationNotExist</td>
    <td>Operation is invalid because multicast association domain association not exist.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_STATUS</td>
    <td>InvalidOperation.MulticastDomainA ssociationStatus</td>
    <td>Operation is invalid, due to multicast domain association not Active.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>InvalidPeerTrMulticast DomainId.NotFound</td>
    <td>InvalidPeerTrMulticastDomainId.No tFound</td>
    <td>The specified PeerTrMulticastDomainId is not found.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IncorrectStatus.PeerTr MulticastDomainId</td>
    <td>IncorrectStatus.PeerTrMulticastDo mainId</td>
    <td>The status of PeerTrMulticastDomainId is incorrect.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>IllegalParam.PeerTrMu lticastDomainId</td>
    <td>IllegalParam.PeerTrMulticastDomai nId</td>
    <td>The specified PeerTrMulticastDomainId is illegal.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>INVALID_OPERATION</td>
    <td>InvalidOperation</td>
    <td>Operation is invalid.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>QUOTA_FULL_MULTIC AST_GROUP_PER_DO MAIN</td>
    <td>QuotaFull.MulticastGroupPerDomai n</td>
    <td>The number of multicast group has exceed the maximum value that can be created.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>QUOTA_FULL_MULTIC AST_MEMBER_PER_GR OUP</td>
    <td>QuotaFull.MulticastMemberPerGrou p</td>
    <td>The number of multicast group member has exceed the maximum value that can be created.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>QUOTA_FULL_MULTIC AST_PEER_MEMBER_P ER_GROUP</td>
    <td>QuotaFull.MulticastPeerMemberPer Group</td>
    <td>The number of multicast group member peer domain has exceed the maximum value that can be created.</td>
  </tr>
  <tr>
    <td>400</td>
    <td>DryRunOperation</td>
    <td>DryRunOperation</td>
    <td>Request validation has been passed with DryRun flag set.</td>
  </tr>
</table>

<a id="section-1-14-11"></a>

### 1.14.11. DeregisterTransitRouterMulticastGroupMembers

Removes multicast members from a multicast group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | DeregisterTransitRouterMulti castGroupMembers | The operation that you want to perform. Set the value to DeregisterTransitRouterM <strong>ulticastGroupMembers</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426655440000 | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRoute rMulticastDo mainId | String | Query | Yes | tr-mcast-domain-91wpg6wbhchjeq\*\*\*\* | The ID of the multicast domain to which the multicast members belong. |
| GroupIpAddr ess | String | Query | Yes | 239.XX.XX.2 | The IP address of the multicast group to which the multicast members belong. |
| DryRun | Boole an | Query | No | false | Specifies whether to perform a only dry run, without performing the actual request. Valid values:<br>• <strong>true</strong>: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong> (default): performs a dry run and performs the actual request. |
| NetworkInter faceIds | Repea tList | Query | No | eni-p0weuda3lszwzjly\*\*\*\* | The IDs of ENIs.<br>You can delete multiple ENIs at a time. Make sure that you specify 5 ENIs or less. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 61D0A553-5E4E-53B5-9DA3-01CBA076A286 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeregisterTransitRouterMulticastGroupMembers
&TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq****
&GroupIpAddress=239.XX.XX.2
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"61D0A553-5E4E-53B5-9DA3-01CBA076A286"
}
```

`XML`  format

```xml
<RequestId>61D0A553-5E4E-53B5-9DA3-01CBA076A286</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidTransitRouterM ulticastDomainId.NotF ound | InvalidTransitRouterMulticastDoma inId.NotFound | The specified TransitRouterMulticastDomainId is not found. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_STATUS | InvalidOperation.MulticastDomainS tatus | Operation is invalid, due to multicast domain not Active. |
| 400 | IncorrectStatus.Multic astGroup | IncorrectStatus.MulticastGroup | The status of MulticastGroup is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

<a id="section-1-14-12"></a>

### 1.14.12. ListTransitRouterMulticastGroups

Queries the multicast sources and members in a multicast domain.

**Usage notes**

You can call the ListTransitRouterMulticastGroups operation to query the multicast sources and members in a multicast domain. Multicast sources and members are also known as multicast resources.

- If you set **GroupIpAddress**, the system queries multicast resources in the multicast domain by multicast group.

- If you set **VSwitchIds**, the system queries multicast resources in the multicast domain by vSwitch.

- If you set **ResourceType**, the system queries the multicast resources of the specified type in the multicast domain.

- If you set **ResourceId**, the system queries multicast resources by resource.

- If you set only **TransitRouterMulticastDomainId**, the system queries all the multicast resources in the multicast domain.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListTransitRouterMulticastGro ups | The operation that you want to perform. Set the value to ListTransitRouterMulticas <strong>tGroups</strong>. |
| ClientToken | String | Query | No | 123e4567-e89b-12d3-a456-426655440000 | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. |
| TransitRoute rMulticastDo mainId | String | Query | No | tr-mcast-domain-5mjb5gjb6dgu98\*\*\*\* | The ID of the multicast domain. |
| GroupIpAddr ess | String | Query | No | 239.XX.XX.2 | The IP address of the multicast group.<br>Each multicast group is identified by its IP address. |
| TransitRoute rAttachment Id | String | Query | No | tr-attach-g3kz2k3u76amsk\*\*\*\* | The ID of the network instance connection. |
| ResourceTyp e | String | Query | No | VPC | The type of the multicast resource.<br>Set the value to <strong>VPC</strong> to query multicast resources in a VPC. |
| ResourceId | String | Query | No | vpc-p0w9alkte4w2htrqe\*\*\*\* | The ID of the resource associated with the multicast resource. |
| MaxResults | Long | Query | No | 20 | The number of entries per page. Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGK Pd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first query and no subsequent queries are to be sent, ignore this parameter.<br>• If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results. |
| IsGroupSour ce | Boole an | Query | No | true | Specifies whether to query the multicast sources. Valid values:<br>• false<br>• true<br><em>This parameter must be</em> <em>specified together with</em> <em>the IsGroupMember</em> <em>parameter.</em> |
| IsGroupMem ber | Boole an | Query | No | false | Specified whether to query the multicast members. Valid values:<br>• false<br>• true<br><em>This parameter must be</em> <em>specified together with</em> <em>the IsGroupMember</em> <em>parameter.</em> |
| VSwitchIds | Repea tList | Query | No | vsw-p0w9s2ig1jnwgrbzl\*\*\*\* | The IDs of the vSwitches.<br>You can specify at most 20 IDs. |
| NetworkInter faceIds | Repea tList | Query | No | eni-p0weuda3lszwzjly\*\*\*\* | The IDs of ENIs.<br>You can specify up to 20 ENIs. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| TransitRouterMul ticastGroups | Array |  | A list of multicast groups. |
| -GroupIpAddress | String | 239.XX.XX.2 | The IP address of the multicast group to which the multicast resource belongs. |
| -TransitRouterAtt achmentId | String | tr-attach-g3kz2k3u76amsk\*\*\*\* | The ID of the network instance connection. |
| -VSwitchId | String | vsw-p0w9s2ig1jnwgrbzl\*\*\* \* | The ID of the vSwitch to which the multicast resource belongs. |
| -NetworkInterface Id | String | eni-p0weuda3lszwzjly\*\*\*\* | The ID of the ENI, which is a multicast resource. |
| -Status | String | Registered | The status of the multicast resource. Valid values:<br>• <strong>Registering</strong>: being created<br>• <strong>Registered</strong>: available<br>• <strong>Deregistering</strong>: being deleted |
| -GroupSource | Boolean | false | Indicates whether the multicast resource is a multicast source. Valid values:<br>• <strong>true</strong>: yes<br>• <strong>false</strong>: no |
| -GroupMember | Boolean | true | Indicates whether the multicast resource is a multicast member. Valid values:<br>• <strong>true</strong>: yes<br>• <strong>false</strong>: no |
| -MemberType | String | Static | The type of the multicast source.<br>If the value is <strong>Static</strong>, the multicast source is manually specified. |
| -SourceType | String | Static | The type of the multicast member.<br>If the value is <strong>Static</strong>, the multicast member is manually specified. |
| -ResourceType | String | VPC | The type of the multicast resource.<br><strong>VPC</strong>: The multicast resource is in a VPC. |
| -ResourceOwnerI d | Long | 1250123456123456 | The UID of the level -1 organization to which the resource associated with the multicast resource belongs. |
| -ResourceId | String | vpc-p0w9alkte4w2htrqe\*\* \*\* | The ID of the resource associated with the multicast resource. |
| -TransitRouterMul ticastDomainId | String | tr-mcast-domain-kx0vk0v7fz8kx4\*\*\*\* | The ID of the multicast domain. |
| RequestId | String | FB3C4A16-0933-5850-9D43-0C3EA37BCBFB | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If a value is returned for <strong>NextToken</strong>, the value indicates the token that is used for the next request to retrieve a new page of results. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastGroups
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "RequestId":"FB3C4A16-0933-5850-9D43-0C3EA37BCBFB",
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "MaxResults":20,
 "TransitRouterMulticastGroups":{
  "TransitRouterAttachmentId":"tr-attach-g3kz2k3u76amsk****",
  "Status":"Registered",
  "GroupMember":true,
  "VSwitchId":"vsw-p0w9s2ig1jnwgrbzl****",
  "SourceType":"Static",
  "ConnectPeerId":"tr-connect-peer-ax66ixf6ubbajw****",
  "ResourceType":"VPC",
  "NetworkInterfaceId":"eni-p0weuda3lszwzjly****",
  "ResourceOwnerId":1250123456123456,
  "GroupIpAddress":"239.XX.XX.2",
  "PeerTransitRouterMulticastDomainId":"tr-mcast-domain-91wpg6wbhchjeq****",
  "MemberType":"Static",
  "ResourceId":"vpc-p0w9alkte4w2htrqe****",
  "TransitRouterMulticastDomainId":"tr-mcast-domain-kx0vk0v7fz8kx4****",
  "GroupSource":false
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<RequestId>FB3C4A16-0933-5850-9D43-0C3EA37BCBFB</RequestId>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<MaxResults>20</MaxResults>
<TransitRouterMulticastGroups>
 <TransitRouterAttachmentId>tr-attach-g3kz2k3u76amsk****</TransitRouterAttachmentId>
 <Status>Registered</Status>
 <GroupMember>true</GroupMember>
 <VSwitchId>vsw-p0w9s2ig1jnwgrbzl****</VSwitchId>
 <SourceType>Static</SourceType>
 <ConnectPeerId>tr-connect-peer-ax66ixf6ubbajw****</ConnectPeerId>
 <ResourceType>VPC</ResourceType>
 <NetworkInterfaceId>eni-p0weuda3lszwzjly****</NetworkInterfaceId>
 <ResourceOwnerId>1250123456123456</ResourceOwnerId>
 <GroupIpAddress>239.XX.XX.2</GroupIpAddress>
 <PeerTransitRouterMulticastDomainId>tr-mcast-domain-91wpg6wbhchjeq****
</PeerTransitRouterMulticastDomainId>
 <MemberType>Static</MemberType>
 <ResourceId>vpc-p0w9alkte4w2htrqe****</ResourceId>
 <TransitRouterMulticastDomainId>tr-mcast-domain-kx0vk0v7fz8kx4****
</TransitRouterMulticastDomainId>
 <GroupSource>false</GroupSource>
</TransitRouterMulticastGroups>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TransitRo uterMulticastDomainI d | IllegalParam.TransitRouterMulticas tDomainId | The specified TransitRouterMulticastDomainId is illegal. |

<a id="section-1-14-13"></a>

### 1.14.13. ListGrantVSwitchEnis

Queries the information about elastic network interfaces (ENIs) that can serve as multicast sources or multicast members in a virtual private cloud (VPC).

**Usage notes**

Before you call the ListGrantVSwitchEnis operation, make sure that the VPC is attached to a transit router. For more information, see CreateTransitRouterVpcAttachment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | Yes | ListGrantVSwitchEnis | The operation that you want to perform. Set the value to <strong>ListGrantVSwitchEnis</strong>. |
| CenId | String | Query | Yes | cen-a7syd349kne38g\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance to which the VPC is attached. |
| VpcId | String | Query | Yes | vpc-p0w9alkte4w2htrqe\*\*\*\* | The VPC ID. |
| VSwitchId | String | Query | Yes | vsw-p0w9s2ig1jnwgrbzl\*\*\*\* | The ID of a vSwitch in the VPC.<br>You can specify only one vSwitch in each call. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| GrantVSwitchEni s | Array |  | The information about the ENI. |
| -VpcId | String | vpc-p0w9alkte4w2htrqe\*\* \*\* | The VPC ID. |
| -VSwitchId | String | vsw-p0w9s2ig1jnwgrbzl\*\*\* \* | The vSwitch ID. |
| -NetworkInterface Id | String | eni-p0w172vv82kxzb49\*\* \*\* | The ENI ID. |
| -Description | String | created by CBN | The ENI description. |
| -TransitRouterFla g | Boolean | false | Indicates whether the ENI is created by a transit router. Valid values:<br>• true<br>• false<br>ENIs that are created by transit routers cannot be used as multicast sources or members. |
| RequestId | String | DBFE1736-2F33-5309-9954-875B11E9519D | The request ID. |
| TotalCount | String | 6 | The total number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListGrantVSwitchEnis
&CenId=cen-a7syd349kne38g****
&VpcId=vpc-p0w9alkte4w2htrqe****
&VSwitchId=vsw-p0w9s2ig1jnwgrbzl****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":"6",
 "RequestId":"DBFE1736-2F33-5309-9954-875B11E9519D",
 "GrantVSwitchEnis":{
  "Description":"created by CBN",
  "TransitRouterFlag":false,
  "VpcId":"vpc-p0w9alkte4w2htrqe****",
  "VSwitchId":"vsw-p0w9s2ig1jnwgrbzl****",
  "NetworkInterfaceId":"eni-p0w172vv82kxzb49****"
 }
}
```

`XML`  format

```xml
<TotalCount>6</TotalCount>
<RequestId>DBFE1736-2F33-5309-9954-875B11E9519D</RequestId>
<GrantVSwitchEnis>
 <Description>created by CBN</Description>
 <TransitRouterFlag>false</TransitRouterFlag>
 <VpcId>vpc-p0w9alkte4w2htrqe****</VpcId>
 <VSwitchId>vsw-p0w9s2ig1jnwgrbzl****</VSwitchId>
 <NetworkInterfaceId>eni-p0w172vv82kxzb49****</NetworkInterfaceId>
</GrantVSwitchEnis>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidCenId.NotFoun d | InvalidCenId.NotFound | The specified CenId is not found. |
| 400 | InvalidVpcId.NotFound | InvalidVpcId.NotFound | The specified VpcId is not found. |
| 400 | INVALID_OPERATION_MULTICAST_DOMAIN_ASSOCIATION_NOT_EX IST | InvalidOperation.MulticastDomainA ssociationNotExist | Operation is invalid because multicast association domain association not exist. |

<a id="section-1-14-14"></a>

### 1.14.14. ListTransitRouterMulticastDomainVSwitches

Queries the vSwitches of multicast domains in a virtual private cloud (VPC).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ListTransitRouterMulticastDo mainVSwitches | The operation that you want to perform. Set the value to ListTransitRouterMulticas <strong>tDomainVSwitches</strong>. |
| CenId | String | Query | Yes | cen-44m0p68spvlrqq\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| VpcId | String | Query | Yes | vpc-p0wr1cd4fcuxy3ui0\*\*\*\* | The VPC ID. |
| MaxResults | Integ er | Query | No | 20 | The number of entries per page. Minimum value: <strong>0</strong>.Default value: <strong>20</strong>. |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGK Pd\*\*\*\* | The pagination token that is used in the next request to retrieve a new page of results. Valid values:<br>• If this is your first request or no next requests are to be sent, you do not need to specify this parameter.<br>• You must specify the token that is obtained from the previous query as the value of the <strong>NextToken</strong> parameter. |
| VSwitchIds | Repea tList | Query | No | The vSwitch IDs. | The vSwitch IDs.<br>You can specify at most 50 vSwitch IDs in each call. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| VSwitchIds | String | vsw-p0w5ejr9bzfsttiza\*\*\*\* | The vSwitch IDs. |
| NextToken | String | FFmyTO70tTpLG6I3F mYAXGKPd\*\*\*\* | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:<br>• If <strong>NextToken</strong> is empty, no next page exists.<br>• If the value returned of <strong>NextToken</strong> is not empty, the value indicates the token that is used for the next query. |
| RequestId | String | B0E7E43C-979A-5130-AA0D-B3ADA69E0827 | The request ID. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| MaxResults | Integer | 20 | The number of entries per page. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomainVSwitches
&CenId=cen-44m0p68spvlrqq****
&VpcId=vpc-p0wr1cd4fcuxy3ui0****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":2,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"B0E7E43C-979A-5130-AA0D-B3ADA69E0827",
 "VSwitchIds":"vsw-p0w5ejr9bzfsttiza****",
 "MaxResults":20
}
```

`XML`  format

```xml
<TotalCount>2</TotalCount>
<NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken>
<RequestId>B0E7E43C-979A-5130-AA0D-B3ADA69E0827</RequestId>
<VSwitchIds>vsw-p0w5ejr9bzfsttiza****</VSwitchIds>
<MaxResults>20</MaxResults>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IllegalParam.NextToke n | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstanc e | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |

<a id="section-1-15"></a>

## 1.15. Routing policies

<a id="section-1-15-1"></a>

### 1.15.1. CreateCenRouteMap

Creates a routing policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | CreateCenRouteMap | The operation that you want to perform. Set the value to <strong>CreateCenRouteMap</strong>. |
| CenId | String | Query | Yes | cen-7qthudw0ll6jmc\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| CenRegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the routing policy.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |

<table>
  <tr>
    <td>TransmitDire ction</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>RegionIn</td>
    <td>The direction in which the routing policy is applied.Valid values:<br>• <strong>RegionIn</strong>: Routes are advertised to the gateways in the regions that are connected by the CEN instance.<br>For example, routes are advertised from network instances deployed in the current region or other regions to the gateway deployed in the current region.<br>• <strong>RegionOut</strong>: Routes are advertised from the gateways in the regions that are connected by the CEN instance.<br>For example, routes are advertised from the gateway deployed in the current region to network instances deployed in the same region, or to gateways deployed in other regions.</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>desctest</td>
    <td>The description of the routing policy.<br>The description must be 2 to 256 characters in length, and can contain letters, digits, hyphens (-), periods (.), and underscores (_). It must start with a letter and cannot start with <code> http:// </code> or <code> https:// </code>.</td>
  </tr>
  <tr>
    <td>Priority</td>
    <td>Integ er</td>
    <td>Query</td>
    <td>Yes</td>
    <td>3</td>
    <td>Enter a priority for the routing policy. Valid values: <strong>1</strong> to <strong>100</strong>. A smaller value indicates a higher priority.<br><em>You cannot specify the</em> <em>same priority for routing</em> <em>policies that apply in the</em> <em>same region and</em> <em>direction. The system</em> <em>evaluates routes based</em> <em>on the match conditions</em> <em>of routing policies in</em> <em>descending order of</em> <em>priority. A smaller value</em> <em>specifies a higher</em> <em>priority. To sort routing</em> <em>policies in the expected</em> <em>order, you must specify</em> <em>appropriate values.</em></td>
  </tr>
  <tr>
    <td>MapResult</td>
    <td>String</td>
    <td>Query</td>
    <td>Yes</td>
    <td>Permit</td>
    <td>The action to be performed on a route that meets all the match conditions. Valid values:<br>• Permit<br>• Deny</td>
  </tr>
  <tr>
    <td>NextPriority</td>
    <td>Integ er</td>
    <td>Query</td>
    <td>No</td>
    <td>20</td>
    <td>The priority of the next routing policy that you want to associate with the current routing policy.<br>• This parameter takes effect only when the <strong>MapResult</strong> parameter is set to <strong>Permit</strong>. This way, the permitted route is matched against the next routing policy.<br>• The region and direction of the routing policy to be associated must be the same as those of the current routing policy.<br>• The priority of the next routing policy must be lower than the priority of the current routing policy.</td>
  </tr>
  <tr>
    <td>CidrMatchM ode</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>Include</td>
    <td>The match method that is used to match routes based on the prefix. Valid values:<br>• <strong>Include</strong>: fuzzy match. A route is a match if the route prefix is included in the match conditions.<br>For example, if you set the match condition to 10.10.0.0/16 and fuzzy match is applied, the route whose prefix is 10.10.1.0/24 meets the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the route prefix is the same as the prefix specified in the match condition.<br>For example, if you set the match condition to 10.10.0.0/16 and exact match is enabled, a route is a match only if the prefix is 10.10.0.0/16.</td>
  </tr>
  <tr>
    <td>AsPathMatch Mode</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>Include</td>
    <td>The match method that is used to evaluate routes based on the AS path. Valid values:<br>• <strong>Include</strong>: fuzzy match. A route meets the match condition if the AS path of the route overlaps with the AS path specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the AS path of the route is the same as the AS path specified in the match condition.</td>
  </tr>
  <tr>
    <td>Community MatchMode</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>Include</td>
    <td>The match method that is used to evaluate routes based on the community.Valid values:<br>• <strong>Include</strong>: fuzzy match. A route meets the match condition if the community of the route overlaps with the community specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route meets the match condition only if the community of the route is the same as the community specified in the match condition.</td>
  </tr>
  <tr>
    <td>Community OperateMod e</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>Additive</td>
    <td>The action that is performed on the community. Valid values:<br>• <strong>Additive</strong>: adds the community to the route.<br>• <strong>Replace</strong>: replaces the original community of the route.<br>The parameter specifies the action to be performed when a route meets the match condition.</td>
  </tr>
  <tr>
    <td>Preference</td>
    <td>Integ er</td>
    <td>Query</td>
    <td>No</td>
    <td>50</td>
    <td>The new priority of the route.<br>Valid values: <strong>1</strong> to <strong>100</strong>. The default priority is <strong>50</strong>. A smaller value indicates a higher priority.<br>This parameter specifies the action to be performed when a route meets the match condition.</td>
  </tr>
  <tr>
    <td>SourceInsta nceIdsRever seMatch</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to exclude the source network instance IDs. Valid values:<br>• <strong>false</strong> (default value): A route meets the match condition if its source network instance ID is in the list specified by <strong>SourceInstanceIds.N</strong>.<br>• <strong>true</strong>: A route is a match if its source network instance ID is not in the list specified by <strong>SourceInstanceIds.N</strong>.</td>
  </tr>
  <tr>
    <td>DestinationI nstanceIdsR everseMatch</td>
    <td>Boole an</td>
    <td>Query</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to exclude the destination network instance IDs. Valid values:<br>• <strong>false</strong> (default value): A route meets the match condition if its destination network instance ID is in the list specified by DestinationInstanceIds.<strong>N</strong>.<br>• <strong>true</strong>: A route meets the match condition if its destination network instance ID is not in the list specified by DestinationInstanceIds.<strong>N</strong>.</td>
  </tr>
  <tr>
    <td>MatchAddre ssType</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>IPv4</td>
    <td>The type of IP address in the match condition. Valid values:<br>• <strong>IPv4</strong>: IPv4 address<br>• <strong>IPv6</strong>: IPv6 address<br>This parameter can be empty. If no value is specified, all types of IP address are a match.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteTableI d</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-gw8nx3515m1mbd1z1****</td>
    <td>The ID of the route table of the transit router.<br>If you do not specify a route table ID, the routing policy is automatically associated with the default route table of the transit router.</td>
  </tr>
  <tr>
    <td>SourceInsta nceIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vpc-adeg3544fdf34vf****</td>
    <td>The IDs of the source network instances from which routes are evaluated.The following network instance types are supported:<br>• VPC<br>• VBR<br>You can enter at most 32 IDs.</td>
  </tr>
  <tr>
    <td>DestinationI nstanceIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vpc-afrfs434465fdf****</td>
    <td>The IDs of the destination network instances to which routes are evaluated. The following network instance types are supported:<br>• VPC<br>• VBR<br>You can enter at most 32 IDs.<br><em>The destination network</em> <em>instance IDs are valid</em> <em>only if the routing policy</em> <em>is applied to scenarios</em> <em>where routes are</em> <em>advertised from the</em> <em>gateway in the current</em> <em>region to network</em> <em>instances in the current</em> <em>region.</em></td>
  </tr>
  <tr>
    <td>SourceRoute TableIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-adfr233vf34rvd4****</td>
    <td>The IDs of the source route tables from which routes are evaluated. You can enter at most 32 route table IDs.</td>
  </tr>
  <tr>
    <td>DestinationR outeTableIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-adefrgtr144vf****</td>
    <td>The IDs of the destination route tables to which the routes belong. You can enter at most 32 route table IDs.<br><em>The destination route</em> <em>table IDs are valid only</em> <em>when the routing policy</em> <em>is applied to scenarios</em> <em>where routes are</em> <em>advertised from the</em> <em>gateway in the current</em> <em>region to route tables in</em> <em>the current region.</em></td>
  </tr>
  <tr>
    <td>SourceRegio nIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>cn-qingdao-env17e-d01</td>
    <td>The IDs of the source regions from which routes are evaluated. You can enter at most 32 region IDs.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list.</td>
  </tr>
  <tr>
    <td>SourceChildI nstanceType s</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>VPC</td>
    <td>The types of source network instances from which routes are evaluated. The following types of network instances are supported:<br>• VPC<br>• VBR<br>You can specify one or more network instance types.</td>
  </tr>
  <tr>
    <td>DestinationC hildInstance Types</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>VPC</td>
    <td>The types of destination network instance to which the routes point. The following types of network instance are supported:<br>• VPC<br>• VBR<br>You can specify one or more network instance types.<br><em>The destination network</em> <em>instance types are valid</em> <em>only if the routing policy</em> <em>is applied to scenarios</em> <em>where routes are</em> <em>advertised from the</em> <em>gateway in the current</em> <em>region to network</em> <em>instances in the current</em> <em>region.</em></td>
  </tr>
  <tr>
    <td>DestinationC idrBlocks</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>10.10.10.0/24</td>
    <td>The prefixes of matching routes.<br>You must specify the IP addresses in CIDR notation.You can enter at most 32 CIDR blocks.</td>
  </tr>
  <tr>
    <td>RouteTypes</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>System</td>
    <td>The type of route to be matched against the match conditions. Valid values: The following route types are supported:<br>• <strong>System</strong>: system routes that are automatically generated by the system.<br>• <strong>Custom</strong>: custom routes that are manually added.<br>• <strong>BGP</strong>: routes that are advertised over Border Gateway Protocol (BGP).<br>You can specify multiple route types.</td>
  </tr>
  <tr>
    <td>MatchAsns</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501</td>
    <td>The AS paths based on which routes are compared.<br>You can specify at most 32 AS numbers.<br><em>Only AS SEQUENCE is</em> <em>supported. AS SET, AS</em> <em>CONFED SEQUENCE,</em> <em>and AS CONFED SET are</em> <em>not supported. In other</em> <em>words, only the AS</em> <em>number list is</em> <em>supported. Sets and</em> <em>sub-lists are not</em> <em>supported.</em></td>
  </tr>
  <tr>
    <td>MatchComm unitySet</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501:1</td>
    <td>The community set based on which routes are evaluated.<br>Specify the community in the format of n:m. Valid values of n and m: <strong>1</strong> to <strong>65535</strong>. Each community must comply with the RFC 1997 standard. The RFC 8092 standard that defines BGP large communities is not supported.<br>You can enter at most 32 communities.<br><em>If the configurations of</em> <em>the communities are</em> <em>incorrect, routes may</em> <em>fail to be advertised to</em> <em>your data center.</em></td>
  </tr>
  <tr>
    <td>OperateCom munitySet</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501:1</td>
    <td>The community set on which actions are performed.<br>Specify the community in the format of n:m. Valid values of n and m: <strong>1</strong> to <strong>65535</strong>. Each community must comply with RFC 1997. The RFC 8092 standard that defines BGP large communities is not supported.<br>You can enter at most 32 communities.<br><em>If the configurations of</em> <em>the communities are</em> <em>incorrect, routes may</em> <em>fail to be advertised to</em> <em>your data center.</em></td>
  </tr>
  <tr>
    <td>PrependAsP ath</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501</td>
    <td>The AS paths that are prepended by using an action statement when regional gateways receive or advertise routes.<br>The AS paths vary based on the direction in which the routing policy is applied:<br>• If AS paths are prepended to a routing policy that is applied in the inbound direction, you must specify source network instance IDs and the source region in the match condition. In addition, the source region must be the same as the region where the routing policy is applied.<br>• If AS paths are prepended to a routing policy that is applied in the outbound direction, you must specify destination network instance IDs in the match condition.<br>This parameter specifies the action to be performed when a route meets the match condition. You can specify at most 32 AS numbers.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RouteMapId | String | cenrmap-w4yf7toozfol3q\*\*\*\* | The ID of the routing policy. |
| RequestId | String | 62172DD5-6BAC-45DF-8D44-56SDF467BAC | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateCenRouteMap
&CenId=cen-7qthudw0ll6jmc****
&CenRegionId=cn-qingdao-env17e-d01
&TransmitDirection=RegionIn
&Priority=3
&MapResult=Permit
&Common request parameters
```

Sample success responses `JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"62172DD5-6BAC-45DF-8D44-56SDF467BAC",
 "RouteMapId":"cenrmap-w4yf7toozfol3q****"
}
```

`XML`  format

```xml
<RequestId>62172DD5-6BAC-45DF-8D44-56SDF467BAC</RequestId>
<RouteMapId>cenrmap-w4yf7toozfol3q****</RouteMapId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_ROUTEMAP_CONFIG_E XIST | Forbidden.CenRouteMapExist | The specified CEN route map ID already exists. |
| 400 | PARAMETER_ILLEGAL_RMAP_SRC_REGION | Invid.Parameter | When using PrependAsPath in the RegionIn, SourceRegionId must be local region Id. |
| 400 | INVALID_OPERATION_ROUTE_MAP_INVALID_ACTION | InvalidOperation.NoEffictiveAction | No effective action be configured. |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_SRC_REGION_EMP TY | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be null |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_GW_ZONE_EMPTY | Invid.Parameter | When using GatewayRegionId, GatewayZoneId must not be null |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_SRC_REGION_ILLE GAL | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be the same with tr region id |
| 400 | PARAMETER_ILLEGAL_RMAP_GW_REGION_ID | Invid.Parameter | GatewayRegionId is invalid |
| 400 | INVALID_OPERATION_TRANSITROUTER_NOT _EXIST | Invid.Parameter | TransitRouter not exist. |
| 400 | PARAMETER_ILLEGAL_RMAP_SRC_INSTANCE | Invid.Parameter | SourceInstanceId is invalid. |
| 400 | PARAMETER_ILLEGAL_RMAP_DEST_INSTANC E | Invid.Parameter | DestinationInstanceId is invalid. |
| 400 | IncorrectStatus.Transi tRouter | IncorrectStatus.TransitRouterInsta nce | The status of TransitRouter is incorrect. |

<a id="section-1-15-2"></a>

### 1.15.2. ModifyCenRouteMap

Modifies a routing policy of a Cloud Enterprise Network (CEN) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | ModifyCenRouteMap | The operation that you want to perform. Set the value to <strong>ModifyCenRouteMap</strong>. |
| CenId | String | Query | Yes | cen-7qthudw0ll6jmc\*\*\*\* | The ID of the CEN instance. |
| CenRegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the routing policy.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| RouteMapId | String | Query | Yes | cenrmap-abcdedfghij\*\*\*\* | The ID of the routing policy. |
| Description | String | Query | No | desctest | The description of the routing policy.<br>The description cannot start with <code> http:// </code> or <code> https:// </code>. It must start with a letter and can contain letters, digits, hyphens (-), periods (.), and underscores (_). |
| MapResult | String | Query | Yes | Permit | The action to be performed on a route that meets all the match conditions. Valid values:<br>• Permit<br>• Deny |
| NextPriority | Integ er | Query | No | 20 | The priority of the next routing policy that you want to associate with the current routing policy.<br>• This parameter takes effect only when the <strong>MapResult</strong> parameter is set to <strong>Permit</strong>. This way, the permitted route is matched against the next routing policy.<br>• The region and direction of the routing policy to be associated must be the same as those of the current routing policy.<br>• The priority of the routing policy to be associated must be lower than the priority of the current routing policy. |
| CidrMatchM ode | String | Query | No | Include | The match method that is used to match routes based on the prefix. Valid values:<br>• <strong>Include</strong>: fuzzy match. A route is a match if the route prefix is included in the match conditions.<br>For example, if you set the match condition to 10.10.0.0/16 and fuzzy match is applied, the route whose prefix is 10.10.1.0/24 meets the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the route prefix is the same as the prefix specified in the match condition.<br>For example, if you set the match condition to 10.10.0.0/16 and exact match is enabled, a route is a match only if the prefix is 10.10.0.0/16. |
| AsPathMatch Mode | String | Query | No | Include | The match method that is used to evaluate routes based on the AS path. Valid values:<br>• <strong>Include</strong>: fuzzy match. A route meets the match condition if the AS path of the route overlaps with the AS path specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the AS path of the route is the same as the AS path specified in the match condition. |
| Community MatchMode | String | Query | No | Include | The match method that is used to evaluate routes based on the community.Valid values:<br>• <strong>Include</strong>: fuzzy match. A route meets the match condition if the community of the route overlaps with the community specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route meets the match condition only if the community of the route is the same as the community specified in the match condition. |
| Community OperateMod e | String | Query | No | Additive | The action that is performed on the community. Valid values:<br>• <strong>Additive</strong>: adds the community to the route.<br>• <strong>Replace</strong>: replaces the original community of the route.<br>The parameter specifies the action to be performed when a route meets the match condition. |
| Preference | Integ er | Query | No | 22 | The new priority of the route.<br>Valid values: <strong>1</strong> to <strong>100</strong>. The default priority is <strong>50</strong>. A smaller value indicates a higher priority.<br>This parameter specifies the action to be performed when a route meets the match condition. |
| Priority | Integ er | Query | Yes | 10 | Enter a priority for the routing policy. Valid values: <strong>1</strong> to <strong>100</strong>. A smaller value indicates a higher priority.<br><em>You cannot specify the</em> <em>same priority for routing</em> <em>policies that apply in the</em> <em>same region and</em> <em>direction. The system</em> <em>evaluates routes based</em> <em>on the match conditions</em> <em>of routing policies in</em> <em>descending order of</em> <em>priority. A smaller value</em> <em>specifies a higher</em> <em>priority. To sort routing</em> <em>policies in the expected</em> <em>order, you must specify</em> <em>appropriate values.</em> |
| SourceInsta nceIdsRever seMatch | Boole an | Query | No | false | Specifies whether to exclude the source network instance IDs. Valid values:<br>• <strong>false</strong> (default value): A route meets the match condition if its source network instance ID is in the list specified by <strong>SourceInstanceIds.N</strong>.<br>• <strong>true</strong>: A route is a match if its source network instance ID is not in the list specified by <strong>SourceInstanceIds.N</strong>. |
| DestinationI nstanceIdsR everseMatch | Boole an | Query | No | false | Specifies whether to exclude the destination network instance IDs. Valid values:<br>• <strong>false</strong> (default value): A route meets the match condition if its destination network instance ID is in the list specified by DestinationInstanceIds.<strong>N</strong>.<br>• <strong>true</strong>: A route meets the match condition if its destination network instance ID is not in the list specified by DestinationInstanceIds.<strong>N</strong>. |
| MatchAddre ssType | String | Query | No | IPv4 | The type of IP address in the match condition. Valid values:<br>• <strong>IPv4</strong>: IPv4 address<br>• <strong>IPv6</strong>: IPv6 address<br>This parameter can be empty. If no value is specified, all types of IP address are a match. |

<table>
  <tr>
    <td>SourceInsta nceIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vpc-afsfdf5435vcvc****</td>
    <td>The IDs of the source network instances from which routes are evaluated.The following network instance types are supported:<br>• Virtual private cloud (VPC)<br>• Virtual border router (VBR)<br>• Cloud Connect Network (CCN) instance<br>• Smart Access Gateway (SAG) instance<br>• The ID of the IPsec-VPN connection.<br>You can enter at most 32 IDs.</td>
  </tr>
  <tr>
    <td>DestinationI nstanceIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vpc-avcdsg34ds****</td>
    <td>The IDs of the destination network instances to which the routes belong. The following network instance types are supported:<br>• VPC<br>• VBR<br>• CCN instance<br>• SAG instance<br>• The ID of the IPsec-VPN connection.<br>You can enter at most 32 IDs.<br><em>The destination network</em> <em>instance IDs are valid</em> <em>only if the routing policy</em> <em>is applied to scenarios</em> <em>where routes are</em> <em>advertised from the</em> <em>gateway in the current</em> <em>region to network</em> <em>instances in the current</em> <em>region.</em></td>
  </tr>
  <tr>
    <td>SourceRoute TableIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-acdbvtbr342cd****</td>
    <td>The IDs of the source route tables from which routes are evaluated. You can enter at most 32 route table IDs.</td>
  </tr>
</table>

<table>
  <tr>
    <td>DestinationR outeTableIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-adfg53c322v****</td>
    <td>The IDs of the destination route tables to which the routes belong. You can enter at most 32 route table IDs.<br><em>The destination route</em> <em>table IDs are valid only</em> <em>when the routing policy</em> <em>is applied to scenarios</em> <em>where routes are</em> <em>advertised from the</em> <em>gateway in the current</em> <em>region to route tables in</em> <em>the current region.</em></td>
  </tr>
  <tr>
    <td>SourceRegio nIds</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>cn-qingdao-env17e-d01</td>
    <td>The IDs of the source regions from which routes are evaluated. You can enter at most 32 region IDs.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list.</td>
  </tr>
  <tr>
    <td>SourceChildI nstanceType s</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>VPC</td>
    <td>The types of source network instances from which routes are evaluated. The following types of network instances are supported:<br>• VPC<br>• VBR</td>
  </tr>
  <tr>
    <td>DestinationC hildInstance Types</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>VPC</td>
    <td>The types of destination network instance to which the routes point. The following types of network instance are supported:<br>• VPC<br>• VBR<br>The destination network instance types are valid only if the routing policy is applied to scenarios where routes are advertised from the gateway in the current region to network instances in the current region.</td>
  </tr>
  <tr>
    <td>DestinationC idrBlocks</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>10.10.10.0/24</td>
    <td>The prefixes of matching routes.<br>You must specify the IP addresses in CIDR notation.You can enter at most 32 CIDR blocks.</td>
  </tr>
  <tr>
    <td>RouteTypes</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>System</td>
    <td>The type of route to be matched against the match conditions. Valid values: The following route types are supported:<br>• <strong>System</strong>: system routes that are automatically generated by the system.<br>• <strong>Custom</strong>: custom routes that are manually added.<br>• <strong>BGP</strong>: routes that are advertised over Border Gateway Protocol (BGP).</td>
  </tr>
  <tr>
    <td>MatchAsns</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501</td>
    <td>The AS paths based on which routes are evaluated.<br><em>Only AS SEQUENCE is</em> <em>supported. AS SET, AS</em> <em>CONFED SEQUENCE,</em> <em>and AS CONFED SET are</em> <em>not supported. In other</em> <em>words, only the AS</em> <em>number list is</em> <em>supported. Sets and</em> <em>sub-lists are not</em> <em>supported.</em></td>
  </tr>
  <tr>
    <td>MatchComm unitySet</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501:1</td>
    <td>The community set based on which routes are evaluated.<br>Specify the community in the format of n:m. Valid values of n and m: <strong>1</strong> to <strong>65535</strong>. Each community must comply with the RFC 1997 standard. The RFC 8092 standard that defines BGP large communities is not supported.<br>You can enter at most 32 communities.<br><em>If the configurations of</em> <em>the communities are</em> <em>incorrect, routes may</em> <em>fail to be advertised to</em> <em>your data center.</em></td>
  </tr>
</table>

<table>
  <tr>
    <td>OperateCom munitySet</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501:1</td>
    <td>The community set on which actions are performed.<br>Specify the community in the format of n:m. Valid values of n and m: <strong>1</strong> to <strong>65535</strong>. Each community must comply with RFC 1997. The RFC 8092 standard that defines BGP large communities is not supported.<br>You can enter at most 32 communities.<br><em>If the configurations of</em> <em>the communities are</em> <em>incorrect, routes may</em> <em>fail to be advertised to</em> <em>your data center.</em></td>
  </tr>
  <tr>
    <td>PrependAsP ath</td>
    <td>Repea tList</td>
    <td>Query</td>
    <td>No</td>
    <td>65501</td>
    <td>The AS paths that are prepended by using an action statement when regional gateways receive or advertise routes.<br>The AS paths vary based on the direction in which the routing policy is applied:<br>• If AS paths are prepended to a routing policy that is applied in the inbound direction, you must specify source network instance IDs and the source region in the match condition. In addition, the source region must be the same as the region where the routing policy is applied.<br>• If AS paths are prepended to a routing policy that is applied in the outbound direction, you must specify destination network instance IDs in the match condition.<br>This parameter specifies the action to be performed when a route meets the match condition.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RequestId | String | 54B48E3D-DF70-471B-AA93-08E683A1B457 | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyCenRouteMap
&CenId=cen-7qthudw0ll6jmc****
&CenRegionId=cn-qingdao-env17e-d01
&RouteMapId=cenrmap-abcdedfghij****
&MapResult=Permit
&Priority=10
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457\t"
}
```

`XML`  format

```xml
<RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457 </RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_ROUTE_MAP_INVALID_ACTION | InvalidOperation.NoEffictiveAction | No effective action be configured. |
| 400 | INVALID_OPERATION_ROUTEMAP_CONFIG_E XIST | InvalidOperation.CenRouteMapExis t | Operation is invalid because an route map config exist. |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_SRC_REGION_EMP TY | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be null |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_GW_ZONE_EMPTY | Invid.Parameter | When using GatewayRegionId, GatewayZoneId must not be null |
| 400 | PARAMETER_ILLEGAL_RMAP_WITH_GW_REGI ON_SRC_REGION_ILLE GAL | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be the same with tr region id |
| 400 | PARAMETER_ILLEGAL_RMAP_GW_REGION_ID | Invid.Parameter | GatewayRegionId is invalid |

<a id="section-1-15-3"></a>

### 1.15.3. DescribeCenRouteMaps

Queries information about routing policies.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenRouteMaps | The operation that you want to perform. Set the value to <strong>DescribeCenRouteMaps</strong>. |
| PageNumber | Integ er | Query | No | 1 | The page number. Default value: <strong>1</strong>. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: <strong>10</strong>. |
| CenId | String | Query | Yes | cen-wx12mmlt17ld82\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| RouteMapId | String | Query | No | cenrmap-y40mxdvf7joc12\*\*\*\* | The ID of the routing policy. |
| CenRegionId | String | Query | No | cn-qingdao-env66-d01 | The region ID of the routing policy.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |

<table>
  <tr>
    <td>TransmitDire ction</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>RegionOut</td>
    <td>The direction in which the routing policy applies. Valid values:<br>• <strong>RegionIn</strong>: Routes are advertised to the gateways in the regions that are connected by the CEN instance.<br>For example, routes are advertised from network instances deployed in the current region or other regions to the gateway deployed in the current region.<br>• <strong>RegionOut</strong>: Routes are advertised from the gateways in the regions that are connected by the CEN instance.<br>For example, routes are advertised from the gateway deployed in the current region to network instances deployed in the same region, or to gateways deployed in other regions.</td>
  </tr>
  <tr>
    <td>TransitRoute rRouteTableI d</td>
    <td>String</td>
    <td>Query</td>
    <td>No</td>
    <td>vtb-gw8nx3515m1mbd1z1****</td>
    <td>The route table ID of the transit router with which the routing policy is associated.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RouteMaps | Array |  | The information about the routing policy. |
| -SourceRegionIds | Normal | cn-qingdao-env66-d01 | The IDs of the source regions to which the routes belong. |
| -SourceChildInsta nceTypes | Normal | VPC | The types of source network instances to which the routes belong.<br>• VPC<br>• VBR |
| -DestinationRoute TableIds | Normal | vtb-adefrgtr144vf\*\*\*\* | The IDs of the destination route tables to which the routes belong. You can enter at most 32 route table IDs.<br><em>The destination route table IDs are valid</em> <em>only when the routing policy is applied to</em> <em>scenarios where routes are advertised from</em> <em>the gateway in the current region to route</em> <em>tables in the current region.</em> |
| -SourceInstanceId s | Normal | vpc-adeg3544fdf34vf\*\*\*\* | The IDs of the source network instances to which the routes belong. |
| -DestinationCidrB locks | Normal | 10.10.10.0/24 | The prefixes of matching routes. |
| -SourceRouteTabl eIds | Normal | vtb-adfr233vf34rvd4\*\*\*\* | The IDs of the source route tables to which the routes belong. |
| -MatchCommunit ySet | Normal | 65501:1 | The community set based on which the routes are compared. |
| -PrependAsPath | Normal | 65501 | The AS paths that are prepended by using an action statement when regional gateways receive or advertise routes.<br>This parameter specifies the action to be performed when a route meets the match condition. |
| -RouteTypes | Normal | System | The type of route that is compared. Valid values:<br>• <strong>System</strong>: system routes that are automatically generated by the system.<br>• <strong>Custom</strong>: custom routes that are manually added.<br>• <strong>BGP</strong>: routes that are advertised over Border Gateway Protocol (BGP). |
| -DestinationChildI nstanceTypes | Normal | VPC | The types of destination network instances to which the routes belong.<br>• VPC<br>• VBR<br><em>The destination network instance types are</em> <em>valid only if the routing policy is applied to</em> <em>scenarios where routes are advertised from</em> <em>the gateway in the current region to</em> <em>network instances in the current region.</em> |
| -DestinationInsta nceIds | Normal | vpc-afrfs434465fdf\*\*\*\* | The IDs of the destination network instances to which routes are evaluated.<br><em>The destination network instance IDs are</em> <em>valid only if the routing policy is applied to</em> <em>scenarios where routes are advertised from</em> <em>the gateway in the current region to</em> <em>network instances in the current region.</em> |
| -MatchAsns | Normal | 65501 | The AS paths based on which the routes are compared. |
| -OperateCommun itySet | Normal | 65501:1 | The community set on which actions are performed. |
| -RouteMapId | String | cenrmap-y40mxdvf7joc12\*\*\*\* | The ID of the routing policy. |
| -Status | String | Active | The status of the route map. Valid values:<br>• <strong>Creating</strong>: The routing policy is being created.<br>• <strong>Active</strong>: The routing policy is available.<br>• <strong>Deleting</strong>: The routing policy is being deleted. |
| -TransmitDirectio n | String | RegionOut | The direction in which the routing policy applies. |
| -SourceInstanceId sReverseMatch | Boolean | false | Indicates whether the source network instance IDs are excluded.<br>• <strong>false</strong> (default): A route is a match if its source network instance ID is in the list specified by <strong>SourceInstanceIds.N</strong>.<br>• <strong>true</strong>: A route is match if its source network instance ID is not in the list specified by <strong>SourceInstanceIds.N</strong>. |
| -CenRegionId | String | cn-qingdao-env66-d01 | The region ID of the routing policy. |
| -CenId | String | cen-wx12mmlt17ld82\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| -Priority | Integer | 5000 | Enter a priority for the routing policy. A smaller value indicates a higher priority. |
| -TransitRouterRo uteTableId | String | vtb-gw8nx3515m1mbd1z 1\*\*\*\* | The route table ID of the transit router with which the routing policy is associated. |
| -CommunityOper ateMode | String | Additive | The action that is performed on the community of the route.<br>• <strong>Additive</strong>: adds the community to the route.<br>• <strong>Replace</strong>: replaces the original community of the route.<br>The parameter specifies the action to be performed when a route meets the match condition. |
| -MapResult | String | Deny | The action performed on a route that meets the match conditions.<br>• <strong>Permit</strong>: the route is permitted.<br>• <strong>Deny</strong>: the route is denied. |
| -CommunityMatc hMode | String | Include | The match method that is used to match routes against the community.<br>• <strong>Include</strong>: fuzzy match. A route is a match if the community of the route overlaps with the community specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route meets the match condition only if the community of the route is the same as the community specified in the match condition. |
| -Description | String | desctest | The description of the routing policy. |
| -AsPathMatchMod e | String | Include | The match method that is used to match routes based on the AS path.<br>• <strong>Include</strong>: fuzzy match. A route is a match if the AS path of the route overlaps with the AS path specified in the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the AS path of the route is the same as an AS path specified in the match condition. |
| -Preference | Integer | 20 | The new priority of the route.<br>A smaller value indicates a higher priority.<br>This parameter indicates the action to be performed when a route meets the match condition. |
| -DestinationInsta nceIdsReverseM atch | Boolean | false | Indicates whether the destination network instance IDs are excluded.<br>• <strong>false</strong> (default): A route is a match if its destination network instance ID is in the list specified by <strong>DestinationInstanceIds.N</strong>.<br>• <strong>true</strong>: A route is a match if its destination network instance ID is not in the list specified by <strong>DestinationInstanceIds.N</strong>. |
| -CidrMatchMode | String | Include | The match method that is used to match routes based on the prefix. Valid values:<br>• <strong>Include</strong>: fuzzy match. A route is a match if the route prefix is included in the match conditions.<br>For example, if you set the match condition to 10.10.0.0/16 and fuzzy match is applied, the route whose prefix is 10.10.1.0/24 meets the match condition.<br>• <strong>Complete</strong>: exact match. A route is a match only if the route prefix is the same as the prefix specified in the match condition.<br>For example, if you set the match condition to 10.10.0.0/16 and exact match is enabled, a route is a match only if the prefix is 10.10.0.0/16. |
| -NextPriority | Integer | 33 | The priority of the next routing policy that you want to associate with the current routing policy. |
| -MatchAddressTy pe | String | IPv4 | The type of IP address to be matched against the match condition. Valid values:<br>• <strong>IPv4</strong>: IPv4 addresses<br>• <strong>IPv6</strong>: IPv6 addresses<br>• If no value is returned, both IPv4 and IPv6 addresses are matched against the match condition. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 24CE1987-D1D1-5324-9BAD-2750B60E6ABB | The request ID. |
| PageNumber | Integer | 1 | The page number. |
| TotalCount | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenRouteMaps
&CenId=cen-wx12mmlt17ld82****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"24CE1987-D1D1-5324-9BAD-2750B60E6ABB",
 "PageNumber":1,
 "RouteMaps":{
  "MatchAddressType":"IPv4",
  "Description":"desctest",
  "SourceInstanceIdsReverseMatch":false,
  "TransmitDirection":"RegionOut",
  "MatchCommunitySet":"65501:1",
  "CenRegionId":"cn-qingdao-env66-d01",
  "SourceRouteTableIds":"vtb-adfr233vf34rvd4****",
  "DestinationInstanceIds":"vpc-afrfs434465fdf****",
  "SourceInstanceIds":"vpc-adeg3544fdf34vf****",
  "DestinationInstanceIdsReverseMatch":false,
  "DestinationRouteTableIds":"vtb-adefrgtr144vf****",
  "DestinationCidrBlocks":"10.10.10.0/24",
  "RouteMapId":"cenrmap-y40mxdvf7joc12****",
  "OperateCommunitySet":"65501:1",
  "DestinationChildInstanceTypes":"VPC",
  "Status":"Active",
  "Priority":5000,
  "SourceChildInstanceTypes":"VPC",
  "AsPathMatchMode":"Include",
  "MapResult":"Deny",
  "CidrMatchMode":"Include",
  "RouteTypes":"System",
  "TransitRouterRouteTableId":"vtb-gw8nx3515m1mbd1z1****",
  "Preference":20,
  "CommunityOperateMode":"Additive",
  "CenId":"cen-wx12mmlt17ld82****",
  "PrependAsPath":"65501",
  "NextPriority":33,
  "CommunityMatchMode":"Include",
  "MatchAsns":"65501",
  "SourceRegionIds":"cn-qingdao-env66-d01"
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<PageSize>10</PageSize>
<RequestId>24CE1987-D1D1-5324-9BAD-2750B60E6ABB</RequestId>
<PageNumber>1</PageNumber>
<RouteMaps>
 <MatchAddressType>IPv4</MatchAddressType>
 <Description>desctest</Description>
 <SourceInstanceIdsReverseMatch>false</SourceInstanceIdsReverseMatch>
 <TransmitDirection>RegionOut</TransmitDirection>
 <MatchCommunitySet>65501:1</MatchCommunitySet>
 <CenRegionId>cn-qingdao-env66-d01</CenRegionId>
 <SourceRouteTableIds>vtb-adfr233vf34rvd4****</SourceRouteTableIds>
 <DestinationInstanceIds>vpc-afrfs434465fdf****</DestinationInstanceIds>
 <SourceInstanceIds>vpc-adeg3544fdf34vf****</SourceInstanceIds>
 <DestinationInstanceIdsReverseMatch>false</DestinationInstanceIdsReverseMatch>
 <DestinationRouteTableIds>vtb-adefrgtr144vf****</DestinationRouteTableIds>
 <DestinationCidrBlocks>10.10.10.0/24</DestinationCidrBlocks>
 <RouteMapId>cenrmap-y40mxdvf7joc12****</RouteMapId>
 <OperateCommunitySet>65501:1</OperateCommunitySet>
 <DestinationChildInstanceTypes>VPC</DestinationChildInstanceTypes>
 <Status>Active</Status>
 <Priority>5000</Priority>
 <SourceChildInstanceTypes>VPC</SourceChildInstanceTypes>
 <AsPathMatchMode>Include</AsPathMatchMode>
 <MapResult>Deny</MapResult>
 <CidrMatchMode>Include</CidrMatchMode>
 <RouteTypes>System</RouteTypes>
 <TransitRouterRouteTableId>vtb-gw8nx3515m1mbd1z1****</TransitRouterRouteTableId>
 <Preference>20</Preference>
 <CommunityOperateMode>Additive</CommunityOperateMode>
 <CenId>cen-wx12mmlt17ld82****</CenId>
 <PrependAsPath>65501</PrependAsPath>
 <NextPriority>33</NextPriority>
 <CommunityMatchMode>Include</CommunityMatchMode>
 <MatchAsns>65501</MatchAsns>
 <SourceRegionIds>cn-qingdao-env66-d01</SourceRegionIds>
</RouteMaps>
```

<a id="section-1-15-4"></a>

### 1.15.4. DeleteCenRouteMap

Deletes a routing policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Type | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DeleteCenRouteMap | The operation that you want to perform. Set the value to <strong>DeleteCenRouteMap</strong>. |
| CenId | String | Query | Yes | cen-7qthudw0ll6jm\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| CenRegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The region ID of the routing policy.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| RouteMapId | String | Query | Yes | cenrmap-abcdedfghij\*\*\*\* | The routing policy ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 5903EE99-D542-4E14-BC65-AAC1CB2D3D03 | The request ID. |

**Example**

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteCenRouteMap
&CenId=cen-7qthudw0ll6jm****
&CenRegionId=cn-qingdao-env17e-d01
&RouteMapId=cenrmap-abcdedfghij****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"5903EE99-D542-4E14-BC65-AAC1CB2D3D03"
}
```

`XML`  format

```xml
<RequestId>5903EE99-D542-4E14-BC65-AAC1CB2D3D03</RequestId>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | INVALID_OPERATION_ROUTE_MAP_STATUS | IncorrectStatus.RouteMap | Operation Failed. The specified route map is configuring, please try again later. |
| 400 | INVALID_OPERATION_TRANSITROUTER_NOT _EXIST | InvalidOperation.TransitRouterNotE xist | Operation is invalid because the transit router not exist. |

<a id="section-1-16"></a>

## 1.16. Health checks

<a id="section-1-16-1"></a>

### 1.16.1. EnableCenVbrHealthCheck

Enables the health check feature for a virtual border router (VBR) to detect anomalies on Express Connect circuits. You can modify the health check configuration of a VBR based on business requirements.

**Usage notes**

You can configure the health check feature for a VBR to monitor the Express Connect circuit between your data center and Alibaba Cloud. This helps you detect connection issues in a timely manner.

Before you use the health check feature, take note of the following information:

- If your VBR uses static routing, you must add a static route for the data center that is connected to the VBR after you configure the health check feature. Set the destination CIDR block to the source IP address of health checks, set the mask length to 32, and set the next hop to the IP address of the VBR on the Alibaba Cloud side.

- If your VBR uses dynamic Border Gateway Protocol (BGP) routing, you do not need to add routes for the data center.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | EnableCenVbrHealthCheck | The operation that you want to perform. Set the value to EnableCenVbrHealthChe ck. |
| CenId | String | Query | Yes | cen-hahhfskfkseig\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| VbrInstance RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The ID of the region where the VBR is deployed.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| VbrInstance Id | String | Query | Yes | vbr-wz95o9aylj181n5mzk\*\*\*\* | The VBR ID. |
| HealthChec kSourceIp | String | Query | No | 192.XX.XX.1 | The source IP address of the health check. You can set the source IP address in the following ways:<br>• Automatic IP Address (recommended): The system automatically assigns an IP address from the 100.96.0.0/16 CIDR block.<br>• Custom IP Address: You must specify an idle IP address from the 10.0.0.0/8, 192.168.0.0/16, or 172.16.0.0/12 CIDR block. The specified IP address must not conflict with the IP address of the VBR on the Alibaba Cloud side, the IP address of the VBR on the customer side, or other IP addresses with which the VBR communicates through the CEN instance. |
| HealthChec kTargetIp | String | Query | Yes | 10.XX.XX.1 | The destination IP address of health check.<br>Set the destination IP address to the IP address of the VBR on the customer side. |
| VbrInstance OwnerId | Long | Query | No | 1250123456123456 | The UID of the level-1 organization to which the VBR belongs.<br><em>This parameter is</em> <em>required if the VBR and</em> <em>CEN instance belong to</em> <em>different organizations.</em> |
| HealthChec kInterval | Integer | Query | No | 2 | The time interval at which probe packets are sent during health check. Unit: seconds. Default value: <strong>2</strong>.Valid values: <strong>2 to 3</strong>. |
| HealthyThre shold | Integer | Query | No | 8 | The number of probe packets that are sent during health check. Unit: packet. Valid values: <strong>3 to</strong> 8. Default value: <strong>8</strong>. |
| HealthChec kOnly | Boolea n | Query | No | false | Specifies whether to enable probing during the health check. Valid values:<br>• true: enables probing.<br>If probing is enabled, the system does not switch to another route when the detected route is not reachable.<br><em>Make sure that a</em> <em>redundant route is</em> <em>available. Otherwise,</em> <em>network</em> <em>disconnections may</em> <em>occur.</em><br>• false: disables probing.<br>Probing is disabled by default. If a redundant route is specified, the system switches to the redundant route when the detected route is not reachable. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| RequestId | String | 1F59F19C-EFD2-40B1-94D5-65B40CA8E34A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=EnableCenVbrHealthCheck
&CenId=cen-hahhfskfkseig****
&VbrInstanceRegionId=cn-qingdao-env17e-d01
&VbrInstanceId=vbr-wz95o9aylj181n5mzk****
&HealthCheckTargetIp=10.XX.XX.1
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"1F59F19C-EFD2-40B1-94D5-65B40CA8E34A"
}
```

`XML`  format

```xml
<RequestId>1F59F19C-EFD2-40B1-94D5-65B40CA8E34A</RequestId>
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | VBR_CAN_NOT_MODIF Y_HC_CHECK | InvalidStatus.HealthCheck | Can't modify, please delete health check config first. |
| 400 | ROUTE_CONFLICT | RouteConflict | The specified route already exists. |
| 400 | PARAMETER_ILLEGAL_SOURCEIP_OR_TARGE TIP | Illegal.SourceIpOrTargetIp | The specified source IP address or destination IP address is invalid. |
| 400 | INVALID_OPERATION_VBR_OR_VPC_CBN_AT TACHMENT_STATUS | OperationFailed.StatusNotSupport | The VBR or VPC instance to CBN attachment is not in a valid state for the operation. |

<a id="section-1-16-2"></a>

### 1.16.2. DisableCenVbrHealthCheck

Disables the health check feature for a virtual border router (VBR).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DisableCenVbrHealthCheck | The operation that you want to perform. Set the value to DisableCenVbrHealthChec <strong>k</strong>. |
| CenId | String | Query | Yes | cen-sjfoejfghhjgghjghkg\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| VbrInstance RegionId | String | Query | Yes | cn-qingdao-env17e-d01 | The ID of the region where the VBR is deployed.<br>You can call the DescribeChildInstanceRegion s operation to query the most recent region list. |
| VbrInstanceI d | String | Query | Yes | vbr-wz95o9aylj181n5\*\*\*\* | The VBR ID. |
| VbrInstance OwnerId | Long | Query | No | 1250123456123456 | The UID of the level-1 organization to which the VBR belongs.<br><em>The parameter is</em> <em>required if the VBR and</em> <em>the CEN instance belong</em> <em>to different</em> <em>organizations.</em> |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | A278B8A6-A5B8-4FDE-9F70-95F0F6A1D68A | The request ID. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DisableCenVbrHealthCheck
&CenId=cen-sjfoejfghhjgghjghkg****
&VbrInstanceRegionId=cn-qingdao-env17e-d01
&VbrInstanceId=vbr-wz95o9aylj181n5****
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "RequestId":"A278B8A6-A5B8-4FDE-9F70-95F0F6A1D68A"
}
```

`XML`  format

```xml
<RequestId>A278B8A6-A5B8-4FDE-9F70-95F0F6A1D68A</RequestId>
```

<a id="section-1-16-3"></a>

### 1.16.3. DescribeCenVbrHealthCheck

Queries the health check configuration of a virtual border router (VBR) in a region.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Paramete r | Type | Positio n | Required | Examples | Description |
| --- | --- | --- | --- | --- | --- |
| Action | String | Query | No | DescribeCenVbrHealthChec k | The operation that you want to perform. Set the value to DescribeCenVbrHealthCh eck. |
| CenId | String | Query | No | cen-6hpdgj7ni6pz1k\*\*\*\* | The ID of the Cloud Enterprise Network (CEN) instance. |
| VbrInstance RegionId | String | Query | Yes | cn-qingdao-env66-d01 | The ID of the region where the VBR is deployed.<br>You can call the DescribeChildInstanceRegio ns operation to query the most recent region list. |
| VbrInstance Id | String | Query | No | vbr-bp1kznorjeembsuhl\*\*\*\* | The VBR ID. |
| VbrInstance OwnerId | Long | Query | No | 253460731706911258 | The UID of the level-1 organization to which the VBR belongs.<br><em>This parameter is</em> <em>required if the VBR and</em> <em>CEN instance belong to</em> <em>different organizations.</em> |
| PageNumbe r | Integer | Query | No | 1 | The number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integer | Query | No | 10 | The number of entries per page. Valid values: <strong>1</strong> to 50. Default value: <strong>10</strong>. |

**Response parameters**

| Parameter | Type | Examples | Description |
| --- | --- | --- | --- |
| VbrHealthChecks | Array |  | The health check configuration of the VBR. |
| -HealthCheckTarg etIp | String | 192.XX.XX.1 | The destination IP address for health checks. |
| -VbrInstanceId | String | vbr-bp1kznorjeembsuhl\*\* \*\* | The VBR ID. |
| -VbrInstanceRegi onId | String | cn-qingdao-env66-d01 | The ID of the region where the VBR is deployed. |
| -CenId | String | cen-6hpdgj7ni6pz1k\*\*\*\* | The ID of the CEN instance. |
| -HealthyThreshol d | Integer | 8 | The number of probe packets that are sent during the health check. |
| -HealthCheckInte rval | Integer | 2 | The time interval at which probe packets are sent during the health check. Unit: seconds. |
| -HealthCheckSour ceIp | String | 172.XX.XX.1 | The source IP address for health checks. |
| -HealthCheckOnly | Boolean | false | Indicates whether probing is enabled. Valid values:<br>• true: Probing is enabled.<br>If probing is enabled, the system does not switch to another route when the detected route is not reachable.<br>• false: Probing is disabled.<br>If probing is disabled and a redundant route is specified, the system switches to the redundant route when the detected route is not reachable. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | B8C9702E-304A-4E18-AC89-BE2D91C2C176 | The request ID. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCenVbrHealthCheck
&VbrInstanceRegionId=cn-qingdao-env66-d01
&Common request parameters
```

Sample success responses

`JSON`  format

```text
HTTP/1.1 200 OK
Content-Type:application/json
{
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"B8C9702E-304A-4E18-AC89-BE2D91C2C176",
 "PageNumber":1,
 "VbrHealthChecks":{
  "VbrInstanceRegionId":"cn-qingdao-env66-d01",
  "HealthCheckInterval":2,
  "VbrInstanceId":"vbr-bp1kznorjeembsuhl****",
  "HealthyThreshold":8,
  "HealthCheckSourceIp":"172.XX.XX.1",
  "CenId":"cen-6hpdgj7ni6pz1k****",
  "HealthCheckTargetIp":"192.XX.XX.1",
  "HealthCheckOnly":false
 }
}
```

`XML`  format

```xml
<TotalCount>1</TotalCount>
<PageSize>10</PageSize>
<RequestId>B8C9702E-304A-4E18-AC89-BE2D91C2C176</RequestId>
<PageNumber>1</PageNumber>
<VbrHealthChecks>
 <VbrInstanceRegionId>cn-qingdao-env66-d01</VbrInstanceRegionId>
 <HealthCheckInterval>2</HealthCheckInterval>
 <VbrInstanceId>vbr-bp1kznorjeembsuhl****</VbrInstanceId>
 <HealthyThreshold>8</HealthyThreshold>
 <HealthCheckSourceIp>172.XX.XX.1</HealthCheckSourceIp>
 <CenId>cen-6hpdgj7ni6pz1k****</CenId>
 <PacketLoss  />
 <HealthCheckTargetIp>192.XX.XX.1</HealthCheckTargetIp>
 <HealthCheckOnly>false</HealthCheckOnly>
</VbrHealthChecks>
```
