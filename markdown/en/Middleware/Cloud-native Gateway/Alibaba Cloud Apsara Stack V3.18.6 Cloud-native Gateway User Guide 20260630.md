Alibaba Cloud  
Apsara Stack  
Cloud-native Gateway User  
Guide  
Product Version: V3.18.6  
Document Version: 20260630

**Table of Contents**

- [1.Product Overview](#section-1)
    - [1.1. What is Cloud-native Gateway?](#section-1-1)
- [2.Getting started](#section-2)
    - [2.1. Log in to the Cloud-native Gateway console](#section-2-1)
    - [2.2. Route management](#section-2-2)
- [3.User Guide](#section-3)
    - [3.1. Gateway management](#section-3-1)
        - [3.1.1. Create a Cloud-native Gateway instance](#section-3-1-1)
        - [3.1.2. View the details of a Cloud-native Gateway instance](#section-3-1-2)
        - [3.1.3. Modify a gateway instance](#section-3-1-3)
        - [3.1.4. Release a Cloud-native Gateway instance](#section-3-1-4)
        - [3.1.5. Stop a Cloud-native Gateway instance](#section-3-1-5)
        - [3.1.6. Restart a gateway instance](#section-3-1-6)
        - [3.1.7. Configure security group rules](#section-3-1-7)
    - [3.2. Route management](#section-3-2)
    - [3.3. Policy configurations](#section-3-3)
        - [3.3.1. Configure a rewrite policy](#section-3-3-1)
        - [3.3.2. Configure a header modification policy](#section-3-3-2)
        - [3.3.3. Configure a timeout policy](#section-3-3-3)
        - [3.3.4. Configure a degradation policy](#section-3-3-4)
    - [3.4. Service management](#section-3-4)
        - [3.4.1. Create a service](#section-3-4-1)
        - [3.4.2. Manage services](#section-3-4-2)
    - [3.5. Consumer management](#section-3-5)
        - [3.5.1. Create a consumer](#section-3-5-1)
        - [3.5.2. View the details of a consumer](#section-3-5-2)
        - [3.5.3. Authorization management](#section-3-5-3)
        - [3.5.4. Modify the configuration of a consumer](#section-3-5-4)
        - [3.5.5. Delete a consumer](#section-3-5-5)
    - [3.6. Plug-in management](#section-3-6)
        - [3.6.1. Create a plug-in](#section-3-6-1)
        - [3.6.2. Manage plug-ins](#section-3-6-2)
        - [3.6.3. Authentication](#section-3-6-3)
            - [3.6.3.1. key-auth](#section-3-6-3-1)
            - [3.6.3.2. jwt-auth](#section-3-6-3-2)
            - [3.6.3.3. basic-auth](#section-3-6-3-3)
            - [3.6.3.4. oidc](#section-3-6-3-4)
            - [3.6.3.5. hmac-auth](#section-3-6-3-5)
            - [3.6.3.6. ext-auth](#section-3-6-3-6)
            - [3.6.3.7. oauth](#section-3-6-3-7)
            - [3.6.3.8. opa](#section-3-6-3-8)
        - [3.6.4. Security](#section-3-6-4)
            - [3.6.4.1. cors](#section-3-6-4-1)
            - [3.6.4.2. ip-restriction](#section-3-6-4-2)
            - [3.6.4.3. waf](#section-3-6-4-3)
            - [3.6.4.4. request-block](#section-3-6-4-4)
            - [3.6.4.5. bot-detect](#section-3-6-4-5)
        - [3.6.5. Traffic management](#section-3-6-5)
            - [3.6.5.1. cluster-key-rate-limit](#section-3-6-5-1)
            - [3.6.5.2. key-rate-limit](#section-3-6-5-2)
            - [3.6.5.3. traffic-tag](#section-3-6-5-3)
            - [3.6.5.4. request-validation](#section-3-6-5-4)
        - [3.6.6. Transmission](#section-3-6-6)
            - [3.6.6.1. transformer](#section-3-6-6-1)
            - [3.6.6.2. frontend-gray](#section-3-6-6-2)
            - [3.6.6.3. custom-response](#section-3-6-6-3)
            - [3.6.6.4. de-graphql](#section-3-6-6-4)
            - [3.6.6.5. cache-control](#section-3-6-6-5)
        - [3.6.7. Observability](#section-3-6-7)
            - [3.6.7.1. geo-ip](#section-3-6-7-1)
            - [3.6.7.2. log-request-response](#section-3-6-7-2)
    - [3.7. Certificate management](#section-3-7)
        - [3.7.1. Create a certificate](#section-3-7-1)
        - [3.7.2. Manage certificates](#section-3-7-2)
    - [3.8. Domain name management](#section-3-8)
        - [3.8.1. Create a domain name](#section-3-8-1)
        - [3.8.2. Manage domain names](#section-3-8-2)
    - [3.9. Observation and analysis](#section-3-9)
        - [3.9.1. View gateway metrics](#section-3-9-1)
    - [3.10. Nginx Ingress migration](#section-3-10)

<a id="section-1"></a>

# 1.Product Overview

<a id="section-1-1"></a>

## 1.1. What is Cloud-native Gateway?

Cloud-native Gateway is a unified gateway service that integrates traffic gateways, microservices gateways, and security gateways. It is built based on open source Istio and Envoy to provide a unified, high-performance, and easy-to-maintain ingress gateway solution for Kubernetes environments.

Cloud-native Gateway provides the following core features:

- Three-in-one architecture: Cloud-native Gateway integrates traffic gateways, microservices gateways, and security gateways in a unified architecture to simplify the product architecture and reduce link latency and O&M complexity.

- Deep ecosystem integration: Cloud-native Gateway supports mainstream microservices components such as Dubbo, Nacos, and Sentinel, which makes it suitable for complex cloud-native application architectures.

- Dynamic configuration and observability: Cloud-native Gateway uses Kubernetes CustomResourceDefinitions (CRDs) to implement declarative configurations, support rolling updates, real-time monitoring, and log tracing, and meet production-grade stability requirements.

- High performance and scalability: Built on Envoy as the data plane, Cloud-native Gateway delivers high-concurrency, low-latency processing capabilities and supports flexible feature extension by using plug-ins.

<a id="section-2"></a>

# 2.Getting started

<a id="section-2-1"></a>

## 2.1. Log in to the Cloud-native Gateway console

This topic describes how to log in to the Cloud-native Gateway console.

**Prerequisites**

- The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer.

- A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/687f6d006b35a4552292b1f7b3755914.jpeg)

   > **Note**
   >
   > - You can click the current language in the upper-right corner to switch to another language.
   >
   > - The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button.
   >
   > - If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.

2. Enter your username and password.

   > **Note**
   >
   > - Obtain the username and password from an operations administrator.
   >
   > - The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Log On**.

4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations in the following scenarios:

   - **This is your first time logging in to the Apsara Uni-manager Management Console after MFA is enabled by the administrator:**

     <ol type="a">

     <li>

     On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device.

     </li>

     <li>

     Enter the username and password again as in Step 2 and click **Log On**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Enter the 6-digit MFA verification code and click **Authenticate**.

     </li>

     </ol>

   - **You have enabled MFA and bound an MFA device:**

     Enter the 6-digit MFA verification code and click **Authenticate**.

     > **Note**
     >
     > For more information about how to enable MFA and bind an MFA device, see the **Manage MFA** topic in Apsara Uni-manager Management Console User Guide.

5. In the top navigation bar, choose **Products > Middleware > Application Integration > API Gateway** to go to the **API Gateway 2.0** console.

   > **Note**
   >
   > Cloud-native Gateway shares the same console entry with API Gateway.

<a id="section-2-2"></a>

## 2.2. Route management

Routes are the primary mechanism by which a gateway exposes its access capabilities. This topic describes how to manage routes.

**Create a route**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**. On the page that appears, click **Create Route**.

5. In the **Create Route** panel, follow the on-screen instructions to configure the parameters and click **Determine**.

   | Parameter | Description |
   | --- | --- |
   | Route Name | The name of the route.<br>Important<br>The route name must be globally unique. |
   | Routing path | The request path and method for matching the route. You can set the matching method to <strong>Prefix Match</strong>, <strong>Exact Match</strong>, or <strong>Regex Match</strong>. |
   | Request Method | The request method for matching the route. If no request method is specified, the route matches requests of any method. |
   | Request Header | The header for matching the route. If multiple headers are added, the AND logic operator is applied to these headers. |
   | Request Query | The request query for matching the route. If multiple queries are added, the AND logic operator is applied to these queries. |
   | Backend Services | The backend services that are associated with the route. You can configure weights for the backend services. |
   | Domain Name | The domain name used to access the route. You can select multiple domain names.<br>Note<br>The combination of the domain name and base path (BasePath) must be globally unique. |

**View route details**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. Optional. On the **Routing Management** page, you can filter routes by **Route Name** or **Service Name**.

6. In the route list, find the route that you want to manage and click its name. On the **Routing details** page, you can view the information on the **Routing Details**, **Plugin configuration**, and **Policy Configuration** tabs.

   - On the **Routing Details** tab, you can view the details of the route in the **Basic information**, **Associated Services**, and **Associated Domain Name** sections.

   - On the **Plugin configuration** tab, you can manage the plug-ins that are bound to the current route. Click **AddPlugin** to bind a plug-in to the route. For more information, see Create a plug-in.

     > **Note**
     >
     > On the route list page, you can click **Policy Configuration** in the **Operation** column to go to the **Policy Configuration** tab.

   - On the **Policy Configuration** tab, you can configure policy rewrite, header modification, timeout, and degradation. For more information, see Policy configuration.

**Modify a route**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. In the route list, find the route that you want to manage and click **Edit** in the **Operation** column.

6. In the **Edit route** panel, modify the route information based on your business requirements and click **Determine**.

**Delete routes**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. Delete routes.

   - Delete a route: In the route list, find the route that you want to manage and click **Delete** in the **Operation** column.

   - Delete multiple routes at a time: In the route list, select the routes that you want to delete and click **Batch Delete**.

6. In the **Alert** message, click **Determine**.

<a id="section-3"></a>

# 3.User Guide

<a id="section-3-1"></a>

## 3.1. Gateway management

<a id="section-3-1-1"></a>

### 3.1.1. Create a Cloud-native Gateway instance

This topic describes how to create a Cloud-native Gateway instance.

**Prerequisites**

A Kubernetes cluster is created. For more information, see **Container Service for Kubernetes User Guide > Create an ACK cluster**.

**Procedure**

1. Log in to the Container Service for Kubernetes (ACK) console.

2. In the left-side navigation pane, click **Clusters**.

3. On the **Clusters** page, find the desired cluster and click the name of the cluster in the Cluster Name/ID column or click **Details** in the **Actions** column.

4. In the left-side navigation pane of the cluster details page, choose **Operations > Add-ons**.

5. On the **Add-ons** page, find the API Gateway Ingress Controller component, and click **Install**.

6. In the dialog box that appears, you can choose whether to check the **Create public network service** option and click **OK**.

   - **Create public network service**: Create an Internet service.

   > **Note**
   >
   > If **Installed** is displayed in the card, the component is successfully installed.

<a id="section-3-1-2"></a>

### 3.1.2. View the details of a Cloud-native Gateway instance

This topic describes how to view the details of a Cloud-native Gateway instance in the Cloud-native Gateway console.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. Optional. On the **Gateway instance** page, you can filter instances by **Instance name** or **Instance ID**.

4. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

5. In the left-side navigation pane, click **Overview** to view the **Basic information**, **Access Point**, and **Observable** information about the instance.

   - **Basic information** tab:

     - **Gateway Overview**: displays the following information about the Cloud-native Gateway instance: **Total routes**, **Number of consumers**, **Total number of services**, and **Total plugins**.

     - **Basic Information**: displays the following information about the Cloud-native Gateway instance: **Instance ID**, **Instance name**, **Status**, **Deployment Architecture**, **Cluster**, **Namespace**, **Creation Time**, **Modified**, and **Engine Type**.

     - **Observable**: You can enable or disable **Log Service** and **Monitoring Plugin** for the Cloud-native Gateway instance.

       - **Log Service**: After you turn on this switch, Simple Log Service (SLS) automatically collects instance logs.

       - **Monitoring Plugin**: After you turn on this switch, instance metrics are collected by Managed Service for Prometheus.

   - **Access Point** tab: displays the access point information about the instance, including **Type**, **Network Type**, **ServiceName**, **External IPs**, **Ports**, and **ClusterIP**.

<a id="section-3-1-3"></a>

### 3.1.3. Modify a gateway instance

This topic describes how to modify the name of a Cloud-native Gateway instance.

**Procedure**

> **Note**
>
> Only the name of a Cloud-native Gateway instance can be modified.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, find the instance that you want to manage, click the <img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1e1baa5cb4a113020a8a73d856acf475.png" width="20" alt="">

   icon in the **Operation** column, and then click **Edit**.

4. On the **Edit Instance** page, modify the **Instance name** and click **Submission**.

<a id="section-3-1-4"></a>

### 3.1.4. Release a Cloud-native Gateway instance

If you no longer require Cloud-native Gateway, you can release your Cloud-native Gateway instances to deactivate the service.

**Usage notes**

After an instance is released, the instance and its data are deleted. Proceed with caution.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, find the instance that you want to manage, click the <img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1e1baa5cb4a113020a8a73d856acf475.png" width="20" alt="">

   icon in the **Operation** column, and then click **Write-off** or **Force Logoff**.

4. In the **Alert** message, click **OK**.

<a id="section-3-1-5"></a>

### 3.1.5. Stop a Cloud-native Gateway instance

This topic describes how to stop a Cloud-native Gateway instance.

**Procedure**

If you no longer need to run a Cloud-native Gateway instance, you can stop the instance.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, find the instance that you want to manage, click the <img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1e1baa5cb4a113020a8a73d856acf475.png" width="20" alt="">

   icon in the **Operation** column, and then click **Shutdown**.

4. In the **Alert** message, click **OK**. In the instance list, the **instance status** changes to **Shutdown**.

<a id="section-3-1-6"></a>

### 3.1.6. Restart a gateway instance

This topic describes how to restart a Cloud-native Gateway instance.

**Procedure**

If you need to continue using a gateway instance, you can restart the gateway instance.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, find the instance that you want to manage, click the <img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1e1baa5cb4a113020a8a73d856acf475.png" width="20" alt="">

   icon in the **Operation** column, and then click **Restart**.

4. In the **Alert** message, click **OK**. In the instance list, the **instance status** changes to **In operation**.

<a id="section-3-1-7"></a>

### 3.1.7. Configure security group rules

If your Cloud-native Gateway instance and the node on which your backend service is deployed belong to different security groups, you can configure a security group rule to authorize your Cloud-native Gateway instance to access the backend service.

**Background information**

A security group functions as a virtual firewall to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances and elastic network interfaces (ENIs). Security groups help improve the security of ECS instances. Security groups provide stateful packet inspection (SPI) and packet filtering capabilities. You can use security groups and security group rules to define security domains in the cloud. For more information, see **Elastic Compute Service User Guide > Security groups** > Overview.

The Cloud-native Gateway instance and the node on which your backend service is deployed belong to different security groups. Therefore, you must authorize the Cloud-native Gateway instance to access the backend service over a range of ports.

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/f4e0d9967338e5afea348013d9df2444.jpeg)

The preceding figure illustrates how you can use a Cloud-native Gateway instance to implement access control and traffic distribution for various types of services. Specifically:

- You can use a client (such as a computer) to access the internal network of a Cloud-native Gateway instance.

- The Cloud-native Gateway instance distributes your request to service-sg1 and service-sg2 based on configurations.

- The pod in service-sg1 processes requests from port 8080/8080.

- The ECS instance in service-sg2 processes requests from port 80/9000.

**Step 1: Obtain the CIDR block of the node where the Cloud-native Gateway instance resides**

1. Log in to the Container Service for Kubernetes (ACK) console. In the left-side navigation pane, click **Clusters**.

2. On the **Clusters** page, find the cluster that you want to manage and click its name. In the left-side pane, choose **Node > Node Pools**.

3. On the **Node Pools** page, find the node pool that you want to manage and click its name. On the page that appears, obtain the ID of **Node vSwitch** in the **Node Configurations** section.

4. Log in to the VPC console. In the left-side navigation pane, click **vSwitch**.

5. On the **vSwitches** page, click the vSwitch ID that you obtained in Step 3.

6. On the **Basic Information** tab of the **vSwitch Details** page, obtain the IPv4 CIDR block, which is the CIDR block of the vSwitch.

**Step 2: Obtain the security group of the node on which your backend service is deployed**

Upstream services that are associated with a Cloud-native Gateway instance are deployed in an ACK cluster or on an Elastic Compute Service (ECS) instance. You can use either of the following methods to obtain the security group ID.

**The backend service is deployed in an ACK cluster**

1. Log in to the Container Service for Kubernetes (ACK) console. In the left-side navigation pane, click **Clusters**.

2. On the **Clusters** page, find the cluster that you want to manage and click its name. In the left-side pane, choose **Node > Node Pools**.

3. On the **Node Pools** page, obtain the ID of the security group in the **Node Pool Information** section.

**The backend service is deployed on an ECS instance**

1. Log in to the ECS console.

2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.

3. On the **ECS Instances** page, click the name of the ECS instance on which your backend service is deployed. On the **Security Groups** tab, obtain the ID of the security group.

**Step 3: Add a security group rule**

1. Log in to the ECS console.

2. In the left-side navigation pane, choose **Network & Security > Security Groups**. On the Security Groups page, click the ID of the security group that you obtained in Step 2.

3. On the **Rules** tab, click the **Inbound** tab. Then, click **Create Rule**. In the dialog box that appears, configure the following parameters and click **OK**.

   | Parameter | Description | Example value |
   | --- | --- | --- |
   | Port Range | The port range of the security group rule. | 1/65535 |
   | Priority | The priority of the security group rule. | 1 |
   | Allowed IP range | Select <strong>IPv4 CIDR Block</strong>. | IPv4 CIDR Block |
   | Authorization Object | Enter the CIDR block of the node where the Cloud-native Gateway instance resides. The CIDR block is obtained in Step 1. | 172.16.0.2/24 |

**Delete a security group rule**

1. Log in to the ECS console.

2. In the left-side navigation pane, choose **Network & Security > Security Groups**. On the Security Groups page, click the ID of the security group that you obtained in Step 2.

3. On the **Rules** tab, use either of the following methods to delete a security group rule.

   - Method 1: Find the security group rule that you want to delete and click **Delete** in the **Actions** column.

   - Method 2: Find the security group rule that you want to delete and click **Modify Properties** in the **Actions** column. In the **Modify Properties** dialog box, delete the IP address range authorized by the corresponding security group.

**FAQ**

**Why cannot I access a service from a Cloud-native Gateway instance after I configure a security group rule?**

Perform the following steps:

1. Check whether the node for which you configure the security group rule is the node on which the service is deployed.

   For example, the service is deployed on Node A, but you configure the security group rule for Node B.

2. Check whether multiple security groups are configured for your service node.

   If multiple security groups are configured for your service node, we recommend that you configure a security group rule for each security group.

**I configured a security group rule for a Cloud-native Gateway instance to access a service and the access was successful. However, the access fails now. Why?**

Perform the following steps:

1. Check whether your service is normal.

   You can run the  `curl`  command on other nodes in the same security group to check the connectivity of the service.

2. Check whether the exposed port of the service is changed.

   For example, the exposed port is changed from 8080 to 8081 but only port 8080 is authorized. In this case, you need to change the port number in the security group rule. To prevent this issue, we recommend that you set Port Range to 1/65535 when you create the security group rule.

<a id="section-3-2"></a>

## 3.2. Route management

Routes are the primary mechanism by which a gateway exposes its access capabilities. This topic describes how to manage routes.

**Create a route**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**. On the page that appears, click **Create Route**.

5. In the **Create Route** panel, follow the on-screen instructions to configure the parameters and click **Determine**.

   | Parameter | Description |
   | --- | --- |
   | Route Name | The name of the route.<br>Important<br>The route name must be globally unique. |
   | Routing path | The request path and method for matching the route. You can set the matching method to <strong>Prefix Match</strong>, <strong>Exact Match</strong>, or <strong>Regex Match</strong>. |
   | Request Method | The request method for matching the route. If no request method is specified, the route matches requests of any method. |
   | Request Header | The header for matching the route. If multiple headers are added, the AND logic operator is applied to these headers. |
   | Request Query | The request query for matching the route. If multiple queries are added, the AND logic operator is applied to these queries. |
   | Backend Services | The backend services that are associated with the route. You can configure weights for the backend services. |
   | Domain Name | The domain name used to access the route. You can select multiple domain names.<br>Note<br>The combination of the domain name and base path (BasePath) must be globally unique. |

**View route details**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. Optional. On the **Routing Management** page, you can filter routes by **Route Name** or **Service Name**.

6. In the route list, find the route that you want to manage and click its name. On the **Routing details** page, you can view the information on the **Routing Details**, **Plugin configuration**, and **Policy Configuration** tabs.

   - On the **Routing Details** tab, you can view the details of the route in the **Basic information**, **Associated Services**, and **Associated Domain Name** sections.

   - On the **Plugin configuration** tab, you can manage the plug-ins that are bound to the current route. Click **AddPlugin** to bind a plug-in to the route. For more information, see Create a plug-in.

     > **Note**
     >
     > On the route list page, you can click **Policy Configuration** in the **Operation** column to go to the **Policy Configuration** tab.

   - On the **Policy Configuration** tab, you can configure policy rewrite, header modification, timeout, and degradation. For more information, see Policy configuration.

**Modify a route**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. In the route list, find the route that you want to manage and click **Edit** in the **Operation** column.

6. In the **Edit route** panel, modify the route information based on your business requirements and click **Determine**.

**Delete routes**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, click **Cloud-native gateway**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. Delete routes.

   - Delete a route: In the route list, find the route that you want to manage and click **Delete** in the **Operation** column.

   - Delete multiple routes at a time: In the route list, select the routes that you want to delete and click **Batch Delete**.

6. In the **Alert** message, click **Determine**.

<a id="section-3-3"></a>

## 3.3. Policy configurations

<a id="section-3-3-1"></a>

### 3.3.1. Configure a rewrite policy

You can configure a rewrite policy to change the paths and hostnames of requests before the requests are forwarded to their destination backend services. This meets the requirements for specific business environments and architectures. The rewrite policy provides precise control over the paths and hostnames of requests and ensures that the requests are correctly routed to the appropriate services or endpoints.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. On the Routing Management page, find the route that you want to manage and click its name to go to the **Routing details** page.

6. On the **Routing details** page, click the **Policy Configuration** tab.

7. On the **Policy Configuration** tab, click **Rewrite**, turn on the **Open** switch, configure **Path Override** and **Host Rewrite**, and then click **Save**.

   > **Note**
   >
   > For more information about how to configure **Path Override** and **Host Rewrite**, see Rewrite policies.

**Rewrite policy**

A rewrite policy allows you to change the paths and hostnames in requests.

**Path rewrite**

For path rewrites, Cloud-native Gateway supports two rewrite modes: exact rewrite and prefix rewrite.

**Exact rewrite**

An exact rewrite can completely change the path in a request.

**Example**

If the path in a request is  `/app/test`  and you want the path to be rewritten as  `/foo/bar` , we recommend that you configure the following rewrite policy:

- Route matching condition: Set the matching method to Exact Match, and set the path to  `/app/test` .

- Rewrite policy: Set the rewrite method to Exact Rewrite, and set the path to  `/foo/bar` .

> **Important**
>
> If you want the rewrite method to be Exact Rewrite, the matching method must be Exact Match or Regex Match. The matching method cannot be Prefix Match.

**Prefix rewrite**

A prefix rewrite changes the path prefix in a request.

**Example 1**

If the path in a request is  `/app/test`  and you want the path to be rewritten as  `/test` , we recommend that you configure the following rewrite policy:

- Route matching condition: Set the matching method to Prefix Match, and set the path to  `/app` .

- Rewrite policy: Set the rewrite method to Prefix Rewrite, and set the path to  `/` .

**Example 2** If the path in a request is  `/v1/test`  and you want the path to be rewritten as  `/v2/test` , we recommend that you configure the following policy:

- Route matching condition: Set the matching method to Prefix Match, and the path to  `/v1` .

- Rewrite policy: Set the rewrite method to Prefix Rewrite, and set the path to  `/v2` .

> **Important**
>
> If you want to use the prefix rewrite method, the matching type of the route must be Prefix Match. The matching type of the route cannot be Exact Match or Regex Match. If the matching type of a route is set to Prefix Match, all requests with paths that contain the specified prefix are matched and rewritten. Before you set the rewrite type of the rewrite policy to Prefix Rewrite, you must confirm whether all requests need to be rewritten. If not all requests need to be rewritten, we recommend that you set the rewrite type to Exact Rewrite.

**Host rewrite**

Cloud-native Gateway allows you to modify hostnames in requests by using the exact rewrite method.

For example, if the hostname in a request is  `test.com` , and you want the hostname to be rewritten as  `dev.com` , you must set Destination Host in the rewrite policy to  `dev.com` .

<a id="section-3-3-2"></a>

### 3.3.2. Configure a header modification policy

You can configure a header modification policy to modify the headers in requests or responses before the requests are forwarded to destination backend services or before the responses of backend services are returned to clients. This topic describes how to configure a header modification policy for a cloud-native gateway.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. On the Routing Management page, find the route that you want to manage and click its name to go to the **Routing details** page.

6. On the **Routing details** page, click the **Policy Configuration** tab.

7. On the **Policy Configuration** tab, click **Header modification** on the left side.

8. In the **Header modification** section, configure the parameters based on your business requirements and click **Save**.

   | Parameter | Description |
   | --- | --- |
   | Open | • If you enable the header modification policy, the gateway controls the headers in requests or responses.<br>• If you disable the header modification policy, the gateway does not control the headers in requests or responses. |
   | Add new request header | Click <strong>Add</strong> and enter a header name and value to add the header to a request.<br>Note<br>If the specified header already exists in a request, the specified header value in this policy is concatenated to the existing header value. The values are separated by commas (,). |
   | Modify Request Header | Click <strong>Add</strong> and enter a header name and value to modify the header in a request.<br>Note<br>• If the specified header does not exist in a request, the header is added to the request based on the header name and value specified in this policy.<br>• If the specified header already exists, its value is overwritten by the specified header value in this policy. |
   | Delete Request Header | Click <strong>Add</strong> and enter a header name to delete the header from a request. |
   | New response header | Click <strong>Add</strong> and enter a header name and value to add the header to a response.<br>Note<br>If the specified header already exists in a response, the specified header value in this policy is concatenated to the existing header value. The values are separated by commas (,). |
   | Modify Response Header | Click <strong>Add</strong> and enter a header name and value to modify the header in a response.<br>Note<br>• If the specified header does not exist in a response, the header is added to the response based on the header name and value specified in this policy.<br>• If the specified header already exists, its value is overwritten by the specified header value in this policy. |
   | Delete Response Header | Click <strong>Add</strong> and enter a header name to delete the header from a response. |

**Verify the results**

In this example, a header is added to responses. The following figure shows the configuration of the policy.

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c4919ee9ebc570bafbba1ba232df76f4.jpeg)

Run the following command to send a testing request:

```bash
curl -I  http://121.196.XX.XX/demo/item/list       // The ingress IP address of the gateway.
```

The following response is returned. The response contains the  `test:demo`  header.

```text
HTTP/1.1 200 OK
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
cache-control: no-cache, no-store, max-age=0, must-revalidate
pragma: no-cache
expires: 0
x-frame-options: DENY
content-type: application/json
content-length: 86
date: Tue, 30 Nov 2021 03:03:04 GMT
x-envoy-upstream-service-time: 4
test: demo
server: istio-envoy
```

<a id="section-3-3-3"></a>

### 3.3.3. Configure a timeout policy

Cloud-native Gateway allows you to configure timeout policies at the route level. If a gateway does not receive a response from the backend service within the specified period of time, the gateway returns an HTTP 504 (Gateway Timeout) status code to the client. This topic describes how to configure a route timeout policy for a cloud-native gateway.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. On the Routing Management page, find the route that you want to manage and click its name to go to the **Routing details** page.

6. On the **Routing details** page, click the **Policy Configuration** tab.

7. On the **Policy Configuration** tab, click the **Timeout** tab.

8. In the **Timeout** section, configure the parameters and click **Save**.

   > **Note**
   >
   > After the timeout policy is created and enabled, you can check whether the timeout policy takes effect based on your business requirements.

   | Parameter | Description |
   | --- | --- |
   | Open | Specifies whether to enable the timeout policy.<br>• If you turn on the switch, the timeout policy takes effect.<br>• If you turn off the switch, the timeout policy does not take effect. |
   | Timeout Duration | The timeout period for the current route. Unit: seconds.<br>Note<br>If you set this parameter to 0 or keep the timeout policy disabled, the gateway waits for responses all the time. |

<a id="section-3-3-4"></a>

### 3.3.4. Configure a degradation policy

Degradation is a fault-tolerance mechanism. When a backend service encounters an exception, such as a timeout or error response code, the system automatically switches to the preconfigured degraded service to ensure system availability and prevent complete service interruption.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Routing**.

5. On the Routing Management page, find the route that you want to manage and click its name to go to the **Routing details** page.

6. On the **Routing details** page, click the **Policy Configuration** tab.

7. On the **Policy Configuration** tab, click the **Downgrade** tab.

8. In the **Downgrade** section, configure the parameters and click **Save**.

   > **Important**
   >
   > - A degraded service should be simple, stable, and capable of responding quickly.
   >
   > - We recommend that you verify the degradation logic in the test environment before you deploy it to the production environment.
   >
   > - Degradation should not affect the core business logic and is used only to ensure availability.

   | Parameter | Description |
   | --- | --- |
   | Open | Specifies whether to enable the route degradation policy.<br>• If you turn on the switch, the degradation policy takes effect.<br>• If you turn off the switch, the degradation policy does not take effect. |
   | Response codes that need to be degraded | Valid values: <strong>4xx</strong> and <strong>5xx</strong>.<br>• <strong>4xx</strong>: indicates a client error. Examples: 404 and 403.<br>• <strong>5xx</strong>: indicates a server error. Examples: 500 and 502. |
   | Downgraded service | Select a backup service as the degraded service. |

<a id="section-3-4"></a>

## 3.4. Service management

<a id="section-3-4-1"></a>

### 3.4.1. Create a service

To allow a gateway to obtain service endpoints, you must add an existing service to the gateway and register the service as a destination service for routing. Cloud-native Gateway allows you to add services from the following sources: fixed endpoints and Domain Name System (DNS) domain names.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Service**.

5. On the **Service List** page, click **Create Service**.

6. On the **Create Service** page, configure the following parameters and then click **Submission**.

   > **Note**
   >
   > When the cloud-native gateway forwards a request to a backend service that uses a specified domain name, the gateway does not rewrite the host domain name as the specified domain name.

   | Parameter | Description |
   | --- | --- |
   | Name | The name of the service. |
   | Source Type | Valid values: <strong>DNS domain name</strong> and <strong>Fixed</strong> <strong>Address</strong>.<br>• <strong>DNS domain name</strong>: The cloud-native gateway allows you to use the DNS resolution result as the backend service endpoint.<br>• <strong>Fixed Address</strong>: If the service discovery mechanism is not provided for the service that you want to add, you must manually add the backend node endpoint of the service to the gateway. |
   | Node | • If you set <strong>Source Type</strong> to <strong>DNS domain</strong> <strong>name</strong>, specify the <strong>Domain Name</strong> and <strong>Port</strong> parameters.<br>• <strong>Domain Name</strong>: the domain name of the service.<br>• <strong>Port</strong>: the port that is used to access the domain name of the service.<br>• If you set <strong>Source Type</strong> to <strong>Fixed Address</strong>, specify <strong>Host name/IP</strong> and <strong>Port</strong> parameters.<br>• <strong>Host name/IP</strong>: the address of the backend node of the service, which can be a hostname or an IP address.<br>• <strong>Port</strong>: the port number of the backend node address for the service. |
   | Protocol Type | The protocol used by the service. Valid values: <strong>HTTP</strong> and <strong>HTTPS</strong>. |
   | Enable Health Check | If health check is enabled, the system proactively sends requests (such as TCP connection or HTTP GET) to check whether the service node is alive and determines whether the node is available. |
   | Health Check Protocol | • <strong>HTTP</strong>: HTTP health checks simulate how a web browser accesses resources by sending requests to check whether the server application is healthy.<br>• <strong>TCP</strong>: TCP health checks detect whether the server port is alive by sending SYN handshake packets. |
   | Health Checkup Path | The URI of the web page on which you want to perform a health check. We recommend that you perform a health check only on static web pages.<br>Note<br>This parameter is required if you set the <strong>Health Check Protocol</strong> parameter to <strong>HTTP</strong>. |
   | Health Check Domain Name (Optional) | It can contain only letters, digits, hyphens (-), and periods (.). By default, the Host header is not used.<br>Note<br>This parameter is required if you set the <strong>Health Check Protocol</strong> parameter to <strong>HTTP</strong>. |
   | Normal status code | Backend servers that return the specified normal status codes are considered healthy.<br>Note<br>This parameter is required if you set the <strong>Health Check Protocol</strong> parameter to <strong>HTTP</strong>. |
   | Health check response timeout duration | The threshold for the timeout period of each health check response. If a health check does not provide a response within the period specified by this parameter, the backend server is considered unhealthy. |
   | Health Check Interval | The interval between two consecutive health checks. |
   | Health Check Health Threshold | The number of times that an unhealthy backend server must consecutively pass health checks before it can be declared healthy. |
   | Health Check Unhealthy Threshold | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. |

<a id="section-3-4-2"></a>

### 3.4.2. Manage services

After you add a service whose Service Source is set to Fixed Address to a cloud-native gateway, the endpoint of the backend node that corresponds to the service may change. In this case, the cloud-native gateway cannot dynamically obtain the new endpoint of the backend node. To allow the gateway to obtain the new endpoint, you must modify the service information to manually adjust the endpoint of the backend node that corresponds to the service. This topic describes how to view, modify, and delete a service.

**View the details of a service**

After a service is created, you can view the details of the service. If a large number of services are available, you can filter and search for services to improve the search efficiency.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Service**.

5. Optional. On the **Service List** page, you can filter services by **Service Name**.

6. In the service list, find the service that you want to manage and click its name. On the **Service Details** page, you can view the information on the **Service Details**, **Plugin configuration**, and **Associated Routing** tabs.

   - On the **Service Details** tab, you can view the details of the service in the **Basic information**, **Node List**, and **Associated Routing** sections.

     - In the **Basic information** section, you can view the **Name**, **Source Type**, and **Protocol Type** settings of the service.

     - In the **Node List** section, you can view **Host name/IP** and **Port**.

   - On the **Plugin configuration** tab, you can manage the plug-ins that are bound to the service. You can click **AddPlugin** to bind a plug-in to the service. For more information, see Create a plug-in.

     > **Note**
     >
     > In the service list, you can click **Plugin configuration** in the **Operation** column to go to the **Plugin configuration** tab.

   - On the **Associated Routing** tab, you can view the routes associated with the service.

**Modify a service**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Service**.

5. In the service list, find the service that you want to modify and click **Edit** in the **Operation** column.

6. In the **Edit Service** panel, modify the relevant parameters and click **Submission**.

   > **Note**
   >
   > You can modify the static IP addresses and Domain Name System (DNS) services that you created. Services of other types cannot be modified, such as Kubernetes services.

**Delete services**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Service**.

5. Delete services.

   - Delete a service: In the service list, find the service that you want to manage and click **Delete** in the **Operation** column.

   - Delete multiple services at a time: In the service list, select the services that you want to delete and click **Batch Delete**.

6. In the **Alert** message, click **Determine**.

<a id="section-3-5"></a>

## 3.5. Consumer management

<a id="section-3-5-1"></a>

### 3.5.1. Create a consumer

Cloud-native Gateway enables authentication for routes and APIs by using consumers. This topic describes how to create a consumer in the Cloud-native Gateway console.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. On the **Consumer** page, click **Create Consumer**.

6. In the **Create Consumer** panel, configure the following parameters and click **Determine**.

   | Parameter | Description |
   | --- | --- |
   | Name | The name of the consumer. The name must be unique within a Cloud-native Gateway instance. |
   | Description | The description of the consumer. |
   | Authentication Method | The authentication method used by the consumer. Currently, only <strong>API KEY</strong> is supported. |
   | Token | The API key.<br>• System-generated: The system automatically generates an API key.<br>• Customize: You need to specify an API key and the source of the API key. |

<a id="section-3-5-2"></a>

### 3.5.2. View the details of a consumer

This topic describes how to view the details of a consumer.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. On the **Consumer** page, click the name of the consumer that you want to view. On the **Consumer Details** page, you can view the information on the **Basic configuration** and **Consumer Authorization** tabs.

   - On the **Basic configuration** tab, you can view **Basic information** and **Consumer Certification** of the consumer.

     - **Basic information**: displays the following information about the consumer: **Consumer ID**, **Consumer Name**, **Consumer Notes**, and **Consumer Status**.

     - **Consumer Certification**: displays the following information: **Authentication method** and **Token**.

   - On the **Consumer Authorization** tab, you can perform authorization management for the consumer. For more information, see Manage authorization.

<a id="section-3-5-3"></a>

### 3.5.3. Authorization management

This topic describes how to manage authorization for API consumers and ensure that only authenticated requests with proper permission verification can access service resources.

**Authorize a consumer to access a route**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. On the **Consumer** page, use one of the following methods to go to the **Consumer Authorization** tab:

   - Method 1: Find the consumer that you want to manage and click **Authorization** in the **Operation** column.

   - Method 2: Find the consumer that you want to manage and click its name. On the **Consumer Details** page, click the **Consumer Authorization** tab.

6. On the **Consumer Authorization** tab, click **Associated Routing**, select the route on which you want the consumer to have access permissions, and then click **Determine**. You can select multiple routes.

   > **Note**
   >
   > If no route is available, create one. For more information, see Route management.

**Revoke authorization**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. On the **Consumer** page, use one of the following methods to go to the **Consumer Authorization** tab:

   - Method 1: Find the consumer that you want to manage and click **Authorization** in the **Operation** column.

   - Method 2: Find the consumer that you want to manage and click its name. On the **Consumer Details** page, click the **Consumer Authorization** tab.

6. In the route list, find the route that you want to revoke authorization and click **Delete** in the **Operation** column. In the **Alert** message, click **Determine**.

<a id="section-3-5-4"></a>

### 3.5.4. Modify the configuration of a consumer

This topic describes how to modify the configuration of a consumer.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. On the **Consumer** page, find the consumer that you want to manage and click **Edit** in the **Operation** column.

6. In the **Edit Consumer** panel, modify the related parameters and click **Determine**.

<a id="section-3-5-5"></a>

### 3.5.5. Delete a consumer

This topic describes how to delete a customer from a cloud-native gateway.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Consumer**.

5. Delete consumers.

   - Delete a consumer: On the **Consumer** page, find the consumer that you want to delete and click **Delete** in the **Operation** column.

   - Delete multiple consumers at a time: On the **Consumer** page, select the consumers that you want to delete and click **Batch Delete**.

6. In the **Alert** message, click **Determine**.

<a id="section-3-6"></a>

## 3.6. Plug-in management

<a id="section-3-6-1"></a>

### 3.6.1. Create a plug-in

Plug-in configurations allow you to apply various plug-ins in a cloud-native gateway to various domain objects and combinations of domain objects. For example, a traffic control plug-in can be configured on a route or a service, which enables greater flexibility in plug-in configurations for the cloud-native gateway.

**Background information**

In Cloud-native Gateway, various plug-ins are available. In addition, the following domain objects exist in Cloud-native Gateway.

- Routes

- Services

- Domain names

In a cloud-native gateway, for the same domain object or combination of domain objects, multiple instances of the same type of plugin configuration can be applied. For example, multiple throttling rules can be configured on a single route.

**Supported plug-in types**

- Authentication

  - key-auth

  - jwt-auth

  - basic-auth

  - oidc

  - hmac-auth

  - ext-auth

  - oauth

  - opa

- Security

  - cors

  - ip-restriction

  - waf

  - request-block

  - bot-detect

- Throttling

  - cluster-key-rate-limit

  - key-rate-limit

  - traffic-tag

  - requet-validation

- Transmission

  - transformer

  - frontend-gray

  - custom-response

  - de-graphql

  - cache-control

- Observability

  - geo-ip

  - log-request-response

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. Go to the entry point for creating a plug-in.

   > **Note**
   >
   > The system provides four entry points for creating plug-ins and their applicable scenarios. You can select one based on your requirements.
   >
   > - Plug-ins created through the main entry point apply to the current instance.
   >
   > - Plug-ins created through the quick entry point apply to the current service, route, or domain name.

   - **Main entry point**: If you want to create a plug-in for the current instance, we recommend that you use this entry point.

     <ol type="a">

     <li>

     In the left-side navigation pane, click **Plugin Management**. Then, click **Create Policy**.

     </li>

     <li>

     On the **Create Policy** page, select a plug-in.

     </li>

     </ol>

   - **Quick entry point 1**: If you want to create a plug-in for a route or a combination of domain objects that contain the route, we recommend that you use this entry point.

     <ol type="a">

     <li>

     In the left-side navigation pane, click **Routing**.

     </li>

     <li>

     On the **Routing Management** page, find the route that you want to manage and click **Policy Configuration** in the **Operation** column.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     On the **Plugin configuration** tab, click **AddPlugin** to go to the **Create Policy** page. Then, select the desired plug-in to create a plug-in.

     </li>

     </ol>

   - **Quick entry point 2**: If you want to create a plug-in for a service or a combination of domain objects that contain the service, we recommend that you use this entry point.

     <ol type="a">

     <li>

     In the left-side navigation pane, click **Service**.

     </li>

     <li>

     On the **Service List** page, find the service that you want to manage and click **Plugin configuration** in the **Operation** column.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     On the **Plugin configuration** tab, click **AddPlugin** to go to the **Create Policy** page. Then, select the desired plug-in to create a plug-in.

     </li>

     </ol>

   - **Quick entry point 3**: If you want to create a plug-in for a domain name or a combination of domain objects that contain the domain name, we recommend that you use this entry point.

     <ol type="a">

     <li>

     In the left-side navigation pane, click **Domain Name**.

     </li>

     <li>

     On the **Domain Name Management** page, find the domain name that you want to manage and click **Plugin Configuration** in the **Operation** column.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     On the **Plugin configuration** tab, click **AddPlugin** to go to the **Create Policy** page. Then, select the desired plug-in to create a plug-in.

     </li>

     </ol>

5. Click **Create a plugin** below the desired card, configure the parameters based on the selected plug-in, and then click **Determine**.

   > **Note**
   >
   > The following example shows how to create a cors plug-in. The procedure for other plug-ins is similar.

   | Parameter | Description |
   | --- | --- |
   | Scope of action | Valid values: <strong>Global</strong> and <strong>Local</strong>.<br>• <strong>Global</strong>: By default, the plug-in is applied to the instance.<br>• <strong>Local</strong>: You need to specify the domain object or combination of domain objects to which the plug-in is bound. The available domain objects vary with the plug-in type. If you specify a combination of domain objects, the relationship between these domain objects is logical AND. For example, if a local plug-in is bound to both a route and a consumer, the plug-in is executed only for requests that carry the consumer token and match the specified route. |
   | Binding Type | This parameter is required only if <strong>Scope of</strong> <strong>action</strong> is set to <strong>Local</strong>.<br>Valid values: <strong>Routing</strong>, <strong>Service</strong>, and <strong>Domain</strong> <strong>name</strong>. |
   | Bind Route | This parameter is required only if <strong>Binding Type</strong> is set to <strong>Routing</strong>.<br>Select the route that you want to associate with the plug-in. If no route is available, create one.For more information, see Route management. |
   | Binding Service | This parameter is required only if <strong>Binding Type</strong> is set to <strong>Service</strong>.<br>Select the service to be bound to the plug-in. If no service is available, create one. For more information, see Create a service. |
   | Bind a domain name | This parameter is required only if <strong>Binding Type</strong> is set to <strong>Domain name</strong>.<br>Select the domain name that you want to bind to the plug-in. If no domain name is available, create one. For more information, see Create a domain name. |
   | cors | Configure the cors plug-in. Click <strong>View</strong> <strong>Document</strong> or see Cross-origin resource sharing for configuration instructions. |

<a id="section-3-6-2"></a>

### 3.6.2. Manage plug-ins

This topic describes how to manage plug-ins.

**View plug-in details**

After a plug-in is created, you can view the details of the plug-in.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Plugin**.

5. Optional. On the **Plugin Management** page, you can filter plug-ins by **Plugin ID** or **Plugin type**.

6. In the plug-in list, find the plug-in that you want to view and click its ID. On the **Policy configuration details** page, you can view **Basic Information** and **Plugin Information**.

   - **Basic Information**: displays the following information about the plug-in: **Name**, **Plugin type**, **Plugin status**, **Scope of action**, **Creation time**, and **Update time**.

   - **Plugin Information**: displays the details of the plug-in.

**Enable and disable a plug-in**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Plugin**.

5. In the plug-in list, find the plug-in that you want to manage and click **Enable** or **Disable** in the **Operation** column.

6. In the **Alert** message, click **Determine**.

**Modify a plug-in**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Plugin**.

5. In the plug-in list, find the plug-in that you want to manage and click **Edit** in the **Operation** column.

6. On the **To edit a plugin** page, modify the configuration of the plug-in and click **Determine**.

**Delete a plug-in**

If you no longer need a plug-in, you can delete it.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Plugin**.

5. In the plug-in list, find the plug-in that you want to delete and click **Delete** in the **Operation** column.

6. In the **Alert** message, click **Determine**.

<a id="section-3-6-3"></a>

### 3.6.3. Authentication

<a id="section-3-6-3-1"></a>

#### 3.6.3.1. key-auth

**Introduction**

The  `key-auth`  plug-in is used for authentication based on API keys. You can use the key-auth plug-in to parse API keys from the URL parameters or request headers of HTTP requests and check whether the API keys are valid for access to services.

**Fields**

- The authorization configuration and authentication configuration cannot coexist in a rule.

- For an authenticated request, an  `X-Mse-Consumer`  field is added to the request header to identify the name of the caller.

**Authentication configuration**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td><code>global_auth</code></td>
    <td>bool</td>
    <td>No (<strong>Required</strong> only for instance-level <strong>configurations</strong>)</td>
    <td>-</td>
    <td>This field can be configured only at the instance level. If this field is set to true, the authentication mechanism globally takes effect. If this field is set to false, the authentication mechanism takes effect only for the configured domain names and routes. If this field is not configured, the authentication mechanism globally takes effect only when no domain names and routes are configured. This is in consideration of the usage habits of existing users.</td>
  </tr>
  <tr>
    <td><code>consumers</code></td>
    <td>array of object</td>
    <td>Yes</td>
    <td>-</td>
    <td>The callers of the service. This field is used to authenticate requests.</td>
  </tr>
  <tr>
    <td><code>keys</code></td>
    <td>array of string</td>
    <td>Yes</td>
    <td>-</td>
    <td>The source fields of the API keys.Source fields can be URL parameters or HTTP request headers.</td>
  </tr>
  <tr>
    <td><code>in_query</code></td>
    <td>bool</td>
    <td>No (You must set at least one of <code> in_query </code> and <code> in_header </code> to true.)</td>
    <td>true</td>
    <td>If this field is set to true, the gateway attempts to parse API keys from URL parameters.</td>
  </tr>
  <tr>
    <td><code>in_header</code></td>
    <td>bool</td>
    <td>No (You must set at least one of <code> in_query </code> and <code> in_header </code> to true.)</td>
    <td>true</td>
    <td>If this field is set to true, the gateway attempts to parse API keys from HTTP request headers.</td>
  </tr>
</table>

The following table describes the fields in  `consumers` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>credential</code> | string | Yes | - | The access credential of the consumer. |
| <code>name</code> | string | Yes | - | The name of the consumer. |

**(Optional) Authorization configuration**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td><code>allow</code></td>
    <td>array of string</td>
    <td>No (<strong>Required</strong> for non-instance-level <strong>configurations</strong>)</td>
    <td>-</td>
    <td>You can only configure this field at a fine granularity such as route or domain name.For requests that meet the matching conditions, you can configure consumers that are allowed for access. This implements fine-grained permission control.</td>
  </tr>
</table>

**Configuration examples**

**Configure global authentication and route-level authorization**

This section provides an example on how to enable authentication and authorization based on the key-auth plug-in for specific routes or domain names of the gateway. The credential field must be unique.

Apply the following plug-in configurations at the instance level:

```text
global_auth: false
consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

Apply the following configurations to the route-a and route-b routes:

```text
allow:
- consumer1
```

Apply the following configurations to the \*.example.com and test.com domain names:

```text
allow:
- consumer2
```

> **Note**
>
> - In this example, the route-a and route-b routes are those specified when the gateway routes are created. If a client request matches one of the two routes, the caller whose name is consumer1 is allowed to access the gateway. Other callers are not allowed to access the gateway.
>
> - In this example, the \*.example.com and test.com domain names are used to match domain names in requests. If a client request matches one of the domain names, the caller whose name is consumer2 is allowed to access the gateway. Other callers are not allowed to access the gateway.

The preceding configurations allow access from the following requests:

**Assume that the following request matches the route-a route. In this case, provide the API key in the custom url parameter.**

```bash
curl  http://xxx.hello.com/test?apikey=2bda943c-ba2b-11ec-ba07-00163e1250b5
```

**Provide the API key in an HTTP request header.**

```bash
curl  http://xxx.hello.com/test -H 'x-api-key: 2bda943c-ba2b-11ec-ba07-
00163e1250b5'
```

After the authentication is passed, the  `X-Mse-Consumer`  field is added to headers of requests to identify the caller. In this example, the value of this field is  `consumer1` .

The preceding configurations deny access from the following requests:

**No API key is specified in the request, and the HTTP 401 status code is returned.**

```bash
curl  http://xxx.hello.com/test
```

**The API key that is specified in the request is invalid, and the HTTP 401 status code is returned.**

```bash
curl  http://xxx.hello.com/test?apikey=926d90ac-ba2e-11ec-ab68-00163e1250b5
```

**The caller that is matched by using the API key has no access permission, and the HTTP 403 status code is returned.**

```bash
# The consumer named consumer2 is not in the allow list of route-a.
curl  http://xxx.hello.com/test?apikey=c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
```

**Enable authentication at the gateway level**

After you apply the following configurations to a gateway, basic authentication is enabled at the instance level and all requests must be authenticated to access the gateway.

```text
global_auth: true
consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

<a id="section-3-6-3-2"></a>

#### 3.6.3.2. jwt-auth

The jwt-auth plug-in is used for authentication and authorization based on JSON Web Tokens (JWTs). This plug-in allows you to parse JWTs from URL parameters, headers, or cookies in HTTP requests and validate JWTs. In addition to the manual configuration of JWT authentication, you can use the jwt-auth plug-in. The plug-in provides the caller identification capability and allows you to configure different JWT credentials for different callers. This topic describes how to configure the jwt-auth plug-in.

**Fields**

**Authentication configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| consumers | array of object | Yes | - | The callers of the service.This field is used to authenticate requests. |
| global_auth | array of string | No (Required only for instance-level configurations) | - | This field can be configured only at the instance level.<br>• If this field is set to true, the authentication mechanism globally takes effect.<br>• If this field is set to false, the authentication mechanism takes effect only for the configured domain names and routes.<br>• If this field is not configured, the authentication mechanism globally takes effect only when no domain names and routes are configured.This is in consideration of the usage habits of existing users. |

The following table describes the fields in the  `consumers`  field.

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| name | string | Yes | - | The name of the consumer. |
| jwks | string | No (You must configure jwks or remote_jwks.) | - | A JWK is a JSON string that represents a cryptographic key. A JSON Web Key Set (JWKS) is a set of public keys or symmetric keys that are used to validate the signature of a JWT. |
| remote_jwks | object | No (You must configure jwks or remote_jwks.) | {"uri":" http://1 27.0.0.1/keys", "servic e":"test.static"," port":"8 0","ttl": 30000," timeout ":3000} | This field is used to periodically pull a JWKS from a specified Uniform Resource Identifier (URI) of a specified service. If you configure both the jwks and remote_jwks fields, the JWKS that is pulled based on the remote_jwks field prevails.<br>Note<br>We recommend that you set the size of the jwks returned by remote_jwks to less than 1 MB. |
| issuer | string | No | - | The JWT issuer. The value of this field must be the same as the value of the iss field in the payload. |
| claims | object | No | - | The key and value of this field correspond to the key and value in the payload.This field can be used to check whether the values of multiple fields are the same as the values of the related fields in the payload. For example, if you configure aud: mobile-site, the value of the aud field in the payload must be mobile-site. |
| claims_to_he aders | array of object | No | - | The header fields that are extracted from the JWT payload. You can configure the fields in the specified request header and forward the request to the backend service. |
| from_header s | array of object | No | \[{"nam e":"Aut horizati on","val ue_pref ix":"Be arer"}\] | The request headers from which you can extract the JWT. |
| from_params | array of string | No | access_token | The URL parameters from which you can extract the JWT. |
| from_cookies | array of string | No | - | The cookies from which you can extract the JWT. |
| clock_skew_s econds | number | No | 60 | The clock skew allowed when the exp and iat fields in the JWT are verified. Unit: seconds. |
| keep_token | bool | No | true | Specifies whether to retain the JWT in the request when the request is forwarded to the backend service. |

> **Note**
>
> The default value is used only if none of  `from_headers` ,  `from_params` , and  `from_cookies`  are configured.

- The following table describes the fields in the  `from_headers`  field.

  | Field | Data type | Required | Defaul t value | Description |
  | --- | --- | --- | --- | --- |
  | name | string | Yes | - | The request header from which you can extract the JWT. |
  | value_prefix | string | Yes | - | The value prefix that needs to be removed from the request header. After the prefix is removed, the remaining part of value is used as the JWT. |

- The following table describes the fields in the  `claims_to_headers`  field.

  | Field | Data type | Required | Defaul t value | Description |
  | --- | --- | --- | --- | --- |
  | claim | string | Yes | - | The field in the JWT payload. The value must be a string or an unsigned integer. |
  | header | string | Yes | - | The request header in which the field value extracted from the payload is configured. The request with this header is forwarded to the backend service. |
  | override | bool | No | true | • If this field is set to true, the request header with the same name is overwritten.<br>• If this field is set to false, the request header with the same name is appended. |

- The following table describes the fields in the  `remote_jwks`  field.

  | Field | Data type | Required | Defaul t value | Description |
  | --- | --- | --- | --- | --- |
  | uri | string | Yes | - | The request URL. |
  | service | string | Yes | - | • Example of a Kubernetes service: foo.default.svc.cluster.loc al.<br>• Example of a Nacos service: foo.DEFAULT-GROUP.public.nacos.<br>• For a DNS service named test, set this field to test.dns.<br>• For a static IP service named test, set this field to test.static. |
  | port | bool | Yes | - | The port number of the service. |
  | timeout | bool | No | 3000 | The timeout period of the service request. Unit: milliseconds. |
  | ttl | bool | No | 30000 | The time to live (TTL) duration. Unit: milliseconds. |

**(Optional) Authorization configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| allow | array of string | No (Required for non-instance-level configurations) | - | You can configure this field only at a fine granularity such as route or domain name. For requests that meet the matching conditions, you can configure consumers that are allowed for access. This implements fine-grained permission control. |

> **Important**
>
> - The authorization configuration and authentication configuration cannot coexist in a rule.
>
> - For authenticated requests, the  `X-Mse-Consumer`  field is added to the request header to identify the names of the callers.

**Configuration examples**

**Configure global authentication and route-level authorization**

This section provides an example on how to enable JWT authentication and authorization for specific routes or domain names of a gateway.

> **Note**
>
> If a JWT matches multiple JWKSs, the first matched consumer is hit based on the configuration order.

**Plug-in configurations**

Apply the following plug-in configurations at the instance level:

```text
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k": 
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqXpNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD-
MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct--
7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC
NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
      ]
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n": 
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha
LMt2iyiSb9LZJAeJmHf7ecguXS_-
4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3-
anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz-
N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT
POGZh_25KXGdF_ZC_MSRw"
        }
      ]
    }
```

**Route and domain name configurations**

Apply the following plug-in configurations to the  `route-a`  and  `route-b`  routes:

```text
allow:
- consumer1
```

Apply the following plug-in configuration to the  `*.example.com`  and  `test.com`  domain names:

```text
allow:
- consumer2
```

> **Note**
>
> - In this example, the  `route-a`  and  `route-b`  routes are those specified when the gateway routes are created. If a client request matches one of the routes, the caller whose  `name`  is  `consumer1`  is allowed to access the gateway. Other callers are not allowed to access the gateway.
>
> - In this example, the  `*.example.com`  and  `test.com`  domain names are used to match domain names in requests. If a client request matches one of the domain names, the caller whose  `name`  is  `consumer2`  is allowed to access the gateway. Other callers are not allowed to access the gateway.

**Sample requests**

The preceding configurations allow access from the following requests. In this example, route-a is matched.

- Configure the JWT in a URL parameter.

  ```bash
  curl  'http://xxx.hello.com/test?
  access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEy****.eyJp************.-v
  BSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
  ```

- Configure the JWT in an HTTP request header.

  ```bash
  curl  http://xxx.hello.com/test -H 'Authorization: Bearer 
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEyMyJ9.eyJpc3MiOiJhYmNkIiwic3ViIjoidGVzdC
  ImlhdCI6MTY2NTY2MDUyNywiZXhwIjoxODY1NjczODE5fQ.-
  vBSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
  ```

**Verify the results**

After the authentication is passed, the  `X-Mse-Consumer`  field is added to headers of requests to identify the caller. In this example, the value of this field is  `consumer1` .

The following requests are denied:

- The JWT is not provided in the request, and the HTTP 401 status code is returned.

- The caller that matches the JWT in the request has no access permissions, and the HTTP 403 status code is returned.

**Enable authentication for gateways at the instance level and disable authentication for specific routes**

Apply the following plug-in configurations at the instance level:

```text
global_auth: true
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k": 
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqXpNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD-
MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct--
7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC
NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
      ]
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n": 
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha
LMt2iyiSb9LZJAeJmHf7ecguXS_-
4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3-
anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz-
N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT
POGZh_25KXGdF_ZC_MSRw"
        }
      ]
    }
```

Apply the following plug-in configuration to  `route-b`  route:

```text
_disable_: true
```

In this example, the  `route-b`  route is the route specified when the gateway route is created. If  `_disable_`  is set to  `true`  and the route is matched, the plug-in feature is disabled. In this case, JWT-based authentication is not required for the route, and the route is accessible to all users.

If  `global_auth`  is set to  `true`  in the global configuration and  `route-b`  is not matched, authentication is enabled for all requests. In this case, JWT-based authentication is required, and both  `consumer1`  and  `consumer2`  are allowed to access the gateway.

**Enable authentication for a domain name and disable authentication for a specific route**

Apply the following plug-in configurations at the instance level:

```text
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k": 
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqXpNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD-
MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct--
7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC
NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
      ]
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n": 
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha
LMt2iyiSb9LZJAeJmHf7ecguXS_-
4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3-
anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz-
N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT
POGZh_25KXGdF_ZC_MSRw"
        }
      ]
    }
```

Apply the following plug-in configuration to  `route-b`  route:

```text
_disable_: true
```

Apply the following plug-in configuration to the  `*.example.com`  domain name:

```text
allow:
- consumer1
- consumer2
```

In this example, the  `route-b`  route is the route specified when the gateway route is created. If  `_disable_`  is set to  `true`  and the route is matched, the plug-in feature is disabled. In this case, JWT-based authentication is not required for the route, and the route is accessible to all users.

In this example, the  `*.example.com`  domain name is used to match the domain name in requests. If the domain name is matched, the caller whose  `name`  is  `consumer1`  or  `consumer2`  is allowed to access the gateway. Other callers are not allowed to access the gateway.

The rules are applied in sequence. If a route or domain name is matched based on a rule, the configuration of the rule is used and other rules are skipped. The route-based match prevails over domain name-based match. You can enable authentication for the configured domain name and disable authentication for specific routes under the domain name.

**Error codes**

| HTTP status code | Error message | Reason |
| --- | --- | --- |
| 401 | Jwt missing | The JWT is not provided in the request header. |
| 401 | Jwt expired | The JWT has expired. |
| 401 | Jwt verification fails | JWT payload verification failed in scenarios such as a mismatch of the iss field. |
| 403 | Access Denied | The consumer is not authorized to access the current route. |

<a id="section-3-6-3-3"></a>

#### 3.6.3.3. basic-auth

The basic-auth plug-in is used for authentication based on the HTTP basic authentication specification. This topic describes how to configure the basic-auth plug-in.

**Plug-in type**

Plug-in for authentication and authorization.

**Fields Authentication configurations**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| consumers | array of object | Yes | - | The callers of the service.This field is used to authenticate requests. |
| global_auth | array of string | No (Required only for instance-level configurations) | - | This field can be configured only at the instance level.<br>• If this field is set to true, the authentication mechanism globally takes effect.<br>• If this field is set to false, the authentication mechanism takes effect only for the configured domain names and routes.<br>• If this field is not configured, the authentication mechanism globally takes effect only when no domain names and routes are configured.This is in consideration of the usage habits of existing users. |

The following table describes the fields in  `consumers` .

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| credential | string | Yes | - | The access credential of the consumer. |
| name | string | Yes | - | The name of the consumer. |

**(Optional) Authorization configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| allow | array of string | No (Required for non-instance-level configurations) | - | You can configure this field only at a fine granularity such as route or domain name. For requests that meet the matching conditions, you can configure consumers that are allowed for access. This implements fine-grained permission control. |

> **Important**
>
> - The authorization configuration and authentication configuration cannot coexist in a rule.
>
> - For authenticated requests, the  `X-Mse-Consumer`  field is added to the request header to identify the names of the callers.

**Configuration examples**

**Configure global authentication and route-level authorization**

This section provides an example on how to enable basic authentication and authorization for specific routes or domain names of a gateway.

> **Note**
>
> - The username and password in the credential information are separated by a colon (:).
>
> - The  `credential`  field must be unique.

Apply the following plug-in configurations at the instance level:

```text
global_auth: false
consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

Apply the following plug-in configurations to the  `route-a`  and  `route-b`  routes:

```text
allow:
- consumer1
```

Apply the following plug-in configuration to the  `*.example.com`  and  `test.com`  domain names:

```text
allow:
- consumer2
```

> **Note**
>
> - In this example, the  `route-a`  and  `route-b`  routes are those specified when the gateway routes are created. If a client request matches one of the routes, the caller whose  `name`  is  `consumer1`  is allowed to access the gateway. Other callers are not allowed to access the gateway.
>
> - In this example, the  `*.example.com`  and  `test.com`  domain names are used to match domain names in requests. If a client request matches one of the domain names, the caller whose  `name`  is  `consumer2`  is allowed to access the gateway. Other callers are not allowed to access the gateway.

- The preceding configurations allow access from the following requests:

  The username and password are specified in the request.

  ```bash
  # In this example, route-a in the request is matched.
  # Use the -u parameter in the curl command to specify the username and password.
  curl -u admin:123456  http://xxx.hello.com/test
  # You can also directly specify the Authorization request header in which the username and password are base64-encoded.
  curl -H 'Authorization: Basic YWRtaW46MTIzNDU2'  http://xxx.hello.com/test
  ```

  > **Note**
  >
  > After the authentication is passed, the  `X-Mse-Consumer`  field is added to headers of requests to identify the caller. In this example, the value of this field is  `consumer1` .

- The preceding configurations deny access from the following requests:

  - The username and password are not specified in the request, and the HTTP 401 status code is returned.

    ```bash
    curl  http://xxx.hello.com/test
    ```

  - The username or password is invalid in the request, and the HTTP 401 status code is returned.

    ```bash
    curl -u admin:abc  http://xxx.hello.com/test
    ```

  - The caller who matches the username and password in the request has no access permission, and the HTTP 403 status code is returned.

    ```bash
    # The consumer named consumer2 is not in the allow list of route-a.
    curl -u guest:abc  http://xxx.hello.com/test
    ```

**Enable authentication for gateways**

After you apply the following configurations to a gateway, basic authentication is enabled at the instance level and all requests must be authenticated to access the gateway.

```text
global_auth: true
consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

**Error codes**

| HTTP status code | Error message | Reason |
| --- | --- | --- |
| 401 | Request denied by Basic Auth check. No Basic Authentication information found. | The credential is not specified in the request. |
| 401 | Request denied by Basic Auth check. Invalid username and/or password. | The request credential is invalid. |
| 403 | Request denied by Basic Auth check. Unauthorized consumer. | The caller of the request does not have access permissions. |

<a id="section-3-6-3-4"></a>

#### 3.6.3.4. oidc

The oidc plug-in supports OpenID Connect (OIDC) authentication. In addition, this plug-in enhances protection against cross-site request forgery (CSRF) attacks and supports the logout endpoint and refresh token mechanisms in the OIDC protocol. After the Wasm plug-in performs OIDC authentication on a request, the request carries an  `Authorization`  header that contains the corresponding access token.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `350` .

**Fields**

| Field | Data type | Description | Default value |
| --- | --- | --- | --- |

<table>
  <tr>
    <td>cookie_name</td>
    <td>string</td>
    <td>the name of the cookie that the oauth_proxy creates. Should be changed to use a cookie prefix(<code> __Host- </code> or <code> __Secure- </code>) if <code> --</code><code>cookie-secure </code> is set.</td>
    <td><code>"_oauth2_proxy"</code></td>
  </tr>
  <tr>
    <td>cookie_secret</td>
    <td>string</td>
    <td>the seed string for secure cookies (optionally base64 encoded)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>cookie_domains</td>
    <td>string|list</td>
    <td>Optional cookie domains to force cookies to, such as<code>.yourcompany.com</code>. The longest domain that matches the request host will be used (or the shortest cookie domain if no match is available).</td>
    <td>-</td>
  </tr>
  <tr>
    <td>cookie_path</td>
    <td>string</td>
    <td>an optional cookie path to force cookies to (e.g. <code> /poc/ </code>)</td>
    <td><code>"/"</code></td>
  </tr>
  <tr>
    <td>cookie_expire</td>
    <td>duration</td>
    <td>expire timeframe for cookie. If set to 0, cookie becomes a session-cookie which will expire when the browser is closed.</td>
    <td>168h0m0s</td>
  </tr>
  <tr>
    <td>cookie_refresh</td>
    <td>duration</td>
    <td>refresh the cookie after this duration; <code> 0 </code> to disable</td>
    <td>-</td>
  </tr>
  <tr>
    <td>cookie_secure</td>
    <td>bool</td>
    <td>set secure (HTTPS only) cookie flag</td>
    <td>true</td>
  </tr>
  <tr>
    <td>cookie_httponly</td>
    <td>bool</td>
    <td>set HttpOnly cookie flag</td>
    <td>true</td>
  </tr>
  <tr>
    <td>cookie_samesite</td>
    <td>string</td>
    <td>set SameSite cookie attribute (<code> "lax" </code>, <code> "strict"</code><code> </code>, <code> "none" </code>, or <code> "" </code>).</td>
    <td><code>""</code></td>
  </tr>
  <tr>
    <td>cookie_csrf_per_reque st</td>
    <td>bool</td>
    <td>Enable having different CSRF cookies per request, making it possible to have parallel requests.</td>
    <td>false</td>
  </tr>
  <tr>
    <td>cookie_csrf_expire</td>
    <td>duration</td>
    <td>expire timeframe for CSRF cookie.</td>
    <td>15m</td>
  </tr>
  <tr>
    <td>client_id</td>
    <td>string</td>
    <td>the OAuth Client ID.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>client_secret</td>
    <td>string</td>
    <td>the OAuth Client Secret.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>provider</td>
    <td>string</td>
    <td>OAuth provider.</td>
    <td>oidc</td>
  </tr>
  <tr>
    <td>pass_authorization_he ader</td>
    <td>bool</td>
    <td>pass OIDC IDToken to upstream via Authorization Bearer header.</td>
    <td>true</td>
  </tr>
  <tr>
    <td>oidc_issuer_url</td>
    <td>string</td>
    <td>the OpenID Connect issuer URL, e.g. <code> "https://dev-</code><code>o43xb1mz7ya7ach4.us.</code><code>auth0.com" </code>.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>oidc_verifier_request_t imeout</td>
    <td>uint32</td>
    <td>OIDC verifier discovery request timeout.</td>
    <td>2000(ms)</td>
  </tr>
  <tr>
    <td>scope</td>
    <td>string</td>
    <td>OAuth scope specification.</td>
    <td>-</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/0c115cffb618385a265d90e4ea63a811.png)

<table>
  <tr>
    <td>redirect_url</td>
    <td>string</td>
    <td>the OAuth Redirect URL, e.g. <code> "https://inter</code> <code>nalapp.yourcompany.c</code><br><code>om/oauth2/callback"</code><code> </code>.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>service_name</td>
    <td>string</td>
    <td>registered name of the OIDC service, e.g. <code> auth.dns </code>, <code> ke</code> <code>ycloak.static</code></td>
    <td>-</td>
  </tr>
  <tr>
    <td>service_port</td>
    <td>int64</td>
    <td>service port of the OIDC service.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>service_host</td>
    <td>string</td>
    <td>host of the OIDC service when type is static ip.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>match_type</td>
    <td>string</td>
    <td>match type (<code> whitelist </code> or <code> bl</code> <code>acklist </code>).</td>
    <td><code>"whitelist"</code></td>
  </tr>
  <tr>
    <td>match_list</td>
    <td>rule|list</td>
    <td>a list of (match_rule_domain, match_rule_path, and match_rule_type).</td>
    <td>-</td>
  </tr>
  <tr>
    <td>match_rule_domain</td>
    <td>string</td>
    <td>match rule domain, support wildcard pattern such as <code> *.bar.com </code>.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>match_rule_path</td>
    <td>string</td>
    <td>match rule path such as <code> /headers </code>.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>match_rule_type</td>
    <td>string</td>
    <td>match rule type can be <code> exact </code> or <code> pref</code> <code>ix </code> or <code> regex </code>.</td>
    <td>-</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/75f26cad32bb41f13a24aadd52a2e8ca.png)

**Usage**

**Generate a cookie secret**

```text
python -c 'import os,base64; 
print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
```

Reference: Oauth2-proxy: Generating a Cookie Secret.

**Blacklist and whitelist modes**

The whitelist or blacklist mode is supported. The whitelist mode is used by default. If the whitelist is empty, all requests must be authenticated. Domain name matching supports wildcards, such as  `*.bar.com` . The matching rules support  `exact`  (exact match),  `prefix`  (prefix match), and  `regex`  (regular expression match).

- **Whitelist mode**

  ```text
  match_type: 'whitelist'
  match_list:
   - match_rule_domain: '*.bar.com'
   match_rule_path: '/foo'
   match_rule_type: 'prefix'
  ```

No authentication is required for requests that use the wildcard domain name  `*.bar.com` with a prefix match of  `/foo` .

- **Blacklist mode**

  ```text
  match_type: 'blacklist'
  match_list:
   - match_rule_domain: '*.bar.com'
   match_rule_path: '/headers'
   match_rule_type: 'prefix'
  ```

Authentication is required only for requests that use the wildcard domain name  `*.bar.com` with a prefix match of  `/header` .

**Log out a user**

When a user performs a logout operation, the application redirects the user to the  `/oauth2/sign_out`  endpoint. This endpoint removes only the cookies set by oauth2-proxy. This indicates that the user remains logged in at the OIDC Provider and may automatically log back in if the user accesses the application again. Therefore, the  `rd`  query parameter must be used to redirect the user to the logout page of the authentication provider. The logout page uses a URL similar to the following one (note that the value of the rd parameter must be URL-encoded):

```text
/oauth2/sign_out?rd=https%3A%2F%2Fmy-oidc-
provider.example.com%2Fsign_out_page
```

Alternatively, you can include the redirect URL in the  `X-Auth-Request-Redirect`  header:

```http
GET /oauth2/sign_out HTTP/1.1
X-Auth-Request-Redirect: https://my-oidc-provider.example.com/sign_out_page
...
```

The redirect URL may include the  `post_logout_redirect_uri`  parameter, which specifies the page to which the user will be redirected after logging out from the OIDC Provider, such as the logout page of a backend service. If this parameter is not included, the user will be redirected to the logout page of the OIDC Provider by default. For more information, see the following examples of auth0 and keycloak.

> **Note**
>
> If the OIDC Provider supports session management and discovery, the sign_out_page should be the  `end_session_endpoint`  obtained from the metadata.

**HTTPS for OIDC**

If the OIDC provider uses HTTPS, see the description of Configure Backend Service Protocol: HTTPS in Higress. You need to use the annotation  `higress.io/backend-protocol: "HTTPS"`  to configure the HTTP protocol for forwarding requests to the backend service. For more information, see the Ingress configuration in the Auth0 example.

**Configuration examples**

**Auth0 configuration example**

**Procedure**

**Step 1: Configure the Auth0 account**

- Log in to the Okta Developer website Developer Auth0 site.

- Register a test web application.

> **Important**
>
> You must configure settings, such as Allowed Callback URLs, Allowed Logout URLs, and Allowed Web Origins. Otherwise, the OIDC Provider considers the redirect URL for login or the logout URL as invalid.

**Step 2: Configure a service source in the cloud-native gateway**

Create an auth0 DNS service source in the cloud-native gateway.

**Step 3: Configure HTTPS for OIDC**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 name: auth0-ingress
 annotations:
 higress.io/destination: auth.dns
 higress.io/backend-protocol: "HTTPS"
 higress.io/ignore-path-case: "false"
spec:
 ingressClassName: higress
 rules:
 - host: foo.bar.com
 http:
 paths:
 - path: /
 pathType: Prefix
 backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
```

**Step 4: Configure the Wasm plug-in**

```text
redirect_url: 'http://foo.bar.com/oauth2/callback'
oidc_issuer_url: 'https://dev-o43xb1mz7ya7ach4.us.auth0.com/'
client_id: 'XXXXXXXXXXXXXXXX'
client_secret: 'XXXXXXXXXXXXXXXX'
scope: 'openid email offline_access'
cookie_secret: 'nqav************_8DCfY='
service_name: 'auth.dns'
service_port: 443
match_type: 'whitelist'
match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/foo'
 match_rule_type: 'prefix'
```

> **Important**
>
> You must configure the service source first. The Wasm plug-in needs to access the configured service to obtain the openid-configuration during initialization.

**Test the results**

**If the login fails when you access the service page, you are redirected to another page.**

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/530cc02330c3ff320baa48418e22ec0f.jpeg)

**The service page appears if the login succeeds.**

The _oauth2_proxy cookie is included in the headers for subsequent login requests. The Authorization header carries the ID token, which is used by the backend service to obtain user information.

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/4480e14644db87e1735adf6c3c407f81.jpeg)

**You are redirected to the logout page upon logout.**

```text
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdev-
o43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout
```

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/e4e00ba4a7beef70172a1567372fb496.jpeg)

**You are redirected to the logout page upon logout (the post_logout_redirect_uri parameter is included to specify the destination URI).**

```text
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdev-
```

```text
o43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout%3Fpost_logout_redirect_uri%3Dhttp%
```

```text
A%2F%2Ffoo.bar.com%2Ffoo
```

> **Important**
>
> The URI specified in post_logout_redirect_uri must be pre-configured in the Allowed URLs of the OIDC Provider to enable successful redirection.

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/29a48ebbe8411f753dcd2c740265f441.jpeg)

**Keycloak configuration example**

**Procedure**

**Step 1: Get started with keycloak on docker**

https://www.keycloak.org/getting-started/getting-started-docker

> **Important**
>
> You must configure settings, such as Valid redirect URIs, Valid post logout URIs, and Web origins. Otherwise, the OIDC Provider considers the redirect URL for login or the logout URL as invalid.

**Step 2: Configure a service source in the cloud-native gateway**

Create a Keycloak fixed-address source service in the cloud-native gateway.

**Step 3: Configure the Wasm plug-in**

```text
redirect_url: 'http://foo.bar.com/oauth2/callback'
oidc_issuer_url: 'http://127.0.0.1:9090/realms/myrealm'
client_id: 'XXXXXXXXXXXXXXXX'
client_secret: 'XXXXXXXXXXXXXXXX'
scope: 'openid email'
cookie_secret: 'nqavJrGvRmQxWwGNptLdyUVKcBNZ2b18Guc1n_8DCfY='
service_name: 'keycloak.static'
service_port: 80
service_host: '127.0.0.1:9090'
match_type: 'blacklist'
match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/headers'
 match_rule_type: 'prefix'
```

**Test the results**

**If the login fails when you access the service page, you are redirected to another page.**

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c99d97874762a67377b420216c2998d6.jpeg)

**The service page appears if the login succeeds.**

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/4480e14644db87e1735adf6c3c407f81.jpeg)

**You are redirected to the logout page upon logout.**

```text
http://foo.bar.com/oauth2/sign_out?
rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenid-
connect%2Flogout
```

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/5d7487438625a8e4ba41fa2aa3c94123.jpeg)

**You are redirected to the logout page upon logout (the post_logout_redirect_uri parameter is included to specify the destination URI).**

```text
http://foo.bar.com/oauth2/sign_out?
rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenid-
connect%2Flogout%3Fpost_logout_redirect_uri%3Dhttp%3A%2F%2Ffoo.bar.com%2Ffoo
```

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/29a48ebbe8411f753dcd2c740265f441.jpeg)

**OIDC process**

oidc_process

**OIDC process parsing**

**User not logged in**

1. Simulate a user to access the corresponding service API.

   ```bash
   curl --url "foo.bar.com/headers"
   ```

2. The cloud-native gateway redirects the user to the login page of the OIDC Provider, carries OIDC authentication parameters such as client_id, response_type, and scope, and sets a CSRF cookie to defend against CSRF attacks.

   ```bash
   curl --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/authorize"\
    --url-query "approval_prompt=force" \
    --url-query "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
    --url-query "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
    --url-query "response_type=code" \
    --url-query "scope=openid+email+offline_access" \
    --url-query "state=nT06************_hCjskrH_VupPqdcdw%3A%2Ffoo" \
    --header "Set-Cookie: 
   ```

   ```text
   _oauth2_proxy_csrf=LPruATEDgcdmelr8zScD_ObhsbP4zSzvcgmPlcNDcJpFJ0OvhxP2hFotsU-
   ```

   ```text
   kZnYxd5KsIjzeIXGTOjf8TKcbTHbDIt-
   ```

   ```text
   aQoZORXI_0id3qeY0Jt78223DPeJ1xBqa8VO0UiEOUFOR53FGxirJOdKFxaAvxDFb1Ok=|17189624
   ```

   ```text
   5|V1QGWyjQ4hMNOQ4Jtf17HeQJdVqHdt5d65uraFduMIU=; Path=/; Expires=Fri, 21 Jun 
   2024 08:06:20 GMT; HttpOnly"
   ```

3. The user is redirected to the login page.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/0ada5e251f0b48f864bb01e372f35f60.jpeg)

4. The user enters the username and password to complete the login.

5. The user is redirected to the cloud-native gateway. The redirection URL carries an authorization code and the state parameter. The authorization code is used to exchange tokens. The state parameter is used to verify the CSRF cookie.

   ```bash
   curl --url "http://foo.bar.com/oauth2/callback" \
    --url-query "state=nT06xdCqn4IqemzBRV5hmO73U_hCjskrH_VupPqdcdw%3A%2Ffoo" \
    --url-query "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm"
   ```

6. The state value encrypted and stored in the CSRF cookie must match the state value in the URL parameter.

7. The gateway uses the authorization code to exchange an id_token and an access_token.

   ```bash
   curl -X POST \
    --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
    --data "grant_type=authorization_code" \
    --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
    --data 
   ```

   ```text
   "client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ
   ```

   ```text
   " \
    --data "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
    --data "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm" \
   ```

   The response contains the id_token, access_token, and refresh_token. The refresh_token is used for subsequent token refreshes.

   ```json
   {
    "access_token": "eyJh************..WP_WRVM-
   ```

   ```text
   y3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o
   ```

   ```text
   xrOOJIzXTgsfFVA2x15g-
   jBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EP-
   omFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs-
   344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP-
   ```

   ```text
   KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh
   ```

   ```text
   BFNX6A.mgGGeeWgugfXcUcsX4T5dQ",
    "refresh_token": "GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG",
    "id_token": 
   "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imc1Z1ExSF9ZbTY0WUlvVkQwSVpXTCJ9
   ```

   ```text
   yJlbWFpbCI6IjE2MDExNTYyNjhAcXEuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJpc3MiOiJ
   dHRwczovL2Rldi1vNDN4YjFtejd5YTdhY2g0LnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJZYWdGcVJEOX
   mTklhYWM1QmFtamhzU2F0anJBbnNuWiIsImlhdCI6MTcxOTE5ODYzOCwiZXhwIjoxNzE5MjM0NjM4L
   JzdWIiOiJhdXRoMHw2NjVkNzFlNzRjMTMxMTc3YmU2NmU2MDciLCJzaWQiOiJjdDJVOF9ZUS16VDdF
   GkwRTNNeUstejc5ZGlWUWhhVSJ9.gfzXKJ0FeqzYqOUDLQHWcUG19IOLqkpLN09xTmIat0umrlGV5V
   ```

   ```text
   SumgWH3XJmmwnhdb8AThH3Jf-7kbRJzu4rM-
   BbGbFTRBTzNHeUajFOFrIgld5VENQ_M_sXHkTp0psWKSr9vF24kmilCfSbvC5lBKjt878ljZ7-xteWuaUYOMUdcJb4DSv0-zjX01sonJxYamTlhji3M4TAW7VwhwqyZt8dBhVSNaRw1wUKj-
   ```

   ```text
   M1JrBDLyx65sroZtSqVA0udIrqMHEbWYb2de7JjzlqG003HRMzwOm7OXgEd5ZVFqgmBLosgixOU5DJ
   ```

   ```text
   A26nlqK92Sp6VqDMRvA-3ym8W_m-wJ_A",
    "scope": "openid email offline_access",
    "expires_in": 86400,
    "token_type": "Bearer"
   }
   ```

8. The obtained id_token, access_token, and refresh_token are encrypted and stored in the _oauth2_proxy cookie.

9. The gateway redirects the user to the backend service, sets a cookie for subsequent verification of the user's login status, and clears the _oauth2_proxy_csrf cookie.

   ```text
   "Set-Cookie": [
    "_oauth2_proxy_csrf=; Path=/; Expires=Mon, 24 Jun 2024 02:17:39 GMT; 
   HttpOnly",
    "_oauth2_proxy=8zM_Pcfpp_gesKFe4SMg08o5Iv0A8WAOQOmG1-vZBbQ56UggYVC0Cu-
   gFMEoxJZU5q1O5vqRlVBizlLetgVjRCksGVbttwl8tQ7h5YiyIubbbtvF1T4JzLh3QfzUUrwbB-
   ```

   ```text
   VznOkh8qLbjAhddocecjBt4rMiDyceKXqMr4eO5TUEMx4vHtJYnTYalMeTYhGXk5MNSyrdZX9NnQnk
   ```

   ```text
   rCjiOQM13ggwob2nYwhGWaAlgzFSWkgkdtBy2Cl_YMWZ8_gKk9rDX289-
   JrJyGpr5k9O9RzRhZoY2iE3Mcr8-Q37RTji1Ga22QO-
   ```

   ```text
   XkAcSaGqY1Qo7jLdmgZTYKC5JvtdLc4rj3vcbveYxU7R3Pt2vEribQjKTh4Sqb0aA03p4cxXyZN4SU
   BW1NAOm4JLPUhKJy8frqC9_E0nVqPvpvnacaoQs8WkX2zp75xHoMa3SD6KZhQ5JUiPEiNkOaUsyafL
   ```

   ```text
   ht6lLkNDhgzW3BP2czoe0DCDBLnsot0jH-qQpMZYkaGr-
   ZnRKI1OPl1vHls3mao5juOAW1VB2A9aughgc8SJ55IFZpMfFMdHdTDdMqPODkItX2PK44GX-
   pHeLxkOqrzp3GHtMInpL5QIQlTuux3erm3CG-
   ntlUE7JBtN2T9LEb8XfIFu58X9_vzMun4JQlje2Thi9_taI_z1DSaTtvNNb54wJfSPwYCCl4OsH-
   BacVmPQhH6TTZ6gP2Qsm5TR2o1U2D9fuVkSM-
   ```

   ```text
   OPCG9l3tILambIQwC3vofMW6X8SIFSmhJUDvN7NbwxowBiZ6Y7GJRZlAk_GKDkpsdrdIvC67QqczZF
   ```

   ```text
   hRVnm6qi-
   gPO41APCbcO6fgTwyOhbP3RrZZKWSIqWJYhNE3_Sfkf0565H7sC7Hc8XUUjJvP3WnjKS9x7KwzWa-
   dsUjV3-Q-VNl-rXTguVNAIirYK-
   ```

   ```text
   qrMNMZGCRcJqcLnUF0V_J2lVmFyVsSlE3t0sDw2xmbkOwDptXFOjQL5Rb4esUMYdCBWFajBfvUtcZE
   tYhD0kb6VcbjXO3NCVW5qKh_l9C9SRCc7TG1vcRAqUQlRXHacTGWfcWsuQkCJ3Mp_oWaDxs1GRDykQ
   ```

   ```text
   xAn5sTICovThWEU2C6o75grWaNrkj5NU-
   0eHh3ryvxLmGLBOXZV9OQhtKShWmUgywSWMxOHOuZAqdAPULc8KheuGFjXYp-
   ```

   ```text
   RnCbFYWePJmwzfQw89kSkj1KUZgMYwKEjSz62z2qc9KLczomv76ortQzvo4Hv9kaW6xVuQj5R5Oq6_
   ```

   ```text
   MBOqsmUMzcXpxCIOGjcdcZRBc0Fm09Uy9oV1PRqvAE4PGtfyrCaoqILBix8UIww63B07YGwzQ-h
   AXDysBK-
   ```

   ```text
   Vca2x7GmGdXsNXXcTgu00bdsjtHZPDBBWGfL3g_rMAXr2vWyvK4CwNjcaPAmrlF3geHPwbIePT0hsk
   ```

   ```text
   boX1v1bsuhzsai7rGM4r53pnb1ZEoTQDa1B-
   ```

   ```text
   HyokFgo14XiwME0zE1ifpNzefjpkz1YY2krJlqfCydNwoKaTit4tD2yHlnxAeFF9iIrxzSKErNUFpm
   ```

   ```text
   La7ge7V33vhEH-6k5oBTLE2Q2BrC6aAkLCcPwU9xv_SzBDQPRY0MEYv3kGF03Swo1crRbGh-
   ```

   ```text
   aifYX9NiHDsmG6r1vAnx0MAOw2Jzuz2x6SSdfBrzlcoWBlrwiZzd9kAKq75n1Uy9uzZ8SRnkBrEZyS
   ```

   ```text
   BwEbu196VklkRE0jqwC-e3wWNNuviSOfwkVeX-
   7QdOoO10yw9VK2sW52lFvIEf4chv_ta7bGfAZOWBjpktG6ZLD81SE6A88zpqG2SysSyNMp9hl-umG-5sFsjCn_c9E8bDvwkUOUVb9bNqhBDsZgR0BNPawiOZjmyfhzmwmWf-
   ```

   ```text
   zgFzfFSV6BvOwNRi3sCOHTsWcuk9NBQ_YK8CpNkVl3WeIBSDfidimuC_QV9UWKs1GPk35ZRkM4zKtL
   ```

   ```text
   2JsBFWKaDy_P80TcOzcMBoP8gIBClXZ-WUqfE8s1yyc4jrq-
   qL1_wJ24ef1O9FktsbyZiDKXw2vnqsT8-g_hCeG-unrT1ZFscf8oNdqczARHX-
   K4vKH2k3uIqEx1M=|1719199056|2rsgdUIClHNEpxBLlHOVRYup6e4oKensQfljtmn4B80=; Path=/; Expires=Mon, 01 Jul 2024 03:17:36 GMT; HttpOnly"
   ]
   ```

0. The gateway checks whether a cookie that stores the user's token exists and whether the token is valid.

1. The user uses a request that carries an Authorization header to access the corresponding API. The Authorization header contains the user's access_token.

   ```bash
   curl --url "foo.bar.com/headers"
    --header "Authorization: Bearer 
   ```

   ```text
   eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtbzQzeGIxbXo3eW
   ```

   ```text
   3YWNoNC51cy5hdXRoMC5jb20vIn0..WP_WRVM-
   ```

   ```text
   y3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o
   ```

   ```text
   xrOOJIzXTgsfFVA2x15g-
   jBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EP-
   omFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs-
   344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP-
   ```

   ```text
   KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh
   ```

   ```text
   BFNX6A.mgGGeeWgugfXcUcsX4T5dQ"
   ```

2. The backend service obtains the user authorization information based on the access_token and returns an HTTP response.

   ```json
   {
    "email": "******",
    "email_verified": false,
    "iss": "https://dev-o43xb1mz7ya7ach4.us.auth0.com/",
    "aud": "YagFqRD9tfNIaac5BamjhsSatjrAnsnZ",
    "iat": 1719198638,
    "exp": 1719234638,
    "sub": "auth0|665d71e74c131177be66e607",
    "sid": "ct2U8_YQ-zT7E8i0E3MyK-z79diVQhaU"
   }
   ```

**User token refresh**

1. Simulate a user to access the corresponding service API.

   ```bash
   curl --url "foo.bar.com/headers"
   ```

2. The gateway checks the expiration time of the token.

3. If a refresh_token is detected in the cookie, the corresponding API can be accessed to exchange a new id_token and access_token.

   ```bash
   curl -X POST \
    --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
    --data "grant_type=refresh_token" \
    --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
    --data 
   ```

   ```text
   "client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ
   ```

   ```text
   " \
    --data "refresh_token=GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG"
   ```

4. The user uses a request that carries an Authorization header to access the corresponding API. The Authorization header contains the user's access_token.

5. The backend service obtains the user authorization information based on the access_token and returns an HTTP response.

<a id="section-3-6-3-5"></a>

#### 3.6.3.5. hmac-auth

The hmac-auth plug-in is used to generate unforgeable signatures for HTTP requests based on the hash-based message authentication code (HMAC) algorithm. The signatures are used for identity authentication. This topic describes how to configure the hmac-auth plug-in.

**Plug-in type**

Authentication plug-in.

**Fields**

**Authentication configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| consumers | array of object | Yes | - | The callers of the service.This field is used to authenticate requests. |
| date_offset | number | No | - | The maximum time offset of the client in seconds. The system uses this field to parse the Universal Time Coordinated (UTC) time of the client from the <code> Date </code> header of the request to prevent replay attacks. If this field is not configured, the system does not verify the UTC time of the client. |
| global_auth | array of string | No (Required only for instance-level configurations) | - | This field can be configured only at the instance level.<br>• If this field is set to true, the authentication mechanism globally takes effect.<br>• If this field is set to false, the authentication mechanism takes effect only for the configured domain names and routes.<br>• If this field is not configured, the authentication mechanism globally takes effect only when no domain names and routes are configured.This is in consideration of the usage habits of existing users. |

The following table describes the fields in  `consumers` .

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| key | string | Yes | - | The access key of the consumer. |
| secret | string | Yes | - | The secret that is used to generate the signature. |
| name | string | Yes | - | The name of the consumer. |

**(Optional) Authorization configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| allow | array of string | No (Required for non-instance-level configurations) | - | You can only configure this field at a fine granularity such as route or domain name. For requests that meet the matching conditions, you can configure consumers that are allowed for access. This implements fine-grained permission control. |

> **Important**
>
> - The authorization configuration and authentication configuration cannot coexist in a rule.
>
> - For authenticated requests, the  `X-Mse-Consumer`  field is added to the request header to identify the names of the callers.

**Configuration examples**

**Configure global authentication and route-level authorization**

This section provides an example on how to enable authentication based on the hmac-auth plug-in for specific routes or domain names of the gateway.

> **Important**
>
> The  `key`  field must be unique.

Apply the following plug-in configurations at the instance level:

```text
global_auth: false
consumers: 
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

Apply the following plug-in configuration to the  `route-a`  and  `route-b`  routes:

```text
allow:
- consumer1
```

Apply the following plug-in configuration to the  `*.example.com`  and  `test.com`  domain names:

```text
allow:
- consumer2
```

> **Note**
>
> - In this example, the  `route-a`  and  `route-b`  routes are those specified when the gateway routes are created. If a client request matches one of the routes, the caller whose  `name`  is  `consumer1`  is allowed to access the gateway. Other callers are not allowed to access the gateway.
>
> - In this example, the  `*.example.com`  and  `test.com`  domain names are used to match domain names in requests. If a client request matches one of the domain names, the caller whose  `name`  is  `consumer2`  is allowed to access the gateway. Other callers are not allowed to access the gateway.

**Enable authentication for gateways**

```text
global_auth: true
consumers: 
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

**Signature mechanism**

**Configuration preparations**

You must configure the following credential settings that are required for generating and verifying signatures.

- key: used in the request header  `x-ca-key` .

- secret: used to generate the request signature.

**Generate a signature on the client**

**Process**

To generate a signature, a client must perform the following steps:

1. Extracts the key data from the original request and generates a signature string.

2. Uses the encryption algorithm and the configured  `secret`  to encrypt the signature string and generate a signature.

3. Adds all headers that are related to the signature to the original HTTP request to obtain the final HTTP request.

**Extract a signature string**

To generate a signature, the client needs to extract key data from the HTTP request and combine the key data into a signature string. The signature string is in the following format:

```text
HTTPMethod
Accept
Content-MD5
Content-Type
Date
Headers
PathAndParameters
```

The preceding fields constitute a signature string and are separated by \\n. If you leave the Headers field empty, \\n is not required. If you leave other fields empty, \\n must be retained. The signature is case-sensitive.

Rules for extracting each field:

- HTTPMethod: the HTTP method used to send a request, such as POST. The value of this field is in uppercase.

- Accept: the value of the Accept header in the request. You can leave the Accept header empty. We recommend that you explicitly specify the Accept header in the request. If the Accept header is empty, some HTTP clients use the default value  `*/*`  for Accept. As a result, the signature verification fails.

- Content-MD5: the value of the Content-MD5 header, which can be left empty. The value is calculated only when a request contains a body of a non-Form type. The following example is used to calculate the value of the Content-MD5 header in the Java format:

  ```text
  String content-MD5 = Base64.encodeBase64(MD5(bodyStream.getbytes("UTF-8")));
  ```

- Content-Type: the value of the Content-Type header, which can be left empty.

- Date: the value of the Date header, which is used for time offset verification. You can leave this field empty if  `date_offset`  is not specified.

- Headers: You can specify the headers to calculate a signature. When you concatenate signature strings, the following rules apply:

  - Header keys are first sorted in alphabetical order and then concatenated based on the following rules:

    ```text
    HeaderKey1 + ":" + HeaderValue1 + "\n"\+
    HeaderKey2 + ":" + HeaderValue2 + "\n"\+
    ...
    HeaderKeyN + ":" + HeaderValueN + "\n"
    ```

  - If the value of a header is empty, use HeaderKey + ":" + "\\n" for the signature. You must retain the header key and colon (:).

  - The header keys that are used for the signature are separated by commas (,) and placed in the header whose key is  `X-Ca-Signature-Headers` .

  - You cannot use the following headers to calculate a signature: X-Ca-Signature, X-Ca-Signature-Headers, Accept, Content-MD5, Content-Type, and Date.

- The PathAndParameters field contains all the path, query, and form parameters.

  ```text
  Path + "?" + Key1 + "=" + Value1 + "&" + Key2 + "=" + Value2 + ... "&" + KeyN + "=" 
  + ValueN
  ```

> **Note**
>
> - Keys of query and form parameters are first sorted in alphabetical order and then concatenated by using the preceding method.
>
> - If the query and form parameters are left empty, you can use path parameters without the need to add signature information.
>
> - If some query and form parameters are array parameters with the same key but different values, the first value is used for signature calculation.

**Example of extracting a signature string**

Initial HTTP request:

```http
POST /http2test/test?param1=test HTTP/1.1
host:api.aliyun.com
accept:application/json; charset=utf-8
ca_version:1
content-type:application/x-www-form-urlencoded; charset=utf-8
x-ca-timestamp:1525872629832
date:Wed, 09 May 2018 13:30:29 GMT+00:00
user-agent:ALIYUN-ANDROID-DEMO
x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44
content-length:33
username=xiaoming&password=123456789
```

Generated signature string:

```text
POST
application/json; charset=utf-8
application/x-www-form-urlencoded; charset=utf-8
Wed, 09 May 2018 13:30:29 GMT+00:00
x-ca-key:203753385
x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44
x-ca-signature-method:HmacSHA256
x-ca-timestamp:1525872629832
/http2test/test?param1=test&password=123456789&username=xiaoming
```

**Calculate a signature**

After the client extracts the key data from the HTTP request and generates a signature string, the client needs to encrypt and encode the signature string to form the final signature.

In the encryption process,  `stringToSign`  specifies the extracted signature string,  `secret` is specified in the plug-in configuration, and  `sign`  specifies the final signature.

```text
Mac hmacSha256 = Mac.getInstance("HmacSHA256");
byte[] secretBytes = secret.getBytes("UTF-8");
hmacSha256.init(new SecretKeySpec(secretBytes, 0, secretBytes.length, "HmacSHA256"));
byte[] result = hmacSha256.doFinal(stringToSign.getBytes("UTF-8"));
String sign = Base64.encodeBase64String(result);
```

In summary,  `stringToSign`  is decoded into a byte array by using UTF-8. The byte array is encrypted by using an encryption algorithm and then encoded by using the Base64 algorithm to generate a signature.

**Add a signature**

The client must include the following headers in the requests sent to Cloud-native API Gateway for signature verification:

- x-ca-key: the AppKey, which is required.

- x-ca-signature-method: the signature algorithm, which is optional. Valid values: HmacSHA256 and HmacSHA1. Default value: HmacSHA256.

- x-ca-signature-headers: the collection of keys for all signature headers, which is optional. The keys are separated by commas (,).

- x-ca-signature: the signature, which is required.

The following example shows an HTTP request with a signature:

```http
POST /http2test/test?param1=test HTTP/1.1
host:api.aliyun.com
accept:application/json; charset=utf-8
ca_version:1
content-type:application/x-www-form-urlencoded; charset=utf-8
x-ca-timestamp:1525872629832
date:Wed, 09 May 2018 13:30:29 GMT+00:00
user-agent:ALIYUN-ANDROID-DEMO
x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44
x-ca-key:203753385
x-ca-signature-method:HmacSHA256
x-ca-signature-headers:x-ca-timestamp,x-ca-key,x-ca-nonce,x-ca-signature-method
x-ca-signature:xfX+bZxY2yl7EB/qdoDy9v/uscw3Nnj1pgoU+Bm6xdM=
content-length:33
username=xiaoming&password=123456789
```

**Verify the signature at the server side**

**Process**

To verify the signature received from the client, the server performs the following steps:

1. Extracts key data from the request to obtain a signature string.

2. Reads the  `key`  from the request and uses the  `key`  to obtain the  `secret` .

3. Uses an encryption algorithm and the  `secret`  to encrypt the signature string to obtain a signature.

4. Reads the client-side signature from the request and compares the server-side signature with the client-side signature.

**Troubleshoot signature errors**

If signature verification fails, the system adds the server-side signature string (StringToSign) to the header of the HTTP response that is returned to the client. The key is X-Ca-Error-Message. You can identify errors when you compare the client-side signature string (StringToSign) with the server-side signature string.

If the two values are the same, check the AppSecret that is used for signature calculation.

HTTP headers do not support line breaks. Line breaks in the signature string (StringToSign) are replaced with number signs ( `#` ).

```text
X-Ca-Error-Message:  Server StringToSign:`GET#application/json##application/json##X-Ca-
Key:200000#X-Ca-Timestamp:1589458000000#/app/v1/config/keys?keys=TEST`
```

**Error codes**

| HTTP status code | Error message | Reason |
| --- | --- | --- |
| 400 | Invalid Signature. | The x-ca-signature request header contains a signature that does not match the server-calculated signature. |
| 400 | Invalid Content-MD5. | The content-md5 request header is invalid. |
| 400 | Invalid Date. | The time offset calculated based on the date request header exceeds the configured date_offset. |
| 401 | Invalid Key. | The x-ca-key request header is not provided or is invalid. |
| 401 | Empty Signature. | The x-ca-signature request header does not contain a signature. |
| 403 | Unauthorized Consumer. | The caller of the request does not have access permissions. |
| 413 | Request Body Too Large. | The size of the request body exceeds 32 MB. |
| 413 | Payload Too Large. | The request body exceeds the value of DownstreamConnectionBufferLimits that is configured for the gateway. You can increase the value of DownstreamConnectionBufferLimits on the parameter configuration page. |

> **Note**
>
> Note: If you increase the value of  `DownstreamConnectionBufferLimits` , the gateway memory usage significantly increases. Exercise caution when you perform this operation.

<a id="section-3-6-3-6"></a>

#### 3.6.3.6. ext-auth

The ext-auth plug-in implements the feature of sending an authentication request to an external authorization service to check whether a client request is authorized. This topic describes how to configure the ext-auth plug-in.

**Running attributes**

Plug-in execution stage: Authentication. Plug-in execution priority:  `360`

**Fields**

| Field | Data type | Req uire d | Defau lt value | Description |
| --- | --- | --- | --- | --- |
| <code>http_service</code> | object | Yes | - | The configuration of the external authorization service. |
| <code>match_type</code> | string | No |  | Valid values: <code> whitelist </code> and <code> blacklist </code>. |
| <code>match_list</code> | array of MatchRule | No |  | A list that contains <code> match_rule_domain </code>, <code> match_rule_path </code>, and <code> match_rule_type </code>. |
| <code>failure_mode_</code><br><code>allow</code> | bool | No | false | When this field is set to true, client requests are accepted even if the communication with the authorization service fails or if the authorization service returns an HTTP 5xx error. |
| <code>failure_mode_</code><br><code>allow_header_ad</code><br><code>d</code> | bool | No | false | When both <code> failure_mode_allow </code> and <code> failure_mode_allow_header_add </code> are set to true, if the communication with the authorization service fails or the authorization service returns an HTTP 5xx error, <code> x-envoy-</code><code>auth-failure-mode-allowed: true </code> is added to the request header. |
| <code>status_on_err</code><br><code>or</code> | int | No | 403 | The HTTP status code returned to the client when the authorization service is unreachable or returns a 5xx status code. The default status code is <code> 403 </code>. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/6da68d948aedfc34f928b2435dd8ffb3.png)

The following table describes the configuration fields in  `http_service` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>endpoint_mode</code> | string | No | envoy | Valid values: <code> envoy </code> and <code>forward_auth</code><code> </code>. |
| <code>endpoint</code> | object | Yes | - | The information about the HTTP service that sends an authentication request. |
| <code>timeout</code> | int | No | 1000 | The connection timeout of the <code>ext-auth</code> service. Unit: milliseconds. |
| <code>authorization_</code><br><code>request</code> | object | No | - | The configuration of an authentication request. |
| <code>authorization_</code><br><code>response</code> | object | No | - | The configuration of the authentication response. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/2d152100fbaeb2441a8e9604dd9a48b0.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/3d4bfbdde7ce1d8068ac126149e06689.png)

The following table describes the configuration fields in  `endpoint` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>service_name</code> | string | Yes | - | Enter the name of the authorization service as a fully qualified domain name (FQDN) including the service type, such as <code> ext-</code><code>auth.dns </code> and <code>ext-auth.my-</code><br><code>ns.svc.cluster.</code><code>local </code>. |
| <code>service_port</code> | int | No | 80 | The service port of the authorization service. |
| <code>service_host</code> | string | No | - | The Host header that is set when the authorization service is requested. If this field is not set, the value is the same as the FQDN. |
| <code>path_prefix</code> | string | This field is required when the <code>endpoint_mode</code> <code> </code> field is set to <code> envoy </code>. | - | The request path prefix used by the client to send requests to the authorization service when the <code>endpoint_mode</code> <code> </code> field is set to <code> envoy </code>. |
| <code>request_method</code> | string | No | GET | The HTTP method used by the client to send requests to the authorization service when the <code>endpoint_mode</code> <code> </code> field is set to <code>forward_auth</code><code> </code>. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/395959f8024e6c5bd8bfa6ac2e16e740.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/d24acf39deed8d0d2a136d53e6507ba6.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/b16de38fc109ce025ccd5fcd7f4b94fb.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/4a3fc5c5cc80c6c543455bdf5069874a.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/bd538db5f7f7ab05c1a10b9336b67d41.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/585bc6295543917dfb0f5fb19e5a4dcd.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/02faedf952150b46fdd88ddc4620e031.png)

<table>
  <tr>
    <td><code>path</code></td>
    <td>string</td>
    <td>This field is required when the <code>endpoint_mode</code> <code> </code> field is set to <code>forward_auth</code><code> </code>.</td>
    <td>-</td>
    <td>The request path used by the client to send requests to the authorization service when the <code>endpoint_mode</code> <code> </code> field is set to <code>forward_auth</code><code> </code>.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/74e23a24eadcf3495aa0abd8173c5b0e.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/fa0b244f79493053065498951cff17a0.png)

The following table describes the configuration fields in  `authorization_request` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>allowed_header</code><br><code>s</code> | array of StringMatcher | No | - | When this field is configured, request headers that match the specified criteria are added to the authorization service request.In addition to user-defined header matching rules, the authorization service request automatically includes the <code>Authorization</code> <code> </code> HTTP header. If the <code>endpoint_mode</code> <code> </code> field is set to <code>forward_auth</code><code> </code>, <code> X-</code><code>Forwarded-*</code> request headers are automatically added. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1233572442de424dd27db2a6b4e6dfb8.png)

<table>
  <tr>
    <td><code>headers_to_add</code></td>
    <td>map[string]string</td>
    <td>No</td>
    <td>-</td>
    <td>A list of request headers that will be included in the authorization service request.<br><img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/9d4239d2d9ef4e48d99dec2ebce4166e.png" width="14" alt=""><br>Important<br>Client request headers with the same name will be overwritten.</td>
  </tr>
  <tr>
    <td><code>with_request_b</code><br><code>ody</code></td>
    <td>bool</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to buffer the client request body and include it in the authentication request (disabled for HTTP methods GET, OPTIONS, and HEAD).</td>
  </tr>
  <tr>
    <td><code>max_request_bo</code><br><code>dy_bytes</code></td>
    <td>int</td>
    <td>No</td>
    <td>10MB</td>
    <td>The maximum size of the client request body that can be buffered in memory. When the client request body reaches this limit, an HTTP 413 status code is returned and the authorization process is not initiated.<br><img src="en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/9d4239d2d9ef4e48d99dec2ebce4166e.png" width="14" alt=""><br>Important<br>This setting takes precedence over the <code>failure_m</code><br><code>ode_allow</code> configuratio n.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/681b4718c311f0fdbe64b11b13d295c6.png)

The following table describes the configuration fields in  `authorization_response` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>allowed_upstre</code><br><code>am_headers</code> | array of StringMatcher | No | - | Response headers from the authorization service that match the specified criteria will be added to the original client request headers.Note that request headers with duplicate names will overwrite existing ones. |
| <code>allowed_client</code><br><code>_headers</code> | array of StringMatcher | No | - | If this field is not set, all response headers from the authorization service are included in the client response when the request is denied. If this field is set, only the response headers matching the specified criteria are included in the client response upon denial. |

The following table describes the configuration fields of the  `StringMatcher`  type. The system configures the StringMatcher elements in the order they are defined in the array when a field of the  `array of StringMatcher`  type is used.

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>exact</code> | string | No. One of <code> exact </code>, <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code> must be specified. | - | Exact match. |
| <code>prefix</code> | string | No. One of <code> exact </code>, <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code> must be specified. | - | Prefix match. |
| <code>suffix</code> | string | No. One of <code> exact </code>, <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code> must be specified. | - | Suffix match. |
| <code>contains</code> | string | No. One of <code> exact </code>, <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code> must be specified. | - | Substring containment check. |
| <code>regex</code> | string | No. One of <code> exact </code>, <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code> must be specified. | - | Regular expression match. |

The following table describes the configuration fields of the MatchRule type. The system configures the MatchRule elements in the order they are defined in the array when a field of the  `array of MatchRule`  type is used.

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>match_rule_dom</code><br><code>ain</code> | string | No | - | The domain name that meets the matching rule. Wildcard patterns are supported, such as <code> *.bar.com </code>. |
| <code>match_rule_met</code><br><code>hod</code> | \[\]string | No | - | Matches requests based on request methods. |
| <code>match_rule_pat</code><br><code>h</code> | string | No | - | The rule that matches the request path. |
| <code>match_rule_typ</code><br><code>e</code> | string | No | - | The type of the rule used to match the request path.Valid values: <code> exact </code> <code> prefix </code>, <code> suffix </code>, <code> contains </code>, and <code> regex </code>. |

**Differences between the two endpoint_mode options**

If the  `endpoint_mode`  field is set to  `envoy` , the authentication request preserves the HTTP method of the original request and constructs the request path by prepending the configured  `path_prefix`  to the original request path.

If the  `endpoint_mode`  field is set to  `forward_auth` , the authentication request uses the configured  `request_method`  as its HTTP method and the configured  `path`  as its request path. In addition, Higress automatically generates and forwards the following headers to the authentication service.

| Header | Description |
| --- | --- |
| <code>x-forwarded-proto</code> | The scheme of the original request, such as HTTP or HTTPS. |
| <code>x-forwarded-method</code> | The method of the original request, such as GET, POST, DELETE, and PATCH. |
| <code>x-forwarded-host</code> | The host of the original request. |
| <code>x-forwarded-uri</code> | The path of the original request, including path parameters, such as <code> /v1/app?test=true </code>. |

**Blacklist and whitelist modes**

The whitelist or blacklist mode is supported. The whitelist mode is used by default. If the whitelist is empty, all requests must be authenticated. Domain matching supports wildcards, such as  `*.bar.com` . The matching rules support  `exact` ,  `prefix` ,  `suffix` ,  `contains` , and  `regex` .

**Whitelist mode**

```text
# The whitelist mode is used. Requests that match any whitelist rule do not need to be authenticated.
match_type: 'whitelist'
match_list:
 # No authentication is required for requests that use api.example.com as thedomain name and the path prefix /public.
 - match_rule_domain: 'api.example.com'
 match_rule_path: '/public'
 match_rule_type: 'prefix'
 # All GET requests to the image resource server images.example.com do not need to be authenticated.
 - match_rule_domain: 'images.example.com'
 match_rule_method: ["GET"]
 # For all domain names, HEAD requests whose paths exactly match /health-check do not need to be authenticated.
 - match_rule_method: ["HEAD"]
 match_rule_path: '/health-check'
 match_rule_type: 'exact'
```

**Blacklist mode**

```text
# The blacklist mode is used. Requests that match any blacklist rule must be authenticated.
match_type: 'blacklist'
match_list:
 # Authentication is required for requests that use admin.example.com as the domain name and the path prefix /sensitive.
 - match_rule_domain: 'admin.example.com'
 match_rule_path: '/sensitive'
 match_rule_type: 'prefix'
 # For all domain names, DELETE requests whose paths exactly match /user must 
be authenticated.
 - match_rule_method: ["DELETE"]
 match_rule_path: '/user'
 match_rule_type: 'exact'
 # All POST requests that use legacy.example.com as the domain name must be authenticated.
 - match_rule_domain: 'legacy.example.com'
 match_rule_method: ["POST"]
```

**Configuration examples**

The following examples assume that the serviceName of the  `ext-auth`  service in Kubernetes is  `ext-auth` , port is  `8090` , path is  `/auth` , and namespace is  `backend` .

**When the endpoint_mode field is set to envoy**

**Example 1**

Configuration of the  `ext-auth`  plug-in:

```text
http_service:
 endpoint_mode: envoy
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_port: 8090
 path_prefix: /auth
 timeout: 1000
```

Use the following request gateway when the  `ext-auth`  plug-in is enabled:

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf-
00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

**Request** to the  `ext-auth`  **service succeeds:**

The  `ext-auth`  service receives the following authentication request:

```http
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1
Host: ext-auth.backend.svc.cluster.local
Authorization: xxx
Content-Length: 0
```

**Request to the**  `ext-auth`  **service fails:**

When the  `ext-auth`  service response is 5xx, the client receives the HTTP 403 response code and the full response header returned by the  `ext-auth`  service.

If the  `ext-auth`  service returns  `x-auth-version: 1.0`  and  `x-auth-failed: true` response headers, they are sent to the client.

```text
HTTP/1.1 403 Forbidden
x-auth-version: 1.0
x-auth-failed: true
date: Tue, 16 Jul 2024 00:19:41 GMT
server: istio-envoy
content-length: 0
```

If the  `ext-auth`  service is unreachable or the status code is 5xx, the HTTP status code configured in  `status_on_error`  is sent to the client to reject the client request.

If the  `ext-auth`  service returns another HTTP status code, the returned status code is sent to the client to reject the client request. If the  `allowed_client_headers`  field is configured, response headers that match the specified criteria are added to the client response.

**Example 2**

Configuration of the  `ext-auth`  plug-in:

```text
http_service:
 authorization_request:
 allowed_headers:
 - exact: x-auth-version
 headers_to_add:
 x-envoy-header: true
 authorization_response:
 allowed_upstream_headers:
 - exact: x-user-id
 - exact: x-auth-version
 endpoint_mode: envoy
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_host: my-domain.local
 service_port: 8090
 path_prefix: /auth
 timeout: 1000
```

Use the following request gateway when the  `ext-auth`  plug-in is enabled:

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf-
00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

The  `ext-auth`  service receives the following authentication request:

```http
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1
Host: my-domain.local
Authorization: xxx
X-Auth-Version: 1.0
x-envoy-header: true
Content-Length: 0
```

If the response returned by the  `ext-auth`  service contains the headers  `x-user-id`  and  `x-auth-version` , the gateway forwards both headers in its upstream request.

**When the endpoint_mode field is set to forward_auth**

**Example 1**

Configuration of the  `ext-auth`  plug-in:

```text
http_service:
 endpoint_mode: forward_auth
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_port: 8090
 path: /auth
 request_method: POST
 timeout: 1000
```

Use the following request gateway when the  `ext-auth`  plug-in is enabled:

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf-
00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "Host: 
foo.bar.com"
```

**Request** to the  `ext-auth`  **service succeeds:**

The  `ext-auth`  service receives the following authentication request:

```http
POST /auth HTTP/1.1
Host: ext-auth.backend.svc.cluster.local
Authorization: xxx
X-Forwarded-Proto: HTTP
X-Forwarded-Host: foo.bar.com
X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5
X-Forwarded-Method: GET
Content-Length: 0
```

**Request to the**  `ext-auth`  **service fails:**

When the  `ext-auth`  service response is 5xx, the client receives the HTTP 403 response code and the full response header returned by the  `ext-auth`  service.

If the  `ext-auth`  service returns  `x-auth-version: 1.0`  and  `x-auth-failed: true` response headers, they are sent to the client.

```text
HTTP/1.1 403 Forbidden
x-auth-version: 1.0
x-auth-failed: true
date: Tue, 16 Jul 2024 00:19:41 GMT
server: istio-envoy
content-length: 0
```

If the  `ext-auth`  service is unreachable or the status code is 5xx, the HTTP status code configured in  `status_on_error`  is sent to the client to reject the client request.

If the  `ext-auth`  service returns another HTTP status code, the returned status code is sent to the client to reject the client request. If the  `allowed_client_headers`  field is configured, response headers that match the specified criteria are added to the client response.

**Example 2**

Configuration of the  `ext-auth`  plug-in:

```text
http_service:
 authorization_request:
 allowed_headers:
 - exact: x-auth-version
 headers_to_add:
 x-envoy-header: true
 authorization_response:
 allowed_upstream_headers:
 - exact: x-user-id
 - exact: x-auth-version
 endpoint_mode: forward_auth
 endpoint:
 service_name: ext-auth.backend.svc.cluster.local
 service_host: my-domain.local
 service_port: 8090
 path: /auth
 request_method: POST
 timeout: 1000
```

Use the following request gateway when the  `ext-auth`  plug-in is enabled:

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf-
00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "X-Auth-Version: 
1.0" -H "Host: foo.bar.com"
```

The  `ext-auth`  service receives the following authentication request:

```http
POST /auth HTTP/1.1
Host: my-domain.local
Authorization: xxx
X-Forwarded-Proto: HTTP
X-Forwarded-Host: foo.bar.com
X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5
X-Forwarded-Method: GET
X-Auth-Version: 1.0
x-envoy-header: true
Content-Length: 0
```

If the response returned by the  `ext-auth`  service contains the headers  `x-user-id`  and  `x-auth-version` , the gateway forwards both headers in its upstream request.

<a id="section-3-6-3-7"></a>

#### 3.6.3.7. oauth

The oauth plug-in is used to issue OAuth 2.0 access tokens based on JSON web tokens (JWTs). The oauth plug-in complies with the RFC 9068 specification. This topic describes how to configure the oauth plug-in.

**Plug-in type**

Plug-in for authentication and authorization.

**Configuration description**

**Fields**

**Authentication configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| consumers | array of object | Yes | - | The callers of the service.This field is used to authenticate requests. |
| issuer | string | No | Higress -Gatewa y | The JWT issuer. |
| auth_path | string | No | /oauth2/token | The suffix of the specified path. The suffix is used to issue tokens. When you configure this field at the route level, you must make sure that the specified route can be matched. When you use the API management feature to create an API, you must create an API that has the same path. |
| global_crede ntials | bool | No | true | Specifies whether to use credentials issued by any route for access if the consumer authentication is passed. |
| auth_header_name | string | No | Authori zation | The request header from which you can obtain the JWT. |
| token_ttl | number | No | 7200 | The time to live (TTL) duration of the token after it is issued. Unit: seconds. |
| clock_skew_s econds | number | No | 60 | The clock skew allowed when the exp and iat fields in the JWT are verified. Unit: seconds. |
| keep_token | bool | No | true | Specifies whether to retain the JWT in the request when the request is forwarded to the backend service. |
| global_auth | array of string | No (Required only for instance-level configurations) | - | This field can be configured only at the instance level.<br>• If this field is set to true, the authentication mechanism globally takes effect.<br>• If this field is set to false, the authentication mechanism takes effect only for the configured domain names and routes.<br>• If this field is not configured, the authentication mechanism globally takes effect only when no domain names and routes are configured.This is in consideration of the usage habits of existing consumers. |

The following table describes the fields in  `consumers` .

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| name | string | Yes | - | The name of the consumer. |
| client_id | string | Yes | - | The ID of the OAuth 2.0 client. |
| client_secret | string | Yes | - | The secret of the OAuth 2.0 client. |

> **Important**
>
> - For a route for which the preceding configurations are enabled, if the path suffix and  `auth_path`  are matched, the system does not forward the route information to the destination service, but uses the route to generate a token.
>
> - If the  `global_credentials`  field is set to false, you must make sure that the route with the plug-in enabled does not use exact match. If another route exists and uses prefix match, an unexpected issue may occur.
>
> - For an authenticated request, an  `X-Mse-Consumer`  field is added to the request header to identify the name of the caller.

**(Optional) Authorization configuration**

| Field | Data type | Required | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| allow | array of string | No (Required for non-instance-level configurations) | - | You can only configure this field at a fine granularity such as route or domain name. For requests that meet the matching conditions, you can configure consumers that are allowed for access. This implements fine-grained permission control. |

> **Important**
>
> The authorization configuration and authentication configuration cannot coexist in a rule.

**Configuration examples**

**Route-level authentication configuration**

Apply the following plug-in configurations to the  `route-a`  and  `route-b`  routes:

```text
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Although the same configurations are used, the credentials issued by  `route-a`  cannot be used to access  `route-b`  and vice versa.

If you want to share the credential access permissions based on the same configurations, you can apply the following configurations:

```text
global_credentials: true
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**Configure global authentication and route-level authorization**

The following configurations enable JWT authentication for a specific route or domain name of the gateway. If a JWT matches multiple  `JSON Web Key Sets (JWKSs)` , the first  `consumer` that is matched is hit based on the configuration sequence.

Apply the following plug-in configurations at the instance level:

```text
global_auth: false
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Apply the following plug-in configurations to the  `route-a`  and  `route-b`  routes:

```text
allow:
- consumer1
```

Apply the following plug-in configurations to the  `*.example.com`  and  `test.com`  domain names:

```text
allow:
- consumer2
```

> **Note**
>
> - In this example, the  `route-a`  and  `route-b`  routes are those specified when the gateway routes are created. If a client request matches one of the routes, the caller whose  `name`  is  `consumer1`  is allowed to access the gateway. Other callers are not allowed to access the gateway.
>
> - In this example, the  `*.example.com`  and  `test.com`  domain names are used to match domain names in requests. If a client request matches one of the domain names, the caller whose  `name`  is  `consumer2`  is allowed to access the gateway. Other callers are not allowed to access the gateway.

**Enable authentication at the gateway level**

The following configurations enable OAuth2 authentication at the gateway level. All requests must be authenticated before they access the gateway.

```text
global_auth: true
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**Sample request**

**Use the Client Credential grant type**

**Obtain an access token**

```bash
# Obtain an access token by using the GET method. We recommend that you use this method.
curl 'http://test.com/oauth2/token?grant_type=client_credentials&client_id=12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Obtain an access token by using the POST method. To perform this operation, you need to match a route that points to a real destination service. Otherwise, the gateway doesnot read request bodies.
curl 'http://test.com/oauth2/token' -H 'content-type: application/x-www-form-urlencoded
' -d 'grant_type=client_credentials&client_id=12345678-xxxx-xxxx-xxxx-
xxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Obtain the value of the access_token field from the response.
{
  "token_type": "bearer",
  "access_token": 
"eyJh************.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW50X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHg
Hh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiOjE2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZX
eSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0ODEwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9.
T_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0",
  "expires_in": 7200
}
```

**Use the access token to initiate a request**

```bash
curl 'http://test.com' -H 'Authorization: Bearer 
eyJhbGciOiJIUzI1NiIsInR5cCI6ImFwcGxpY2F0aW9uXC9hdCtqd3QifQ.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW
X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHgteHh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiO
2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZXdheSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0
EwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9.NkT_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0'
```

**Error codes**

| HTTP status code | Error message | Reason |
| --- | --- | --- |
| 401 | Invalid Jwt token. | No JWT is provided in the request header, the JWT format is invalid, or the JWT expires. |
| 403 | Access Denied. | The consumer is not authorized to access the current route. |

<a id="section-3-6-3-8"></a>

#### 3.6.3.8. opa

The opa plug-in implements  `Open Policy Agent (OPA)`  policy control. This topic describes how to configure the opa plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `225`

**Fields**

| Field | Data type | Require d | Defaul t value | Description |
| --- | --- | --- | --- | --- |
| policy | string | Yes | - | The OPA policy. |
| timeout | string | Yes | - | The access timeout period. |
| serviceSource | string | Yes | - | Valid values: k8s, nacos, ip, and route. |
| host | string | No | - | The service host. This field is required if the serviceSource field is set to <code> ip </code>. |
| serviceName | string | No | - | The service name. This field is required if the serviceSource field is set to <code> k8s, </code> <code>nacos, or ip </code>. |
| servicePort | string | No | - | The service port. This field is required if the serviceSource field is set to <code> k8s, </code> <code>nacos, or ip </code>. |
| namespace | string | No | - | The namespace. This field is required if the serviceSource field is set to <code> k8s or </code> <code>nacos </code>. |

**Configuration example**

```text
serviceSource: k8s
serviceName: opa
servicePort: 8181
namespace: higress-backend
policy: example1
timeout: 5s
```

**OPA service installation guide**

**Start the OPA service**

```bash
docker run -d --name opa -p 8181:8181 openpolicyagent/opa:0.35.0 run -s
```

**Create an OPA policy**

```python
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
 -H 'Content-Type: text/plain' \
 -d 'package example1

import input.request

default allow = false

allow {
 # HTTP method must GET
 request.method == "GET"
}'
```

**Query the policy**

```bash
curl -X POST '127.0.0.1:8181/v1/data/example1/allow' \
 -H 'Content-Type: application/json' \
 -d '{"input":{"request":{"method":"GET"}}}'
```

<a id="section-3-6-4"></a>

### 3.6.4. Security

<a id="section-3-6-4-1"></a>

#### 3.6.4.1. cors

**Introduction**

The  `cors`  plug-in can automatically add the response headers required for Cross-Origin Resource Sharing (CORS) to the HTTP responses returned by the server side.

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td>allow_origins</td>
    <td>array of string</td>
    <td>No</td>
    <td>*</td>
    <td>The origin allowed for cross-origin access in the format scheme://host:po rt. Example: http://example.co m:8081. When allow_credentials is set to false, an asterisk (*) can be used to indicate that all origins are allowed.</td>
  </tr>
</table>

<table>
  <tr>
    <td>allow_origin_patt erns</td>
    <td>array of string</td>
    <td>No</td>
    <td>-</td>
    <td>The origin pattern matching for cross-origin access. You can use an asterisk (*) to match a domain name or port number.<br>For example, http://<em>.example.c</em> <em>om matches</em> <em>domain names,</em> <em>http://</em>.example.c om:[8080,9090] matches domain names and the specified ports, and http://<em>.example.c</em> <em>om:[</em>] matches domain names and all ports. A standalone * matches all origins (all domain names and ports).</td>
  </tr>
  <tr>
    <td>allow_methods</td>
    <td>array of string</td>
    <td>No</td>
    <td>GET, PUT, POST, DELETE, PATCH, OPTIONS</td>
    <td>The method that is allowed for cross-origin access, such as GET and POST.You can use * to indicate that all methods are allowed.</td>
  </tr>
  <tr>
    <td>allow_headers</td>
    <td>array of string</td>
    <td>No</td>
    <td>DNT,X-CustomHeader,K eep-Alive,User-Agent,X-Requested-With,<br>If-Modified-Since,Cache-Control,Content-Type,Authorizatio n</td>
    <td>Non-CORS-standard headers that can be included in requests for cross-origin access. The wildcard * can be used to allow any header.</td>
  </tr>
  <tr>
    <td>expose_headers</td>
    <td>array of string</td>
    <td>No</td>
    <td>-</td>
    <td>Non-CORS-standard headers that can be included in responses for cross-origin access. The wildcard * can be used to allow any header.</td>
  </tr>
  <tr>
    <td>allow_credentials</td>
    <td>bool</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether requests for cross-origin access can include credentials, such as cookies.According to CORS specifications, if you set this field to true, you cannot use * in allow_origins.Instead, you can use allow_origin_patt erns *.</td>
  </tr>
  <tr>
    <td>max_age</td>
    <td>number</td>
    <td>No</td>
    <td>86,400 seconds</td>
    <td>The maximum time for the browser to cache CORS results.Unit: seconds.<br>Within this time window, the browser reuses the last check result.</td>
  </tr>
</table>

**Configuration examples Allow all cross-origin access and disallow requests to carry credentials.**

```text
allow_origins:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: false
max_age: 7200
```

**Allow all cross-origin access and allow requests to carry credentials.**

```text
allow_origin_patterns:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: true
max_age: 7200
```

**Allow cross-origin access for specific subdomain names, specific HTTP methods, and specific request headers, and allow requests to carry credentials.**

```text
allow_origin_patterns:
 - http://*.example.com
 - http://*.example.org:[8080,9090]
allow_methods:
 - GET
 - PUT
 - POST
 - DELETE
allow_headers:
 - Token
 - Content-Type
 - Authorization
expose_headers:
 - '*'
allow_credentials: true
max_age: 7200
```

**Tests Test configurations**

```yaml
apiVersion: networking.higress.io/v1
kind: McpBridge
metadata:
 name: mcp-cors-httpbin
 namespace: higress-system
spec:
 registries:
 - domain: httpbin.org
 name: httpbin
 port: 80
 type: dns
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 annotations:
 higress.io/destination: httpbin.dns
 higress.io/upstream-vhost: "httpbin.org"
 higress.io/backend-protocol: HTTP
 name: ingress-cors-httpbin
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - host: httpbin.example.com
 http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: mcp-cors-httpbin
 path: /
 pathType: Prefix
---
apiVersion: extensions.higress.io/v1alpha1
kind: WasmPlugin
metadata:
 name: wasm-cors-httpbin
 namespace: higress-system
spec:
 defaultConfigDisable: true
 matchRules:
 - config:
 allow_origins:
 - http://httpbin.example.net
 allow_origin_patterns:
 - http://*.example.com:[*]
 - http://*.example.org:[9090,8080]
 allow_methods:
 - GET
 - POST
 - PATCH
 allow_headers:
 - Content-Type
 - Token
 - Authorization
 expose_headers:
 - X-Custom-Header
 - X-Env-UTM
 allow_credentials: true
 max_age: 3600
 configDisable: false
 ingress:
 - ingress-cors-httpbin
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/cors:1.0.0
 imagePullPolicy: Always
```

**Test requests**

**Simple request**

```bash
curl -v -H "Origin: http://httpbin2.example.org:9090" -H  "Host: httpbin.example.com"  http://127.0.0.1/anything/get\?foo\=1

< HTTP/1.1 200 OK
> x-cors-version: 1.0.0
> access-control-allow-origin: http://httpbin2.example.org:9090
> access-control-expose-headers: X-Custom-Header,X-Env-UTM
> access-control-allow-credentials: true
```

**Preflight requests**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H  "Host: 
httpbin.example.com" -H "Access-Control-Request-Method: POST"  -H "Access-Control-Request-Headers: Content-Type, Token" http://127.0.0.1/anything/get\?foo\=1

< HTTP/1.1 200 OK
< x-cors-version: 1.0.0
< access-control-allow-origin: http://httpbin2.example.org:9090
< access-control-allow-methods: GET,POST,PATCH
< access-control-allow-headers: Content-Type,Token,Authorization
< access-control-expose-headers: X-Custom-Header,X-Env-UTM
< access-control-allow-credentials: true
< access-control-max-age: 3600
< date: Tue, 23 May 2023 11:41:28 GMT
< server: istio-envoy
< content-length: 0
<
* Connection #0 to host 127.0.0.1 left intact
* Closing connection 0
```

**Preflight request with an invalid CORS origin**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org" -H  "Host: 
httpbin.example.com" -H "Access-Control-Request-Method: GET"  
http://127.0.0.1/anything/get\?foo\=1

 HTTP/1.1 403 Forbidden
< content-length: 70
< content-type: text/plain
< x-cors-version: 1.0.0
< date: Tue, 23 May 2023 11:27:01 GMT
< server: istio-envoy
<
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**Preflight request with an invalid CORS method**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H  "Host: 
httpbin.example.com" -H "Access-Control-Request-Method: DELETE"  
http://127.0.0.1/anything/get\?foo\=1

< HTTP/1.1 403 Forbidden
< content-length: 49
< content-type: text/plain
< x-cors-version: 1.0.0
< date: Tue, 23 May 2023 11:28:51 GMT
< server: istio-envoy
<
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**Preflight request with an invalid CORS header**

```bash
 curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H  "Host: 
httpbin.example.com" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request-Headers: TokenView"  http://127.0.0.1/anything/get\?foo\=1

< HTTP/1.1 403 Forbidden
< content-length: 52
< content-type: text/plain
< x-cors-version: 1.0.0
< date: Tue, 23 May 2023 11:31:03 GMT
< server: istio-envoy
<
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

<a id="section-3-6-4-2"></a>

#### 3.6.4.2. ip-restriction

The ip-restriction plug-in can restrict access to services or routes by whitelisting or blacklisting IP addresses. It can restrict access based on individual IP addresses, multiple IP addresses, and CIDR blocks, such as 10.10.10.0/24. This topic describes how to configure the ip-restriction plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `210`

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| ip_source_type | string | No | origin-source | Valid values:<br><code>• origin-</code><code>source </code>: indicates the peer-end socket IP address.<br>• <code> header </code>: obtains an IP address from the header. |
| ip_header_name | string | No | x-forwarded-for | The header from which an IP address is obtained. This field takes effect when <code>ip_source_typ</code> <code>e </code> is set to <code> header </code>. |
| allow | array | No | \[\] | The IP address whitelist. |
| deny | array | No | \[\] | The IP address blacklist. |
| status | int | No | 403 | The HTTP status code that is returned when access is denied. |
| message | string | No | Your IP address is blocked. | The information returned when access is denied. |

```text
ip_source_type: origin-source
allow:
 - 10.0.0.1
 - 192.168.0.0/16
```

```text
ip_source_type: header
ip_header_name: x-real-iP
deny:
 - 10.0.0.1
 - 192.169.X.X/16
```

<a id="section-3-6-4-3"></a>

#### 3.6.4.3. waf

The waf plug-in is a rule protection engine based on ModSecurity. You can use the waf plug-in to block suspicious requests based on the configured rules. The waf plug-in supports OWASP ModSecurity Core Rule Set (CRS) to provide basic protection features for websites. This topic describes how to configure the waf plug-in.

**Running attributes**

Plug-in execution stage:  `Authorization` . Plug-in execution priority:  `330` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| useCRS | bool | No | false | Specifies whether to enable OWASP CRS. For more information, see coreruleset. |
| secRules | array of string | No | - | The custom protection rules configured for the waf plug-in.For more information about the syntax, see ModSecurity documentation. |

**Configuration examples**

**Observation mode**

```text
useCRS: true
secRules:
 - "SecRuleEngine DetectionOnly"
```

**Remove a specific rule**

For example, if you enable the observation mode and find that a rule with an ID of 10 causes false blocking, you can remove this rule separately.

```text
useCRS: true
secRules:
 - "SecRuleRemoveById 10"
 - "SecRuleEngine On"
```

**Use custom protection rules**

```text
useCRS: true
secRules:
 - "SecDebugLogLevel 3"
 - "SecRuleEngine On"
 - "SecAction \"id:100,phase:1,pass\""
 - "SecRule REQUEST_URI \"@streq /admin\" \"id:101,phase:1,t:lowercase,deny\""
 - "SecRule REQUEST_BODY \"@rx maliciouspayload\" \"id:102,phase:2,t:lowercase,deny\""
```

The following request is blocked based on the preceding rule configuration.

```bash
curl http://example.com/admin
curl http://example.com -d "maliciouspayload"
```

<a id="section-3-6-4-4"></a>

#### 3.6.4.4. request-block

The request-block plug-in is used to block HTTP requests based on characteristics such as URLs and request headers. The request-block plug-in can be used to protect some website resources from external exposure. This topic describes how to configure the request-block plug-in.

**Running attributes**

Plug-in execution stage:  `Authorization` . Plug-in execution priority:  `320` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td>block_urls</td>
    <td>array of string</td>
    <td>No (You must configure <code> block_urls </code>, <code>block_exact_u</code> <code>rls </code>, <code>block_regexp_</code><code>urls </code>, <code>block_headers</code><code> </code>, or <code>block_bodies</code><code> </code>.)</td>
    <td>-</td>
    <td>The URLs that are used to match the requests to be blocked.</td>
  </tr>
  <tr>
    <td>block_exact_urls</td>
    <td>array of string</td>
    <td>No (You must configure <code> block_urls </code>, <code>block_exact_u</code> <code>rls </code>, <code>block_regexp_</code><code>urls </code>, <code>block_headers</code><code> </code>, or <code>block_bodies</code><code> </code>.)</td>
    <td>-</td>
    <td>The URLs that are used to exactly match the requests to be blocked.</td>
  </tr>
  <tr>
    <td>block_regexp_url s</td>
    <td>array of string</td>
    <td>No (You must configure <code> block_urls </code>, <code>block_exact_u</code> <code>rls </code>, <code>block_regexp_</code><code>urls </code>, <code>block_headers</code><code> </code>, or <code>block_bodies</code><code> </code>.)</td>
    <td>-</td>
    <td>The regular expressions that are used to match the URLs to be blocked.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c83e5dd082dd60ae3b9f6aba315b0361.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/7eee44ef4d23c3422ea991ce7067d615.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/9a78accb265dc76cfdbac3ca98097ce9.png)

<table>
  <tr>
    <td>block_headers</td>
    <td>array of string</td>
    <td>No (You must configure <code> block_urls </code>, <code>block_exact_u</code> <code>rls </code>, <code>block_regexp_</code><code>urls </code>, <code>block_headers</code><code> </code>, or <code>block_bodies</code><code> </code>.)</td>
    <td>-</td>
    <td>The headers that are used to match the requests to be blocked.</td>
  </tr>
  <tr>
    <td>block_bodies</td>
    <td>array of string</td>
    <td>No (You must configure <code> block_urls </code>, <code>block_exact_u</code> <code>rls </code>, <code>block_regexp_</code><code>urls </code>, <code>block_headers</code><code> </code>, or <code>block_bodies</code><code> </code>.)</td>
    <td>-</td>
    <td>The bodies that are used to match the requests to be blocked.</td>
  </tr>
  <tr>
    <td>blocked_code</td>
    <td>number</td>
    <td>No</td>
    <td>403</td>
    <td>The HTTP status code that is returned if a request is blocked.</td>
  </tr>
  <tr>
    <td>blocked_message</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>The HTTP response body that is returned if a request is blocked.</td>
  </tr>
  <tr>
    <td>case_sensitive</td>
    <td>bool</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether the conditions that are used to match requests are case-sensitive. Default value: true.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/4425aaa0fd6fdd63cf7d3bd432c16765.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/b14d07e3096092f60e80ea313027d9cc.png)

**Configuration examples**

**Block requests based on URLs**

```text
block_urls:
- swagger.html
- foo=bar
case_sensitive: false
```

The following requests are blocked based on the preceding rule configuration.

```bash
curl http://example.com?foo=Bar
curl http://exmaple.com/Swagger.html
```

**Block requests based on URLs that match exactly**

```text
block_exact_urls:
- /swagger.html?foo=bar
case_sensitive: false
```

The following request is blocked based on the preceding rule configuration.

```bash
curl http://exmaple.com/Swagger.html?foo=Bar
```

**Block requests based on URLs that match a regular expression**

```text
block_exact_urls:
- .*swagger.*
case_sensitive: false
```

The following request is blocked based on the preceding rule configuration.

```bash
curl http://exmaple.com/Swagger.html?foo=Bar
```

**Block requests based on request headers**

```text
block_headers:
- example-key
- example-value
```

The following requests are blocked based on the preceding rule configuration.

```bash
curl http://example.com -H 'example-key: 123'
curl http://exmaple.com -H 'my-header: example-value'
```

**Block requests based on request bodies**

```text
block_bodies:
- "hello world"
case_sensitive: false
```

The following requests are blocked based on the preceding rule configuration.

```bash
curl http://example.com -d 'Hello World'
curl http://exmaple.com -d 'hello world'
```

**Limit on the request body size**

If  `block_bodies`  is configured, only requests whose bodies are less than 32 MB are used for matching based on bodies. If the body of a request is greater than 32 MB and the request does not meet the rules specified by  `block_urls`  and  `block_headers` , the request is not blocked. If  `block_bodies`  is configured and the request body exceeds the value of DownstreamConnectionBufferLimits that is configured for the gateway, the error message  `413 Payload Too Large`  is returned.

<a id="section-3-6-4-5"></a>

#### 3.6.4.5. bot-detect

The bot-detect plug-in is used to identify web crawlers and prevent web crawlers from crawling websites. This topic describes how to configure the bot-detect plug-in.

**Running attributes**

Plug-in execution stage:  `Authorization` . Plug-in execution priority:  `310` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| allow | array of string | No | - | The regular expression that is used to match User-Agent request headers.If a User-Agent request header is matched, the request is allowed. |
| deny | array of string | No | - | The regular expression that is used to match User-Agent request headers.If a User-Agent request header is matched, the request is blocked. |
| blocked_code | number | No | 403 | The HTTP status code that is returned if a request is blocked. |
| blocked_message | string | No | - | The HTTP response body that is returned if a request is blocked. |

If the  `allow`  and  `deny`  fields are not configured, the default logic to identify crawlers is executed. You can configure the  `allow`  field to allow requests that hit the default crawler identification logic. You can configure the  `deny`  field to add additional crawler identification logic.

The following code shows the default set of regular expressions for crawler identification:

```text
# Bots General matcher 'name/0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50}))[/ ](\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots General matcher 'name 0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50})) (\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots containing spider|scrape|bot(but not CUBOT)|Crawl
 ((?:[A-z0-9]{1,50}|[A-z\-]{1,50} ?|)(?: the |)(?:[Ss][Pp][Ii][Dd][Ee][Rr]|[Ss]crape|[Cc][Rr][Aa][Ww][Ll])[A-z0-9]{0,50})(?:(?:[ /]| v)(\d+)(?:\.(\d+)|)(?:\.(\d+)|)|)
# Bots Pattern '/name-0.0'
 /((?:Ant-)?Nutch|[A-z]+[Bb]ot|[A-z]+
[Ss]pider|Axtaris|fetchurl|Isara|ShopSalad|Tailsweep)[ \-](\d+)(?:\.(\d+)(?:\.(\d+))?)?
# Bots Pattern 'name/0.0'
 
\b(008|Altresium|Argus|BaiduMobaider|BoardReader|DNSGroup|DataparkSearch|EDI|Goodzer|Grub
NGRID|Infohelfer|LinkedInBot|LOOQ|Nutch|OgScrper|PathDefender|Peew|PostPost|Steeler|Twitt
bot|VSE|WebCrunch|WebZIP|Y!J-BR[A-Z]|YahooSeeker|envolk|sproose|wminer)/(\d+)(?:\.(\d+)
|)(?:\.(\d+)|)
# More bots
 (CSimpleSpider|Cityreview Robot|CrawlDaddy|CrawlFire|Finderbots|Index crawler|Job Roboter|KiwiStatus Spider|Lijit Crawler|QuerySeekerSpider|ScollSpider|
```

**Configuration examples**

**Allow requests that hit the default crawler identification logic**

```text
allow:
- ".*Go-http-client.*"
```

If you do not configure the allow field, the Golang web library request is considered as a crawler, and the request is blocked.

**Add crawler identification logic**

```text
deny:
- "spd-tools.*"
```

The following requests are blocked based on the preceding rule configuration.

```bash
curl http://example.com -H 'User-Agent: spd-tools/1.1'
curl http://exmaple.com -H 'User-Agent: spd-tools'
```

<a id="section-3-6-5"></a>

### 3.6.5. Traffic management

<a id="section-3-6-5-1"></a>

#### 3.6.5.1. cluster-key-rate-limit

The cluster-key-rate-limit plug-in implements cluster throttling based on Redis. This plug-in is suitable for scenarios where you need to implement a global consistent throttling across multiple cloud-native gateways. This topic describes how to configure the cluster-key-rate-limit plug-in.

**Feature overview**

The  `cluster-key-rate-limit`  plug-in implements **cluster throttling** based on Redis. This plug-in is suitable for scenarios where you need to implement **global consistent throttling** across multiple cloud-native gateways.

Two throttling modes are supported:

- **Rule-level global throttling**: You can configure global throttling thresholds for custom rule groups based on the same  `rule_name`  and  `global_threshold`  configurations.

- **Key-level dynamic throttling**: Grouped throttling is performed based on dynamic keys in requests, such as URL parameters, request headers, client IP addresses, consumer names, and cookies.

**Running attributes**

Plug-in execution stage:  `default stage` . Plug-in execution priority:  `20` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| rule_name | string | Yes | - | The name of the throttling rule.You can concatenate the throttling rule name, throttling type, throttling key name, and actual value of the throttling key into a Redis key. |
| global_threshold | Object | No (You must specify <code>global_thresh</code> <code>old </code> or <code> rule_items </code>.) | - | Throttling is performed on the custom rule group. |
| rule_items | array of object | No (You must specify <code>global_thresh</code> <code>old </code> or <code> rule_items </code>.) | - | An array of throttling rules, which are matched in <strong>sequence</strong>. If a rule that meets the specified conditions is hit, throttling is triggered, and matching is not performed on subsequent rules. |
| show_limit_quota _header | bool | No | false | Specifies whether to display the <code> X-</code><code>RateLimit-</code><code>Limit </code> (the total number of throttled requests) and <code>X-RateLimit-</code><code>Remaining </code> (the number of remaining allowed requests) parameters in the response header. |
| rejected_code | int | No | 429 | The HTTP status code that is returned when requests are throttled. |
| rejected_msg | string | No | Too many requests | The response body that is returned when requests are throttled. |
| redis | object | Yes | - | The Redis-related configurations. |

The following table describes the fields in  `global_threshold` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| query_per_secon d | int | No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.) | - | The number of requests that are allowed per second. |
| query_per_minut e | int | No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.) | - | The number of requests that are allowed per minute. |
| query_per_hour | int | No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.) | - | The number of requests that are allowed per hour. |
| query_per_day | int | No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.) | - | The number of requests that are allowed per day. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/5cadeafe07fbc970925f988fd7b22f7d.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/8c2fbd69e2a0f34777871cfb4568d8cb.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/9f4160c177528199209f2773413d2a14.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/fb3e775fa59619c4bffbf9a5f77852df.png)

The following table describes the fields in  `rule_items` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| limit_by_header | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The name of the HTTP request header that is used to obtain the key value for throttling. |
| limit_by_param | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The name of the URL parameter that is used to obtain the key value for throttling. |
| limit_by_consume r | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The name of the consumer that is used for throttling. You do not need to specify the actual value. |
| limit_by_cookie | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The name of the cookie key that is used to obtain the key value for throttling. |
| limit_by_per_hea der | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The names of the HTTP request headers that are used to obtain the key value for throttling. The system matches specific HTTP request headers based on rules and separately calculates the rate based on each request header. When you configure <code> limit_keys </code>, regular expressions or asterisks (<code> * </code>) are supported. |
| limit_by_per_para m | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The names of the URL parameters that are used to obtain the key value for throttling. The system matches specific URL parameters based on rules and separately calculates the rate based on each URL parameter. When you configure <code> limit_keys </code>, regular expressions or asterisks (<code> * </code>) are supported. |
| limit_by_per_cons umer | string | No (You can configure only one of the <code>limit_by_*</code> fields.) | - | The names of the consumers that are used to obtain the key value for throttling. The system matches specific consumers based on rules and separately calculates the rate based on each consumer.You do not need to specify the actual value.When you configure <code> limit_keys </code>, regular expressions or asterisks (<code> * </code>) are supported. |

<table>
  <tr>
    <td>limit_by_per_cook ie</td>
    <td>string</td>
    <td>No (You can configure only one of the <code>limit_by_*</code> fields.)</td>
    <td>-</td>
    <td>The names of the cookie keys that are used to obtain the key value for throttling. The system matches specific cookie keys based on rules and separately calculates the rate based on each cookie key.When you configure <code> limit_keys </code>, regular expressions or asterisks (<code> * </code>) are supported.</td>
  </tr>
  <tr>
    <td>limit_by_per_ip</td>
    <td>string</td>
    <td>No (You can configure only one of the <code>limit_by_*</code> fields.)</td>
    <td>-</td>
    <td>The IP addresses that are used to obtain the key value for throttling. You can configure <code>from-header-</code><code>Header name </code>, such as <code> from-</code><code>header-x-</code><br><code>forwarded-</code><code>for </code>, to obtain IP addresses from request headers. You can also configure <code>from-remote-</code><code>addr </code> to directly obtain the peer socket IP address. The system matches specific IP addresses based on rules and separately calculates the rate based on each IP address.</td>
  </tr>
  <tr>
    <td>limit_keys</td>
    <td>array of object</td>
    <td>Yes</td>
    <td>-</td>
    <td>The number of times throttling is triggered after a specific key value is matched.</td>
  </tr>
</table>

The following table describes the fields in  `limit_keys` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| key | string | Yes | - | The matched key value. Regular expressions or asterisks (\*) are supported for <code>limit_by_per_</code><code>header </code>, <code>limit_by_per_</code><code>param </code>, <code>limit_by_per_</code><code>consumer </code>, and <code>limit_by_per_</code><code>cookie </code>. If you want to use a regular expression, you must place regexp: before the regular expression. If you use an asterisk (\*), all the key values are matched.Example of a regular expression: <code> regexp:^d.* </code>.In this example, all strings that start with d can be matched. IP addresses or CIDR blocks are supported for <code>limit_by_per_</code><code>ip </code>. |
| query_per_secon d | int | No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.) | - | The number of requests that are allowed per second. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/a944496cd4e06a4f934031c781b46e95.png)

<table>
  <tr>
    <td>query_per_minut e</td>
    <td>int</td>
    <td>No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.)</td>
    <td>-</td>
    <td>The number of requests that are allowed per minute.</td>
  </tr>
  <tr>
    <td>query_per_hour</td>
    <td>int</td>
    <td>No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.)</td>
    <td>-</td>
    <td>The number of requests that are allowed per hour.</td>
  </tr>
  <tr>
    <td>query_per_day</td>
    <td>int</td>
    <td>No (You can configure only one of the <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, and <code>query_per_day</code> <code> </code> fields.)</td>
    <td>-</td>
    <td>The number of requests that are allowed per day.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/1554d44ee1f9f581c12bd36a9df14060.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/ac772f007508f056609e03a12c05f5ed.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/690afb083f0594e8009497c6062c1a3f.png)

The following table describes the fields in  `redis` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td>service_name</td>
    <td>string</td>
    <td>Yes</td>
    <td>-</td>
    <td>The Redis service name, which is a fully qualified domain name (FQDN) with a specific service type, such as my-redis.dns or redis.my-ns.svc.cluster.loc al.</td>
  </tr>
  <tr>
    <td>service_port</td>
    <td>int</td>
    <td>No</td>
    <td>If the service type is static service, the default value is<br>80. For other services, the default value is 6379.</td>
    <td>The port number of the Redis service.</td>
  </tr>
  <tr>
    <td>username</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>The username that is used to log in to the Redis service.</td>
  </tr>
  <tr>
    <td>password</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>The password that is used to log in to the Redis service.</td>
  </tr>
  <tr>
    <td>timeout</td>
    <td>int</td>
    <td>No</td>
    <td>1000</td>
    <td>The connection timeout period of the Redis service. Unit: milliseconds.</td>
  </tr>
  <tr>
    <td>database</td>
    <td>int</td>
    <td>No</td>
    <td>0</td>
    <td>The ID of the database that you want to use.For example, if you set this field to 1, <code> SELECT </code> <code>1 </code> is used.</td>
  </tr>
</table>

**Configuration examples**

**Custom rule group for global throttling**

```text
rule_name: routeA-global-limit-rule
global_threshold:
 query_per_minute: 1000 # The custom rule group allows 1,000 requests per minute.
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Identify requests based on the apikey parameter and perform different throttling operations for the requests**

```text
rule_name: routeA-request-param-limit-rule
rule_items:
 - limit_by_param: apikey
 limit_keys:
 - key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 query_per_minute: 10
 - key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 query_per_hour: 100
 - limit_by_per_param: apikey
 limit_keys:
 # A regular expression is used to match all API keys that start with a. For each matched API key, 10 requests are allowed per second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # A regular expression is used to match all API keys that start with b. For each matched API key, 100 requests are allowed per minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: For each consumer, 1,000 requests are allowed per hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Identify requests based on the request header x-ca-key and perform different throttling operations for the requests**

```text
rule_name: routeA-request-header-limit-rule
rule_items:
 - limit_by_header: x-ca-key
 limit_keys:
 - key: 102234
 query_per_minute: 10
 - key: 308239
 query_per_hour: 10
 - limit_by_per_header: x-ca-key
 limit_keys:
 # A regular expression is used to match all API keys that start with a. For each matched API key, 10 requests are allowed per second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # A regular expression is used to match all API keys that start with b. For each matched API key, 100 requests are allowed per minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: For each consumer, 1,000 requests are allowed per hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Obtain the peer IP addresses based on the request header x-forwarded-for and perform different throttling operations for requests**

```text
rule_name: routeA-client-ip-limit-rule
rule_items:
 - limit_by_per_ip: from-header-x-forwarded-for # Throttling based on the IP addresses in x-forwarded-for headers
 limit_keys:
 # Exact IP address: 1.1.X.X, limited to 10 requests per day
 - key: 1.1.X.X
 query_per_day: 10
 # CIDR block 1.1.1.0/24: 100 requests are allowed per day for each IP address.
 - key: 1.1.1.0/24
 query_per_day: 100
 # Fallback rule: 1000 requests are allowed per day for each IP address.
 - key: 0.0.0.0/0
 query_per_day: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Identify requests based on consumers and perform different throttling operations for the requests**

```text
rule_name: routeA-consumer-limit-rule
rule_items:
 - limit_by_consumer: ''
 limit_keys:
 - key: consumer1
 query_per_second: 10
 - key: consumer2
 query_per_hour: 100
 - limit_by_per_consumer: ''
 limit_keys:
 # A regular expression is used to match all consumers that start with a. For each matched consumer, 10 requests are allowed per second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # A regular expression is used to match all consumers that start with b. For each matched consumer, 100 requests are allowed per minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: For each consumer, 1,000 requests are allowed per hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Identify requests based on key-value pairs in cookies and perform different throttling operations for the requests**

```text
rule_name: routeA-cookie-limit-rule
rule_items:
 - limit_by_cookie: key1 # Throttling is performed based on the cookie key key1.
 limit_keys:
 # Fixed value value1: 10 requests are allowed per minute.
 - key: value1
 query_per_minute: 10
 # Fixed value value2: 100 requests are allowed per hour.
 - key: value2
 query_per_hour: 100
 - limit_by_per_cookie: key1 # Throttling is performed independently based on each value of the cookie key key1.
 limit_keys:
 # A regular expression is used to match all values that start with a. For each matchedvalue, 10 requests are allowed per second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # A regular expression is used to match all values that start with b. For each matchedvalue, 100 requests are allowed per minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: For each value, 1,000 requests are allowed per hour.
 - key: "*"
 query_per_hour: 1000
rejected_code: 200
rejected_msg: '{"code":-1,"msg":"Too many requests"}'
redis:
 service_name: redis.static
show_limit_quota_header: true
```

<a id="section-3-6-5-2"></a>

#### 3.6.5.2. key-rate-limit

The key-rate-limit plug-in implements rate limiting based on specific key values. Key values can be obtained from URL parameters or HTTP request headers. This topic describes how to configure the key-rate-limit plug-in.

**Running attributes**

Plug-in execution stage:  `default stage` . Plug-in execution priority:  `10` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| limit_by_header | string | No (You must configure <code>limit_by_head</code> <code>er </code> or <code>limit_by_para</code> <code>m </code>.) | - | The HTTP request header from which the key value for rate limiting is obtained. |
| limit_by_param | string | No (You must configure <code>limit_by_head</code> <code>er </code> or <code>limit_by_para</code> <code>m </code>.) | - | The URL parameter from which the key value for rate limiting is obtained. |
| limit_keys | array of object | Yes | - | The number of times rate limiting is triggered after a specific key value is matched. |

The following table describes the configuration fields in  `limit_keys` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| key | string | Yes | - | The key value that is used to match requests. |
| query_per_secon d | number | No (You must configure <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, or <code>query_per_day</code><code> </code>.) | - | The number of requests that are allowed per second. |
| query_per_minut e | number | No (You must configure <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, or <code>query_per_day</code><code> </code>.) | - | The number of requests that are allowed per minute. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/cebf8d4a278bcf21817e692a761f61b2.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/45b4bd66cf7700c1ce8fc778fe60c462.png)

<table>
  <tr>
    <td>query_per_hour</td>
    <td>number</td>
    <td>No (You must configure <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, or <code>query_per_day</code><code> </code>.)</td>
    <td>-</td>
    <td>The number of requests that are allowed per hour.</td>
  </tr>
  <tr>
    <td>query_per_day</td>
    <td>number</td>
    <td>No (You must configure <code>query_per_sec</code> <code>ond </code>, <code>query_per_min</code> <code>ute </code>, <code>query_per_hou</code> <code>r </code>, or <code>query_per_day</code><code> </code>.)</td>
    <td>-</td>
    <td>The number of requests that are allowed per day.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/0087cf329262c6f1389112c8773ee6ac.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/5a712f8973ae28454653afc13ce59ee6.png)

**Configuration examples**

**Identify requests based on the apikey parameter and perform different rate limiting operations for the requests**

```text
limit_by_param: apikey
limit_keys:
- key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 query_per_second: 10
- key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 query_per_minute: 100
```

**Identify requests based on the request header x-ca-key and perform different rate limiting operations for the requests**

```text
limit_by_header: x-ca-key
limit_keys:
- key: 102234
 query_per_second: 10
- key: 308239
 query_per_hour: 10
```

<a id="section-3-6-5-3"></a>

#### 3.6.5.3. traffic-tag

You can use the traffic-tag plug-in to tag request traffic based on weight or specific request content by adding specific request headers. You can use the traffic-tag plug-in to configure complex-logic rules for traffic tagging. This topic describes how to configure the traffic-tag plug-in.

**Running attributes**

Plug-in execution stage:  `default stage` . Plug-in execution priority:  `400` .

**Fields**

This section describes the fields that you can configure for the plug-in.

| Field | Data type | Default value | Required | Description |
| --- | --- | --- | --- | --- |
| <code>conditionGroup</code><br><code>s</code> | array of object | - | No | The content-based condition groups. For more information, see the conditionGroups configurations section in this topic. |
| <code>weightGroups</code> | array of object | - | No | The weight-based condition groups. For more information, see the weightGroups configurations section in this topic. |
| <code>defaultTagKey</code> | string | - | No | The default tag key. If no condition is matched, the default tag key is used. This field takes effect only if the defaultTagVal field is configured. |
| <code>defaultTagVal</code> | string | - | No | The default tag value. If no condition is matched, the default tag value is used. This field takes effect only if the defaultTagKey field is configured. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/9d91b0433c79b4505e0cfee987ed0cb0.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/7b5ea1a8f41f53a119f3100fa900c8cf.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/086098cfe649fd2c019eb7d9c9e8cab2.png)

**conditionGroups configurations**

The following table describes the fields in the  `conditionGroups`  field.

| Field | Data type | Default value | Required | Description |
| --- | --- | --- | --- | --- |
| <code>headerName</code> | string | - | Yes | The name of the HTTP header that you want to add or modify. |
| <code>headerValue</code> | string | - | Yes | The value of the HTTP header. |
| <code>logic</code> | string | - | Yes | The logical relationship among conditions, which can be <code> and </code> or <code> or </code>. The value must be in lowercase. |
| <code>conditions</code> | array of object | - | Yes | The specific conditions. For more information about the structure, see the fields in the <code>conditions</code> field. |

The following table describes the fields in the  `conditions`  field.

| Field | Data type | Default value | Required | Description |
| --- | --- | --- | --- | --- |
| <code>conditionType</code> | string | - | Yes | The condition type, which can be <code> header </code>, <code> parameter </code>, or <code> cookie </code>. |
| <code>key</code> | string | - | Yes | The condition keyword. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/726d27e6537e8c18de4af971f78cdfaf.png)

<table>
  <tr>
    <td><code>operator</code></td>
    <td>string</td>
    <td>-</td>
    <td>Yes</td>
    <td>The operator, which can be <code> equal </code>, <code> not_equal </code>, <code> prefix </code>, <code> in </code>, <code> not_in </code>, <code> regex </code>, or <code> percentage </code>.</td>
  </tr>
  <tr>
    <td><code>value</code></td>
    <td>array of string</td>
    <td>-</td>
    <td>Yes</td>
    <td>The condition value. You can configure multiple values <strong>only if</strong> the operator is <code> in </code> or <code> not_in </code>.</td>
  </tr>
</table>

> **Note**
>
> If the operator is regex, the regular expression engine RE2 is used. For more information, see RE2 official documentation.

**weightGroups configurations**

The following table describes the fields in the  `weightGroups`  field.

| Field | Data type | Default value | Required | Description |
| --- | --- | --- | --- | --- |
| <code>headerName</code> | string | - | Yes | The name of the HTTP header that you want to add or modify. |
| <code>headerValue</code> | string | - | Yes | The value of the HTTP header. |
| <code>weight</code> | integer | - | Yes | The traffic weight in percentage. |

**Supported operators**

| Operator | Description |
| --- | --- |
| <code>equal</code> | If a value is exactly the same as the specified value, the condition is met. |
| <code>not_equal</code> | If a value differs from the specified value, the condition is met. |
| <code>prefix</code> | If a value is prefixed with the specified value, the condition is met. |
| <code>in</code> | If a value is included in the specified list, the condition is met. |
| <code>not_in</code> | If a value is excluded from the specified list, the condition is met. |
| <code>regex</code> | If a value complies with the regular expression rules, the condition is met. |
| <code>percentage</code> | If the inequality <code> hash(get(key)) % 100 &lt; </code> <code>value </code> is true, the condition is met. |

> **Important**
>
> If you use the percentage operator, the system determines whether a request meets specified percentage conditions. If you use the weight field, the system distributes traffic in a static and random manner.

**Configuration examples**

**Example 1: content-based matching**

In the following sample code, if the header  `role`  of a request is  `user` ,  `viewer` , or  `editor`  and  `foo=bar`  is specified in the request, the header  `x-mse-tag: gray`  is added to the request. If no condition is matched for a request, the header  `x-mse-tag: base`  is added to the request, as defined in the configurations of the  `defaultTagKey`  and  `defaultTagVal`  fields.

```text
defaultTagKey: x-mse-tag
defaultTagVal: base
conditionGroups:
 - headerName: x-mse-tag
 headerValue: gray
 logic: and
 conditions:
 - conditionType: header
 key: role
 operator: in
 value:
 - user
 - viewer
 - editor
 - conditionType: parameter
 key: foo
 operator: equal
 value:
 - bar
```

**Example 2: weight-based matching**

In the following sample code, a request has a 30% chance of being added with the request header  `x-mse-tag: gray` , another 30% chance of being added with the request header  `x-mse-tag: blue` , and a 40% chance of being added with no request header.

```text
# The total weight is 100. The weight value 40, which is not configured, indicates thatno header is added.
weightGroups:
 - headerName: x-mse-tag
 headerValue: gray
 weight: 30
 - headerName: x-mse-tag
 headerValue: blue
 weight: 30
```

<a id="section-3-6-5-4"></a>

#### 3.6.5.4. request-validation

The request-validation plug-in is used to validate requests before they are forwarded to the upstream service. This plug-in uses the  `JSON Schema`  mechanism for data validation. It can validate the body and header data of a request. This topic describes how to configure the request-validation plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `220` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| header_schema | object | No | - | The JSON schema used to validate a request header. |
| body_schema | object | No | - | The JSON schema used to validate a request body. |
| rejected_code | number | No | 403 | The HTTP status code that is returned when a request is rejected. |
| rejected_msg | string | No | - | The HTTP response body that is returned when a request is rejected. |
| enable_swagger | bool | No | false | Specifies whether to enable validation on Swagger documentation. |
| enable_oas3 | bool | No | false | Specifies whether to enable validation on OpenAPI 3.0 (OAS3) documentation. |

> **Important**
>
> The validation rules are the same for headers and bodies.

**Configuration examples**

**Enum validation**

```text
body_schema:
 type: object
 required:
 - enum_payload
 properties:
 enum_payload:
 type: string
 enum:
 - "enum_string_1"
 - "enum_string_2"
 default: "enum_string_1"
```

**Boolean validation**

```text
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
 default: true
```

**Number or integer validation**

```text
body_schema:
 type: object
 required:
 - integer_payload
 properties:
 integer_payload:
 type: integer
 minimum: 1
 maximum: 10
```

**String validation**

```text
body_schema:
 type: object
 required:
 - string_payload
 properties:
 string_payload:
 type: string
 minLength: 1
 maxLength: 10
```

**Regex validation**

```text
body_schema:
 type: object
 required:
 - regex_payload
 properties:
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**Array validation**

```text
body_schema:
 type: object
 required:
 - array_payload
 properties:
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
```

**Combined validation**

```text
body_schema:
 type: object
 required:
 - boolean_payload
 - array_payload
 - regex_payload
 properties:
 boolean_payload:
 type: boolean
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**Custom rejection information**

```text
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
rejected_code: 403
rejected_msg: "Request rejected"
```

<a id="section-3-6-6"></a>

### 3.6.6. Transmission

<a id="section-3-6-6-1"></a>

#### 3.6.6.1. transformer

The transformer plug-in can transform request/response headers, request query parameters, and request/response body parameters. The supported transformation operations include remove, rename, replace, add, append, map, and dedupe. This topic describes how to configure the transformer plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `410` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| reqRules | string | No (You must specify at least one of reqRules and respRules.) | - | The request transformer configuration, which specifies the transformation operation and the transformation rules for the request headers, request query parameters, and request body. |
| respRules | string | No (You must specify at least one of reqRules and respRules.) | - | The response transformer configuration, which specifies the transformation operation and the transformation rules for the response headers and response body. |

The following table describes the fields in  `reqRules`  and  `respRules` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td>operate</td>
    <td>string</td>
    <td>Yes (Valid values: <code> remove </code>, <code> rename </code>, <code> replace </code>, <code> add </code>, <code> append </code>, <code> map </code>, and <code> dedupe </code>)</td>
    <td>-</td>
    <td>The transformation operation.Supported operations include remove, rename, replace, add, append, map, and dedupe. If multiple transformation rules of different types exist, the operations are executed in the order listed here.</td>
  </tr>
  <tr>
    <td>mapSource</td>
    <td>string</td>
    <td>No (Valid values: <code> headers </code>, <code> querys </code>, and <code> body </code>)</td>
    <td>-</td>
    <td>This field is valid only when the operate field is set to <code> map </code>.This field specifies the mapping source.If this field is left empty, the default mapping source is the current object.</td>
  </tr>
  <tr>
    <td>headers</td>
    <td>array of object</td>
    <td>No</td>
    <td>-</td>
    <td>The transformation rule for the request/response headers.</td>
  </tr>
  <tr>
    <td>querys</td>
    <td>array of object</td>
    <td>No</td>
    <td>-</td>
    <td>The transformation rule for the request query parameters.</td>
  </tr>
  <tr>
    <td>body</td>
    <td>array of object</td>
    <td>No</td>
    <td>-</td>
    <td>The transformation rule for request and response body parameters. For a request body, the content-type can be <code>application/j</code> <code>son </code>, <code>application/x</code><br><code>-www-form-</code><code>urlencoded </code>, or <code>multipart/for</code> <code>m-data </code>. For a response body, the content-type can be <code>application/j</code> <code>son </code>.</td>
  </tr>
</table>

The following table describes the fields in  `headers` ,  `querys` , and  `body` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| key | string | No | - | This field is valid when the operate field is set to <code> remove </code>. For more information, see Transformation operations. |
| oldKey | string | No | - | This field is valid when the operate field is set to <code> rename </code>. For more information, see Transformation operations. |
| newKey | string | No | - | This field is valid when the operate field is set to <code> rename </code>. For more information, see Transformation operations. |
| key | string | No | - | This field is valid when the operate field is set to <code> replace </code>. For more information, see Transformation operations. |
| newValue | string | No | - | This field is valid when the operate field is set to <code> replace </code>. For more information, see Transformation operations. |
| key | string | No | - | This field is valid when the operate field is set to <code> add </code>. For more information, see Transformation operations. |
| value | string | No | - | This field is valid when the operate field is set to <code> add </code>. For more information, see Transformation operations. |
| key | string | No | - | This field is valid when the operate field is set to <code> append </code>. For more information, see Transformation operations. |
| appendValue | string | No | - | This field is valid when the operate field is set to <code> append </code>. For more information, see Transformation operations. |
| fromKey | string | No | - | This field is valid when the operate field is set to <code> map </code>. For more information, see Transformation operations. |
| toKey | string | No | - | This field is valid when the operate field is set to <code> map </code>. For more information, see Transformation operations. |
| key | string | No | - | This field is valid when the operate field is set to <code> dedupe </code>. For more information, see Transformation operations. |
| strategy | string | No | - | This field is valid when the operate field is set to <code> dedupe </code>. For more information, see Transformation operations. |
| value_type | string | No (Valid values: <code> object </code>, <code> boolean </code>, <code> number </code>, and <code> string </code>) | string | When content-type is <code>application/j</code> <code>son </code>, this field specifies the value type of the request/response body parameters. |
| host_pattern | string | No | - | The hostname matching rule for the request. This field takes effect when the operate field is set to <code> replace </code>, <code> add </code>, or <code> append </code>. |
| path_pattern | string | No | - | The path matching rule for the request. This field takes effect when the operate field is set to <code> replace </code>, <code> add </code>, or <code> append </code>. |

Note:

- `request transformer`  supports the following transformation objects: request headers, request query parameters, and request body (application/json, application/x-www-form-urlencoded, and multipart/form-data).

- `response transformer`  supports the following transformation objects: response headers and response body (application/json).

- The transformer plug-in supports bidirectional transformation. That is, a single plug-in can transform both requests and responses.

- The execution sequence of transformation operations follows the sequence defined in the configuration file, such as remove > rename > replace > add > append > map > dedupe or dedupe > map > append > add > replace > rename > remove.

- When the transformation object is headers,  `key`  is case-insensitive. When the transformation object is headers and the operation is  `rename`  or  `map` ,  `value`  is also case-insensitive (because the value field serves as the key-like identifier in these cases). When the transformation object is querys or body, both  `key`  and  `value`  are case-sensitive.

- `value_type`  takes effect only for request/response bodies whose content-type is application/json.

- `host_pattern`  and  `path_pattern`  support RE2 syntax and take effect only for  `replace` ,  `add` , and  `append`  operations. You can specify only one of the two matching rules in a transformation rule. If both matching rules are specified,  `host_pattern`  takes effect and  `path_pattern`  does not.

**Transformation operations**

| Operation | Meaning of the key field | Meaning of the value field | Description |
| --- | --- | --- | --- |
| remove | The destination key. | You do not need to specify this field. | If the specified <code> key </code> exists, remove it.Otherwise, no operation is performed. |
| rename | The destination oldKey. | The name of the new key. | If the specified <code> oldKey:value </code> pair exists, rename its key name <code> newKey </code> to obtain <code> newKey:value </code>.Otherwise, no operation is performed. |
| replace | The destination key. | The new value. | If the specified <code> key:value </code> pair exists, update its value to <code> newValue </code> to obtain <code> key:newValue </code>.Otherwise, no operation is performed. |
| add | The key to be added. | The value to be added. | If the specified <code> key:value </code> pair does not exist, add it.Otherwise, no operation is performed. |
| append | The destination key. | The value to be added. | If the specified <code> key:value </code> pair exists, append appendValue to obtain <code>key:[value...</code><code>appendValue] </code>.Otherwise, perform an add operation to obtain <code> key:appendValue </code>. |
| map | The mapping source fromKey. | The mapping destination toKey. | If the specified <code>fromKey:fromValue</code> <code> </code> pair exists, map its value fromValue to the value of toKey to obtain the <code>toKey:fromValue</code> pair while retaining the original <code>fromKey:fromValue</code> <code> </code> pair.<br>Note<br>If toKey already exists, its value is overwritten.Otherwise, no operation is performed. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/b9618b8434afc70c35a29df83fce1845.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/f9eb03e22791c00bf91e56e00bf9aac7.png)

<table>
  <tr>
    <td>dedupe</td>
    <td>The destination key.</td>
    <td>The value specifies a deduplication strategy.</td>
    <td>Valid values for <code> strategy </code>:<br>• <code> RETAIN_UNIQUE </code>: Retain all unique values in order. For example, <code> k1:</code> <code>[v1,v2,v3,v3,v2,v1</code><code>] </code> becomes <code> k1:</code> <code>[v1,v2,v3] </code> after deduplication.<br>• <code> RETAIN_LAST </code>: Retain the last value. For example, <code>k1:[v1,v2,v3]</code> becomes <code> k1:v3 </code> after deduplication.<br><code>• RETAIN_FIRST</code> (default): Retain the first value. For example, <code> k1:</code> <code>[v1,v2,v3]</code> becomes <code> k1:v1 </code> after deduplication.<br>Note<br>If only one element v1 is left after deduplication, the key-value pair becomes <code> k1:v1 </code>, rather than <code> k1:[v1] </code>.</td>
  </tr>
</table>

**Configuration examples**

**Implement routing based on body parameters**

Configuration example:

```text
reqRules:
- operate: map
 headers:
 - fromKey: userId
 toKey: x-user-id
 mapSource: body
```

This rule parses the value of  `userId`  from the request body and sets  `x-user-id`  in the request header to the userId value. This enables body parameter-based routing by using the gateway capability to match routes based on request headers.

This configuration supports request bodies of the  `application/json`  and  `application/x-www-form-urlencoded`  types.

Example:

**For a request body of the application/json type**

```bash
curl localhost -d '{"userId":12, "userName":"johnlanni"}' -H 'content-
type:application/json'
```

The gateway extracts the value of the  `userId`  field from the JSON format and sets  `x-user-id`  to the value. The request received by the backend service includes the header  `x-usr-id: 12` .

After the plug-in adds this header, the gateway recalculates the routing. Therefore, the gateway routing configuration can match the route with a specific destination service based on this request header.

**For a request body of the application/x-www-form-urlencoded type**

```bash
curl localhost -d 'userId=12&userName=johnlanni'
```

The gateway extracts the value of the  `userId`  field from the  `k1=v1&k2=v2`  form format and sets  `x-user-id`  to the value. The request received by the backend service includes the header  `x-usr-id: 12` .

After the plug-in adds this header, the gateway recalculates the routing. Therefore, the gateway routing configuration can match the route with a specific destination service based on this request header.

**Support for JSON paths**

Fields can be extracted from complex JSON structures by using GJSON Path Syntax.

Common operations are illustrated with the following JSON code:

```json
{
 "name": {"first": "Tom", "last": "Anderson"},
 "age":37,
 "children": ["Sara","Alex","Jack"],
 "fav.movie": "Deer Hunter",
 "friends": [
 {"first": "Dale", "last": "Murphy", "age": 44, "nets": ["ig", "fb", "tw"]},
 {"first": "Roger", "last": "Craig", "age": 68, "nets": ["fb", "tw"]},
 {"first": "Jane", "last": "Murphy", "age": 47, "nets": ["ig", "tw"]}
 ]
}
```

The following extraction can be implemented:

```text
name.last "Anderson"
name.first "Tom"
age 37
children ["Sara","Alex","Jack"]
children.0 "Sara"
children.1 "Alex"
friends.1 {"first": "Roger", "last": "Craig", "age": 68}
friends.1.first "Roger"
```

If you want to extract the first field of the second item in friends from the preceding JSON-formatted body and configure it in the  `x-first-name`  header, and extract the last field and configure it in the  `x-last-name`  header, you can use the following plug-in configuration:

```text
reqRules:
- operate: map
 headers:
 - fromKey: friends.1.first
 toKey: x-first-name
 - fromKey: friends.1.last
 toKey: x-last-name
 mapSource: body
```

**Request Transformer**

**Transform request headers**

```text
reqRules:
- operate: remove
 headers:
 - key: X-remove
- operate: rename
 headers:
 - oldKey: X-not-renamed
 newKey: X-renamed
- operate: replace
 headers:
 - key: X-replace
 newValue: replaced
- operate: add
 headers:
 - key: X-add-append
 value: host-$1
 host_pattern: ^(.*)\.com$
- operate: append
 headers:
 - key: X-add-append
 appendValue: path-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: map
 headers:
 - fromKey: X-add-append
 toKey: X-map
- operate: dedupe
 headers:
 - key: X-dedupe-first
 strategy: RETAIN_FIRST
 - key: X-dedupe-last
 strategy: RETAIN_LAST
 - key: X-dedupe-unique
 strategy: RETAIN_UNIQUE
```

Send a request:

```bash
$ curl -v console.higress.io/get -H 'host: foo.bar.com' \
-H 'X-remove: exist' -H 'X-not-renamed:test' -H 'X-replace:not-replaced' \
-H 'X-dedupe-first:1' -H 'X-dedupe-first:2' -H 'X-dedupe-first:3' \
-H 'X-dedupe-last:a' -H 'X-dedupe-last:b' -H 'X-dedupe-last:c' \
-H 'X-dedupe-unique:1' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:3' \
-H 'X-dedupe-unique:3' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:1'

# HTTPBin response
{
 "args": {},
 "headers": {
 ...
 "X-Add-Append": "host-foo.bar,path-get",
 ...
 "X-Dedupe-First": "1",
 "X-Dedupe-Last": "c",
 "X-Dedupe-Unique": "1,2,3",
 ...
 "X-Map": "host-foo.bar,path-get",
 "X-Renamed": "test",
 "X-Replace": "replaced"
 },
 ...
}
```

**Transform request query parameters**

```text
reqRules:
- operate: remove
 querys:
 - key: k1
- operate: rename
 querys:
 - oldKey: k2
 newKey: k2-new
- operate: replace
 querys:
 - key: k2-new
 newValue: v2-new
- operate: add
 querys:
 - key: k3
 value: v31-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: append
 querys:
 - key: k3
 appendValue: v32
- operate: map
 querys:
 - fromKey: k3
 toKey: k4
- operate: dedupe
 querys:
 - key: k4
 strategy: RETAIN_FIRST
```

Send a request:

```bash
$ curl -v "console.higress.io/get?k1=v11&k1=v12&k2=v2"

# HTTPBin response
{
 "args": {
 "k2-new": "v2-new",
 "k3": [
 "v31-get",
 "v32"
 ],
 "k4": "v31-get"
 },
 ...
 "url": "http://foo.bar.com/get?k2-new=v2-new&k3=v31-get&k3=v32&k4=v31-get"
}
```

**Transform the request body**

```text
reqRules:
- operate: remove
 body:
 - key: a1
- operate: rename
 body:
 - oldKey: a2
 newKey: a2-new
- operate: replace
 body:
 - key: a3
 newValue: t3-new
 value_type: string
- operate: add
 body:
 - key: a1-new
 value: t1-new
 value_type: string
- operate: append
 body:
 - key: a1-new
 appendValue: t1-$1-append
 value_type: string
 host_pattern: ^(.*)\.com$
- operate: map
 body:
 - fromKey: a1-new
 toKey: a4
- operate: dedupe
 body:
 - key: a4
 strategy: RETAIN_FIRST
```

Send a request:

- **Content-Type: application/json**

  ```bash
  $ curl -v -x POST console.higress.io/post -H 'host: foo.bar.com' \
  -H 'Content-Type: application/json' -d '{"a1":"t1","a2":"t2","a3":"t3"}'

  # HTTPBin response
  {
   ...
   "headers": {
   ...
   "Content-Type": "application/json",
   ...
   },
   "json": {
   "a1-new": [
   "t1-new",
   "t1-foo.bar-append"
   ],
   "a2-new": "t2",
   "a3": "t3-new",
   "a4": "t1-new"
   },
   ...
  }
  ```

- **Content-Type: application/x-www-form-urlencoded**

  ```bash
  $ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \
  -d 'a1=t1&a2=t2&a3=t3'

  # HTTPBin response
  {
   ...
   "form": {
   "a1-new": [
   "t1-new",
   "t1-foo.bar-append"
   ],
   "a2-new": "t2",
   "a3": "t3-new",
   "a4": "t1-new"
   },
   "headers": {
   ...
   "Content-Type": "application/x-www-form-urlencoded",
   ...
   },
   ...
  }
  ```

- **Content-Type: multipart/form-data**

  ```bash
  $ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \
  -F a1=t1 -F a2=t2 -F a3=t3

  # HTTPBin response
  {
   ...
   "form": {
   "a1-new": [
   "t1-new",
   "t1-foo.bar-append"
   ],
   "a2-new": "t2",
   "a3": "t3-new",
   "a4": "t1-new"
   },
   "headers": {
   ...
   "Content-Type": "multipart/form-data; boundary=------------------------
  1118b3fab5afbc4e",
   ...
   },
   ...
  }
  ```

**Response Transformer**

Similar to Request Transformer, this section provides only the usage notes for converting JSON-formatted request/response bodies.

**key nesting with**  **`.`**

1. In most cases, a dot ( `.` ) in the specified key indicates nesting, as shown in the following code:

   ```text
   respRules:
   - operate: add
    body:
    - key: foo.bar
    value: value
   ```

   ```bash
   $ curl -v console.higress.io/get

   # HTTPBin response
   {
    ...
    "foo": {
    "bar": "value"
    },
    ...
   }
   ```

2. When the dot ( `.` ) in key is escaped with  `\.` , it indicates a non-nesting structure, as shown in the following code:

   > **Note**
   >
   > When a string is enclosed in double quotation marks, use \\\\. to escape the dot.

   ```text
   respRules:
   - operate: add
    body:
    - key: foo\.bar
    value: value
   ```

   ```bash
   $ curl -v console.higress.io/get

   # HTTPBin response
   {
    ...
    "foo.bar": "value",
    ...
   }
   ```

**Access the array element**  **`.index`**

You can use the array subscript array.index to access array elements. The subscript starts from 0:

```json
{
 "users": [
 {
 "123": { "name": "zhangsan", "age": 18 }
 },
 {
 "456": { "name": "lisi", "age": 19 }
 }
 ]
}
```

1. Remove the first element from  `users` :

   ```text
   reqRules:
   - operate: remove
    body:
    - key: users.0
   ```

   ```bash
   $ curl -v -X POST console.higress.io/post \
   -H 'Content-Type: application/json' \
   -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'

   # HTTPBin response
   {
    ...
    "json": {
    "users": [
    {
    "456": {
    "name": "lisi"
    }
    }
    ]
    },
    ...
   }
   ```

2. Rename the key of the first element in  `users`  from  `123`  to  `msg` :

   ```text
   reqRules:
   - operate: rename
    body:
    - oldKey: users.0.123
    newKey: users.0.first
   ```

   ```bash
   $ curl -v -X POST console.higress.io/post \
   -H 'Content-Type: application/json' \
   -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'


   # HTTPBin response
   {
    ...
    "json": {
    "users": [
    {
    "msg": {
    "name": "zhangsan"
    }
    },
    {
    "456": {
    "name": "lisi"
    }
    }
    ]
    },
    ...
   }
   ```

**Traverse array elements with**  **`.#`**

You can use  `array.#`  to traverse array elements:

> **Note**
>
> This operation is currently supported only in replace operations. Do not use it in other transformations, as it may lead to unpredictable results.

```json
{
 "users": [
 {
 "name": "zhangsan",
 "age": 18
 },
 {
 "name": "lisi",
 "age": 19
 }
 ]
}
```

```text
reqRules:
- operate: replace
 body:
 - key: users.#.age
 newValue: 20
```

```bash
$ curl -v -X POST console.higress.io/post \
-H 'Content-Type: application/json' \
-d '{"users":[{"name":"zhangsan","age":18},{"name":"lisi","age":19}]}'


# HTTPBin response
{
 ...
 "json": {
 "users": [
 {
 "age": "20",
 "name": "zhangsan"
 },
 {
 "age": "20",
 "name": "lisi"
 }
 ]
 },
 ...
}
```

<a id="section-3-6-6-2"></a>

#### 3.6.6.2. frontend-gray

The frontend-gray plug-in helps you implement canary release for your frontend users. This plug-in supports A/B tests and ensures system stability during releases and O&M based on grayscale, monitoring, and rollback policies. This topic describes how to configure the frontend-gray plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `450` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>grayKey</code> | string | No | - | The unique identifier for a user. It can be from a cookie or a request header, such as <code> userid </code>. If this field is not specified, the system uses <code>rules[].grayT</code> <code>agKey </code> and <code>rules[].grayT</code> <code>agValue </code> to filter canary release rules. |
| <code>graySubKey</code> | string | No | - | The user ID may be in the JSON format, such as <code>userInfo:{</code><br><code>userCode:"001"</code><code>} </code>. In this example, the value of <code>graySubKey</code> is <code> userCode </code>. |
| <code>rules</code> | array of object | Yes | - | User-defined canary release rules to adapt to different canary release scenarios. |
| <code>rewrite</code> | object | Yes | - | The rewrite configuration.This parameter is typically used for Object Storage Service (OSS) and CDN front ends. |
| <code>baseDeployment</code> | object | No | - | The baseline rule configuration. |
| <code>grayDeployment</code><br><code>s</code> | array of object | No | - | The rule for canary release to take effect and the effective release version. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/39d1a0e6a35640aa61d3b468c2db1113.png)

The following table describes the fields in  `rules` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>name</code> | string | Yes | - | The rule name.This field takes effect together with <code>deploy.gray[]</code><code>.name </code>. |
| <code>grayKeyValue</code> | array of string | No | - | A whitelist of user IDs. |
| <code>grayTagKey</code> | string | No | - | The tag key that is used to categorize users.The tag key comes from cookies. |
| <code>grayTagValue</code> | array of string | No | - | The tag value that is used to categorize users.The tag value comes from cookies. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/a62059827ae4a1bf50db1eb2c91ef093.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c24101132a823796bec781f1c6cd7705.png)

The following table describes the fields in  `rewrite` :

`indexRouting`  (home page rewriting) and  `fileRouting`  (file rewriting) are essentially prefix matching. For example,  `/app1` :  `/mfe/app1/{version}/index.html`  indicates that a request prefixed with /app1 is routed to the  `/mfe/app1/{version}/index.html`  page, where  `{version}`  represents a version number and is dynamically replaced by  `baseDeployment.version`  or  `grayDeployments[].version`  during execution.

`{version}`  is a reserved field that indicates the frontend version. This field is dynamically replaced by  `baseDeployment.version`  or  `grayDeployments[].version`  during execution.

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>host</code> | string | No | - | The host address. For OSS, set this field to a VPC endpoint. |
| <code>notFoundUri</code> | string | No | - | The 404 page configuration. |
| <code>indexRouting</code> | map of string to string | No | - | The routing rule that is used to rewrite the home page. Each key specifies a home page route path, and each value specifies a destination file to redirect the home page. For example, a key of <code> /app1 </code> corresponds to a value of<code>/mfe/app1/{ve</code><br><code>rsion}/index.ht</code> <code>ml </code>. If the effective version is <code> 0.0.1 </code> and the access path is <code> /app1 </code>, you are redirected to<code>/mfe/app1/0.0</code><br><code>.1/index.html</code>. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/5410b244238fc9e4bfaac080ad11b9e2.png)

<table>
  <tr>
    <td><code>fileRouting</code></td>
    <td>map of string to string</td>
    <td>No</td>
    <td>-</td>
    <td>The routing rule that is used to rewrite a resource file.Each key specifies a resource access path, and each value specifies a destination file to redirect the request. For example, a key of <code> /app1 </code> corresponds to a value of<code>/mfe/app1/{ve</code> <code>rsion} </code>. If the effective version is <code> 0.0.1 </code> and the access path is<code>/app1/js/a.js</code><code> </code>, you are redirected to<code>/mfe/app1/0.0</code><code>.1/js/a.js </code>.</td>
  </tr>
</table>

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/23258c23a4ab4995a4ed07618669b03e.png)

The following table describes the fields in  `baseDeployment` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>version</code> | string | Yes | - | The baseline version. |

The following table describes the fields in  `grayDeployments` .

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| <code>version</code> | string | Yes | - | The version to be used. If the rule is hit, this version is used. For non-CDN deployments, add <code> x-</code><code>higress-tag </code> to the header. |
| <code>backendVersion</code> | string | Yes | - | The backend canary release version. <code> x-mse-</code><code>tag </code> is added to the header of the <code>XHR/Fetch</code> request that is sent to the backend. |
| <code>name</code> | string | Yes | - | The rule name.This field takes effect together with <code>rules[].name</code><code> </code>. |
| <code>enabled</code> | boolean | Yes | - | Specifies whether to enable the current rule. |

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c4c2733cd175cead81cd8d194b31ee62.png)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/04c1fe2b24efe411f141d4dceaf50010.png)

**Configuration examples**

**Basic configurations**

```text
grayKey: userid
rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

`userid`  specifies user IDs in the cookie. The  `beta-user`  rule is configured in the current canary release rule.

When the following conditions are met, the version specified in  `version: gray`  is used:

- `userid`  is  `00000002`  or  `00000003` .

- `level`  is  `level3`  or  `level5` .

Otherwise, the version specified in  `version: base`  is used.

**Store user information in JSON**

```text
grayKey: appInfo
graySubKey: userId
rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

The cookie contains  `appInfo`  data in the JSON format, in which  `userId`  is contained as the only identifier. The  `beta-user`  rule is configured in the current canary release rule. When the following conditions are met, the version specified in  `version: gray`  is used:

- `userid`  is  `00000002`  or  `00000003` .

- `level`  is  `level3`  or  `level5` .

Otherwise, the version specified in  `version: base`  is used.

**Configure rewrite configurations**

> **Note**
>
> These configurations are generally used in CDN scenarios.

```text
grayKey: userid
rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
rewrite:
 host: frontend-gray.oss-cn-shanghai-internal.aliyuncs.com
 notFoundUri: /mfe/app1/dev/404.html
 indexRouting:
 /app1: '/mfe/app1/{version}/index.html'
 /: '/mfe/app1/{version}/index.html',
 fileRouting:
 /: '/mfe/app1/{version}'
 /app1/: '/mfe/app1/{version}'
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

`{version}`  is dynamically replaced with the actual version during execution.

**indexRouting: home page rewriting**

Access requests to  `/app1` ,  `/app123` ,  `/app1/index.html` ,  `/app1/xxx` , and  `/xxxx`  are routed to '/mfe/app1/{version}/index.html'.

**fileRouting: file rewriting**

The following file mappings take effect:

- `/js/a.js`  =>  `/mfe/app1/v1.0.0/js/a.js`

- `/js/template/a.js`  =>  `/mfe/app1/v1.0.0/js/template/a.js`

- `/app1/js/a.js`  =>  `/mfe/app1/v1.0.0/js/a.js`

- `/app1/js/template/a.js`  =>  `/mfe/app1/v1.0.0/js/template/a.js`

<a id="section-3-6-6-3"></a>

#### 3.6.6.3. custom-response

The custom-response plug-in allows you to configure custom responses, including HTTP status codes, HTTP response headers, and HTTP response bodies. The custom-response plug-in can also be used for mock responses, or used to provide custom responses after a specific HTTP status code is determined. For example, you can use the plug-in to configure a custom response that is returned when a gateway throttling policy is triggered. This topic describes how to configure the custom-response plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `910` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| status_code | number | No | 200 | The custom HTTP status code returned. |
| headers | array of string | No | - | The custom headers in the HTTP response.Separate keys and values with equal signs (<code> = </code>). |
| body | string | No | - | The custom body in the HTTP response. |
| enable_on_status | array of number | No | - | The original status code that is matched to generate a custom response. If you do not specify this field, the system does not determine the original status code. |

**Configuration examples**

**Return a custom response in mock response scenarios**

```text
status_code: 200
headers:
- Content-Type=application/json
- Hello=World
body: "{\"hello\":\"world\"}"
```

The preceding configurations allow the following custom response to be returned:

```text
HTTP/1.1 200 OK
Content-Type: application/json
Hello: World
Content-Length: 17

{"hello":"world"}
```

**Return a custom response when throttling is triggered**

```text
enable_on_status:
- 429
status_code: 302
headers:
- Location=https://example.com
```

When throttling is triggered, the HTTP  `429`  status code is returned in most cases. In this case, the following custom response is returned:

```text
HTTP/1.1 302 Found
Location: https://example.com
```

This way, a browser-based 302 redirection mechanism is implemented to redirect the throttled user to another page, such as a static page uploaded to CDN.

If you want other status codes to be returned when throttling is triggered, configure the required fields by referring to the "Return a custom response in mock response scenarios" section.

<a id="section-3-6-6-4"></a>

#### 3.6.6.4. de-graphql

The de-graphql plug-in maps URIs for query in GraphQL. This way, upstream GraphQL APIs can be accessed as conventional services. This topic describes how to configure the de-graphql plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `430` .

**Parameter configurations**

| Parameter | Description | Default value |
| --- | --- | --- |
| <code>gql</code> | The GraphQL query. | Cannot be left empty |
| <code>endpoint</code> | The query endpoint. | <code>/graphql</code> |
| <code>timeout</code> | The timeout period of a query connection. Unit: milliseconds. | <code>5000</code> |
| <code>domain</code> | The service domain name. This parameter is required if the service source is DNS. | - |

**Use the plug-in**

- Test configurations

```yaml
apiVersion: networking.higress.io/v1
kind: McpBridge
metadata:
 name: default
 namespace: higress-system
spec:
 registries:
 - domain: api.github.com
 name: github
 port: 443
 type: dns
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 annotations:
 higress.io/destination: github.dns
 higress.io/upstream-vhost: "api.github.com"
 higress.io/backend-protocol: HTTPS
 name: github-api
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /api
 pathType: Prefix
---
apiVersion: extensions.higress.io/v1alpha1
kind: WasmPlugin
metadata:
 name: de-graphql-github-api
 namespace: higress-system
spec:
 matchRules:
 - ingress:
 - github-api
 config:
 timeout: 5000
 endpoint: /graphql
 domain: api.github.com
 gql: |
 query ($owner:String!  $name:String!){
 repository(owner:$owner, name:$name) {
 name
 forkCount
 description
 }
 }
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/de-graphql:1.0.0
```

- Test results

```bash
curl "http://localhost/api?owner=alibaba&name=higress" -H "Authorization: Bearer some-token"

{
 "data": {
 "repository": {
 "description": "Next-generation Cloud Native Gateway",
 "forkCount": 149,
 "name": "higress"
 }
 }
}
```

**About GraphQL**

**GraphQL endpoint**

A RESTful API has multiple endpoints, whereas a GraphQL API has only one endpoint.

```text
https://api.github.com/graphql
```

**Communicate with GraphQL**

A GraphQL operation consists of multiple lines of JSON data. Therefore, you can use cURL or any other HTTP-based library. In REST, the HTTP verb varies based on the action to be performed. In GraphQL, a JSON request body is required when a query is executed, and therefore the used HTTP verb is POST. The only exception is an introspective query, which is a simple GET request that queries against an endpoint.

**GraphQL POST request parameters**

A standard GraphQL POST request contains the following parameters:

- HTTP headers added by using Content-Type: application/json

- A request body in the JSON format

- Parameters in the request body, which are passed in the following sections:

  - query: required for document queries

  - variables: optional variables

  - operationName: the optional name of the operation (required when multiple operations are performed)

```json
{
 "query": "{viewer{name}}",
 "operationName": "",
 "variables": {
 "name": "value"
 }
}
```

**Basic parameter types in GraphQL**

- GraphQL parameters fall into the following basic types: String, Int, Float, and Boolean.

- [Type] represents an array. For example, [Int] represents an array of integers.

- Parameter passing:

  - A pair of parentheses is used to define a formal parameter. Note that you must define a type for the parameter.

  - An exclamation mark (!) indicates that the parameter cannot be left empty.

```text
query ($owner : String!, $name : String!) {
 repository(owner: $owner, name: $name) {
 name
 forkCount
 description
 }
}
```

**GraphQL test on GitHub**

You can run cURL commands to perform GraphQL queries. Remember to use a valid JSON request body to send a POST request. A valid request body must contain a string named query.

```bash
curl https://api.github.com/graphql -X POST \
-H "Authorization: bearer <PAT>" \
-d "{\"query\": \"query { viewer { login }}\"}"

{
 "data": {
 "viewer": {
 "login": "2456868764"
 }
 }
}
```

```bash
curl 'https://api.github.com/graphql' -X POST \
-H 'Authorization: bearer <PAT>' \
-d '{"query":"query ($owner: String!, $name: String!) {\n  repository(owner: $owner, name: $name) {\n    name\n    forkCount\n    description\n  }\n}\n","variables":
{"owner":"2456868764","name":"higress"}}'

{
 "data": {
 "repository": {
 "name": "higress",
 "forkCount": 149,
 "description": "Next-generation Cloud Native Gateway"
 }
 }
}
```

**References**

- https://github.com/graphql/graphql-spec

- https://docs.github.com/zh/graphql/guides/forming-calls-with-graphql

- https://github.com/altair-graphql/altair

<a id="section-3-6-6-5"></a>

#### 3.6.6.5. cache-control

The cache-control plug-in can add the  `Expires`  and  `Cache-Control`  headers to responses based on URL file suffixes. This allows browsers to cache files with specific suffixes, such as  `jpg`  and  `png` . This topic describes how to configure the cache-control plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `420` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |
| suffix | string | No. The suffix to match, such as <code> jpg </code> and <code> png </code>.<br>To match multiple suffixes, separate suffixes with a vertical bar (<code> &#124; </code>).Example: <code> png&#124;jpg </code>.<br>If you do not specify this parameter, all suffixes are matched. | - | This field specifies the suffix of files to match. |
| expires | string | Yes. The maximum period of time to cache files for.<br>If you specify digits as the value, the unit is seconds. For example, to specify a period of 1 hour, you must enter 3600.<br>epoch and max are supported and carry the same semantics as in nginx. | - | This field specifies the maximum period of time to cache files for. |

**Configuration examples**

1. Cache files whose suffix is  `jpg` ,  `png` , or  `jpeg`  for one hour:

   ```text
   suffix: jpg|png|jpeg
   expires: 3600
   ```

   Based on the preceding configuration, the  `Expires`  and  `Cache-Control`  headers will be added to responses to the following requests to cache matched files for one hour:

   ```bash
   curl http://example.com/test.png
   curl http://exmaple.com/test.jpg
   ```

2. Cache all files until  `Thu, 31 Dec 2037 23:55:55 GMT` :

   ```text
   expires: max
   ```

<a id="section-3-6-7"></a>

### 3.6.7. Observability

<a id="section-3-6-7-1"></a>

#### 3.6.7.1. geo-ip

The geo-ip plug-in can obtain user geographical locations based on user IP addresses and then pass the locations to subsequent plug-ins as a request attribute or header. This topic describes how to configure the geo-ip plug-in.

**Running attributes**

Plug-in execution stage:  `Authentication` . Plug-in execution priority:  `440` .

**Fields**

| Field | Data type | Required | Default value | Description |
| --- | --- | --- | --- | --- |

<table>
  <tr>
    <td>ip_protocol</td>
    <td>string</td>
    <td>No</td>
    <td>ipv4</td>
    <td>The IP protocol to be used. Valid values: ipv4 and ipv6.<br>• If ipv4 is specified, only the geographical information of IPv4 users is collected and passed to subsequent plug-ins. Requests from IPv6 users skip the plug-in.<br>• Support for ipv6 is under development.When ipv6 is supported and specified, only the geographical information of IPv6 users is collected and passed to subsequent plug-ins. Requests from IPv4 users skip the plug-in.<br>Note<br>The current processing method still skips the plug-in, and requests are processed by the subsequent plug-ins.</td>
  </tr>
  <tr>
    <td>ip_source_type</td>
    <td>string</td>
    <td>No</td>
    <td>origin-source</td>
    <td>The source type. Valid values:<br>• <code> origin-source </code>: indicates the peer-end socket IP address.<br>• <code> header </code>: obtains an IP address from the header.</td>
  </tr>
  <tr>
    <td>ip_header_nam e</td>
    <td>string</td>
    <td>No</td>
    <td>x-forwarded-for</td>
    <td>The header from which an IP address is obtained. This field takes effect when <code> ip_source_type </code> is set to <code> header </code>.</td>
  </tr>
</table>

**Configuration examples**

```text
ip_protocol: ipv4
ip_source_type: header
ip_header_name: X-Real-Ip
```

**How to use properties**

You can call proxywasm.SetProperty() in the geo-ip plug-in to set country, city, province, and isp as request properties. This way, the plug-in can call proxywasm.GetProperty() to obtain the geographical information corresponding to user IP addresses.

**Carry user geographical locations by combining the AI prompt decorator plug-in and the geo-ip plug-in**

If you want to prepend or append user geographical locations in LLM requests, you must keep both the geo-ip plug-in and the AI prompt decorator plug-in enabled. In addition, you must ensure that the geo-ip plug-in has a higher priority than the ai-prompt-decorator plug-in in the same processing stage. This way, the geo-ip plug-in calculates the user's geographical location based on the user IP address, and then passes the location information to subsequent plug-ins by using a request attribute. For example, in the default phase, the priority of the geo-ip plug-in is 1000, and that of the ai-prompt-decorator plug-in is 500.

Configuration example of a geo-ip plug-in:

```text
ipProtocal: "ipv4"
```

Configuration example of an ai-prompt-decorator plug-in:

```text
prepend:
- role: system
 content: "The current geographical location of the user is: country:${geo-country}, province:${geo-province}, city:${geo-city}"
append:
- role: user
 content: "Each time you answer a question, try to ask a rhetorical question."
```

Use the preceding configurations to initiate a request.

```bash
curl http://localhost/test \
-H "content-type: application/json" \
-H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \
-d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "user",
 "content": "What is the weather like today?"
 }
 ]
}'
```

The following code shows a sample processed request:

```bash
curl http://localhost/test \
-H "content-type: application/json" \
-H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \
-d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "system",
 content: "The current geographical location of the user is: country: China, province: 
Beijing, city: Beijing"
 },
 {
 "role": "user",
 "content": "What is the weather like today?"
 },
 {
 "role": "user",
 content: "Each time you answer a question, try to ask a rhetorical question."
 }
 ]
}'
```

<a id="section-3-6-7-2"></a>

#### 3.6.7.2. log-request-response

This topic describes how to configure the log-request-response plug-in.

This plug-in is used to add the following information to the access logs of Higress:

- HTTP request header (added  `%FILTER_STATE(wasm.log-request-headers:PLAIN)%` ).

- Request body of POST, PUT, and PATCH requests (added  `%FILTER_STATE(wasm.log-request-body:PLAIN)%` ).

- Response header (added  `%FILTER_STATE(wasm.log-response-headers:PLAIN)%` ).

- Response body (added  `%FILTER_STATE(wasm.log-response-body:PLAIN)%` ).

**Parameter configurations**

When you configure the log-request-response plug-in in the Higress console, use the following structured YAML configuration:

```text
# Request-related configuration: # Request header configuration: # Whether to record request headers (default: false; enabled: true) # Request body configuration: # Whether to record the request body (default: false; enabled: true) # Maximum size of records in bytes (default: 10 KB; maxSize: 10240) # Content type of the request body to be recorded (common content types are included by default. contentTypes:- application/json)
      - application/xml
      - application/x-www-form-urlencoded
      - text/plain

# Response-related configuration: # Response header configuration: # Whether to record response headers (default: false; enabled: true) # Response body configuration: # Whether to record the response body (default: false; enabled: true) # Maximum size of records in bytes (default: 10 KB; maxSize: 10240) # Content type of the response body to be recorded (common content types are included by default. contentTypes:- application/json)
      - application/xml
      - text/plain
      - text/html
```

**How the plug-in works**

- When a request is processed, the plug-in determines whether to record the request headers and request body based on the configuration.

- The request body is recorded only if the request method is POST, PUT, or PATCH and the content type is in the configured  `request.body.contentTypes`  list.

- When a response is processed, the plug-in determines whether to record the response headers and response body based on the configuration.

- The response body is recorded only if the content type of the response is in the configured  `response.body.contentTypes`  list.

- All records are limited to the size specified by the configured  `maxSize` .

- The plug-in processes both request and response bodies in streaming mode, without blocking or modifying the transmission of the original content.

- The recorded content is stored in the filter state of Envoy and can be obtained based on the access log configuration.

**Access log configuration**

To display the filter state data added by the plug-in in the access logs of Higress, you need to modify the access log configuration of Higress. Modify the ConfigMap:

```bash
kubectl edit cm -n higress-system higress-config
```

Add the following content to the  `format`  field under  `envoyAccessLogService.config.accessLog` :

```json
{"request_headers": "%FILTER_STATE(wasm.log-request-headers:PLAIN)%","request_body": "%
FILTER_STATE(wasm.log-request-body:PLAIN)%","response_headers": 
"%FILTER_STATE(wasm.log-response-headers:PLAIN)%","response_body": 
"%FILTER_STATE(wasm.log-response-body:PLAIN)%"}
```

The following code shows a complete access log configuration (add it to the existing configuration):

```text
mesh:accessLogFile: "/dev/stdout"accessLogFormat: |
    {
      "authority": "%REQ(:AUTHORITY)%",
      "bytes_received": "%BYTES_RECEIVED%",
      "bytes_sent": "%BYTES_SENT%",
      "downstream_local_address": "%DOWNSTREAM_LOCAL_ADDRESS%",
      "downstream_remote_address": "%DOWNSTREAM_REMOTE_ADDRESS%",
      "duration": "%DURATION%",
      "method": "%REQ(:METHOD)%",
      "path": "%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%",
      "protocol": "%PROTOCOL%",
      "request_id": "%REQ(X-REQUEST-ID)%",
      "requested_server_name": "%REQUESTED_SERVER_NAME%",
      "response_code": "%RESPONSE_CODE%",
      "response_flags": "%RESPONSE_FLAGS%",
      "route_name": "%ROUTE_NAME%",
      "start_time": "%START_TIME%",
      "trace_id": "%REQ(X-B3-TRACEID)%",
      "upstream_cluster": "%UPSTREAM_CLUSTER%",
      "upstream_host": "%UPSTREAM_HOST%",
      "upstream_local_address": "%UPSTREAM_LOCAL_ADDRESS%",
      "upstream_service_time": "%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%",
      "upstream_transport_failure_reason": "%UPSTREAM_TRANSPORT_FAILURE_REASON%",
      "user_agent": "%REQ(USER-AGENT)%",
      "x_forwarded_for": "%REQ(X-FORWARDED-FOR)%",
      "request_headers": "%FILTER_STATE(wasm.log-request-headers:PLAIN)%",
      "request_body": "%FILTER_STATE(wasm.log-request-body:PLAIN)%",
      "response_headers": "%FILTER_STATE(wasm.log-response-headers:PLAIN)%",
      "response_body": "%FILTER_STATE(wasm.log-response-body:PLAIN)%"
    }
```

**Log output example**

After the configuration is complete, the access logs of Higress contain the following extra fields (depending on the configuration options you enabled):

```json
{"authority": "example.com","method": "POST","path": "/api/users","response_code": 200,
"request_headers": "
{\"host\":\"example.com\",\"path\":\"/api/users\",\"method\":\"POST\",\"content-type\":
\"application/json\"}","request_body": "{\"name\":\"Test user 
\",\"email\":\"test@example.com\"}","response_headers": "{\"content-
type\":\"application/json\",\"status\":\"200\"}","response_body": "
{\"id\":123,\"status\":\"success\"}"}
```

**Usage notes**

- All log record options are disabled by default and need to be enabled to record the corresponding content.

- For large request or response bodies, the size of recorded data can be limited by using the  `request.body.maxSize`  or  `response.body.maxSize`  parameter to avoid excessively large logs.

- The plug-in processes the request body and response body in streaming mode without affecting the original content.

- The content of request bodies is recorded only for POST, PUT, and PATCH requests of the specified content type.

- The content of response bodies is recorded only for responses of the specified content type.

- Make sure that the plug-in is properly configured to avoid recording sensitive information to logs.

<a id="section-3-7"></a>

## 3.7. Certificate management

<a id="section-3-7-1"></a>

### 3.7.1. Create a certificate

The certificate management feature allows you to upload a certificate to a cloud-native gateway. After a successful upload, when you access the gateway over HTTPS, the gateway returns the corresponding certificate based on the domain name that you requested, thereby completing the TLS handshake.

**Create a certificate**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Certificate**.

5. On the **Certificate Management** page, click **Create Certificate**. In the Create Certificate panel, configure the parameters and click **Determine**.

   | Parameter | Description |
   | --- | --- |
   | Certificate Name | The name of the certificate. The name can be up to 15 characters in length. |
   | Certificate Type | Only <strong>Server Certificate</strong> is supported. |
   | Certificate File | You can enter the content of the certificate file in the text box or click <strong>Upload Certificate</strong> to read the content from a file. |
   | Certificate Key | You can enter the content of the certificate key in the text box or click <strong>Upload Key</strong> to read the content from a file. |

<a id="section-3-7-2"></a>

### 3.7.2. Manage certificates

The certificate management feature allows you to update, delete, and view certificate details. This enables you to conveniently manage the full lifecycle of certificates.

**View certificate details**

After a certificate is uploaded, you can view the details of the certificate.

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Certificate**.

5. On the **Certificate Management** page, click the name of a certificate to view the certificate details:

   - **Basic Information**: You can view the following information: **Certificate ID**, **Serial Number**, **Certificate Name**, **Algorithm**, **Certificate Type**, **Private Key Length**, **Time of Issue**, and **Expiration Time**.

   - **Issuer Information**: You can view the following information: **Name of Issuer** and **Issuer Department**.

     ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/3cbfd6dc7e58fa73744162e50cd0de27.jpeg)

**Update a certificate**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Certificate**.

5. On the **Certificate Management** page, find the certificate that you want to manage and click **Update** in the **Operation** column.

6. In the **Update Certificate** panel, enter the updated certificate information and click **Determine**.

**Delete a certificate**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Certificate**.

5. On the **Certificate Management** page, find the certificate that you want to manage and click **Delete** in the **Operation** column.

6. In the **Alert** message, click **Determine**.

**Access the gateway**

After you upload the certificate, use the domain name corresponding to the certificate and an incorrect domain name to access the gateway. Sample results:

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/e49f3eff033c9698c4bacca9b066cbc3.jpeg)

![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/2767215a84004d911fe6d9b97ca7bfc3.jpeg)

The results show that only the correct domain name can be used to access the gateway and obtain the corresponding certificate from the gateway, thereby achieving a successful handshake.

<a id="section-3-8"></a>

## 3.8. Domain name management

<a id="section-3-8-1"></a>

### 3.8.1. Create a domain name

Cloud-native Gateway supports multi-domain name management that allows you to manage protocols, certificates, and route configurations of different domain names.

**Prerequisites**

An Internet Content Provider (ICP) number is obtained for the domain name.

> **Note**
>
> If you want to associate independent domain names with Cloud-native Gateway instances in a region in the Chinese mainland, you must apply for ICP numbers in the Alibaba Cloud ICP Filing system or add Alibaba Cloud as a service provider to the ICP filing information of the domain names. If you want to associate independent domain names with Cloud-native Gateway instances in a region outside the Chinese mainland, ICP numbers are not required.

**Procedure**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Domain Name**.

5. On the Domain Name Management page, click **Associated Domain Name**. In the **Associated Domain Name** panel, configure the parameters and click **Determine**.

   | Parameter | Description |
   | --- | --- |
   | Domain Name | Enter a domain name, such as <code> hello.com </code>.You can independently manage the protocols and certificates of the domain name. Route configurations are isolated based on the domain name. |
   | Agreement | Select <strong>HTTP</strong> or <strong>HTTPS</strong> from the drop-down list.The supported port number varies based on the protocol:<br>• <strong>HTTP</strong>: Port 80 is supported.<br>• <strong>HTTPS</strong>: Port 443 is supported. |
   | Server Certificate | Note<br>This parameter is required if you set the <strong>Agreement</strong> parameter to <strong>HTTPS</strong>.<br>Select the SSL certificate created by the certificate management service. |
   | Enable two-way authentication | Specifies whether to enable mutual authentication. |
   | CA Certificate | Note<br>This parameter is required only when mutual authentication is enabled.<br>Select a CA certificate. If no CA certificate is available, create one. For more information, see Certificate management. |
   | Add request header fields to get client certificate holder (Subject) information | Note<br>This parameter is required only when mutual authentication is enabled.<br>You can select or clear this parameter. If you select this parameter, the system automatically specifies the custom request header based on the CA certificate. |
   | Add a Request Header Field to Get Client Certificate Issuer (Issuer) Information | Note<br>This parameter is required only when mutual authentication is enabled.<br>You can select or clear this parameter. If you select this parameter, the system automatically specifies the custom request header based on the CA certificate. |

**Verify the results**

The system automatically configures a routing rule for the path of the domain name that you associated with the Cloud-native Gateway instance.

- If the resolution of your domain name takes effect, you can verify the result by directly accessing a website that meets the configured routing rule from a browser.

- If no Domain Name System (DNS) record is configured for your domain name, you can run one of the following commands to verify the result based on the supported protocol. In the following examples, the associated domain name is  `hello.com` . Replace {Public IP address} in the following URLs with your public IP address:

  - HTTP:

    ```bash
    curl http://hello.com --resolve "hello.com:80:{Public IP address}"
    ```

  - HTTPS:

    ```bash
    curl -v -k https://hello.com --resolve "hello.com:443:{Public IP address}" --cacertmy-cert.pem
    ```

<a id="section-3-8-2"></a>

### 3.8.2. Manage domain names

After you create a domain name, you can modify or delete the domain name, and view its details.

**View the details of domain name**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Domain Name**.

5. On the **Domain Name Management** page, find the domain name that you want to manage and click its name to go to the **Domain Name Details** page. On the Domain Name Details page, you can view the information about the domain name on the following tabs: **Basic information**, **Plugin configuration**, and **Associated Routing**.

   - On the **Basic information** tab, you can view the settings of **Domain Name** and **Agreement**.

   - On the **Plugin configuration** tab, you can manage the plug-ins that are bound to the current domain name. You can click **AddPlugin** to bind a plug-in to the domain name. For more information, see Create a plug-in.

     > **Note**
     >
     > On the domain name list page, you can click **Plugin Configuration** in the **Operation** column to go to the **Plugin configuration** tab.

   - On the **Associated Routing** tab, you can view the information about the routes that are associated with the current domain name. You can click the name of a route or service to go to the details page of the route or service.

**Modify a domain name**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Domain Name**.

5. On the **Domain Name Management** page, find the domain name that you want to manage and click **Edit** in the **Operation** column.

6. In the **Modify Domain Name** panel, modify the protocol or certificate and click **Determine**.

**Delete a domain name**

1. Log in to the Cloud-native Gateway console.

2. In the left navigation pane, go to **Cloud Native Gateway > instance list**.

3. On the **Gateway instance** page, click the ID of the target gateway or click **Details** in the **Operation** column of the gateway.

4. In the left-side navigation pane, click **Domain Name**.

5. On the **Domain Name Management** page, find the domain name that you want to manage and click **Delete** in the **Operation** column.

6. In the **Alert** message, click **Determine**.

<a id="section-3-9"></a>

## 3.9. Observation and analysis

<a id="section-3-9-1"></a>

### 3.9.1. View gateway metrics

The cloud-native gateway is integrated with the monitoring service to enable comprehensive observability of core runtime metrics of the gateway. This topic describes how to view gateway metrics after the monitoring service is enabled.

**Prerequisites**

The **Monitoring Plugin** feature is enabled on the **Overview** page of the cloud-native gateway.

**Procedure**

1. In the top navigation bar, choose **Products > Middleware > Cloud-native Observability > Prometheus Monitoring 2.0** to log in to the Prometheus Monitoring 2.0 console.

2. In the left-side navigation pane, click **Access Management**. On the **Integrated Environments** tab, search for the environment where the gateway resides.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/26c8cc0072309933e90ab58f44cd7114.jpeg)

3. Click the environment name to go to the **Details** page.

4. On the **Details** page, click **Self-Monitoring > Targets**. You can find **higress-gateway-metrics** in the right-side list.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/c826ecf09c970ed3155cf293d911b3fd.jpeg)

5. Expand **higress-gateway-metrics** and click the endpoint in the Endpoint column to go to the details page.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/92180ca9f3679072143939861fa3f6eb.jpeg)

   The details page displays all metrics.

   ![](en-cloud-native-gateway-user-guide-v3.18.6-20260630.assets/993744808f0e18fb03e99010ae4ce949.jpeg)

<a id="section-3-10"></a>

## 3.10. Nginx Ingress migration

Nginx Ingress migration is a one-stop automated migration tool provided by the cloud-native API gateway platform. It is designed to help users smoothly and securely migrate traffic routing rules (Ingress resources) based on the Nginx Ingress Controller in their existing Kubernetes clusters to the next-generation high-performance gateway, the Higress gateway. This topic describes how to create an Nginx Ingress migration task.

**Create a migration task**

1. Log in to the Cloud-native Gateway console.

2. In the left-side navigation pane, choose **Cloud-native gateway > Nginx Ingress Migration**.

3. On the **Nginx Ingress Migration** page, click **Create a migration task**.

4. Under **Confirm migration scope**, set the parameters as follows and click **Create and start evaluation**.

   | Parameter | Description |
   | --- | --- |
   | Task name | Specify a name for the migration task. |
   | K8s cluster | Select the Kubernetes cluster that contains the Nginx Ingress resources to be migrated. |
   | IngressClass | Specify the IngressClass of the Ingress resources to be migrated. |
   | Namespace | Specify the Kubernetes namespace of the Ingress resources to be migrated.<br>Note<br>If this parameter is left empty, all namespaces are selected. |

5. Under **Compatibility evaluation**, click **Start evaluation**. After the evaluation succeeds, click **Next step: Configure migration rules**.

   > **Note**
   >
   > - If the evaluation fails, click **Re-evaluation**.
   >
   > - The evaluation results mainly fall into two categories:
   >
   >   - **There are no blocking issues**: The migration can proceed. This category includes the following three types:
   >
   >     - Fully compatible: natively supported by Higress and can be used directly.
   >
   >     - Partially compatible: The handling strategy is "migrate with risks", meaning it will not be considered a blocking issue. The behavior is as follows: The annotations are retained as is in the Higress Ingress. The parts that API Gateway can recognize will take effect, whereas unsupported parts (such as the AJP protocol or the ewma algorithm) will become invalid. Users need to assess whether this is acceptable based on the  `solution`  and  `risk`  fields in the evaluation report.
   >
   >   - **There are blocking issues**: These issues must be resolved before you proceed with the migration. Blocking issues include the following two types:
   >
   >     - INCOMPATIBLE: explicitly marked as unsupported by Higress in the compatibility database.
   >
   >     - UNKNOWN: No record is found for the annotation in the compatibility database, making it impossible to determine the compatibility. Manual evaluation is required.

6. In **Migration rule configuration**, configure the following parameters and click **Perform migration**.

   | Parameter | Description |
   | --- | --- |
   | Migration mode | • <strong>Migrate to the same cluster</strong>: migrates Ingress resources from one namespace to another within the same Kubernetes cluster.<br>• <strong>Cross-cluster migration</strong>: migrates Ingress resources from one Kubernetes cluster to another.<br>Warning<br>During cross-cluster migration, ensure that the target cluster can access all backend services. Otherwise, the routes will not work properly after the migration. |
   | Target instance | Specify the gateway instance that receives the migrated resources. |
   | Migration scope | Select the range of Ingress resources to be migrated.<br>Note<br>Incompatible and unnecessary annotations are automatically removed during migration. Equivalent replaceable and partially compatible annotations are retained. |
   | Execution mode | • <strong>Incremental migration (skip migrated)</strong>: Only resources that have not been successfully migrated are migrated. If an Ingress resource has already been successfully migrated, it will not be processed again.<br>• <strong>Full coverage (regeneration)</strong>: Regardless of whether an Ingress resource has been migrated before, the system will perform a full rebuild. Existing resources with the same name in the target cluster will be automatically replaced. |

7. In **Traffic switching**, follow the traffic switch guide displayed on the page to change the backend of domain resolution or load balancing from the Server Load Balancer (SLB) instance of the Nginx Ingress Controller to the SLB instance of the Higress gateway. After the traffic is switched, click **Complete Migration**.

**More operations**

On the **Nginx Ingress Migration** page, you can quickly search for migration tasks by task name. The list displays **Task name**, **SOURCE cluster ID/name**, **Target instance ID/name**, **Target cluster ID/name**, **Creation time**, and **Task Status**.

Click a task name to jump to its current execution step.
