Alibaba Cloud  
Apsara Stack  
Elastic IP Address  
Developer Guide  
Product Version: V3.18.3  
Document Version: 20241025

**Table of Contents**

- [1.Preparations](#section-1)
    - [1.1. Log on to OpenAPI Explorer](#section-1-1)
    - [1.2. Obtain the information and the endpoint of an API operation](#section-1-2)
    - [1.3. Obtain an AccessKey pair](#section-1-3)
    - [1.4. Obtain an STS AccessKey 3-tuple](#section-1-4)
    - [1.5. Obtain the values of common header parameters](#section-1-5)
    - [1.6. Obtain EIP SDK](#section-1-6)
- [2.Call examples for SDK for Java](#section-2)
    - [2.1. Quick start](#section-2-1)
    - [2.2. Use SDK](#section-2-2)
        - [2.2.1. Install SDK for Java](#section-2-2-1)
        - [2.2.2. Configure authentication credentials](#section-2-2-2)
        - [2.2.3. Configure connection requests](#section-2-2-3)
        - [2.2.4. Initiate a request](#section-2-2-4)
        - [2.2.5. Troubleshooting](#section-2-2-5)
        - [2.2.6. Use CommonRequest to call API operations](#section-2-2-6)
- [3.Call examples for SDK for Python](#section-3)
    - [3.1. Quick start](#section-3-1)
    - [3.2. Use SDK](#section-3-2)
        - [3.2.1. Install SDK for Python](#section-3-2-1)
        - [3.2.2. Configure authentication credentials](#section-3-2-2)
        - [3.2.3. Set HTTPS requests](#section-3-2-3)
        - [3.2.4. Initiate a request](#section-3-2-4)
        - [3.2.5. Handle errors](#section-3-2-5)
        - [3.2.6. Use CommonRequest to call API operations](#section-3-2-6)
- [4.Call examples for SDK for Go](#section-4)
    - [4.1. Quick start](#section-4-1)
    - [4.2. Use SDK](#section-4-2)
        - [4.2.1. Install the core package of SDK for Go](#section-4-2-1)
        - [4.2.2. Configure authentication credentials](#section-4-2-2)
        - [4.2.3. Initiate a request](#section-4-2-3)
        - [4.2.4. Handle errors](#section-4-2-4)
        - [4.2.5. Use CommonRequest to call API operations](#section-4-2-5)
- [5.API reference](#section-5)
    - [5.1. List of operations by function](#section-5-1)
    - [5.2. Make API requests](#section-5-2)
        - [5.2.1. Request syntax](#section-5-2-1)
        - [5.2.2. API authorization](#section-5-2-2)
        - [5.2.3. Signature method guidelines](#section-5-2-3)
    - [5.3. RAM authentication](#section-5-3)
    - [5.4. Common parameters](#section-5-4)
    - [5.5. Elastic IP addresses](#section-5-5)
        - [5.5.1. AllocateEipAddress](#section-5-5-1)
        - [5.5.2. AllocateEipAddressPro](#section-5-5-2)
        - [5.5.3. AssociateEipAddress](#section-5-5-3)
        - [5.5.4. AllocateEipSegmentAddress](#section-5-5-4)
        - [5.5.5. DescribeEipSegment](#section-5-5-5)
        - [5.5.6. ReleaseEipSegmentAddress](#section-5-5-6)
        - [5.5.7. ModifyEipAddressAttribute](#section-5-5-7)
        - [5.5.8. DescribeEipAddresses](#section-5-5-8)
        - [5.5.9. UnassociateEipAddress](#section-5-5-9)
        - [5.5.10. ReleaseEipAddress](#section-5-5-10)
        - [5.5.11. DescribeEipGatewayInfo](#section-5-5-11)
        - [5.5.12. DescribeEipMonitorData](#section-5-5-12)
        - [5.5.13. MoveResourceGroup](#section-5-5-13)
        - [5.5.14. DescribeHighDefinitionMonitorLogAttribute](#section-5-5-14)
- [6.Appendixes](#section-6)
    - [6.1. STS overview](#section-6-1)
        - [6.1.1. What is STS?](#section-6-1-1)
        - [6.1.2. Obtain an STS token](#section-6-1-2)

<a id="section-1"></a>

# 1.Preparations

<a id="section-1-1"></a>

## 1.1. Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

- The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel.

- A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a browser and press the Enter key.

2. Enter your username and password.

   Obtain the username and password from an administrator.

   > **Note**
   >
   > The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
   >
   > - Letters
   >
   > - Digits
   >
   > - Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log on**.

4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations in the following scenarios:

   - The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator.

     <ol type="a">

     <li>

     On the Bind Virtual MFA Device page, bind an MFA device.

     </li>

     <li>

     Re-enter the username and password as in Step 2 and click **Log On**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Enter a six-digit MFA verification code and click **Authenticate**.

     </li>

     </ol>

   - You have enabled MFA and bound an MFA device.

     Enter a six-digit MFA verification code and click **Authenticate**.

     > **Note**
     >
     > For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide**.

5. In the top navigation bar, choose **Products > Application Services > OpenAPI Explorer**.

<a id="section-1-2"></a>

## 1.2. Obtain the information and the endpoint of an API operation

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.

2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI Explorer**.

3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top navigation bar.

   ![](assets/2c46abb9ede40ba27b69fc91474a92c6.jpeg)

4. In the left-side navigation pane, select the cloud service that you want to manage.

5. Select an API version from the **Version** drop-down list.

6. In the API operation list, you can view all API operations of the current version.

7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter on the Parameter tab.

   ![](assets/b048c661554e8741512853a99d6813fa.jpeg)

<a id="section-1-3"></a>

## 1.3. Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string.

You can use RAM or STS to assign an AccessKey pair for authentication.

- An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret.

- An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an AccessKey pair assigned by STS.

The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning**
>
> The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Header | Description |
| --- | --- |
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-\*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For information about how to obtain an organization ID, see the <strong>GetOrganizationList</strong> section in <strong>Apsara Uni-</strong>manager Management Console Developer <strong>Guide</strong>. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For information about how to obtain a resource set ID, see the <strong>ListResourceGroup</strong> section in <strong>Apsara Uni-</strong>manager Management Console Developer <strong>Guide</strong>. |
| x-acs-instanceid | The ID of the instance that you want to manage.If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console.

2. Click the profile picture in the upper-right corner of the page and click **User Information**.

3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

   ![](assets/a0c6c22806c62349a0f9840932305e11.png)

   > **Note**
   >
   > The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Resources > Organizations**.

4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.

5. On the right side of the page that appears, click **Management AccessKey**.

6. In the dialog box that appears, view the AccessKey pair of the organization.

<a id="section-1-4"></a>

## 1.4. Obtain an STS AccessKey 3-tuple

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations in Apsara Stack.

An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS.

**Procedure**

1. Obtain the  `RAM role` .

   <ol type="i">

   <li>

   Log on to the Apsara Uni-manager Management Console.

   </li>

   <li>

   Click the profile picture in the upper-right corner of the page and click **User**

   </li>

   </ol>

   **Information**.

   <ol type="i" start="3">

   <li>

   Click **View Current Role Policy**.

   </li>

   </ol>

   In the **View Policies of Current Role** dialog box, view your  `RAM role` .

2. Obtain the STS AccessKey 3-tuple.

   > **Note**
   >
   > In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.
   >
   > The following section describes the variable parameters:
   >
   > - &lt;yourRegionID>: Replace the parameter with the region ID.
   >
   > - &lt;yourAccessKeyID>: Replace the parameter with your AccessKey ID.
   >
   > - &lt;yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
   >
   > - &lt;yourRoleSessionName>: Replace the parameter with the name of the current session.
   >
   > - &lt;yourRoleArn>: Replace the parameter with your RAM role.
   >
   > - &lt;sts.aliyuns.com>: Replace the parameter with the STS endpoint.

   ```xml
   public static void main(String[] args) {
       // Create and initialize a DefaultAcsClient instance. 
       // Specify the region ID, AccessKey ID, and AccessKey secret.
       DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
   <yourAccessKeyID>", "<yourAccessKeySecret>");
       HttpClientConfig clientConfig = HttpClientConfig.getDefault();
       clientConfig.setIgnoreSSLCerts(true);
       clientConfig.setProtocolType(ProtocolType.HTTPS);
       profile.setHttpClientConfig(clientConfig);
       IAcsClient client = new DefaultAcsClient(profile);
       String assumeRole = callAssumeRole(client);
       if (StringUtils.isEmpty(assumeRole)) return;
       JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
       JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
       // Obtain the STS AccessKey 3-tuple.
       String stsAK = credentials.getString("AccessKeyId");
       String stsSK = credentials.getString("AccessKeySecret");
       String stsToken = credentials.getString("SecurityToken");
   }

   private static String callAssumeRole(IAcsClient client) {
       CommonRequest request = new CommonRequest();
       // Replace "<sts.aliyuns.com>" with the STS endpoint in the sts-
   vpc.${global:region}.${global:internet-domain}.
       request.setSysDomain("<sts.aliyuns.com>");
       request.setSysProduct("Sts");
       request.setSysAction("AssumeRole");
       request.setSysVersion("2015-04-01");
       request.setSysMethod(MethodType.POST);
       request.setHttpContentType(FormatType.FORM);
       // Replace "<yourRoleSessionName>" with the name of the current session.
       request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
       // Replace "<yourRoleArn>" with the RAM role ARN that is obtained in the previousstep.
       request.putQueryParameter("RoleArn", "<yourRoleArn>");
       try {
           CommonResponse response = client.getCommonResponse(request);
           return response.getData();
       } catch (ServerException e) {
           System.out.println(e.getErrCode());
           System.out.println(e.getErrMsg());
       } catch (ClientException e) {
           System.out.println(e.getErrCode());
           System.out.println(e.getErrMsg());
       }
       return null;
   }
   ```

3. Use the STS AccessKey 3-tuple to call an API operation of a cloud service. The following sample code provides an example on how to call the  `DescribeEipAddresses`  operation of Elastic IP Address (EIP).

   > **Note**
   >
   > In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.
   >
   > The following section describes the variable parameters:
   >
   > - &lt;yourRegionID>: Replace the parameter with the region ID.
   >
   > - &lt;yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID.
   >
   > - &lt;yourStsAccessKeySecret>: Replace the parameter with your STS AccessKey secret.
   >
   > - &lt;yourStsToken>. Replace the parameter with your security token.
   >
   > - &lt;yourResourceGroupID>: Replace the parameter with the resource set ID.
   >
   > - &lt;yourOrganizationID>: Replace the parameter with the organization ID.

   ```xml
   public static void main(String[] args) {
       // Replace "<yourRegionID>" with the region ID.
       // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and AccessKey secret of the 3-tuple obtained in the previous step.
       DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
   <yourStsAccesskey>", "<yourStsAccessSecret>");
       HttpClientConfig clientConfig = HttpClientConfig.getDefault();
       clientConfig.setIgnoreSSLCerts(true);
       clientConfig.setProtocolType(ProtocolType.HTTPS);
       profile.setHttpClientConfig(clientConfig);
       IAcsClient client = new DefaultAcsClient(profile);
       CommonRequest request = new CommonRequest();
       request.setSysDomain("vpc.aliyuns.com");
       request.setSysProduct("Vpc");
       request.setSysAction("DescribeEipAddresses");
       request.setSysVersion("2016-04-28");
       request.setSysMethod(MethodType.POST);
       request.setHttpContentType(FormatType.FORM);
       // Replace "<yourRegionID>" with the region ID.
       request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
       // Replace "<yourStsToken>" with the security token of the 3-tuple obtained in the previous step.
       request.putQueryParameter("SecurityToken", "<yourStsToken>");
       // Optional. Replace the parameter with the resource set ID.
       // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
       // Required. Replace the parameter with the organization ID.
       request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
       try {
           CommonResponse response = client.getCommonResponse(request);
           System.out.println(response.getData());
       } catch (ServerException e) {
           System.out.println(e.getErrCode());
           System.out.println(e.getErrMsg());
       } catch (ClientException e) {
           System.out.println(e.getErrCode());
           System.out.println(e.getErrMsg());
       }
   }
   ```

<a id="section-1-5"></a>

## 1.5. Obtain the values of common header parameters

You must set header parameters when you call API operations. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the return values of some parameters after you call API operations.

**Header parameters**

| Parameter | Description |
| --- | --- |
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Resources** > **Regions**.

4. Click the name of the organization that you want to view.

5. View the region ID in the **Regions** section on the right.

**Obtain an organization ID**

You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the *GetOrganizationList* section in *Apsara Uni-manager Management Console Developer Guide*.

**Obtain a resource set ID**

You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the *ListResourceGroup* section in *Apsara Uni-manager Management Console Developer Guide*.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an elastic IP address (EIP), perform the following steps:

1. Log on to the Apsara Uni-manager Management Console.

2. In the top navigation bar, choose **Products** > **Networking** > **Elastic IP Address**.

3. In the left-side navigation pane, click **Elastic IP Addresses**.

4. View the **IDs and names** of EIPs in the **Elastic IP Addresses** list.

**Response parameters**

The following response parameters are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
| --- | --- |
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

<a id="section-1-6"></a>

## 1.6. Obtain EIP SDK

When you call API operations of a cloud service in Apsara Stack by using the point of presence (POP) gateway, you must use an SDK. This topic describes how to obtain Alibaba Cloud SDK.

**Background information**

To use the features of Elastic IP address (EIP), you must install Virtual Private Cloud (VPC) SDK and the Alibaba Cloud core library. For example, to use VPC SDK for Java, you must download  `aliyun-java-sdk-vpc`  and  `aliyun-java-sdk-core` .

- VPC SDK encapsulates the API released on April 28, 2016. The SDK identifies callers based on their AccessKey pairs and provides features such as automatic signing to allow you to create and manage resources by calling API operations. Alibaba Cloud SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require.

- We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is applicable to all cloud services and is compatible with Apsara Stack.

**Instructions**

Alibaba Cloud SDK supports Java, Python, and Go. You can select an SDK from Alibaba Cloud SDK based on your business requirements.

> **Note**
>
> We recommend that you use an SDK for Java, Python, or Go. If you use SDKs in other programming languages, the SDKs may be incompatible with your system.

<a id="section-2"></a>

# 2.Call examples for SDK for Java

<a id="section-2-1"></a>

## 2.1. Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Java. The features of Elastic IP Address (EIP) are implemented by using VPC SDK.

**Preparations**

- An authorized Apsara Stack account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair.

- Obtain the endpoint of EIP. For more information, see Obtain the information and the endpoint of an API operation.

- Java Development Kit (JDK) 1.8 or later is installed.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage Java projects, import JAR files to the pom.xml file of the projects.

To use the VPC SDK, you must install the SDK core library and VPC SDK. We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.2.0.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

**Use Apsara Stack SDK for Java**

To use Apsara Stack SDK for Java, perform the following steps:

1. Create a DefaultAcsClient instance and initialize the instance.

2. Create an API request and configure the required parameters.

3. Initiate the API request and process the response or exception.

   > **Note**
   >
   > |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
   >
   > The following section describes the variables.
   >
   > - Replace &lt;yourRegionID> with the region ID.
   >
   > - Replace &lt;yourAccessKeyID> with your AccessKey ID.
   >
   > - Replace &lt;yourAccessKeySecret> with your AccessKey secret.
   >
   > - Replace &lt;Product> with the service name.
   >
   > - Replace &lt;Endpoint> with the endpoint of the service.
   >
   > - Replace &lt;readTimeout> with the read timeout period. Unit: milliseconds.
   >
   > - Replace &lt;connectionTimeout> with the connection timeout period. Unit: milliseconds.
   >
   > - Replace &lt;maxRequestsPerHost> with the maximum number of requests for each host.
   >
   > - Replace &lt;maxRequests> with the maximum number of requests.
   >
   > - Replace &lt;http://192.168.XX.XX:33XX> with the proxy IP address and port.

   ```java
    import com.aliyuncs.http.HttpClientConfig;
    import com.aliyuncs.http.ProtocolType;
    import com.aliyuncs.profile.DefaultProfile;
    import com.aliyuncs.DefaultAcsClient;
    import com.aliyuncs.IAcsClient;
    import com.aliyuncs.exceptions.ClientException;
    import com.aliyuncs.exceptions.ServerException;
    import com.aliyuncs.vpc.model.v20160428.*;
    import com.google.gson.Gson;
    public class Main {
        public static void main(String[] args) {
           // Create a DefaultAcsClient instance and initialize it.
           DefaultProfile profile = DefaultProfile.getProfile(
               "<yourRegionID>",          // Replace it with the region ID.
               "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
               "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
           // Specify the endpoint of the current service. 
           profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
           // Configure the request parameters.
           HttpClientConfig clientConfig = HttpClientConfig.getDefault();
           clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate.
           clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the read timeout period. Unit: milliseconds.
           clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Specify the connection timeout period. Unit: milliseconds.
           clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify 
   the maximum number of requests per host.
           clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum number of requests.
           clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the request protocol. Default value: HTTP.
           /* Optional. Specify the IP address and port of the proxy.
           clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
           or
           clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
           */
           profile.setHttpClientConfig(clientConfig);
           IAcsClient client = new DefaultAcsClient(profile);
           // Create an API request and configure the request parameters.
           DescribeEipAddressesRequest request = new DescribeEipAddressesRequest();
           // Set service-related parameters.
           request.setPageSize(10);
           request.setPageNumber(1);
           // Set the organization ID and resource set ID for special header parameters. 
   Resources are isolated.
           request.putHeaderParameter("x-acs-organizationid", "1");
           request.putHeaderParameter("x-acs-resourcegroupid", "11");
           // Initiate the API request and handle the response or exception.
           DescribeEipAddressesResponse response;
           try {
               DescribeEipAddressesResponse response = client.getAcsResponse(request);
               System.out.println(new Gson().toJson(response));
           } catch (ServerException e) {
               e.printStackTrace();
           } catch (ClientException e) {
               System.out.println("ErrCode:" + e.getErrCode());
               System.out.println("ErrMsg:" + e.getErrMsg());
               System.out.println("RequestId:" + e.getRequestId());
           }
        }
    }
   ```

<a id="section-2-2"></a>

## 2.2. Use SDK

<a id="section-2-2-1"></a>

### 2.2.1. Install SDK for Java

This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Java. The features of Elastic IP Address (EIP) are implemented by using VPC SDK.

Alibaba Cloud SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Alibaba Cloud SDK for Java by adding Maven dependencies or downloading Alibaba Cloud SDK.

To use VPC SDK, you must install the core library of Alibaba Cloud SDK for Java and VPC SDK for Java. We recommend that you use the core library version 4.5.17 or later, and use VPC SDK for Java 3.2.0.

To use VPC SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDK.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

<a id="section-2-2-2"></a>

### 2.2.2. Configure authentication credentials

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials.

SDK for Java supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair.

If you want to use your AccessKey pair to access Alibaba Cloud, you must configure the AccessKey pair as a credential when you initialize the client.

> **Note**
>
> Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```text
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace the parameter with the region ID.
    "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
```

> **Note**
>
> In the preceding sample code, replace the variable parameters with the actual information. Remove the angle brackets (<>) in the final code.

<a id="section-2-2-3"></a>

### 2.2.3. Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object.

You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

> **Note**
>
> You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code.
>
> The following list describes the variables:
>
> - &lt;readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds.
>
> - &lt;connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds.
>
> - &lt;maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
>
> - &lt;maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
>
> - &lt;http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

```text
// Obtain the HttpClientConfig object.
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
// Specify whether to ignore certificates.
clientConfig.setIgnoreSSLCerts(true);
// (Optional) Specify the read timeout period. Unit: milliseconds.
clientConfig.setReadTimeoutMillis(<readTimeout>);
// (Optional) Specify the connection timeout period. Unit: milliseconds.
clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);
// (Optional) Specify the maximum number of requests that are supported by each server.
The supported data type is INTEGER.
clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);
// (Optional) Specify the maximum number of requests. The supported data type is INTEGE
R.
clientConfig.setMaxRequests(<maxRequests>);
// (Optional) Specify the protocol type.
clientConfig.setProtocolType(ProtocolType.HTTP);
/** (Optional) Specify whether to configure the proxy based on your business 
requirements. The following code is available:
clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
Or
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
*/
profile.setHttpClientConfig(clientConfig);
```

<a id="section-2-2-4"></a>

### 2.2.4. Initiate a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Java to initiate a request. The features of Elastic IP Address (EIP) are implemented by using VPC SDK.

**Procedure**

1. Create an AcsClient instance.

   ```text
   IAcsClient client = new DefaultAcsClient(profile);
   ```

2. Create a request.

   Name the request in the following format:  `${apiName}Request` . Replace **${apiName}** with the API name, for example, DescribeCustomerGateway.

   When multiple service SDKs are used, different requests may have the same name. You can differentiate the requests based on package names.

   ```text
   DescribeEipAddressesRequest request = new DescribeEipAddressesRequest();
   // Service-related parameters.
   request.setPageSize(10);
   request.setPageNumber(1);
   // Set the organization ID and resource set ID for special header parameters. Resources are isolated.
   request.putHeaderParameter("x-acs-organizationid", "1");
   request.putHeaderParameter("x-acs-resourcegroupid", "");
   ```

3. Initiate the request and handle the response.

   ```java
   DescribeEipAddressesResponse response;
   try {
       DescribeEipAddressesResponse response = client.getAcsResponse(request);
       System.out.println(new Gson().toJson(response));
   } catch (ServerException e) {
       e.printStackTrace();
   } catch (ClientException e) {
       e.printStackTrace();
   }
   ```

   In normal cases, all returned fields are deserialized into the response. You can directly use  `response.getXXX()`  to obtain the response fields.

   ```text
   instanceStatus := response.getStatus();
   ```

   If an exception occurs or you need the original HTTP response, use  `doAction()`  to obtain the original response.

   ```text
   HttpResponse response = client.doAction(request);
   ```

<a id="section-2-2-5"></a>

### 2.2.5. Troubleshooting

If the server or SDK encounters an error when you use SDK for Java, it returns an error response. The error response contains an error code and an error message.

In most cases, you do not need to handle the errors returned by SDK for Java. You need to only handle the errors returned by the server based on error messages.

- `ServerException`  indicates a server error.

- `ClientException`  indicates an SDK error.

For example, when the following error occurs, you can modify the AccessKey ID based on the error message to solve the problem:

```text
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified accesskey is not found.
```

If you want to handle SDK errors, refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, you can submit a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

<a id="section-2-2-6"></a>

### 2.2.6. Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide an SDK, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics:

- Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product.

- Easy and convenient: You can call the latest API without updating the SDK.

- Fast iteration

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters: You can obtain the values for these parameters from the API documents.

- Domain: the endpoint of the service.

- Version: the version number of the API, in the YYYY-MM-DD format.

  You can get the API version from the common parameters in the API documents.

- Operation information: the name of the API operation that you want to call.

  You must obtain the **Action** parameter and specify the API operation by using  `request.setSysAction("<Action>")` .

  For example, if you want to call the DescribeEipAddresses operation, you must use  `request.set_action_name('DescribeEipAddresses')`  to specify the API operation when you initiate a CommonRequest request.

**Example: Call an RPC API operation**

The following code provides an example on how to obtain the information about elastic IP addresses (EIPs) by calling the DescribeEipAddresses operation of EIP. The API of EIP uses RPC.

> **Note**
>
> Replace the variable parameters in the following sample code with the actual
>
> information. Remove the angle brackets (<>) in the final code.
>
> The following section describes the variable parameters:
>
> - Replace &lt;yourRegionID> with the region ID.
>
> - Replace &lt;yourAccessKeyID> with your AccessKey ID.
>
> - Replace &lt;yourAccessKeySecret> with your AccessKey secret.
>
> - Replace &lt;yourSecurityToken> with your security token.
>
> - Replace &lt;yourResourceGroupID> with the resource set ID.
>
> - Replace &lt;yourOrganizationID> with the organization ID.
>
> - Replace &lt;yourInstanceID> with the instance ID.
>
> - Replace &lt;http://192.168.XX.XX:33XX> with the proxy IP address and port.

```java
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.http.HttpClientConfig;
import com.aliyuncs.http.ProtocolType;
public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionUD>",          // Replace the parameter with the region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey 
secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        Specify whether to configure HTTP proxy based on your requirements.
        To configure HTTP proxy, perform the following steps:
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
        Replace the parameter with the proxy IP address and port.
        */
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Replace the parameter with the service domain name.
        request.setSysDomain("vpc.aliyuncs.com");
        request.setSysProduct("Vpc");
        request.setSysVersion("2016-04-28");
        request.setSysAction("DescribeEipAddresses");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Specify the resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Specify the organization ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. 
Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 
Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query an instance.
        /** 
        When you use STS AccessKey credentials to call an API operation, you must add the SecurityToken field in the request parameters.
        Use the following method:
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
        Replace the parameter with the actual token.
        */
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClientException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

<a id="section-3"></a>

# 3.Call examples for SDK for Python

<a id="section-3-1"></a>

## 3.1. Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Python. To use the features of Elastic IP Address (EIP), you must install VPC SDK.

**Preparations**

- An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair.

- Obtain the endpoint of EIP. For more information, see Obtain the information and the endpoint of an API operation.

**Install Apsara Stack SDK for Python**

1. Install the SDK core library.

   - If you use Python 2.x, run the following command:

     ```bash
     pip install aliyun-python-sdk-core
     ```

   - If you use Python 3.x, run the following command to install the core library of Alibaba Cloud SDK:

     ```bash
     pip3 install aliyun-python-sdk-core-v3
     ```

2. Install the SDK.

   The following examples describe how to install VPC SDK for Python:

   - If you use Python 2.x, run the following command to install VPC SDK:

     ```bash
     pip install aliyun-python-sdk-vpc
     ```

   - If you use Python 3.x, run the following command to install VPC SDK:

     ```bash
     pip3 install aliyun-python-sdk-vpc
     ```

**Usage**

The following steps describe how to use VPC SDK for Python:

1. Create a client instance. Before you create a client instance, you must obtain a region ID, an AccessKey ID, and an AccessKey secret.

2. Create an API request and specify the required parameters.

3. Initiate the API request and process the response or exception.

   > **Note**
   >
   > |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
   >
   > The following section describes the variables.
   >
   > - Replace &lt;yourRegionID> with the region ID.
   >
   > - Replace &lt;yourAccessKeyID> with your AccessKey ID.
   >
   > - Replace &lt;yourAccessKeySecret> with your AccessKey secret.
   >
   > - Replace &lt;vpc.aliyuns.com> with the endpoint of the service.

   ```python
   #!/usr/bin/env python
   #coding=utf-8
   from aliyunsdkcore import client
   from aliyunsdkcore.profile import region_provider
   from aliyunsdkvpc.request.v20160428 import DescribeEipAddressesRequest
   # global config
   region_id = '<yourRegionID>' # Specify your region ID.
   access_key = '<yourAccessKeyID>' # Specify the AccessKey ID.
   acces_secret = '<yourAccessKeySecret>' # Specify your AccessKey secret.
   # product config
   product_name = 'Vpc' # Specify the service name.
   endpoint = '<vpc.aliyuns.com>' # Specify the endpoint of the service.
   # create client
   region_provider.modify_point(product_name, region_id, endpoint)
   clt = client.AcsClient(access_key, acces_secret, region_id)
   # setup request
   request = DescribeEipAddressesRequest.DescribeEipAddressesRequest()
   request.set_accept_format('json') # Specify the response format.
   # get response
   response = clt.do_action_with_exception(request)
   print response # If you use Python 3.x, the code here is print (response).
   ```

<a id="section-3-2"></a>

## 3.2. Use SDK

<a id="section-3-2-1"></a>

### 3.2.1. Install SDK for Python

This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Python. The features of Elastic IP Address (EIP) are implemented by using VPC SDK.

Alibaba Cloud SDK for Python supports Python 2.6.x, 2.7.x, and 3.x. You can install Alibaba Cloud SDK for Python by using pip.

> **Note**
>
> To use a service SDK, you must install the core library of Alibaba Cloud SDK
>
> for Python. For example, if you want to use VPC SDK for Python, you must install the core library of Alibaba Cloud SDK for Python and VPC SDK for Python.

- If you use Python 2.x, run the following command to install the core library of Alibaba Cloud SDK:

  ```bash
  pip install aliyun-python-sdk-core
  ```

- If you use Python 3.x, run the following command to install the core library of Alibaba Cloud SDK:

  ```bash
  pip3 install aliyun-python-sdk-core-v3
  ```

The following example describes how to install VPC SDK.

- If you use Python 2.x, run the following command to install VPC SDK:

  ```bash
  pip install aliyun-python-sdk-vpc
  ```

- If you use Python 3.x, run the following command to install VPC SDK:

  ```bash
  pip3 install aliyun-python-sdk-vpc
  ```

<a id="section-3-2-2"></a>

### 3.2.2. Configure authentication credentials

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication.

SDK for Python supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair.

If you want to use your AccessKey pair to access Alibaba Cloud, you must configure the AccessKey pair as a credential when you initialize the client.

> **Important**
>
> Do not disclose any code that may contain your AccessKey pair. For
>
> example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```text
clt = client.AcsClient(secret_id, secret_key, region_id)
```

<a id="section-3-2-3"></a>

### 3.2.3. Set HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS.

You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

> **Note**
>
> The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

OpenSSL support in Python is required for sending HTTPS requests by using SDK for Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later.

Run the  `python -c "import ssl"`  command to check whether your Python environment supports OpenSSL. If the  `ImportError: No module named ssl`  error message does not appear in the command output, OpenSSL is supported.

If OpenSSL is not supported, run the following command to install it:

```bash
pip install pyopenssl# You need to use this command if you use Python 2 in your local environment.
```

> **Note**
>
> If you use Python 3 in your local environment, run the  `pip3 install pyopenssl"` command.

**Set the protocol to HTTP or HTTPS for a request**

The following sample code provides an example on how to set HTTPS as the protocol for a request:

```python
import DescribeInstancesRequest
request = DescribeInstancesRequest()
request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global default protocol**

The following sample code provides an example on how to set a global default protocol:

```python
import aliyunsdkcore.request
aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request. 
```

<a id="section-3-2-4"></a>

### 3.2.4. Initiate a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Python to initiate a request. The features of Elastic IP Address (EIP) are implemented by using VPC SDK.

**Procedure**

1. Import VPC SDK.

   ```python
   from aliyunsdkcore import client
   from aliyunsdkcore.profile import region_provider
   from aliyunsdkvpc.request.v20160428 import DescribeEipAddressesRequest
   ```

2. Create an AcsClient instance.

   ```text
   client.region_provider.modify_point(product_name, region_id, endpoint)
   clt = client.AcsClient(access_key, access_secret, region_id)
   ```

3. Create a request object.

   ```text
   request = DescribeEipAddressesRequest.DescribeEipAddressesRequest()
   request.set_accept_format('json')
   ```

4. Initiate the request and process the response.

   ```text
   response = clt.do_action_with_exception(request)

   print response
   ```

<a id="section-3-2-5"></a>

### 3.2.5. Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message.

Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message.

- `ServerException`  is the error message on the server side.

- `ClientException`  is the error message on the SDK side.

For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```text
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 
Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle the errors returned by the Python SDK, see the following code example for reference:

```text
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own error handling logic here.
    # For example, print the detailed error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

<a id="section-3-2-6"></a>

### 3.2.6. Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics:

- Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product.

- Easy and convenient: You can call the latest API without updating the SDK.

- Fast iteration

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API references.

- Domain: the endpoint of the service.

- Version: the version of the API in the YYYY-MM-DD format.

  You can obtain the API version from the sections about common parameters in the API references.

- Operation information: the name of the API operation that you want to call.

  RPC API operation: You must obtain the value of the **Action** parameter and specify an API operation in  `request.set_action_name('Action')` .

  For example, if you want to call the DescribeEipAddresses operation, you must use  `request.set_action_name('DescribeEipAddresses')`  to specify the API operation when you initiate a CommonRequest request.

**Example: Call an RPC API operation**

The following code shows how to obtain information about elastic IP addresses (EIPs) by calling the DescribeEipAddresses operation of EIP.

> **Note**
>
> In the following code, replace the variable parameters with your actual
>
> information. Delete the angle brackets (<>) in the final code.
>
> The following section describes the variable parameters:
>
> - &lt;yourRegionID>: Replace the parameter with the region ID.
>
> - &lt;yourAccessKeyID>: Replace the parameter with your AccessKey ID.
>
> - &lt;yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
>
> - &lt;yourSecurityToken>: Replace the parameter with your security token.
>
> - &lt;yourResourceGroupID>: Replace the parameter with the resource set ID.
>
> - &lt;yourOrganizationID>: Replace the parameter with the organization ID.
>
> - &lt;yourInstanceID>: Replace the parameter with the instance ID.
>
> - &lt;vpc.aliyuncs.com>: Replace the parameter with the endpoint of the service.

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, the AccessKey secret, and the region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', 
'{<yourRegionID>}')
request = CommonRequest()
request.set_product('Vpc')
request.set_action_name('DescribeEipAddresses')
request.set_version('2016-04-28')
request.set_domain('<vpc.aliyuncs.com>') # Replace the variable parameter with the endpoint of the service.
# or:
# request = = CommonRequest(product='Vpc', 
action_name='DescribeEipAddresses',version='2016-04-28',domain='vpc.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS in the following manner:
# request.set_protocol_type('https') 
######
request.set_accept_format('json')
request.set_method('POST')
request.add_query_param('PageNumber', '1')
request.add_query_param('PageSize', '30')
######
# When you use STS AccessKey credentials to call an API operation, you must add the SecurityToken field in the request parameters.
# Format:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Specify your security token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")

response = client.do_action_with_exception(request)
print(str(response, encoding = 'utf-8'))
```

<a id="section-4"></a>

# 4.Call examples for SDK for Go

<a id="section-4-1"></a>

## 4.1. Quick start

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Go. To use the features of Elastic IP Address (EIP), you must install VPC SDK.

**Preparations**

- An Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair.

- Obtain the endpoint of EIP. For more information, see Obtain the information and the endpoint of an API operation.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library: You can check whether the latest version of the core package is installed on the Alibaba Cloud SDK for Go page.

```text
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use Apsara Stack SDK for Go**

To use Apsara Stack SDK for Go, perform the following steps:

1. Initialize a client instance.

2. Create an API request and specify the required parameters.

3. Initiate the API request and process the response or exception.

   > **Note**
   >
   > |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
   >
   > The following section describes the variables.
   >
   > - Replace &lt;yourRegionID> with the region ID.
   >
   > - Replace &lt;yourAccessKeyID> with your AccessKey ID.
   >
   > - Replace &lt;yourAccessKeySecret> with your AccessKey secret.
   >
   > - Replace &lt;Endpoint> with the actual endpoint.

   ```go
   package main
   import (
       "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc"
       "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
       "fmt"
   )
   func main() { 
       // Create a vpcClient instance.
       vpcClient, err := vpc.NewClientWithAccessKey(
           "<yourRegionID>",             // Replace the parameter with the region ID.
           "<yourAccessKeyID>",         // Replace it with your AccessKey ID.
           "<yourAccessKeySecret>")        // Replace the variable parameter with your 
   AccessKey secret.
       if err != nil {
           // Handle exceptions.
           panic(err)
       }
       // Create a request and configure the required parameters.
       request := vpc.CreateDescribeEipAddressesRequest()
       // Specify the endpoint of the service. 
       request.Domain = "<Endpoint>"
       // Set request.PageSize to 10.
       request.PageSize = requests.NewInteger(10)
       // Initiate the request and handle exceptions.
       response, err := vpcClient.DescribeEipAddresses(request)
       if err != nil {
           // Handle exceptions.
           panic(err)
       }
       fmt.Println(response)
   }
   ```

4. (Optional) Switch to HTTP or HTTPS.

   ```text
   request.Scheme = "HTTPS"
   ```

<a id="section-4-2"></a>

## 4.2. Use SDK

<a id="section-4-2-1"></a>

### 4.2.1. Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go.

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```text
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

<a id="section-4-2-2"></a>

### 4.2.2. Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication.

SDK for Go supports authentication through an AccessKey pair. For more information, see Obtain an AccessKey pair.

If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Important**
>
> Do not disclose any code containing your AccessKey pair. For example,
>
> do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

The following code provides an example on how to initialize a vpcClient instance.

```text
// Initialize a vpcClient instance.
vpcClient, err := vpc.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace the parameter with the region ID.
        "<yourAccessKeyID>",             // Replace the parameter with your AccessKey ID
.
        "<yourAccessKeySecret>")        // Replace the parameter with your AccessKey 
secret.
```

> **Note**
>
> In the preceding code, replace the variable parameters with your actual
>
> information. Delete the angle brackets (<>) in the final code.

<a id="section-4-2-3"></a>

### 4.2.3. Initiate a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Go to initiate a request. To use the features of Elastic IP Address (EIP), you must install VPC SDK.

The following example shows how to use VPC SDK for Go to initiate a request.

1. Import VPC SDK for Go.

   ```text
   import github.com/aliyun/alibaba-cloud-sdk-go/services/vpc
   ```

2. Create a VPC client. The client includes all APIs of the VPC.

   > **Note**
   >
   > In the following code, replace the variable parameters with your actual
   >
   > information. Delete the angle brackets (<>) in the final code.

   ```text
   vpcClient,err := <vpc>.NewClientWithAccessKey(  //Replace the parameter with the nameof the service.
       "<yourRegionID>",  // Replace the parameter with the region ID.         
       "<yourAccessKeyID>",  // Replace the parameter with your AccessKey ID.            

       "<yourAccessKeySecret>")  // Replace the parameter with your AccessKey secret.
   vpcClient.Domain = "vpc.aliyuns.com" //Specify the endpoint of the service.
   ```

3. Use the  `xxx.CreateXXXRequest`  method to create a request. The naming convention for this method is  `${service}.Create${apiName}Request` .

   - **${service}** specifies the service name in lowercase, such as vpc.

   - **${apiName}** specifies the name of an API operation, such as DescribeEipAddresses.

   ```text
   request := vpc.CreateDescribeEipAddressesRequest()
   request.InstanceId = ""
   ```

4. Initiate the call.

   ```text
   response, err := vpcClient.DescribeEipAddresses(request)
   ```

<a id="section-4-2-4"></a>

### 4.2.4. Handle errors

When you use Alibaba Cloud SDK for Go, a  `ClientError`  or a  `ServerError`  is returned when an error occurs on the server side or on the SDK side. Both error types are included in  `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors.

**Handle errors**

You can use the following code to handle errors:

```text
response,err  := vpcClient.DescribeEipAddresses(request)
if err != nil {
    // Obtain the error information.
   err.Error()
}
```

**ClientError**

When you send a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a  `ClientError` .

The following code shows how to determine and obtain the error message in a  `ClientError` of VPC SDK for Go:

> **Important**
>
> When you use a specific error struct, you must add the error package
>
> `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors`  by using the following code:
>
> ```go
> package main
> import (
>     "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the service.
>     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
>     // The error package that you want to add.
>     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
>     "fmt"
> )
> ```

```text
response, err := vpcClient.DescribeEipAddresses(request)
if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
}
```

**ServerError**

When the server returns an error message, the SDK wraps the message into a  `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response.

The following code shows how to determine and obtain the error message in a server error and response of VPC SDK for Go:

> **Important**
>
> When you use a specific error struct, you must add the error package
>
> `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors`  by using the following code:
>
> ```go
> package main
> import (
>     "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the service.
>     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
>     // The error package that you want to add.
>     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
>     "fmt"
> )
> ```

```text
response, err := vpcClient.DescribeEipAddresses(request)    
if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
}
```

<a id="section-4-2-5"></a>

### 4.2.5. Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Example: Call an RPC API operation**

The following code provides an example on how to obtain the information of elastic IP addresses (EIPs) by calling the DescribeEipAddresses operation of EIP. The API of EIP uses RPC.

> **Note**
>
> In the following code, replace the variable parameters with your actual
>
> information. Delete the angle brackets (<>) in the final code.
>
> The following section describes the variable parameters:
>
> - &lt;yourRegionID>: Replace the parameter with the region ID.
>
> - &lt;yourAccessKeyID>: Replace the parameter with your AccessKey ID.
>
> - &lt;yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
>
> - &lt;vpc.aliyuncs.com>: Replace the parameter with the endpoint of the service.
>
> - &lt;yourSecurityToken>: Replace the parameter with your security token.
>
> - &lt;yourResourceGroupID>: Replace the parameter with the resource set ID.
>
> - &lt;yourOrganizationID>: Replace the parameter with the organization ID.
>
> - &lt;yourInstanceID>: Replace the parameter with the instance ID.

```go
package main
import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
)
func main() {
    client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",        //Replace the parameter with the region ID.
        "<yourAccessKeyID>",     //Replace the parameter with the AccessKey ID.
        "<yourAccessKeySecret>") //Replace the parameter with your AccessKey secret.
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<vpc.aliyuncs.com>" // Replace the parameter with the endpoint ofthe service.
    request.Product = "Vpc"
    request.Version = "2016-04-28"
    // This is an RPC API operation. Therefore, the ApiName(Action) parameter must be specified.
    request.ApiName = "DescribeEipAddresses"
    // Configure service-related parameters.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    /* 
     When you use STS AccessKey credentials to call an RPC API operation, you must add the SecurityToken field in the request parameters.
     Format:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Specify your security token.
     */
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Specify the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Specify the organization ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query an instance.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

<a id="section-5"></a>

# 5.API reference

<a id="section-5-1"></a>

## 5.1. List of operations by function

The following table lists API operations available for use in Elastic IP Address (EIP).

| API | Description |
| --- | --- |
| AllocateEipAddress | Applies for an EIP. |
| AllocateEipAddressPro | Applies for a specified EIP. |
| AssociateEipAddress | Associates an EIP with a cloud resource. |
| AllocateEipSegmentAddress | Applies for a contiguous EIP group. |
| DescribeEipSegment | Queries contiguous EIP groups. |
| ReleaseEipSegmentAddress | Releases a contiguous EIP group. |
| ModifyEipAddressAttribute | Modifies the name, description, and bandwidth limit of a specified EIP. |
| DescribeEipAddresses | Queries the EIPs in a specified region. |
| UnassociateEipAddress | Disassociates an EIP from a cloud resource. |
| ReleaseEipAddress | Releases a specified EIP. |
| DescribeEipGatewayInfo | Queries the gateway and subnet mask information about a specified EIP. |
| DescribeEipMonitorData | Queries monitoring information about a specified EIP. |
| MoveResourceGroup | Changes the resource group to which a specified cloud resource belongs. |
| DescribeHighDefinitionMonitorLogAttribute | Queries fine-grained monitoring configurations of an EIP. |

<a id="section-5-2"></a>

## 5.2. Make API requests

<a id="section-5-2-1"></a>

### 5.2.1. Request syntax

To call an Elastic IP Address (EIP) API operation, you must send an HTTP GET request to the endpoint of the EIP API. Before you send a request, you must specify the request parameters for the operation. A response is returned for each request. Requests and responses are encoded in UTF-8.

EIP API operations use the RPC protocol. You can call EIP API operations by sending HTTP GET requests.

The following request syntax is used:

```text
http://Endpoint/?Action=xx&Parameters
```

Where:

- **Endpoint**: the endpoint of the API. The endpoint of the EIP API is  `vpc.example.com` .

  > **Note**
  >
  > `example.com`  is a custom domain name. For more information about how to obtain the endpoint, see Obtain the information and the endpoint of an API operation.

- **Action**: the name of the operation that you want to perform. For example, to query EIPs, you must set the Action parameter to DescribeEipAddresses.

- **Version**: the version of the API that you want to call. The current EIP API version is 2016-04-28.

- **Parameters**: the request parameters for the operation. Separate multiple parameters with ampersands (&).

  Request parameters include common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see Common parameters.

The following example describes how to call the DescribeEipAddresses operation to query EIPs.

> **Note**
>
> The following code has been formatted for ease of reading.

```text
https://vpc.example.com/?Action=DescribeEipAddresses
&Format=xml 
&Version=2016-04-28
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-5-2-2"></a>

### 5.2.2. API authorization

To ensure the security of your account, we recommend that you call EIP API operations as a RAM user. To call the EIP API as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations.

For more information about the EIP resources and API operations that allow the authorization, see RAM authentication.

<a id="section-5-2-3"></a>

### 5.2.3. Signature method guidelines

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller.

Elastic IP Address (EIP) implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Alibaba Cloud accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair.

You must add the signature to the EIP API request in the following format:

```text
  https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf 
```

Take DescribeEipAddresses as an example. If the AccessKey ID is  `testid`  and the AccessKey secret is  `testsecret` , the pre-signed request URL is:

```text
http://vpc.example.com/?Action=DescribeEipAddresses
&Timestamp=2016-02-23T12:46:24Z
&Format=XML
&AccessKeyId=testid 
&SignatureMethod=HMAC-SHA1
&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
&Version=2016-04-28
&SignatureVersion=1.0
```

Perform the following operations to calculate the signature:

1. Use the request parameters to create a string-to-sign.

   ```text
   GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeEipAddresses&Format%3DXML&SignatureMethod
   DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-
   4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-
   23T12%253A46%253A24Z&Version%3D2014-05-15
   ```

2. Calculate the HMAC value of the string to be signed.

   Append an ampersand (&) to the end of the AccessKey secret as the key to calculate the HMAC value. In this example, the key is  `testsecret&` .

   ```text
   CT9X0VtwR86fNWSnsc6v8YGOjuE=
   ```

3. Add the signature string to the request:

   ```text
   http://vpc.example.com/?Action=DescribeEipAddresses
   &Timestamp=2016-02-23T12:46:24Z
   &Format=XML
   &AccessKeyId=testid
   &SignatureMethod=HMAC-SHA1
   &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
   &Version=2016-04-28
   &SignatureVersion=1.0
   &Signature=xxxx%xxxx%3D
   ```

<a id="section-5-3"></a>

## 5.3. RAM authentication

Before you call an EIP operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM account. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource.

**EIP resources that allow authorized access**

The following table lists the EIP resources that allow authorized access and their ARNs.

<table>
  <tr>
    <th>Resource type</th>
    <th>ARN</th>
  </tr>
  <tr>
    <td rowspan="3">EIPs</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/$allocationid</code></td>
  </tr>
  <tr>
    <td><code>acs:vpc:$regionid:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td><code>acs:vpc:*:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td rowspan="2">General resources</td>
    <td><code>acs:vpc:$regionid:$accountid:*</code></td>
  </tr>
  <tr>
    <td><code>acs:vpc:*:$accountid:*</code></td>
  </tr>
</table>

`$regionid/accoutid/vrouterid`  are IDs of the specific resources,  `*`  represents all resources.

**EIP API operations that allow authorized access**

The following table lists the EIP API operations that allow authorized access and their ARNs.

<table>
  <tr>
    <th>API</th>
    <th>ARN</th>
  </tr>
  <tr>
    <td>AllocateEipAddress</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td>AllocateEipAddressPro</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td rowspan="2">AssociateEipAddres</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td>Associate an Elastic Compute Service (ECS) instance<br><code>acs:vpc:$regionid:$accountid:eip/$allocationid</code><br><code>acs:ecs:$regionid:$accountid:instance/$instanceid</code></td>
  </tr>
  <tr>
    <td>DescribeEipAddresses</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/*</code></td>
  </tr>
  <tr>
    <td>UnassociateEipAddres s</td>
    <td>Associate an ECS instance<br><code>acs:vpc:$regionid:$accountid:eip/$allocationid</code><br><code>acs:ecs:$regionid:$accountid:instance/$instanceid</code></td>
  </tr>
  <tr>
    <td>ReleaseEipAddress</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/$allocationid</code></td>
  </tr>
  <tr>
    <td rowspan="2">DescribeEipMonitorDat a</td>
    <td><code>acs:vpc:$regionid:$accountid:eip/$allocationid</code></td>
  </tr>
  <tr>
    <td><code>acs:ecs:$regionid:$accountid:instance/$instanceid</code></td>
  </tr>
</table>

<a id="section-5-4"></a>

## 5.4. Common parameters

This topic describes common parameters, including common request parameters and common response parameters. Common parameters are required in all API operations, regardless of the operation being called.

**Common request parameters**

Common request parameters must be included in all EIP API requests.

Table 1. Common request parameters

| Parameter | Type | Requi red | Description |
| --- | --- | --- | --- |
| Format | Strin g | No | The format in which to return the response. Valid values:<br>JSON and XML. Default value: JSON. |
| Version | Strin g | Yes | The version number of the API. Format: <code> YYYY-MM-DD </code>. Set the value to<br>2016-04-28 |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | Strin g | Yes | The signature string of the current request. |
| SignatureMe thod | Strin g | Yes | The encryption method of the signature string. Set the value to<br>HMAC-SHA1 |
| Timestamp | Strin g | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the <code> YYYY-MM-DDThh:mm:ssZ </code> format. The time must be in UTC.<br>For example, 2013-01-10T12:00:00Z. |
| SignatureVer sion | Strin g | Yes | The version of the signature encryption algorithm. Set the value to<br>1.0 |
| SignatureNo nce | Strin g | Yes | A unique, random number used to prevent replay attacks.<br>You must use different numbers for different requests. |

**Examples**

```text
http://vpc.example.com/?Action=DescribeEipAddresses
&Timestamp=2016-02-23T12:46:24Z
&Format=XML
&AccessKeyId=testid 
&SignatureMethod=HMAC-SHA1
&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
&Version=2016-04-28
&SignatureVersion=1.0
```

**Common response parameters**

API responses use the HTTP response format where a 2XX status code indicates a successful call and a 4XX or 5XX status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML.

Every response returns a unique **RequestId** regardless of whether the call is successful.

- XML format

  ```text
  <? xml version="1.0" encoding="utf-8"? > 
        <!—Result Root Node-->
        <Interface Name+Response>
        <!—Return Request Tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Return Result Data-->
        </Interface Name+Response>
                      
  ```

- JSON format

  ```json
  {
        "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
        /*Return Result Data*/
    }
  ```

<a id="section-5-5"></a>

## 5.5. Elastic IP addresses

<a id="section-5-5-1"></a>

### 5.5.1. AllocateEipAddress

Applies for an elastic IP address (EIP).

**Description**

After you call this operation, the system randomly allocates an EIP that is in the **Available** state in the specified region. EIPs support only the ICMP, TCP, and UDP transport layer protocols. The IGMP and SCTP protocols are not supported.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | AllocateEipAddr ess | The operation that you want to perform. Set the value to <strong>AllocateEipAddress</strong>. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where you want to apply for an EIP. You can call the <code> DescribeRegions </code> operation to query region IDs. |
| Bandwidth | String | No | 1 | The bandwidth limit of the EIP. Valid values: <strong>1</strong> to <strong>200</strong>. Unit: Mbit/s.<br>Default value: <strong>1</strong>. |
| Period | Integer | No | 1 | The subscription duration of the EIP.<br>When <strong>PricingCycle</strong> is set to <strong>Month</strong>, <strong>Period</strong> can be set from <strong>1 to 9</strong>.<br>When <strong>PricingCycle</strong> is set to <strong>Year</strong>, <strong>Period</strong> can be set from <strong>1 to 3</strong>.<br>This parameter is required when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>. When <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, ignore this parameter.<br>Note This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |
| ISP | String | No | BGP | The line type. Default value: <strong>BGP</strong>.<br>• If your account is in the single-path BGP whitelist, you can set the parameter to <strong>ChinaTelecom</strong>, <strong>ChinaUnicom</strong>, or <strong>ChinaMobile</strong>.<br>• This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to <strong>BGP_FinanceCloud</strong>. |
| ActivityId | Long | No | 111111 | The promotion code. You can leave this parameter empty. |
| Netmode | String | No | public | The type of network. Set the value to <strong>public</strong> (Internet). |

<table>
  <tr>
    <td>AutoPay</td>
    <td>Boolean</td>
    <td>No</td>
    <td>false</td>
    <td>Specifies whether to enable automatic payment. Valid values:<br><strong>false</strong>: disables automatic payment.After an order is generated, you must go to the order center to complete the payment.<br><strong>true</strong>: enables automatic payment.After an order is generated, the system automatically deducts fees from your account balance to pay for the order.<br>This parameter is required when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>. When <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, this parameter is not required.<br>Note This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site.</td>
  </tr>
  <tr>
    <td>PricingCycle</td>
    <td>String</td>
    <td>No</td>
    <td>Month</td>
    <td>The billing cycle of the subscription EIP. Valid values:<br><strong>Month</strong>: billed on a monthly basis.This is the default value.<br><strong>Year</strong>: billed on an annual basis.<br>This parameter is required when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>. When <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, this parameter is not required.<br>Note This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site.</td>
  </tr>
</table>

<table>
  <tr>
    <td>InstanceChargeT ype</td>
    <td>String</td>
    <td>No</td>
    <td>PostPaid</td>
    <td>The billing method of the EIP. Valid values:<br><strong>PrePaid</strong>: subscription.<br><strong>PostPaid</strong>: pay-as-you-go. This is the default value.<br>When <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>, you must set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong>. When <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, you can set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong> or <strong>PayByTraffic</strong>.<br>Note If you want to purchase an EIP from the Alibaba Cloud International site, you must set this parameter to <strong>PostPaid</strong> (pay-as-you-go).</td>
  </tr>
  <tr>
    <td>InternetChargeT ype</td>
    <td>String</td>
    <td>No</td>
    <td>PayByTraffic</td>
    <td>The metering method of the EIP.Valid values:<br><strong>PayByBandwidth</strong>: pay-by-bandwidth. This is the default value.<br><strong>PayByTraffic</strong>: pay-by-data-transfer.<br>When <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>, <strong>InternetChargeType</strong> must be set to <strong>PayByBandwidth</strong>.<br>When <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, <strong>InternetChargeType</strong> can be set to <strong>PayByBandwidth</strong> or <strong>PayByTraffic</strong>.</td>
  </tr>
  <tr>
    <td>ResourceGroupI d</td>
    <td>String</td>
    <td>No</td>
    <td>rg-acfmxazffggds** **</td>
    <td>The ID of the enterprise resource group.</td>
  </tr>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>No</td>
    <td>0c593ea1-3bea-11e9-b96b-88e9fe637760</td>
    <td>The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. <strong>ClientToken</strong> can contain only ASCII characters and cannot exceed 64 characters in length.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EipAddress | String | 10.XX.XX.78 | The allocated EIP. |
| AllocationId | String | eip-25877c70gddh\*\*\*\* | The ID of the EIP. |
| OrderId | Long | 10 | The order number. This parameter is returned only when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>. |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The ID of the request. |
| ResourceGrou pId | String | rg-acfmxazfdgdg\*\*\*\* | The ID of the enterprise resource group. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=AllocateEipAddress
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<AllocateEipAddressrResponse>
  <ResourceGroupId>rg-acfmxazfdgdg****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>10.XX.XX.78</EipAddress>
  <OrderId>10</OrderId>
</AllocateEipAddressrResponse>
```

`JSON`  format

```json
{
    "AllocateEipAddressrResponse": {
        "ResourceGroupId": "rg-acfmxazfdgdg****",
        "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
        "AllocationId": "eip-25877c70gddh****",
        "EipAddress": "10.XX.XX.78",
        "OrderId": 10
    }
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the EIP. |
| 400 | InvalidRegion.NotS upport | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGro upId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |
| 409 | OperationConflict | Request was denied due to conflict with a previos request. | The error message returned because a request conflict occurs. Try again later or submit a ticket to report the problem. |

<a id="section-5-5-2"></a>

### 5.5.2. AllocateEipAddressPro

Applies for a specified EIP.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | AllocateEipAddr essPro | The operation that you want to perform. Set the value to <strong>AllocateEipAddressPro</strong>. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region ID of the specified EIP for which you want to apply.<br>You can call the <code> DescribeRegions </code> operation to query the most recent region list. |
| IpAddress | String | No | 12.XX.XX.23 | The IP address of the specified EIP.<br>Specify <strong>IpAddress</strong> or <strong>InstanceId</strong>. If you leave both parameters empty, the system randomly allocates an EIP. |
| InstanceId | String | No | eip-25877c70gddh\* \*\*\* | The ID of the specified EIP.<br>Specify <strong>IpAddress</strong> or <strong>InstanceId</strong>. If you leave both parameters empty, the system randomly allocates an EIP. |
| Bandwidth | String | No | 5 | The bandwidth limit of the specified EIP. Unit: Mbit/s.<br>Default value: <strong>1</strong>. |
| Period | Integer | No | 1 | The subscription duration of the EIP.<br>If <strong>PricingCycle</strong> is set to <strong>Month</strong>, set Period to a value from <strong>1</strong> to <strong>9</strong>.<br>If <strong>PricingCycle</strong> is set to <strong>Year</strong>, set Period to a value from <strong>1</strong> to <strong>3</strong>.<br>This parameter is required when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>.<br>Leave this parameter empty when <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>. |
| ISP | String | No | BGP | The line type. Default value: <strong>BGP</strong>.<br>If your account is in the single-path BGP whitelist, you can set the parameter to <strong>ChinaTelecom</strong>, <strong>ChinaUnicom</strong>, or <strong>ChinaMobile</strong>.<br>This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to <strong>BGP_FinanceCloud</strong>. |
| Netmode | String | No | public | The type of network. Set the value to <strong>public</strong> (Internet).<br>Default value: <strong>public</strong> (Internet). |
| Name | String | No | Test123 | The name of the EIP.<br>The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter. It cannot start with <code> http:// </code> or <code> https:// </code>. |
| Description | String | No | abc | The description of the EIP.<br>The description must be 2 to 256 characters in length. It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values:<br><strong>false</strong>: disables automatic payment.After an order is generated, you must go to the Order Center to make the payment.<br><strong>true</strong>: enables automatic payment.Payments are automatically made.<br>This parameter is required when <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>.<br>Leave this parameter empty when <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>. |
| PricingCycle | String | No | Month | The billing cycle of the subscription EIP. Valid values:<br>• <strong>Month</strong> (default): The instance is billed on a monthly basis.<br>• <strong>Year</strong>: The instance is billed on an annual basis.<br>This parameter is required if <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>. This parameter is optional if <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>. |
| InstanceChargeT ype | String | No | PostPaid | The billing method of the specified EIP. Valid values:<br><strong>PrePaid</strong>: subscription<br><strong>PostPaid</strong> (default): pay-as-you-go<br>If <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>, you must set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong>.<br>If <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, you can set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong> or <strong>PayByTraffic</strong>. |
| InternetChargeT ype | String | No | PayByBandwidth | The metering method of the specified EIP. Valid values:<br><strong>PayByBandwidth</strong> (default): pay-by-bandwidth<br><strong>PayByTraffic</strong>: pay-by-data-transfer<br>If <strong>InstanceChargeType</strong> is set to <strong>PrePaid</strong>, you must set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong>.<br>If <strong>InstanceChargeType</strong> is set to <strong>PostPaid</strong>, you can set <strong>InternetChargeType</strong> to <strong>PayByBandwidth</strong> or <strong>PayByTraffic</strong>. |
| ResourceGroupI d | String | No | rg-resourcegroup\*\* \*\* | The ID of the resource group to which the EIP belongs. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b-88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. <strong>ClientToken</strong> can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AllocationId | String | eip-25877c70gddh\*\*\*\* | The ID of the specified EIP. |
| EipAddress | String | 12.XX.XX.23 | The IP address of the specified EIP. |
| OrderId | Long | 20190000 | the ID of the order. |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The ID of the request. |
| ResourceGrou pId | String | rg-resourcegroup\*\*\*\* | The ID of the resource group. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=AllocateEipAddressPro
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<AllocateEipAddressProResponse>
  <ResourceGroupId>rg-resourcegroup****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>12.XX.XX.23</EipAddress>
  <OrderId>20190000</OrderId>
</AllocateEipAddressProResponse>
```

`JSON`  format

```json
{
    "ResourceGroupId": "rg-resourcegroup****",
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "AllocationId": "eip-25877c70gddh****",
    "EipAddress": "12.XX.XX.23",
    "OrderId": 20190000
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the EIP. |
| 400 | InvalidRegion.NotS upport | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGro upId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |

<a id="section-5-5-3"></a>

### 5.5.3. AssociateEipAddress

Associates an elastic IP address (EIP) with an instance in the same region.

**Description**

When you call the operation, take note of the following items:

- You can associate an EIP with an Elastic Compute Service (ECS) instance, a Server Load Balancer (SLB) instance, a secondary elastic network interface (ENI), or a NAT gateway that is deployed in a virtual private cloud (VPC). The EIP and the instance with which you want to associate the EIP must belong to the same region.

- To associate an EIP with a NAT gateway, make sure that no NAT service plan that was purchased before November 3, 2017 exists in your account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | AssociateEipAdd ress | The operation that you want to perform. Valid values: <strong>AssociateEipAddress</strong> . |
| AllocationId | String | Yes | eip-2zeerraiwb7ujsx dc\*\*\*\* | The ID of the EIP that you want to associate with an instance. |
| InstanceId | String | Yes | i-2zebb08phyczza we\*\*\*\* | The ID of the instance with which you want to associate the EIP.<br>NAT gateways, SLB instances, ECS instances, secondary ENIs, and high-availability virtual IP addresses (HAVIPs) are supported. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance with which you want to associate the EIP. Valid values:<br>• <strong>Nat</strong> : NAT Gateway.<br>• <strong>SlbInstance</strong> : SLB SLB.<br>• <strong>EcsInstance</strong> : ECS instances.<br>• <strong>NetworkInterface</strong> : auxiliary Elastic Network Interface.<br>• <strong>HaVip</strong> : High-availability virtual IP addresses. |
| InstanceRegionI d | String | No | cn-hangzhou | The ID of the region where the instance to be associated with the EIP is deployed.<br>Note This parameter is required only when the EIP is associated with a shared-bandwidth Global Accelerator (GA) instance. |
| PrivateIpAddress | String | No | 192.1.XX.XX | An IP address that belongs to the CIDR block of a vSwitch.<br>If you do not set this parameter, the system allocates a private IP address based on the VPC ID and vSwitch ID. |
| Mode | String | No | NAT | The binding mode. Valid values:<br>• <strong>NAT</strong> : NAT mode (normal mode).<br>• <strong>MULTI_BINDED</strong> : The multi-EIP network interface controller visible mode.<br>• <strong>BINDED</strong> : The visible mode of the EIP network interface controller.<br>Only <strong>InstanceType</strong> Configure as <strong>NetworkInterface</strong> this parameter is required. |
| ClientToken | String | No | 02fb3da4-130e-11e9-8e44-001sdfg | Guaranteed request idempotence.You can use the client to generate the value, but you must ensure that it is unique among different requests. <code>  ClientToken  </code> Only ASCII characters are supported and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | C0FD0EED-F90D-4479-803D-DD62335357E5 | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=AssociateEipAddress
&AllocationId=eip-2zeerraiwb7ujsxdc****
&InstanceId=i-2zebb08phyczzawe****
&<Public request parameters>
```

Sample success responses

`XML`  format

```xml
<AssociateEipAddressResponse>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5</RequestId>
</AssociateEipAddressResponse>
```

`JSON`  format

```json
{
  "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5" 
}    
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidAssociation.Duplicated | Specified instance already is associated. | The error message returned because an EIP or a GA instance is already associated with the specified instance.You must disassociate the EIP or GA instance from the specified instance before you can perform the operation. |
| 400 | OperationDenied | Specified instance is not in VPC. | The error message returned because the specified instance does not exist in the VPC. |
| 400 | InvalidParameter.M ismatch | Specified elastic IP address and ECS instance are not in the same region. | The error message returned because the specified EIP and ECS instance do not belong to the same region. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation | The error message returned because the state of the EIP does not support the operation. |
| 404 | InvalidInstanId.Not Found | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the ID is valid. |
| 400 | IncorrectInstanceSt atus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |
| 400 | InvalidInstanceTyp e.ValueNotSupport ed | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStat us | HaVip can be operated by this action only when it's status is Available or InUse. | The error message returned because the state of the HAVIP does not support the operation. You can perform the operation only when the HAVIP is in the Available or InUse state. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the specified value of the parameter is invalid. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because the operation is not supported by EIPs in the default VPC. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatu s | The eip binding status invalid. | The error message returned because the EIP is in an invalid state. |
| 400 | BIND_INSTANCE_H AVE_PORTMAP_OR_BIND_EIP | The instance may have portMap or already bind eip. | The error message returned because a port forwarding rule is configured for the ECS instance. Delete the port forwarding rule and try again. |
| 400 | BIND_INSTANCE_O WENER_ERROR | Cannot operate the eip. | The error message returned because you are unauthorized to manage the specified EIP. |
| 404 | InvalidAllocationId.NotFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParams.NotF ound | instance not found | The error message returned because the specified instance does not exist. |
| 503 | ServiceUnavailable | The request has failed due to a temporary failure of the server. | The error message returned because the request failed due to a temporary malfunction of the server. |

<a id="section-5-5-4"></a>

### 5.5.4. AllocateEipSegmentAddress

Applies for a contiguous elastic IP address (EIP) group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | AllocateEipSegm entAddress | The operation that you want to perform. Set the value to <strong>AllocateEipSegmentAddress</strong>. |
| EipMask | String | Yes | 28 | The subnet mask length for the contiguous EIP group. Valid values:<br>• <strong>28</strong>: applies for 16 contiguous EIPs in each call.<br>• <strong>27</strong>: applies for 32 contiguous EIPs in each call.<br>• <strong>26</strong>: applies for 64 contiguous EIPs each call.<br>• <strong>25</strong>: applies for 128 contiguous EIPs in each call.<br>• <strong>24</strong>: applies for 256 contiguous EIPs in each call.<br>Note The number of contiguous EIPs allocated by the system may be less than the requested number because one, three, or four EIPs may be reserved. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region ID of the contiguous EIP group.<br>You can call the <strong>DescribeRegions</strong> operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e-11e9-8e44-001sdfg | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.<br>Note If you do not set this parameter, the system automatically uses <strong>RequestId</strong> as <strong>ClientToken</strong>. <strong>RequestId</strong> of each API request may be different. |
| Bandwidth | String | No | 5 | The maximum bandwidth of the EIP.Unit: Mbit/s. Default value: <strong>5</strong>. |
| Netmode | String | No | public | The network type. Valid values:<br>• <strong>public</strong> (default): Internet. After the contiguous EIP group is associated with a cloud resource, the cloud resource can communicate with the Internet by using the EIPs in the contiguous EIP group.<br>• <strong>hybrid</strong>: hybrid cloud. After the contiguous EIP group is associated with a cloud resource, the cloud resource can communicate with a hybrid cloud by using the EIPs in the contiguous EIP group.<br>Note This network type is available only to users who are included in the whitelist. To use this network type, contact your business manager. |
| InternetChargeT ype | String | No | PayByBandwidth | The metering method of the contiguous EIP group. Valid values:<br>• <strong>PayByBandwidth</strong> (default): pay-by-bandwidth<br>• <strong>PayByTraffic</strong>: pay-by-data-transfer<br>Note If the <strong>Netmode</strong> parameter is set to <strong>hybrid</strong>, you can set <strong>InternetChargeType</strong> only to <strong>PayByBandwidth</strong>. |
| ResourceGroupI d | String | No | rg-bp67acfmxazb4 ph\*\*\*\* | The ID of the resource group to which the contiguous EIP group belongs. |
| Isp | String | No | BGP | The line type. Valid values:<br>• <strong>BGP</strong>: BGP (Multi-ISP)<br>• <strong>BGP_PRO</strong>: BGP (Multi-ISP) Pro |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EipSegmentIns tanceId | String | eipsg-2zett8ba055tbsxm e\*\*\*\* | The ID of the contiguous EIP group. |
| OrderId | Long | 20190000 | The ID of the order. |
| RequestId | String | F7A6301A-64BA-41EC-8284-8F4838C15D1F | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=AllocateEipSegmentAddress
&EipMask=28
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<AllocateEipSegmentAddress>
  <EipSegmentInstanceId>eipsg-2zett8ba055tbsxme****</EipSegmentInstanceId>
  <RequestId>F7A6301A-64BA-41EC-8284-8F4838C15D1F</RequestId>
  <OrderId>20190000</OrderId>
</AllocateEipSegmentAddress>
```

`JSON`  format

```json
{
    "EipSegmentInstanceId": "eipsg-2zett8ba055tbsxme****",
    "RequestId": "F7A6301A-64BA-41EC-8284-8F4838C15D1F",
    "OrderId": 20190000
}
```

**Error code**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. Apply for the required permissions and try again. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth value is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because you do not have sufficient balance within your Apsara Stack tenant account.Top up your Apsara Stack tenant account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs has reached the upper limit.We recommend that you use NAT gateways if you want to use more EIPs. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the specified EIP. |
| 400 | InvalidRegion.NotS upport | The specified region does not support. | The error message returned because the operation is not supported in the specified region. |
| 400 | InvalidResourceGro upId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |
| 409 | OperationConflict | Request was denied due to conflict with a previos request. | The error message returned because your request is conflicting with another request. Try again later. |
| 400 | ORDER.QUANTITY_I NVALID | User quota has exceeded the limit. | The error message returned because the number of EIPs that you have created has reached the upper limit. Go to the Quota Management page to request a quota increase. |
| 500 | OrderError.EIP | The Account failed to create order. | The error message returned because the system failed to generate the order. |

<a id="section-5-5-5"></a>

### 5.5.5. DescribeEipSegment

Queries contiguous elastic IP address (EIP) groups.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeEipSeg ment | The operation that you want to perform. Set the value to <strong>DescribeEipSegment</strong>. |
| RegionId | String | Yes | cn-qingdao-env66-d01 | The ID of the region to which the contiguous EIP group belongs.<br>You can call the <strong>DescribeRegions</strong> operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e-11e9-8e44-00\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.<br>Note If you do not set this parameter, the system automatically uses <strong>RequestId</strong> as <strong>ClientToken</strong>. <strong>RequestId</strong> of each API request may be different. |
| SegmentInstanc eId | String | No | eipsg-2zett8ba055tbsx me\*\*\*\* | The ID of the contiguous EIP group that you want to query. |
| PageNumber | Integer | No | 1 | The page number of the page to return. Default value: <strong>1</strong>. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: <strong>50</strong>.Default value: <strong>10</strong>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EipSegments | Array of EipSegment |  | The details of the contiguous EIP groups. |
| EipSegment |  |  |  |
| CreationTime | String | 2021-03-06T12:30:07Z | The time when the contiguous EIP group was created. The time is in the <code> ISO </code> <code>8601 </code> standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC+0. |
| Descritpion | String | MyEipSegment | The description of the contiguous EIP group. |
| InstanceId | String | eipsg-2zett8ba055tbsxm e\*\*\*\* | The ID of the contiguous EIP group. |
| IpCount | String | 28 | The number of EIPs in the contiguous EIP group. |
| Name | String | MyEipSegment | The name of the contiguous EIP group. |
| RegionId | String | cn-qingdao-env66-d01 | The ID of the region to which the contiguous EIP group belongs. |
| Segment | String | 161.XX.XX.0/28 | The CIDR block and subnet mask of the contiguous EIP group. |
| Status | String | Allocated | The status of the contiguous EIP group.Valid values:<br>• <strong>Allocating</strong>: being allocated<br>• <strong>Allocated</strong>: allocated<br>• <strong>Releasing</strong>: being released<br>• <strong>Released</strong>: released |
| PageNumber | Integer | 2 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | F7A6301A-64BA-41EC-8284-8F4838C15D1F | The ID of the request. |
| TotalCount | Integer | 1 | The number of entries returned. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeEipSegment
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeEipSegmentResponse>
  <EipSegments>
        <Status>Allocated</Status>
        <Descritpion>MyEipSegment</Descritpion>
        <IpCount>28</IpCount>
        <InstanceId>eipsg-2zett8ba055tbsxme****</InstanceId>
        <CreationTime>2021-03-06T12:30:07Z</CreationTime>
        <RegionId>cn-qingdao-env66-d01</RegionId>
        <Segment>161.XX.XX.0/28</Segment>
        <Name>MyEipSegment</Name>
  </EipSegments>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>F7A6301A-64BA-41EC-8284-8F4838C15D1F</RequestId>
  <PageNumber>2</PageNumber>
</DescribeEipSegmentResponse>
```

`JSON`  format

```json
{
    "EipSegments": {
        "Status": "Allocated",
        "Descritpion": "MyEipSegment",
        "IpCount": 28,
        "InstanceId": "eipsg-2zett8ba055tbsxme****",
        "CreationTime": "2021-03-06T12:30:07Z",
        "RegionId": "cn-qingdao-env66-d01",
        "Segment": "161.XX.XX.0/28",
        "Name": "MyEipSegment"
    },
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "F7A6301A-64BA-41EC-8284-8F4838C15D1F",
    "PageNumber": 2
}
```

<a id="section-5-5-6"></a>

### 5.5.6. ReleaseEipSegmentAddress

Releases contiguous elastic IP addresses (EIPs).

**Description**

You can call this operation to release all EIPs in a group of contiguous EIPs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ReleaseEipSegm entAddress | The operation that you want to perform. Set the value to <strong>ReleaseEipSegmentAddress</strong>. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region ID of the contiguous EIPs.<br>You can call the <strong>DescribeRegions</strong> operation to query the most recent region list. |
| SegmentInstanc eId | String | Yes | eipsg-2zett8ba055tbsx me\*\*\*\* | The ID of the group to which the contiguous EIPs to be released belongs.<br>The system releases all EIPs in the group. |
| ClientToken | String | No | 02fb3da4-130e-11e9-8e44-00\*\*\*\* | The client token that is used to ensure the idempotence of the request.<br>You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.<br>Note If you do not set this parameter, the system automatically uses <strong>RequestId</strong> as <strong>ClientToken</strong>. <strong>RequestId</strong> of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F7A6301A-64BA-41EC-8284-8F4838C15D1F | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ReleaseEipSegmentAddress
&RegionId=cn-qingdao-env17-d01
&SegmentInstanceId=eipsg-2zett8ba055tbsxme****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ReleaseEipSegmentAddressResponse> 
  <RequestId>F7A6301A-64BA-41EC-8284-8F4838C15D1F</RequestId>
</ReleaseEipSegmentAddressResponse>
```

`JSON`  format

```json
{
    "RequestId": "F7A6301A-64BA-41EC-8284-8F4838C15D1F"
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because you cannot perform the operation when the specified EIPs are in the current state. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | Forbidden.ChargeT ypeIsPrepaid | It's forbidden to release a prepaid EIP | The error message returned because you cannot release subscription EIPs. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because the EIPs do not belong to you. Check whether you are unauthorized to perform the operation on the EIPs. |
| 400 | TaskConflict.Associ ateGlobalAccelerati onInstance | Operate too frequent. | The error message returned because the number of requests that you send exceeds the upper limit. |

<a id="section-5-5-7"></a>

### 5.5.7. ModifyEipAddressAttribute

Modifies the name, description, and bandwidth limit of a specified elastic IP address (EIP).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyEipAddres sAttribute | The operation that you want to perform. Set the value to <strong>ModifyEipAddressAttribute</strong>. |
| AllocationId | String | Yes | eip-2zeerraiwb7uj6i 0d\*\*\*\* | The ID of the EIP that you want to modify. |
| Bandwidth | String | No | 100 | The bandwidth limit of the EIP. Valid values: <strong>1</strong> to <strong>200</strong>. Unit: Mbit/s. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region to which the EIP belongs. |
| Name | String | No | Test123 | The name of the EIP.<br>The name must be 2 to 128 characters in length, and can contain, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter. The name cannot start with <code> http:// </code> or <code> https:// </code>. |
| Description | String | No | abc | The description of the EIP.<br>The description must be 2 to 256 characters in length. It must start with a letter but cannot start with <code> http:// </code> or <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyEipAddressAttribute
&AllocationId=eip-2zeerraiwb7uj6i0d****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyEipAddressAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyEipAddressAttributeResponse>
```

`JSON`  format

```json
{
    "ModifyEipAddressAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
    }
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InsufficientBalance.Eip | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 404 | InvalidAllocationId.NotFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not supported. | The error message returned because the specified bandwidth limit is invalid. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 404 | InvalidAllocationId.NotFound | Specified allocation ID is not found.. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | The parameter is invalid. | The error message returned because the parameter is set to an invalid value. |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

<a id="section-5-5-8"></a>

### 5.5.8. DescribeEipAddresses

Queries elastic IP addresses (EIPs) created in a specific region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeEipAddr esses | The operation that you want to perform. Set the value to <strong>DescribeEipAddresses</strong>. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region ID of the EIP. You can call the <code> DescribeRegions </code> operation to query the most recent region list. |
| Tag.N.Key | String | No | TestKey | The key of tag N of the instance that you want to query. Valid values of N: <strong>1</strong> to <strong>20</strong>. |
| Tag.N.Value | String | No | TestValue | The value of tag N of the instance that you want to query. Valid values of N: <strong>1</strong> to <strong>20</strong>. |
| IncludeReservati onData | Boolean | No | true | Specify whether to return data of orders that have not taken effect.Valid values:<br>• <strong>false</strong>: does not return data of orders that have not taken effect.This is the default value.<br>• <strong>true</strong>: returns data of orders that have not taken effect. |
| Status | String | No | Available | The status of the EIP. Valid values:<br>• <strong>Associating</strong>: The EIP is being associated with an instance.<br>• <strong>Unassociating</strong>: The EIP is being disassociated from an instance.<br>• <strong>InUse</strong>: The EIP is associated with an instance.<br>• <strong>Available</strong>: The EIP is available. |
| EipAddress | String | No | 116.xx.xx.28 | The IP address of the EIP that you want to query.<br>You can enter up to 50 IP addresses of EIPs. Separate multiple IP addresses with commas (,).<br>Note If both the <strong>EipAddress</strong> and <strong>AllocationId</strong> parameters are set, you can enter up to 50 IP addresses of EIPs in <strong>EipAddress</strong>, and enter up to 50 IDs of EIPs in <strong>AllocationId</strong>. |
| AllocationId | String | No | eip-2zeerraiwb7ujxs cd\*\*\*\* | The ID of the EIP that you want to query.<br>You can enter up to 50 IDs of EIPs.Separate multiple IDs with commas (,).<br>Note If both the <strong>EipAddress</strong> and <strong>AllocationId</strong> parameters are set, you can enter up to 50 IDs of EIPs in <strong>AllocationId</strong>, and enter up to 50 IP addresses of EIPs in <strong>EipAddress</strong>. |
| SegmentInstanc eId | String | No | eipsg-t4nr90yik5oy38 xdy\*\*\*\* | The IDs of contiguous EIPs. |
| ResourceGroupI d | String | No | rg-acfmxazb4pcdvf \*\*\*\* | The ID of the resource group to which the EIPs belong. |
| PageNumber | Integer | No | 10 | The number of the page to return.Default value: <strong>1</strong>. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: <strong>100</strong>.Default value: <strong>10</strong>. |
| ISP | String | No | BGP | The Internet service provider (ISP).Set the value to <strong>BGP</strong>. |
| Filter.1.Key | String | No | CreationStartTi me | The filter key used to query resources. Set the value to <strong>CreationStartTime</strong>, which indicates the time when the system started to create the resource. |
| Filter.2.Key | String | No | CreationEndTim e | The filter key used to query resources. Set the value to <strong>CreationEndTime</strong>, which indicates the time when the system completed creating the resource. |
| Filter.1.Value | String | No | 2018-01-22T09:12Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in <code> YYYY-MM-</code><code>DDThh:mmZ </code> format. The time must be in UTC. |
| Filter.2.Value | String | No | 2018-01-22T09:15Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in <code> YYYY-MM-</code><code>DDThh:mmZ </code> format. The time must be in UTC. |
| LockReason | String | No | financial | The reason why the EIP is locked.Valid values:<br>• <strong>financial</strong>: The EIP is locked due to overdue payments.<br>• <strong>security</strong>: The EIP is locked for security reasons. |
| AssociatedInstan ceType | String | No | EcsInstance | The type of the cloud resource with which you want to associate the EIP.Valid values:<br>• <strong>EcsInstance</strong>: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This is the default value.<br>• <strong>SlbInstance</strong>: a Server Load Balancer (SLB) instance in a VPC.<br>• <strong>Nat</strong>: a NAT gateway.<br>• <strong>HaVip</strong>: a high-availability virtual IP address (HAVIP).<br>• <strong>NetworkInterface</strong>: a secondary elastic network interface (ENI).<br>You can associate only one EIP with each ECS instance, SLB instance, or HAVIP. You can associate multiple EIPs with each NAT gateway. The number of EIPs that can be associated with a secondary ENI depends on the EIP association mode. |
| AssociatedInstan ceId | String | No | i-2zebb08phyccd vf\*\*\*\* | The ID of the cloud resource with which the EIP is associated. |
| ChargeType | String | No | None | The billing method of the EIP. Valid values:<br>• <strong>PostPaid</strong>: pay-as-you-go<br>• <strong>PrePaid</strong>: subscription |
| DryRun | Boolean | No | false | Specifies whether to precheck only this request. Valid values:<br>• <strong>true</strong>: prechecks the request only.EIPs are not queried. The system checks the required parameters, request syntax, and service limits.If the request fails the precheck, the corresponding error message is returned. If the request passes the precheck, the <code> DryRunOperation </code> error code is returned.<br>• <strong>false</strong>: prechecks the request. This is the default value. After the request passes the check, a 2xx HTTP status code is returned and EIPs are queried. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EipAddresses | Array of EipAddress |  | The details about the EIP. |
| EipAddress |  |  |  |
| AllocationId | String | eip-2zeerraiwb7ujcdvf\* \*\*\* | The ID of the EIP. |
| AllocationTime | String | 2019-04-23T01:37:38Z | The time when the EIP was created. |
| AvailableRegio ns | List | cn-east-hangzhou-01 | The ID of the region to which the EIP belongs. |
| Bandwidth | String | 5 | The bandwidth limit of the EIP. Unit: Mbit/s. |
| BandwidthPac kageBandwidt h | String | 50 | The bandwidth of the EIP bandwidth plan.Unit: Mbit/s. |
| BandwidthPac kageId | String | cbwp-bp1ego3i4j07ccdvf \*\*\*\* | The ID of the EIP bandwidth plan. |
| BandwidthPac kageType | String | CommonBandwidth Package | The type of the bandwidth. Only <strong>CommonBandwidthPackage</strong> (EIP Bandwidth Plan) is returned. |
| ChargeType | String | PostPaid | The billing method of the EIP.<br>• <strong>PrePaid</strong>: subscription<br>• <strong>PostPaid</strong>: pay-as-you-go |
| DeletionProtec tion | Boolean | true | Indicates whether deletion protection is enabled. Valid values:<br>• <strong>true</strong>: enabled<br>• <strong>false</strong>: disabled |
| Descritpion | String | abc | The description of the EIP. |
| EipBandwidth | String | 101 | The bandwidth limit of the EIP when it is not associated with an EIP bandwidth plan. |
| ExpiredTime | String | 2019-04-29T02:00Z | The expiration date. The time follows the ISO 8601 standard and is displayed in UTC. Format: <code> YYYY-MM-ddTHH:mmZ </code>. |
| HDMonitorStat us | String | false | Indicates whether fine-grained monitoring is enabled for the EIP. Valid values:<br>• <strong>false</strong>: disabled<br>• <strong>true</strong>: enabled |
| HasReservatio nData | String | false | Indicates whether renewal data is included.<br>This parameter returns <strong>true</strong> only when the <strong>IncludeReservationData</strong> parameter is set to <strong>true</strong> and some orders have not taken effect. |
| ISP | String | BGP | The ISP. |
| InstanceId | String | i-bp15zckdt37cdvf\*\* \*\* | The ID of the instance with which the EIP is associated. |
| InstanceRegio nId | String | cn-east-hangzhou-01 | The region ID of the associated resource. |
| InstanceType | String | EcsInstance | The type of the instance associated with the EIP. Valid values:<br>• <strong>EcsInstance</strong>: an ECS instance in a VPC.<br>• <strong>SlbInstance</strong>: an SLB instance in a VPC.<br>• <strong>Nat</strong>: a NAT gateway.<br>• <strong>HaVip</strong>: an HAVIP.<br>• <strong>NetworkInterface</strong>: a secondary ENI. |
| InternetCharg eType | String | PayByBandwidth | The metering method of the EIP. Valid values:<br>• <strong>PayByBandwidth</strong>: pay-by-bandwidth<br>• <strong>PayByTraffic</strong>: pay-by-data-transfer |
| IpAddress | String | 101.xx.xx.36 | The IP address of the EIP. |
| Mode | String | NAT | The association mode. Valid values:<br>• <strong>NAT</strong> (default): the standard NAT mode<br>• <strong>MULTI_BINDED</strong>: multi-EIP-to-ENI mode<br>• <strong>BINDED</strong>: cut-through mode<br>This parameter is returned only when <strong>InstanceType</strong> is set to <strong>NetworkInterface</strong>. |
| Name | String | test | The name of the EIP. |
| Netmode | String | public | The type of network. The value <strong>public</strong> (Internet) is returned. |
| OperationLock s | Array of LockReason |  | The details about the locked EIP. |
| LockReason |  |  |  |
| LockReason | String | financial | The reason why the EIP is locked. Valid values:<br>• <strong>financial</strong>: The EIP is locked due to overdue payments.<br>• <strong>security</strong>: The EIP is locked for security reasons. |
| PrivateIpAddre ss | String | 192.1.XX.XX | An IP address in the CIDR block of the vSwitch. |
| RegionId | String | cn-east-hangzhou-01 | The ID of the region to which the EIP belongs. |
| ReservationAc tiveTime | String | 2019-03-11T16:00:00Z | The time when the renewal takes effect. |
| ReservationBa ndwidth | String | 12 | The bandwidth after the renewal takes effect. |
| ReservationInt ernetChargeTy pe | String | PayByBandwidth | The metering method of the renewal. Valid values:<br>• <strong>PayByBandwidth</strong>: pay-by-bandwidth<br>• <strong>PayByTraffic</strong>: pay-by-data-transfer |
| ReservationOr derType | String | RENEWCHANGE | The type of the renewal order. Valid values:<br>• <strong>RENEWCHANGE</strong>: upgrade or downgrade<br>• <strong>TEMP_UPGRADE</strong>: temporary upgrade<br>• <strong>UPGRADE</strong>: upgrade |
| ResourceGrou pId | String | rg-acfmxazcdxs\*\*\*\* | The ID of the resource group. |
| SecondLimited | Boolean | false | Indicates whether level-2 throttling is configured. Valid values:<br>• <strong>true</strong>: yes<br>• <strong>false</strong>: no |
| SegmentInsta nceId | String | eipsg-t4nr90yik5oy38xdy jth8 | The IDs of contiguous EIPs.<br>This value is returned only when contiguous EIPs are specified. |
| Status | String | Associating | The status of the EIP. Valid values:<br>• <strong>Associating</strong>: The EIP is being associated with an instance.<br>• <strong>Unassociating</strong>: The EIP is being disassociated from an instance.<br>• <strong>InUse</strong>: The EIP is associated with an instance.<br>• <strong>Available</strong>: The EIP is available. |
| Tags | Array of Tag |  | The tags used to query resources. |
| Tag |  |  |  |
| Key | String | testX | The filter key used to query resources. |
| Value | String | testY | The filter value used to query resources. |
| TotalCount | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74-4534-BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeEipAddresses
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeEipAddressesResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <EipAddresses>
        <HDMonitorStatus>false</HDMonitorStatus>
        <PrivateIpAddress>192.1.XX.XX</PrivateIpAddress>
        <ResourceGroupId>rg-acfmxazcdxs****</ResourceGroupId>
        <AllocationId>eip-2zeerraiwb7ujcdvf****</AllocationId>
        <SecondLimited>false</SecondLimited>
        <Name>test</Name>
        <SegmentInstanceId>eipsg-t4nr90yik5oy38xdyjth8</SegmentInstanceId>
        <ReservationOrderType>RENEWCHANGE</ReservationOrderType>
        <InstanceRegionId>cn-east-hangzhou-01</InstanceRegionId>
        <ExpiredTime>2019-04-29T02:00Z</ExpiredTime>
        <Bandwidth>5</Bandwidth>
        <BandwidthPackageId>cbwp-bp1ego3i4j07ccdvf****</BandwidthPackageId>
        <ReservationActiveTime>2019-03-11T16:00:00Z</ReservationActiveTime>
        <InstanceType>EcsInstance</InstanceType>
        <ReservationBandwidth>12</ReservationBandwidth>
        <Status>Associating</Status>
        <InstanceId>i-bp15zckdt37cdvf****</InstanceId>
        <Mode>NAT</Mode>
        <ISP>BGP</ISP>
        <HasReservationData>false</HasReservationData>
        <DeletionProtection>true</DeletionProtection>
        <BandwidthPackageType>CommonBandwidthPackage</BandwidthPackageType>
        <BandwidthPackageBandwidth>50</BandwidthPackageBandwidth>
        <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
        <InternetChargeType>PayByBandwidth</InternetChargeType>
        <AllocationTime>2019-04-23T01:37:38Z</AllocationTime>
        <Descritpion>abc</Descritpion>
        <EipBandwidth>101</EipBandwidth>
        <Netmode>public</Netmode>
        <ChargeType>PostPaid</ChargeType>
        <IpAddress>101.xx.xx.36</IpAddress>
        <RegionId>cn-east-hangzhou-01</RegionId>
        <OperationLocks>
              <LockReason>financial</LockReason>
        </OperationLocks>
        <Tags>
              <Value>testY</Value>
              <Key>testX</Key>
        </Tags>
        <AvailableRegions>cn-east-hangzhou-01</AvailableRegions>
  </EipAddresses>
  <PageNumber>10</PageNumber>
</DescribeEipAddressesResponse>
```

`JSON`  format

```json
{
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "EipAddresses": {
        "HDMonitorStatus": false,
        "PrivateIpAddress": "192.1.XX.XX",
        "ResourceGroupId": "rg-acfmxazcdxs****",
        "AllocationId": "eip-2zeerraiwb7ujcdvf****",
        "SecondLimited": false,
        "Name": "test",
        "SegmentInstanceId": "eipsg-t4nr90yik5oy38xdyjth8",
        "ReservationOrderType": "RENEWCHANGE",
        "InstanceRegionId": "cn-east-hangzhou-01",
        "ExpiredTime": "2019-04-29T02:00Z",
        "Bandwidth": 5,
        "BandwidthPackageId": "cbwp-bp1ego3i4j07ccdvf****",
        "ReservationActiveTime": "2019-03-11T16:00:00Z",
        "InstanceType": "EcsInstance",
        "ReservationBandwidth": 12,
        "Status": "Associating",
        "InstanceId": "i-bp15zckdt37cdvf****",
        "Mode": "NAT",
        "ISP": "BGP",
        "HasReservationData": false,
        "DeletionProtection": true,
        "BandwidthPackageType": "CommonBandwidthPackage",
        "BandwidthPackageBandwidth": 50,
        "ReservationInternetChargeType": "PayByBandwidth",
        "InternetChargeType": "PayByBandwidth",
        "AllocationTime": "2019-04-23T01:37:38Z",
        "Descritpion": "abc",
        "EipBandwidth": 101,
        "Netmode": "public",
        "ChargeType": "PostPaid",
        "IpAddress": "101.xx.xx.36",
        "RegionId": "cn-east-hangzhou-01",
        "OperationLocks": {
            "LockReason": "financial"
        },
        "Tags": {
            "Value": "testY",
            "Key": "testX"
        },
        "AvailableRegions": "cn-east-hangzhou-01"
    },
    "PageNumber": 10
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the region is valid. |
| 404 | InvalidLockReason.NotFound | The specified LockReason is not found | The error message returned because the reason why the EIP is locked is unknown. |
| 400 | InvalidIAssociatedI nstanceType.Value NotSupported | The specified value of AssociatedInstanceType is not supported. | The error message returned because AssociatedInstanceType is set to an invalid value. Check whether the value is valid. |
| 400 | InvalidChargeType.ValueNotSupported | The specified ChargeType is not supported. | The error message returned because the specified billing method is not supported. Set a supported billing method. |
| 400 | InvalidResourceGro upId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |
| 400 | OperationUnsuppor ted.ResourceGroup Id | ResourceGroup is not supported in this region. | The error message returned because the resource group feature is disabled. |

<a id="section-5-5-9"></a>

### 5.5.9. UnassociateEipAddress

Disassociates an elastic IP address (EIP) from an instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | UnassociateEipA ddress | The operation that you want to perform. Set the value to <strong>UnassociateEipAddress</strong>. |
| AllocationId | String | Yes | eip-2zeerraiwb7uj6i 0d\*\*\*\* | The ID of the EIP that you want to disassociate. |
| InstanceId | String | Yes | i-hp3akk9irtd69ja d\*\*\*\* | The ID of the instance from which you want to disassociate the EIP. |
| Force | Boolean | No | false | Specifies whether to disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. Valid values:<br>• <strong>false</strong> (default): does not disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway.<br>• <strong>true</strong>: disassociates the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance from which you want to disassociate the EIP. Valid values:<br>• <strong>EcsInstance</strong> (default): an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC)<br>• <strong>SlbInstance</strong>: a Server Load Balancer (SLB) instance that is deployed in a VPC<br>• <strong>NetworkInterface</strong>: a secondary elastic network interface (ENI) that is deployed in a VPC<br>• <strong>Nat</strong>: a NAT gateway<br>• <strong>HaVip</strong> a high-availability virtual IP address (HAVIP) |
| PrivateIpAddress | String | No | 192.XX.XX.2 | The private IP address of the ECS instance or the secondary ENI from which you want to disassociate the EIP. |
| ClientToken | String | No | 02fb3da4-130e-11e9-8e44-001\*\*\* | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0ED8D006-F706-4D23-88ED-E11ED28DCAC0 | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=UnassociateEipAddress
&AllocationId=eip-2zeerraiwb7uj6i0d****
&InstanceId=i-hp3akk9irtd69jad****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<UnassociateEipAddressResponse>
   <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</UnassociateEipAddressResponse>
```

`JSON`  format

```json
{ 
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | InvalidAllocationId.NotFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 400 | InvalidInstanceId.N otFound | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the specified instance is valid. |
| 400 | IncorrectInstanceSt atus | The current status of instance does not support this operation. | The error message returned because the state of the instance does not support the operation. |
| 400 | InvalidInstanceTyp e.ValueNotSupport ed | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStat us | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified HAVIP is in the Available or InUse state. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because EIPs in the default VPC do not support the operation. |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the parameter is set to an invalid value. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatu s | The eip binding status invalid. | The error message returned because the binding mode of the EIP is invalid. |

<a id="section-5-5-10"></a>

### 5.5.10. ReleaseEipAddress

Releases a specified elastic IP address (EIP).

**Description**

Before you release an EIP, make sure that the EIP meets the following requirements:

- You can release only EIPs that are in the **Available** state.

- You can release only EIPs that are billed on a pay-as-you-go basis. You cannot release subscription EIPs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ReleaseEipAddr ess | The operation that you want to perform. Set the value to <strong>ReleaseEipAddress</strong>. |
| AllocationId | String | Yes | eip-2zeerraiwb7uj6i 0d\*\*\*\* | The ID of the EIP that you want to release. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region to which the EIP belongs. You can call the <code> DescribeRegions </code> operation to query region IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 748C38F6-9A3D-482E-83FB-DB6C39C68AEA | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ReleaseEipAddress
&AllocationId=eip-2zeerraiwb7uj6i0d****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ReleaseEipAddressResponse>
      <RequestId>748C38F6-9A3D-482E-83FB-DB6C39C68AEA</RequestId>
</ReleaseEipAddressResponse>
```

`JSON`  format

```json
{
  "RequestId": "748C38F6-9A3D-482E-83FB-DB6C39C68AEA"
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | InvalidAllocationId.NotFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | Forbidden.ChargeT ypeIsPrepaid | It's forbidden to release a prepaid EIP | The error message returned because you cannot release subscription EIPs. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | TaskConflict.Associ ateGlobalAccelerati onInstance | Operate too frequent. | The error message returned because the number of requests that you send exceeds the upper limit. |

<a id="section-5-5-11"></a>

### 5.5.11. DescribeEipGatewayInfo

Queries information about the gateway and subnet mask of an elastic IP address (EIP).

**Description**

You can query only EIPs that are associated with secondary elastic network interfaces (ENIs) in multi-EIP to ENI mode.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeEipGate wayInfo | The operation that you want to perform. Set the value to <strong>DescribeEipGatewayInfo</strong>. |
| InstanceId | String | Yes | eni-bp1d66qjxb3qoi n3\*\*\*\* | The ID of the secondary ENI that is associated with the EIP. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region to which the EIP that you want to query belongs. You can call the <code> DescribeRegions </code> operation to query region IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Code | String | 200 | The status code of the operation. |
| EipInfos | Array of EipInfo |  | Detailed information about the EIP. |
| EipInfo |  |  |  |
| Ip | String | 47.XX.XX.236 | The IP address of the EIP. |
| IpGw | String | 47.XX.XX.1 | The IP address of the gateway that is associated with the EIP. |
| IpMask | String | 255.255.255.0 | The subnet mask of the EIP. |
| Message | String | successful | The result of the operation. |
| RequestId | String | C0FD0EED-F90D-4479-803D-DD62335357E5 | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeEipGatewayInfo
&InstanceId=eni-bp1d66qjxb3qoin3****
&RegionId=cn-qingdao-env17-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeEipGatewayInfoResponse>
  <Message>successful</Message>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5    </RequestId>
  <Code>200</Code>
  <EipInfos>
        <IpMask>255.255.255.0</IpMask>
        <IpGw>47.XX.XX.1</IpGw>
        <Ip>47.XX.XX.236</Ip>
  </EipInfos>
</DescribeEipGatewayInfoResponse>
```

`JSON`  format

```json
{
    "Message": "successful",
    "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5",
    "Code": 200,
    "EipInfos": {
        "IpMask": "255.255.255.0",
        "IpGw": "47.XX.XX.1",
        "Ip": "47.XX.XX.236"
    }
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |

<a id="section-5-5-12"></a>

### 5.5.12. DescribeEipMonitorData

Queries the monitoring data of an elastic IP address (EIP).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeEipMoni torData | The operation that you want to perform. Set the value to <strong>DescribeEipMonitorData</strong>. |
| AllocationId | String | Yes | eip-2zeerraiwb7uj6i dcfv\*\*\*\* | The ID of the EIP. |
| EndTime | String | Yes | 2017-01-05T01:05:10Z | The end of the time range to query.The time must be in UTC. The time follows the ISO 8601 standard and is displayed in the YYYY-MM-DDThh:mm:ssZ format. Example: 2013-01-10T12:00:00Z, which specifies 20:00:00 (UTC+8) on January 10, 2013.<br>If the value of seconds (ss) is not 00, the end time is automatically rounded up to the next minute. |
| StartTime | String | Yes | 2017-01-05T02:05:05Z | The beginning of the time range to query. The time must be in UTC. The time follows the ISO 8601 standard and is displayed in the YYYY-MM-DDThh:mm:ssZ format. Example: 2013-01-10T12:00:00Z, which specifies 20:00:00 (UTC+8) on January 10, 2013.<br>If the value of seconds (ss) is not 00, the start time is automatically rounded up to the next minute. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region to which the EIP belongs. |
| Period | Integer | No | 60 | The duration of each monitoring data entry. Valid values: <strong>60</strong>, <strong>300</strong>, <strong>900</strong>, and <strong>3600</strong>. Default value: 60. Unit: seconds.<br>• If the value of (EndTime-StartTime)/Period is greater than 200, a maximum of 200 monitoring data entries are returned at a time.<br>• If the value of (EndTime-StartTime)/Period is less than or equal to 200, only the monitoring data collected between the start time and end time are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EipMonitorDat as | Array of EipMonitorDat a |  | The detailed information about the monitoring data of the EIP. |
| EipMonitorDat a |  |  |  |
| EipBandwidth | Integer | 10 | The bandwidth. This value is equal to that of EipFlow/60. Unit: bit/s. |
| EipFlow | Integer | 675 | The sum of the inbound and outbound bandwidth. |
| EipPackets | Integer | 3434 | The number of packages. |
| EipRX | Long | 122 | The inbound bandwidth. Unit: Bit/s. |
| EipTX | Long | 343 | The outbound bandwidth. Unit: Bit/s. |
| TimeStamp | String | 2010-01-21T09:50:23Z | The timestamp of the monitoring data.The time follows the ISO 8601 standard.Example: 2018-12-20T03:14:00Z. |
| RequestId | String | C8B26B44-0189-443E-9816-D951F59623A9 | The ID of the request. |

**Examples**

Sample requests

```text
https://vpc.aliyuncs.com/?Action=DescribeEipMonitorData
&AllocationId=eip-2zeerraiwb7uj6idcfv****
&EndTime=2017-01-05T01:05:10Z
&StartTime=2017-01-05T02:05:05Z
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeEipMonitorDataResponse>
   <RequestId>B7D72D42-8A6C-4764-963B-5F7C049FA769</RequestId>
   <EipMonitorDatas>
      <EipMonitorData>
         <TimeStamp>2019-05-29T03:39:00Z</TimeStamp>
         <EipFlow>32666910</EipFlow>
         <EipTX>140370</EipTX>
         <EipPackets>23700</EipPackets>
         <EipRX>32526540</EipRX>
         <EipBandwidth>544448</EipBandwidth>
      </EipMonitorData>
      <EipMonitorData>
         <TimeStamp>2019-05-29T03:40:00Z</TimeStamp>
         <EipFlow>43020</EipFlow>
         <EipTX>17730</EipTX>
         <EipPackets>120</EipPackets>
         <EipRX>25290</EipRX>
         <EipBandwidth>717</EipBandwidth>
      </EipMonitorData>
   </EipMonitorDatas>
</DescribeEipMonitorDataResponse>
```

`JSON`  format

```json
{
    "DescribeEipMonitorDataResponse": {
        "RequestId": "B7D72D42-8A6C-4764-963B-5F7C049FA769",
        "EipMonitorDatas": {
            "EipMonitorData": [
                {
                    "TimeStamp": "2019-05-29T03:39:00Z",
                    "EipFlow": 32666910,
                    "EipTX": 140370,
                    "EipPackets": 23700,
                    "EipRX": 32526540,
                    "EipBandwidth": 544448
                },
                {
                    "TimeStamp": "2019-05-29T03:40:00Z",
                    "EipFlow": 43020,
                    "EipTX": 17730,
                    "EipPackets": 120,
                    "EipRX": 25290,
                    "EipBandwidth": 717
                }
            ]
        }
    }
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 404 | InvalidInstanceId.N otFound | The InstanceId provided does not exist in our records. | The error message returned because the specified Elastic Compute Service (ECS) instance is not found in the specified VPC. |
| 400 | InvalidStartTime.M alformed | The specified parameter "StartTime" is not valid. | The error message returned because the start time is invalid. |
| 400 | InvalidEndTime.Mal formed | The specified parameter "EndTime" is not valid. | The error message returned because the end time is invalid. |
| 400 | InvalidPeriod.Value NotSupported | The specified parameter "Period" is not valid. | The error message returned because the value of the Period parameter is invalid. |
| 400 | InvalidStartTime.To oEarly | The specified parameter "StartTime" is too early. | The error message returned because the start time is invalid. |
| 400 | InvalidAllocationId.NotFound | Specified allocation id is not found. | The error message returned because the specified EIP does not exist. Check whether the EIP is valid. |
| 400 | OperationDenied.T ooManyDataQuerie d | Specified operation is denied as too many data to return. | The error message returned because an excessive amount of data is returned for a single query. |
| 404 | Forbidden.RegionN otFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the region ID is valid. |

<a id="section-5-5-13"></a>

### 5.5.13. MoveResourceGroup

Moves a resource to a different resource group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | MoveResourceG roup | The operation that you want to perform. Set the value to <strong>MoveResourceGroup</strong>. |
| NewResourceGr oupId | String | Yes | rg-acfm3peow3k\*\* \*\* | The ID of the resource group to which the cloud resource is to be moved.<br>Note You can use resource groups to manage resources owned by your Apsara Stack account. Resource groups simplify the resource and permission management of your Apsara Stack account. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The region ID of the cloud resource.<br>You can call the <code> DescribeRegions </code> operation to query the most recent region list. |
| ResourceId | String | Yes | vpc-hp31psbg8ec30 23s6\*\*\*\* | The ID of the instance that you want to move. |
| ResourceType | String | Yes | vpc | The type of the cloud resource. Valid values:<br>• <strong>vpc</strong>: a virtual private cloud (VPC)<br>• <strong>eip</strong>: an elastic IP address (EIP) |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F84A05B3-7275-4C8B-8AEE-9088C639C271 | The ID of the request. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=MoveResourceGroup
&NewResourceGroupId=rg-acfm3peow3k****
&RegionId=cn-qingdao-env17-d01
&ResourceId=vpc-hp31psbg8ec3023s6****
&ResourceType=vpc
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<MoveResourceGroup>
  <RequestId>F84A05B3-7275-4C8B-8AEE-9088C639C271</RequestId>
</MoveResourceGroup>
```

`JSON`  format

```json
{
    "RequestId": "F84A05B3-7275-4C8B-8AEE-9088C639C271"
}
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidResourceGro upId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

<a id="section-5-5-14"></a>

### 5.5.14. DescribeHighDefinitionMonitorLogAttribute

Queries configurations about the fine-grained monitoring feature of an elastic IP address (EIP).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeHighDef initionMonitorLo gAttribute | The operation that you want to perform. Set the value to DescribeHighDefinitionMonitorLo <strong>gAttribute</strong>. |
| InstanceId | String | Yes | eip-wz9fi6qboho9fw gx7\*\*\*\* | The ID of the instance whose fine-grained monitoring configurations you want to query. |
| RegionId | String | Yes | cn-qingdao-env66-d01 | The region ID of the instance.<br>You can call the <code> DescribeRegions </code> operation to query the most recent region list. |
| InstanceType | String | No | EIP | The type of the instance. Set the value to <strong>EIP</strong>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| InstanceId | String | eip-wz9fi6qboho9fwgx 7\*\*\*\* | The ID of the instance whose fine-grained monitoring configurations you want to query. |
| InstanceType | String | EIP | The type of the monitoring instance that is queried. The value is set to <strong>EIP</strong>. |
| LogProject | String | hdmonitor-cn-qingdao-165820696\*\*\*\* | The name of the project of Log Service. |
| LogStore | String | hdmonitor | The name of the Logstore of Log Service. |
| RequestId | String | 54B48E3D-DF70-471B-AA93-08E683A1B457 | The ID of the request. |
| Success | String | true | Indicates whether the operation is performed. Valid values:<br>• <strong>true</strong>: yes<br>• <strong>false</strong>: no |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeHighDefinitionMonitorLogAttribute
&InstanceId=eip-wz9fi6qboho9fwgx7****
&RegionId=cn-qingdao-env66-d01
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeHighDefinitionMonitorLogAttribute>
  <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
  <LogStore>hdmonitor</LogStore>
  <InstanceId>eip-wz9fi6qboho9fwgx7****</InstanceId>
  <InstanceType>EIP</InstanceType>
  <LogProject>hdmonitor-cn-qingdao-165820696****</LogProject>
  <Success>true</Success>
</DescribeHighDefinitionMonitorLogAttribute>
```

`JSON`  format

```json
{
    "DescribeHighDefinitionMonitorLogAttribute": {
        "RequestId": "54B48E3D-DF70-471B-AA93-08E683A1B457",
        "LogStore": "hdmonitor",
        "InstanceId": "eip-wz9fi6qboho9fwgx7****",
        "InstanceType": "EIP",
        "LogProject": "hdmonitor-cn-qingdao-165820696****",
        "Success": true
    }
}
```

<a id="section-6"></a>

# 6.Appendixes

<a id="section-6-1"></a>

## 6.1. STS overview

<a id="section-6-1-1"></a>

### 6.1.1. What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use a RAM user to obtain an STS token**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources.

**Benefits**

- STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user.

- STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis.

- You can attach custom policies to STS tokens for flexible and fine-grained authorization.

<a id="section-6-1-2"></a>

### 6.1.2. Obtain an STS token

You can call the AssumeRole operation to obtain a Security Token Service (STS) token. A Resource Access Management (RAM) user can use the STS token to assume a RAM role whose trusted entity is an Alibaba Cloud account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | Obtain an STS token | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012\*\*\*\*:role/adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role.<br>The trusted entity of the RAM role is an Alibaba Cloud account. |
| RoleSessionNa me | String | Yes | alice | The custom name of the role session.<br>Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the API caller. For example, you can specify a username. You can specify <strong>RoleSessionName</strong> to identify API callers that assume the same RAM role in ActionTrail logs. This allows you to track the users that perform the operations.<br>The value must be 2 to 64 characters in length, and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). |
| Policy | String | No | {"Statement": \[{"Action": \["\*"\],"Effect": "Allow","Resourc e": \["\*"\]}\],"Version":" 1"} | The policy that specifies the permissions of the returned STS token.You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. Details:<br>• If you specify this parameter, the permissions of the returned STS token are the permissions that are included in the value of this parameter and owned by the RAM role.<br>• If you do not specify this parameter, the returned STS token has all the permissions of the RAM role.<br>The value of the parameter must be 1 to 1,024 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6894B13B-6D71-4EF5-88FA-F32781734A7F | The request ID. |
| Credentials | N/A | None | The STS credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1\*\*\*\* | The AccessKey ID. |
| AccessKeySecret | String | wyLTSmsyPGP1ohv vw8xYgB29dlGI8KM iH2pK\*\*\*\* | The AccessKey secret. |
| SecurityToken | String | \*\*\*\*\*\*\*\* | The STS token. |
| Expiration | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | N/A | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::12345678 9012\*\*\*\*:role/admi nrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495\*\* \*\*:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS 3-tuple.**

In the following sample code, the  `Sts::AssumeRole::2015-04-01`  operation is used to obtain the 3-tuple.

```xml
package com.aliyuns.test;

import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.HttpClientConfig;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.profile.DefaultProfile;
import org.apache.commons.lang3.StringUtils;

public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance. 
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the endpoint is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the current role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role in the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS 3-tuple.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " 
+ stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        }
    }
}
```

**Sample requests**

In the following sample code, the  `DescribeZones`  operation in Elastic Compute Service (ECS) is used.

```xml
package com.aliyuns.test;

import com.aliyuncs.CommonRequest;
importcom.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.HttpClientConfig;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.profile.DefaultProfile;

public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the 
AccessKey ID and AccessKey secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain("ecs.aliyuns.com");
        request.setSysProduct("Ecs");
        request.setSysAction("DescribeZones");
        request.setSysVersion("2014-05-26");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained 
in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Specify the resource set ID. This parameter is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. This parameter is required.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        }
    }
}
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length, and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid.The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
