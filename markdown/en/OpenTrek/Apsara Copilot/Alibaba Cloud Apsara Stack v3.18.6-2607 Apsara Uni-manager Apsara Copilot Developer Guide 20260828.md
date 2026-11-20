Alibaba Cloud  
Apsara Stack  
Apsara Uni-manager  
Apsara Copilot Developer  
Guide  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Preparations](#section-1)
    - [1.1. Obtain the information and the endpoint of an API operation](#section-1-1)
    - [1.2. Obtain an AccessKey pair](#section-1-2)
    - [1.3. Obtain the values of common request headers](#section-1-3)
    - [1.4. Obtain access credentials assigned by STS](#section-1-4)
- [2.Use POP to make API calls](#section-2)
    - [2.1. Preparations](#section-2-1)
    - [2.2. SDK for Java](#section-2-2)
    - [2.3. Go](#section-2-3)
    - [2.4. Python version](#section-2-4)
- [3.API list](#section-3)
    - [3.1. IntelligentAnalysis](#section-3-1)
    - [3.2. IntelligentSearch](#section-3-2)
    - [3.3. IntelligentQa](#section-3-3)
    - [3.4. CreateChat](#section-3-4)
    - [3.5. IntelligentCoding](#section-3-5)
    - [3.6. GetChatHistory](#section-3-6)
    - [3.7. ListHistoryChats](#section-3-7)
    - [3.8. PushChatMessage](#section-3-8)
    - [3.9. MessageFeedback](#section-3-9)
    - [3.10. DeleteChat](#section-3-10)

<a id="section-1"></a>

# 1.Preparations

<a id="section-1-1"></a>

## 1.1. Obtain the information and the endpoint of an API operation

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

<a id="section-1-2"></a>

## 1.2. Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization.

**Background information**

AccessKey supports the following authorization methods:

- Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters.

- Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters.

This topic describes how to obtain an AccessKey pair authorized by RAM. For more information about how to obtain an AccessKey pair authorized by STS, see **Obtain an STS AccessKey pair**.

We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
| --- | --- |
| x-acs-regionid | The ID of the region, such as cn-hangzhou-\*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

> **Warning**
>
> The AccessKey pair of a personal account is managed and controlled by
>
> the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console.

2. In the upper-right corner of the homepage, move the pointer over the profile picture and choose **User Information** from the shortcut menu.

3. In the **Apsara Stack AccessKey Pair** section, obtain the AccessKey pair.

   ![](assets/a0c6c22806c62349a0f9840932305e11.png)

   > **Note**
   >
   > The AccessKey pair consists of an AccessKey ID and an AccessKey secret.
   >
   > These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Resources > Organizations**.

4. In the organization navigation tree, click the name of the level-1 organization for which you want to obtain AccessKey pairs.

5. Click **Management AccessKey** on the right side of the page.

6. In the AccessKey message, view the AccessKey pair of the organization.

<a id="section-1-3"></a>

## 1.3. Obtain the values of common request headers

You must provide multiple request headers when you call API operations in Apsara Stack. This topic describes how to obtain the values of common request headers. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Resources** > **Regions**.

4. Click the name of the desired organization.

5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain an organization ID. You can obtain an organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI Explorer**.

3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top navigation bar.

4. Move the pointer over the <img src="assets/a399ea52e5bed707f6f6a0b92044c5ca.png" width="26" alt=""> icon and choose **Platform** > **Apsara Uni-manager**. Select

   **2019-05-10** from the **Version** drop-down list.

5. Search for the  `GetOrganizationList`  operation and debug the operation online. Set the name parameter to the name of the organization that you want to query and click Initiate Call. Obtain the organization ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the *GetOrganizationList* topic in *Apsara Uni-manager Operations Console Developer Guide*.

**Obtain a resource set ID**

You must call a specific API operation to obtain a resource set ID. You can obtain a resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI Explorer**.

3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top navigation bar.

4. Move the pointer over the <img src="assets/a399ea52e5bed707f6f6a0b92044c5ca.png" width="26" alt=""> icon and choose **Platform** > **Apsara Uni-manager**. Select

   **2019-05-10** from the **Version** drop-down list.

5. Search for the  `ListResourceGroup`  operation and debug the operation online. Obtain the resource set ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the *ListResourceGroup* topic in *Apsara Uni-manager Operations Console Developer Guide*.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an API gateway, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console.

2. In the top navigation bar, choose **Products** > Application Services > API Gateway.

3. In the left-side navigation pane, click **Instances**.

4. View the **instance ID** in the instance list.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
| --- | --- |
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of a resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of an organization. |

<a id="section-1-4"></a>

## 1.4. Obtain access credentials assigned by STS

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your  `Resource Access Management (RAM) role` .

   <ol type="i">

   <li>

   Log on to the Apsara Uni-manager Management Console.

   </li>

   <li>

   In the upper-right corner of the homepage, click the profile picture and then click **User**

   </li>

   </ol>

   **Information**.

   <ol type="i" start="3">

   <li>

   On the page that appears, click **View Current Role Policy**.

   </li>

   </ol>

   In the **View Policies of Current Role** dialog box, view the ARN of your  `RAM role` .

2. Use the following code to obtain an AccessKey ID ( `stsAK` ), AccessKey secret ( `stsSK` ), and STS token ( `stsToken` ) by assuming the  `RAM role` .

   ```java
   public static void main(String[] args) {
        ASClient asClient = new ASClient();
        // Specify the description of the call source.
           asClient.setSdkSource("test");
        // Specify the ARN.
           String assumeRole = AssumeRole(asClient, "<RAM Role>");

           JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);

           JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");

           // Obtain the access credentials assigned by STS.
           String stsAK = credentials.getString("AccessKeyId");
           String stsSK = credentials.getString("AccessKeySecret");
           String stsToken = credentials.getString("SecurityToken");
   }

   public static String AssumeRole(ASClient asClient, String roleArn) {

           Map<String, String> headers = new HashMap<>();

           Map<String, Object> reqParams = new HashMap<>();

           reqParams.put("action", "AssumeRole");

           reqParams.put("Product", "Sts");

           reqParams.put("Version", "2015-04-01");

           reqParams.put("regionId", regionId);

        // The AccessKey ID of the current user.
           reqParams.put("AccessKeyId", <The AccessKey ID of the current user>);
        // The AccessKey secret of the current user.
           reqParams.put("AccessKeySecret", <The AccessKey secret of the current user>);

           reqParams.put("roleSessionName", "StsUser");

           reqParams.put("roleArn", roleArn);

           return asClient.doRequest(endpoint, headers, reqParams);
   }
   ```

3. Use the access credentials assigned by STS to call an API operation of a cloud service. In this example, the Elastic Compute Service (ECS) API is used.

   ```java
   public static void main(String[] args) {
        ASClient asClient = new ASClient();
           asClient.setSdkSource("test");
     // Call an API operation of ECS.
           String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
   }


   public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, String stsToken) {

           Map<String, String> headers = new HashMap<>();

           Map<String, Object> reqParams = new HashMap<>();

           reqParams.put("action", "DescribeZones");

           reqParams.put("Product", "Ecs");

           reqParams.put("Version", "2014-05-26");

           reqParams.put("regionId", "<your-RegionID>");

           // Specify the AccessKey ID, AccessKey secret, and STS token.
           reqParams.put("AccessKeyId", <stsAK>);
           reqParams.put("AccessKeySecret", <stsSK>);
           reqParams.put("SecurityToken", <stsToken>);

           return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);

       }
   ```

<a id="section-2"></a>

# 2.Use POP to make API calls

<a id="section-2-1"></a>

## 2.1. Preparations

You can use the POP gateway to call Apsara Stack API operations in the same way as you do for Alibaba Cloud. This topic describes the required preparations.

**Background information**

For a convenient and consistent experience similar to using Alibaba Cloud, we recommend that you use the POP gateway to call Apsara Stack API operations.

**Obtain a product endpoint**

**Obtain an endpoint from the Developer Portal**

1. Log on to the Apsara Uni-manager Management Console.

2. In the top menu bar, choose **Products** > **Development Tools** > **API & Tools** > **Developer Portal**.

3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.

   ![](assets/2c46abb9ede40ba27b69fc91474a92c6.jpeg)

4. In the navigation pane on the left, select the target product.

5. From the **Version** drop-down list, select the target API version.

6. In the API list, you can view all API operations for the current version.

7. Select an API operation and obtain the POP Endpoint information under the parameter name.

**Obtain an endpoint from Apsara Infrastructure Management**

When you use the POP gateway to call Apsara Stack API operations, you must use the product's service domain Endpoint. You can obtain the Endpoint from an onsite Alibaba Cloud O&M engineer.

You can also obtain the Endpoint yourself. The following procedure describes how to do this.

1. Log on to the Apsara Uni-manager Operations Console.

2. In the top menu bar, choose **Platform O&M** > **Apsara Infrastructure Management** > **Resource Management**.

3. In the navigation pane on the left, choose **Resource Management** > **Product Cluster O&M**.

4. On the **Product Cluster O&M** page, enter  `apsara-copilot`  in the **Product|Cluster** field.

5. In the **Operation** column of the cluster, click **Cluster Details**.

6. On the **Cluster Details** page, click the **Resource Details** tab.

7. On the Resource Details tab, find the resource with the name  `copilot-api-dns`  and type

   `dns` . Then, click the <img src="assets/f9387f3709671f07787cb98488ef1c63.png" width="19" alt=""> icon in the **Resource Request Result** column.

8. Click the text in the **Resource Request Result** column. In the dialog box that appears, you can view the domain value. This value is the  `Endpoint` .

**Obtain common parameters**

For information about how to obtain common parameters, such as the organization ID, resource set ID, region ID, and instance ID, see the **Obtain common header parameters** section in the **Preparations** topic of this guide. These parameters are used to call Apsara Stack API operations through the POP gateway.

<a id="section-2-2"></a>

## 2.2. SDK for Java

Before you use an SDK for Java to call the API of a cloud service over the point of presence (POP) gateway, you must check the style of the service API. A service API can be of the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample Code** in the top navigation bar.

> **Important**
>
> We recommend that you do not download SDKs from the SDK Center and use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14.

Sample code:

```xml
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

public class DescribeApiGroups {

    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance. 
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");

        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters. 
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the service endpoint.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the service code.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        
        // If you use Security Token Service (STS) to call RPC API operations, you mustspecify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");

        // Specify service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");

        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");

        try {
            // Initiate the request and handle the response or exceptions. 
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
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

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07.

Sample code:

```xml
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

public class GetNamespaceList {

    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance. 
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");

        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters. 
        CommonRequest request = new CommonRequest();

        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-06-07");
        // Specify the uriPattern parameter, which is required for ROA APIs.
        request.setSysUriPattern("/namespace");
        // Specify the service code.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");

        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");


        // If you use access credentials assigned by STS to call ROA API operations, you must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");

        try {
            // Initiate the request and handle the response or exceptions. 
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
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

> **Important**
>
> By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
>
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting:
>
> Java
>
> ```text
> HttpClientConfig clientConfig = HttpClientConfig.getDefault();
> // Disable certificate verification for the client.
> clientConfig.setIgnoreSSLCerts(true)
> ```

<a id="section-2-3"></a>

## 2.3. Go

This topic describes how to use the POP Go software development kit (SDK) to make API calls.

**Prerequisites**

For Apsara Stack, use CommonRequest to make API calls. In the Apsara Uni-manager Management Console, go to **Products** > **Development Tools** > **API And Tools** > **Developer Portal**. Then, choose **API Integration** > **API Debugging** to view the recommended SDK versions and sample code.

> **Important**
>
> Do not download SDKs directly from the SDK Center for Apsara Stack environments. SDKs for the Alibaba Cloud public cloud might not support Apsara Stack APIs and can cause compatibility issues. Use them with caution.

**Background information**

You can call APIs using the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**CommonRequest call examples**

The API information for the RPC example is as follows: Product (apigateway), API operation (DescribeApiGroups), and Version (2016-07-14).

The following code is an example:

```go
package main

import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
  
)

func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<AccessKey secret>")

    request := requests.NewCommonRequest()
    
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use an STS AccessKey pair to call an RPC API, add the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"

    // Required. Specify the source of the call.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. Required for modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"

    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

The API information for the ROA example is as follows: Product (CR), API operation (GetNamespaceList), and Version (2016-06-07).

The following code is an example:

```xml
package main

import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
)



func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "
<yourAccessSecret>")
 request := requests.NewCommonRequest()

 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"

 request.PathPattern = "/namespace"
 // If you use an STS AccessKey pair to call a ROA API, add the x-acs-security-token field to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. Specify the source of the call.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. Required for modify and delete operations.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"

 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
 }
 fmt.Print(response.GetHttpContentString())
}
```

**Set a proxy**

You may need to set a proxy when you call an instance. You can set the proxy in one of the following two ways.

- Set the proxy using environment variables.

  Use the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variables.

  The following code is an example:

  ```go
  import (
      "os"
  )
  func main(){
   os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment variable.
   os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment variable.
  }
  ```

- Set the proxy on the client.

  The following code is an example:

  ```text
  // Proxy settings on the client have a higher priority than environment variables.
  client.SetHttpProxy("http://x.x.x.x:xxxx")   // Set the HTTP proxy.
  client.GetHttpProxy()                          // Get the HTTP proxy.

  client.SetHttpsProxy("https://x.x.x.x:xxxx")   // Set the HTTPS proxy.
  client.GetHttpsProxy()                           // Get the HTTPS proxy.

  client.SetNoProxy("127.0.0.1,localhost")     // Set the proxy whitelist.
  client.GetNoProxy()                          // Get the proxy whitelist.
  ```

**SSL verification**

**Summary**

This setting controls the SSL certificate verification behavior for requests.

- Set to  `true`  to disable certificate verification. This is an insecure practice. We recommend that you configure a certificate.

- Set to  `false`  to enable SSL certificate verification. By default, the operating system's CA certificates are used.

**Default value**

The default value is  `false` .

**Settings**

> **Important**
>
> When you access OpenAPI over HTTPS, the SDK enables SSL certificate validation by default. If your code environment does not have a certificate, a validation error occurs. To ensure secure communication in a production environment, keep this validation enabled. To ignore certificate validation in a test environment, use the following settings.

```text
// Set HTTPSInsecure for the request (affects only the current request).
request.SetHTTPSInsecure(true)                           // Set HTTPSInsecure for the re
quest to true.
isInsecure := request.GetHTTPSInsecure()                 // Get the HTTPSInsecure settin
g for the request.
```

The client-level setting takes effect only if the request-level setting is not set.

```text
// Set HTTPSInsecure for the client (affects all requests sent by the client).
client.SetHTTPSInsecure(true)                         // Set HTTPSInsecure for the clien
t to true.
isInsecure := client.GetHTTPSInsecure()               // Get the HTTPSInsecure setting f
or the client.
```

<a id="section-2-4"></a>

## 2.4. Python version

This topic describes how to use the POP Python software development kit (SDK) to call cloud product APIs.

**Prerequisites**

In Apsara Stack, use CommonRequest to make API calls. You can find the recommended SDK version and sample code in the Apsara Uni-manager Management Console. To do this, navigate to **Products** > **Development Tools** > **API And Tools** > **Developer Portal** and select **API Integration** > **API Debugging**.

> **Important**
>
> Do not download SDKs directly from the SDK Center for Apsara Stack scenarios. The SDKs for the public cloud may not support Apsara Stack APIs or have compatibility issues. Use them with caution.

**Background information**

Currently, you can call APIs only using the Remote Procedure Call (RPC) method.

**CommonRequest call example**

The following example shows how to call the DescribeInstances operation of ECS. The API version is 2014-05-26.

The following is the sample code:

```python
from aliyunsdkcore.client import AcsClient
import os
from aliyunsdkcore.request import CommonRequest

# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey secret>",
    "<your-RegionID>",
    timeout=1000,  # Set the timeout period.
    verify=False, # Ignore the certificate or set verify='<certificate_path>'.
);
# Use with HTTPS.
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"

# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create a request and set its parameters.
    request = CommonRequest()

    # When you call an RPC API using an STS AccessKey pair, add the SecurityToken fieldto the parameters.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)

    headers = {
        # Required. A description of the call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. Required for versions earlier than Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource group ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. Required for modify and delete operations.
        # "x-acs-instanceid":"<your-InstanceID>"

    }
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> withthe actual endpoint.
    request.set_product("apigateway")
    request.set_method("POST")

    # Initiate the API request and print the return value.
    response = client.do_action_with_exception(request)
    print(response)


if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Set a proxy**

When you call an API, you may need to set the HTTP_PROXY and HTTPS_PROXY environment variables.

The following is the sample code:

```text
# HTTPS proxy 
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"

# HTTP proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes how to access OpenAPI using the HTTPS protocol.

**Use the HTTPS protocol**

By default, the SDK uses the HTTPS protocol.

```python
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import 
DescribeInstancesRequest
from aliyunsdkcore.client import AcsClient
client = AcsClient(
    region_id='<region_id>',  # Region ID
)

request = DescribeInstancesRequest()
request.set_protocol_type('https')  # Use HTTPS.

client.do_action_with_exception(request)   
```

**Ignore certificates**

> **Important**
>
> - When you access OpenAPI using the HTTPS protocol, the SDK verifies the SSL/TLS certificate by default. If your code environment does not have a certificate, a certificate verification error is reported.
>
> - To ensure secure communication in a production environment, keep this verification enabled. If you must ignore certificate verification in a test environment, set the  `verify`  parameter.

```python
from aliyunsdkcore.client import AcsClient
client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify=False  # Ignore SSL certificate verification.
)
```

**Specify a CA certificate file**

```python
from aliyunsdkcore.client import AcsClient
client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify='./cacert.pem'  # Certificate path
)
```

<a id="section-3"></a>

# 3.API list

<a id="section-3-1"></a>

## 3.1. IntelligentAnalysis

The system supports intelligent data querying for the following scenarios: 1. Cloud platform billing and cost analysis: The system provides annual and monthly billing statistics, trend analysis, and year-over-year or month-over-month calculations at the organization, resource set, and resource levels. 2. Cloud resource optimization and governance analysis: The system analyzes resource idleness, bottlenecks, and health status at the organization, resource set, and resource levels. 3. Cloud resource statistics: The system counts cloud resources and calculates utilization rates by organization, resource set, and other dimensions.

This API uses Server-Sent Events (SSE) for communication. Its response type is text/event-stream, meaning the server returns data progressively via streaming transmission. Clients continuously listen to the event stream to receive each segment of the response from the server in real time. This approach suits scenarios requiring segmented output or long-duration processing, such as model inference and real-time Q&A.

During the response, the server sends each piece of data as an independent event. The typical format is: data: {"content": "This is the first segment of the response"}. Clients can parse and process these events one by one to achieve dynamic updates and real-time feedback.

**Request headers**

This operation uses common request headers only. For more information, see Common request parameters.

**Request syntax**

```http
POST /api/open/api/IntelligentAnalysis HTTP/1.1
```

**Request parameters**

| Parameter | Typ e | Positio n | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| messages | Arra y | Body | No | \[{"role":"user","content":" Help me query the ECS instance with IP xx under organization xx"}\] | The parameter "messages" is a list composed of multiple maps (List&lt;Map&lt;String, Object&gt;&gt;), representing the user's utterances in a conversation. Each map object represents a single message and contains the following two fixed fields:<br>role: A required string whose value must be "user", indicating the sender's role.<br>content: A required string that represents the user's question or input. |
| domain | Strin g | Body | No | cloud_optimized | The data domain for intelligent analysis.Available data domains include:<br>• bill_analysis: The cost analysis domain.<br>• resource_analysis: The resource analysis domain.<br>• cloud_optimized: The cloud optimization domain. |
| tables | Arra y | Body | No | \["instance_health_score"\] | The data table information under the specified data domain. |

**Examples**

Sample requests

```http
POST /api/open/api/IntelligentAnalysis HTTP/1.1
Content-Type: application/json
Accept: text/event-stream
x-acs-userid: 5003
x-acs-roleid: 1

{
  "messages": [
    {
      "role": "user",
      "content": "Count the top 5 level-1 organizations with the most ECS instances"
    }
  ]
}
```

Sample success responses

`JSON`  format

````text
data: {"choices": [{"delta": {"role": "function", "name": "action_node_type", "content": "data_analysis", "status": "waiting", "extra": {}}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "<TeamixStep>Data retrieval intent</TeamixStep>", "phase": "execute", "status": "ongoing", 
"chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "Theuser wants to count the top 5 level-1 organizations with the most ECS instances. The most relevant table is the resource instance table in the resource analysis domain, involving the organization and resource type dimensions and the instance count metric. I will filter for data where the resource type is ECS instance, aggregate by organization, and select the top 5 level-1 organizations by instance count.", "phase": "execute", "status": "ongoing", "chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "", 
"phase": "execute", "status": "ongoing", "chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "<TeamixStep>Relevant metrics</TeamixStep>", "phase": "execute", "status": "ongoing", "chat
Source": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "| Data domain   | Table     | Metric   ||:------|:------|:-----|| Resource analysis domain 
| Resource instance table | Instance count |", "phase": "execute", "status": "ongoing",
"chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "<TeamixStep>Query and display data</TeamixStep>", "phase": "execute", "status": "ongoing",
"chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "<TeamixStepEnd />", "phase": "execute", "status": "done", "chatSource": "", 
"chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "**Data domain**: Resource analysis domain, **Table**: Resource instance table, **Dimensions**: Organization, Resource type, **Metric**: Instance count", "reasonContent": "", "phase": "answer", "status": "ongoing", "chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "reasonContent": "", 
"phase": "answer", "status": "ongoing", "chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": 
"```TeamixModule{\"moduleInfo\": {\"name\": \"renderAIPanel\",\"hideLoadTime\": true}, 
\"moduleProps\": {\"title\": \"Top 5 level-1 organizations with the most ECS instances\
", \"description\": \"\", \"chartConfig\": {\"type\": \"bar\", \"config\": {\"column\":true, \"zoom\": true}}, \"dataSource\": {\"success\": true, \"type\": \"chart\", \"table\": [{\"data\": [[\"ascmTest\", 118], [\"iaas_test\", 100], [\"acs-autotest\", 26], [\
"amc-storage\", 21], [\"coms standard org\", 13]], \"name\": \"ECS instance count\"}], 
\"tableName\": \"Top 5 level-1 organizations with the most ECS instances\"}, 
\"dataConfig\": {\"type\": \"apsara-copilot\", \"request\": { \"url\": 
\"/data/api.json\", \"method\": \"POST\", \"data\": {\"$product\": \"ascm\", \"$version
\": \"2025-03-10\", \"$action\": \"GetAnalysisDataForCard\", \"cardId\": \"3dd606e9-d071-4364-8a41-042b1387390e\", \"cardVersion\": \"v1\"}}}}}```", "reasonContent": "", "phase": "answer", "status": "ongoing", "chatSource": "", "chatSourceProps": null}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "status": "ongoing", 
"phase": "answer"}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "### Data 
interpretation", "status": "ongoing", "phase":"answer"}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "According to the statistical results", "status": "ongoing", "phase": "answer"}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "...<Summary and analysistext>", "status": "ongoing", "phase": "answer"}}]}

data: {"choices": [{"delta": {"role": "assistant", "content": "", "status": "ongoing", 
"phase": "answer"}}]}

data: [DONE]
````

<a id="section-3-2"></a>

## 3.2. IntelligentSearch

Intelligent search for cloud service instances, organizations, resource sets, and users.

This API uses Server-Sent Events (SSE) for communication. The response type is text/event-stream, meaning the server returns data progressively via streaming transmission. The client listens continuously to the event stream to receive each segment of the response from the server in real time. This approach suits scenarios requiring segmented output or long-duration processing, such as model inference and real-time Q&A.

During the response, the server sends each piece of data as an independent event. The typical format is: data: {"content": "This is the first segment of the answer"}. The client can parse and process these events one by one to achieve dynamic updates and real-time feedback.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/IntelligentSearch HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positio n | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| messages | Json | Body | No | {"messages": \[{"role":"user","content": "Help me query the ECS instance with IP xx under organization xx"}\]} | The parameter "messages" is a list composed of multiple maps (List&lt;Map&lt;String, Object&gt;&gt;), representing the user's utterances in a conversation. Each map object represents a single message and contains the following two fixed fields:<br>role: A required string whose value must be "user", indicating the message sender's role.<br>content: A required string that represents the user's question or input. |

Streaming response

**Examples**

Sample requests

```http
POST /api/open/api/IntelligentSearch HTTP/1.1
{
  "messages": [
    {
      "role": "user",
      "content": "Query the ECS instances I created"
    }
  ]
}
```

Sample success responses

`JSON`  format

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

`XML`  format

```xml
<data>[{}]</data>
<success>true</success>
<dynamicMessages>[]</dynamicMessages>
<errorMessage>&quot;&quot;</errorMessage>
<errorCode>500</errorCode>
<httpCode>200</httpCode>
```

<a id="section-3-3"></a>

## 3.3. IntelligentQa

The cloud product knowledge Q&A answers questions about using and configuring the cloud platform and cloud resources. The system supports two modes: context-aware conversations based on dialogue history, and single-turn Q&A without dialogue history.

API description

This API uses Server-Sent Events (SSE) for communication. Its response type is text/event-stream, meaning the server returns data progressively via streaming transmission. The client listens continuously to the event stream to receive each segment of the response from the server in real time. This approach suits scenarios requiring segmented output or long-duration processing, such as model inference and real-time Q&A.

During the response, the server sends each piece of data as an independent event. The typical format is: data: {"content": "This is the first segment of the answer"}. The client can parse and process these events one by one to enable dynamic updates and real-time feedback.

**Preparations**

- If you need to use chat management, create a chat or prepare a valid chatId first.

**Notes**

- When you provide the chatId parameter, the system activates stateful mode and performs multi-turn interactions based on the historical conversation context.

- When you do not provide the chatId parameter, the system runs in stateless mode, suitable for single, independent Q&A scenarios.

**Best practices**

- For continuous conversation scenarios: First, call CreateChat to create a session and obtain a chatId. Then, use this chatId in subsequent requests to maintain conversation context.

- For single Q&A scenarios: Call the API directly without passing the chatId parameter to achieve lightweight question answering.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/IntelligentQa HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application. |
| outerType | Strin g | Body | No | coms | The type identifier for the external application. |
| chatId | Strin g | Body | No | 8932b258-75b5-42e7-8c52-0be053a88d64 | The chat session ID. The system enables stateful mode if you provide this parameter; Otherwise, it runs in stateless mode. |
| model | Strin g | Body | No | qwen3 | The name of the model to use.<br>Note<br>• This parameter is optional. If you do not specify it, the system uses the default model. |
| parentId | Strin g | Body | No | 5d2db7cc-4182-4a80-a9b7-a9d49a460a1f | The parent message ID.<br>Note<br>• This parameter is optional, but required if you provide chatId. |
| messages | Json | Body | No | Stateless: {"messages": \[{"role":"user","content": "Q&amp;A content"}\]} Stateful: \[{"role":"user","msgId":"4 2511985-4941-49d1-ac10-7573ff19671f","content": "Briefly answer the previous question","chatSourcePro ps": {"intranetSearch":false}}\] | The list of messages.<br>Note<br>• The parameter "messages" is a list composed of multiple maps (List&lt;Map&lt;String, Object&gt;&gt;), representing the user's utterances in a conversation. Each map object represents a single message and contains the following two fixed fields:<br>• role: A required string whose value must be "user", indicating the message sender's role.<br>• content: A required string that represents the user's question or input.<br>• msgId: String type, representing the current message ID, required if you provide chatId.<br>• chatSourceProps: Object type.<br>• chatSourceProps.intran etSearch: Boolean type, indicating whether to enable intranet search. |
| product | Strin g | Body | No | ECS | The product code, such as ECS or VPC. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt message. |
| data | String | \[{}\] | The returned data. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| errorCode | String | 500 | The error code. |
| errorMessage | String | "" | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |

The return type is StreamingResponse. The response format is text/event-stream (SSE), meaning the server returns data progressively via event stream. During streaming transmission, the server sends each piece of data as an independent event. The event content is a JSON object containing the content field. The content field is of the string type and carries the answer content generated progressively by the model. Example: data: {\\"content\\": \\"This is the first segment of the answer\\"}.

**Examples**

Sample requests

```http
POST /api/open/api/IntelligentQa HTTP/1.1

Content-Type: application/json

{
  "chatId": "8932b258-75b5-42e7-8c52-0be053a88d64",
  "parentId": "2e469579-5c6f-4f55-accb-ae339a1aff78",
  "messages": [
    {
      "role": "user",
      "msgId": "42511985-4941-49d1-ac10-7573ff19671f",
      "content": "Briefly answer the previous question",
      "chatSourceProps": {
        "intranetSearch": false
      }
    }
  ]
}
```

Sample success responses

`JSON`  format

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

`XML`  format

```xml
<data>[{}]</data>
<success>true</success>
<dynamicMessages>[]</dynamicMessages>
<errorMessage>&quot;&quot;</errorMessage>
<errorCode>500</errorCode>
<httpCode>200</httpCode>
```

<a id="section-3-4"></a>

## 3.4. CreateChat

Create a new chat and return its globally unique identifier and the generated title (by default, the title is the user's first input).

API description

**Preparations**

- Prepare a message ID (msgId). It must be a non-empty string.

- Prepare the chat content (content). It must be a non-empty string.

- Optionally, provide external application identifiers (outerType and outerId). You must pass both outerType and outerId. Do not use only one of them.

**Notes**

- Both msgId and content are required parameters and cannot be empty.

- content must be of the string type.

- msgId must be of the string type.

- The system automatically generates a unique chatId.

**Best practices**

- Call this API when a user starts a new chat.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/CreateChat HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| msgId | Strin g | Body | No | 8158be15-ccf5-4e57-a3b9-68c7af900000 | The unique identifier of the first message.<br>Note<br>• This parameter is required. |
| content | Strin g | Body | No | What can the AI assistant do for me? | The conten of the chat, which serves as the conversation title.<br>Note<br>• This parameter is required. |

**Response data**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt message. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The response message. |
| errorCode | String | UnknownError | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |
| data | Struct | {} | The returned data. |
| -chatId | String | 8158be15-ccf5-4e57-a3b9-68c7af900000 | The unique identifier of the chat. |
| -title | String | What is the AI assistant? | The chat title. |

**Examples**

Sample requests

```http
POST /api/open/api/CreateChat HTTP/1.1

Content-Type: application/json

{
    "msgId": "8158be15-ccf5-4e57-a3b9-68c7af900000",
    "content": "What is the AI assistant?",
    "outerId":"123456",
    "outerType":"coms"
}
```

Sample success responses

`JSON`  format

```json
{
 "data":{
  "chatId":"8158be15-ccf5-4e57-a3b9-68c7af900000",
  "title":"What is the AI assistant?"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"System exception",
 "errorCode":"UnknownError",
 "message":"success",
 "httpCode":200
}
```

`XML`  format

```xml
<data>
 <chatId>8158be15-ccf5-4e57-a3b9-68c7af900000</chatId>
 <title>What is the AI assistant?</title>
</data>
<success>true</success>
<dynamicMessages>[]</dynamicMessages>
<errorMessage>System exception</errorMessage>
<errorCode>UnknownError</errorCode>
<message>success</message>
<httpCode>200</httpCode>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 500 | INTERNAL_ERROR | %s | An internal error occurred. The system carries a dynamic error code and dynamic error message from the business layer. |

<a id="section-3-5"></a>

## 3.5. IntelligentCoding

Generate code samples for Open Platform OpenAPI and Terraform.

This API uses Server-Sent Events (SSE) for communication. The response type is text/event-stream, meaning the server returns data progressively via streaming transmission. The client listens continuously to the event stream to receive each segment of the response from the server in real time. This approach suits scenarios requiring segmented output or long-duration processing, such as model inference and real-time Q&A.

During the response process, the server sends each piece of data as an independent event. The typical format is: data: {"content": "This is the first segment of the response"}. The client can parse and process these events one by one to achieve dynamic updates and real-time feedback.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/IntelligentCoding HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| messages | Json | Body | No | {"messages": \[{"role":"user","content": "Help me write OpenAPI code to create an ECS instance"}\]} | The parameter "messages" is a list composed of multiple maps (List&lt;Map&lt;String, Object&gt;&gt;), representing the user's utterances in a chat. Each map object represents a single message and contains the following two fixed fields:<br>role: A required string whose value must be "user", indicating the message sender's role.<br>content: A required string that represents the user's question or input. |
| product | Strin g | Body | No | ECS | The code of the cloud service. |
| scene | Strin g | Body | No | api_code_gen | api_code_gen: Answers user questions about OpenAPI code generation and SDK integration. It provides sample code for Open Platform APIs.terraform_code_gen: Answers user questions about Terraform code generation and usage. It provides developers with Terraform templates and sample code to help users efficiently manage cloud resources such as ECS, VPC, and MQ by using Terraform.<br>code_check: Answers user questions about code diagnostics. This includes diagnosing sample code for private SDKs, Terraform resources, and Java, Python, and Golang code. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt messages. |
| data | String | \[{}\] | The returned data. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| errorCode | String | 500 | The error code. |
| errorMessage | String | A system exception occurred. | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```http
POST /api/open/api/IntelligentCoding HTTP/1.1
```

Sample success responses

`JSON`  format

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"A system exception occurred.",
 "errorCode":"500",
 "httpCode":200
}
```

`XML`  format

```xml
<data>[{}]</data>
<success>true</success>
<dynamicMessages>[]</dynamicMessages>
<errorMessage>A system exception occurred.</errorMessage>
<errorCode>500</errorCode>
<httpCode>200</httpCode>
```

<a id="section-3-6"></a>

## 3.6. GetChatHistory

Retrieve the complete chat history by chat ID.

API description

**Preparations**

- Obtain a valid chatId.

**Notes**

- The chatId parameter is required and cannot be empty.

- Filter chats from specific sources by using outerType and outerId. You must provide both outerType and outerId. Do not use only one of them.

**Best practices**

- Call this API to retrieve the complete chat history when a user opens a historical chat.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/GetChatHistory HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| chatId | Strin g | Body | No | fe5ad98e-0ed7-4f99-8bf6-cbf9d3e878f9 | The unique identifier of the chat.<br>Note<br>• This parameter is required. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt messages. |
| title | String | What can the AI assistant do for me？ | The title of the chat. |
| chatId | String | e379688d-6d52-4e68-9ac6-92b75d003e6d | The unique ID of the chat. |
| namespace | String | default | The namespace. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The return message. |
| errorCode | String | UnknownError | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |
| chat | Struct | {} | The chat details. |
| -messages | Array | \[{}\] | The list of messages, sorted by time. |
| --childrenIds | List | \["ecd0f609-9fd5-49d7-a3bc-dddd89658100"\] | The list of child message IDs. |
| --content | String | What can the AI assistant do for me？ | The message content. |
| --feedback | String | Feedback content | User feedback. |
| --msgId | String | 02fab45f-5770-45b9-85e2-dc8e4defa06a | The unique ID of the message. |
| --parentId | String | 02fab45f-5770-45b9-85e2-dc8e4defa06a | The parent message ID. |
| --rating | Integer | 0 | The user rating for this message.<br>Note<br>• Unrated: 0 / Thumbs up: 1 / Thumbs down: -1 |
| --role | String | user | The message role.<br>Note<br>• user / assistant |
| --timestamp | String | 2026-01-22T09:04:45Z | The modification time. |
| --type | String | content | The message type. |
| --reasonContent | String | Intent recognition Document understanding and analysis Retrieving relevant documents and analyzing them to generate a reference answer for you. | The reasoning process. |
| --actionNodeTyp e | String | rag | The action node type. |
| --thinkingEnable d | String | 0 | Indicates whether thinking mode is enabled. |
| --chatSource | String | rag | The source of the chat. |
| -title | String | What can the AI assistant do for me? | The chat title. |
| -chatId | String | 8a5544e8-6704-4981-9241-caa15fd9fc3d | The unique ID of the chat. |
| -chatType | String | default | The chat type. |
| -history | Struct | {} | The history. |
| --currentId | String | ecd0f609-9fd5-49d7-a3bc-dddd89658100 | The current message ID. |
| --messages | Map | {"ecd0f609-9fd5-49d7-a3bc-dddd89658100": {"role":"assistant", "reasonContent":" Intent recognition Document understanding and analysis Retrieving relevant documents and analyzing them to generate a reference answer for you.","thinkingEna bled":0,"rating":0," childrenIds": \[\],"msgId":"ecd0f6 09-9fd5-49d7-a3bc-dddd89658100","ty pe":"content","cont ent":"### The AI assistant provides intelligent support for your cloud services, helping you use cloud products and services more simply and efficiently.","parent Id":"02fab45f-5770-45b9-85e2-dc8e4defa06a","ch atSource":"default","actionNodeType": "rag","timestamp": "2026-01-22T09:04:45Z"},"0 2fab45f-5770-45b9-85e2-dc8e4defa06a": {"role":"user","thin kingEnabled":0,"rat ing":0,"childrenIds":\["ecd0f609-9fd5-49d7-a3bc-dddd89658100"\]," msgId":"02fab45f-5770-45b9-85e2-dc8e4defa06a","ty pe":"content","cont ent":"What can the AI assistant do for me?","chatSource": | The message dictionary. The key is the message ID, and the value is the message object. |

"default","actionNo

**Examples**

deType":"default"," timestamp":"2026-

Sample requests

01-22T09:04:29Z"}}

```http
POST /api/open/api/GetChatHistory HTTP/1.1

Content-Type: application/json

{
  "outerId": "123456",
  "outerType": "coms",
  "chatId": "ff536d45-014c-43ca-a97f-f7e4dca3bed9"
}
```

Sample success responses

`JSON`  format

```json
{
    "chatId": "8a5544e8-6704-4981-9241-caa15fd9fc3d",
    "chat": {
        "chatId": "8a5544e8-6704-4981-9241-caa15fd9fc3d",
        "messages": [
            {
                "role": "user",
                "thinkingEnabled": 0,
                "rating": 0,
                "childrenIds": [
                    "ecd0f609-9fd5-49d7-a3bc-dddd89658100"
                ],
                "msgId": "02fab45f-5770-45b9-85e2-dc8e4defa06a",
                "type": "content",
                "chatSource": "default",
                "content": "In one sentence, tell me what the AI Assistant can do for 
me?",
                "actionNodeType": "default",
                "timestamp": "2026-01-22T09:04:29Z"
            },
            {
                "role": "assistant",
                "reasonContent": "<TeamixStep>Intent recognition</TeamixStep><TeamixStep
End /><TeamixStep>Document understanding and analysis</TeamixStep>Retrieving relevant documents and analyzing them to generate a reference answer for you.<TeamixStepEnd />",
                "thinkingEnabled": 0,
                "rating": 0,
                "childrenIds": [],
                "msgId": "ecd0f609-9fd5-49d7-a3bc-dddd89658100",
                "type": "content",
                "chatSource": "default",
                "content": "### The AI Assistant provides intelligent support for your cloud services, helping you use cloud products and services more simply and efficiently.",
                "parentId": "02fab45f-5770-45b9-85e2-dc8e4defa06a",
                "actionNodeType": "rag",
                "timestamp": "2026-01-22T09:04:45Z"
            }
        ],
        "history": {
            "currentId": "ecd0f609-9fd5-49d7-a3bc-dddd89658100",
            "messages": {
                "ecd0f609-9fd5-49d7-a3bc-dddd89658100": {
                    "role": "assistant",
                    "reasonContent": "<TeamixStep>Intent recognition</TeamixStep><Teamix
StepEnd /><TeamixStep>Document understanding and analysis</TeamixStep>Retrieving relevant documents and analyzing them to generate a reference answer for you.<TeamixStepEnd /
>",
                    "thinkingEnabled": 0,
                    "rating": 0,
                    "childrenIds": [],
                    "msgId": "ecd0f609-9fd5-49d7-a3bc-dddd89658100",
                    "type": "content",
                    "content": "### The AI Assistant provides intelligent support for yo
ur cloud services, helping you use cloud products and services more simply and efficiently.",
                    "parentId": "02fab45f-5770-45b9-85e2-dc8e4defa06a",
                    "chatSource": "default",
                    "actionNodeType": "rag",
                    "timestamp": "2026-01-22T09:04:45Z"
                },
                "02fab45f-5770-45b9-85e2-dc8e4defa06a": {
                    "role": "user",
                    "thinkingEnabled": 0,
                    "rating": 0,
                    "childrenIds": [
                        "ecd0f609-9fd5-49d7-a3bc-dddd89658100"
                    ],
                    "msgId": "02fab45f-5770-45b9-85e2-dc8e4defa06a",
                    "type": "content",
                    "content": "In one sentence, tell me what the AI Assistant can do fo
r me?",
                    "chatSource": "default",
                    "actionNodeType": "default",
                    "timestamp": "2026-01-22T09:04:29Z"
                }
            }
        },
        "title": "In one sentence, tell me what the AI Assistant can do for me?",
        "chatType": "default"
    },
    "namespace": "default",
    "title": "In one sentence, tell me what the AI Assistant can do for me?"
}
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
    <td>500</td>
    <td>INTERNAL_ERROR</td>
    <td>%s</td>
    <td>An internal error. The system carries a dynamic error code and a dynamic error message from the business layer.</td>
  </tr>
</table>

<a id="section-3-7"></a>

## 3.7. ListHistoryChats

List a user's chat history.

API description

**Notes**

- By default, the system returns the 20 most recent records. You can specify the number of returned records through parameters, but pagination is not supported.

- You can filter chats from specific sources by using outerType and outerId. You must pass both outerType and outerId together. Do not use only one of them.

**Best practices**

- Call this API when a user views the chat history list.

- This API is suitable for building a chat history page that allows users to quickly browse and select previous chats.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/ListHistoryChats HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| namespac e | Strin g | Body | No | default | The namespace.<br>Note<br>• This parameter is optional. By default, the system queries chats under default. |
| pageSize | Integ er | Body | No | 20 | The number of chats to return. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt messages. |
| data | Array | \[{}\] | The returned data. |
| -chatId | String | b6aaa1fe-9cbd-40e7-b70b-53f0865e6192 | The unique ID of the chat. |
| -namespace | String | default | The namespace. |
| -chatType | String | default | The type of the chat. |
| -title | String | What can the AI assistant do for me? | The title of the chat. |
| -created | String | 2026-01-22T08:28:51Z | The creation time. |
| -updated | String | 2026-01-22T08:29:12Z | The last modification time. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The return message. |
| errorCode | String | UnknownError | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```http
POST /api/open/api/ListHistoryChats HTTP/1.1

Content-Type: application/json

{
  "pageSize": 20,
  "outerId": "123456",
  "outerType": "coms"
}
```

Sample success responses

`JSON`  format

```json
{
    "data": [
        {
            "chatId": "b6aaa1fe-9cbd-40e7-b70b-53f0865e6192",
            "created": "2026-01-22T08:28:51Z",
            "namespace": "default",
            "title": "What can the AI assistant do for me?",
            "updated": "2026-01-22T08:29:12Z",
            "chatType": "default"
        }
    ],
    "success": true
}
```

**Error codes**

<table>
  <tr>
    <td>HTTP status code</td>
    <td>Error code</td>
    <td>Error message</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>500</td>
    <td>INTERNAL_ERROR</td>
    <td>%s</td>
    <td>An internal error. The system carries a dynamic error code and a dynamic error message from the business layer.</td>
  </tr>
</table>

<a id="section-3-8"></a>

## 3.8. PushChatMessage

Save historical chat messages.

API description

**Preparations**

- Obtain a valid chatId.

- Prepare the list of messages to push, including message ID, content, role, and other information.

- Ensure the parent-child relationships in the message list are correct (linked by parentId).

**Notes**

- The chatId parameter is required and cannot be empty.

- The message sequence must form a coherent chain with only one leaf node.

- If you push messages based on historical messages, the parent node must already exist in the database.

- You can filter chats from specific sources by using outerType and outerId. You must pass both outerType and outerId together. Do not use only one of them.

**Best practices**

- After Apsara Copilot generates a response, push the response message and the question to the chat history.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/PushChatMessage HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| chatId | Strin g | Body | No | fe5ad98e-0ed7-4f99-8bf6-cbf9d3e878f9 | The unique identifier of the chat.<br>Note<br>• This parameter is required. |
| actionNod eType | Strin g | Body | No | rag | The type of the action node.<br>Note<br>• This parameter is required.<br>• The default value is <code> rag </code>. |

<table>
  <tr>
    <td>messages</td>
    <td>Json</td>
    <td>Body</td>
    <td>No</td>
    <td>[ { "chatSource": "rag", "msgId": "8158be15-ccf5-4e57-a3b9-68c7af9a1220", "parentId": null, "content": "What is the AI assistant?", "role": "user", "reasonContent": "", "phase": "answer" }, {"actionNodeType": "rag", "msgId": "8158be15-ccf5-4e57-a3b9-68c7af9a1221", "parentId": "8158be15-ccf5-4e57-a3b9-68c7af9a1220", "content": "Omit answer content", "role": "assistant", "reasonContent": " Intent recognition The user asks about the functional scope of the AI assistant, intending to understand available services and capabilities. Document understanding and analysis Retrieving relevant documents and analyzing them to generate a reference answer for you.", "phase": "answer", "model": "qwen3" } ]</td>
    <td>The list of messages to push.<br>Note<br>• This parameter is required.<br>Fields<br>• chatSource: The source of the message. The default value is <code> rag </code>.<br>• msgId: The unique ID of the message.<br>• parentId: The unique ID of the parent message, establishing parent-child relationships between messages.<br>• role: The role of the message (user/assistant).<br>• content: The content of the message, either a question or an answer.<br>• reasonContent: The reasoning process.<br>• phase: The generation phase. The default value is <code> answer </code>.<br>• model: The language model used.<br>• actionNodeType: The default value is <code> rag </code>.</td>
  </tr>
</table>

**Response data**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt messages. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The return message. |
| errorCode | String | UnknownError | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```xml
POST /api/open/api/PushChatMessage HTTP/1.1

Content-Type: application/json

{
  "outerId":"123456",
  "outerType":"coms",
  "chatId": "fe5ad98e-0ed7-4f99-8bf6-cbf9d3e878f9",
  "messages": [
    {
      "chatSource": "rag",
      "msgId": "8158be15-ccf5-4e57-a3b9-68c7af9a1220",
      "parentId": null,
      "content": "What is the AI assistant?",
      "role": "user",
      "reasonContent": "",
      "phase": "answer"
    },
    {
      "actionNodeType": "rag",
      "msgId": "8158be15-ccf5-4e57-a3b9-68c7af9a1221",
      "parentId": "8158be15-ccf5-4e57-a3b9-68c7af9a1220",
      "content": "Omit answer content",
      "role": "assistant",
      "reasonContent": "<TeamixStep>Intent recognition</TeamixStep>The user asks about the functional scope of the AI assistant, intending to understand available services and capabilities.
<TeamixStepEnd /><TeamixStep>Document understanding and analysis</TeamixStep>Retrieving 
relevant documents and analyzing them to generate a reference answer for you.<TeamixStepEnd />",
      "phase": "answer",
      "model": "qwen3"
    }
  ],
  "actionNodeType": "rag"
}
```

Sample success responses

`JSON`  format

```json
{
    "success": true
}
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 500 | INTERNAL_ERROR | %s | An internal error. The system carries a dynamic error code and a dynamic error message from the business layer. |

<a id="section-3-9"></a>

## 3.9. MessageFeedback

Use this API to submit rating feedback for a specific chat message. It supports thumbs-up and thumbs-down operations.

API description

**Preparations**

- Obtain a valid chatId and msgId.

- Determine the user's rating for the message (for example, 1 indicates a thumbs-up, -1 indicates a thumbs-down).

**Notes**

- chatId and msgId must exist and be valid.

- You can filter chats from specific sources by using outerType and outerId. You must pass both outerType and outerId together. Do not use only one of them.

**Best practices**

- Call this API after the user performs a thumbs-up or thumbs-down operation on a response.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/MessageFeedback HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| msgId | Strin g | Body | No | 8158be15-ccf5-4e57-a3b9-68c7af900000 | The unique identifier of the message.<br>Note<br>• This parameter is required. |
| chatId | Strin g | Body | No | d96cbf45-f2a7-4dea-b745-e4069d171e79 | The unique identifier of the chat.<br>Note<br>• This parameter is required. |
| rating | Integ er | Body | No | 1 | The user's rating for this message.<br>Note<br>• This parameter is required.<br>• Thumbs-up: 1 /Thumbs-down: -1 |
| reason | Strin g | Body | No | ignore | The reason for performing this operation. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt messages. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The return message. |
| errorCode | String | UnknownError | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```http
POST /api/open/api/MessageFeedback HTTP/1.1

Content-Type: application/json

{
  "chatId": "fe5ad98e-0ed7-4f99-8bf6-cbf9d3e878f9",
  "msgId": "8158be15-ccf5-4e57-a3b9-68c7af9a1221",
  "rating": -1,
  "reason": ""
}
```

Sample success responses

`JSON`  format

```json
{
    "success": true,
    "message": "success"
}
```

**Error code**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 500 | INTERNAL_ERROR | %s | An internal error. The system carries a dynamic error code and a dynamic error message from the business layer. |

<a id="section-3-10"></a>

## 3.10. DeleteChat

Delete the specified chat record.

API description

**Preparations**

- Obtain a valid chatId.

**Notes**

- The chatId parameter is required and cannot be empty.

- You can filter chats from specific sources by using outerType and outerId. You must pass both outerType and outerId together. Do not use only one of them.

**Best practices**

- Call this API when the user confirms the deletion of a specific chat.

- Use this API to clean up unnecessary historical chat records.

**Request headers**

This API uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```http
POST /api/open/api/DeleteChat HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positio n | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| outerId | Strin g | Body | No | 123456 | The user ID of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerType. |
| outerType | Strin g | Body | No | coms | The type identifier of the external application.<br>Note<br>• This parameter is optional. You must use it together with outerId. |
| chatId | Strin g | Body | Yes | 2a902b57-dd58-416f-b190-cba7dc74e12c | The unique identifier of the chat to delete.<br>Note<br>• This parameter is required. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| dynamicMessa ges | List | \[\] | The dynamic prompt message. |
| success | Boolean | true | The return status.<br>• Success: true.<br>• Failure: false. |
| message | String | success | The return message. |
| errorCode | String | InvalidParameter.c hatId | The error code. |
| errorMessage | String | System exception | The error message. |
| httpCode | Integer | 200 | The HTTP status code. |
| data | Struct | {} | The returned data. |
| -chatId | String | d96cbf45-f2a7-4dea-b745-e4069d171e79 | The unique identifier of the deleted chat. |

**Examples**

Sample requests

```http
POST /api/open/api/DeleteChat HTTP/1.1

Content-Type: application/json

{
    "chatId": "2a902b57-dd58-416f-b190-cba7dc74e12c"
}
```

Sample success responses

`JSON`  format

```json
{
    "data": {
        "chatId": "d96cbf45-f2a7-4dea-b745-e4069d171e79"
    },
    "success": true
}
```

**Error codes**

| HttpCode | Error code | Error message | Description |
| --- | --- | --- | --- |
| 500 | INTERNAL_ERROR | %s | An internal error. The system carries a dynamic error code and a dynamic error message from the business layer. |
