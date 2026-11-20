Alibaba Cloud  
Apsara Stack  
API Gateway  
Developer Guide  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Preparations](#section-1)
    - [1.1. Obtain API information and endpoints](#section-1-1)
    - [1.2. Obtain an AccessKey](#section-1-2)
    - [1.3. Get common header parameters](#section-1-3)
    - [1.4. Obtain an STS AccessKey](#section-1-4)
    - [1.5. Obtain user and role information](#section-1-5)
    - [1.6. Obtain the region ID and organization ID](#section-1-6)
- [2.Calling Apsara Stack APIs through a POP gateway](#section-2)
    - [2.1. Java version](#section-2-1)
    - [2.2. Common API call methods](#section-2-2)
        - [2.2.1. API call - Cluster management](#section-2-2-1)
        - [2.2.2. API call - Origin management](#section-2-2-2)
        - [2.2.3. API call - Service management](#section-2-2-3)
        - [2.2.4. API call - Instance management](#section-2-2-4)
        - [2.2.5. API call - Group management](#section-2-2-5)
        - [2.2.6. API call - Route management](#section-2-2-6)
        - [2.2.7. API call - Policy configuration management](#section-2-2-7)
        - [2.2.8. API call - Consumer management](#section-2-2-8)
        - [2.2.9. API call - Domain name management](#section-2-2-9)
        - [2.2.10. API call - Route plugin management](#section-2-2-10)
        - [2.2.11. API call - Certificate management](#section-2-2-11)
- [3.API Gateway](#section-3)
    - [3.1. Cluster management](#section-3-1)
        - [3.1.1. ListClusters](#section-3-1-1)
        - [3.1.2. GetK8sClusterInfoByGwInstanceId](#section-3-1-2)
        - [3.1.3. GetK8sClusterName](#section-3-1-3)
        - [3.1.4. ImportCluster](#section-3-1-4)
        - [3.1.5. UpdateCluster](#section-3-1-5)
        - [3.1.6. CancelImportCluster](#section-3-1-6)
        - [3.1.7. CheckConnectCluster](#section-3-1-7)
        - [3.1.8. ListK8sAllNamespaces](#section-3-1-8)
        - [3.1.9. ListAllNamespaces](#section-3-1-9)
    - [3.2. Instance Management](#section-3-2)
        - [3.2.1. ListInstances](#section-3-2-1)
        - [3.2.2. ListAllInstances](#section-3-2-2)
        - [3.2.3. ListInstancesByServiceId](#section-3-2-3)
        - [3.2.4. GetInstanceInfo](#section-3-2-4)
        - [3.2.5. CreateInstance](#section-3-2-5)
        - [3.2.6. AscmCreateInstance](#section-3-2-6)
        - [3.2.7. ModifyInstance](#section-3-2-7)
        - [3.2.8. ModifyInstanceImageUrl](#section-3-2-8)
        - [3.2.9. UpgradeInstance](#section-3-2-9)
        - [3.2.10. DeleteInstance](#section-3-2-10)
        - [3.2.11. RestartInstance](#section-3-2-11)
        - [3.2.12. StopInstance](#section-3-2-12)
        - [3.2.13. RefreshInstance](#section-3-2-13)
        - [3.2.14. CreateInstanceDeployConfig](#section-3-2-14)
        - [3.2.15. GetInstanceDeployDeployConfig](#section-3-2-15)
        - [3.2.16. GetInstanceDeployMsg](#section-3-2-16)
        - [3.2.17. GetCustomDeployConfig](#section-3-2-17)
        - [3.2.18. GetInstanceAccessModeConfig](#section-3-2-18)
        - [3.2.19. GetResource](#section-3-2-19)
        - [3.2.20. ModifyResource](#section-3-2-20)
    - [3.3. Group Management](#section-3-3)
        - [3.3.1. ModifyGroup](#section-3-3-1)
        - [3.3.2. CreateGroup](#section-3-3-2)
        - [3.3.3. ListGroups](#section-3-3-3)
        - [3.3.4. GetAllGroups](#section-3-3-4)
        - [3.3.5. GetGroup](#section-3-3-5)
        - [3.3.6. DeleteGroup](#section-3-3-6)
        - [3.3.7. AddGroupDomain](#section-3-3-7)
        - [3.3.8. DeleteGroupDomain](#section-3-3-8)
    - [3.4. Ingress management](#section-3-4)
        - [3.4.1. CreateRoute](#section-3-4-1)
        - [3.4.2. BatchDeleteRoute](#section-3-4-2)
        - [3.4.3. ListRoutes](#section-3-4-3)
        - [3.4.4. ListRoutesByAppId](#section-3-4-4)
        - [3.4.5. ListRoutesByGwInstanceId](#section-3-4-5)
        - [3.4.6. GetAllRoutePath](#section-3-4-6)
        - [3.4.7. GetRoute](#section-3-4-7)
        - [3.4.8. GetProtocolByRoute](#section-3-4-8)
        - [3.4.9. ModifyRoute](#section-3-4-9)
        - [3.4.10. DeleteRoute](#section-3-4-10)
        - [3.4.11. ChangeRouteStatus](#section-3-4-11)
    - [3.5. Source Management](#section-3-5)
        - [3.5.1. ListSources](#section-3-5-1)
        - [3.5.2. ListAllSources](#section-3-5-2)
        - [3.5.3. GetSource](#section-3-5-3)
        - [3.5.4. CreateSource](#section-3-5-4)
        - [3.5.5. ModifySource](#section-3-5-5)
        - [3.5.6. DeleteSource](#section-3-5-6)
        - [3.5.7. BatchDeleteSource](#section-3-5-7)
    - [3.6. Service Management](#section-3-6)
        - [3.6.1. ListServices](#section-3-6-1)
        - [3.6.2. ListAllServices](#section-3-6-2)
        - [3.6.3. GetService](#section-3-6-3)
        - [3.6.4. CreateService](#section-3-6-4)
        - [3.6.5. ModifyService](#section-3-6-5)
        - [3.6.6. ModifyNode](#section-3-6-6)
        - [3.6.7. DeleteService](#section-3-6-7)
        - [3.6.8. BatchDeleteService](#section-3-6-8)
        - [3.6.9. ImportServices](#section-3-6-9)
    - [3.7. Consumer management](#section-3-7)
        - [3.7.1. ListApps](#section-3-7-1)
        - [3.7.2. ListAppsByGwInstanceId](#section-3-7-2)
        - [3.7.3. GetApp](#section-3-7-3)
        - [3.7.4. CreateApp](#section-3-7-4)
        - [3.7.5. ModifyApp](#section-3-7-5)
        - [3.7.6. DeleteApp](#section-3-7-6)
        - [3.7.7. ModifyAppOpenStatus](#section-3-7-7)
        - [3.7.8. ModifyAppWhiteListStatus](#section-3-7-8)
        - [3.7.9. GetAppAuth](#section-3-7-9)
        - [3.7.10. CreateAppAuth](#section-3-7-10)
        - [3.7.11. BatchCreateAppAuthByRoute](#section-3-7-11)
        - [3.7.12. ModifyAppAuthStatus](#section-3-7-12)
        - [3.7.13. DeleteAppAuth](#section-3-7-13)
        - [3.7.14. RefreshToken](#section-3-7-14)
        - [3.7.15. ResetSecretKey](#section-3-7-15)
        - [3.7.16. HandlerConsumerAuth](#section-3-7-16)
        - [3.7.17. CreateAppAuthByRoute](#section-3-7-17)
        - [3.7.18. BatchDeleteApp](#section-3-7-18)
    - [3.8. Plugin Management](#section-3-8)
        - [3.8.1. ListPlugins](#section-3-8-1)
        - [3.8.2. ListOpenPlugins](#section-3-8-2)
        - [3.8.3. ListGlobalPlugins](#section-3-8-3)
        - [3.8.4. ListRoutePlugins](#section-3-8-4)
        - [3.8.5. GetPlugin](#section-3-8-5)
        - [3.8.6. CreatePlugin](#section-3-8-6)
        - [3.8.7. CreateGlobalPlugin](#section-3-8-7)
        - [3.8.8. CreateRoutePlugin](#section-3-8-8)
        - [3.8.9. ModifyPlugin](#section-3-8-9)
        - [3.8.10. ModifyGlobalPlugin](#section-3-8-10)
        - [3.8.11. ModifyRoutePlugin](#section-3-8-11)
        - [3.8.12. DeletePlugin](#section-3-8-12)
        - [3.8.13. DeleteGlobalPlugin](#section-3-8-13)
        - [3.8.14. DeleteRoutePlugin](#section-3-8-14)
        - [3.8.15. ModifyGlobalPluginStatus](#section-3-8-15)
        - [3.8.16. ModifyRoutePluginStatus](#section-3-8-16)
        - [3.8.17. ListPluginUsage](#section-3-8-17)
    - [3.9. Policy Management](#section-3-9)
        - [3.9.1. ModifyStrategyConfig](#section-3-9-1)
        - [3.9.2. CreateStrategyConfig](#section-3-9-2)
        - [3.9.3. ListStrategies](#section-3-9-3)
        - [3.9.4. ListStrategyConfigs](#section-3-9-4)
        - [3.9.5. GetStrategy](#section-3-9-5)
        - [3.9.6. GetStrategyConfig](#section-3-9-6)
        - [3.9.7. GetRoutePolicies](#section-3-9-7)
        - [3.9.8. ModifyRoutePolicy](#section-3-9-8)
        - [3.9.9. DeleteStrategyConfig](#section-3-9-9)
        - [3.9.10. ModifyStrategyConfigStatus](#section-3-9-10)
    - [3.10. Domain name management](#section-3-10)
        - [3.10.1. ListDomains](#section-3-10-1)
        - [3.10.2. ListAllDomains](#section-3-10-2)
        - [3.10.3. GetDomain](#section-3-10-3)
        - [3.10.4. CreateDomain](#section-3-10-4)
        - [3.10.5. ModifyDomain](#section-3-10-5)
        - [3.10.6. DeleteDomain](#section-3-10-6)
    - [3.11. Certificate Management](#section-3-11)
        - [3.11.1. ListCertificates](#section-3-11-1)
        - [3.11.2. ListAllServerCertificates](#section-3-11-2)
        - [3.11.3. ListAllCACertificates](#section-3-11-3)
        - [3.11.4. GetCertificate](#section-3-11-4)
        - [3.11.5. CreateCertificate](#section-3-11-5)
        - [3.11.6. ModifyCertificate](#section-3-11-6)
        - [3.11.7. DeleteCertificate](#section-3-11-7)
    - [3.12. Other](#section-3-12)
        - [3.12.1. GetTotalityInfo](#section-3-12-1)
        - [3.12.2. GetSettings](#section-3-12-2)
        - [3.12.3. GetSlsStatistics](#section-3-12-3)

<a id="section-1"></a>

# 1.Preparations

<a id="section-1-1"></a>

## 1.1. Obtain API information and endpoints

Obtain information about a product's open API operations, including the product name (code), API operation name, and API version.

**Background information**

The API information in the API directory of the Apsara Uni-manager Management Console is for reference only. For instructions on how to use a specific API, see the developer guide for the corresponding cloud product. If any inconsistencies exist, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.

2. In the top menu bar, choose **Products** > **Developer Tools** > **API & Tools** > **Developer Portal**.

3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.

   ![](assets/2c46abb9ede40ba27b69fc91474a92c6.jpeg)

4. In the navigation pane on the left, select the target cloud product.

5. From the **Version** drop-down list, select the target API version.

6. In the API list, review the API operations for the current version.

7. Select the desired API operation. Obtain the POP Endpoint information for the cloud product, which is displayed under the parameter name.

<a id="section-1-2"></a>

## 1.2. Obtain an AccessKey

An AccessKey supports two authorization patterns: Resource Access Management (RAM) and Security Token Service (STS). You can use an AccessKey from either pattern to initiate a call. This topic describes how to obtain an AccessKey that uses RAM authorization.

**Background information**

An AccessKey uses an AccessKey ID and an AccessKey secret for symmetric encryption to authenticate the identity of a request sender. The AccessKey ID identifies the user, and the AccessKey secret is a string used to create an encrypted signature.

The two authorization patterns for an AccessKey are:

- RAM authorization, which grants an AccessKey ID and an AccessKey secret to a third-party requester.

- STS authorization, which grants an AccessKey ID, an AccessKey secret, and a security token to a third-party requester. For more information, see Obtain an STS AccessKey.

The Apsara Uni-manager Management Console provides individual AccessKeys and organization AccessKeys. Only operations administrators and primary organization administrators can obtain organization AccessKeys. You can use an individual account AccessKey to call the APIs of the Apsara Uni-manager Management Console and related cloud products. If you use an individual account AccessKey, you must add the following restrictive parameters to the header. Otherwise, a permission error may occur:

> **Warning**
>
> An individual account AccessKey is a restricted AccessKey managed by the permission system of the Apsara Uni-manager Management Console, whereas an organization AccessKey has broader permissions. Therefore, administrators must confirm the security of operations that use an organization AccessKey.

| Parameter | Description |
| --- | --- |
| x-acs-regionid | The region, such as cn-hangzhou-\*. |
| x-acs-organizationid | The ID of the corresponding organization in the Apsara Uni-manager Management Console. For more information, see the <strong>GetOrganizationList</strong> topic in the <strong>Apsara Uni-manager</strong> <strong>Management Console Developer Guide</strong>. |
| x-acs-resourcegroupid | The ID of the corresponding resource set in the Apsara Uni-manager Management Console. For more information, see the <strong>ListResourceGroup</strong> topic in the <strong>Apsara Uni-manager</strong> <strong>Management Console Developer Guide</strong>. |
| x-acs-instanceid | The ID of the instance on which you want to perform an operation. For example, you can find the instance ID of an ECS instance in the ECS instance list. |

**Obtain an individual account AccessKey**

To obtain an AccessKey for an individual account, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console.

2. In the upper-right corner of the page, click your profile picture, and then click **Personal Information**.

3. In the **AccessKey** section, view the AccessKey information for your individual account.

   ![](assets/a0c6c22806c62349a0f9840932305e11.png)

   > **Note**
   >
   > The AccessKey ID and AccessKey secret are the keys to access your cloud resources and grant full permissions to your account. Keep them confidential.

**Obtain an organization AccessKey**

To obtain an organization AccessKey, perform the following steps:

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top menu bar, click **Enterprise**.

3. In the navigation pane on the left, choose **Resource Management > Organization Management**.

4. In the organization chart, click the name of the target primary organization.

5. Click **Manage AccessKey**.

6. In the dialog box that appears, view the organization AccessKey information.

<a id="section-1-3"></a>

## 1.3. Get common header parameters

API calls require several header parameters. This topic describes how to obtain these parameters and explains the return values.

**Get the Region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top menu bar, click **Enterprise**.

3. In the navigation pane on the left, choose **Resource Management** > **Region Management**.

4. Click the name of the target organization.

5. In the **Region List** on the right, find the **Region Name**. This value is the Region ID.

**Get the organization ID**

You can obtain the organization ID by calling an API. You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the organization ID.

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top menu bar, click **Products**, and then choose **Developer Tools** > **APIs And Tools** > **Developer Portal**.

3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.

4. Click the <img src="assets/a399ea52e5bed707f6f6a0b92044c5ca.png" width="26" alt=""> button, choose **Cloud Platform** > **Unified Cloud Management Platform**,

   and set **Version** to **2019-05-10**.

5. In the text box, enter  `GetOrganizationList`  to start online debugging. For the name parameter, enter the target organization name and make the call. If the call is successful, find the value of **id** in the **Call Result**. This value is the organization ID. For more information, see the *GetOrganizationList* chapter in the *Apsara Uni-manager Management C onsole Development Guide*.

**Get the resource group ID**

You can obtain the resource group ID by calling an API. You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the resource group ID.

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top menu bar, click **Products**, and then choose **Developer Tools** > **APIs And Tools** > **Developer Portal**.

3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.

4. Click the <img src="assets/a399ea52e5bed707f6f6a0b92044c5ca.png" width="26" alt=""> button, choose **Cloud Platform** > **Unified Cloud Management Platform**,

   and set **Version** to **2019-05-10**.

5. In the text box, enter  `ListResourceGroup`  to start online debugging. If the call is successful, find the value of **id** in the **Call Result**. This value is the resource group ID. For more information, see the *ListResourceGroup* chapter in the *Apsara Uni-manager Managem ent Console Development Guide*.

**Get the instance ID**

You can obtain the instance ID from the instance list of a cloud product in the Apsara Uni-manager Management Console. This topic uses API Gateway as an example.

1. Log on to the Apsara Uni-manager Management Console.

2. In the top menu bar, choose **Products** > **Middleware** > **Application Integration** > **API Gateway**.

3. In the navigation pane on the left, click **Instance List**.

4. In the instance list, find the **Instance ID**.

**Return parameters**

When you call an API to list resource instances of a cloud product, the following parameters are returned by default.

| Name | Description |
| --- | --- |
| ResourceGroupName | The name of the resource group. |
| ResourceGroup | The ID of the resource group. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

<a id="section-1-4"></a>

## 1.4. Obtain an STS AccessKey

This topic describes how to use Security Token Service (STS) to call product APIs in Apsara Stack.

**Background information**

Alibaba Cloud Security Token Service (STS) is a service that provides temporary access permissions. You can use STS to call Apsara Stack product APIs.

**Procedure**

1. Obtain the  `RAM Role`  of the user role.

   <ol type="i">

   <li>

   Log on to the Apsara Uni-manager Management Console.

   </li>

   <li>

   In the upper-right corner of the page, click the profile picture and select **Personal**

   </li>

   </ol>

   **Information**.

   <ol type="i" start="3">

   <li>

   Click **View Current Role Policy**.

   </li>

   </ol>

   In the **Current Role Policy** dialog box, you can view the  `RAM Role` .

2. Use the following code and the  `RAM Role`  to obtain the  `stsAK` ,  `stsSK` , and  `stsToken` .

   ```java
   public static void main(String[] args) {
        ASClient asClient = new ASClient();
        // Specify the call source.
           asClient.setSdkSource("test");
        // Pass the ARN.
           String assumeRole = AssumeRole(asClient, "<RAM Role>");

           JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);

           JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");

           // Obtain the STS trituple.
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
           reqParams.put("AccessKeyId", <your_access_key_id>);
        // The AccessKey secret of the current user.
           reqParams.put("AccessKeySecret", <your_access_key_secret>);

           reqParams.put("roleSessionName", "StsUser");

           reqParams.put("roleArn", roleArn);

           return asClient.doRequest(endpoint, headers, reqParams);
   }
   ```

3. Use the STS credentials to call product APIs, as shown in the following example.

   ```java
   import com.aliyun.credentials.Client;
   import com.aliyun.credentials.models.Config;

   // The following example shows how to use an STS token to initialize the credential client. This example does not include the procedure for obtaining the STS token.
   public class DemoStsTest {
       public static void main(String[] args) {
           Config credentialConfig = new Config();
           credentialConfig.setType("sts");
           // Replace this with the AccessKeyId from the STS trituple obtained in the previous step.
           credentialConfig.setAccessKeyId("your_AccessKeyId");
           // Replace this with the AccessKeySecret from the STS trituple obtained in the previous step.
           credentialConfig.setAccessKeySecret("your__AccessKeySecret");
           // Replace this with the SecurityToken from the STS trituple obtained in the previous step.
           credentialConfig.setSecurityToken("your__SecurityToken");
           Client credentialClient = new Client(credentialConfig);

           // Continue to call the API. For more information, see the complete API documentation.
       }
   }
   ```

<a id="section-1-5"></a>

## 1.5. Obtain user and role information

This topic describes how to obtain user and role information.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. Create a user.

   <ol type="i">

   <li>

   In the top navigation bar, select **Enterprise**.

   </li>

   <li>

   In the left-side navigation pane, select **User Management > User Management**.

   </li>

   <li>

   On the **System Users** tab, click **Create User.**

   </li>

   <li>

   In the **Create User** dialog box, configure the user information and click **OK**.

   For more information about configuration, see the **Apsara Uni-manager Management Console User Guide > Create a user** section.

   </li>

   </ol>

3. Create a role.

   <ol type="i">

   <li>

   In the left-side navigation pane, select **Role-Based Access Control** **> Role Authorization**.

   </li>

   <li>

   Above the role list, click **Create Custom Role**.

   </li>

   <li>

   Set **Basic Configurations** and click **Next**.

   </li>

   </ol>

   **Management scope**: Select **Resource set**.

   <ol type="i" start="4">

   <li>

   Set **Management Permission**. In the permission list, select the permissions for **View RAM Service Roles** and **Create RAM Service Roles**, and then click **Next**.

   </li>

   <li>

   Set **Application Permissions**. In the permission list, select **API Gateway** with **Read-Only** and **Read and write permissions**, and then click **Next**.

   </li>

   <li>

   Set **Menu Permissions**. In the list, select **API Gateway** and click **Next** or **Create**.

   </li>

   </ol>

4. Assign the role to the user.

   <ol type="i">

   <li>

   In the left-side navigation pane, select **User Management > User Management**.

   </li>

   <li>

   On the **System Users** tab, find the newly created user, click <img src="assets/c266cf685bb43a5383d1f321e8e2788f.png" width="14" alt=""> in the **Actions** column,

   </li>

   </ol>

   and then select **Role Authorization**.

   <ol type="i" start="3">

   <li>

   In the **Role Authorization** dialog box, add the newly created user role and click **OK**.

   </li>

   </ol>

5. Add the user to a resource set.

   <ol type="i">

   <li>

   On the **System Users** tab, find the newly created user and click the username.

   </li>

   <li>

   On the **Resource Sets** tab, click **Join Resource Set** above the list.

   </li>

   <li>

   In the **Join Resource Set** dialog box, select the user role from the **Select Role Type**

   </li>

   </ol>

   drop-down list, select the resource sets to join in the **Select Resource Set** list, and then click **OK**.

<a id="section-1-6"></a>

## 1.6. Obtain the region ID and organization ID

This topic describes how to obtain the region ID and organization ID.

**Obtain the region ID**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Enterprise**.

3. **Resource Management > Region Management**.

4. In the left-side organizational structure, click the target organization. On the right side, find the **Region List** and obtain the Region ID.

**Obtain the organization ID**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Product > Middleware > Application Integration > API Gateway**.

3. In the left-side navigation pane, select **API Gateway > Instance list** or **AI Gateway**.

4. On the **Gateway Instance** page, open the developer tools, click the Network tab, and then refresh the page.

5. In the search box, enter **ListResourceGroupByOrgId**. Click the API operation name. On the Preview tab on the right, obtain the organization ID.

   ![](assets/bc213dbcb115fa0cda3a0fb4c4090d7d.jpeg)

<a id="section-2"></a>

# 2.Calling Apsara Stack APIs through a POP gateway

<a id="section-2-1"></a>

## 2.1. Java version

**Environment requirements**

Supports JDK 8 to JDK 19. The platform supports Linux, Mac, and Windows.

**Installation code**

Use the Maven dependency configuration:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <!-- Note: Use the version number specified in the developer documentation for your
Apsara Stack environment. -->
    <version>4.6.0</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.53</version>
</dependency>
```

**Installation documentation**

**Configuration instructions**

| Parameter | Description |
| --- | --- |
| regionId | The ID of the region.<br>See Obtain the region ID and organization ID. |
| AccessKeyId | The AccessKey ID of the user.<br>See Obtain an AccessKey. |
| AccessKeySecret | The AccessKey secret of the user.<br>See Obtain an AccessKey. |
| endpoint | The endpoint for API access.<br>See Obtain API information and endpoints. |
| organizationId | The ID of the organization.<br>See Obtain the region ID and organization ID. |
| httpProxy | The proxy endpoint (optional).<br>Contact Alibaba Cloud on-site personnel to obtain this information. |

**Code example**

The following example shows how to call an API Gateway console interface by using a common request:

```java
package com.aliyun.apsarastack;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.AcsResponse;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.HttpClientConfig;
import com.aliyuncs.http.HttpResponse;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

/**
 * Example of calling an API Gateway console interface by using a common request
 */
public class Sample {

    private static IAcsClient client;

    // Define the API path.
    private static final String LIST_ROUTES = "/route/listRoutes";

    public static void main(String[] args) throws ClientException {
        listRoutes();
    }

    /**
     * Example of querying a route list
     */
    private static void listRoutes() throws ClientException {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);
        request.put("size", 10);
        request.put("gwInstanceId", "your_instance_id");

        CommonResponse response = getCommonResponse(request, LIST_ROUTES, 
MethodType.POST);
        HttpResponse httpResponse = response.getHttpResponse();

        if (httpResponse.getStatus() == 200) {
            JSONObject jsonObject = 
JSON.parseObject(httpResponse.getHttpContentString());
            if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
                Object data = jsonObject.get("data");
                if (data instanceof JSONObject) {
                    JSONObject dataObj = (JSONObject) data;
                    JSONArray records = (JSONArray) dataObj.get("records");
                    records.forEach(record -> {
                        System.out.println(JSON.toJSONString(record));
                    });
                }
            }
            System.out.println(jsonObject);
        }
    }

    /**
     * Common request method
     *
     * @param param Request parameters
     * @param path API path
     * @param methodType HTTP method type
     * @return Response result
     * @throws ClientException Client exception
     */
    public static CommonResponse getCommonResponse(Object param, String path, MethodType methodType) throws ClientException {
        CommonRequest request = new CommonRequest();
        request.setSysUriPattern(path);
        request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8", 
FormatType.JSON);
        initDefaultHeader(request, methodType);
        return client.getCommonResponse(request);
    }

    static {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
                "<your-regionId>",      // The region ID.
                "<AccessKey ID>",        // The AccessKey ID.
                "<AccessKey Secret>");   // The AccessKey secret.

        // Optional: Configure a proxy.
        HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
        httpClientConfig.setHttpProxy("http://127.0.0.1:9898");
        profile.setHttpClientConfig(httpClientConfig);

        client = new DefaultAcsClient(profile);
    }

    /**
     * Configure request headers.
     *
     * @param request Request object
     * @param methodType HTTP method type
     * @param <T> Response type
     */
    private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request, MethodType methodType) {
        // Required: Specify the caller. Typically, use the unique identifier of the calling application.
        request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name");

        // Required: Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");

        // Optional: Specify the resource group ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");

        // Optional: Specify the role ID.
        // request.putHeadParameter("x-acs-roleId", "<your-roleId>");

        // Set the request method.
        request.setSysMethod(methodType);

        // Set the cloud service endpoint.
        request.setSysDomain("<your-endpoint>");

        // Set LocationProduct.
        request.setSysProduct("csb-cop");

        // Set the API version.
        request.setSysVersion("2023-02-06");
    }
}
```

**Step examples**

1. **Initialize the client**

Create  `DefaultProfile`  and configure information such as the AccessKey ID, AccessKey secret, and endpoint:

```text
DefaultProfile profile = DefaultProfile.getProfile(
        "<your-regionId>",      // The region ID.
        "<AccessKey ID>",        // The AccessKey ID.
        "<AccessKey Secret>");   // The AccessKey secret.

// Optional: Configure a proxy.
HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
httpClientConfig.setHttpProxy("http://127.0.0.1:9898");
profile.setHttpClientConfig(httpClientConfig);

IAcsClient client = new DefaultAcsClient(profile);
```

2. **Build request parameters**

Build a request parameter map based on the requirements of the specific API:

```text
Map<String, Object> request = new HashMap<>();
request.put("current", 1);
request.put("size", 10);
request.put("gwInstanceId", "your_instance_id");
```

3. **Create a CommonRequest**

Set the request path, request body, and request method:

```text
CommonRequest request = new CommonRequest();
request.setSysUriPattern("/route/listRoutes");
request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8", FormatType.JSON);
```

4. **Set request headers**

Set required header information:

```text
request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name");
request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
request.setSysMethod(MethodType.POST);
request.setSysDomain("<your-endpoint>");
request.setSysProduct("csb-cop");
request.setSysVersion("2023-02-06");
```

5. **Send the request and process the response**

```java
CommonResponse response = client.getCommonResponse(request);
HttpResponse httpResponse = response.getHttpResponse();

if (httpResponse.getStatus() == 200) {
    JSONObject jsonObject = JSON.parseObject(httpResponse.getHttpContentString());
    if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
        Object data = jsonObject.get("data");
        // Process the returned data.
        System.out.println(JSON.toJSONString(data));
    }
}
```

6. **Handle exceptions**

```java
try {
    CommonResponse response = client.getCommonRequest(request);
    // Process the response.
} catch (ClientException e) {
    // Handle client exceptions.
    System.out.println("ErrorCode: " + e.getErrCode());
    System.out.println("ErrorMessage: " + e.getErrMsg());
}
```

**Call method for self-managed ACK environments**

In a self-managed ACK environment, you do not need information such as the AccessKey pair or proxy. You can make calls directly through the endpoint of the console service.

**Obtain the console endpoint**

```bash
kubectl get svc -n <namespace where the console service resides>
```

Find the IP address of  `cop-gateway-admin-svc`  and use it as the endpoint.

**Code example**

```text
static {
    // Create a DefaultAcsClient instance and initialize it.
    DefaultProfile profile = DefaultProfile.getProfile(
            "-",  // The region ID is not required.
            "-",  // The AccessKey ID is not required.
            "-"); // The AccessKey secret is not required.

    client = new DefaultAcsClient(profile);
}

private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request, MethodType methodType) {
    // The authentication header specific to self-managed ACK environments.
    request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
    request.putHeadParameter("X-CSB-OPENAPI", "true");

    request.setSysMethod(methodType);
    request.setSysDomain("<IP address of the console service>");  
    request.setSysProduct("csb-cop");
    request.setSysVersion("2023-02-06");
}
```

**Common API paths**

| Feature | API path |
| --- | --- |
| Query the instance list | <code>/gatewayInstance/listInstances</code> |
| Create a service | <code>/microservice/createService</code> |
| Query the route list | <code>/route/listRoutes</code> |
| Create a route | <code>/route/createRoute</code> |
| Query the domain name list | <code>/domain/listDomains</code> |

<a id="section-2-2"></a>

## 2.2. Common API call methods

**Overview**

This document describes the common API call methods for the API Gateway console, including request format, response format, and authentication method. These methods apply to all interfaces of API Gateway (SCG) and AI Gateway (Higress).

**Basic interface information**

| Item | Description |
| --- | --- |
| Protocol | HTTP/HTTPS |
| Request method | POST (primary), GET |
| Data format | JSON |
| Character encoding | UTF-8 |
| Interface prefix | <code>/</code> |

**Unified request format**

**Request headers**

| Parameter | Required | Description |
| --- | --- | --- |
| <code>Content-Type</code> | Yes | <code> application/json </code>. |
| <code>Authorization</code> | Yes | The user authentication token. |
| <code>x-acs-request-id</code> | No | The request trace ID for log tracing. |

**Request body**

All APIs use a JSON-formatted request body. The basic structure is as follows:

```json
{
  "gwInstanceId": "xxx",
  ... // Other business parameters
}
```

> **Note**
>
> Most APIs require the gwInstanceId parameter to specify the gateway instance for the operation.

**Unified response format**

**Response structure**

| Parameter | Type | Description |
| --- | --- | --- |
| <code>requestId</code> | String | The request trace ID. |
| <code>code</code> | Integer | The response status code. |
| <code>msg</code> | String | The response message. The system returns an error message if an error occurs. |
| <code>data</code> | Object | The response data, which is the business data. |

**Status code description**

| Status code | Description |
| --- | --- |
| <code>200</code> | The request succeeded. |
| <code>500</code> | The request failed due to a business exception. |
| <code>400</code> | The request parameters are invalid. |
| <code>401</code> | Unauthorized or authentication failed. |

**Successful response example**

```json
{
  "requestId": "abc****456",
  "code": 200,
  "msg": null,
  "data": {
    "routeId": "route-001",
    "routeName": "test-route"
  }
}
```

**Failed response example**

```json
{
  "requestId": "ab****f456",
  "code": 500,
  "msg": "Route not found",
  "data": null
}
```

**Paged response example**

```json
{
  "requestId": "ab****456",
  "code": 200,
  "msg": null,
  "data": {
    "size": 10,
    "current": 1,
    "total": 100,
    "records": [
      { "id": "1", "name": "item-1" },
      { "id": "2", "name": "item-2" }
    ]
  }
}
```

**Authentication method**

**User authentication**

Pass the authentication token through the  `Authorization`  request header:

```text
Authorization: Bearer <token>
```

Or use cookie-based authentication (for the web console).

**Consumer authentication (API call)**

When calling a gateway API, the consumer passes the API key in one of the following ways:

| Method | Description |
| --- | --- |
| Request header | <code> Authorization: Bearer &lt;api-key&gt; </code> or <code> x-</code><code>api-key: &lt;api-key&gt; </code>. |
| Query parameter | <code> ?api_key=&lt;api-key&gt; </code>. |

The specific authentication method depends on the authentication configuration of the gateway instance.

**General parameter description Gateway instance ID (gwInstanceId)**

Most APIs require the gateway instance ID to identify the target instance for the operation. The system automatically identifies the gateway type based on the instance ID and executes the corresponding processing logic.

**Pagination parameters**

List query APIs support the following pagination parameters:

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| <code>current</code> | Integer | 1 | The current page number. |
| <code>size</code> | Integer | 10 | The number of entries per page. |

**Search parameters**

List query APIs support the following search parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| <code>searchName</code> | String | The search keyword. The system performs a fuzzy match by name. |

**API overview**

**API Gateway APIs**

| Module | API path | Description |
| --- | --- | --- |
| Route management | <code>/route</code> | Manage route configurations. |
| Service management | <code>/service</code> | Manage service registration. |
| Domain name management | <code>/domain</code> | Manage domain name bindings. |
| Consumer management | <code>/app</code> | Manage consumers and API keys. |
| Certificate management | <code>/certificate</code> | Manage SSL certificates. |
| Origin management | <code>/source</code> | Manage service origins. |
| Policy management | <code>/strategy</code> | Configure routing policies. |
| Policy configuration | <code>/strategyConfig</code> | Manage policy instances. |
| Instance management | <code>/gatewayInstance</code> | Manage gateway instances. |
| Cluster management | <code>/k8sCluster</code> | Manage Kubernetes clusters. |

**Error handling**

**Business exceptions**

When a business logic exception occurs, the system returns:

```json
{
  "code": 500,
  "msg": "<error message>",
  "data": null
}
```

Common business exceptions:

| Error message | Description |
| --- | --- |
| <code>Route not found</code> | The route does not exist. |
| <code>Service not found</code> | The service does not exist. |
| <code>Permission denied</code> | Insufficient permissions. |
| <code>Instance not found</code> | The gateway instance does not exist. |

**Parameter validation exceptions**

When request parameter validation fails, the system returns:

```json
{
  "code": 500,
  "msg": "<field> <error message>",
  "data": null
}
```

Example:

```json
{
  "code": 500,
  "msg": "gwInstanceId must not be blank",
  "data": null
}
```

**Request examples**

**cURL example**

```bash
# Create a route
curl -X POST 'http://localhost:8080/route/createRoute' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <token>' \
  -d '{
    "gwInstanceId": "instance-001",
    "routeName": "test-route",
    "path": "/api/test",
    "serviceId": "service-001"
  }'
```

**HTTP request example**

```http
POST /route/createRoute HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Authorization: Bearer <token>

{
  "gwInstanceId": "instance-001",
  "routeName": "test-route",
  "path": "/api/test",
  "serviceId": "service-001"
}
```

**Best practice**

1. **Request tracing**

- Always include a unique  `x-acs-request-id`  in the request header.

- The response returns the same requestId to facilitate log tracing and troubleshooting.

  2. **Error handling**

- Check the  `code`  field in the response to determine whether the request succeeded.

- `code=200`  indicates success. Other values indicate failure.

- Obtain error messages from the  `msg`  field.

  3. **Paged queries**

- Use pagination parameters for list operations to avoid excessive data volume.

- Obtain the total number of records from the  `total`  field.

- Obtain the data for the current page from the  `records`  field.

  4. **Instance differentiation**

- Confirm the gateway type that corresponds to  `gwInstanceId`  before you perform an operation.

- Call  `/gatewayInstance/getInstance`  to query instance details and confirm the type.

<a id="section-2-2-1"></a>

### 2.2.1. API call - Cluster management

**Overview**

The cluster management module provides features to import, query, and update Kubernetes clusters. A cluster provides the deployment environment for gateway instances. The system supports two cluster types: self-managed Kubernetes clusters and ACK clusters.

- **Applicable engines**: SCG / Higress

- **API path prefix**:  `/k8s`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header and use a valid AccessKey pair.

**Import a cluster**

**API description**

Import a Kubernetes cluster to the gateway console.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/importCluster</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ImportK8sClusterRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| k8sClusterName | String | Yes | The name of the cluster. The name must contain 2 to 128 characters and start with a letter. |
| k8sClusterType | String | No | The cluster type:<br>• self-built: Self-managed Kubernetes cluster<br>• container-service: ACK cluster |
| configContent | String | Conditional | The configuration content of the KubeConfig file.<br>Note<br>You must specify this parameter for self-managed clusters. |
| k8sClusterAttribute | Object | Conditional | The extended attributes of the cluster.<br>Note<br>You must specify this parameter for ACK clusters. |

**k8sClusterAttribute structure**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| csClusterId | String | Conditional | The ID of the ACK cluster.<br>Note<br>You must specify this parameter when the type is <code>container-</code><code>service </code>. |

**Query the cluster list**

**API description**

Query the Kubernetes cluster list by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/listClusters</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListK8sClusterRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| clusterName | String | No | The name of the cluster. This parameter supports fuzzy search. |

**Query all clusters**

**API description**

Query the list of all Kubernetes clusters without pagination.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/getClusterList</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

This API requires no request parameters.

**Update a cluster**

**API description**

Update the information of a Kubernetes cluster.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/updateCluster</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpdateK8sClusterRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| clusterCode | String | Yes | The cluster code. |
| k8sClusterAttribute | String | Yes | The extended attributes of the cluster (JSON string). |

**Cancel cluster import**

**API description**

Cancel the import of a Kubernetes cluster.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/cancelImportCluster</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CancelImportK8sClusterRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| k8sClusterCode | String | Yes | The cluster code. |

**Test the cluster connection**

**API description**

Test whether the Kubernetes cluster connection is normal.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/checkConnectCluster</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CheckK8sClusterConnectRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| clusterCode | String | Yes | The cluster code. |

**Query the cluster name**

**API description**

Query the cluster name by cluster code.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/getK8sClusterName</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetK8sClusterNameRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| clusterCode | String | Yes | The cluster code. |

**Query cluster information associated with an instance**

**API description**

Query the associated Kubernetes cluster information by instance ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/k8s/getK8sClusterInfoByGwInstanceId</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetK8sClusterInfoRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the cluster management API by using the Common Request method. A self-managed ACK environment and an Enterprise Edition environment differ only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class ClusterApiDemo {

    // ========== Environment configuration (modify based on the actual environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Import a self-managed Kubernetes cluster ==========
        String clusterCode = importSelfBuiltCluster(client);

        // ========== Import an ACK cluster ==========
        // String csClusterCode = importContainerServiceCluster(client);

        // ========== Test cluster connectivity ==========
        checkConnect(client, clusterCode);

        // ========== Query the cluster list ==========
        listClusters(client);

        // ========== Query all clusters ==========
        getClusterList(client);

        // ========== Query the cluster name ==========
        getK8sClusterName(client, clusterCode);

        // ========== Cancel cluster import ==========
        // cancelImportCluster(client, clusterCode);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Import a self-managed Kubernetes cluster (based on ImportK8sClusterRequest)
     */
    private static String importSelfBuiltCluster(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-self-built-cluster");         // [Required] Cl
uster name
        request.put("k8sClusterType", "self-built");                    // [Optional] Cl
uster type: self-built
        request.put("configContent", "your-kubeconfig-content");        // [Required] Ku
beConfig configuration

        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importSelfBuiltCluster success, clusterCode: " + 
clusterCode);
            return clusterCode;
        } else {
            System.out.println("importSelfBuiltCluster failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Import an ACK cluster (based on ImportK8sClusterRequest)
     */
    private static String importContainerServiceCluster(IAcsClient client) throws Exception {
        Map<String, Object> attribute = new HashMap<>();
        attribute.put("csClusterId", "ce********b5587f5ec1c");  // [Required] ACK 
cluster ID

        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-cs-cluster");                  // [Required] C
luster name
        request.put("k8sClusterType", "container-service");              // [Required] C
luster type: container-service
        request.put("k8sClusterAttribute", attribute);                   // [Required] C
luster extended attributes

        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importContainerServiceCluster success, clusterCode: " +clusterCode);
            return clusterCode;
        } else {
            System.out.println("importContainerServiceCluster failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Query the cluster list (based on ListK8sClusterRequest)
     */
    private static void listClusters(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);                                       // [Required] Cu
rrent page number
        request.put("size", 10);                                         // [Required] Nu
mber of entries per page
        // request.put("clusterName", "");                                  // [Optional]
Cluster name (fuzzy search)

        CommonRequest commonRequest = createBaseRequest("/k8s/listClusters");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listClusters: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query all clusters
     */
    private static void getClusterList(IAcsClient client) throws Exception {
        CommonRequest commonRequest = createBaseRequest("/k8s/getClusterList");
        commonRequest.setHttpContent(new byte[0], "UTF-8", FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getClusterList: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Test cluster connectivity (based on CheckK8sClusterConnectRequest)
     */
    private static void checkConnect(IAcsClient client, String clusterCode) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required] 
Cluster code

        CommonRequest commonRequest = createBaseRequest("/k8s/checkConnectCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("checkConnectCluster: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query the cluster name (based on GetK8sClusterNameRequest)
     */
    private static void getK8sClusterName(IAcsClient client, String clusterCode) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required] 
Cluster code

        CommonRequest commonRequest = createBaseRequest("/k8s/getK8sClusterName");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getK8sClusterName: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query the cluster information associated with an instance (based on 
GetK8sClusterInfoRequest)
     */
    private static void getK8sClusterInfoByGwInstanceId(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // [Required] G
ateway instance ID

        CommonRequest commonRequest = 
createBaseRequest("/k8s/getK8sClusterInfoByGwInstanceId");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getK8sClusterInfoByGwInstanceId: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Update a cluster (based on UpdateK8sClusterRequest)
     */
    private static void updateCluster(IAcsClient client, String clusterCode) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required] 
Cluster code
        request.put("k8sClusterAttribute", "{\"key\":\"value\"}");       // [Required] 
Cluster extended attributes in JSON format

        CommonRequest commonRequest = createBaseRequest("/k8s/updateCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("updateCluster: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Cancel cluster import (based on CancelImportK8sClusterRequest)
     */
    private static void cancelImportCluster(IAcsClient client, String clusterCode) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterCode", clusterCode);                      // [Required] C
luster code

        CommonRequest commonRequest = createBaseRequest("/k8s/cancelImportCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("cancelImportCluster: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Cluster type description**

| k8sClusterType | Description |
| --- | --- |
| self-built | Self-managed Kubernetes cluster. You must provide the KubeConfig. |
| container-service | ACK cluster. You must provide the cluster ID. |

**Response code description**

| Code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | The request contains invalid parameters. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-2"></a>

### 2.2.2. API call - Origin management

**Overview**

The origin management module provides functions to create, delete, modify, and query service registration centers. Origins are used for service discovery. SCG supports four origin types: Nacos, microservice namespace (EDAS), Eureka, and Database.

- **Applicable engine**: SCG (API Gateway)

- **API path prefix**:  `/source`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header, and use a valid AK/SK pair.

**Create an origin**

**API description**

Create an origin for a service registry.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/source/createSource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| sourceName | String | Yes | The name of the origin. |
| sourceType | Integer | Yes | The type of the origin:<br>• 1: Nacos<br>• 2: Microservice space (EDAS)<br>• 3: Eureka<br>• 5: Database |
| description | String | No | The description of the origin. |
| sourceStruct | Object | Yes | The configuration structure of the origin.<br>Note<br>The configuration structure varies depending on the origin type. |

**sourceStruct configurations for different origin types**

**Nacos (sourceType=1):**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| nacosRegistry | String | Yes | The endpoint of the Nacos registry. |
| nacosNamespaceId | String | Yes | The ID of the Nacos namespace. |
| nacosGroupName | String | No | The name of the Nacos group. Default value: DEFAULT_GROUP. |
| nacosAccessKey | String | No | The AccessKey for Nacos authentication. |
| nacosSecretKey | String | No | The SecretKey for Nacos authentication. |
| checkType | Integer | No | The validation type:<br>• 0: No validation<br>• 1: Validate connection |

**Microservice namespace/EDAS (sourceType=2):**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| edasNameSpaceId | String | Yes | The ID of the EDAS namespace. |
| type | Integer | Yes | The type:<br>0: Nacos (DNCS)<br>1: ConfigServer (DNCS) |
| edasEndPoint | String | Conditional | The endpoint of EDAS.<br>Note<br>This parameter is required in address server mode. |
| edasServerAddr | String | Conditional | The server address of EDAS.<br>Note<br>This parameter is required in direct connection mode. |
| edasAccessKey | String | Yes | The AccessKey of EDAS. |
| edasSecretKey | String | Yes | The SecretKey of EDAS. |

**Eureka (sourceType=3):**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| eurekaRegistry | String | Yes | The endpoint of the Eureka registration center. |
| checkType | Integer | No | The verification type:<br>• 0: No verification<br>• 1: Verify connection |

**Database (sourceType=5):**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| databaseType | Integer | Yes | The type of the database:<br>0: MySQL<br>1: PostgreSQL |
| jdbcUrl | String | Yes | The JDBC connection string. |
| username | String | Yes | The username for the database. |
| password | String | Yes | The password for the database. |
| maxConnection | Integer | No | The maximum number of connections. |
| maxIdleConnection | Integer | No | The maximum number of idle connections. |
| connectionIdleTime | Integer | No | The idle time of a connection, in seconds. |

**Query the origin list**

**API description**

Query origins by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/source/listSources</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| sourceName | String | No | The name of the origin. Fuzzy search is supported. |
| sourceType | Integer | No | The filter condition for the origin type. |

**Query origin details**

**API description**

Query detailed information by origin ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/source/getSource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sourceId | String | Yes | The ID of the origin. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify origin**

**API description**

Modify an existing origin configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/source/modifySource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

Same as the parameters for creating an origin. You must also specify  `sourceId` .

**Delete origin**

**API description**

Delete the specified origin.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/source/deleteSource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sourceId | String | Yes | The ID of the origin. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Origin Management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class SourceApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create Nacos origin ==========
        String nacosSourceId = createNacosSource(client);

        // ========== Create EDAS namespace origin ==========
        // String edasSourceId = createEdasSource(client);

        // ========== Create Eureka origin ==========
        // String eurekaSourceId = createEurekaSource(client);

        // ========== Create Database origin ==========
        // String dbSourceId = createDatabaseSource(client);

        // ========== List origins ==========
        listSources(client);

        // ========== Get origin details ==========
        getSource(client, nacosSourceId);

        // ========== Modify origin ==========
        modifySource(client, nacosSourceId);

        // ========== Delete origin ==========
        deleteSource(client, nacosSourceId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create Nacos origin
     */
    private static String createNacosSource(IAcsClient client) throws Exception {
        // Nacos configuration structure
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");       // 【Requir
ed】Nacos registration center address
        sourceStruct.put("nacosNamespaceId", "public");                      // 【Require
d】Nacos namespace ID
        sourceStruct.put("nacosGroupName", "DEFAULT_GROUP");                 // 
【Optional】Nacos group name
        // sourceStruct.put("nacosAccessKey", "");                             // 【Optio
nal】Nacos authentication AccessKey
        // sourceStruct.put("nacosSecretKey", "");                             // 【Optio
nal】Nacos authentication SecretKey
        sourceStruct.put("checkType", 0);                                    // 
【Optional】Validation type: 0-no validation

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("sourceName", "my-nacos-source");                       // 【Required
】Origin name
        request.put("sourceType", 1);                                       // 【Required
】Origin type: 1-NACOS
        request.put("sourceStruct", sourceStruct);                          // 【Required
】Origin configuration structure
        request.put("description", "Nacos service registry");               // 
【Optional】Origin description

        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createNacosSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createNacosSource failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * Create EDAS namespace origin
     */
    private static String createEdasSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("edasNameSpaceId", "edas-ns-xxx");                  // 
【Required】EDAS namespace ID
        sourceStruct.put("type", 0);                                         // 
【Required】Type: 0-Nacos(DNCS), 1-ConfigServer(DNCS)
        sourceStruct.put("edasEndPoint", "edas-endpoint.aliyuncs.com");      // 【Condit
ionally required】EDAS Endpoint
        sourceStruct.put("edasServerAddr", "edas-server_addr");              // 
【Conditionally required】EDAS server address
        sourceStruct.put("edasAccessKey", "your-edas-ak");                   // 
【Required】EDAS AccessKey
        sourceStruct.put("edasSecretKey", "your-edas-sk");                   // 
【Required】EDAS SecretKey

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-edas-source");
        request.put("sourceType", 2);                                       // 【Required
】Origin type: 2-EDAS namespace
        request.put("sourceStruct", sourceStruct);

        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEdasSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEdasSource failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * Create Eureka origin
     */
    private static String createEurekaSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("eurekaRegistry", "http://eureka-server:8761/eureka/");  // 【R
equired】Eureka registration center address
        sourceStruct.put("checkType", 0);                                    // 
【Optional】Validation type

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-eureka-source");
        request.put("sourceType", 3);                                       // 【Required
】Origin type: 3-Eureka
        request.put("sourceStruct", sourceStruct);

        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEurekaSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEurekaSource failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Create Database origin
     */
    private static String createDatabaseSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("databaseType", 0);                                 // 【Require
d】Database type: 0-MySQL, 1-PostgreSQL
        sourceStruct.put("jdbcUrl", "jdbc:mysql://mysql-server:3306/mydb");  // 【Requir
ed】JDBC connection URL
        sourceStruct.put("username", "db_user");                             // 【Require
d】Database username
        sourceStruct.put("password", "db_password");                         // 【Require
d】Database password
        // sourceStruct.put("maxConnection", 100);                             // 【Optio
nal】Maximum connections
        // sourceStruct.put("maxIdleConnection", 20);                          // 【Optio
nal】Maximum idle connections
        // sourceStruct.put("connectionIdleTime", 300);                        // 【Optio
nal】Connection idle time (seconds)

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-database-source");
        request.put("sourceType", 5);                                       // 【Required
】Origin type: 5-Database
        request.put("sourceStruct", sourceStruct);

        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createDatabaseSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createDatabaseSource failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * List origins
     */
    private static void listSources(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of items per page
        // request.put("sourceName", "");                                     // 
【Optional】Origin name (fuzzy search)
        // request.put("sourceType", 1);                                      // 
【Optional】Origin type filter

        CommonRequest commonRequest = createBaseRequest("/source/listSources");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listSources: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get origin details
     */
    private static void getSource(IAcsClient client, String sourceId) throws Exception 
{
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/source/getSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getSource: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify origin
     */
    private static void modifySource(IAcsClient client, String sourceId) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");
        sourceStruct.put("nacosNamespaceId", "public");
        sourceStruct.put("checkType", 0);

        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("sourceName", "my-nacos-source-modified");              // 
【Required】Origin name
        request.put("sourceType", 1);                                       // 【Required
】Origin type
        request.put("sourceStruct", sourceStruct);                          // 【Required
】Origin configuration structure

        CommonRequest commonRequest = createBaseRequest("/source/modifySource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifySource: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete origin
     */
    private static void deleteSource(IAcsClient client, String sourceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/source/deleteSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteSource: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Origin type description (SCG)**

| sourceType | Type name | Description |
| --- | --- | --- |
| 1 | Nacos | The Nacos registration center. |
| 2 | EDAS namespace | The EDAS microservice namespace. |
| 3 | Eureka | The Eureka registration center. |
| 5 | Database | The database origin (MySQL/PostgreSQL). |

**Database type description**

| databaseType | Type name | Description |
| --- | --- | --- |
| 0 | MySQL | The MySQL database. |
| 1 | PostgreSQL | The PostgreSQL database. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-3"></a>

### 2.2.3. API call - Service management

**Overview**

The service management module provides features to create, delete, modify, and query backend services. A service is the target of route forwarding. It can be a static node, a discovered service, or an imported service.

**Applicable engine**: SCG / Higress (The API is engine-agnostic and works universally.)

**API path prefix**:  `/microservice/**`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header, and use a valid AccessKey pair.

**Create a service**

**API description**

Create a new backend service.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/createService</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateMicroserviceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the service (identifier in the gateway). |
| upstreamType | Integer | Yes | The upstream type:<br>• 1: Static node<br>• 2: Service discovery<br>• 3: Service import |
| loadBalanceType | Integer | Yes | The load balancing type (see description below). |
| protocol | String | Yes | The protocol:<br>• HTTP<br>• GRPC<br>• Webservice<br>• Dubbo<br>• HSF |
| serviceStruct | Object | Yes | The service structure configuration (see detailed description below). |
| serviceType | Integer | No | The service type:<br>• 0: RPC service<br>• 1: Database<br>Note<br>Default value is 0. |
| description | String | No | The description of the service. |
| serviceName | String | Conditional | The name of the service registered in the registration center.<br>Note<br>Use this parameter for service discovery. |
| serviceSourceType | Integer | Conditional | The source type.<br>Note<br>Use this parameter for service discovery. |
| isOpenHealthCheck | Boolean | No | Specifies whether to enable health check. |
| healthCheckStruct | HealthCheckStruct | No | The health check configuration (SCG). |
| activeHealthCheckStru ct | ActiveHealthCheckStru ct | No | The active health check configuration (Higress). |
| proxyServerName | String | No | The name of the proxy server. |
| isDisasterRecovery | Boolean | No | Specifies whether the service is for disaster recovery. Default value is false. |

**Load balancing type description (based on LoadBalanceTypeEnum)**

| Value | Type name | Description | Applicable scenario |
| --- | --- | --- | --- |
| 1 | WEIGHT_ROUND_ROBI N | Weighted round-robin. | Static nodes only |
| 2 | WEIGHT_RANDOM | Weighted random. | Static nodes only |
| 3 | ROUND_ROBIN | Round robin. | General-purpose |
| 4 | RANDOM | Random. | General-purpose |
| 5 | LEAST_REQUEST | Least requests. | Higress Nacos |
| 6 | CONSISTENT_HASH | Consistent hash. | Higress Nacos |
| 7 | LEAST_CONN | Least connections. | Higress Nacos |

**serviceStruct configuration description**

**Static node (upstreamType=1):**

```json
{
    "nodes": [
        {
            "ip": "192***.*.100",     // Required. The IP address of the node.
            "port": 8080,              // Required. The port.
            "weight": 100,             // Optional. The weight. Default value is 100.
            "enable": true             // Optional. Specifies whether to enable the node
. Default value is true.
        }
    ]
}
```

**Nacos service discovery (upstreamType=2):**

```json
{
    "nacosNamespaceId": "public",      // Required. The ID of the Nacos namespace.
    "nacosGroupName": "DEFAULT_GROUP"  // Optional. The name of the Nacos group.
}
```

**HealthCheckStruct structure (SCG health check)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | int | Yes | The type of the health check. |
| healthPath | String | Yes | The path for the health check. |
| httpStatuses | String | Yes | The HTTP status codes indicating health, such as "200, 301". |
| timeout | int | Yes | The request timeout in seconds. |
| healthInterval | int | Yes | The interval between health checks in seconds. |
| unHealthInterval | int | Yes | The interval between unhealthy checks in seconds. |
| httpSuccesses | int | Yes | The success threshold. |
| httpFailures | int | Yes | The failure threshold. |

**ActiveHealthCheckStruct structure (Higress active health check)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| enable | Boolean | Yes | Specifies whether to enable the feature. |
| protocol | String | Yes | The protocol. Valid values:<br>• http<br>• tcp |
| timeout | Integer | Yes | The timeout period in seconds. |
| interval | Integer | Yes | The interval between health checks in seconds. |
| healthyThreshold | Integer | Yes | The healthy threshold. |
| unhealthyThreshold | Integer | Yes | The unhealthy threshold. |
| httpPath | String | Conditional | The HTTP health check path.<br>Note<br>Configure this parameter when <code>protocol=http</code><code> </code>. |
| httpHost | String | No | The host for the HTTP health check. |
| expectedStatuses | List | Conditional | The expected status codes, such as \["200", "301"\]. |

![](assets/d4f416b1676e9ca966e90c82f71bfa86.png)

**Query the list of services**

**API description**

Query the list of services by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/listServices</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GatewayServiceListByPageRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| serviceName | String | No | The service name.Fuzzy search is supported. |
| serviceId | String | No | The service ID. Exact match is required. |
| sourceName | String | No | The name of the source. |
| isDisasterRecovery | Boolean | No | Specifies whether to filter disaster recovery services. |
| sourceTypeList | List | No | The list of source types. |
| provider | String | No | The provider of the AI gateway. |

**Query service details**

**API description**

Query the detailed information of a service by its service ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/getService</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a service**

**API description**

Modify an existing service configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/modifyService</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

The parameters are the same as those for creating a service. You must also specify  `serviceId` .

**Modify service nodes**

**API description**

Modify the node configuration of a service individually.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/modifyNode</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpdateNodeRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| nodes | List | Yes | The list of nodes. |

**Delete a service**

**API description**

Delete a specified service.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/deleteService</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Delete services in batches**

**API description**

Delete multiple services in batches.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/batchDeleteService</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| serviceIds | List | Yes | The list of service IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**List all services**

**API description**

List all services under the gateway instance (without pagination).

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/microservice/listAllServices</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| serviceType | Integer | No | The filter for service type. |

**Common Request call examples**

The following examples show how to call the service management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ServiceApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-managed ACK console address

    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create fixed-node service ==========
        String serviceId = createFixedNodeService(client);

        // ========== Create Nacos service discovery service ==========
        // String nacosServiceId = createNacosService(client);

        // ========== List services ==========
        listServices(client);

        // ========== Get service details ==========
        getService(client, serviceId);

        // ========== Modify service ==========
        modifyService(client, serviceId);

        // ========== Delete service ==========
        deleteService(client, serviceId);
    }

    /**
     * Create client (common for self-managed ACK and Enterprise Edition)
     */
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create fixed-node service
     */
    private static String createFixedNodeService(IAcsClient client) throws Exception {
        // Node configuration (based on Node structure)
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.100");                                    // [Required]
Node IP address
        node.put("port", 8080);                                             // [Required]
Port
        node.put("weight", 100);                                            // [Optional]
Weight, default is 100
        node.put("enable", true);                                           // [Optional]
Whether enabled, default is true

        // Service structure configuration
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));

        // Create request (based on CreateMicroserviceRequest)
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "service-demo-01");                             // [Required]
Service name (identifier in gateway)
        request.put("upstreamType", 1);                                     // [Required]
Upstream type: 1 - fixed node
        request.put("loadBalanceType", 3);                                  // [Required]
Load balancing type: 3 - round robin
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceStruct", serviceStruct);                        // 
[Required] Service structure configuration
        request.put("serviceType", 0);                                      // [Optional]
Service type: 0 - RPC service
        request.put("description", "demo backend service");                 // 
[Optional] Service description
        request.put("isOpenHealthCheck", false);                            // [Optional]
Whether health check is enabled

        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createFixedNodeService success, serviceId: " + 
serviceId);
            return serviceId;
        } else {
            System.out.println("createFixedNodeService failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Create Nacos service discovery service
     */
    private static String createNacosService(IAcsClient client) throws Exception {
        // Nacos service structure configuration
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nacosNamespaceId", "public");                    // 
[Required] Nacos namespace ID
        serviceStruct.put("nacosGroupName", "DEFAULT_GROUP");               // [Optional
] Nacos group name

        // Create request
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "service-nacos-demo");                          // 
[Required] Service name
        request.put("upstreamType", 2);                                     // [Required]
Upstream type: 2 - service discovery
        request.put("loadBalanceType", 3);                                  // [Required]
Load balancing type
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceName", "user-service");                         // 
[Required] Service name in registry
        request.put("serviceSourceType", 1);                                // [Required]
Source type: 1 - NACOS
        request.put("sourceId", "nacos-source-id");                         // 
[Required] Source ID
        request.put("serviceStruct", serviceStruct);                        // 
[Required] Service structure configuration

        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createNacosService success, serviceId: " + serviceId);
            return serviceId;
        } else {
            System.out.println("createNacosService failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Create service with health check
     */
    private static String createServiceWithHealthCheck(IAcsClient client) throws Exception {
        // Node configuration
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.168.1.100");
        node.put("port", 8080);
        node.put("weight", 100);
        node.put("enable", true);

        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));

        // SCG health check configuration (based on HealthCheckStruct)
        Map<String, Object> healthCheckStruct = new HashMap<>();
        healthCheckStruct.put("type", 0);                                   // [Required]
Check type
        healthCheckStruct.put("healthPath", "/health");                     // 
[Required] Check path
        healthCheckStruct.put("httpStatuses", "200,301");                   // 
[Required] Healthy status codes
        healthCheckStruct.put("timeout", 5);                                // [Required]
Request timeout (seconds)
        healthCheckStruct.put("healthInterval", 30);                        // 
[Required] Health check interval (seconds)
        healthCheckStruct.put("unHealthInterval", 60);                      // 
[Required] Unhealthy check interval (seconds)
        healthCheckStruct.put("httpSuccesses", 3);                          // 
[Required] Success threshold
        healthCheckStruct.put("httpFailures", 3);                           // 
[Required] Failure threshold

        // Higress active health check configuration (based on ActiveHealthCheckStruct)
        // Map<String, Object> activeHealthCheckStruct = new HashMap<>();
        // activeHealthCheckStruct.put("enable", true);                       // 
[Required] Whether enabled
        // activeHealthCheckStruct.put("protocol", "http");                   // [Requir
ed] Protocol
        // activeHealthCheckStruct.put("timeout", 5);                         // 
[Required] Timeout (seconds)
        // activeHealthCheckStruct.put("interval", 30);                       // 
[Required] Check interval (seconds)
        // activeHealthCheckStruct.put("healthyThreshold", 3);                // [Requir
ed] Healthy threshold
        // activeHealthCheckStruct.put("unhealthyThreshold", 3);              // [Requir
ed] Unhealthy threshold
        // activeHealthCheckStruct.put("httpPath", "/health");                // [Requir
ed] HTTP check path
        // activeHealthCheckStruct.put("expectedStatuses", Arrays.asList("200", 
"301"));  // [Required] Expected status codes

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("name", "service-health-check");
        request.put("upstreamType", 1);
        request.put("loadBalanceType", 3);
        request.put("protocol", "HTTP");
        request.put("serviceStruct", serviceStruct);
        request.put("isOpenHealthCheck", true);                             // [Required]
Enable health check
        request.put("healthCheckStruct", healthCheckStruct);                // [Required
] Health check configuration

        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createServiceWithHealthCheck success, serviceId: " + 
serviceId);
            return serviceId;
        } else {
            System.out.println("createServiceWithHealthCheck failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * List services (based on GatewayServiceListByPageRequest)
     */
    private static void listServices(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("serviceName", "");                                    // [Optiona
l] Service name (fuzzy search)
        // request.put("serviceId", "");                                      // [Optiona
l] Service ID (exact search)
        // request.put("isDisasterRecovery", false);                          // 
[Optional] Filter by whether it is a disaster recovery service

        CommonRequest commonRequest = createBaseRequest("/microservice/listServices");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listServices: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get service details
     */
    private static void getService(IAcsClient client, String serviceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
Service ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/microservice/getService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getService: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify service
     */
    private static void modifyService(IAcsClient client, String serviceId) throws Exception {
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.101");
        node.put("port", 8081);
        node.put("weight", 100);
        node.put("enable", true);

        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));

        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
ID of the service to modify
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "service-demo-modified");                       // 
[Required] Service name
        request.put("upstreamType", 1);                                     // [Required]
Upstream type
        request.put("loadBalanceType", 1);                                  // [Required]
Load balancing type
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceStruct", serviceStruct);                        // 
[Required] Service structure configuration

        CommonRequest commonRequest = createBaseRequest("/microservice/modifyService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyService: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete service
     */
    private static void deleteService(IAcsClient client, String serviceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
Service ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/microservice/deleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteService: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Batch delete services
     */
    private static void batchDeleteServices(IAcsClient client, List<String> serviceIds) 
throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceIds", serviceIds);                              // [Required]
List of service IDs
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required]GatewayinstanceID

        CommonRequest commonRequest = 
createBaseRequest("/microservice/batchDeleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteService: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Upstream type description**

| upstreamType | Description | Configuration method |
| --- | --- | --- |
| 1 | Static node | Configure the IP address, port, and weight in <code> serviceStruct.nodes </code>. |
| 2 | Service discovery | Specify the service name in the registration center by using <code> serviceName </code>. You must configure <code> sourceId </code>. |
| 3 | Service import | Import a service from an existing source. |

**Protocol type description**

| protocol | Description |
| --- | --- |
| HTTP | The HTTP or HTTPS protocol. |
| GRPC | The gRPC protocol. |
| Webservice | The WebService protocol. |
| Dubbo | The Dubbo RPC protocol. |
| HSF | The HSF RPC protocol. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-4"></a>

### 2.2.4. API call - Instance management

**Overview**

The instance management module manages gateway instances. An instance is a running entity of the gateway. You can deploy it on a Kubernetes cluster. The instance supports two engine types: SCG and Higress.

- **Applicable engines**: SCG / Higress

- **API path prefix**:  `/gatewayInstance`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header. Use a valid AccessKey pair.

**Create an instance**

**API description**

Create a new gateway instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/createInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateGwInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceName | String | Yes | The instance name. It must be 2 to 128 characters in length and start with a letter. |
| clusterCode | String | Yes | The cluster code. |
| namespace | String | Yes | The Kubernetes namespace. |
| brokerEngineType | String | No | The engine type:<br>• SCG<br>• HIGRESS<br>• SHARED_SCG<br>• CLOUD_NATIVE_GAT EWAY |
| deployMode | String | No | The deployment mode: adp, edas, tiangong, custom, k8s, and so on. |
| instanceClass | String | No | The instance specification. |
| instanceNumber | String | No | The number of instance nodes. |
| vpcId | String | No | The VPC ID. |
| vswId | String | No | The vSwitch ID. |
| ingressName | String | No | The Ingress name. |
| deployConfigContent | String | No | The custom deployment configuration. |
| accessModeConfigCon tent | String | No | The access mode configuration. |

**Query the list of instances API description**

Query gateway instances by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/listInstances</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListGwInstancesRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| current | Integer | Yes | The page number.Start from 1. |
| size | Integer | Yes | The number of entries per page. |
| name | String | No | The instance name for fuzzy search. |
| gwInstanceId | String | No | Filter by instance ID. |
| deployMode | String | No | Filter by deployment mode. |
| status | Integer | No | Filter by instance status. |
| brokerEngineType | String | No | Filter by engine type. |

**List all instances**

**API description**

List all gateway instances without pagination.

**Request information**

| Item | Value |
| --- | --- |
| URL | <code>/gatewayInstance/listAllInstances</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

No request parameters are required.

**Query instance details**

**API description**

Query detailed information by instance ID.

**Request information**

| Item | Value |
| --- | --- |
| URL | <code>/gatewayInstance/getInstanceInfo</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetInstanceInfoRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Modify an instance**

**API description**

Modify the name of the instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/modifyInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ModifyInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |
| instanceName | String | Yes | The new name of the instance. |

**Delete an instance**

**API description**

Delete the specified gateway instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/deleteInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on DeleteGwInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Restart an instance**

**API description**

Restart the specified gateway instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/restartInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RestartGwInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Stop instance**

**API description**

Stop the specified gateway instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/stopInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on StopInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Upgrade instance**

**API description**

Upgrade the instance to the latest version.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/upgradeInstance</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpgradeGwInstanceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Modify instance resources**

**API description**

Scale the instance up or down by modifying its specification and node count.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/modifyResource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ModifyInstanceResourceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |
| instanceClass | String | No | The specification of the instance. |
| instanceNumber | Integer | No | The number of instance nodes. |
| specificationTemplate | Integer | No | The specification template. |

**Query instance resources**

**API description**

Query the specification and node information of an instance.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/gatewayInstance/getResource</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetInstanceResourceRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the instance. |

**Common request call examples**

The following examples show how to call the instance management API by using Common Request. The only difference between a self-managed ACK environment and an Enterprise Edition environment lies in the authentication settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class InstanceApiDemo {

    // ========== Environment configuration (modify according to the actual 
environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create an instance ==========
        String instanceId = createInstance(client);

        // ========== Query the instance list ==========
        listInstances(client);

        // ========== Query instance details ==========
        getInstanceInfo(client, instanceId);

        // ========== Modify the instance name ==========
        modifyInstance(client, instanceId);

        // ========== Query instance resources ==========
        getResource(client, instanceId);

        // ========== Delete the instance ==========
        // deleteInstance(client, instanceId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create an instance (based on CreateGwInstanceRequest)
     */
    private static String createInstance(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceName", "my-gateway-instance");            // 
【Required】Instance name
        request.put("clusterCode", "cluster-code-xxx");                  // 【Required】C
luster code
        request.put("namespace", "default");                             // 
【Required】Kubernetes namespace
        request.put("brokerEngineType", "SCG");                          // 
【Optional】Engine type: SCG/HIGRESS
        // request.put("deployMode", "adp");                                // 【Optional
】Deployment mode
        // request.put("instanceClass", "standard");                        // 【Optional
】Instance specification
        // request.put("instanceNumber", "2");                              // 【Optional
】Number of nodes

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/createInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String instanceId = result.getString("data");
            System.out.println("createInstance success, instanceId: " + instanceId);
            return instanceId;
        } else {
            System.out.println("createInstance failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * Query the instance list (based on ListGwInstancesRequest)
     */
    private static void listInstances(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
```

`request.put("current", 1);                                       //` 【`Required`】`Cu`

```text
rrent page number
```

`request.put("size", 10);                                         //` 【`Required`】`Nu`

```java
mber of entries per page
        // request.put("name", "");                                         // 【Optional
】Instance name (fuzzy search)
        // request.put("brokerEngineType", "SCG");                          // 【Optional
】Engine type filter
        // request.put("status", 2);                                        // 【Optional
】Status filter: 2-running

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/listInstances");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listInstances: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query instance details (based on GetInstanceInfoRequest)
     */
    private static void getInstanceInfo(IAcsClient client, String gwInstanceId) throws 
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/getInstanceInfo");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getInstanceInfo: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify the instance name (based on ModifyInstanceRequest)
     */
    private static void modifyInstance(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        request.put("instanceName", "modified-instance-name");           // 
【Required】New instance name

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/modifyInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyInstance: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query instance resources (based on GetInstanceResourceRequest)
     */
    private static void getResource(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/getResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getResource: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify instance resources (based on ModifyInstanceResourceRequest)
     */
    private static void modifyResource(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        request.put("instanceClass", "large");                           // 
【Optional】Instance specification
        request.put("instanceNumber", 3);                                // 
【Optional】Number of nodes

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/modifyResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyResource: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Restart the instance (based on RestartGwInstanceRequest)
     */
    private static void restartInstance(IAcsClient client, String gwInstanceId) throws 
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/restartInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("restartInstance: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Stop the instance (based on StopInstanceRequest)
     */
    private static void stopInstance(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/stopInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("stopInstance: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete the instance (based on DeleteGwInstanceRequest)
     */
    private static void deleteInstance(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID

        CommonRequest commonRequest = 
createBaseRequest("/gatewayInstance/deleteInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteInstance: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Instance status description**

| status | Status name | Description |
| --- | --- | --- |
| 0 | starting | The instance is starting. |
| 1 | error | The instance is in an error state. |
| 2 | running | The instance is running. |
| 3 | unknown | The status is unknown. |
| 4 | stopped | The instance has stopped. |
| 5 | wait_deploy | The system is waiting for deployment. |
| 6 | updating | The system is updating (upgrading or scaling). |
| 7 | stopping | The instance is stopping. |

**Engine type description**

| brokerEngineType | Description |
| --- | --- |
| SCG | Spring Cloud Gateway (API gateway). |
| HIGRESS | Higress (AI gateway). |
| SHARED_SCG | Shared Spring Cloud Gateway. |
| CLOUD_NATIVE_GATEWAY | Cloud-native gateway. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-5"></a>

### 2.2.5. API call - Group management

**Overview**

The group management module lets you create, delete, modify, and query route groups. Groups logically classify routes. You can configure a base path and a default domain name for each group.

**Applicable engines**: SCG / Higress (The API is engine-agnostic and works universally.)

**API path prefix**:  `/group`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header. Use a valid AccessKey pair.

**Create a group**

**API description**

Create a new route group.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/createGroup</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateGroupRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the group. |
| basePath | String | Yes | The base path of the group, such as<code> /api/v1 </code>. |
| groupId | String | No | The ID of the group.This parameter is optional and the system generates it automatically. |
| description | String | No | The description of the group. |
| needDefaultDomain | boolean | No | Specifies whether to use the default domain name. Default value: false. |
| defaultDomainForRout e | Boolean | No | Specifies whether to generate a default domain name for routes. Default value: false. |
| domainIds | List | No | The list of associated domain IDs. |
| isDisasterRecovery | Boolean | No | Specifies whether the group is for disaster recovery. Default value: false. |

**List groups**

**API description**

Query the list of route groups by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/listGroups</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListGroupsRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| groupId | String | No | Filter by group ID. |
| groupIdList | List | No | Filter by a list of group IDs. |
| name | String | No | Perform fuzzy search by group name. |
| defaultDomainIsNull | Boolean | No | Filter by whether the default domain name is empty. |
| editable | Boolean | No | Filter by whether the group is editable. |
| isDisasterRecovery | Boolean | No | Filter by whether the group is for disaster recovery. |

**Query group details API description**

Query detailed information by group ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/getGroup</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetGroupRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |

**Modify a group**

**API description**

Modify the configuration of an existing group.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/modifyGroup</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ModifyGroupRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |
| name | String | No | The name of the group. |
| basePath | String | No | The base path of the group. |
| description | String | No | The description of the group. |
| domainIds | List | No | The list of associated domain IDs. |
| defaultDomainForRout e | Boolean | No | Specifies whether to generate a default domain name for the route. |

**Delete a group**

**API description**

Delete the specified group.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/deleteGroup</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |

**Add a domain name for a group**

**API description**

Add an associated domain name for a group.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/addGroupDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on AddGroupDomainRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |
| domainIds | List | Yes | The list of domain IDs to add. |

**Delete group domain**

**API description**

Delete the domain name associated with the group.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/deleteGroupDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on DeleteGroupDomainRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |
| domainId | String | Yes | The ID of the domain name to delete. |

**Query all groups**

**API description**

Query all groups under the gateway instance without pagination.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/group/getAllGroups</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common request call example**

The following example shows how to call the group management API by using the common request method. The difference between a self-managed ACK environment and an enterprise edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create group ==========
        String groupId = createGroup(client);

        // ========== List groups ==========
        listGroups(client);

        // ========== Get group details ==========
        getGroup(client, groupId);

        // ========== Modify group ==========
        modifyGroup(client, groupId);

        // ========== Add group domain ==========
        addGroupDomain(client, groupId, Arrays.asList("domain-id-xxx"));

        // ========== Delete group domain ==========
        deleteGroupDomain(client, groupId, "domain-id-xxx");

        // ========== Delete group ==========
        deleteGroup(client, groupId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create group (based on CreateGroupRequest)
     */
    private static String createGroup(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("name", "api-group-demo");                              // 【Required
】Group name
        request.put("basePath", "/api/v1");                                 // 【Required
】Group base path
        request.put("description", "API demo group");                       // 
【Optional】Group description
        // request.put("groupId", "");                                         // 
【Optional】Group ID (system-generated)
        // request.put("needDefaultDomain", false);                            // 【Optio
nal】Whether to require a default domain
        // request.put("defaultDomainForRoute", false);                        // 【Optio
nal】Whether to generate a default domain for routing
        // request.put("domainIds", Arrays.asList("domain-id-xxx"));           // 【Opti
onal】List of associated domain IDs
        // request.put("isDisasterRecovery", false);                           // 【Optio
nal】Whether this is a disaster recovery group

        CommonRequest commonRequest = createBaseRequest("/group/createGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String groupId = result.getString("data");
            System.out.println("createGroup success, groupId: " + groupId);
            return groupId;
        } else {
            System.out.println("createGroup failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * List groups (based on ListGroupsRequest)
     */
    private static void listGroups(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page
```

`// request.put("name", "");                                            //` 【`Option`

```java
al】Group name (fuzzy search)
        // request.put("editable", true);                                      // 
【Optional】Filter by editable status
        // request.put("isDisasterRecovery", false);                           // 【Optio
nal】Filter by disaster recovery status

        CommonRequest commonRequest = createBaseRequest("/group/listGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listGroups: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get group details (based on GetGroupRequest)
     */
    private static void getGroup(IAcsClient client, String groupId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID

        CommonRequest commonRequest = createBaseRequest("/group/getGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getGroup: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify group (based on ModifyGroupRequest)
     */
    private static void modifyGroup(IAcsClient client, String groupId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("name", "api-group-modified");                          // 【Optional
】Group name
        request.put("basePath", "/api/v2");                                 // 【Optional
】Group base path
        request.put("description", "Modified group description");           // 【Optiona
l】Group description

        CommonRequest commonRequest = createBaseRequest("/group/modifyGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyGroup: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Add group domain (based on AddGroupDomainRequest)
     */
    private static void addGroupDomain(IAcsClient client, String groupId, List<String> domainIds) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("domainIds", domainIds);                                // 【Required
】List of domain IDs to add

        CommonRequest commonRequest = createBaseRequest("/group/addGroupDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("addGroupDomain: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete group domain (based on DeleteGroupDomainRequest)
     */
    private static void deleteGroupDomain(IAcsClient client, String groupId, String domainId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("domainId", domainId);                                  // 【Required
】Domain ID to delete

        CommonRequest commonRequest = createBaseRequest("/group/deleteGroupDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteGroupDomain: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete group
     */
    private static void deleteGroup(IAcsClient client, String groupId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID

        CommonRequest commonRequest = createBaseRequest("/group/deleteGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteGroup: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get all groups
     */
    private static void getAllGroups(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/group/getAllGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getAllGroups: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Group attribute description**

| Attribute | Description |
| --- | --- |
| groupId | The unique identifier of the group. |
| name | The name of the group. |
| basePath | The base path of the group. All routes under this group inherit this path prefix. |
| description | The description of the group. |
| defaultDomain | The default domain name of the group. |
| editable | Whether the group is editable:<br>• true: The group is editable.<br>• false: The group is not editable (such as the DEFAULT group). |
| isDisasterRecovery | Whether the group is a disaster recovery group. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-6"></a>

### 2.2.6. API call - Route management

**Overview**

The route management module provides functions to create, delete, modify, and query routes. A route defines how a request forwards from the gateway to the backend service.

**Applicable engine**: SCG / Higress (the API is engine-agnostic and universally applicable)

**API path prefix**:  `/route`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header, and use a valid AccessKey pair.

**Validate parameters before creating a route**

**API description**

Validate parameters before you create a route. The system checks whether the route name is duplicate.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/checkCreateRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Create a route**

**API description**

Create a new routing rule.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/createRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RouteCreateRequest + AbstractRouteRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeName | String | Yes | The name of the route.This is a unique identifier. |
| groupId | String | Yes | The ID of the group.The default group is "DEFAULT". |
| routePath | List | Yes | The list of paths.Supports Ant-style wildcards. |
| serviceType | String | Yes | The type of service:<br>• SINGLE: Single service<br>• WEIGHTED: Weighted |
| serviceId | String | Conditional | The ID of the backend service.<br>Note<br>This parameter is required in single-service mode. |
| serviceIds | List | Conditional | The list of services and their weights.<br>Note<br>This parameter is required in weighted mode. |
| path | RoutePath | No | The new path matching configuration. It has higher priority than <code> routePath </code>. |
| order | int | No | The priority of the route. A smaller number indicates a higher priority. The default value is 0. |
| enableStatus | Boolean | No | The enabled status.The default value is true. |
| openStripPrefix | boolean | No | Specifies whether to enable path prefix stripping. The default value is false. |
| stripPrefix | int | No | The number of prefix layers to strip. Use this parameter together with openStripPrefix. |
| methods | List | No | The HTTP methods that are allowed, such as <code> ["GET","POST"] </code>. |
| header | List | No | The list of header matching conditions. |
| cookie | List | No | The list of cookie matching conditions. |
| queryParam | List | No | The list of query parameter matching conditions. |
| domainIds | List | No | The list of associated domain IDs. |
| requestTimeout | Integer | No | The request timeout period, in milliseconds. |
| isDisasterRecovery | Boolean | No | Specifies whether the route is for disaster recovery. |
| disasterRecoveryServi ceId | String | No | The ID of the disaster recovery service. |
| disasterRecoveryServi ceIds | List | No | The list of disaster recovery service IDs and their weights. |
| hsfMethodMappingCon fig | HsfMethodMappingCon fig | No | The HSF method mapping configuration. This applies only to HSF protocol configurations. |

**RoutePath structure**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| matchType | String | Yes | The match type:<br>• PRE: Prefix<br>• EXACT: Exact<br>• REGEX: Regex |
| matchValue | String | No | The match value. |
| caseSensitive | Boolean | No | Specifies whether the match is case-sensitive. |

**KvPair structure**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| key | String | Yes | The key name. |
| value | String | Yes | The key value. |

**ServiceAndWeight structure**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| serviceId | String | Yes | The ID of the service. |
| weight | Integer | Yes | The weight. Valid values: 0 to 100. |

**List routes**

**API description**

Query routes by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/listRoutes</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RouteListRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| routeName | String | No | The name of the route.Fuzzy search is supported. |
| serviceName | String | No | The name of the service. Fuzzy search is supported. |
| exactServiceId | String | No | The ID of the service.Exact match is supported. |
| enableStatus | Boolean | No | The filter for the enabled status. |
| routeId | String | No | The ID of the route. |
| groupName | String | No | The name of the group. |
| domainName | String | No | The domain name. |
| routePath | String | No | The path of the route.Fuzzy search is supported. |
| isDisasterRecovery | Boolean | No | Indicates whether the route is for disaster recovery. |

**Query route details**

**API description**

Query the detailed information of a route by its ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/getRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a route**

**API description**

Modify an existing route configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/modifyRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

The request parameters are the same as those for creating a route. You must also specify  `routeId` .

**Delete a route**

**API description**

Delete the specified route.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/deleteRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify the enabled status of a route**

**API description**

Enable or disable a route.

> **Note**
>
> This API applies only to the SCG engine. The Higress engine does not support this API.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/changeRouteStatus</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| enableStatus | Boolean | Yes | • true: Enable the route.<br>• false: Disable the route. |

**Delete routes in batches**

**API description**

Delete multiple routes in batches.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/batchDeleteRoute</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| routeIds | List | Yes | The list of route IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common request call examples**

The following examples show how to call the route management API by using the common request method. The difference between a self-managed ACK environment and an enterprise edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RouteApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-managed ACK console address

    // Enterprise edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    // Gateway instance ID and backend service ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String SERVICE_ID = "your-service-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Validate before creating route ==========
        checkCreateRoute(client);

        // ========== Create route ==========
        String routeId = createRoute(client);

        // ========== List routes ==========
        listRoutes(client);

        // ========== Get route details ==========
        getRoute(client, routeId);

        // ========== Modify route ==========
        modifyRoute(client, routeId);

        // ========== Change route status ==========
        changeRouteStatus(client, routeId, false);

        // ========== Delete route ==========
        deleteRoute(client, routeId);
    }

    /**
     * Create client (common for self-managed ACK and enterprise edition)
     */
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Validate before creating route
     */
    private static void checkCreateRoute(IAcsClient client) throws Exception {
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/checkCreateRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("checkCreateRoute: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Create route
     */
    private static String createRoute(IAcsClient client) throws Exception {
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/createRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonRequest(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String routeId = result.getString("data");
            System.out.println("createRoute success, routeId: " + routeId);
            return routeId;
        } else {
            System.out.println("createRoute failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * Build route request parameters
     */
    private static Map<String, Object> buildRouteRequest() {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("routeName", "route-demo-01");                          // 
[Required] Route name
        request.put("groupId", "DEFAULT");                                  // [Required]
Group ID
        request.put("routePath", Arrays.asList("/api-demo/**"));            // [Required
] Path list
        request.put("serviceType", "SINGLE");                               // [Required]
Service type: SINGLE/WEIGHTED
        request.put("serviceId", SERVICE_ID);                               // [Required]
Backend service ID (SINGLE mode)
        request.put("enableStatus", true);                                  // [Optional]
Enable status
        request.put("order", 100);                                          // [Optional]
Route priority
        // request.put("openStripPrefix", false);                             // [Optiona
l] Whether to enable path prefix stripping
        // request.put("stripPrefix", 1);                                     // [Optiona
l] Number of prefix levels to strip
        // request.put("methods", Arrays.asList("GET", "POST"));              // [Option
al] HTTP method restriction
        // request.put("domainIds", new ArrayList<>());                        // 
[Optional] Associated domain ID list

        // New path matching configuration (takes precedence over routePath)
        // Map<String, Object> path = new HashMap<>();
        // path.put("matchType", "PRE");                                      // PRE/EXAC
T/REGEX
        // path.put("matchValue", "");                                        // Match va
lue
        // path.put("caseSensitive", false);                                  // Whether 
case-sensitive
        // request.put("path", path);

        // Weighted mode service list (WEIGHTED mode)
        // List<Map<String, Object>> serviceIds = new ArrayList<>();
        // Map<String, Object> service1 = new HashMap<>();
        // service1.put("serviceId", "service-id-1");
        // service1.put("weight", 80);
        // Map<String, Object> service2 = new HashMap<>();
        // service2.put("serviceId", "service-id-2");
        // service2.put("weight", 20);
        // serviceIds.add(service1);
        // serviceIds.add(service2);
        // request.put("serviceIds", serviceIds);

        // Header match conditions
        // List<Map<String, Object>> header = new ArrayList<>();
        // Map<String, Object> headerCondition = new HashMap<>();
        // headerCondition.put("key", "X-Version");
        // headerCondition.put("value", "v1");
        // header.add(headerCondition);
        // request.put("header", header);

        // Cookie match conditions
        // List<Map<String, Object>> cookie = new ArrayList<>();
        // Map<String, Object> cookieCondition = new HashMap<>();
        // cookieCondition.put("key", "sessionId");
        // cookieCondition.put("value", "session-*");
        // cookie.add(cookieCondition);
        // request.put("cookie", cookie);

        // Query parameter match conditions
        // List<Map<String, Object>> queryParam = new ArrayList<>();
        // Map<String, Object> queryCondition = new HashMap<>();
        // queryCondition.put("key", "version");
        // queryCondition.put("value", "1.0");
        // queryParam.add(queryCondition);
        // request.put("queryParam", queryParam);

        // Disaster recovery route configuration
        // request.put("isDisasterRecovery", true);                           // 
[Optional] Whether it is a disaster recovery route
        // request.put("disasterRecoveryServiceId", "disaster-service-id");   // 
[Optional] Disaster recovery service ID

        return request;
    }

    /**
     * List routes
     */
    private static void listRoutes(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("routeName", "");                                      // [Optiona
l] Route name (fuzzy search)
        // request.put("serviceName", "");                                    // [Optiona
l] Service name (fuzzy search)
        // request.put("enableStatus", true);                                 // [Optiona
l] Enable status filter

        CommonRequest commonRequest = createBaseRequest("/route/listRoutes");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listRoutes: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get route details
     */
    private static void getRoute(IAcsClient client, String routeId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/route/getRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getRoute: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify route
     */
    private static void modifyRoute(IAcsClient client, String routeId) throws Exception
{
        Map<String, Object> request = buildRouteRequest();
        request.put("routeId", routeId);                                    // [Required]
Route ID to modify
        request.put("routeName", "route-demo-01-modified");                 // 
[Optional] Modify route name
        request.put("order", 200);                                          // [Optional]
Modify priority

        CommonRequest commonRequest = createBaseRequest("/route/modifyRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoute: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Change route status
     */
    private static void changeRouteStatus(IAcsClient client, String routeId, boolean enableStatus) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("enableStatus", enableStatus);                          // 
[Required] Enable status

        CommonRequest commonRequest = createBaseRequest("/route/changeRouteStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("changeRouteStatus: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete route
     */
    private static void deleteRoute(IAcsClient client, String routeId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/route/deleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteRoute: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Batch delete routes
     */
    private static void batchDeleteRoutes(IAcsClient client, List<String> routeIds) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeIds", routeIds);                                  // [Required]
Route ID list
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/route/batchDeleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteRoute: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Path matching type description**

| matchType | Description | Example |
| --- | --- | --- |
| PRE | Prefix match. | <code> /api/** </code> matches all paths that start with <code> /api/ </code>. |
| EXACT | Exact match. | <code> /api/user </code> matches only<code> /api/user </code>. |
| REGEX | Regex match. | Use a regular expression to match the path. |

**Service type description**

| serviceType | Description | Usage |
| --- | --- | --- |
| SINGLE | Single service | Use <code> serviceId </code> to specify one backend service. |
| WEIGHTED | Weighted service | Use <code> serviceIds </code> to specify multiple services and their weights. |

**Response code descriptions**

| code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | The parameter is invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-7"></a>

### 2.2.7. API call - Policy configuration management

**Overview**

The policy configuration management module manages policies. You can create, delete, modify, and query policies. A policy configures behaviors for routes, services, and consumers, such as throttling, circuit breaking, retry, and CORS.

**Applicable engine**: SCG / Higress (The API is engine-agnostic and works universally.)

**API path prefix**:  `/strategyConfig/**`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header and use a valid AccessKey pair.

**Create a policy configuration**

**API description**

Create a new policy configuration. The structure of the  `config`  field varies by policy type. For more information, see the policy configuration examples below.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/createStrategyConfig</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| strategyName | String | Yes | The English name of the policy type. |
| strategyConfigName | String | No | The name of the policy configuration. |
| config | Object | No | The policy configuration parameters in map format. |
| rawConfig | String | No | The policy configuration parameters in YAML format. |
| routeIds | List | No | The list of associated route IDs. |
| serviceIds | List | No | The list of associated service IDs. |
| appIds | List | No | The list of associated consumer IDs. |
| domainIds | List | No | The list of associated domain IDs. |

**Query the list of policy configurations**

**API description**

Query the list of policy configurations by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/listStrategyConfigs</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| strategyName | String | No | The name of the policy type used for filtering. |
| routeId | String | No | The ID of the associated route used for filtering. |
| serviceId | String | No | The ID of the associated service used for filtering. |
| appId | String | No | The ID of the associated consumer used for filtering. |

**Query policy configuration details**

**API description**

Query detailed information by policy configuration ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/getStrategyConfig</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify policy configuration**

**API call description**

Modify an existing policy configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/modifyStrategyConfig</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

Use the same parameters as those for creating a policy configuration. Additionally, specify  `strategyConfigId` .

**Modify policy configuration status**

**API call description**

Enable or disable a policy configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/modifyStrategyConfigStatus</code> |
| Method | POST |
| Content-Type | application/json |

![](assets/93efe767e68f15e59fd733d2f822f274.png)

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| isOpen | Boolean | Yes | • true: Enable the policy<br>• false: Disable the policy |

**Delete a policy configuration**

**API description**

Delete a specified policy configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/strategyConfig/deleteStrategyConfig</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the policy configuration management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StrategyConfigApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-managed ACK console address

    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";  // Enterprise Edition Endpoint
    private static final String ACCESS_KEY_ID = "your-access-key-id";                // 
AccessKey ID
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";        //
AccessKey Secret
    private static final String ORGANIZATION_ID = "your-org-id";                     // 
Enterprise organization ID

    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        // Initialize client
        IAcsClient client = createClient();

        // ========== Example: Create different types of policy configurations 
==========

        // 1. Flow control policy
        String flowControlStrategyId = createFlowControlStrategy(client);

        // 2. Timeout policy
        String timeoutStrategyId = createTimeoutStrategy(client);

        // 3. Circuit breaker policy
        String circuitBreakerStrategyId = createCircuitBreakerStrategy(client);

        // 4. Cross-domain policy
        String corsStrategyId = createCorsStrategy(client);

        // 5. Caching policy
        String cacheStrategyId = createCacheStrategy(client);

        // 6. IP allowlist and blocklist policy
        String ipBlockStrategyId = createIpBlockStrategy(client);

        // 7. ACL permission control policy
        String aclStrategyId = createAclStrategy(client);

        // 8. Mock policy
        String mockStrategyId = createMockStrategy(client);

        // 9. Request tracing policy
        String tracingStrategyId = createTracingStrategy(client);

        // 10. Request body size limit policy
        String requestSizeStrategyId = createRequestSizeStrategy(client);

        // ========== Query policy configuration list ==========
        listStrategyConfigs(client);

        // ========== Query policy configuration details ==========
        getStrategyConfig(client, flowControlStrategyId);

        // ========== Modify policy configuration status ==========
        modifyStrategyConfigStatus(client, flowControlStrategyId, false);

        // ========== Delete policy configuration ==========
        deleteStrategyConfig(client, flowControlStrategyId);
    }

    /**
     * Create client (common for self-managed ACK and Enterprise Edition)
     */
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            // Self-managed ACK environment: AK/SK do not need to be filled in
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            // Enterprise Edition environment: Requires valid AK/SK
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    /**
     * Get endpoint
     */
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    /**
     * Set authentication headers (common for self-managed ACK and Enterprise Edition)
     */
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            // Self-managed ACK environment authentication
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            // Enterprise Edition environment authentication
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    /**
     * Create base request object
     */
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    // ========== Policy configuration creation examples ==========

    /**
     * 1. Flow control policy (Flow Control Policy)
      config structure: CacheGatewayFlowRule
     */
    private static String createFlowControlStrategy(IAcsClient client) throws Exception 
{
        // Flow control rule configuration
        Map<String, Object> flowRule = new HashMap<>();
        flowRule.put("resource", "route-id-xxx");                           // 【Required
】Resource name (route ID)
        flowRule.put("resourceMode", 0);                                    // 【Required
】Resource mode: 0-route ID, 1-API group
        flowRule.put("grade", 1);                                           // 【Required
】Throttling threshold type: 1-QPS
        flowRule.put("count", 100.0);                                       // 【Required
】Throttling threshold (QPS quantity)
        flowRule.put("controlBehavior", 0);                                 // 【Optional
】Flow control effect: 0-fast failure, 2-uniform queuing
        flowRule.put("intervalSec", 1L);                                    // 【Optional
】Statistical time window (seconds)
        flowRule.put("burst", 20);                                          // 【Optional
】Burst capacity
        flowRule.put("maxQueueingTimeoutMs", 500);                          // 【Optional
】Maximum queue waiting time (milliseconds)
        flowRule.put("enable", true);                                       // 【Optional
】Whether to enable

        // Optional: Parameter throttling configuration
        // Map<String, Object> paramItem = new HashMap<>();
        // paramItem.put("parseStrategy", 0);                                // Parameter
extraction strategy: 0-client IP, 1-Host, 2-Header, 3-URL parameter
        // paramItem.put("fieldName", "X-User-Id");                          // 
Parameter field name
        // paramItem.put("pattern", "user-*");                               // Matching 
pattern
        // paramItem.put("matchStrategy", 0);                                // Matching 
strategy: 0-exact, 1-regex
        // flowRule.put("paramItem", paramItem);

        List<Map<String, Object>> gatewayFlowRules = new ArrayList<>();
        gatewayFlowRules.add(flowRule);

        Map<String, Object> config = new HashMap<>();
        config.put("isOpenTrafficControl", true);                           // 【Required
】Whether to enable flow control
        config.put("gatewayFlowRules", gatewayFlowRules);                   // 
【Required】Flow control rule list

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Flow Control Policy");
        request.put("strategyConfigName", "route-flow-control");
        request.put("config", config);

        return executeCreate(client, request, "Flow Control Policy");
    }

    /**
     * 2. Timeout policy (Timeout Policy)
     * config structure: RequestTimeoutConfig
     */
    private static String createTimeoutStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("timeout", 30000);                                       // 【Required
】Timeout duration (milliseconds)

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Timeout Policy");
        request.put("strategyConfigName", "route-timeout");
        request.put("config", config);

        return executeCreate(client, request, "Timeout Policy");
    }

    /**
     * 3. Circuit breaker policy (Circuit Breaker Policy)
     * config structure: CacheRouteFuse
     */
    private static String createCircuitBreakerStrategy(IAcsClient client) throws Exception {
        // Circuit breaker condition configuration
        Map<String, Object> fuseCondition = new HashMap<>();
        fuseCondition.put("type", 2);                                       // 【Required
】Rule type: 1-average response time, 2-error count, 3-backend timeout
        fuseCondition.put("operator", "in");                                // 【Required
】Comparator: gt(greater than), in(includes), notIn(excludes)
        fuseCondition.put("judgValue", "500,502,503");                      // 【Required
】Judgment value (error code list or response time)
        fuseCondition.put("errorCount", 5.0);                               // 【Optional
】Error count threshold
        fuseCondition.put("statInterval", 30);                              // 【Optional
】Judgment time window (seconds)
        fuseCondition.put("timeWindow", 20);                                // 【Optional
】Circuit breaker duration (seconds)
        fuseCondition.put("minRequestAmount", 10);                          // 【Optional
】Minimum request count

        List<Map<String, Object>> routeFusesCondition = new ArrayList<>();
        routeFusesCondition.add(fuseCondition);

        // Degradation Mock configuration (used when degradeStrategy=1)
        Map<String, Object> fuseMock = new HashMap<>();
        fuseMock.put("isOpen", 1);                                          // 0-
disabled, 1-enabled
        fuseMock.put("responseCode", 200);                                  // 【Optional
】Response status code
        fuseMock.put("responseBody", "{\"code\":0,\"msg\":\"service degraded\"}");  // 
【Optional】Response body
        fuseMock.put("responseHeader", Arrays.asList("Content-Type:application/json"));  
// 【Optional】Response header list

        Map<String, Object> config = new HashMap<>();
        config.put("isOpenFuse", true);                                     // 【Required
】Whether to enable circuit breaking
        config.put("combinedCondition", "any");                             // 【Optional
】Combination condition: all(all satisfied), any(any satisfied)
        config.put("routeFusesCondition", routeFusesCondition);             // 
【Required】Circuit breaker condition list
        config.put("degradeStrategy", 1);                                   // 【Optional
】Degradation strategy: 1-Mock response
        config.put("fuseMock", fuseMock);                                   // 【Optional
】Degradation Mock configuration

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Circuit Breaker Policy");
        request.put("strategyConfigName", "route-circuit-breaker");
        request.put("config", config);

        return executeCreate(client, request, "Circuit Breaker Policy");
    }

    /**
     * 4. Cross-domain policy (Cross-domain Policy)
     * config structure: RouteCross
     */
    private static String createCorsStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenCross", true);                                    // 【Required
】Whether to enable cross-domain
        config.put("crossType", "cors");                                    // 【Optional
】Cross-domain type: cors, jsonp
        config.put("allowedOrigins", "*");                                  // 【Required
】Allowed origins (* means all)
        config.put("allowedMethods", Arrays.asList("GET", "POST", "PUT", "DELETE", 
"OPTIONS"));  // 【Required】Allowed methods
        config.put("allowedHeaders", "*");                                  // 【Optional
】Allowed request headers
        config.put("exposedHeaders", "X-Custom-Header");                    // 
【Optional】Exposed response headers
        config.put("allowedCredentials", true);                             // 【Optional
】Whether to allow credentials
        config.put("maxAge", 3600L);                                        // 【Optional
】Preflight request cache time (seconds)
        config.put("callbackFunc", "callback");                             // 【Optional
】JSONP callback function name

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Cross-domain Policy");
        request.put("strategyConfigName", "route-cors");
        request.put("config", config);

        return executeCreate(client, request, "Cross-domain Policy");
    }

    /**
     * 5. Caching policy (Caching Policy)
     * config structure: ResponseCache
     */
    private static String createCacheStrategy(IAcsClient client) throws Exception {
        // Cache interface configuration
        Map<String, Object> cacheRequest = new HashMap<>();
        cacheRequest.put("routeId", "route-id-xxx");                        // 【Required
】Route ID
        cacheRequest.put("cacheKey", "query:userId");                       // 【Optional
】Cache key rule

        List<Map<String, Object>> routeInterfaceList = new ArrayList<>();
        routeInterfaceList.add(cacheRequest);

        Map<String, Object> config = new HashMap<>();
        config.put("isOpenResponseCache", true);                            // 【Required
】Whether to enable caching
        config.put("routeInterfaceList", routeInterfaceList);               // 
【Optional】Cache interface list
        config.put("isOpenCacheControl", true);                             // 【Optional
】Whether to enable browser cache control
        config.put("maxAge", 300L);                                         // 【Optional
】Browser cache time (seconds)
        config.put("allowedStatusCodes", Arrays.asList(200, 301, 302));     // 【Optiona
l】Allowed cacheable status codes

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Caching Policy");
        request.put("strategyConfigName", "route-cache");
        request.put("config", config);

        return executeCreate(client, request, "Caching Policy");
    }

    /**
     * 6. IP allowlist and blocklist policy (IP Blacklist and Whitelist Policy)
     * config structure: RouteIpBlockConfig
     */
    private static String createIpBlockStrategy(IAcsClient client) throws Exception {
        // IP rule configuration
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("ip", "192.168.1.100");                               // 【Required
】IP address (supports CIDR format)
        allowRule.put("policy", "allow");                                   // 【Required
】Policy: allow-allowlist, deny-blocklist

        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("ip", "10.0.0.0/8");                                   // 【Required
】IP address (CIDR format)
        denyRule.put("policy", "deny");                                     // 【Required
】Policy

        List<Map<String, Object>> ipBlockRules = new ArrayList<>();
        ipBlockRules.add(allowRule);
        ipBlockRules.add(denyRule);

        Map<String, Object> config = new HashMap<>();
        config.put("isOpenIpBlock", true);                                  // 【Required
】Whether to enable IP allowlist/blocklist
        config.put("ipBlockRules", ipBlockRules);                           // 【Required
】IP rule list

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "IP Allowlist and Blocklist Policy");
        request.put("strategyConfigName", "route-ip-block");
        request.put("config", config);

        return executeCreate(client, request, "IP Allowlist and Blocklist Policy");
    }

    /**
     * 7. ACL permission control policy (ACL Permission Control Policy)
     * config structure: RouteACLConfig
     */
    private static String createAclStrategy(IAcsClient client) throws Exception {
        // ACL rule configuration
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("group", "consumer-group-allow");                     // 【Required
】Consumer group/ID
        allowRule.put("policy", "allow");                                   // 【Required
】Policy: allow-allow, deny-deny

        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("group", "consumer-group-deny");                       // 【Required
】Consumer group/ID
        denyRule.put("policy", "deny");                                     // 【Required
】Policy

        List<Map<String, Object>> aclRules = new ArrayList<>();
        aclRules.add(allowRule);
        aclRules.add(denyRule);

        Map<String, Object> config = new HashMap<>();
        config.put("isEnableACL", true);                                    // 【Required
】Whether to enable ACL permission control
        config.put("aclRules", aclRules);                                   // 【Required
】ACL rule list

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "ACL Permission Control Policy");
        request.put("strategyConfigName", "route-acl");
        request.put("config", config);

        return executeCreate(client, request, "ACL Permission Control Policy");
    }

    /**
     * 8. Mock policy (MOCK Policy)
     * config structure: CacheMockConfig
     */
    private static String createMockStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenMock", true);                                     // 【Required
】Whether to enable Mock
        config.put("responseCode", 200);                                    // 【Optional
】Response status code
        config.put("responseBody", "{\"code\":0,\"data\":{\"id\":1}}");     // 【Optiona
l】Response body
        config.put("responseHeader", Arrays.asList(                         // 【Optional
】Response header list
            "Content-Type:application/json",
            "X-Mock:true"
        ));

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "MOCK Policy");
        request.put("strategyConfigName", "route-mock");
        request.put("config", config);

        return executeCreate(client, request, "MOCK Policy");
    }

    /**
     * 9. Request tracing policy (Request Tracing Policy)
     * config structure: RouteTracingConfig
     */
    private static String createTracingStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isEnableTracing", true);                                // 【Required
】Whether to enable tracing
        config.put("traceHeader", "X-Trace-Id");                            // 【Required
】Tracing header name
        config.put("isEnableDownstream", true);                             // 【Optional
】Whether to pass to downstream services

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Tracing Policy");
        request.put("strategyConfigName", "route-tracing");
        request.put("config", config);

        return executeCreate(client, request, "Request Tracing Policy");
    }

    /**
     * 10. Request body size limit policy (Request Size Limit Policy)
     * config structure: DataSize
     */
    private static String createRequestSizeStrategy(IAcsClient client) throws Exception 
{
        Map<String, Object> config = new HashMap<>();
        config.put("dataSize", "10MB");                                     // 【Required
】Maximum request body size (supports KB/MB/GB units)

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Size Limit Policy");
        request.put("strategyConfigName", "route-request-size");
        request.put("config", config);

        return executeCreate(client, request, "Request Size Limit Policy");
    }

    // ========== Common operation methods ==========

    /**
     * Execute creation of policy configuration
     */
    private static String executeCreate(IAcsClient client, Map<String, Object> request,
String strategyName) throws Exception {
        CommonRequest commonRequest = 
createBaseRequest("/strategyConfig/createStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String strategyId = result.getString("data");
            System.out.println("create " + strategyName + " success, strategyId: " + strategyId);
            return strategyId;
        } else {
            System.out.println("create " + strategyName + " failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Query policy configuration list
     */
    private static void listStrategyConfigs(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("current", 1);
        request.put("size", 10);

        CommonRequest commonRequest = 
createBaseRequest("/strategyConfig/listStrategyConfigs");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listStrategyConfigs: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Query policy configuration details
     */
    private static void getStrategyConfig(IAcsClient client, String strategyConfigId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);

        CommonRequest commonRequest = 
createBaseRequest("/strategyConfig/getStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getStrategyConfig: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify policy configuration status
     */
    private static void modifyStrategyConfigStatus(IAcsClient client, String 
strategyConfigId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("isOpen", isOpen);

        CommonRequest commonRequest = 
createBaseRequest("/strategyConfig/modifyStrategyConfigStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyStrategyConfigStatus: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete policy configuration
     */
    private static void deleteStrategyConfig(IAcsClient client, String 
strategyConfigId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);

        CommonRequest commonRequest = 
createBaseRequest("/strategyConfig/deleteStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteStrategyConfig: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Policy type description (strategyName)**

The policy type uses the English identifier  `strategyName` . Different engines support different policy types.

**SCG policy (for SCG engine)**

| strategyName | Category | Description |
| --- | --- | --- |
| <code>Authentication Policy</code> | Authentication | The system supports authentication methods such as JWT, BASIC, and APIKEY, as well as custom authentication to protect application security. |
| <code>Flow Control Policy</code> | Traffic | The system limits the request rate to prevent a sudden surge of data from overwhelming the network. |
| <code>Timeout Policy</code> | Traffic | The system limits the maximum timeout duration for gateway-forwarded requests. |
| <code>Circuit Breaker Policy</code> | Traffic | The gateway blocks calls to service providers to protect application services. |
| <code>MOCK Policy</code> | Transformation | Set filtering rules and return values to handle data objects that are difficult to construct or obtain. |
| <code>Signature Policy</code> | Security | The system generates signatures for requests passing through the gateway. |
| <code>Cross-domain Policy</code> | Transformation | Documents or scripts from one domain can request resources from another domain through the gateway. |
| <code>Caching Policy</code> | Traffic | The system caches responses to avoid repeatedly requesting the same resources from backend services. |
| <code>IP Blacklist and</code><br><code>Whitelist Policy</code> | Security | The system restricts source IP addresses of requests to enhance backend service security. |
| <code>Request Tracing Policy</code> | Observability | The system adds request tracing headers to track request chains for requests passing through this gateway. |
| <code>ACL Permission Control</code><br><code>Policy</code> | Authentication | The system controls which consumers can access services. |
| <code>Request Size Limit</code><br><code>Policy</code> | Traffic | The system limits the maximum size of the request body. |
| <code>HSF Protocol Mapping</code><br><code>Policy</code> | Transformation | The system controls the specific HSF method targeted by routing and sets HTTP-to-HSF parameter format mappings. |

**Higress policies (for Higress engine)**

**Authentication policies**

| strategyName | Description |
| --- | --- |
| <code>basic-auth</code> | Authenticate and authorize based on the HTTP Basic Auth standard. |
| <code>hmac-auth</code> | Generate signatures based on the HMAC algorithm to authenticate and authorize identities. |
| <code>jwt-auth</code> | Authenticate and authorize based on JSON Web Token. |
| <code>key-auth</code> | Authenticate and authorize identities based on API keys. |
| <code>oauth</code> | Authenticate and authorize based on OAuth2. |
| <code>oidc</code> | Verify user identity based on the OpenID Connect standard. |
| <code>ext-auth</code> | Send authorization requests to external authorization services to check client request permissions. |

**Security policies**

| strategyName | Description |
| --- | --- |
| <code>bot-detect</code> | Identify and block internet crawlers from scraping site resources. |
| <code>ip-restriction</code> | Restrict access by adding IP addresses to an allowlist or blocklist. |
| <code>request-block</code> | Block HTTP requests based on characteristics such as URI and request headers. |
| <code>request-validation</code> | Validate the body and header data of forwarded requests. |
| <code>waf</code> | Configure WAF rules based on OWASP ModSecurity CRS. |

**Traffic policies**

| strategyName | Description |
| --- | --- |
| <code>key-rate-limit</code> | Limit traffic based on specific key values. |
| <code>cluster-key-rate-limit</code> | Limit traffic at the cluster level based on specific key values. |
| <code>cache-control</code> | Add Expires and Cache-Control headers to responses. |
| <code>cors</code> | Enable CORS on the server to return HTTP response headers. |

**Transformation policies**

| strategyName | Description |
| --- | --- |
| <code>custom-response</code> | Configure custom HTTP response status codes, headers, and body. |
| <code>de-graphql</code> | Convert RESTful APIs into GraphQL requests. |
| <code>transformer</code> | Transform request/response headers, query parameters, and body parameters. |
| <code>geo-ip</code> | Query geographic location information based on IP address and pass it to subsequent plugins. |
| <code>frontend-gray</code> | Implement frontend user grayscale functionality for business A/B testing. |
| <code>model-mapper</code> | Map model parameter values in LLM protocols according to specified rules. |
| <code>model-router</code> | Route requests based on the model parameter in LLM protocols. |

**Observability policies**

| strategyName | Description |
| --- | --- |
| <code>traffic-tag</code> | Tag traffic by adding request headers based on weight or request content. |
| <code>log-request-response</code> | Record request and response information for debugging and monitoring. |

**Other policies**

| strategyName | Description |
| --- | --- |
| <code>opa</code> | Implement OPA policy control. |

**Policy scope description (scope)**

You can apply policies to different scopes. The priority is: **route > domain > service > consumer > instance.**

| scope | bitMask | Description |
| --- | --- | --- |
| <code>INSTANCE</code> | 1 | Apply the policy to the entire gateway instance. |
| <code>ROUTE</code> | 2 | Apply the policy to a specific route. |
| <code>SERVICE</code> | 4 | Apply the policy to a specific service. |
| <code>CONSUMER</code> | 8 | Apply the policy to a specific consumer. |
| <code>DOMAIN</code> | 16 | Apply the policy to a specific domain. |

**Composite scope**: You can apply a policy to multiple scopes simultaneously. For example,  `scope=3`  means applying the policy to both instance and route (INSTANCE + ROUTE = 1 + 2 = 3).

**Response code description**

| code | Description |
| --- | --- |
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-8"></a>

### 2.2.8. API call - Consumer management

**Overview**

The consumer management module lets you create, delete, modify, and query consumers. Consumers handle API authentication and authorization and can bind to routes for access control.

- **Applicable engine**: SCG / Higress (engine-agnostic, interface is universal)

- **Path prefix**:  `/application`

**Authentication method**

- **Self-built ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true` to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header and use a valid AccessKey pair.

**Create a consumer**

**API description**

Create a new consumer (application).

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/createApp</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| appName | String | Yes | The name of the consumer. |
| authType | Integer | Yes | The authentication type:<br>• 1: BASIC<br>• 2: OAuth2<br>• 3: JWT<br>• 4: CUSTOM<br>• 5: API_KEY<br>• 6: API_GATEWAY<br>• 7: CSB_AUTH |
| key | String | Yes | The authentication key (API key or username). |
| password | String | Conditional | The password.<br>Note<br>Use this parameter for BASIC authentication. |
| description | String | No | The description of the consumer. |
| expireTime | Long | No | The expiration timestamp in milliseconds. A value of <code> null </code> indicates that the key never expires. |

**List consumers**

**API description**

List consumers by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/listApps</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on AppRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number.Start from 1. |
| size | Integer | Yes | The number of entries per page. |
| appName | String | No | The name of the consumer. The system performs a fuzzy search. |
| authType | String | No | The authentication type for filtering. |
| appType | Integer | No | The application category:<br>• 0: Backend application<br>• 1: Portal application |
| isDisasterRecovery | Boolean | No | Specifies whether to filter disaster recovery consumers. |

**Query consumer details**

**API description**

Query the detailed information based on the consumer ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/getApp</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a consumer**

**API description**

Modify the configuration of an existing consumer.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/modifyApp</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| appName | String | Yes | The name of the consumer. |
| description | String | No | The description of the consumer. |

**Delete a consumer**

**API description**

Delete the specified consumer.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/deleteApp</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Delete consumers in batches**

**API description**

Delete multiple consumers in batches.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/batchDeleteApp</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appIds | List | Yes | The list of consumer IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Refresh token**

**API description**

Refresh the token (authentication credential) of the consumer.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/refreshToken</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Query all consumers**

**API description**

Query all consumers under the gateway instance without pagination.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/application/listAppsByGwInstanceId</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Consumer management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ConsumerApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create consumer (BASIC authentication) ==========
        String appId = createBasicConsumer(client);

        // ========== Create consumer (API Key authentication) ==========
        // String apiKeyAppId = createApiKeyConsumer(client);

        // ========== List consumers ==========
        listApps(client);

        // ========== Get consumer details ==========
        getApp(client, appId);

        // ========== Modify consumer ==========
        modifyApp(client, appId);

        // ========== Delete consumer ==========
        deleteApp(client, appId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create BASIC authentication consumer
     */
    private static String createBasicConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("appName", "consumer-demo-01");                         // 【Required
】Consumer name
        request.put("authType", 1);                                         // 【Required
】Authentication type: 1-BASIC
        request.put("key", "user-001");                                     // 【Required
】Username
        request.put("password", "secret-password");                         // 【Required
】Password (for BASIC authentication)
        request.put("description", "API consumer application");             // 【Optiona
l】Consumer description
        // request.put("expireTime", 315360000000L);                         // 【Optiona
l】Expiration timestamp (in milliseconds)

        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createBasicConsumer success, appId: " + appId);
            return appId;
        } else {
            System.out.println("createBasicConsumer failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Create API Key authentication consumer
     */
    private static String createApiKeyConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】GatewayinstanceID
        request.put("appName", "consumer-apikey-demo");                     // 
【Required】Consumer name
        request.put("authType", 5);                                         // 【Required
】Authentication type: 5-API_KEY
        request.put("key", "api-key-xxx");                                  // 【Required
】API Key value

        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createApiKeyConsumer success, appId: " + appId);
            return appId;
        } else {
            System.out.println("createApiKeyConsumer failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * List consumers
     */
    private static void listApps(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page
        // request.put("appName", "");                                        // 
【Optional】Consumer name (fuzzy search)
        // request.put("authType", "1");                                      // 
【Optional】Filter by authentication type
        // request.put("appType", 0);                                         // 
【Optional】Application category: 0-backend, 1-portal

        CommonRequest commonRequest = createBaseRequest("/application/listApps");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listApps: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get consumer details
     */
    private static void getApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/application/getApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getApp: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify consumer
     */
    private static void modifyApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("appName", "consumer-demo-modified");                   // 
【Required】Consumer name
        request.put("description", "Updated description");                  // 
【Optional】Consumer description

        CommonRequest commonRequest = createBaseRequest("/application/modifyApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyApp: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete consumer
     */
    private static void deleteApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/application/deleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteApp: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Batch delete consumers
     */
    private static void batchDeleteApps(IAcsClient client, List<String> appIds) throws 
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appIds", appIds);                                      // 【Required
】List of consumer IDs
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/application/batchDeleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteApp: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Refresh token
     */
    private static void refreshToken(IAcsClient client, String appId) throws Exception 
{
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/application/refreshToken");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("refreshToken: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Authentication type description**

| authType | Type name | Description |
| --- | --- | --- |
| 1 | BASIC | HTTP Basic authentication with username and password. |
| 2 | OAuth2.0 | OAuth2 authentication. |
| 3 | JWT | JWT authentication. |
| 4 | CUSTOM | Custom authentication. |
| 5 | API_KEY | API Key authentication. |
| 6 | API_GATEWAY | API gateway authentication. |
| 7 | CSB_AUTH | CSB authentication. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-9"></a>

### 2.2.9. API call - Domain name management

**Overview**

The Domain Name management module lets you create, delete, modify, and query domain names. A domain name configures the access domain name for a gateway to provide external services and supports the HTTP and HTTPS protocols.

- **Applicable engine**: SCG / Higress (The API is universal and does not distinguish between engines.)

- **API path prefix**:  `/domain`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header and use a valid AccessKey pair.

**Create a domain name**

**API description**

Create a new domain name configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/createDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateOrUpdateDomainRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| domain | String | Yes | The domain name, such as <code> api.example.com </code>. |
| protocol | String | Yes | The protocol type: HTTP or HTTPS. |
| certificateId | String | Conditional | The ID of the certificate.<br>Note<br>This parameter is required when you use the HTTPS protocol. |
| caCertificateId | String | No | The ID of the CA certificate. Use this parameter for mutual authentication. |
| clientAuth | Integer | No | The client authentication type:<br>• 0: None<br>• 1: Enabled |
| subjectDn | String | No | The header that contains information about the owner of the client certificate. |
| issuerDn | String | No | The header that contains information about the issuer of the client certificate. |

**List domains**

**API description**

List domains by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/listDomains</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListDomainsRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| domain | String | No | The domain name for fuzzy search. |
| protocol | String | No | The protocol type for filtering. |

**Query domain name details**

**API description**

Query the detailed information of a domain name by its ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/getDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetDomainRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| domainId | String | Yes | The ID of the domain name. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a domain name**

**API description**

Modify an existing domain name configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/modifyDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

Use the same parameters as those for creating a domain name. Additionally, you must specify  `domainId` .

**Delete a domain name**

**API description**

Delete the specified domain name.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/deleteDomain</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on DeleteDomainRequest)**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| domainId | String | Yes | The ID of the domain name. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**List all domain names**

**API description**

List all domain names under the gateway instance (without pagination).

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/domain/listAllDomains</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to use the Common Request method to call the Domain Name management API. The difference between a self-built ACK environment and an Enterprise Edition environment lies only in the Authentication Setting.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class DomainApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    // Self-hosted ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-hosted ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-hosted ACK console address

    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create an HTTP Domain Name ==========
        String httpDomainId = createHttpDomain(client);

        // ========== Create an HTTPS Domain Name (with certificate) ==========
        // String httpsDomainId = createHttpsDomain(client);

        // ========== List Domain Names ==========
        listDomains(client);

        // ========== Get Domain Name details ==========
        getDomain(client, httpDomainId);

        // ========== Modify Domain Name ==========
        modifyDomain(client, httpDomainId);

        // ========== Delete Domain Name ==========
        deleteDomain(client, httpDomainId);
    }

    /**
     * Create client (common for self-hosted ACK and Enterprise Edition)
     */
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create an HTTP Domain Name (based on CreateOrUpdateDomainRequest)
     */
    private static String createHttpDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("domain", "api.example.com");                           // 
[Required] Domain Name
        request.put("protocol", "HTTP");                                    // [Required]
Protocol type: HTTP

        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpDomain failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * Create an HTTPS Domain Name (with certificate)
     */
    private static String createHttpsDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("domain", "secure.example.com");                        // 
[Required] Domain Name
        request.put("protocol", "HTTPS");                                   // [Required]
Protocol type: HTTPS
        request.put("certificateId", "cert-id-xxx");                        // 
[Required]CertificateID(requiredforHTTPS)
        // request.put("caCertificateId", "ca-cert-id");                     // 
[Optional] CA certificate ID (used for mutual authentication)
        // request.put("clientAuth", 1);                                     // [Optional
] Client Authentication type: 0-none, 1-enabled
        // request.put("subjectDn", "CN=client");                            // [Optional
] Client certificate owner information header
        // request.put("issuerDn", "CN=issuer");                             // [Optional
] Client certificate issuer information header

        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpsDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpsDomain failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * List Domain Names (based on ListDomainsRequest)
     */
    private static void listDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("domain", "example");                                 // [Optional
] Domain Name (fuzzy search)
        // request.put("protocol", "HTTP");                                  // [Optional
] Protocol type filter

        CommonRequest commonRequest = createBaseRequest("/domain/listDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listDomains: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get Domain Name details (based on GetDomainRequest)
     */
    private static void getDomain(IAcsClient client, String domainId) throws Exception 
{
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/domain/getDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getDomain: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify Domain Name
     */
    private static void modifyDomain(IAcsClient client, String domainId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID to modify
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("domain", "api-new.example.com");                       // 
[Required] Domain Name
        request.put("protocol", "HTTP");                                    // [Required]
Protocol type

        CommonRequest commonRequest = createBaseRequest("/domain/modifyDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonRequest(commonRequest);
        System.out.println("modifyDomain: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete Domain Name (based on DeleteDomainRequest)
     */
    private static void deleteDomain(IAcsClient client, String domainId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/domain/deleteDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteDomain: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * List all Domain Names
     */
    private static void listAllDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/domain/listAllDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listAllDomains: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Protocol type description**

| protocol | Description |
| --- | --- |
| HTTP | The HTTP protocol does not require a certificate. |
| HTTPS | The HTTPS protocol requires binding an SSL certificate. |

**Client authentication type description**

| clientAuth | Description |
| --- | --- |
| 0 | No client authentication. |
| 1 | Enable mutual authentication. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The operation succeeded. |
| 400 | The parameter is invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-10"></a>

### 2.2.10. API call - Route plugin management

**Overview**

The route plugin management module provides plugin configuration at the route level. Plugins add extra features to routes, such as request/response processing, authentication, and logging.

- **Applicable engine**: SCG only (The Higress engine does not support this API. Use the policy configuration module instead.)

- **API path prefix**:  `/route`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header, and use a valid AccessKey pair.

**Create a route plugin**

**API call description**

Create a plugin configuration for a route.

> **Important**
>
> This applies only to the SCG engine.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/createRoutePlugin</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| pluginId | String | Yes | The ID of the plugin.You must query the plugin list first. |
| pluginName | String | Yes | The name of the plugin. |
| pluginConfig | Object | Yes | The configuration of the plugin in JSON format. |
| isOpen | Boolean | No | Specifies whether to enable the plugin.Default value: true. |

**Query the plugin list for a route**

**API call description**

Query the list of plugins under a route.

> **Important**
>
> This API call applies only to the SCG engine.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/listRoutePlugins</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |

**Modify route plugin**

**API description**

Modify the plugin configuration of a route.

> **Important**
>
> This applies only to the SCG engine.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/modifyRoutePlugin</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |
| pluginConfig | Object | Yes | The new plugin configuration. |

**Modify route plugin status**

**API description**

Enable or disable the route plugin.

> **Important**
>
> This feature applies only to the SCG engine.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/modifyRoutePluginStatus</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |
| isOpen | Boolean | Yes | • true: Enable the plugin.<br>• false: Disable the plugin. |

**Delete route plugin**

**API description**

Delete the plugin configuration of a route.

> **Important**
>
> This feature applies only to the SCG engine.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/route/deleteRoutePlugin</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |

**Common request call example**

The following example shows how to use the Common Request method to call the route Plugin management API. The difference between a self-hosted ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class RoutePluginApiDemo {

    // ========== Environment configuration (modify according to actual environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-h****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";

    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String ROUTE_ID = "your-route-id";
    private static final String PLUGIN_ID = "your-plugin-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create route Plugin ==========
        String routePluginId = createRoutePlugin(client);

        // ========== List route Plugins ==========
        listRoutePlugins(client);

        // ========== Modify route Plugin ==========
        modifyRoutePlugin(client, routePluginId);

        // ========== Modify route Plugin status ==========
        modifyRoutePluginStatus(client, routePluginId, false);

        // ========== Delete route Plugin ==========
        deleteRoutePlugin(client, routePluginId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create route Plugin
     */
    private static String createRoutePlugin(IAcsClient client) throws Exception {
        // Plugin configuration example (Header modification Plugin)
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "custom-value");
        pluginConfig.put("addHeaders", addHeaders);

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("pluginId", PLUGIN_ID);                                 // 【Required
】Plugin ID
        request.put("pluginName", "request-header-modifier");               // 
【Required】Plugin name
        request.put("pluginConfig", pluginConfig);                          // 【Required
】Plugin configuration
        request.put("isOpen", true);                                        // 【Optional
】Whether to enable

        CommonRequest commonRequest = createBaseRequest("/route/createRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String routePluginId = result.getString("data");
            System.out.println("createRoutePlugin success, routePluginId: " + 
routePluginId);
            return routePluginId;
        } else {
            System.out.println("createRoutePlugin failed: " + result.getString("msg"));
            return null;
        }
    }

    /**
     * List route Plugins
     */
    private static void listRoutePlugins(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page

        CommonRequest commonRequest = createBaseRequest("/route/listRoutePlugins");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listRoutePlugins: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify route Plugin
     */
    private static void modifyRoutePlugin(IAcsClient client, String routePluginId) throws Exception {
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "new-value");
        pluginConfig.put("addHeaders", addHeaders);

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID
        request.put("pluginConfig", pluginConfig);                          // 【Required
】New Plugin configuration

        CommonRequest commonRequest = createBaseRequest("/route/modifyRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoutePlugin: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify route Plugin status
     */
    private static void modifyRoutePluginStatus(IAcsClient client, String 
routePluginId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID
        request.put("isOpen", isOpen);                                      // 【Required
】true to enable, false to disable

        CommonRequest commonRequest = 
createBaseRequest("/route/modifyRoutePluginStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoutePluginStatus: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete route Plugin
     */
    private static void deleteRoutePlugin(IAcsClient client, String routePluginId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID

        CommonRequest commonRequest = createBaseRequest("/route/deleteRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatTypeJSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteRoutePlugin: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Notes**

- The route Plugin applies only to the SCG engine. Use the policy configuration module for the Higress engine.

- Query the Plugin list to obtain a valid  `pluginId`  before you create a route Plugin.

- The Plugin configuration format varies depending on the Plugin type.

**Response code description**

| code | Description |
| --- | --- |
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-2-2-11"></a>

### 2.2.11. API call - Certificate management

**Overview**

The certificate management module manages SSL/TLS certificates. You can create, delete, modify, and query certificates. Use certificates to configure HTTPS domains. The module supports server certificates and CA certificates.

- **Applicable engine**: SCG / Higress (engines are not distinguished; the API is universal)

- **API path prefix**:  `/certificate`

**Authentication method**

- **Self-managed ACK environment**: Add  `X-CSB-TOKEN: csb@2022`  and  `X-CSB-OPENAPI: true`  to the request header.

- **Enterprise Edition environment**: Add  `x-acs-organizationid`  and  `x-acs-caller-sdk-source`  to the request header. Also, use a valid AccessKey pair.

**Create a certificate API call description**

Create an SSL/TLS certificate.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/certificate/createCertificate</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the certificate. |
| certType | Integer | Yes | The type of the certificate:<br>• 0: Server certificate<br>• 1: CA certificate |
| cert | String | Yes | The content of the certificate in PEM format. |
| key | String | Conditional | The content of the private key.<br>Note<br>This parameter is required for server certificates. |

**Query the certificate list**

**API call description**

Query certificates by page.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/certificate/listCertificates</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| name | String | No | The certificate name for fuzzy search. |
| certType | Integer | No | The filter for certificate type. |

**Query certificate details**

**API call description**

Query detailed information by certificate ID.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/certificate/getCertificate</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| certificateId | String | Yes | The ID of the certificate. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a certificate**

**API call description**

Modify an existing certificate configuration.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/certificate/modifyCertificate</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

These parameters are the same as those for creating a certificate. You must also specify  `certificateId` .

**Delete a certificate**

**API call description**

Delete the specified certificate.

**Request information**

| Item | Content |
| --- | --- |
| URL | <code>/certificate/deleteCertificate</code> |
| Method | POST |
| Content-Type | application/json |

**Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| certificateId | String | Yes | The ID of the certificate. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Certificate API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.http.FormatType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;

import java.util.HashMap;
import java.util.Map;

public class CertificateApiDemo {

    // ========== Environment configuration (modify according to your actual 
environment) ==========

    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";

    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = yourorgid;

    private static final String GW_INSTANCE_ID = "your-gw-instance-id";

    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();

        // ========== Create a server certificate ==========
        String certId = createServerCertificate(client);

        // ========== Create a CA certificate ==========
        // String caCertId = createCACertificate(client);

        // ========== List certificates ==========
        listCertificates(client);

        // ========== Get certificate details ==========
        getCertificate(client, certId);

        // ========== Delete a certificate ==========
        deleteCertificate(client, certId);
    }

    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", 
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }

    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }

    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }

    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }

    /**
     * Create a server certificate
     */
    private static String createServerCertificate(IAcsClient client) throws Exception {
        // Certificate content in PEM format (replace with real certificate content in practice)
        String certContent = "-----BEGIN CERTIFICATE-----\n" +
                "**********************" +
                "-----END CERTIFICATE-----";

        String keyContent = "-----BEGIN PRIVATE KEY-----\n" +
                "**********************\n" +
                "-----END PRIVATE KEY-----";

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "my-server-cert");                              // [Required]
Certificate name
        request.put("certType", 0);                                         // [Required]
Certificate type: 0 - Server certificate
        request.put("cert", certContent);                                   // [Required]
Certificate content (PEM format)
        request.put("key", keyContent);                                     // [Required]
Private key content (required for server certificate)

        CommonRequest commonRequest = 
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createServerCertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createServerCertificate failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * Create a CA certificate
     */
    private static String createCACertificate(IAcsClient client) throws Exception {
        String caCertContent = "-----BEGIN CERTIFICATE-----\n" +
                "MIIBkTCB+wIJAKHHCgVZUffVMA0GCSqGSIb3DQEBCwUAMBExDzANBglghkgBZQME\n" +
                "-----END CERTIFICATE-----";

        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "my-ca-cert");                                  // [Required]
Certificate name
        request.put("certType", 1);                                         // [Required]
Certificate type: 1 - CA certificate
        request.put("cert", caCertContent);                                 // [Required]
Certificate content (PEM format)

        CommonRequest commonRequest = 
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result = 
JSON.parseObject(response.getHttpResponse().getHttpContentString());

        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createCACertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createCACertificate failed: " + 
result.getString("msg"));
            return null;
        }
    }

    /**
     * List certificates
     */
    private static void listCertificates(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("name", "");                                            // 
[Optional] Certificate name (fuzzy search)
        // request.put("certType", 1);                                         // 
[Optional] Filter by certificate type

        CommonRequest commonRequest = 
createBaseRequest("/certificate/listCertificates");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listCertificates: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Get certificate details
     */
    private static void getCertificate(IAcsClient client, String certificateId) throws 
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = createBaseRequest("/certificate/getCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getCertificate: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Modify a certificate
     */
    private static void modifyCertificate(IAcsClient client, String certificateId) throws Exception {
        String certContent = "-----BEGIN CERTIFICATE-----\n...new certificate content...
\n-----END CERTIFICATE-----";
        String keyContent = "-----BEGIN PRIVATE KEY-----\n...new private key content...\
n-----END PRIVATE KEY-----";

        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID
        request.put("name", "my-server-cert-modified");                     // 
[Required] Certificate name
        request.put("certType", 1);                                         // [Required]
Certificate type
        request.put("cert", certContent);                                   // [Required]
Certificate content
        request.put("key", keyContent);                                     // [Required]
Private key content

        CommonRequest commonRequest = 
createBaseRequest("/certificate/modifyCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyCertificate: " + 
response.getHttpResponse().getHttpContentString());
    }

    /**
     * Delete a certificate
     */
    private static void deleteCertificate(IAcsClient client, String certificateId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 
[Required] Gateway instance ID

        CommonRequest commonRequest = 
createBaseRequest("/certificate/deleteCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8", 
FormatType.JSON);

        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteCertificate: " + 
response.getHttpResponse().getHttpContentString());
    }
}
```

**Certificate type description**

| certType | Type name | Description |
| --- | --- | --- |
| 0 | Server Certificate | Use this certificate for HTTPS domains. You must provide both the certificate and the private key. |
| 1 | CA Certificate | Use this certificate for mutual TLS authentication. |

**Response code description**

| code | Description |
| --- | --- |
| 200 | The request succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

<a id="section-3"></a>

# 3.API Gateway

<a id="section-3-1"></a>

## 3.1. Cluster management

<a id="section-3-1-1"></a>

### 3.1.1. ListClusters

Queries a list of clusters.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size |
| clusterNa me | Strin g | Body | No | my-cluster | The name of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --k8sClusterCod e | String | k8s-cluster-001 | The code of the Kubernetes cluster. |
| --k8sClusterNa me | String | production-cluster | The name of the Kubernetes cluster. |
| --masterUrl | String | https://k8s-master.example.co m:6443 | The URL of the master node. |
| --k8sClusterStat us | Integer | 1 | The status of the Kubernetes cluster. |
| --k8sClusterStat usDesc | String | running | The description of the Kubernetes cluster status. |
| --k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | The time when the Kubernetes cluster was imported. |
| --k8sClusterTyp e | String | ACK | The type of the Kubernetes cluster. |
| --k8sClusterAttri bute | Struct | {} | The properties of the Kubernetes cluster. |
| ---csClusterId | String | c-123456abcdef | The ID of the container service cluster. |
| ---csClusterNam e | String | prod-k8s-cluster | The name of the container service cluster. |
| ---slbType | String | alb | The type of the Server Load Balancer. |
| ---vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| ---mappingIP | String | 10.0.0.1 | The mapped IP address. |
| ---mappingPort | Integer | 8080 | The mapped port. |
| ---tunnelName | String | vpn-tunnel-001 | The name of the channel. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

<a id="section-3-1-2"></a>

### 3.1.2. GetK8sClusterInfoByGwInstanceId

Queries Kubernetes cluster information based on a gateway instance ID.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -k8sClusterCod e | String | k8s-cluster-001 | The code of the Kubernetes cluster. |
| -k8sClusterNa me | String | production-cluster | The name of the Kubernetes cluster. |
| -masterUrl | String | https://k8s-master.example.co m:6443 | The URL of the master node. |
| -k8sClusterStat us | Integer | 1 | The status of the Kubernetes cluster. |
| -k8sClusterStat usDesc | String | Running | The description of the Kubernetes cluster status. |
| -k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | The time when the Kubernetes cluster was imported. |

<a id="section-3-1-3"></a>

### 3.1.3. GetK8sClusterName

Queries the name of a Kubernetes cluster.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | String | {} | The returned data. |

<a id="section-3-1-4"></a>

### 3.1.4. ImportCluster

Imports a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| configCont ent | Strin g | Body | No | key=value | The configuration content. |
| k8sCluster Name | Strin g | Body | No | production-cluster | The name of the Kubernetes cluster. |
| k8sCluster Type | Strin g | Body | No | ACK | The type of the Kubernetes cluster. |
| k8sCluster Attribute | Json | Body | No | {} | The properties of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-1-5"></a>

### 3.1.5. UpdateCluster

Updates a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| clusterCod e | Strin g | Body | No | cluster-001 | The cluster code. |
| k8sCluster Attribute | Strin g | Body | No | {} | The properties of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-1-6"></a>

### 3.1.6. CancelImportCluster

Cancels the import of a cluster.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| k8sCluster Code | Strin g | Body | No | k8s-cluster-001 | The code of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The data |

<a id="section-3-1-7"></a>

### 3.1.7. CheckConnectCluster

Checks the connection status of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| configCont ent | Strin g | Body | No | key=value | The configuration content. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | Struct | {} | The data |
| -connectStatus | Integer | 1 | The connection status. |
| -connectStatus Desc | String | Connected | The description of the connection status. |

<a id="section-3-1-8"></a>

### 3.1.8. ListK8sAllNamespaces

Queries all namespaces in the Kubernetes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| clusterCod e | Strin g | Body | No | cluster-001 | The cluster code. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The returned data. |

<a id="section-3-1-9"></a>

### 3.1.9. ListAllNamespaces

Lists all namespaces.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -namespaceId | String | ns-abc123 | The namespace ID. |
| -namespaceNa me | String | Production environment | The namespace name. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |

<a id="section-3-2"></a>

## 3.2. Instance Management

<a id="section-3-2-1"></a>

### 3.2.1. ListInstances

Queries a list of instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| name | Strin g | Body | No | my-resource | The name of the resource. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| deployMod e | Strin g | Body | No | rolling | The deployment mode. |
| status | Integ er | Body | No | 1 | The status. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -records | Array | \[\] | The list of records. |
| --accessMode | Array | \[\] | The list of access modes. |
| ---ips | String | \[\] | The list of IP addresses. |
| ---ports | String | \[\] | The list of ports. |
| ---externalIps | String | \[\] | The list of external IP addresses. |
| ---clusterIp | String | \[\] | The list of cluster IP addresses. |
| ---accessModeTy pe | String | public | The type of the access mode. |
| ---loadBalancerN etworkType | String | public | The network type of the Server Load Balancer (SLB) instance. |
| ---loadBalancerA ddressType | String | internet | The address type of the SLB instance. |
| ---serviceName | String | user-service | The name of the service. |
| --edasAppInfos | Array | \[\] | The list of EDAS application information. |
| ---appId | String | 12345678 | The ID of the application. |
| ---edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| ---k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| ---k8sNamespac e | String | default | The Kubernetes namespace. |
| --status | Integer | 1 | The status. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --name | String | my-resource | The name. |
| --instanceName | String | instance-001 | The name of the instance. |
| --deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| --deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| --deployCluster Name | String | Production cluster | The name of the deployment cluster. |
| --k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --modifyTime | String | 2024-10-14 12:30:00 | The update time. |
| --tid | String | t-123456789 | The ID of the task. |
| --vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| --regionId | String | cn-hangzhou | The ID of the region. |
| --zoneId | String | cn-hangzhou-b | The ID of the zone. |
| --deployMode | String | rolling | The deployment mode. |
| --edasAppId | String | edas-app-123456 | The ID of the EDAS application. |
| --edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| --k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| --k8sNamespac e | String | default | The Kubernetes namespace. |
| --instanceClass | String | ecs.g6.large | The instance type. |
| --department | String | Technology department | The department. |
| --resourceGroup | String | rg-default | The resource group. |
| --ingressClassN ame | String | nginx | The class name of the Ingress. |
| --brokerEngineT ype | String | RocketMQ | The type of the message engine. |
| --brokerEngineV ersion | String | 5.0 | The version of the message engine. |
| --brokerLatestE ngineVersion | String | 5.1.0 | The latest version of the message engine. |
| --deployCluster Attribute | String | {"zone":"cn-hangzhou-a"} | The attributes of the deployment cluster. |
| --nodeNumber | Integer | 5 | The number of nodes. |
| --sharedInstanc e | Boolean | false | Indicates whether the instance is a shared instance. |
| --sharedInstanc eSource | String | aliyun | The source of the shared instance. |
| --vSwitchId | String | vsw-bp1234567890 | The ID of the vSwitch. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The number of the current page. |
| -size | Integer | 100 | The size. |

<a id="section-3-2-2"></a>

### 3.2.2. ListAllInstances

Queries a list of all instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -accessMode | Array | \[\] | A list of access modes. |
| --ips | String | \[\] | A list of IP addresses. |
| --ports | String | \[\] | A list of ports. |
| --externalIps | String | \[\] | A list of external IP addresses. |
| --clusterIp | String | \[\] | A list of cluster IP addresses. |
| --accessModeTy pe | String | public | The access mode type. |
| --loadBalancerN etworkType | String | public | The network type of the Server Load Balancer instance. |
| --loadBalancerA ddressType | String | internet | The address type of the Server Load Balancer instance. |
| --serviceName | String | user-service | The service name. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| -status | Integer | 1 | The status. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-2-3"></a>

### 3.2.3. ListInstancesByServiceId

This operation queries a list of instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -serviceStruct | Map | {} | The service structure. |
| -instanceList | Map | {} | The list of instances. |

<a id="section-3-2-4"></a>

### 3.2.4. GetInstanceInfo

Queries information about an instance.

**Request headers**

This operation uses only common request headers. For more information, see the Common Request Parameters document.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -accessMode | Array | \[\] | The list of access modes. |
| --ips | String | \[\] | The list of IP addresses. |
| --ports | String | \[\] | The list of ports. |
| --externalIps | String | \[\] | The list of external IP addresses. |
| --clusterIp | String | \[\] | The list of cluster IP addresses. |
| --accessModeTy pe | String | public | The access mode type. |
| --loadBalancerN etworkType | String | public | The network type of the Server Load Balancer (SLB) instance. |
| --loadBalancerA ddressType | String | internet | The address type of the SLB instance. |
| --serviceName | String | user-service | The service name. |
| -edasAppInfos | Array | \[\] | The list of EDAS application information. |
| --appId | String | 12345678 | The application ID. |
| --edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| --k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| --k8sNamespac e | String | default | The Kubernetes namespace. |
| -status | Integer | 1 | The status. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| -instanceName | String | instance-001 | The instance name. |
| -deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| -deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| -deployCluster Name | String | Production Cluster | The name of the deployment cluster. |
| -k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -modifyTime | String | 2024-10-14 12:30:00 | The modification time. |
| -tid | String | t-123456789 | The task ID. |
| -vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -deployMode | String | rolling | The deployment mode. |
| -edasAppId | String | edas-app-123456 | The ID of the EDAS application. |
| -edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| -k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| -k8sNamespac e | String | default | The Kubernetes namespace. |
| -instanceClass | String | ecs.g6.large | The instance type. |
| -department | String | Technical Department | The department. |
| -resourceGroup | String | rg-default | The resource group. |
| -ingressClassN ame | String | nginx | The Ingress class name. |
| -brokerEngineT ype | String | RocketMQ | The message engine type. |
| -brokerEngineV ersion | String | 5.0 | The message engine version. |
| -brokerLatestE ngineVersion | String | 5.1.0 | The latest version of the message engine. |
| -deployCluster Attribute | String | {"zone":"cn-hangzhou-a"} | The properties of the deployment cluster. |
| -nodeNumber | Integer | 5 | The number of nodes. |
| -sharedInstanc e | Boolean | false | Indicates whether the instance is a shared instance. |
| -sharedInstanc eSource | String | Alibaba Cloud | The source of the shared instance. |
| -vSwitchId | String | vsw-bp1234567890 | The ID of the virtual switch. |

<a id="section-3-2-5"></a>

### 3.2.5. CreateInstance

Creates an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eName | Strin g | Body | No | Production Gateway Instance | The name of the gateway instance. |
| clusterCod e | Strin g | Body | No | cluster-001 | The code of the cluster. |
| deployCon figContent | Strin g | Body | No | replicas: 3 image: nginx:latest | The content of the deployment configuration. |
| accessMod eConfigCo ntent | Strin g | Body | No | mode: public enabled: true | The content of the access mode configuration. |
| namespac e | Strin g | Body | No | prod-ns | The namespace |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | The ID of the VPC. |
| vswId | Strin g | Body | No | vsw-1234567890 | The ID of the vSwitch. |
| ingressNa me | Strin g | Body | No | my-ingress | The name of the Ingress. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |
| instanceCl ass | Strin g | Body | No | ecs.g6.large | The instance type. |
| instanceN umber | Strin g | Body | No | INS20240101001 | The instance number. |
| o11y | Json | Body | No | {"enabled":true,"metrics":"prometheus"} | The observability configuration. |
| deployMod e | Strin g | Body | No | rolling | The deployment mode. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-2-6"></a>

### 3.2.6. AscmCreateInstance

Creates an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eName | Strin g | Body | No | production-gateway-instance | The gateway instance name. |
| clusterCod e | Strin g | Body | No | cluster-001 | Cluster code. |
| instanceN umber | Strin g | Body | No | INS20240101001 | Instance number. |
| instanceCl ass | Strin g | Body | No | ecs.g6.large | Instance type. |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | VPC ID. |
| backupZon eId | Strin g | Body | No | cn-hangzhou-h | Backup zone ID. |
| backupVS witchId | Strin g | Body | No | vsw-bp1234567890 | Backup vSwitch ID. |
| thirdZoneI d | Strin g | Body | No | cn-hangzhou-c | Third zone ID. |
| thirdVSwit chId | Strin g | Body | No | vsw-third-001 | Third zone vSwitch ID. |
| zoneType | Strin g | Body | No | primary | Zone type. |
| uid | Strin g | Body | No | user-1234567890 | User ID. |
| deployMod e | Strin g | Body | No | rolling | Deployment mode. |
| edasName spaceId | Strin g | Body | No | edas-ns-001 | EDAS namespace ID. |
| k8sClusterI d | Strin g | Body | No | c-abc123def456 | Kubernetes cluster ID. |
| k8sNames pace | Strin g | Body | No | default | Kubernetes namespace. |
| edasAppIn fos | Repe atLis t | Body | No | \[\] | A list of EDAS application information. |
| -appId | Strin g | Body | No | 12345678 | Application ID. |
| -edasName spaceId | Strin g | Body | No | edas-ns-001 | EDAS namespace ID. |
| -k8sClusterI d | Strin g | Body | No | c-abc123def456 | Kubernetes cluster ID. |
| -k8sNames pace | Strin g | Body | No | default | Kubernetes namespace. |
| deployCon figContent | Strin g | Body | No | replicas: 3 image: nginx:latest | Deployment configuration content. |
| accessMod eConfigCo ntent | Strin g | Body | No | mode: public enabled: true | Access mode configuration content. |
| namespac e | Strin g | Body | No | prod-ns | Namespace. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | Message engine type. |
| ingressCla ssName | Strin g | Body | No | nginx | Ingress class name. |
| o11y | Json | Body | No | {"enabled":true,"metrics":"prometheus"} | Observability configuration. |
| Departme nt | Strin g | Body | No | 1 | Department ID. |
| ResourceG roup | Strin g | Body | No | rg-acfmxazb4ph6aiy | Resource group. |
| RegionId | Strin g | Body | No | cn-hangzhou | Region ID. |
| ZoneId | Strin g | Body | No | cn-hangzhou-a | Zone ID. |
| vSwitchId | Strin g | Body | No | vsw-bp1234567890 | vSwitch ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

<a id="section-3-2-7"></a>

### 3.2.7. ModifyInstance

Modifies an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| instanceNa me | Strin g | Body | No | instance-001 | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

<a id="section-3-2-8"></a>

### 3.2.8. ModifyInstanceImageUrl

Modifies the image URL of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| imageUrl | Strin g | Body | No | https://example.com/logo.png | The URL of the image. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

<a id="section-3-2-9"></a>

### 3.2.9. UpgradeInstance

Upgrades an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common Request Parameters document.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

<a id="section-3-2-10"></a>

### 3.2.10. DeleteInstance

Deletes an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| forcedDele te | Bool ean | Body | No | false | Specifies whether to force delete the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

<a id="section-3-2-11"></a>

### 3.2.11. RestartInstance

Restarts an instance.

**Request headers**

This operation includes only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The data. |

<a id="section-3-2-12"></a>

### 3.2.12. StopInstance

Stops an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

<a id="section-3-2-13"></a>

### 3.2.13. RefreshInstance

Refreshes an instance.

**Request headers**

This operation uses only common request headers. For more information about these headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eCode | Strin g | Body | No | gw-instance-001 | The code of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The status code. |
| msg | String | Operation successful | The message |
| data | Struct | {} | The returned data. |
| -accessMode | Array | \[\] | The list of access modes. |
| --ips | String | \[\] | The list of IP addresses. |
| --ports | String | \[\] | The list of ports. |
| --externalIps | String | \[\] | The list of external IP addresses. |
| --clusterIp | String | \[\] | The list of cluster IP addresses. |
| --accessModeTy pe | String | public | The type of the access mode. |
| -status | Integer | 1 | The status. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| -name | String | my-resource | The name. |
| -deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| -deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| -deployCluster Name | String | Production Cluster | The name of the deployment cluster. |
| -k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| -createTime | String | 2024-10-14 08:00:00 | TThe creation time. |
| -modifyTime | String | 2024-10-14 12:30:00 | The update time. |
| -tid | String | t-123456789 | The task ID. |

<a id="section-3-2-14"></a>

### 3.2.14. CreateInstanceDeployConfig

Creates an instance deployment configuration.

**Request headers**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| cpuReques t | Strin g | Body | No | 1000m | The CPU request. |
| cpuLimit | Strin g | Body | No | 2000m | The CPU limit. |
| memoryRe quest | Strin g | Body | No | 512Mi | The memory request. |
| memoryLi mit | Strin g | Body | No | 1Gi | The memory limit. |
| replicas | Integ er | Body | No | 3 | The number of replicas. |
| jvmArgs | Strin g | Body | No | -Xms512m -Xmx1024m | The JVM parameters. |
| gwInstanc eName | Strin g | Body | No | Production Gateway Instance | The name of the gateway instance. |
| accessMod eType | Strin g | Body | No | public | The access mode type. |
| ports | Repe atLis t | Body | No | \[\] | The list of ports. |
| -port | Integ er | Body | No | 8080 | The port number. |
| -targetPort | Strin g | Body | No | 8080 | The target port. |
| -nodePort | Integ er | Body | No | 30080 | The node port. |
| -name | Strin g | Body | No | my-resource | The name. |
| -protocol | Strin g | Body | No | HTTP | The protocol. |
| namespac e | Strin g | Body | No | prod-ns | The namespace. |
| externalTr afficPolicy | Strin g | Body | No | Local | The external traffic policy. |
| ipType | Strin g | Body | No | IPv4 | The IP type. |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | The ID of the VPC. |
| vswId | Strin g | Body | No | vsw-1234567890 | The ID of the vSwitch. |
| uid | Strin g | Body | No | user-1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -deployConfigY amlStr | String | apiVersion: apps/v1 kind: Deployment | The deployment configuration as a YAML string. |
| -accessModeCo nfigYamlStr | String | mode: public enabled: true | The access mode configuration as a YAML string. |

<a id="section-3-2-15"></a>

### 3.2.15. GetInstanceDeployDeployConfig

Queries the deployment configuration of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-2-16"></a>

### 3.2.16. GetInstanceDeployMsg

Queries the deployment message of an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -accessModeLis t | Array | \[\] | The list of access modes. |
| --intranetUrlStrL ist | String | \[\] | The list of internal network URLs. |
| --networkUrlStrL ist | String | \[\] | The list of network URLs. |
| --name | String | my-resource | The name. |
| --type | String | 1 | The type. |
| -podInfoList | Array | \[\] | The list of pod information. |
| --ipList | Array | \[\] | The list of IP addresses. |
| ---ip | String | 192.168.1.100 | The IP address. |
| ---ipType | String | IPv4 | The IP address type. |
| --name | String | my-resource | The name. |
| --isReady | Boolean | true | Whether it is ready. |
| -deploymentNa me | String | app-deployment | The deployment name. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -instanceName | String | instance-001 | The instance name. |
| -engineSpecific ation | String | MSE_GTW_16_32_2 00_c | The engine specifications. |
| -vpcId | String | vpc-bp1234567890 | The VPC ID. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -vSwitchId | String | vsw-bp1234567890 | The virtual switch ID. |
| -resConfig | Struct | {} | Response Configuration |
| --cpuRequest | String | 1000m | The requested CPU resources. |
| --memoryReque st | String | 512Mi | The requested memory resources. |
| --cpuLimit | String | 2000m | The CPU limit. |
| --memoryLimit | String | 1Gi | The memory limit. |
| --replicas | Integer | 3 | The number of replicas. |
| --jvmArgs | String | -Xms512m -Xmx1024m | The JVM parameters. |
| -clusterConfig | Struct | {} | The cluster configuration. |
| --clusterName | String | my-cluster | The cluster name. |
| --namespace | String | prod-ns | The namespace. |
| --clusterCode | String | cluster-001 | The cluster code. |

<a id="section-3-2-17"></a>

### 3.2.17. GetCustomDeployConfig

Queries a custom deployment configuration.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -deploymentYa mlStr | String | apiVersion: apps/v1 kind: Deployment | The deployment YAML string. |
| -serviceYamlStr | String | apiVersion: v1 kind: Service | The service YAML string. |
| -jarStr | String | my-service.jar | The JAR file name. |
| -wgetStr | String | wget https://example.co m/file | The Wget command string. |

<a id="section-3-2-18"></a>

### 3.2.18. GetInstanceAccessModeConfig

Retrieves the access mode configuration of an instance.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The response message. |
| data | Map | {} | The data |

<a id="section-3-2-19"></a>

### 3.2.19. GetResource

Queries the resources of an instance.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -replicas | Integer | 3 | The number of replicas. |
| -jvmArgs | String | -Xms512m -Xmx1024m | The JVM parameters. |
| -instanceName | String | instance-001 | The instance name. |
| -engineSpecific ation | String | MSE_GTW_16_32_2 00_c | The engine specifications. |
| -vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -backupZoneId | String | cn-hangzhou-h | The ID of the backup zone. |
| -backupVSwitc hId | String | vsw-bp1234567890 | The ID of the backup vSwitch. |
| -thirdZoneId | String | cn-hangzhou-c | The ID of the third zone. |
| -thirdVSwitchId | String | vsw-third-001 | The ID of the vSwitch in the third zone. |
| -zoneType | String | primary | The type of the zone. |
| -vSwitchId | String | vsw-bp1234567890 | The vSwitch ID. |
| -cpuRequest | Struct | 1000m | The requested CPU resources. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| -memoryReque st | Struct | 512Mi | Memory Request |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| -cpuLimit | Struct | 2000m | The CPU limit. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| -memoryLimit | Struct | 1Gi | The memory limit. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |

<a id="section-3-2-20"></a>

### 3.2.20. ModifyResource

Modifies the resources of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| replicas | Integ er | Body | No | 3 | The number of replicas. |
| specificati onTemplat e | Integ er | Body | No | 1 | The specification template. |
| source | Strin g | Body | No | manual | The source. |
| instanceCl ass | Strin g | Body | No | ecs.g6.large | The instance type. |
| backupZon eId | Strin g | Body | No | cn-hangzhou-h | The ID of the backup zone. |
| backupVS witchId | Strin g | Body | No | vsw-bp1234567890 | The ID of the backup vSwitch. |
| thirdZoneI d | Strin g | Body | No | cn-hangzhou-c | The ID of the third zone. |
| thirdVSwit chId | Strin g | Body | No | vsw-third-001 | The ID of the vSwitch in the third zone. |
| zoneType | Strin g | Body | No | primary | The type of the zone. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-3"></a>

## 3.3. Group Management

<a id="section-3-3-1"></a>

### 3.3.1. ModifyGroup

This operation modifies a group.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| name | Strin g | Body | No | my-resource | The name. |
| basePath | Strin g | Body | No | /api/v1 | The base path. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| domainIds | Repe atLis t | Body | No | \[\] | A list of domain name IDs. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-3-2"></a>

### 3.3.2. CreateGroup

Creates a group.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| name | Strin g | Body | No | my-resource | The name. |
| basePath | Strin g | Body | No | /api/v1 | The base path. |
| needDefau ltDomain | Bool ean | Body | No | true | Specifies whether a default domain name is required. |
| description | Strin g | Body | No | This is an example service | The description. |
| domainIds | Repe atLis t | Body | No | \[\] | The list of domain name IDs. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-3-3"></a>

### 3.3.3. ListGroups

Retrieves a list of groups.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| name | Strin g | Body | No | my-resource | The name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --domains | Array | \[\] | The list of domain names. |
| ---domainId | String | domain-123456 | The domain ID. |
| ---domain | String | api.example.com | The domain name. |
| ---protocol | String | HTTP | The protocol. |
| ---createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --groupId | String | group-123456 | The group ID. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --name | String | my-resource | The group name. |
| --basePath | String | /api/v1 | The base path. |
| --description | String | This is a sample service. | The description. |
| --defaultDomain | String | api.example.com | The default domain name. |
| --editable | Boolean | true | Indicates whether the group is editable. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

<a id="section-3-3-4"></a>

### 3.3.4. GetAllGroups

Retrieves a list of all groups.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -domains | Array | \[\] | A list of domain names. |
| --domainId | String | domain-123456 | The ID of the domain name. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -groupId | String | group-123456 | The ID of the group. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| -name | String | my-resource | The name |
| -basePath | String | /api/v1 | The base path. |
| -description | String | This is an example service. | Description. |
| -defaultDomain | String | api.example.com | The default domain name. |
| -editable | Boolean | true | Indicates whether the group is editable. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-3-5"></a>

### 3.3.5. GetGroup

Queries the details of a group.

**Request headers**

This operation uses common request headers and does not use special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -domains | Array | \[\] | The list of domain names. |
| --domainId | String | domain-123456 | The domain ID. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -groupId | String | group-123456 | The group ID. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| -basePath | String | /api/v1 | The base path. |
| -description | String | This is an example service. | The description. |
| -defaultDomain | String | api.example.com | The default domain name. |
| -editable | Boolean | true | Indicates whether the group is editable. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |

<a id="section-3-3-6"></a>

### 3.3.6. DeleteGroup

Deletes a group.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| groupId | Strin g | Body | No | group-123456 | The ID of the group. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

<a id="section-3-3-7"></a>

### 3.3.7. AddGroupDomain

Adds a domain name to a group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | gw-cn-wwo36s5y001 | The gateway instance ID. |
| groupId | Strin g | Body | No | 16782 | The API group ID. |
| domainIds | Repe atLis t | Body | No | \["3412", "3413"\] | The IDs of the domain names to attach. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The return code. A value of 200 indicates success. Other values indicate an error. |
| msg | String | success | The returned message. If the request is successful, 'success' is returned. If the request fails, an error message is returned. |
| data | String | true | The returned data. If the operation is successful, the string 'true' is returned. |

**Examples**

Request example

```json
{
  "gwInstanceId": "gw-cn-wwo36s5y001",
  "groupId": "16782",
  "domainIds": [
    "3412",
    "3413"
  ]
}
```

Successful response example

`JSON`  format

```json
{
  "code": 200,
  "msg": "success",
  "data": "true"
}
```

<a id="section-3-3-8"></a>

### 3.3.8. DeleteGroupDomain

Deletes a domain name from a group.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-4"></a>

## 3.4. Ingress management

<a id="section-3-4-1"></a>

### 3.4.1. CreateRoute

Creates a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```json
{
  "gwInstanceId": "string",
  "groupId": "string",
  "serviceId": "string",
  "routeName": "string",
  "routePath": [
    "string"
  ],
  "path": {
    "matchType": "string",
    "matchValue": "string",
    "caseSensitive": true
  },
  "openStripPrefix": true,
  "serviceType": "string",
  "serviceIds": [
    {
      "serviceId": "string",
      "weight": 0
    }
  ],
  "enableStatus": true,
  "stripPrefix": 0,
  "order": 0,
  "methods": [
    "string"
  ],
  "header": [
    {
      "key": "string",
      "value": "string"
    }
  ],
  "cookie": [
    {
      "key": "string",
      "value": "string"
    }
  ],
  "queryParam": [
    {
      "key": "string",
      "value": "string"
    }
  ],
  "domainIds": [
    "string"
  ],
  "routeId": "string",
  "hsfMethodMappingConfig": {
    "hsfMethod": "string",
    "parameterMappingList": [
      {
        "name": "string",
        "schema": {
          "type": "string",
          "items": "string",
          "array": true,
          "primitive": true,
          "generic": true
        },
        "location": "string",
        "required": true,
        "order": 0
      }
    ]
  }
}
```

**Request parameters**

| Parameter Name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| order | Integ er | Body | No | 100 | The sort number. |
| filters | Strin g | Body | No | path=/api/\*\* | The filter. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| routeNam e | Strin g | Body | No | user-service-route | The route name. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceTyp e | Strin g | Body | No | REST | The service type. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| methods | Repe atLis t | Body | No | \[\] | A list of request methods. |
| header | Repe atLis t | Body | No | \[\] | A list of request headers. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| cookie | Repe at list | Body | No | \[\] | A list of cookies. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| queryPara m | Repe atLis t | Body | No | \[\] | A list of query parameters. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| domainIds | Repe atLis t | Body | No | \[\] | A list of domain name IDs. |
| routePath | Repe atLis t | Body | No | /api/v1/users | The route path. |
| stripPrefix | Integ er | Body | No | 1 | The number of prefix levels to strip. |
| requestTi meout | Integ er | Body | No | 30000 | The request timeout period, in milliseconds. |
| openStripP refix | Bool ean | Body | No | true | Specifies whether to strip the prefix. |
| enableForc eNonceCh eck | Bool ean | Body | No | false | Specifies whether to enforce a random number check. |
| path | JSON | Body | No | /api/v1/resource | The path. |
| serviceIds | Repe atLis t | Body | No | \[\] | A list of service IDs. |
| -serviceId | Strin g | Body | No | service-123456 | The service ID. |
| -weight | Integ er | Body | No | 100 | The weight. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| enableStat us | Bool ean | Body | No | true | The enabled status. |
| hsfMethod MappingCo nfig | JSON | Body | No | {"method":"invoke","para ms":\[\]} | The HSF method mapping configuration. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-4-2"></a>

### 3.4.2. BatchDeleteRoute

Deletes multiple routes at once.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the document on common request parameters.

**Request parameters**

| Parameter Name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | Gateway instance ID. |
| routeIds | Repe atLis t | Body | No | \[\] | List of route IDs. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation succeeded | The message. |
| data | Struct | {} | The data. |
| -successIds | String | \[\] | List of successful IDs. |
| -failedIds | String | \[\] | List of failed IDs. |

<a id="section-3-4-3"></a>

### 3.4.3. ListRoutes

Queries a list of routes.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```http
POST /route/listRoutes HTTP/1.1
```

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 10 | The number of rows per page in a paged query. |
| current | Integ er | Body | No | 1 | Set the page on which the returned results are displayed. The default value is 1, indicating that the display starts on page 1. |
| routeNam e | Strin g | Body | No | demo-route | The name of the route. |
| serviceNa me | Strin g | Body | No | demo-service | The name of the service. |
| exactServi ceId | Strin g | Body | No | 1001 | The specified exact service ID is 1001, which uniquely identifies a specific service instance. |
| enableStat us | Bool ean | Body | No | true | The enabling status. |
| gwInstanc eId | Strin g | Body | No | i-demo | The ID of the gateway instance. |
| routeId | Strin g | Body | No | xxx-xxx-xxx-xxx | The ID of the route. |
| groupNam e | Strin g | Body | No | test | The name of the group. |
| domainNa me | Strin g | Body | No | example.com | The domain name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The Request is not authorization. | The error message. |
| data | Struct | {} | The returned data. |
| -records | Array | \[\] | The list of returned data records. |
| --routePath | String | /reviews/v1 | The path of the route. |
| --domains | String | \["example.com", "www.example.co m"\] | The list of domain names. |
| --routeId | String | RouteId_1 | The ID of the route. |
| --routeName | String | http-route | The name of the route. |
| --enableStatus | Boolean | true | Whether to enable it.disable: disabled enable: enable. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --serviceId | String | service-123456 | The ID of the service. |
| --serviceName | String | user-service | The name of the service. |
| --groupId | String | group-123456 | The ID of the group. |
| --groupName | String | Default group | The name of the group. |
| --path | Struct | /api/v1/resource | The path. |
| ---matchType | String | prefix | The match type. |
| ---matchValue | String | /v1/users | The match value. |
| ---caseSensitive | Boolean | false | Indicates whether the match is case-sensitive. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

**Examples**

Request example

```http
POST /route/listRoutes HTTP/1.1
{

}
```

Response example

`JSON`  format

```json
{
 "msg":"",
 "code":"",
 "data":{
  "total":"",
  "current":"",
  "size":"",
  "records":[
   {
    "routePath":"",
    "groupName":"",
    "routeId":"",
    "createTime":"",
    "groupId":"",
    "domains":"",
    "serviceId":"",
    "serviceName":"",
    "enableStatus":"",
    "path":[
     {
      "matchType":"",
      "caseSensitive":"",
      "matchValue":""
     }
    ],
    "routeName":""
   }
  ]
 }
}
```

<a id="section-3-4-4"></a>

### 3.4.4. ListRoutesByAppId

Queries a list of routes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| total | Integ er | Body | No | 1000 | The total number of entries. |
| routeNam e | Strin g | Body | No | user-service-route | The route name. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |
| --routePath | String | /api/v1/users | The route path. |
| --serviceId | String | service-123456 | The service ID. |
| --serviceName | String | user-service | The service name. |
| --serviceProtoco l | String | HTTP | The service protocol. |
| --authId | String | auth_123456 | The authentication ID. |
| --authStatus | Integer | 1 | The authentication status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-4-5"></a>

### 3.4.5. ListRoutesByGwInstanceId

Queries a list of routes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -routeId | String | route-123456 | The route ID. |
| -routeName | String | user-service-route | The route name. |
| -routePath | String | /api/v1/users | The route path. |
| -serviceId | String | service-123456 | The service ID. |
| -serviceName | String | user-service | The service name. |
| -serviceProtoco l | String | HTTP | The service protocol. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-4-6"></a>

### 3.4.6. GetAllRoutePath

Retrieves all routing paths.

**Request headers**

No special request headers are required for this operation. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| body | Strin g | Body | No | {"key":"value"} | The content of the request body. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Code | Integer | 200 | The response code. |
| Msg | String | The operation was successful. | The message |
| Data | Struct | {} | The data |
| -RoutePaths | String | \[\] | The list of routing paths. |

<a id="section-3-4-7"></a>

### 3.4.7. GetRoute

Queries the details of a specified route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -routePath | String | /api/v1/users | The path of the route. |
| -methods | String | \[\] | The list of request methods. |
| -header | Array | \[\] | The list of request headers. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -cookie | Array | \[\] | The list of cookies. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -queryParam | Array | \[\] | The list of query parameters. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -plugins | Array | \[\] | The list of plugins. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -sigSchemeDT OList | Array | \[\] | The list of signature schemes. |
| --sigSchemeStat us | Integer | 1 | The status of the signature scheme. |
| --sigSchemeNa me | String | HMAC-SHA256 | The name of the signature scheme. |
| --sigSchemeId | String | sig-scheme-001 | The ID of the signature scheme. |
| --sigAlg | String | SHA256withRSA | The signature algorithm. |
| --secretKey | String | sk_1234567890abc def | The secret key. |
| -domainVO | Array | \[\] | The list of domain name view objects. |
| --domainId | String | domain-123456 | The domain name ID. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The time when it was created. |
| -groupDomainV O | Array | \[\] | The list of group domain name view objects. |
| --domainId | String | domain-123456 | The domain name ID. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -strategyConfig s | Array | \[\] | The list of policy configurations. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --strategyConfig Id | String | strategy-config-001 | The ID of the policy configuration. |
| --strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| --strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | \[\] | The list of authorization scopes. |
| ---routeInfos | Array | \[\] | The list of route information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | \[\] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | \[\] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | \[\] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | ID |
| ---mcpServerInfo s | Array | \[\] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -serviceIds | Array | \[\] | The list of service IDs. |
| -routeId | String | route-123456 | The ID of the route. |
| -routeName | String | user-service-route | The name of the route. |
| -enableStatus | Boolean | true | The enabled status. |
| -openStripPrefi x | Boolean | true | Indicates whether to strip the prefix. |
| -stripPrefix | Integer | 1 | The number of prefix levels to strip. |
| -order | Integer | 100 | The sorting number. |
| -routeCreateTi me | String | 2024-10-14 09:00:00 | The time when the route was created. |
| -groupId | String | group-123456 | The group ID. |
| -groupName | String | Default Group | The group name. |
| -basePath | String | /api/v1 | The base path. |
| -serviceName | String | user-service | The service name. |
| -serviceId | String | service-123456 | The service ID. |
| -serviceDescrip tion | String | User Management Service | The service description. |
| -upstreamType | Integer | 1 | The upstream type. |
| -upstreamType Name | String | HTTP Service | The name of the upstream type. |
| -loadBalanceTy pe | Integer | 1 | The load balancing type. |
| -loadBalanceTy peName | String | Polling | The name of the load balancing type. |
| -serviceCreateT ime | String | 2024-10-14 08:00:00 | The time when the service was created. |
| -isOpenFreeCer t | Boolean | false | Indicates whether to enable the free certificate. |
| -isOpenTraffic | Boolean | true | Indicates whether to enable traffic shaping. |
| -isOpenMock | Boolean | false | Indicates whether to enable mocking. |
| -isOpenTimeOu t | Boolean | true | Indicates whether to enable timeout. |
| -requestTimeo ut | Integer | 30000 | The request timeout period, in milliseconds. |
| -isOpenPlugin | Boolean | true | Indicates whether to enable plugins. |
| -isOpenFuse | Boolean | true | Indicates whether to enable circuit breaking. |
| -isOpenSig | Boolean | true | Indicates whether to enable signing. |
| -isRewrite | Boolean | true | Indicates whether to enable rewriting. |
| -isOpenCross | Boolean | true | Indicates whether to enable cross-domain requests. |
| -isOpenRespon seCache | Boolean | true | Indicates whether to enable response caching. |
| -serviceType | String | REST | The service type. |
| -path | Struct | /api/v1/resource | The path. |
| --matchType | String | prefix | The match type. |
| --matchValue | String | /v1/users | The match value. |
| --caseSensitive | Boolean | false | Indicates whether the matching is case-sensitive. |
| -trafficControl | Struct | {} | The traffic shaping configuration. |
| --id | Integer | 123456 | The ID. |
| --userId | String | uid-123456 | The user ID. |
| --namespace | String | prod-ns | The namespace. |
| --routeId | String | route-123456 | The ID of the route. |
| --resourceMode | Integer | 1 | The resource mode. |
| --thresholdType | Integer | 1 | The threshold type. |
| --count | Float | 10.5 | The number. |
| --controlBehavio r | Integer | 1 | The throttling behavior. |
| --intervalSec | Integer | 30 | The time interval, in seconds. |
| --burst | Integer | 100 | The maximum burst traffic. |
| --maxQueueing TimeoutMs | Integer | 5000 | The maximum queuing timeout period, in milliseconds. |
| --isRequestAttr | Boolean | false | Indicates whether it is a request property. |
| --enable | Boolean | true | Indicates whether it is enabled. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --attrStr | Struct | {} | The property structure. |
| ---paramAttr | Integer | 1 | The parameter property. |
| ---paramAttrDeta il | String | query | The details of the parameter property. |
| ---isOpenMatch | Integer | 1 | Indicates whether to enable matching. |
| ---matchMode | Integer | 1 | The match mode. |
| ---matchString | String | /api/\* | The match string. |
| --thresholdByQp s | Struct | {} | The configuration for the QPS threshold. |
| ---qpsThreshold | Integer | 1000 | The QPS threshold. |
| ---timeInterval | Integer | 300 | The time interval, in seconds. |
| ---timeUnit | Integer | 1 | The time unit. |
| ---flowControlMe thod | Integer | 1 | The throttling method. |
| ---flowControlInf o | Integer | 1 | The throttling information. |
| --thresholdByTh readVo | Struct | {} | The configuration for the thread count threshold. |
| ---threadNum | Integer | 10 | The number of threads. |
| -routeMockCon figVo | Struct | {} | The route mock configuration. |
| --responseHead er | String | \[\] | The list of response headers. |
| --isOpen | Integer | true | Indicates whether it is enabled. |
| --responseBody | String | {"code":200,"data":{}} | The response body. |
| --responseCode | Integer | 200 | The response code. |
| -routeFusesCon figVo | Struct | {} | The route circuit breaking configuration. |
| --routeFusesCon dition | Array | \[\] | The list of route circuit breaking conditions. |
| ---id | Integer | 123456 | The ID. |
| ---type | Integer | 1 | The type. |
| ---operator | String | admin | The operator. |
| ---judgValue | String | 100 | The judgment value. |
| ---errorCount | Float | 5.0 | The number of errors. |
| ---statInterval | Integer | 60 | The statistics interval, in seconds. |
| ---timeWindow | Integer | 60 | The time window, in seconds. |
| ---minRequestA mount | Integer | 10 | The minimum number of requests. |
| ---halfOpenBase AmountPerSte p | Integer | 5 | The base number of requests per step in the half-open state. |
| ---halfOpenReco veryStepNum | Integer | 3 | The number of recovery steps in the half-open state. |
| --resourceId | String | res-abc123 | The resource ID. |
| --combinedCond ition | String | A AND B | The combined conditional expression. |
| --degradeStrate gy | Integer | 1 | The degradation policy. |
| --fuseMock | Struct | {} | The circuit breaking mock configuration. |
| ---responseHead er | String | \[\] | The list of response headers. |
| ---isOpen | Integer | true | Indicates whether it is enabled. |
| ---responseBody | String | {"code":200,"data":{}} | The response body. |
| ---responseCode | Integer | 200 | The response code. |
| -routeAuthVO | Struct | {} | The route authentication configuration. |
| --requestHeader | String | Content-Type | The request header. |
| --authType | Integer | jwt | The authentication type. |
| --appCodeAuthT ype | String | oauth2 | The application code authentication type. |
| --customAuth | Struct | {} | The custom authentication configuration. |
| ---authRequestH eader | String | \[\] | The list of authentication request headers. |
| ---authResponse Header | String | \[\] | The list of authentication response headers. |
| ---authServerHos t | String | auth.example.com | The authentication server host. |
| ---authServerUri | String | /oauth/token | The authentication server URI. |
| ---authTimeout | Integer | 30000 | The authentication timeout period, in milliseconds. |
| ---keepAlive | Integer | 60 | The keep-alive duration, in seconds. |
| ---tokenExpiratio n | Integer | 7200 | The token expiration time, in seconds. |
| ---authAssertTyp e | String | header | The authentication assertion type. |
| ---authAssertVal ue | String | Bearer token | The authentication assertion value. |
| ---openLoosePatt ern | Boolean | false | Indicates whether to enable loose mode. |
| ---cachedClient | Map | {} | The cached client information. |
| --apiKey | Struct | {} | The API key configuration. |
| ---enableInHead er | Boolean | true | Indicates whether to enable the API key in the request header. |
| ---enableInQuery | Boolean | true | Indicates whether to enable the API key in query parameters. |
| ---apiKeyName | String | my-api-key | The API key name. |
| ---enableRmPara m | Boolean | false | Indicates whether to remove the parameter. |
| ---enableOptions FreeAuth | Boolean | true | Indicates whether to exempt OPTIONS requests from authentication. |
| -crossConfig | Struct | {} | The cross-domain configuration. |
| --allowedMetho ds | String | \[\] | The list of allowed request methods. |
| --isOpenCross | Boolean | true | Indicates whether to enable cross-domain requests. |
| --crossType | String | CORS | The cross-domain type. |
| --allowedOrigins | String | \* | The allowed origin domain names. |
| --exposedHeade rs | String | X-Custom-Header,X-Request-Id | The exposed response headers. |
| --allowedHeader s | String | Content-Type,Authorization | The allowed request headers. |
| --allowedCreden tials | Boolean | true | Indicates whether to allow credentials. |
| --maxAge | Integer | 3600 | The maximum cache duration, in seconds. |
| --callbackFunc | String | handleCallback | The name of the callback function. |
| -responseCach eConfig | Struct | {} | The response cache configuration. |
| --routeInterface List | Array | \[\] | The list of route interfaces. |
| ---method | String | GET | The request method. |
| ---headers | String | Content-Type: application/json | The request headers. |
| ---path | String | /api/v1/resource | The path. |
| ---queryParams | String | page=1&amp;size=10 | The query parameter string. |
| --maxAge | Integer | 3600 | The maximum cache duration, in seconds. |
| --isOpenCacheC ontrol | Boolean | true | Indicates whether to enable cache control. |
| --allowedStatus Code | String | 200,201,204 | The allowed status codes. |
| --isOpenRespon seCache | Boolean | true | Indicates whether to enable response caching. |
| -routeIpBlockC onfigVO | Struct | {} | The route IP address blocking configuration. |
| --ipBlockRules | Array | \[\] | The list of IP address blocking rules. |
| ---ip | String | 192.168.1.100 | The IP address. |
| ---policy | String | allow | The policy. |
| --isOpenIpBlock | Boolean | false | Indicates whether to enable IP address blocking. |
| -routeACLConfi g | Struct | {} | The route access control configuration. |
| --aclRules | Array | \[\] | The list of access control rules. |
| ---group | String | default-group | The group. |
| ---policy | String | allow | The policy. |
| --isEnableACL | Boolean | true | Indicates whether to enable access control. |
| -routeTracingC onfig | Struct | {} | The route tracing configuration. |
| --traceHeader | String | X-Trace-Id | The tracing request header. |
| --isEnableDown stream | Boolean | true | Indicates whether to enable downstream tracing. |
| --isEnableTracin g | Boolean | true | Indicates whether to enable tracing. |

<a id="section-3-4-8"></a>

### 3.4.8. GetProtocolByRoute

Queries the protocol of a route.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| type | Integ er | Body | No | 1 | The type. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data |

<a id="section-3-4-9"></a>

### 3.4.9. ModifyRoute

Modifies a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| order | Integ er | Body | No | 100 | The priority of the route.A smaller value indicates a higher priority. This parameter is used in scenarios where multiple routes may match the same request. |
| filters | Strin g | Body | No | \[{"name":"jwtAuthFilter"}, {"name":"rateLimitFilter "}\] | The filter chain associated with the route. This is typically a JSON string that defines various plugins in the request processing flow, such as authentication and rate limiting. |
| routeId | Strin g | Body | No | rt-a1b2c3d4e5f6 | The unique ID of the route to modify. |
| routeNam e | Strin g | Body | No | User Service V2 Ingress | A human-readable name for the route. This makes the route easy to identify and manage. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceTy pe | Strin g | Body | No | HTTP | The type of the backend service, such as HTTP or GRPC. |
| gwInstanc eId | Strin g | Body | No | gw-prod-cluster-01 | The ID of the gateway instance to which the route belongs. |
| methods | Repe atList | Body | No | \["GET", "POST"\] | A list of HTTP methods that the route matches, such as GET and POST. |
| header | Repe atList | Body | No | \[{"key":"X-Version", "value":"v2"}\] | A list of request header conditions for the route to match. This is used to implement header-based routing. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| cookie | Repe atList | Body | No | \[{"key":"user-group", "value":"canary"}\] | A list of cookie conditions for the route to match. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| queryPara m | Repe atList | Body | No | \[{"key":"env", "value":"test"}\] | A list of URL query parameter conditions for the route to match. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| domainIds | Repe atList | Body | No | \["dm-api-example-com"\] | A list of domain name IDs for the route to match. The Host header of the request must match one of these IDs. |
| routePath | Repe atList | Body | No | \["/api/v2/users/\*"\] | A list of URL path patterns for the route to match. The asterisk (\*) wildcard character is supported. |
| stripPrefix | Integ er | Body | No | 2 | If openStripPrefix is set to true, this parameter specifies the number of path levels to strip before forwarding the request to the backend service. For example, if the path is /api/v2/users and stripPrefix is 2, the backend service receives /users. |
| requestTi meout | Integ er | Body | No | 5000 | The timeout period for the gateway to request the backend service.Unit: milliseconds. |
| openStrip Prefix | Boole an | Body | No | true | Specifies whether to enable the path prefix stripping feature. |
| enableFor ceNonceC heck | Boole an | Body | No | false | Specifies whether to enforce Nonce verification to prevent signature replay attacks. |
| path | Json | Body | No | /api/v1/resource | The path. |
| serviceIds | Repe atList | Body | No | \[{"serviceId":"svc-user-v2-stable", "weight":80}, {"serviceId":"svc-user-v2-canary", "weight":20}\] | (Multi-service/Phased release mode) A list of target services and their weights for routing. The sum of the weights for all services must be 100. |
| -serviceId | Strin g | Body | No | service-123456 | The service ID. |
| -weight | Integ er | Body | No | 100 | The weight. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The business return code. A value of 200 indicates that the operation is successful.Other values indicate that the operation failed. |
| msg | String | success | The returned message. If the operation is successful, success is typically returned. |
| data | String | rt-a1b2c3d4e5f6 | The returned data. If the operation is successful, the ID of the modified route is typically returned. |

<a id="section-3-4-10"></a>

### 3.4.10. DeleteRoute

Deletes a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-4-11"></a>

### 3.4.11. ChangeRouteStatus

Changes the status of a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| enableStat us | Bool ean | Body | No | true | The enabled status of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

<a id="section-3-5"></a>

## 3.5. Source Management

<a id="section-3-5-1"></a>

### 3.5.1. ListSources

Queries a list of sources.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --sourceId | String | src-123456 | The source ID. |
| --sourceName | String | Internal System | The source name. |
| --sourceType | Integer | 1 | The source type. |
| --sourceTypeNa me | String | Kubernetes | The name of the source type. |
| --description | String | This is an example service. | The description. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-5-2"></a>

### 3.5.2. ListAllSources

Queries a list of all sources.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Name | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -sourceId | String | src-123456 | The ID of the source. |
| -sourceName | String | Internal system | The name of the source. |
| -sourceType | Integer | 1 | The type of the source. |
| -sourceTypeNa me | String | Kubernetes | The name of the source type. |
| -sourceStruct | Map | {} | The structure of the source. |
| code | Integer | 200 | The response code. |
| msg | String | The operation is successful. | The message. |

<a id="section-3-5-3"></a>

### 3.5.3. GetSource

Queries a source.

**Request headers**

This operation uses common request headers and does not have special request headers. For more information, see the document on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -sourceId | String | src-123456 | The ID of the source. |
| -sourceName | String | Internal System | The name of the source. |
| -sourceType | Integer | 1 | The type of the source. |
| -sourceTypeNa me | String | Kubernetes | The name of the source type. |
| -sourceStruct | Map | {} | The structure of the source. |
| -description | String | This is a sample service. | The description. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |

<a id="section-3-5-4"></a>

### 3.5.4. CreateSource

Creates a source.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| sourceNa me | Strin g | Body | No | Internal System | The name of the source. |
| host | Strin g | Body | No | api.example.com | The host address. |
| port | Integ er | Body | No | 8080 | The port number. |
| username | Strin g | Body | No | zhangsan | The username. |
| password | Strin g | Body | No | \*\*\*\*\*\*\*\* | The password. |
| description | Strin g | Body | No | This is an example service. | The description. |
| sourceTyp e | Integ er | Body | No | 1 | The type of the source. |
| sourceStru ct | Json | Body | No | {} | The structure of the source. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-5-5"></a>

### 3.5.5. ModifySource

Modifies a source.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |
| sourceStru ct | Json | Body | No | {} | The source structure. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| sourceTyp e | Integ er | Body | No | 1 | The source type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-5-6"></a>

### 3.5.6. DeleteSource

Deletes a source.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-5-7"></a>

### 3.5.7. BatchDeleteSource

Deletes sources in batches.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| sourceIds | Repe atLis t | Body | No | \[\] | A list of resource IDs. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data. |
| -successIds | String | \[\] | The successful IDs. |
| -failedIds | String | \[\] | A list of IDs of the sources that failed to be deleted. |

<a id="section-3-6"></a>

## 3.6. Service Management

<a id="section-3-6-1"></a>

### 3.6.1. ListServices

Queries a list of services.

**Request headers**

This operation uses common request headers and does not require any special request headers. For more information, see the Common Parameters document.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --nodes | Array | \[\] | The list of nodes. |
| ---ip | String | 192.168.1.100 | The IP address. |
| ---port | Integer | 8080 | The port number. |
| ---weight | Integer | 100 | The weight. |
| ---enable | Boolean | true | Indicates whether the node is enabled. |
| --serviceId | String | service-123456 | The service ID. |
| --name | String | my-resource | The name. |
| --upstreamType | Integer | 1 | The upstream type. |
| --serviceType | Integer | REST | The service type. |
| --upstreamType Name | String | HTTP Service | The name of the upstream type. |
| --serviceProtoco l | String | HTTP | The service protocol. |
| --sourceId | String | src-123456 | The source ID. |
| --sourceName | String | Internal System | The source name. |
| --sourceType | Integer | 1 | The source type. |
| --sourceTypeNa me | String | Kubernetes | The name of the source type. |
| --createTime | String | 2024-10-14 08:00:00 | The time when the service was created. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The number of the returned page. |

<a id="section-3-6-2"></a>

### 3.6.2. ListAllServices

Queries the list of all services.

**Request header**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -serviceId | String | service-123456 | The ID of the service. |
| -serviceName | String | user-service | The name of the service. |
| -protocol | String | HTTP | The protocol. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-6-3"></a>

### 3.6.3. GetService

Retrieves the details of a service.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a1700 | The ID of the gateway instance. |
| serviceId | Strin g | Body | No | bailian | The service ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -zones | String | \[\] | The list of zones. |
| -routeList | Array | \[\] | The list of routes. |
| --routePath | String | /api/v1/users | The route path. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |
| -strategyConfig s | Array | \[\] | The list of policy configurations. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --strategyConfig Id | String | strategy-config-001 | The policy configuration ID. |
| --strategyConfig Name | String | Default Policy | The policy configuration name. |
| --strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | \[\] | The list of authorization scopes. |
| ---routeInfos | Array | \[\] | The list of route information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | \[\] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | \[\] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | \[\] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---mcpServerInfo s | Array | \[\] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -serviceId | String | service-123456 | The service ID. |
| -name | String | my-resource | The name. |
| -serviceName | String | user-service | The service name. |
| -description | String | This is a sample service. | The description. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -protocol | String | HTTP | The protocol. |
| -serviceType | Integer | REST | The service type. |
| -upstreamType | Integer | 1 | The upstream type. |
| -upstreamType Name | String | HTTP service | The name of the upstream type. |
| -loadBalanceTy pe | Integer | 1 | The load balancing type. |
| -loadBalanceTy peName | String | Polling | The name of the load balancing type. |
| -sourceType | Integer | 1 | The source type. |
| -serviceSource Type | Integer | 1 | The service source type. |
| -serviceStruct | Map | {} | The service structure. |
| -isOpenHealthC heck | Boolean | true | Indicates whether health checks are enabled. |
| -healthCheckSt ruct | Struct | {} | The health check configuration. |
| --type | Integer | 1 | The type. |
| --healthPath | String | /health | The health check path. |
| --httpStatuses | String | 200,201,204 | The HTTP status codes. |
| --timeout | Integer | 30000 | The timeout period. Unit: milliseconds. |
| --healthInterval | Integer | 30 | The health check interval. Unit: seconds. |
| --unHealthInterv al | Integer | 10 | The unhealthy check interval. Unit: seconds. |
| --httpSuccesses | Integer | 3 | The number of consecutive successful HTTP checks. |
| --httpFailures | Integer | 5 | The number of consecutive failed HTTP checks. |

<a id="section-3-6-4"></a>

### 3.6.4. CreateService

Creates a service.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| description | Strin g | Body | No | This is an example service. | The description of the service. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |
| name | Strin g | Body | No | my-resource | The name. |
| upstreamT ype | Integ er | Body | No | 1 | The type of the upstream service. |
| serviceSou rceType | Integ er | Body | No | 1 | The source type of the service. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| loadBalanc eType | Integ er | Body | No | 1 | The type of load balancing. |
| serviceStr uct | Json | Body | No | {} | The structure of the service. |
| isOpenHea lthCheck | Bool ean | Body | No | true | Specifies whether to enable health checks. |
| healthChe ckStruct | Json | Body | No | {} | The health check configuration. |
| protocol | Strin g | Body | No | HTTP | The protocol. |
| serviceId | Strin g | Body | No | service-123456 | The ID of the service. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-6-5"></a>

### 3.6.5. ModifyService

This operation modifies a service.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| name | Strin g | Body | No | my-resource | The name. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| upstreamT ype | Integ er | Body | No | 1 | The upstream type. |
| serviceSou rceType | Integ er | Body | No | 1 | The service source type. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |
| loadBalanc eType | Integ er | Body | No | 1 | The load balancing type. |
| serviceStr uct | Json | Body | No | {} | The service structure. |
| isOpenHea lthCheck | Bool ean | Body | No | true | Specifies whether to enable health checks. |
| healthChe ckStruct | Json | Body | No | {} | The health check configuration. |
| protocol | Strin g | Body | No | HTTP | The protocol. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-6-6"></a>

### 3.6.6. ModifyNode

Modifies a service node.

**Request headers**

This operation uses only common request headers. For more information, see the document about common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceSou rceType | Integ er | Body | No | 1 | The source type of the service. |
| serviceStr uct | Json | Body | No | {} | The service structure. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-6-7"></a>

### 3.6.7. DeleteService

Deletes a service.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request syntax**

```http
POST /microservice/deleteService HTTP/1.1
```

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | test-service | The instance ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

**Examples**

Sample request

```http
POST /microservice/deleteService HTTP/1.1
{

}
```

Sample successful response

`JSON`  format

```json
{
 "msg":"",
 "code":"",
 "data":""
}
```

<a id="section-3-6-8"></a>

### 3.6.8. BatchDeleteService

Deletes multiple services at a time.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceIds | Repe atLis t | Body | No | \[\] | A list of service IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The Data. |
| -successIds | String | \[\] | List of success IDs. |
| -failedIds | String | \[\] | List of failed IDs. |

<a id="section-3-6-9"></a>

### 3.6.9. ImportServices

This operation imports services.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| description | Strin g | Body | No | This is a sample service | The description. |
| loadBalanc eType | Integ er | Body | No | 1 | The load balancing type. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| sourceNa mespaceId | Strin g | Body | No | ns-source-001 | The ID of the source namespace. |
| groupNam e | Strin g | Body | No | Default Group | The group name. |
| port | Integ er | Body | No | 8080 | The port number. |
| serviceList | Repe atLis t | Body | No | \[\] | The list of services. |
| protocol | Strin g | Body | No | HTTP | The protocol. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| data | String | {} | The data. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The messages |

<a id="section-3-7"></a>

## 3.7. Consumer management

<a id="section-3-7-1"></a>

### 3.7.1. ListApps

Queries a list of consumers.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| appName | Strin g | Body | No | Sample Application | The application name. |
| appTags | Strin g | Body | No | \[\] | The list of application tags. |
| authType | Strin g | Body | No | jwt | The authentication type. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| email | Strin g | Body | No | admin@example.com | The email address. |
| status | Integ er | Body | No | 1 | The status. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| appType | Integ er | Body | No | 1 | The application type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --ipWhiteList | String | \[\] | The IP address whitelist. |
| --groups | String | \[\] | The list of groups. |
| --appTags | Array | \[\] | The list of application tags. |
| --appId | String | 12345678 | The application ID. |
| --appName | String | Sample Application | The application name. |
| --appAddress | String | https://example.co m | The application address. |
| --useAuth | Boolean | true | Indicates whether authentication is used. |
| --authType | Integer | jwt | The authentication type. |
| --authTypeNam e | String | JWT | The name of the authentication type. |
| --useWhiteList | Boolean | true | Indicates whether a whitelist is used. |
| --description | String | This is a sample service. | The description. |
| --chargePerson Name | String | Zhang San | The name of the owner. |
| --createBy | Integer | 1001 | The ID of the user who created the application. |
| --createTime | String | 2024-10-14 08:00:00 | The time when the application was created. |
| --updateBy | Integer | 1001 | The modifier ID. |
| --updateTime | String | 2024-10-14 15:00:00 | The time when the application was last updated. |
| --userId | String | uid-123456 | The user ID. |
| --userName | String | Zhang San | The username. |
| --delFlag | String | 0 | The deletion flag. |
| --isDisable | Boolean | false | Indicates whether the application is disabled. |
| --enable | Boolean | true | Indicates whether the application is enabled. |
| --timeOut | Boolean | false | Indicates whether the request timed out. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

<a id="section-3-7-2"></a>

### 3.7.2. ListAppsByGwInstanceId

Queries a list of applications by gateway instance ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -groups | String | \[\] | The list of groups. |
| -appTags | Array | \[\] | The list of application tags. |
| -strategyConfig s | Array | \[\] | The list of policy configurations. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --strategyConfig Id | String | strategy-config-001 | The policy configuration ID. |
| --strategyConfig Name | String | Default Policy | The policy configuration name. |
| --strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -appId | String | 12345678 | The application ID. |
| -appName | String | Sample Application | The application name. |
| -useAuth | Boolean | true | Indicates whether authentication is used. |
| -authType | Integer | jwt | The authentication type. |
| -requestHeader | String | Content-Type | The request header. |
| -authTypeNam e | String | JWT | The name of the authentication type. |
| -ipWhiteList | String | \[\] | The IP whitelist. |
| -useWhiteList | Boolean | true | Indicates whether the whitelist is used. |
| -description | String | This is a sample service. | The description. |
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9... | The token. |
| -appSecret | String | as_abcdefghijklmn op | The application ciphertext. |
| -isDisable | Boolean | false | is disabled |
| -enable | Boolean | true | Indicates whether the application is enabled. |
| -key | String | api-key-001 | The key. |
| -password | String | \*\*\*\*\*\*\*\* | The password. |
| -expireTime | Integer | 2025-10-14 23:59:59 | The expiration time. |
| -appCode | String | APP20240101 | The application code. |
| -accessKey | String | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| -secretKey | String | sk_1234567890abc def | The secret key. |
| -payload | Struct | {} | The request payload. |
| --subject | String | CN=example.com | The certificate subject. |
| --issuer | String | https://auth.examp le.com | The issuer. |
| -oauth2Payload | Struct | {} | The OAuth2 payload. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --authorizationC ode | Boolean | true | Indicates whether the authorization code grant is enabled. |
| --clientCredenti als | Boolean | true | Indicates whether the client credentials grant is enabled. |
| --implicitGrant | Boolean | false | Indicates whether the implicit grant is enabled. |
| --passwordGran t | Boolean | true | Indicates whether the password grant is enabled. |
| --tokenExpiratio n | Integer | 7200 | The token expiration time, in seconds. |
| --refreshTokenE xpiration | Integer | 86400 | The refresh token expiration time, in seconds. |
| --clientId | String | client_123456 | The client ID. |
| --clientSecret | String | secret_abc123 | The client secret. |
| --redirectUris | String | https://example.co m/callback | The redirection URI. |
| --pkce | Boolean | true | Indicates whether PKCE is enabled. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-7-3"></a>

### 3.7.3. GetApp

Queries a consumer.

**Request headers**

This operation uses only common request headers. For more information, see the Common parameters document.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -groups | String | \[\] | The list of groups. |
| -appTags | Array | \[\] | The list of application tags. |
| -strategyConfig s | Array | \[\] | The list of policy configurations. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --strategyConfig Id | String | strategy-config-001 | The ID of the policy configuration. |
| --strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| --strategyName | String | Throttling Policy | The name of the policy. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | \[\] | The list of authorization scopes. |
| ---routeInfos | Array | \[\] | The list of routing information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | \[\] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | \[\] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | \[\] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---mcpServerInfo s | Array | \[\] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -appId | String | 12345678 | The ID of the application. |
| -appName | String | Sample Application | The name of the application. |
| -useAuth | Boolean | true | Indicates whether authentication is enabled. |
| -authType | Integer | jwt | The authentication type. |
| -requestHeader | String | Content-Type | The request header. |
| -authTypeNam e | String | JWT | The name of the authentication type. |
| -ipWhiteList | String | \[\] | The IP whitelist. |
| -useWhiteList | Boolean | true | Indicates whether the whitelist is enabled. |
| -description | String | This is a sample service. | The description. |
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9... | The token. |
| -appSecret | String | as_abcdefghijklmn op | The application secret. |
| -isDisable | Boolean | false | Indicates whether the application is disabled. |
| -enable | Boolean | true | Indicates whether the application is enabled. |
| -key | String | api-key-001 | The key. |
| -password | String | \*\*\*\*\*\*\*\* | The password. |
| -expireTime | Integer | 2025-10-14 23:59:59 | The expiration time. |
| -appCode | String | APP20240101 | The application code. |
| -accessKey | String | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| -secretKey | String | sk_1234567890abc def | The AccessKey secret. |
| -payload | Struct | {} | The request payload. |
| --subject | String | CN=example.com | The subject of the certificate. |
| --issuer | String | https://auth.examp le.com | The issuer of the certificate. |
| -oauth2Payload | Struct | {} | The OAuth 2.0 payload. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --authorizationC ode | Boolean | true | Indicates whether the authorization code grant is enabled. |
| --clientCredenti als | Boolean | true | Indicates whether the client credentials grant is enabled. |
| --implicitGrant | Boolean | false | Indicates whether the implicit grant is enabled. |
| --passwordGran t | Boolean | true | Indicates whether the password grant is enabled. |
| --tokenExpiratio n | Integer | 7200 | The validity period of the token, in seconds. |
| --refreshTokenE xpiration | Integer | 86400 | The validity period of the refresh token, in seconds. |
| --clientId | String | client_123456 | The client ID. |
| --clientSecret | String | secret_abc123 | The client secret. |
| --redirectUris | String | https://example.co m/callback | The redirection URI. |
| --pkce | Boolean | true | Indicates whether Proof Key for Code Exchange (PKCE) is enabled. |

<a id="section-3-7-4"></a>

### 3.7.4. CreateApp

Creates a consumer.

**Request headers**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | \*\*\*\*\*\*\*\* | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as_abcdefghijklmnop | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |
| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | \[\] | The IP whitelist. |
| appName | Strin g | Body | No | SampleApp | The application name. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | ZhangSan | The username. |
| appKey | Strin g | Body | No | ak_1234567890abcdef | The application key. |
| groups | Repe atLis t | Body | No | \[\] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |
| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| secretKey | Strin g | Body | No | sk_1234567890abcdef | The secret key. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-7-5"></a>

### 3.7.5. ModifyApp

Modifies a consumer.

**Request header**

This operation uses common request headers. For more information, see the topic on common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | \*\*\*\*\*\*\*\* | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as_abcdefghijklmnop | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |
| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | \[\] | The IP address whitelist. |
| appName | Strin g | Body | No | ExampleApp | The application name. |
| description | Strin g | Body | No | This is an example service. | The description. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| appKey | Strin g | Body | No | ak_1234567890abcdef | The application key. |
| groups | Repe atLis t | Body | No | \[\] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |
| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| secretKey | Strin g | Body | No | sk_1234567890abcdef | The AccessKey secret. |
| appAddres s | Strin g | Body | No | https://example.com | The application address. |
| appTagsSt r | Strin g | Body | No | tag1,tag2,tag3 | A string of application tags. |
| chargePers onName | Strin g | Body | No | Zhang San | The name of the owner. |
| openCross | Bool ean | Body | No | true | Specifies whether to enable cross-domain requests. |
| allowedOri gins | Strin g | Body | No | \* | The allowed source domain names. |
| allowedHe aders | Strin g | Body | No | Content-Type,Authorization | The allowed request headers. |
| allowedMe thods | Strin g | Body | No | \[\] | The list of allowed request methods. |
| isDisable | Bool ean | Body | No | false | Specifies whether to disable the application. |
| appType | Integ er | Body | No | 1 | The application type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The returned message. |
| data | String | {} | The data |

<a id="section-3-7-6"></a>

### 3.7.6. DeleteApp

Deletes a consumer.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-7-7"></a>

### 3.7.7. ModifyAppOpenStatus

Enables or disables a consumer application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| enable | Bool ean | Body | No | true | Specifies whether to enable the application. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

<a id="section-3-7-8"></a>

### 3.7.8. ModifyAppWhiteListStatus

Modifies the status of a consumer whitelist.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| isOpen | Bool ean | Body | No | true | Specifies whether to enable the whitelist. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-7-9"></a>

### 3.7.9. GetAppAuth

Queries the authorization for a consumer.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| authId | Strin g | Body | No | auth_123456 | The authentication ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -authId | Integer | auth_123456 | The authentication ID. |
| -appId | String | 12345678 | The application ID. |
| -routeId | String | route-123456 | The route ID. |
| -routePath | String | /api/v1/users | The route path. |
| -serviceId | Integer | service-123456 | The service ID. |
| -serviceName | String | user-service | The service name. |
| -serviceProtoco l | String | HTTP | The service protocol. |
| -authStatus | Integer | 1 | The authentication status. |

<a id="section-3-7-10"></a>

### 3.7.10. CreateAppAuth

Creates a consumer authorization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| body | Strin g | Body | No | {"key":"value"} | The request body. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| Code | Integer | 200 | The response code. |
| Msg | String | Operation successful | The response message. |
| Data | String | {} | The data. |

<a id="section-3-7-11"></a>

### 3.7.11. BatchCreateAppAuthByRoute

Grants batch authorization to consumers.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| routeId | Repe atLis t | Body | No | route-123456 | The ID of the route. |
| authStatus | Integ er | Body | No | 1 | The authentication status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

<a id="section-3-7-12"></a>

### 3.7.12. ModifyAppAuthStatus

Modifies the authorization status of a consumer.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| authId | Strin g | Body | No | auth_123456 | The authorization ID. |
| authStatus | Integ er | Body | No | 1 | The authorization status. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -id | Integer | 123456 | The ID. |
| -createBy | Integer | 1001 | The ID of the user who created the resource. |
| -updateBy | Integer | 1001 | The ID of the user who last updated the resource. |
| -appId | String | 12345678 | The application ID. |
| -authId | String | auth_123456 | The authorization ID. |
| -routeId | String | route-123456 | The routing ID. |
| -authStatus | Integer | 1 | The authorization status. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |

<a id="section-3-7-13"></a>

### 3.7.13. DeleteAppAuth

Deletes a consumer authorization.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| authId | Strin g | Body | No | auth_123456 | The authorization ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

<a id="section-3-7-14"></a>

### 3.7.14. RefreshToken

Refreshes a token.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | \*\*\*\*\*\*\*\* | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as_abcdefghijklmnop | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |
| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | \[\] | The IP whitelist. |
| appName | Strin g | Body | No | Sample Application | The application name. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| appKey | Strin g | Body | No | ak_1234567890abcdef | The application key. |
| groups | Repe atLis t | Body | No | \[\] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |
| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| secretKey | Strin g | Body | No | sk_1234567890abcdef | The secret key. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

<a id="section-3-7-15"></a>

### 3.7.15. ResetSecretKey

Resets a secret key.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Boolean | {} | The data |

<a id="section-3-7-16"></a>

### 3.7.16. HandlerConsumerAuth

Queries the authentication information for a consumer.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| isOpen | Bool ean | Body | No | true | Specifies whether the feature is enabled. |
| name | Strin g | Body | No | my-resource | The name. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

<a id="section-3-7-17"></a>

### 3.7.17. CreateAppAuthByRoute

Create a consumer authorization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| authStatus | Integ er | Body | No | 1 | The authorization status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation is successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-7-18"></a>

### 3.7.18. BatchDeleteApp

Deletes consumers in a batch.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| appIds | Repe atLis t | Body | No | \[\] | A list of application IDs. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -successIds | String | \[\] | Successful IDs |
| -failedIds | String | \[\] | Failed IDs |

<a id="section-3-8"></a>

## 3.8. Plugin Management

<a id="section-3-8-1"></a>

### 3.8.1. ListPlugins

Queries a list of plugins.

**Request header**

This operation has no special request headers. For more information about common request headers, see the common request parameters document.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| searchNa me | Strin g | Body | No | search keyword | The name to search for. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --config | Array | \[\] | The list of configurations. |
| ---name | String | my-resource | The name. |
| ---required | Boolean | true | Indicates whether the parameter is required. |
| --pluginId | String | plugin-123456 | The plugin ID. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --pluginName | String | rate-limiter | The plugin name. |
| --description | String | This is an example service. | The description. |
| --downloadURL | String | https://example.co m/download/file.zip | The download URL. |
| --type | Integer | 1 | The type. |
| --used | Boolean | false | Indicates whether the plugin is used. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-8-2"></a>

### 3.8.2. ListOpenPlugins

Lists the open plugins.

**Request headers**

This operation uses only the common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| searchNa me | Strin g | Body | No | Search keyword | The search keyword. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -config | Array | \[\] | The list of configurations. |
| --name | String | my-resource | The name. |
| --required | Boolean | true | Indicates whether the parameter is required. |
| -pluginId | String | plugin-123456 | The plugin ID. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -pluginName | String | rate-limiter | The plugin name. |
| -description | String | This is a sample service. | The description. |
| -downloadURL | String | https://example.co m/download/file.zip | The download URL. |
| -type | Integer | 1 | The type. |
| -used | Boolean | false | Indicates whether the plugin is used. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-8-3"></a>

### 3.8.3. ListGlobalPlugins

Retrieves a list of global plugins.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| searchNa me | Strin g | Body | No | A search keyword | Search by name. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --pluginId | String | plugin-123456 | The ID of the plugin. |
| --routePluginId | String | plugin-route-001 | The ID of the routing plugin. |
| --pluginName | String | rate-limiter | The name of the plugin. |
| --config | String | \[\] | The list of configurations. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The time when the plugin was created. |
| --updateTime | String | 2024-10-14 15:00:00 | The time when the plugin was last updated. |
| --order | Integer | 100 | The sort number. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-8-4"></a>

### 3.8.4. ListRoutePlugins

Queries a list of routing plugins.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | Size |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The routing ID. |
| searchNa me | Strin g | Body | No | Search keyword | Search by name |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| --routeId | String | route-123456 | The routing ID. |
| --pluginId | String | plugin-123456 | The plugin ID. |
| --routePluginId | String | plugin-route-001 | The routing plugin ID. |
| --pluginName | String | rate-limiter | The plugin name. |
| --config | String | \[\] | The list of configurations. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --order | Integer | 100 | The sort number. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-8-5"></a>

### 3.8.5. GetPlugin

Retrieves a plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -config | Array | \[\] | The list of configurations. |
| --name | String | my-resource | The name. |
| --required | Boolean | true | Indicates whether the parameter is required. |
| -pluginId | String | plugin-123456 | The plugin ID. |
| -gwInstanceId | String | i-c0a81bb16a1524a 17 | The gateway instance ID. |
| -pluginName | String | rate-limiter | The plugin name. |
| -description | String | This is a sample service. | Description. |
| -downloadURL | String | https://example.co m/download/file.zip | The download URL. |
| -type | Integer | 1 | The type. |
| -used | Boolean | false | Indicates whether the plugin is used. |

<a id="section-3-8-6"></a>

### 3.8.6. CreatePlugin

Creates a plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginNam e | Strin g | Body | No | rate-limiter | The plugin name. |
| description | Strin g | Body | No | This is an example service. | The description. |
| downloadU RL | Strin g | Body | No | https://example.com/dow nload/file.zip | The download URL. |
| config | Repe atLis t | Body | No | \[\] | The configuration list. |
| -name | Strin g | Body | No | my-resource | The name. |
| -required | Bool ean | Body | No | true | Specifies whether the configuration is required. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-7"></a>

### 3.8.7. CreateGlobalPlugin

Creates a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| order | Integ er | Body | No | 100 | The sorting number. |
| status | Bool ean | Body | No | 1 | The status. |
| config | Strin g | Body | No | \[\] | The list of configurations. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-8"></a>

### 3.8.8. CreateRoutePlugin

Creates a routing plugin.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| order | Integ er | Body | No | 100 | The order number. |
| status | Bool ean | Body | No | 1 | The status. |
| config | Strin g | Body | No | \[\] | The list of configurations. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-9"></a>

### 3.8.9. ModifyPlugin

Modifies a plugin.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| downloadU RL | Strin g | Body | No | https://example.com/dow nload/file.zip | The download URL. |
| config | Repe atLis t | Body | No | \[\] | A list of configurations. |
| -name | Strin g | Body | No | my-resource | The name. |
| -required | Bool ean | Body | No | true | Specifies whether the configuration is required. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-10"></a>

### 3.8.10. ModifyGlobalPlugin

Modifies a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The routing plugin ID. |
| order | Integ er | Body | No | 100 | The order number. |
| config | Strin g | Body | No | \[\] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | String | {} | The data. |

<a id="section-3-8-11"></a>

### 3.8.11. ModifyRoutePlugin

Modifies a routing plugin.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the routing plugin. |
| order | Integ er | Body | No | 100 | The order number. |
| config | Strin g | Body | No | \[\] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-12"></a>

### 3.8.12. DeletePlugin

Deletes a plugin.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-8-13"></a>

### 3.8.13. DeleteGlobalPlugin

Deletes a global plugin.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the routing plugin. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-14"></a>

### 3.8.14. DeleteRoutePlugin

Deletes a route plugin.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the route plugin. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

<a id="section-3-8-15"></a>

### 3.8.15. ModifyGlobalPluginStatus

Modifies the status of a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The routing plugin ID. |
| order | Integ er | Body | No | 100 | The sort number. |
| config | Strin g | Body | No | \[\] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-16"></a>

### 3.8.16. ModifyRoutePluginStatus

Modifies the status of a route plugin.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The route plugin ID. |
| order | Integ er | Body | No | 100 | The sort number. |
| config | Strin g | Body | No | \[\] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-8-17"></a>

### 3.8.17. ListPluginUsage

Queries the usage of plugins.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The list of records. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |
| --status | Boolean | 1 | The status. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-9"></a>

## 3.9. Policy Management

<a id="section-3-9-1"></a>

### 3.9.1. ModifyStrategyConfig

Modifies a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| strategyCo nfigName | Strin g | Body | No | DefaultPolicy | The name of the policy configuration. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
| strategyNa me | Strin g | Body | No | ThrottlingPolicy | The policy name. |
| config | Json | Body | No | \[\] | The list of configurations. |
| rawConfig | Strin g | Body | No | {"timeout":30} | Original configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The routing ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |
| routeIds | Repe atLis t | Body | No | \[\] | The list of routing IDs. |
| serviceIds | Repe atLis t | Body | No | \[\] | The list of service IDs. |
| appIds | Repe atLis t | Body | No | \[\] | The list of application IDs. |
| domainIds | Repe atLis t | Body | No | \[\] | The list of domain IDs. |
| mcpIds | Repe atLis t | Body | No | \[\] | The list of MCP IDs. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-9-2"></a>

### 3.9.2. CreateStrategyConfig

Creates a strategy configuration.

**Request header**

This operation uses common request headers and requires no special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter Name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| strategyCo nfigName | Strin g | Body | No | Default Policy | The name of the strategy configuration. |
| strategyNa me | Strin g | Body | No | default | The name of the policy. |
| config | Json | Body | No | \[\] | The list of configurations. |
| rawConfig | Strin g | Body | No | {"timeout":30} | The raw configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| mcpServer Id | Strin g | Body | No | mcp-server-001 | The ID of the MCP server. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |
| routeIds | Repe atLis t | Body | No | \[\] | A list of route IDs. |
| serviceIds | Repe atLis t | Body | No | \[\] | A list of service IDs. |
| appIds | Repe atLis t | Body | No | \[\] | A list of application IDs. |
| domainIds | Repe atLis t | Body | No | \[\] | A list of domain IDs. |
| mcpIds | Repe atLis t | Body | No | \[\] | A list of MCP IDs. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the strategy configuration. |

**Response parameters**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message |
| data | String | {} | The data. |

<a id="section-3-9-3"></a>

### 3.9.3. ListStrategies

Queries a list of policies.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size |
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| scope | Strin g | Body | No | openid profile | The authorization scope. |
| strategyNa me | Strin g | Body | No | throttling policy | The policy name. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data. |
| -strategies | Array | \[\] | The list of policies. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --uiStyles | String | \[\] | The list of UI styles. |
| --strategyName | String | throttling policy | The policy name. |
| --strategyTitle | String | Advanced Throttling | The policy title. |
| --description | String | This is an example service. | The description. |
| --supportCascad e | Integer | 1 | Indicates whether cascading is supported. |
| --rawConfigExa mple | String | {"enabled":true} | An example of the raw configuration. |
| --order | Integer | 100 | The order number. |
| --document | String | API operation document | The document. |
| -category | Struct | {} | The category information. |
| --name | String | my-resource | The name. |
| --title | String | API operation title | The title. |
| --order | Integer | 100 | The order number. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-9-4"></a>

### 3.9.4. ListStrategyConfigs

Queries a list of policy configurations.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| strategyCo nfigName | Strin g | Body | No | Default Policy | The name of the policy configuration. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
| strategyNa me | Strin g | Body | No | throttling policy | The name of the policy. |
| scope | Json | Body | No | openid profile | The authorization scope. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message |
| data | Struct | {} | The data |
| -records | Array | \[\] | The list of records. |
| --scopes | String | \[\] | The list of authorization scopes. |
| --strategyConfig Id | String | strategy-config-001 | The ID of the policy configuration. |
| --strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| --strategyName | String | throttling policy | The name of the policy. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | \[\] | The list of authorization scopes. |
| ---routeInfos | Array | \[\] | The list of routing information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | \[\] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | \[\] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | \[\] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---mcpServerInfo s | Array | \[\] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

<a id="section-3-9-5"></a>

### 3.9.5. GetStrategy

Queries a policy.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| strategyNa me | Strin g | Body | No | throttling policy | The name of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -scopes | String | \[\] | The list of authorization scopes. |
| -uiStyles | String | \[\] | The list of UI styles. |
| -strategyName | String | throttling policy | The name of the policy. |
| -strategyTitle | String | Advanced Throttling | The title of the policy. |
| -description | String | This is an example service. | The description. |
| -supportCascad e | Integer | 1 | Indicates whether cascading is supported. |
| -rawConfigExa mple | String | {"enabled":true} | An example of the raw configuration. |
| -order | Integer | 100 | The sort number. |
| -document | String | API operation document | The document. |

<a id="section-3-9-6"></a>

### 3.9.6. GetStrategyConfig

Queries a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -scopes | String | \[\] | A list of authorization scopes. |
| -strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| -strategyConfig Id | String | strategy-config-001 | The ID of the policy configuration. |
| -strategyName | String | Throttling Policy | The name of the policy. |
| -routeId | String | route-123456 | The ID of the route. |
| -routeName | String | user-service-route | The name of the route. |
| -serviceId | String | service-123456 | The ID of the service. |
| -serviceName | String | user-service | The name of the service. |
| -appId | String | 12345678 | The ID of the application. |
| -appName | String | Sample Application | The name of the application. |
| -domainId | String | domain-123456 | The ID of the domain name. |
| -domainName | String | example.com | The domain name. |
| -status | Boolean | 1 | The status. |
| -config | Map | \[\] | A list of configurations. |
| -rawConfig | String | {"timeout":30} | The raw configuration. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -scope | Struct | openid profile | The authorization scope. |
| --scopes | String | \[\] | A list of authorization scopes. |
| --routeInfos | Array | \[\] | A list of route information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --serviceInfos | Array | \[\] | A list of service information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --appInfos | Array | \[\] | A list of application information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --domainInfos | Array | \[\] | A list of domain name information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --mcpServerInfo s | Array | \[\] | A list of MCP server information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |

<a id="section-3-9-7"></a>

### 3.9.7. GetRoutePolicies

Queries routing policies.

**Request headers**

This operation uses common request headers. For more information, see Common parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -rewrite | Struct | {} | The rewrite configuration. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| --path | String | /api/v1/resource | The path. |
| --host | String | api.example.com | The host address. |
| -headerControl | Struct | {} | The request header control configuration. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| --request | Struct | {} | The request structure. |
| ---remove | String | \[\] | The list of items to remove. |
| ---add | Array | \[\] | The list of items to add. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| ---set | Array | \[\] | The list of items to set. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| --response | Struct | {} | The response structure. |
| ---remove | String | \[\] | The list of items to remove. |
| ---add | Array | \[\] | Add a list |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| ---set | Array | \[\] | The list of items to set. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| -timeoutConfig | Struct | {} | The timeout configuration. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| --timeout | Integer | 30000 | The timeout period in milliseconds. |
| -fallbackConfig | Struct | {} | The fallback configuration. |
| --responseCode s | String | \[\] | The list of response codes. |
| --services | Array | \[\] | The list of services. |
| ---name | String | my-resource | The name. |
| ---port | Integer | 8080 | The port number. |
| ---version | String | 1.0.0 | The version number. |
| ---weight | Integer | 100 | The weight. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| --fallbackStrate gy | String | default | The fallback strategy. |

<a id="section-3-9-8"></a>

### 3.9.8. ModifyRoutePolicy

Modifies a routing policy.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| configType | Strin g | Body | No | yaml | The configuration type. |
| configData | Json | Body | No | {} | The configuration data. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-9-9"></a>

### 3.9.9. DeleteStrategyConfig

Deletes a policy configuration.

**Request headers**

This operation uses common request headers and requires no special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data. |

<a id="section-3-9-10"></a>

### 3.9.10. ModifyStrategyConfigStatus

Modifies the status of a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| isOpen | Bool ean | Body | No | true | Specifies whether to enable the policy configuration. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | String | {} | The data |

<a id="section-3-10"></a>

## 3.10. Domain name management

<a id="section-3-10-1"></a>

### 3.10.1. ListDomains

Queries a list of domain names.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 10 | The number of entries to return on each page for a paged query. |
| current | Integ er | Body | No | 1 | Set the page on which the returned results are displayed. The default value is 1, indicating that the display starts on page 1. |
| domain | Strin g | Body | No | www.aliyun.com | The domain name. |
| gwInstanc eId | Strin g | Body | No | i-xxxxxxx | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Code | Integer | 200 | The interface status or POP error code. |
| Msg | String | success | The status description. If \`Code\` is \`200\`, \`Msg\` is usually empty. |
| Data | Struct | {} | The response data. |
| -Records | Array | \[\] | The record that returns the data result. |
| --DomainId | String | 00efd71a-770e-4255-b54e-6fe5659baffe | The domain name ID. |
| --CertificateId | String | 12345678-1234-1234-1234-12345678\*\*\*\* | The certificate ID. |
| --CertificateNam e | String | myCertificate | The name of the SSL certificate. |
| --Domain | String | www.aliyun.com | The domain name. |
| --Protocol | String | HTTP | The protocol type. |
| --CreateTime | String | 2024-03-15T01:46Z | The creation time. |
| --UpdateTime | String | 2024-03-15T01:46Z | The update time. |
| --ClientAuth | Integer | 0 | Indicates whether mutual authentication is enabled. 0: disabled. 1: enabled. |
| --CaCertificateId | String | 00efd71a-770e-4255-b54e-6fe5659baffe | The CA certificate ID. |
| --CaCertificateN ame | String | test | The name of the CA certificate. |
| -Size | Long | 20 | The number of entries on each page. |
| -Total | Long | 1 | The total number of entries. |
| -Current | Long | 1 | The current page number. |

**Examples**

Sample response in  `JSON`  format

```json
{
 "Msg":"success",
 "Data":{
  "Records":[
   {
    "DomainId":"00efd71a-770e-4255-b54e-6fe5659baffe",
    "CertificateId":"12345678-1234-1234-1234-12345678****",
    "CreateTime":"2024-03-15T01:46Z",
    "UpdateTime":"2024-03-15T01:46Z",
    "CertificateName":"myCertificate",
    "Domain":"www.aliyun.com",
    "Protocol":"HTTP",
    "ClientAuth":0,
    "CaCertificateName":"test",
    "CaCertificateId":"00efd71a-770e-4255-b54e-6fe5659baffe"
   }
  ],
  "Size":20,
  "Total":1,
  "Current":1
 },
 "Code":200
}
```

<a id="section-3-10-2"></a>

### 3.10.2. ListAllDomains

Queries a list of all domain names.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The data |
| -domainId | String | domain-123456 | The domain name ID. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -certificateNam e | String | MyCert | The certificate name. |
| -domain | String | api.example.com | The domain name. |
| -protocol | String | HTTP | The protocol. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -clientAuth | Integer | 1 | The client authentication method. |
| -caCertificateId | String | cert-123456 | The CA certificate ID. |
| -caCertificateN ame | String | MyCA | The name of the CA certificate. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-10-3"></a>

### 3.10.3. GetDomain

Queries the details of a domain name.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -routeInfos | Array | \[\] | The list of routing information. |
| --routeId | String | route-123456 | The routing ID. |
| --routeName | String | user-service-route | The routing name. |
| --serviceId | String | service-123456 | The service ID. |
| --serviceName | String | user-service | The service name. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -domainId | String | domain-123456 | The domain name ID. |
| -domain | String | api.example.com | The domain name. |
| -protocol | String | HTTP | The protocol. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -clientAuth | Integer | 1 | The client authentication method. |
| -caCertificateId | String | cert-123456 | The CA certificate ID. |
| -subjectDn | String | CN=example.com, O=Example,C=CN | The subject distinguished name (DN) of the certificate. |
| -issuerDn | String | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

<a id="section-3-10-4"></a>

### 3.10.4. CreateDomain

Creates a domain name.

**Request headers**

This operation uses common request headers and does not use special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| protocol | Strin g | Body | No | HTTP | The protocol. |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| domain | Strin g | Body | No | api.example.com | The domain name. |
| clientAuth | Integ er | Body | No | 1 | The client authentication method. |
| caCertifica teId | Strin g | Body | No | cert-123456 | The CA certificate ID. |
| subjectDn | Strin g | Body | No | CN=example.com,O=Exa mple,C=CN | The subject distinguished name (DN) of the certificate. |
| issuerDn | Strin g | Body | No | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-10-5"></a>

### 3.10.5. ModifyDomain

Modifies a domain name.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| protocol | Strin g | Body | No | HTTP | The protocol. |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| domain | Strin g | Body | No | api.example.com | The domain name. |
| clientAuth | Integ er | Body | No | 1 | The client authentication method. |
| caCertifica teId | Strin g | Body | No | cert-123456 | The CA certificate ID. |
| subjectDn | Strin g | Body | No | CN=example.com,O=Exa mple,C=CN | The subject DN of the certificate. |
| issuerDn | Strin g | Body | No | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-10-6"></a>

### 3.10.6. DeleteDomain

Deletes a domain name.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-11"></a>

## 3.11. Certificate Management

<a id="section-3-11-1"></a>

### 3.11.1. ListCertificates

Retrieves a list of certificates.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| size | Integ er | Body | No | 100 | The size |
| current | Integ er | Body | No | 1 | The current page number. |
| sni | Strin g | Body | No | example.com | The Server Name Indication (SNI) domain name. |
| certType | Integ er | Body | No | 1 | The certificate type. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | \[\] | The record list. |
| --snis | String | \[\] | The list of SNI domain names. |
| --expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --certificateNam e | String | MyCert | The certificate name. |
| --certificateId | String | cert-987654 | The certificate ID. |
| --certType | Integer | 1 | The certificate type. |
| -size | Integer | 100 | The size |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

<a id="section-3-11-2"></a>

### 3.11.2. ListAllServerCertificates

Queries the list of all server certificates.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Map | {} | The data |

<a id="section-3-11-3"></a>

### 3.11.3. ListAllCACertificates

Retrieves the list of all CA certificates.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| data | Array | {} | The Data. |
| -snis | String | \[\] | The list of SNI domain names. |
| -expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -certificateNam e | String | MyCert | The certificate name. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -certType | Integer | 1 | The certificate type. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

<a id="section-3-11-4"></a>

### 3.11.4. GetCertificate

Queries a certificate.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -snis | String | \[\] | The list of SNI domain names. |
| -signTime | String | 2024-10-14 10:30:00 | The time when the certificate was signed. |
| -expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| -algorithm | String | sha256 | The type of the algorithm. |
| -privateKeyLen | Integer | 2048 | The length of the private key. |
| -fingerPrint | String | a1b2c3d4e5f6 | Fingerprint. |
| -signerCN | String | Example Corp | The common name (CN) of the signer. |
| -signerOU | String | IT Department | The organizational unit (OU) of the signer. |
| -certificateNam e | String | MyCert | The certificate name. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -domainId | String | domain-123456 | The domain name ID. |
| -certType | Integer | 1 | The certificate type. |
| -SN | String | SN12345678 | The serial number. |

<a id="section-3-11-5"></a>

### 3.11.5. CreateCertificate

Creates a certificate.

**Request headers**

This operation uses common request headers and no special request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| certificates | Strin g | Body | No | cert1,cert2 | The list of certificates. |
| privateKey | Strin g | Body | No | -----BEGIN PRIVATE KEY----- | The private key. |
| certificate Name | Strin g | Body | No | MyCert | The certificate name. |
| certType | Integ er | Body | No | 1 | The certificate type. |
| isImport | Bool ean | Body | No | false | Specifies whether to import the certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

<a id="section-3-11-6"></a>

### 3.11.6. ModifyCertificate

Modifies a certificate.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| certificates | Strin g | Body | No | cert1,cert2 | The list of certificates. |
| privateKey | Strin g | Body | No | -----BEGIN PRIVATE KEY----- | The private key. |
| certificate Name | Strin g | Body | No | MyCert | The certificate name. |
| certType | Integ er | Body | No | 1 | The certificate type. |
| isImport | Bool ean | Body | No | false | Specifies whether to import the certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

<a id="section-3-11-7"></a>

### 3.11.7. DeleteCertificate

Deletes a certificate.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

<a id="section-3-12"></a>

## 3.12. Other

<a id="section-3-12-1"></a>

### 3.12.1. GetTotalityInfo

This operation queries summary information.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter name | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -routeTotal | Integer | 150 | The number of routes. |
| -serverCount | Integer | 5 | The number of servers. |
| -interfaceCount | Integer | 50 | The number of interfaces. |
| -todayRequest Count | Integer | 15000 | The number of requests today. |
| -portalAppTotal | Integer | 50 | The total number of portal applications. |
| -backAppTotal | Integer | 10 | The total number of backend applications. |
| -mcpServerCou nt | Integer | 3 | The number of MCP servers. |
| -strategyCount | Integer | 5 | The number of policies. |

<a id="section-3-12-2"></a>

### 3.12.2. GetSettings

Queries system settings.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | Struct | {} | The data |
| -supportDeploy Modes | String | \[\] | A list of supported deployment modes. |
| -licenseInfoList | Array | \[\] | A list of license information. |
| --region | String | cn-hangzhou | The region. |
| --vcpuCount | Integer | 4 | The number of virtual CPU cores. |
| --upLimitNum | Integer | 10000 | The upper limit. |
| --routeCount | Integer | 25 | The number of routes. |
| --aiProxyCount | Integer | 10 | The number of AI proxies. |
| --percentage | Float | 85.5 | The percentage. |
| --warn | Boolean | false | Indicates whether a warning is reported. |
| --error | Boolean | false | Indicates whether an error is reported. |
| -capacityPlatfor mEnable | Boolean | true | Indicates whether the capacity platform is enabled. |
| -licenseEnable | Boolean | true | Indicates whether the license is enabled. |
| -customPluginE nable | Boolean | true | Indicates whether custom plugins are enabled. |

<a id="section-3-12-3"></a>

### 3.12.3. GetSlsStatistics

Queries statistics information from Simple Log Service (SLS).

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| body | Strin g | Body | No | {"key":"value"} | The request body. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| Code | Integer | 200 | The response code. |
| Msg | String | Operation successful | The message |
| Data | Struct | {} | The data |
| -Records | Array | \[\] | The record list. |
| --ServiceId | String | service-123456 | The service ID. |
| --ServiceGroupI d | String | group-001 | The service group ID. |
| --ConsumerId | String | consumer-123 | The consumer ID. |
| --Time | String | 2024-10-14 14:00:00 | The time. |
| --InputToken | Long | 1024 | The number of input tokens. |
| --OutputToken | Long | 2048 | The number of output tokens. |
| --TotalRequestC ount | Long | 500000 | The total number of requests. |
| --FailedRequest Count | Long | 150 | The number of failed requests. |
| -Total | Long | 1000 | The total number of entries. |
| -Current | Long | 1 | The current page number. |
| -Size | Long | 100 | The size |
