Alibaba Cloud  
Apsara Stack  
IDaaS  
User Guide  
Product Version: v3.18.6-2607  
Document Version: 20260831

**Table of Contents**

- [1.IdPs](#section-1)
    - [1.1. Associate IDaaS with DingTalk - outbound direction](#section-1-1)
    - [1.2. Bind a DingTalk first-party application to IDaaS](#section-1-2)
    - [1.3. Connect WeCom to IDaaS](#section-1-3)
    - [1.4. Connect IDaaS to Feishu](#section-1-4)
    - [1.5. Connect IDaaS to AD](#section-1-5)
    - [1.6. Connect IDaaS to OpenLDAP](#section-1-6)
    - [1.7. Bind IDaaS to an OIDC IdP](#section-1-7)
        - [1.7.1. Bind IDaaS to Okta](#section-1-7-1)
        - [1.7.2. Bind IDaaS to Microsoft Entra ID (FKA Azure AD)](#section-1-7-2)
    - [1.8. Field mappings](#section-1-8)
    - [1.9. Introduction to cron expressions](#section-1-9)
- [2.User portal](#section-2)
    - [2.1. Portal page](#section-2-1)
    - [2.2. Self-service](#section-2-2)
    - [2.3. Access the IDaaS portal from the DingTalk console](#section-2-3)
    - [2.4. Login by scanning DingTalk QR codes](#section-2-4)
    - [2.5. General login page](#section-2-5)
- [3.Accounts](#section-3)
    - [3.1. Create an account or an organization](#section-3-1)
    - [3.2. Manage accounts](#section-3-2)
    - [3.3. Move an account](#section-3-3)
    - [3.4. Account lifecycle](#section-3-4)
    - [3.5. Field management](#section-3-5)
    - [3.6. Advanced expressions for account fields](#section-3-6)
    - [3.7. Manage organizations](#section-3-7)
    - [3.8. Manage groups](#section-3-8)
    - [3.9. Synchronize accounts](#section-3-9)
    - [3.10. Import files and export data](#section-3-10)
- [4.Applications](#section-4)
    - [4.1. Create Application](#section-4-1)
        - [4.1.1. Application overview](#section-4-1-1)
        - [4.1.2. Application marketplace](#section-4-1-2)
        - [4.1.3. 2. Standard protocols](#section-4-1-3)
        - [4.1.4. 3. Custom applications](#section-4-1-4)
    - [4.2. Manage Applications](#section-4-2)
        - [4.2.1. General configurations](#section-4-2-1)
        - [4.2.2. Configure SSO](#section-4-2-2)
        - [4.2.3. SAML 2.0 SSO](#section-4-2-3)
            - [4.2.3.1. Configuration of SAML 2.0-based SSO](#section-4-2-3-1)
            - [4.2.3.2. Configure accounts for an SAML-based application](#section-4-2-3-2)
            - [4.2.3.3. Rules for configuring SAML Attribute Statements](#section-4-2-3-3)
            - [4.2.3.4. Multi-relay state access](#section-4-2-3-4)
        - [4.2.4. OIDC SSO](#section-4-2-4)
            - [4.2.4.1. Configure SSO for an OIDC-based application](#section-4-2-4-1)
            - [4.2.4.2. Rules for the values of the extended OIDC id_token fields](#section-4-2-4-2)
            - [4.2.4.3. Login by using OIDC Device Flow](#section-4-2-4-3)
            - [4.2.4.4. M2M applications (machine-to-machine permission management)](#section-4-2-4-4)
                - [4.2.4.4.1. Call examples of M2M Client Token](#section-4-2-4-4-1)
        - [4.2.5. Configure SSO for custom applications](#section-4-2-5)
        - [4.2.6. Advanced: SLO](#section-4-2-6)
        - [4.2.7. Grant application permissions](#section-4-2-7)
        - [4.2.8. Synchronize accounts - IDaaS event callbacks](#section-4-2-8)
        - [4.2.9. Synchronize IDaaS accounts to an application by using SCIM](#section-4-2-9)
        - [4.2.10. Synchronize data from an application to IDaaS by using SCIM](#section-4-2-10)
        - [4.2.11. Open API operations](#section-4-2-11)
        - [4.2.12. Management permissions on Apsara Stack applications](#section-4-2-12)
    - [4.3. Configurations of common applications](#section-4-3)
        - [4.3.1. Configure 2FA for establishing SSL-VPN connections in Alibaba Cloud](#section-4-3-1)
- [5.Login](#section-5)
    - [5.1. General settings](#section-5-1)
    - [5.2. Authentication configuration](#section-5-2)
        - [5.2.1. 2FA](#section-5-2-1)
        - [5.2.2. WebAuthn login](#section-5-2-2)
        - [5.2.3. CAPTCHA verification](#section-5-2-3)
    - [5.3. Password policies](#section-5-3)
- [6.Logs](#section-6)
    - [6.1. Management operations](#section-6-1)
    - [6.2. User behavior](#section-6-2)
    - [6.3. Synchronization logs](#section-6-3)
- [7.Branding](#section-7)
    - [7.1. Branding](#section-7-1)
    - [7.2. Custom terms](#section-7-2)
    - [7.3. SMS gateway](#section-7-3)
    - [7.4. Email gateways](#section-7-4)
- [8.Other configurations](#section-8)
    - [8.1. Network endpoints](#section-8-1)
    - [8.2. Network scopes](#section-8-2)
- [9.Use Cases](#section-9)
    - [9.1. Synchronize AD domain data to DingTalk](#section-9-1)
    - [9.2. Log in to applications from DingTalk through SSO](#section-9-2)
    - [9.3. Use an AD or OpenLDAP account to log in to a third-party application](#section-9-3)
    - [9.4. Use AD, LDAP, or IDaaS accounts to log in to DingTalk Enterprise](#section-9-4)
    - [9.5. Use Alibaba Cloud IDaaS to synchronize account data from DingTalk, WeCom, Feishu, AD, and other IdPs to Alibaba Cloud RAM](#section-9-5)
    - [9.6. Synchronize accounts and groups to CloudSSO by using SCIM in Alibaba Cloud IDaaS](#section-9-6)
    - [9.7. Synchronize accounts to RAM by using SCIM in Apsara Stack IDaaS](#section-9-7)
    - [9.8. Use IDaaS to log in to Apsara Stack DevOps from IdPs such as AD, DingTalk, and WeCom](#section-9-8)
    - [9.9. Configure Alibaba Cloud API Gateway](#section-9-9)
    - [9.10. Use RAM to configure AccessKey-free access](#section-9-10)
    - [9.11. Synchronize users or groups from Azure AD to IDaaS by using SCIM](#section-9-11)
    - [9.12. Synchronize users or groups from Okta to IDaaS by using SCIM](#section-9-12)
    - [9.13. Use IDaaS to implement user-based SSO and role-based SSO for Grafana](#section-9-13)
    - [9.14. Log in to IDaaS applications from Lark by using SSO](#section-9-14)
    - [9.15. Log in to IDaaS applications in WeCom through SSO](#section-9-15)
    - [9.16. Configure SSO for AI Coding Assistant Lingma](#section-9-16)

<a id="section-1"></a>

# 1.IdPs

<a id="section-1-1"></a>

## 1.1. Associate IDaaS with DingTalk - outbound direction

This topic describes how to associate IDaaS with DingTalk for data push, including how to create an application, assign permissions, select scenarios, and map fields. This helps you smoothly connect Identity as a Service ( IDaaS) to DingTalk and synchronize data.

**Step 1: Create an application**

1. **Enter the basic information**.

   <ol type="i">

   <li>

   Display Name: Enter a name that is displayed to a user when the user logs in to and uses IDaaS.

   </li>

   <li>

   CorpId: You can obtain the value on the Home tab of DingTalk Platform.

   </li>

   </ol>

2. **Enter the application information**

   <ol type="i">

   <li>

   Go to DingTalk Open Platform > Enterprise Internal Applications and click **Create Application**.

   </li>

   <li>

   Obtain the **AppKey** and **AppSecret** in **Credentials and Basic Information**.

   </li>

   </ol>

3. **Enter the development information.**

   You also need to enter the following information in DingTalk:

   <ol type="i">

   <li>

   Callback domain name: Enter the URL in **Development Settings > Sharing Settings**. You must configure this parameter before you can log in to IDaaS by scanning a QR code with DingTalk.

   </li>

   <li>

   Application homepage URL: Go to **Security Settings > In-app Login-free Address**.

   </li>

   </ol>

   After you configure this parameter, when a user clicks the application in the DingTalk console, the user can log in to the IDaaS application by using single sign-on (SSO). You can set Privacy Level for the application in **Version Management and Publishing**.

   <ol type="i" start="3">

   <li>

   Outbound IP address: If you want only IDaaS to request the DingTalk application, click

   </li>

   </ol>

   **Security Settings** in the left-side navigation pane and configure the **Server Outbound IP** parameter.

**Step 2: Grant permissions**

1. Grant permissions in the current DingTalk application. Click **Permission Management**, select all permissions in **Address Book Management** and **Application Management**, and then click **Batch Request**. Select **All Employees**.

2. After you grant permissions, click **Next** in IDaaS. IDaaS verifies whether the application has the permissions to manage DingTalk Contacts. If yes, the configuration is complete.

**Step 3: Select a scenario**

**Features**

- Synchronization direction: The data of the IDaaS account or organization selected as the source node is imported to the DingTalk destination node. Set the destination node to the ID of the DingTalk department. The department ID is displayed when you edit the department in the DingTalk Admin Console. The default ID of the DingTalk root department is 1.

- Incremental synchronization: If this feature is enabled, all changed data of the IDaaS account or organization is synchronized to DingTalk Contacts in real time. When an IDaaS account is exported to DingTalk, IDaaS matches the account to the DingTalk user based on the **mapping identifiers** specified in **Step 4: Field mapping**. You can define the mapping rules in Field Mapping. If the matching is successful, the existing IDaaS account is updated. Otherwise, an IDaaS account is created.

- DingTalk QR code login: If this feature is selected, the **DingTalk QR Code Login** option is provided and enabled in the **Login** menu. Users can log in to IDaaS by scanning the provided QR code with DingTalk.

> **Warning**
>
> We recommend that you test the synchronization by using the data of a small number of accounts or in a non-production environment. This prevents the data of DingTalk from being affected by improper configuration.

**Step 4: Configure field mappings**

If you already have data in DingTalk and need to associate the accounts or organizations in IDaaS with the DingTalk users or departments, or if you want to use some data of an IDaaS account as the data of a DingTalk user, you must configure field mapping. For example, you must configure field mapping if you want to use the display name of the IDaaS account as the name of the DingTalk user.

> **Important**
>
> When you log in to DingTalk Enterprise by using an IDaaS account, make sure that the user ID (userid) of the DingTalk user is the same as that of the IDaaS account.

1. By default, IDaaS allows you to customize field values such as the DingTalk name, mobile number, email address, title, and employee number. You can add other fields, such as workplace, based on your business requirements.

   - Field Name: This parameter is displayed only in IDaaS.

   - Field Identifier: You must use a DingTalk field name which is unique for the current identity provider. In the preceding figure, the field identifier of workplace is  `work_place` . For more information about DingTalk fields, see All fields of DingTalk users and All fields of DingTalk departments.

2. If you confirm that the configuration of field mapping is correct, select **Save and Push**. In this case, all IDaaS data selected in **Step 3** is synchronized to DingTalk. If you are not sure whether the configuration of field mapping is correct, select **Save Only**. You can modify the configuration in **Modify Settings > Field Mapping** of this identity provider later.

> **Important**
>
> Before you use the incremental synchronization feature, make sure that full data synchronization is performed at least once. Otherwise, incremental synchronization may fail.

<a id="section-1-2"></a>

## 1.2. Bind a DingTalk first-party application to IDaaS

This topic describes how to bind a DingTalk first-party application to Alibaba Cloud Identity as a Service (IDaaS). The steps include creating an application, granting permissions, selecting a scenario, and configuring field mappings.

**Scenario**

After you bind a DingTalk first-party application to IDaaS, you can use the following integration capabilities.

| Category | Capability |
| --- | --- |
| Account management | • <strong>Full synchronization</strong>: You can use one of the following methods to synchronize data from your DingTalk address book to IDaaS.<br>• Manual synchronization<br>• Scheduled synchronization (synchronization frequency can be configured)<br>• <strong>Incremental synchronization</strong>: You can monitor DingTalk address book changes in real time and automatically synchronize the changed data to IDaaS to ensure data timeliness<strong>.</strong> |
| Login integration | • <strong>Unified authentication</strong>: You can use DingTalk to scan code to log in.<br>• Directly log in to IDaaS<br>• Log in to various application systems integrated with IDaaS |

**Procedure**

> **Important**
>
> DingTalk requires strict application permissions. Make sure that your account has **developer permissions**. Otherwise, you cannot use core features such as data synchronization. You must configure the required permissions before you perform subsequent operations.

**Step 1: Create an application**

1. **Create an application in DingTalk**.

   <ol type="i">

   <li>

   Log in to the DingTalk Open Platform and go to the developer backend. On the Internal Enterprise Applications page, click **Create An Application**. Then specify **Application Name** and **Description**. You can also upload an **application icon** as needed. This parameter is optional.

   </li>

   <li>

   After the application is created, go to the application details page and click **Credentials**

   </li>

   </ol>

   **And Basic Information** to obtain the **AppKey** and **AppSecret**. Then, click the icon in the upper-right corner, copy the **CorpID**, and enter it in the IDaaS console.

2. **Create an application in IDaaS**.

   <ol type="i">

   <li>

   Log in to the Alibaba Cloud IDaaS console and select the corresponding IDaaS instance. On the **IdPs** page, click **Other IdPs**. In the Add IdP panel, click **DingTalk - Inbound (First-party Application).**

   </li>

   <li>

   Enter the basic information. Enter the **display name** and **CorpId** as required.

   </li>

   <li>

   Enter the application information. Enter the obtained **AppKey** and **AppSecret** in the

   </li>

   </ol>

   IDaaS console. Click **Next** to proceed.

   > **Note**
   >
   > The system automatically verifies the validity of the AppKey, AppSecret, and CorpID that you entered. **Make sure that the CorpID is unique within the same instance**.

**Step 2: Grant permissions**

1. On the DingTalk application details page, choose **Permission Management > Address Book Management**. Configure the following query permissions on the address book, which are required to enable data synchronization and user login.

   <table>
     <tr>
       <th>Permission</th>
       <th>Permission name</th>
       <th>Note</th>
     </tr>
     <tr>
       <td>Enterprise employee mobile number information</td>
       <td>fieldMobile</td>
       <td rowspan="2">You must select one of the two properties. You can select which field to use for the corresponding activation based on your business requirements.</td>
     </tr>
     <tr>
       <td>Email and other personal information</td>
       <td>fieldEmail</td>
     </tr>
     <tr>
       <td>Obtain the basic information of contacts</td>
       <td>qyapi_get_department_list</td>
       <td>--</td>
     </tr>
     <tr>
       <td>Permission to read department members in contacts</td>
       <td>qyapi_get_department_member</td>
       <td>--</td>
     </tr>
     <tr>
       <td>Permissions to read information about members</td>
       <td>qyapi_get_member</td>
       <td>--</td>
     </tr>
   </table>

2. On the **Permission Management** page, configure data permissions. This setting determines which users and organizations can synchronize data to IDaaS and log in to DingTalk.

3. After you configure permissions, click **Next** in the IDaaS console. The system automatically verifies the API and data permissions. After the verification is passed, you can proceed with the subsequent process.

**Step 3: Select a scenario**

1. **Synchronization target**: Select Alibaba Cloud IDaaS from the drop-down list. The address book data of DingTalk is imported to the IDaaS destination node.

2. **Incremental synchronization**: You must enable this feature after you configure IDaaS. This feature depends on the DingTalk event callback mechanism and requires that IDaaS is available.

3. **Scheduled verification**: You can configure synchronization policies by using scheduled tasks or cron expressions to update local user data incrementally.

4. **QR code login**: After you enable this mode, you can scan QR code by using DingTalk to log in to IDaaS.

**Step 4: Configure field mappings**

If you have existing data in IDaaS, you must associate the **DingTalk Address Book Users/departments** with the existing IDaaS **Accounts/organizations**, or map the fields of the DingTalk user (such as the name) to the IDaaS account attributes (such as the display name). In this step, complete the field mapping configuration and click **Save**.

**Step 5: Configure security settings**

1. On the IDaaS application modification page, you must configure the security settings of DingTalk, including obtaining the shared public IP address whitelist and application homepage URL, and entering them in the relevant fields of the DingTalk internal application. Shared endpoints and dedicated endpoints are supported. The former uses shared IP addresses to implement basic network policies, whereas the latter uses dedicated IP addresses to provide stricter data synchronization and login control.

   <ol type="i">

   <li>

   **Shared endpoint**

   - Obtain the **Shared Public Network Egress IP List** and **Application Homepage Address** from the IDaaS application modification page and configure them in the security settings of DingTalk.

   </li>

   <li>

   **Dedicated endpoint**

   - If stricter network policies are required, select a dedicated endpoint and obtain a dedicated IP address. For more information about how to add a dedicated endpoint, see the "Add a dedicated endpoint" section of the Network endpoints topic.

   - Configure the dedicated IP address to the same security settings of the DingTalk application. This helps you implement independent data synchronization and QR code login to enhance controllability.

   </li>

   </ol>

2. Go to the details page of the DingTalk application, click **Security Settings**, and then enter the **Server Egress IP** and **Redirect URL (callback Domain)** obtained from the IDaaS console.

   <ol type="i">

   <li>

   Server Egress IP: When IDaas calls the DingTalk interface, DingTalk checks whether the service initiation address is in the list of trusted IP addresses.

   </li>

   <li>

   Redirect URL: This parameter corresponds to the homepage URL of the application in

   </li>

   </ol>

   IDaaS. When QR code login is enabled, DingTalk will redirect to this URL with an authorization code after the user scans the code and completes authorization.

**Data synchronization**

1. **Manual-triggered synchronization:** If you manually pull full data in the console, the system automatically performs an incremental update.

   In the IdP list, click **Trigger Synchronization**. In the upper-left corner, click **View Details** to view the synchronization result. You can also check the synchronization result based on the user directory structure.

2. **Incremental synchronization:** After event subscription is enabled, DingTalk pushes notifications when data changes. IDaaS synchronizes incremental data in real time.

   <ol type="i">

   <li>

   In the DingTalk Open Platform, click **Event Subscription**.

   <ol type="a">

   <li>

   Set **Push Method** to **HTTP Push**.

   </li>

   <li>

   Click the Refresh button next to the **Encryption AesKey** and **Signature Token** boxes to generate the corresponding information.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   The format of **Request URL** is **{Application Homepage Address}/callback/idp/dingtalk/orgapp/{CoprId}**.

   > **Note**
   >
   > - {Application Homepage Address} is the login homepage URL in the application details in the IDaaS application list.
   >
   > - {CoprId} is the ID of the current enterprise in DingTalk.

   </li>

   <li value="500">

   You cannot click Save in the current step. You must configure the aesKey and signature token in the IDaaS console and then click Save in DingTalk.

   </li>

   </ol>

   </li>

   <li>

   In the IDaaS console, go to the **IdPs** page and click **Modify** in the **IdP** column. Enter the

   </li>

   </ol>

   **Encryption AesKey**, **Signature Token**, and **Request URL** obtained from the DingTalk Open Platform.

   <ol type="i" start="3">

   <li>

   In the DingTalk Open Platform, click **Save Event Subscription**.

   </li>

   </ol>

   <ol type="a">

   <li>

   When you save the configurations, the DingTalk server initiates a permission verification request to IDaaS. The verification process uses the aesKey and signature token generated by the DingTalk Open Platform for identity verification.

   </li>

   <li>

   On the **Event Subscription** page, find the events to which you want to subscribe, and enable event subscription.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   The description of the subscribed event.

   | No. | Interface name | Change type | Description |
   | --- | --- | --- | --- |
   | 1 | user_add_org | User change | A user is added to the address book. |
   | 2 | user_modify_org | User change | A user in the address book is changed. |
   | 3 | user_leave_org | User change | A user in the address book is resigned. |
   | 4 | org_dept_create | Department change | An enterprise department in the address book is created. |
   | 5 | org_dept_modify | Department change | An enterprise department in the address book is modified. |
   | 6 | org_dept_remove | Department change | An enterprise department is removed from the address book. |

   </li>

   <li value="4">

   Enable incremental synchronization in the IDaaS console. After you configure incremental synchronization, you can verify event subscription based on logs or changes in the organization structure.

   </li>

   </ol>

3. **Scheduled synchronization:** If you configure a scheduled synchronization task, IDaaS regularly pulls full user data from DingTalk and automatically converts it to an incremental update.

   IDaaS can use one of the following methods: a fixed point in time every day or a Cron expression. During this time range, IDaaS automatically pulls all user information from DingTalk to synchronize incremental data.

<a id="section-1-3"></a>

## 1.3. Connect WeCom to IDaaS

This topic describes how to connect Identity as a Service (IDaaS) to WeCom and the common operations that you can perform.

**Process overview**

Only four steps are required for connecting WeCom to IDaaS:

1. Create an application: Create an application in the WeCom Management Back Office and an application in the IDaaS console. Configure the basic information of the applications, trusted domain names, and trusted IP addresses to meet the security compliance requirements of WeCom.

2. Grant permissions: You can adjust the visibility scope of the WeCom application and determine the contact data (only departments and members) that IDaaS can access. The contact data is the source data to be synchronized in subsequent steps.

3. Select scenarios: Select scenarios for different features such as contact data synchronization or login through QR code scanning, configure synchronization rules such as full synchronization or field matching logic, and specify the login method.

4. Create field mappings: Bind or map fields related to WeCome members or departments to account or organization fields in IDaaS to ensure the relevance and consistency of data.

**Preparations**

For security reasons, when you call the API operations of WeCom for contact verification and identity authentication, the system verifies the domain name and IP address that you use. If the verification is successful, the domain name and IP address are trusted. A trusted IP address can be used only by one enterprise in WeCom. If a trusted IP address is used by multiple enterprises, the IP address is considered as that of a service provider. As a result, the API operations for contact verification and identity authentication become unavailable. To meet the security requirements of WeCom, you must prepare the following items.

| Verification item | Description |
| --- | --- |
| Trusted domain name | A dedicated domain name. The principal of the domain name must be the same as the principal for authentication in WeCom. |
| Trusted IP address | At least one dedicated endpoint must be configured for an IDaaS Employee Identity and Access Management (EIAM) instance. This way, the instance can access WeCom by using the dedicated public outbound IP address. For more information, see Network endpoints. |

**Scenarios**

After you connect WeCom to IDaaS, you can perform the following operations.

| Category | Operation |
| --- | --- |
| Account | • Synchronize the non-sensitive data of WeCom contacts to IDaaS EIAM.<br>• Synchronize the sensitive data, such as mobile phone numbers and email addresses, of WeCom contacts to IDaaS EIAM. |
| Login | Scan a QR code by using WeCom to log in to IDaaS EIAM or an IDaaS EIAM application. |

**Procedure**

**Step 1: Create an application**

1. **Create a WeCom application**

   <ol type="i">

   <li>

   **Create an application in WeCom**

   **Log in to the** WeCom Management Back Office. Choose **Application Management > Applications** and click **Create Application**.

   </li>

   <li>

   **Configure application information**

   Upload **Application Logo**, specify **Application Name**, **Application Introduction (Optional)**, and **Visibility Scope**. Visibility Scope specifies the contact data that is synchronized to IDaaS EIAM and users can access after logging in to IDaaS EIAM. Return to the Application Management page.

   </li>

   <li>

   **View the application**

   Return to the Application Management page. The list shows that the application that you created.

   </li>

   </ol>

2. **Create an application in IDaaS**.

   <ol type="i">

   <li>

   **Connect WeCom to IDaaS in the IDaaS console**

   Log in to the IDaaS Console and find the desired IDaaS instance. On the **IdPs** page, choose **Other IdPs > WeCom** to connect WeCom to IDaaS.

   > **Important**
   >
   > If no dedicated endpoint is configured for the instance, you must configure a dedicated endpoint. For more information, see Network endpoints.

   </li>

   <li>

   **Enter the basic information**

   Specify **Display Name** and **CorpID**.

   - **Display Name**: Enter a name that is displayed to a user when the user logs in to and uses IDaaS EIAM.

   - **CorpID**: **Log in to the** WeCom Management Back Office. Choose **My Company > Company Information** and obtain **CorpID**.

   </li>

   <li>

   **Enter the application information**

   Specify **AgentId** and **Secret**.

   <ol type="a">

   <li>

   Log in to the WeCom Management Back Office. Choose **Application Management > Applications** and access the details page of the application that you created.

   </li>

   <li>

   On the application details page, click **View** next to the Secret field.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   In the message that appears, confirm to send the secret. Then, you can view the secret in **WeCom team messages**.

   </li>

   </ol>

   </li>

   <li>

   **Enter the development information**

   > **Note**
   >
   > This example uses a custom domain name.
   >
   > - You can synchronize only non-sensitive data and use WeCom to scan a QR code for login.
   >
   > - Specify a dedicated domain name as the trusted domain name. Make sure that the domain name belongs to the verified entity of the WeCom account and is not required by the workloads of IDaaS EIAM. The parameter values in the Development Information section, excluding the Trusted Domain Name parameter, are automatically provided by the system.

   <ol type="a">

   <li>

   **Configure the trusted domain name**.

   <ol type="a">

   <li>

   On the application details page of the WeCom Management Back Office, click **Set Trusted Domain Name**.

   </li>

   <li>

   Enter a trusted domain name for the OAuth2.0-based web page authorization feature.

   > **Note**
   >
   > The trusted domain name must belong to the verified entity of WeCom and cannot include the protocol or path.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   After the trusted domain name is verified, you must complete domain name ownership verification as prompted in WeCom.

   </li>

   </ol>

   </li>

   <li>

   **Configure the enterprise trusted IP address**. Click the drop-down list and select a dedicated network endpoint.

   <ol type="a">

   <li>

   Allow the IDaaS EIAM instance to use the dedicated public outbound IP address of the network endpoint to access WeCom.

   </li>

   <li>

   Select a network endpoint from the Enterprise Trusted IP drop-down list and click View next to **Dedicated Public Outbound IP Address**.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   In the dialog box that appears, view the public IP addresses that the IDaaS EIAM instance can use. Then, click **Copy All IP Addresses**.

   </li>

   <li value="500">

   Go to the application details page of the WeCom Management Back Office and click Settings in the **Enterprise Trusted IP** section.

   </li>

   </ol>

   > **Important**
   >
   > All WeCom APIs can be called by IDaaS EIAM through a trusted IP address. If the trusted IP address is invalid or unavailable, you cannot use features such as data synchronization from WeCom and WeCom-based QR code login. The logic for verifying a trusted IP address in WeCom is not disclosed. To ensure that you can log in to IDaaS, you must also enable another login method, such as username and password-based authentication or verification code-based authentication.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   **Configure the authorized callback domain.**

   <ol type="a">

   <li>

   On the **Bind WeCom - Inbound** page, copy the authorized callback domain.

   </li>

   <li>

   Go to the application details page of the WeCom Management Back Office and click **Setting** in the **Login Authorized by WeCom**.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   In the **Web Page** section, click **Set Authorized Callback Domain**. Enter the authorized callback domain copied from IDaaS.

   </li>

   </ol>

   </li>

   </ol>

   After you complete the configuration, click **Next** to proceed to **Grant Permissions**.

   </li>

   </ol>

**Step 2: Grant permissions**

In this step, follow the on-screen instructions to modify the **visibility scope**. The **visibility scope** specifies the contact data that is synchronized to IDaaS EIAM and users can access after logging in to IDaaS EIAM. For data synchronization, the visibility scope specified the source of data to be synchronized.

**Step 3: Select a scenario**

In this step, configure the features that you want to use in a specific scenario.

**Features**

- Synchronization Scope: After you select an IDaaS node, WeCom contacts are synchronized to the node.

- Scheduled Verification: If you turn on Scheduled Verification, IDaaS automatically synchronizes full data from the source node of WeCom every morning.

  - You can configure mapping identifiers in the Field Mapping step of an IDaaS account to a field of a WeCom user. For example, you can match the Username field of an IDaaS account to the  `userid`  field of a WeCom user. If the matching is successful and the WeCom user is updated, the IDaaS account is also updated from the WeCom user. If the matching fails, an IDaaS account is created by using the information about the WeCom user.

  - To synchronize the latest data, you must manually trigger full synchronization.

  - IDaaS provides synchronization protection. When more than 30 accounts or more than 10 organizations need to be deleted, the synchronization task is automatically canceled to prevent accidental data deletion. We recommend that you adjust the synchronization protection settings based on the scale of your enterprise.

- Sign-In with QR Code: If you turn on Sign-In with QR Code, the QR Code (WeCom) option is provided and enabled on the **login page of IDaaS**. This way, users can scan a QR code by using WeCom to log in to IDaaS.

**Step 4: Configure field mappings**

If you already have accounts or organizations in IDaaS and you want to map them to the WeCom users or departments, or if you want to use specific fields of an IDaaS account as the fields of a WeCom user, you must configure field mappings. For example, if you want to use the display name of an IDaaS account as the name of a WeCom user, you must configure a field mapping.

> **Important**
>
> If the  `userid`  field in WeCom is automatically generated, the field can be modified once. The userid field is the primary key used by IDaaS to identify users. If you modify the field, the corresponding IDaaS account is deleted, and another IDaaS account is created. Do not modify the field unless necessary.

**Manage WeCom**

After you connect WeCom to IDaaS, you are redirected to the **IdPs** page. You can manage different features that are used to interact with identity providers (IdPs) on the IdPs page.

**Usage notes**

**QR code-based login**

When you use QR code-based login by using WeCom, you are redirected to the address specified by the **Authorized Callback Domain** parameter. Specifically, if you want to use WeCom to scan a QR code to log in to IDaaS EIAM or an IDaaS EIAM application, you must ensure consistency between the domain name of the IDaaS EIAM login page, the value of the Authorized Callback Domain parameter for the WeCom IdP in IDaaS, and the authorized callback domain name in WeCom.

**Sensitive data synchronization**

Before you can access sensitive data, you must manually authorize the request in IDaaS EIAM. When you initiate SSO from the WeCom web page, a page appears that prompts you to complete the authorization. After the authorization is complete, the mobile phone number and email address of the WeCom account are used in the IDaaS EIAM account. If no email address of the WeCom account exists, you can specify a personal email address.

If you access the WeCom application within 30 days, no authorization operations are required. If you want to modify the authorization of sensitive data within 30 days, access the WeCom application that you created in Step 1 and select **Personal Sensitive Information Authorization Management** on the details page of the application.

In addition to manual authorization, the administrator must perform the following steps: Go to the WeCom Admin Console and choose **My Company > Contacts Management > Member Info Display**. Then, check whether the display of sensitive data such as the mobile phone number and email address is configured. Only sensitive data on which you have access permissions and is configured to be displayed by the administrator can be synchronized to IDaaS EIAM.

**Other login methods**

> **Important**
>
> IDaaS makes every effort to ensure the availability of data synchronization and identity authentication for your WeCom contacts. However, due to the lack of publicly disclosed details regarding the verification methods, such as trusted domain names and trusted IP addresses in WeCom, and the risk management policies, Alibaba Cloud cannot guarantee that you can consistently and reliably log in to IDaaS by using your WeCom account.
>
> To mitigate the risk of being unable to access IDaaS when WeCom is unavailable, you must also enable other login methods, such as username and password-based authentication or verification code-based authentication. If you cannot log in to IDaaS by using a WeCom account and do not use another login method, you are liable for losses.

For more information about other login methods, see Login.

<a id="section-1-4"></a>

## 1.4. Connect IDaaS to Feishu

This topic describes how to connect Identity as a Service (IDaaS) to Feishu and the common operations that you can perform.

**Process overview**

You can connect IDaaS to Feishu in four steps:

1. Application Authorization Configuration: In the Feishu Open Platform, configure the required permissions for your application to ensure that it can access the necessary data and features.

2. Development Configuration: In the IDaaS console, configure development-related settings, such as webhook addresses and application credentials.

3. Select Scenario: Select the integration scenarios and authentication methods that meet your business requirements.

4. Field Mapping: Configure the mapping between Feishu user attributes and IDaaS user attributes to ensure that data is synchronized correctly.

**Scenarios**

After you connect IDaaS to Feishu, you can use the following features.

| Category | Feature |
| --- | --- |
| Account | • Synchronize the full data of Feishu address book to IDaaS Enterprise Identity Access Management (EIAM). Scheduled verification is supported. |
| Login | • Scan a QR code by using Feishu to log in to IDaaS EIAM or an application in it.<br>• Initiate single sign-on (SSO) from the Feishu workbench to log in to IDaaS EIAM or an application in it. |

**Procedure**

On the **IdPs** page, click **Other IdPs**. In the panel that appears, click **Feishu**.

**Step 1: Configure parameters in the Application Authorization Configuration step**

> **Important**
>
> Feishu has fine-grained requirements for granting permissions to applications. Specific permissions can take effect only after the permissions are approved by administrators and the required application is published. When you grant permissions, you may require assistance from other administrators in your enterprise. If you do not grant permissions to your application, you cannot use features such as data synchronization. We recommend that you first configure application permissions in this step before you proceed to the next step.

1. **Create a Feishu application**.

   <ol type="i">

   <li>

   Go to the Feishu Open Platform and log in to the developer console. In the developer console, create a self-managed Feishu application for your enterprise.

   </li>

   <li>

   After you create the Feishu application, you are redirected to the details page of the

   </li>

   </ol>

   application. In the left-side navigation pane, click **Credentials & Basic Info**. On the page that appears, copy the values of the **App ID** and **App Secret** parameters.

2. Paste the values of **App ID** and **App Secret** into IDaaS.

3. In the left-side navigation pane of the details page of the Feishu application, choose **Permissions & Scopes > Add permission scopes to app**. On the panel that appears, find the **Address Book** section and grant the following permissions. The permissions are query permissions on the address book, which are required to enable data synchronization and user login.

   | Permission description | Permission name | Note |
   | --- | --- | --- |
   | Read the basic information of the address book | contact:contact.base:readonly | -- |
   | Read user IDs | contact:user.employee_id:readonly | -- |
   | Read the basic information of departments | contact:department.base:readonly | -- |
   | Read the organizational structure of departments in the address book | contact:department.organize:readonl y | After you apply for this permission, you must submit a release request for the latest application version and wait for approval before the permission takes effect. |
   | Read the basic information of users | contact:user.base:readonly | -- |
   | Read the organizational structure of users | contact:user.department:readonly | After you apply for this permission, you must submit a release request for the latest application version and wait for approval before the permission takes effect. |
   | Read the email addresses of users | contact:user.email:readonly | This permission is optional. You must grant this permission only if you want to synchronize the corresponding fields to IDaaS. |
   | Read the mobile numbers of users | contact:user.phone:readonly | After you apply for this permission, you must submit a release request for the latest application version and wait for approval before the permission takes effect.<br>This permission is optional. You must grant this permission only if you want to synchronize the corresponding fields to IDaaS. |

   > **Note**
   >
   > After you submit a release request, your Feishu administrator is notified. The administrator must review the request in the Feishu Admin console.

4. **Grant data permissions to the Feishu application**.

   <ol type="i">

   <li>

   In the left-side navigation pane, click **Permissions & Scopes**. On the Permissions & Scopes page, click **Configure** next to **Range of accessible data** to grant data permissions.

   </li>

   <li>

   Select data permissions based on your business requirements. Users and organizations in

   </li>

   </ol>

   the scope that you configure can be synchronized to IDaaS and can log in to IDaaS by using Feishu.

5. **Submit the application creation request in IDaaS.** After you complete the preceding permission configurations, click **Next** in IDaaS. IDaaS verifies the API permissions and data permissions. After IDaaS confirms that the required permissions are granted, you can proceed to the next step.

**Step 2: Configure parameters in the Development Configuration step**

1. **Enter the basic information**.

   <ol type="i">

   <li>

   Specify the **Display Name**.

   </li>

   <li>

   Specify the **Enterprise ID**. You must obtain the enterprise ID from the Feishu Admin

   </li>

   </ol>

   console, as shown in the following figure.

2. **Configure the development information.**

   <ol type="i">

   <li>

   **Redirect URL.**

   <ol type="a">

   <li>

   **View and copy the redirect URL in IDaaS**. This URL specifies the page to which a user is redirected after a login request is successfully processed.

   </li>

   <li>

   **Configure the redirect URL in Feishu**. Go to the details page of the Feishu application. In the left-navigation pane, click **Security Settings**. On the page that appears, click the **Redirect URLs** tab, and then paste the URL. Click **Add**.

   </li>

   </ol>

   </li>

   <li>

   **Application homepage.**

   <ol type="a">

   <li>

   **View and copy the application homepage URL in IDaaS**. If you want users to access the IDaaS user portal by initiating SSO from the Feishu workbench, you must configure an application homepage in Feishu.

   </li>

   <li>

   **Configure the application homepage URL in Feishu**. Go to the details page of the Feishu application. In the left-side navigation pane, click **Add Features**. On the page that appears, click the By Feature tab, find Web app, and then click **Configure**.

   Then, paste the URL into the Desktop homepage and Mobile homepage fields.

   </li>

   </ol>

   </li>

   <li>

   **IP address whitelist.**

   <ol type="a">

   <li>

   **View and copy the IP address whitelist in IDaaS**.

   - Shared Network Access Endpoint: A shared endpoint is the default endpoint that an IDaaS EIAM instance uses to access the Internet. All IDaaS EIAM instances can use the shared endpoint. You can use a shared endpoint to access only the Internet.

   - Dedicated Network Access Endpoint: A dedicated endpoint is an exclusive endpoint for an IDaaS EIAM instance. You can use a dedicated endpoint to synchronize data of Feishu and enable Feishu authentication. For more information, see Network endpoints.

   </li>

   <li>

   **Configure the IP address whitelist in Feishu**. If you want to implement access control, copy the egress IP addresses of IDaaS. Go to the details page of the Feishu application. In the left-side navigation pane, click **Security Settings**. On the page that appears, click the **IP allowlist** tab and click **Batch Modify**. Then, paste the IP addresses.

   </li>

   </ol>

   </li>

   </ol>

**Step 3: Configure parameters in the Select Scenario step**

In this step, configure the features that you want to use.

**Feature description**

- **Synchronization Scope**: Select Alibaba Cloud IDaaS from the drop-down list. The address book data of Feishu is imported to the IDaaS destination node.

- **Scheduled Verification**: By default, IDaaS automatically performs a full synchronization of Feishu data at 00:00 every day to ensure data consistency. You can use field mapping to specify the matching rules between IDaaS accounts and Feishu users. For example, you can specify that an IDaaS account name corresponds to a Feishu user ID. If the IDaaS account name matches the Feishu user ID, related data is updated and associated. Otherwise, a new account is created. To synchronize data in real time, you can manually trigger a full data synchronization task. IDaaS has a built-in protection mechanism that stops the synchronization task if it detects many deletions, such as the deletion of more than 30 accounts or 10 organizations, to prevent accidental data loss. We recommend that you adjust the threshold based on your enterprise size.

- **Scheduled Verification Time**: The synchronization is scheduled to run once per day. You can use a cron expression to customize the time. IDaaS has a built-in protection mechanism that stops the synchronization task if it detects many deletions, such as the deletion of more than 30 accounts or 10 organizations, to prevent accidental data loss.

- **Incremental Data Synchronization**: This feature is disabled by default. To enable it, you must first configure event notification after the connection is established. If event notification is not configured, the incremental data synchronization feature cannot be enabled. The users need to adjust the related configurations in the Add or Modify process to activate this feature.

  - On the **IdPs** page, find the Feishu application that you created and click **Modify**.

  - In the Configure Event panel, configure the **Encrypt Key** and **Verification Token** parameters. To obtain these parameters, go to the details page of the Feishu application. In the left-side navigation pane, click **Events and Callbacks**. On the page that appears, click the **Encryption Strategy** tab. On the Encryption Strategy tab, find and copy the Encrypt Key and Verification Token parameters.

  - Copy the value of **Request URL** in the Configure Event panel. Go to the details page of the Feishu application. In the left-side navigation pane, click **Events and Callbacks**. On the page that appears, click the **Event Configuration** tab. On the Event Configuration tab, paste the URL in the Request URL field under Send Event to Developer Server.

- **QR code-based logon**: If you enable this feature, the IDaaS login page displays the QR Code-based Logon with Feishu option. You can scan the QR code to complete authentication. If an application homepage is configured, you can also access IDaaS from the Feishu workbench without authentication for improved convenience.

**Step 4: Configure parameters in the Field Mapping step**

If you already have accounts or organizations in IDaaS and you want to map them to Feishu users or departments, or if you want to use specific fields of an IDaaS account as the fields of a Feishu user, you must configure field mappings. For example, if you want to use the display name of an IDaaS account as the name of a Feishu user, you must configure a field mapping.

> **Important**
>
> The  `userid`  field in Feishu is the unique identifier of a Feishu user and can be modified. The userid field is the primary key used by IDaaS to identify users. If you modify the field, the corresponding IDaaS account is deleted, and another IDaaS account is created. Do not modify the field unless necessary.

**Manage Feishu**

After you connect IDaaS to Feishu, you are redirected to the **IdPs** page. You can manage different features that are used to interact with identity providers on the IdPs page.

<a id="section-1-5"></a>

## 1.5. Connect IDaaS to AD

This topic describes how to connect Identity as a Service (IDaaS) to Active Directory (AD) and the common operations that you can perform.

**About AD**

**Overview**

AD is a directory service that runs on Microsoft Windows Server. AD allows administrators to centrally manage computers, user services, network resources, and permissions within domains in medium and large network environments.

**Procedure**

Log in to the IDaaS console. On the EIAM page, click the required instance. In the left-side navigation pane, click **Quick Start** or **IdPs**. On the page that appears, click **Bind AD**.

![](assets/bff598c8cdb1e565bb3b150aff62fc19.jpeg)

**Step 1: Configure parameters in the Connect to AD step**

Configure the following parameters in IDaaS:

![](assets/3f3b5070a1ca64a92b02060ba98ae691.jpeg)

- Nickname: the name that is displayed to a user when the user logs in to and uses IDaaS.

- Network Access Endpoint: the network endpoint of the IDaaS instance. If you want to allow only IDaaS to access the AD server, add the network endpoint to the IP address whitelist of the AD server. If an IDaaS instance uses a shared endpoint, the IDaaS instance is provided with a shared and fixed public outbound IP address. If an IDaaS instance uses a dedicated endpoint, the IDaaS instance is provided with a dedicated and custom private outbound IP address and a public outbound IP address. An IDaaS instance that is configured with a dedicated endpoint can access an Apsara Stack virtual private cloud (VPC) by using the dedicated endpoint. This way, you can allow the IDaaS instance to access your AD without the need to open public ports. For more information, see Network endpoints.

- Server Address: the address of the server where AD resides. Example: 127.0.0.1:389. By default, port 389 is used for AD. If LDAPS or StartTLS is enabled, port 636 is used.

- Enable StartTLS: specifies whether to enable StartTLS. We recommend that you enable LDAPS or StartTLS to improve the security of the connection. For more information about how to enable LDAPS or StartTLS, see the AD security configuration section of this topic.

- Administrator Account: the AD administrator account used by IDaaS to read AD information for data synchronization or delegated authentication. The account must have read permissions at a minimum. Enter the value in the User Principal Name (UPN) format such as example@example.com, or Distinguished Name (DN) format such as cn=admin, ou=technical department, dc=example, dc=com.

- Administrator Password: the login password of the administrator account.

**Step 2: Configure parameters in the Select Scenario step**

In this step, configure the features that you want to use.

![](assets/a9d1a7177906ad590728090c4156f67d.jpeg)

**Features**

- Synchronization Direction: The data of the AD user or organization selected as the source code is imported to the IDaaS destination node. Enter the DN of the AD node as the **source node**. The DN of the AD root node is dc=example, dc=com (your domain).

> **Note**
>
> Only synchronization from AD to IDaaS is supported. Synchronization from IDaaS to AD is not supported.

- Incremental Synchronization: IDaaS listens to the data of AD users or organizations, and synchronizes the changed data from AD to IDaaS every 10 minutes. If a large amount of data is involved in a single synchronization, latency may occur. We recommend that you perform full data synchronization on a regular basis to ensure data consistency between AD and IDaaS.

  - You can configure mapping identifiers in the Field Mapping step of an IDaaS account to a field of an AD user. For example, you can match the Mobile Phone Number field of an IDaaS account against the Mobile Phone Number field of an AD user. If the matching is successful and the AD user is updated, the IDaaS account is also updated from the AD user. If the matching fails, an IDaaS account is created by using the information about the AD user.

  - When incremental synchronization is performed for the first time, full data synchronization is automatically performed.

  - Failure to import a single data entry does not affect the import of other data entries.

  - You can view the failure information in **synchronization logs**.

  - You must enable AD Recycle Bin to receive messages about deletion events in AD. For more information about how to enable this feature, see the Incremental synchronization section of this topic.

- Delegated Authentication: If this feature is enabled, a user can log in to IDaaS by using an AD username and password.

- Automatic Password Update: When a user attempts to log in to IDaaS by using AD delegated authentication, if the password of the IDaaS account is empty, the password is automatically updated to the password of the AD user. The AD password must meet the requirements specified in the password policies of IDaaS. Otherwise, the IDaaS password cannot be automatically updated to the AD password.

**Advanced Settings**

- User/Organization  `ObjectClass` : You can use  `ObjectClass`  to define a type of object as a user or organization. For example, the object whose  `ObjectClass is user`  in the query result is considered a user. In most cases, no modification is required.

- User Sign-in ID: When a user attempts to log in to IDaaS by using AD delegated authentication, IDaaS uses the attributes to query the user in AD and matches the password. If the password is correct, the user is allowed to log in to IDaaS. You can separate multiple attributes with commas (,). In this case, these attributes have an OR relationship. This means that you can use one of them to log in to IDaaS. Make sure that multiple attributes correspond to the same AD user. Otherwise, the user cannot log in to IDaaS.

- FILTER Statement for Filtering Users: If you want to synchronize specific users from different organizations to IDaaS, you can use a custom  `filter`  statement to filter users. Only users that meet the filter conditions can be synchronized to IDaaS. By default, the  `filter`  statement contains  `ObjectClass`  conditions in the AND relationship. You can click **View Details** to view the complete statement. For more information, see the Filter section of this topic.

  ![](assets/7f7b3ac8e61e190234380111a5193fa0.jpeg)

**Step 3: Configure parameters in the Field Mapping step**

If you already have accounts or organizations in IDaaS and you want to map them to the AD users or organizations, or if you want to use specific fields of an IDaaS account as the fields of an AD user, you must configure field mappings. For example, if you want to use the name of an IDaaS account as the mobile phone number of an AD user, you must configure a field mapping. You can turn on the Mapped switch in the Mapping Identifier column.

![](assets/327712361dde0f70e3ea0c8a09f92aa4.jpeg)

For more information, see Field mappings.

**AD security configuration**

By default, data is transmitted in plaintext without encryption or protection in LDAP. This may cause data theft. You can use LDAPS or StartTLS to improve the security of data transmission. After you configure a certificate in AD, you can use LDAPS or StartTLS in IDaaS. We recommend that you enable LDAPS or StartTLS.

In **Server Manager**, install roles, upgrade the server to a domain server, add the certificate (use SHA256 as the signature algorithm), and then configure the certificate.

After you configure the certificate, you can obtain the certificate fingerprint in IDaaS to build the trust of IDaaS for the AD certificate. This reduces the risk of fake certificates.

![](assets/b39054c14ba0a4846fc4677af2cec7f6.jpeg)

> **Note**
>
> If you need to quickly check whether the certificate fingerprint displayed in AD is the same as that obtained from IDaaS, run the following script:
>
> ```bash
> openssl s_client -connect server_host:port | openssl x509 -noout -pubkey | openssl pkey -pubin -outform DER | openssl dgst -sha256
> ```

**AD custom configuration**

**ObjectClass**

`ObjectClass`  in AD is a set of attributes. Each object must have an  `ObjectClass` . You can use  `ObjectClass`  to define an object as a user, organization, or computer. For example, as shown in the following figure, the system can find the user by using the  `objectclass=person` or  `objectclass=user`  statement. You can view  `ObjectClass`  in the **attributes** of the AD object.

![](assets/610d3233a26ddbe887a8d283f83957fe.jpeg)

**User Sign-in ID**

When a user attempts to log in to IDaaS by using AD delegated authentication, IDaaS uses the attributes to query the user in AD and matches the password. If the password is correct, the user is allowed to log in to IDaaS.

You can use one of the attributes such as userPrincipalName, sAMAccountName, mobile phone number, email address, and employee number to log in to IDaaS. You can define the attributes when you create identity providers (IdPs) or on the **Delegated Authentication** page. If you use multiple attributes, make sure that the attributes are unique and correspond to the same AD user. Otherwise, the user cannot use delegated authentication.

**Filter**

> **Important**
>
> The modifications of the  `ObjectClass`  conditions and the  `filter`  statement affect the filter conditions of the AD node. During full data synchronization, IDaaS accounts and organizations that do not meet the filter conditions are deleted. We recommend that you adjust the synchronization protection settings and fully test whether the filtered results meet your expectations before you modify the ObjectClass conditions and the filter statement. For example, you can use another IDaaS instance to perform a test.

**Overview**

If you want to synchronize specific users from different organizations to IDaaS, you can use a custom  `filter`  statement to filter users. Only users that meet the filter conditions can be synchronized to IDaaS. By default, the  `filter`  statement contains  `ObjectClass` conditions in the AND relationship. You can click **View Details** to view the complete statement.

![](assets/1d5ceaa4e86889784f26a5bb73dfe93e.jpeg)

The following sections describe the common operators and  `filter`  statements for AD.

**Common operators**

| Operator | Description | Example |
| --- | --- | --- |
| = | Equal to | (cn=Alice) |
| &gt;= | Greater than or equal to | (pwdLastSet&gt;=1319563845000000000) |
| &lt;= | Less than or equal to | (sAMAccountName&lt;=a) |
| &amp; | AND relationship, which indicates that all conditions must be met | (&amp;(cn=CN\*)(memberOf=cn=Test,ou=HQ,dc=Domain,dc=com)) |
| \| | OR relationship, which indicates that at least one condition must be met | (\|(cn=Test\*)(cn=Admin\*)) |
| ! | NOT relationship, which indicates that all conditions must not be met | (!(memberOf=cn=Test,ou=HQ,dc=Domain,dc=com)) |

**Common statements**

| Scenario | Example |
| --- | --- |
| Select users whose usernames start with CN | (cn=CN\*) |
| Select the user with the specified email address | (\|(proxyAddresses=\*:alice@example.com)(mail=alice@example.com)) |
| Select users in the specified group | (memberOf=cn=Test,ou=HQ,dc=Domain,dc=com) |

**AD synchronization configuration**

**Obtain Base DN**

Base DN is the path identifier of a node in AD. IDaaS performs operations such as queries and data synchronization only within this node. You can configure the Base DN of the source node in **Synchronization Direction**.

The format of DN is ou=organization, dc=example, dc=com. The DN of the root node is dc=example, dc=com (your domain). You can also view the DN of the node in AD Administrative Center, as shown in the following figure.

![](assets/f63ad8241e28728c0e094507c24c1367.jpeg)

If the path of a node changes, the Base DN of the node also changes. To prevent AD data synchronization errors caused by node path changes, IDaaS uses the  `ObjectGuid`  of the node as the node fingerprint when you configure the Base DN of the source node in IDaaS. If the changed Base DN of the node does not match the node fingerprint, data synchronization is stopped. You can synchronize data after you reconfigure the source node.

**Incremental synchronization**

IDaaS listens to the data of AD users or organizations, and synchronizes the changed data from AD to IDaaS every 10 minutes. If a large amount of data is involved in a single synchronization, latency may occur. We recommend that you perform full data synchronization on a regular basis to ensure data consistency between AD and IDaaS.

Because of the limits of AD incremental synchronization, IDaaS must use AD Recycle Bin to obtain messages about deletion events. Enable the Recycle Bin feature in **AD Administrative Center**. This feature is supported on Windows Server 2012 and later.

![](assets/b7bcd4822b8e274edb7557fa2a632a80.jpeg)

<a id="section-1-6"></a>

## 1.6. Connect IDaaS to OpenLDAP

This topic describes how to connect Identity as a Service (IDaaS) to OpenLDAP and the common operations that you can perform.

**Introduction to OpenLDAP**

**Overview**

OpenLDAP is an open source implementation of Lightweight Directory Access Protocol (LDAP). OpenLDAP is widely used to manage resources such as users, computers, and networks within an enterprise. OpenLDAP is commonly referred to as LDAP.

**Procedure**

Log on to the IDaaS console. On the EIAM page, click the required instance. In the left-side navigation pane, click **IdPs**. On the page that appears, click **Bind OpenLDAP**.

![](assets/dbcc3ca22218355625ad1e6b18aa91f0.jpeg)

**Step 1: Connect to LDAP**

Configure the following parameters in IDaaS:

![](assets/90d6dac2927d2e5a6f8be573d5238533.jpeg)

- Nickname: the name that is displayed to a user when the user logs on to and uses IDaaS.

- Network Access Endpoint: the network endpoint of the IDaaS instance. If you want to allow only IDaaS to access the LDAP server, add the network endpoint to the IP address whitelist of the LDAP server. If an IDaaS instance uses a shared endpoint, the IDaaS instance is provided with a shared and fixed public outbound IP address. If an IDaaS instance uses a dedicated endpoint, the IDaaS instance is provided with a dedicated and custom private outbound IP address and a public outbound IP address. An IDaaS instance that is configured with a dedicated endpoint can access an Alibaba Cloud virtual private cloud (VPC) by using the dedicated endpoint. This way, you can allow the IDaaS instance to access your LDAP without the need to open public ports. For more information, see Endpoints.

- Server Address: the address of the server where LDAP resides. Example: 127.0.0.1:389. By default, port 389 is used for LDAP. If LDAPS or StartTLS is enabled, port 636 is used.

- Enable StartTLS: specifies whether to enable StartTLS. We recommend that you enable LDAPS or StartTLS to improve the security of the connection. For more information about how to enable LDAPS or StartTLS, see the LDAP security configuration section of this topic.

- Administrator Account: the LDAP administrator account used by IDaaS to read LDAP information for data synchronization or delegated authentication. The account must have read permissions at a minimum. Enter the value in the Distinguished Name (DN) format, such as cn=admin, ou=technical department, dc=example, dc=com.

- Administrator Password: the login password of the administrator account.

**Step 2: Configure features based on your scenario**

In this step, configure the features that you want to use.

![](assets/dd6fd42b3e086f2ce5b777aad243132b.jpeg)

**Features**

- Synchronization Direction: The data of the LDAP user or organization selected as the source code is imported to the IDaaS destination node. Enter the DN of the LDAP node as the **source node**. The DN of the LDAP root node is dc=example, dc=com (your domain).

> **Note**
>
> Only synchronization from LDAP to IDaaS is supported. Synchronization from IDaaS to LDAP is not supported.

- Scheduled Verification: LDAP does not support queries of incremental data. IDaaS automatically synchronizes full data under the LDAP source node every morning.

  - You can configure mapping identifiers in the Field Mapping step of an IDaaS account to a field of an LDAP user. For example, you can match the Mobile Phone Number field of an IDaaS account against the Mobile Phone Number field of an LDAP user. If the matching is successful and the LDAP user is updated, the IDaaS account is also updated from the LDAP user. If the matching fails, an IDaaS account is created by using the information about the LDAP user.

  - To synchronize the latest data, you must manually trigger full data synchronization.

  - IDaaS provides synchronization protection. When more than 30 accounts or more than 10 organizations need to be deleted, the synchronization task is automatically canceled to prevent data from being accidentally deleted. We recommend that you adjust the synchronization protection settings based on the size of your enterprise.

    ![](assets/2ff59193f8e0b8cd38aa8c38bb136c92.jpeg)

  - Failure to import a single data entry does not affect the import of other data entries.

  - You can view the failure information in **synchronization logs**.

- Delegated Authentication: If this feature is enabled, a user can log in to IDaaS by using an LDAP user account and password.

- Automatic Password Update: When a user attempts to log in to IDaaS by using LDAP delegated authentication, if the password of the IDaaS account is empty, the password is automatically updated as the password of the LDAP user. The LDAP password must meet the requirements specified in the password policies of IDaaS. Otherwise, the IDaaS password cannot be automatically updated to the LDAP password.

**Advanced Settings**

- User/Organization  `ObjectClass` : You can use  `ObjectClass`  to define a type of object as a user or organization. For example, the object whose  `ObjectClass is user`  in the query result is considered a user.

> **Important**
>
> LDAP allows flexible customization. If you define the  `ObjectClass`  of a user or organization, make sure that the  `ObjectClass`  in LDAP is consistent with that in IDaaS. This ensures that the data synchronized to  `IDaaS`  meets your expectations.

- User Sign-in ID: When a user attempts to log in to IDaaS by using LDAP delegated authentication, IDaaS uses the attributes to query the user in LDAP and matches the password. If the password is correct, the user is allowed to log in to IDaaS. You can separate multiple attributes with commas (,). In this case, these attributes are in the OR relationship. This means that a user can use one of them to log in to IDaaS. Make sure that multiple attributes correspond to the same LDAP user. Otherwise, the user cannot log in to IDaaS.

- `FILTER`  Statement for Filtering Users: If you want to synchronize specific users from different organizations to IDaaS, you can use a custom  `filter`  statement to filter users. Only users that meet the filter conditions can be synchronized to IDaaS. By default, the  `filter`  statement contains  `ObjectClass`  conditions in the AND relationship. You can click **View Details** to view the complete statement. For more information, see the Filter section of this topic.

![](assets/d60b8dfe91d8d13d6a20681a2fbda455.jpeg)

**Step 3: Configure field mapping**

If you already have accounts or organizations in IDaaS and you want to map them to the LDAP users or organizations, or if you want to use specific fields of an IDaaS account as the fields of an LDAP user, you must configure field mappings. For example, if you want to use the name of an IDaaS account as the mobile phone number of an LDAP user, you must configure a field mapping. For example, you must configure the field mapping if you want to use the mobile phone number of an LDAP user as the name of an IDaaS account.

![](assets/52a47854a49e7bf8cdaee8278997e7ca.jpeg)

For more information, see Field mappings.

**LDAP security configuration**

By default, data is transmitted in plaintext without encryption or protection in LDAP. This may cause data theft. You can use LDAPS or StartTLS to improve the security of data transmission. After you configure a certificate in LDAP, you can use LDAPS or StartTLS in IDaaS. We recommend that you enable LDAPS or StartTLS.

After you configure the certificate, you can obtain the certificate fingerprint in IDaaS to build the trust of IDaaS for the LDAP certificate. This reduces the risk of fake certificates.

![](assets/4df7262fe6dc230a58ab65f2c0f2d73a.jpeg)

**LDAP custom configuration**

**ObjectClass**

`ObjectClass`  in LDAP is a set of attributes. Each object must have an  `ObjectClass` . You can use  `ObjectClass`  to define an object as a user, organization, or computer. For example, as shown in the following figure, if you set **User**  `ObjectClass`  to "inetOrgPerson,posixAccount,top" in IDaaS, IDaaS takes the object as a user.  `ObjectClass` is displayed when you edit an object in LDAP.

![](assets/ab342bf615cdbfb58fd49c47729091c2.jpeg)

> **Important**
>
> LDAP allows flexible customization. If you define the  `ObjectClass`  of a user or organization, make sure that the  `ObjectClass`  in LDAP is consistent with that in IDaaS. This ensures that the data synchronized to IDaaS meets your expectations.

**User Sign-in ID**

When a user attempts to log in to IDaaS by using LDAP delegated authentication, IDaaS uses the attributes to query the user in LDAP and matches the password. If the password is correct, the user is allowed to log in to IDaaS.

You can use one of the attributes such as  `UID` , mobile phone number, email address, and employee number to log in to IDaaS. You can define the attributes when you create identity providers (IdPs) or on the **Delegated Authentication** page. If you use multiple attributes, make sure that the attributes are unique and correspond to the same LDAP user. Otherwise, the user cannot use delegated authentication.

**Filter**

> **Important**
>
> The modifications of the  `ObjectClass`  conditions and the  `filter`  statement affect the filter conditions of the LDAP node. During full data synchronization, IDaaS accounts and organizations that do not meet the filter conditions are deleted. We recommend that you adjust the synchronization protection settings and fully test whether the filtered results meet your expectations before you modify the ObjectClass conditions and the filter statement. For example, you can use another IDaaS instance to perform a test.

**Overview**

If you want to synchronize specific users from different organizations to IDaaS, you can use a custom  `filter`  statement to filter users. Only users that meet the filter conditions can be synchronized to IDaaS. By default, the  `filter`  statement contains  `ObjectClass` conditions in the AND relationship. You can click **View Details** to view the complete statement.

![](assets/d60b8dfe91d8d13d6a20681a2fbda455.jpeg)

You can enter the  `filter`  statement in LDAP Admin to check the filtered results.

![](assets/8cebc4558965d6df1837a21545812d70.jpeg)

The following sections describe the common operators and filter statements for LDAP.

**Common operators**

| Operator | Description | Example |
| --- | --- | --- |
| = | Equal to | (cn=Alice) |
| &gt;= | Greater than or equal to | (pwdLastSet&gt;=1319563845000000000) |
| &lt;= | Less than or equal to | (employeeNumber&lt;=1000) |
| &amp; | AND relationship, which indicates that all conditions must be met | (&amp;(cn=CN\*)(title=RD)) |
| \| | OR relationship, which indicates that at least one condition must be met | (\|(cn=Test\*)(cn=Admin\*)) |
| ! | NOT relationship, which indicates that all conditions must not be met | (!(cn=Test\*)(cn=Admin\*)) |

**Common statements**

| Scenario | Example |
| --- | --- |
| Select users whose usernames start with CN | (cn=CN\*) |
| Select the user with the specified email address | (mail=alice@example.com) |

**LDAP synchronization configuration**

**Obtain Base DN**

Base DN is the path identifier of a node in LDAP. IDaaS performs operations such as queries and data synchronization only within this node. You can set the Base DN of the source node in **Synchronization Direction**.

The format of DN is ou=organization, dc=example, dc=com. The DN of the root node is dc=example, dc=com (your domain). You can also view the DN of the node in LDAP, as shown in the following figure.

![](assets/67980464d90231ff37c5512e27e0f698.jpeg)

If the path of a node changes, the Base DN of the node also changes. To prevent LDAP data synchronization errors caused by node path changes, IDaaS uses the  `ObjectGuid`  of the node as the node fingerprint when you configure the Base DN of the source node in IDaaS. If the changed Base DN of the node does not match the node fingerprint, data synchronization is stopped. You can synchronize data after you reconfigure the source node.

**Scheduled verification**

LDAP does not support queries of incremental data. IDaaS automatically synchronizes full data within the LDAP source node every morning. To synchronize the latest data, you must manually trigger full data synchronization.

IDaaS provides synchronization protection. When more than 30 accounts or more than 10 organizations need to be deleted, the synchronization task is automatically canceled to prevent data from being accidentally deleted. We recommend that you adjust the synchronization protection settings based on the size of your enterprise.

![](assets/9f890a411fa440db8b198f5a7cd43105.jpeg)

<a id="section-1-7"></a>

## 1.7. Bind IDaaS to an OIDC IdP

This topic describes how to configure and use enterprise-level identity providers (IdPs) such as Okta, Azure AD, and self-developed systems to interact with Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) over the OpenID Connect (OIDC) protocol.

**Basic concepts**

After you bind IDaaS to an OIDC IdP such as Okta, Azure AD, or a self-developed system, users can use accounts configured in the IdP to log in to IDaaS EIAM.

| Concept | Description |
| --- | --- |
| OIDC | An upgraded version of the OAuth protocol. The OIDC protocol builds an identity layer based on OAuth 2.0. For more information about common configurations of OIDC, see OIDC SSO configuration. |
| IdP | An identity provider. In this topic, Okta, Azure AD, or a self-developed system works as an IdP. As defined in Security Assertion Markup Language (SAML), an IdP verifies and authenticates a user and returns the authentication result in a SAML response to a service provider (SP). IdP now refers to a unified identity management platform in general. |
| SP | A service provider. In this topic, IDaaS EIAM works as an SP. As defined in SAML, an SP receives a response from an IdP and parses the response to obtain the authentication result. In general, an SP is an application that interacts with an IdP. |
| Federated authentication | An authentication mode in which an SP trusts and uses the authentication result from an IdP. In this topic, IDaaS EIAM trusts the authentication result from Okta, Azure AD, or a self-developed system. Users who pass federated authentication can log on to IDaaS EIAM by using their accounts configured in an IdP. Federated authentication is often used for single sign-on (SSO). |

**Bind IDaaS to an OIDC IdP**

IDaaS EIAM uses the standard authorization code flow of OIDC to implement federated authentication. Therefore, a user can use an account configured in your IdP such as Okta, Azure AD, or a self-managed system to log on to IDaaS EIAM, provided that your IdP supports SSO based on the standard authorization code flow of OIDC.

> **Note**
>
> You can initiate an SSO request only on the logon page of IDaaS EIAM, which works as an SP. In this case, an IdP is displayed as a logon method on the logon page of IDaaS EIAM. You cannot initiate an SSO request from an IdP.

In the process of binding IDaaS to an OIDC IdP, mutual trust is established between IDaaS and the IdP. You must obtain and configure information in both IDaaS and the IdP.

**Step 1: Configure basic information**

**Obtain the configuration information in IDaaS**

1. Go to the details page of your IDaaS EIAM instance. In the left-side navigation pane, click

**IdPs**. On the IdPs page, click **Other IdPs**. In the Add IdP panel, click OIDC IdP.

![](assets/888c6e98807375d119714cdb2f202ff4.png)

2. In the Bind OIDC Identity Provider panel, copy the value of the **IDaaS Redirect URI**

parameter. This uniform resource identifier (URI) is used to receive authentication results and ID tokens. You need to specify this URI when you create an application in your IdP.

![](assets/d914c14391ffb445d28b829a24f8cfc4.png)

**Obtain the configuration information in your IdP**

1. Create an application that supports the OIDC protocol in your IdP and configure the value

of the **IDaaS Redirect URI** parameter that you copied in the previous step as the redirect URI of the application.

2. Obtain the following information and configure the parameters in the Bind OIDC Identity

Provider panel in the IDaaS console:

- Client ID: the client ID that is used to send requests to IDaaS EIAM. Enter the ID of your IdP application.

- Client Secret: the client secret that is used to send requests to IDaaS EIAM. Enter the secret of your IdP application.

- Issuer: the discovery endpoint of the OIDC issuer.

  3. In the Bind OIDC Identity Provider panel, click **Parse** in the Endpoint Configurations

section. Then, the endpoints are automatically entered.

![](assets/8c66cb3a9619491041bf05c7a5aef30d.png)

4. Confirm the configurations and click **Next** to go to the Select Scenario step.

**Step 2: Select a scenario**

In the **Select Scenario** step, you can enable one or more features based on your business requirements.

![](assets/19e2447b9a48e7d78f80e81bb56f73be.png)

- **Federated Authentication**: If you enable this feature, you can implement OIDC-based logon.

- **Manual Account Binding**: After you enable this feature, if the OIDC account of a user is not bound to an IDaaS account, the user can manually bind the two accounts during OIDC-based login. After the two accounts are bound, the user can use the OIDC account to log in to IDaaS EIAM.

- **Automatic Account Binding**: After you enable this feature, if the OIDC account of a user is not bound to an IDaaS account and the field of the IDaaS account has the same value as the field of the OIDC account, the system automatically binds the two accounts. You can set the Mapping Rule parameter to **Select Field** and select a field in the  `ID token` . You can also use an advanced expression to add a custom field. For more information, see Advanced expressions for account fields. After the two accounts are bound, the user can use the OIDC account to log in to IDaaS EIAM.

- **Automatically Create Account:** After you enable this feature, if the OIDC account of a user is not bound to an IDaaS account, an IDaaS account is automatically created during OIDC-based login. The account information is updated each time the user logs in to IDaaS EIAM by using the OIDC account.

- **Specified Organization**: If you log in to IDaaS EIAM by using an OIDC account, the IDaaS account that does not belong to an organization is automatically assigned to the organization that you select. By default, the root organization is selected when you configure this field. You can search for an organization or select an organization from the drop-down list.

- **Automatically Update Information**: After you enable this feature, if you log in to IDaaS EIAM by using an OIDC account, the IDaaS account information is automatically updated based on field mappings.

> **Note**
>
> If you enable both **Manual Account Binding** and **Automatic Account Binding,** the system preferentially performs an automatic account binding during OIDC-based login<strong>.</strong> The Automatic Account Binding feature is available only for IDaaS instances of Trial Edition and Enterprise Edition. If you want to use this feature, make sure that your IDaaS instance meets this requirement in advance.

Confirm the configurations and click **Confirm**.

**Step 3: (Optional) Configure field mappings**

> **Note**
>
> After you turn on **Automatically Create Account** or **Automatically Update Information**, the **Field Mapping** step appears.

![](assets/466219877a1a3f4fda194709cfee2915.png)

> **Important**
>
> If an IDaaS account is created by an IdP such as DingTalk or Azure AD, the account data is updated based on the IdP instead of field mappings.

After you turn on Automatically Create Account, the field values of the IDaaS account are automatically changed based on the values of the fields in the ID token when you log in to

![](assets/1f7c3d1d3a4deacd9e94d1c68d84ee7e.png)

IDaaS EIAM by using an OIDC account.   For example, the display name of the IDaaS account is set to the name in the ID token.

> **Note**
>
> Users can log in to IDaaS EIAM by using an account in the following priority order: an OIDC account that is bound to an IDaaS account, an OIDC account that can be automatically bound to an IDaaS account, and an OIDC account that can be manually bound to an IDaaS account or an IDaaS account that is automatically created.

If an OIDC account is not bound to an IDaaS account or cannot be automatically bound to an IDaaS account, the following dialog box appears. Users can choose to manually bind the OIDC account to an existing IDaaS account or manually create an IDaaS account.

![](assets/34e9a3105bdac1e7dd40262a99fa4d26.jpeg)

> **Important**
>
> You can delete an **OIDC IdP** on the **IdPs** page. After an OIDC IdP is deleted, the related configurations are immediately deleted and **cannot be recovered**, and the related features **become unavailable**.

<a id="section-1-7-1"></a>

### 1.7.1. Bind IDaaS to Okta

This topic describes how to configure and use the enterprise-class identity provider (IdP) Okta to log in to the Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) portal over the OpenID Connect (OIDC) protocol.

**Step 1: Bind IDaaS to Okta**

1. Go to the details page of your IDaaS EIAM instance. In the left-side navigation pane, click

**IdPs**. On the IdPs page, click **Other IdPs**. In the Add IdP panel, click OIDC IdP.

![](assets/888c6e98807375d119714cdb2f202ff4.png)

2. In the **Bind OIDC Identity Provider** panel, enter a display name in the **Nickname** field

and select an authentication mode. Proof Key for Code Exchange (PKCE) provides an additional layer of security. You can enable this mode based on your business requirements. Okta PKCE supports only Secure Hash Algorithm 256 (SHA-256) for generating a code challenge.

![](assets/e8ee07157ac3fc9fcf342f88d7175ae2.jpeg)

3. In the lower part of the panel, copy the value of the **IDaaS Redirect URI** parameter. This

URI is used to receive authentication results and ID tokens that are sent by Okta.

![](assets/d914c14391ffb445d28b829a24f8cfc4.png)

**Step 2: Create an application in Okta**

1. Log in to the admin console of Okta.

2. Choose Applications > Create App Integration.

3. Set the Sign-in method parameter to OIDC - OpenID Connect and the Application type

parameter to Web Application.

4. Configure the App integration name parameter.

5. Paste the value of the IDaaS Redirect URI parameter that you copied in Step 1 in the Sign-

in redirect URIs field.

6. Configure the Controlled access parameter. If the application that you want to create is

used for testing or does not require controlled access, you can select Allow everyone in your organization to access. If you select another option, you must grant permissions to users or groups.

7. Confirm the configurations and click Save. After the application is created, the details page

of the application appears.

**Step 3: Configure the OIDC IdP information**

1. Obtain the following information on the details page of the Okta application and configure

the following parameters in the Bind OIDC Identity Provider panel of the IDaaS console:

- Client ID: On the General tab, click the Copy icon next to the Client ID parameter and paste the copied value in the Client ID field in the Bind OIDC Identity Provider panel. If PKCE is enabled in Step 1, you must select Require PKCE as additional verification in this step.

  ![](assets/289003a927bb178290c4b24d1c7a5c45.jpeg)

- Client Secret: On the General tab, click the Copy icon next to the Client Secret parameter and paste the copied value in the Client Secret field in the Bind OIDC Identity Provider panel.

  ![](assets/f15d9001ed90cedd37764808f63c887d.jpeg)

- Issuer: On the Sign On tab, click Edit in the OpenID Connect ID Token section. Set the Issuer parameter to Okta URL, copy the URL, and then paste the copied URL in the Issuer field in the Bind OIDC Identity Provider panel.

  ![](assets/4c141a9e41affba46176440b661a3d14.jpeg)

> **Note**
>
> The Okta issuer supports the Dynamic mode. To use this mode, perform the following operations: In the admin console of Okta, choose Security > API and copy the issuer URI displayed on the Authorization Servers tab. If you use a self-managed authorization server, you must add access policies for the Okta application.

2. In the Bind OIDC Identity Provider panel, click **Parse** next to the Issuer parameter. Then,

the endpoints are automatically entered.

![](assets/8c66cb3a9619491041bf05c7a5aef30d.png)

3. Confirm the configurations and click Next to go to the Select Scenario step.

**Log in to IDaaS EIAM**

This section describes the process of logging in to IDaaS EIAM by using an Okta account.

1. Click the button for Okta on the login page of IDaaS EIAM.

![](assets/446f91c7ba0464c405bc354994dffeea.jpeg)

2. The system sends an authentication request to Okta. If no Okta account is logged in, the

Okta login page appears. If an Okta account is logged in, you are redirected to IDaaS EIAM.

![](assets/21bbe15e42b239c0784f044624006e19.jpeg)

3. If the Okta account is associated with your IDaaS account, you can directly log in to IDaaS

EIAM. If the Okta account is not associated with your IDaaS account, the system automatically associates with the Okta account. If the association fails, you must manually associate with the Okta account or initiate the system to create an account. For more information, see Step 2: Select a scenario.

<a id="section-1-7-2"></a>

### 1.7.2. Bind IDaaS to Microsoft Entra ID (FKA Azure AD)

This topic describes how to configure and use Microsoft Entra ID, formerly known as Azure Active Directory (AD), as an enterprise-level identity provider (IdP) to log in to the Identity as a Service (IDaaS) portal over the OpenID Connect (OIDC) protocol.

**Step 1: Create an application in Microsoft Entra ID**

1. Create an application.

   <ol type="i">

   <li>

   Log in to the Azure Entra admin center. Enter Microsoft Entra ID into the top search box and click the service.

   </li>

   <li>

   On the **Overview** page, choose **Add > App registration**.

   </li>

   <li>

   On the **Register an application** page, enter an application name, set the Supported

   </li>

   </ol>

   account types parameter to Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox), and then select Web from the Redirect URI drop-down list. Click Register to create an application. The application name is IDaaS.

   <ol type="i" start="4">

   <li>

   The redirect URI is the value of **IDaaS Redirect URI** obtained in Step 3.

   </li>

   </ol>

2. Configure the application.

   <ol type="i">

   <li>

   After you create the application, the **Overview** page of the application automatically appears. You can view the application that you created on the **App registrations > All applications** page.

   > **Note**
   >
   > The value of the Application (client) ID parameter is the client ID of the OIDC application.

   </li>

   <li>

   Add a client credential.

   </li>

   </ol>

   > **Note**
   >
   > The value in the Value column is the client secret of the OIDC application. Save the secret.

   <ol type="i" start="3">

   <li>

   In the left-side navigation pane, click Token configuration. On the Optional claims page,

   </li>

   </ol>

   click **Add groups claim**. In the Edit groups claim panel, add a groups claim. After you add the groups claim, the claim is displayed on the Optional claims page and is named  `groups` .

   Click Add optional claim. In the Add optional claim panel, select claims for ID and access tokens. This way, the OIDC client can obtain the token information. The following figures show the claims.

   <ol type="i" start="4">

   <li>

   Add scopes. In the left-side navigation pane, click **Expose an API**. On the Expose an API page, click Add a scope and add the following scopes:  `User.Read` ,  `User.Read.All` ,  `GroupMember.Read.All` , and  `Group.Read.All` . Configure the scopes based on the configurations shown in the following figures.

   </li>

   <li>

   After you add the preceding scopes, grant permissions to the client application. In the left-side navigation pane, click **API permissions**. On the API permissions page, click Microsoft Graph in the API / Permissions name column.

   </li>

   <li>

   In the Request API permissions panel, select the permissions that your application requires.

   </li>

   </ol>

3. Obtain the endpoint of the OIDC application.

   Choose **Overview > Endpoints** and obtain the https://login.microsoftonline.com/common/v2.0 URL, which is the URL of the OIDC metadata file.

   The key configuration information is obtained.

**Step 2: Bind IDaaS to Microsoft Entra ID**

1. Log in to the IDaaS console and click **Console** in the Actions column of the desired IDaaS instance.

2. On the **IdPs** page, choose **Other IdPs > OIDC IdP**.

**Step 3: Bind IDaaS to an OIDC IdP**

1. **Basic Information**

   <ol type="i">

   <li>

   **Logon Method Icon**: Upload the icon of the IdP, which must be a PNG or JPG file of no larger than 1 MB. We recommend that you set the pixel aspect ratio to 256\*256. The icon is displayed on the login page.

   </li>

   <li>

   **Display Name**: Enter a name for the login method into the **Display Name** field, which is displayed on the login page. During the first time you specify or modify the login method name, the system automatically reviews the name. After the name is approved, the name is automatically applied. The default name or the existing name is displayed during the review.

   </li>

   </ol>

2. **Network Configurations**

   <ol type="i">

   <li>

   **Network Access Endpoint**: Select **Shared Network Access Endpoint** or **Dedicated Network Access Endpoint** based on your business requirements. For more information, see Network endpoints.

   </li>

   </ol>

3. **Logon Settings**

   <ol type="i">

   <li>

   **Grant Types**: Select the OIDC authorization mode to be used. In most cases, the authorization code mode is used. Proof Key for Code Exchange (PKCE) provides an additional layer of security. You can enable PKCE based on your business requirements.

   </li>

   <li>

   **Authentication Method**: You can select any authentication mode.

   <ol type="a">

   <li>

   client_secret_post: Carry the key pair information in POST requests that are sent to an authentication endpoint. This option is selected in most cases.

   </li>

   <li>

   client_secret_basic: Carry the encoded key pair information in the Authorization header of requests.

   </li>

   </ol>

   <ol type="i" start="3">

   <li>

   Client ID: Copy the value of the Application (client) ID parameter in Step 1: Create an

   </li>

   </ol>

   application in Microsoft Entra IDand then paste the value to the Client ID field.

   </li>

   <li value="4">

   Client Secret: Click Add a certificate or secret next to the Client credentials parameter in Step 1: Create an application in Microsoft Entra ID. On the **Client secrets** tab, copy the secret in the Value column and then paste the value into the Client Secret field.

   </li>

   <li>

   Scopes: Select a scope based on your business requirements. If you want to obtain email addresses, select email.

   </li>

   </ol>

4. **Endpoint Configurations**

   <ol type="i">

   <li>

   Issuer: On the Overview page of the application in Step 1: Create an application in Microsoft Entra ID, choose **Endpoints > OpenID Connect metadata document**, copy the URL, and then paste it into the Issuer field.

   </li>

   <li>

   Click **Parse** next to the Issuer field. Then, the endpoints are automatically specified.

   </li>

   <li>

   Confirm the configuration and click **Next** to go to the Select Scenario step. For more

   </li>

   </ol>

   information about the configuration in the Select Scenario step, see Step 2: Select a scenario.

   <ol type="i" start="4">

   <li>

   **IDaaS Redirect URI**: You must specify the URI in the OIDC service in Step 1: Create an application in Microsoft Entra ID.

   </li>

   </ol>

**Step 4: Verify the login process**

This section describes how to log in to IDaaS by using a Microsoft Entra ID account.

1. Click AAD on the login page of IDaaS.

2. Then, the system sends an authentication request to Microsoft Entra ID. If no Microsoft Entra ID account is logged in, the sign-in page of Microsoft Entra ID appears. If a Microsoft Entra ID account is logged in, you are navigated to IDaaS.

3. If the Microsoft Entra ID account is bound to your IDaaS account, you can directly log in to IDaaS. If the Microsoft Entra ID account is not bound to your IDaaS account, the system automatically binds the Microsoft Entra ID account. If the binding fails, you must manually bind the Microsoft Entra ID account or allow the system to create an account. For more information, see Step 2: Select a scenario.

<a id="section-1-8"></a>

## 1.8. Field mappings

You can use field mappings to manage the relationship between different account systems and accounts or organizations in Identity as a Service (IDaaS). This topic introduces the basic concepts related to field mappings and describes how to map fields.

**Terms**

You can use field mappings to synchronize an IDaaS account with an external account.

- Accounts: You can bind accounts to synchronize account status. If you bind a DingTalk user to an IDaaS account after you import users from DingTalk, when you delete the user from DingTalk, the IDaaS account is also deleted.

- Fields: After you bind accounts, you can map the fields of the accounts to synchronize account information. For example, you can use the enterprise email addresses of DingTalk users as the display names of IDaaS accounts when you import users from DingTalk. When the enterprise email address of a DingTalk user is changed, the display name of the IDaaS account is also changed.

> **Note**
>
> You can unbind a DingTalk user from an IDaaS account, organization, or group only after you delete the IDaaS account, organization, or group. You can also bind organizations and map the fields of organizations. However, mapping identifiers are unavailable for organizations.

**Configure field mappings**

You can use the following methods to configure field mappings.

- Configure field mappings when you create an identity provider (IdP). However, you cannot configure field mappings when you create an IdP to synchronize data from DingTalk.

- Configure field mappings when you modify an IdP. On the **IdPs** page, click **Modify Settings**. In the panel that appears, click the **Field Mapping** tab, configure field mappings, and then click Confirm.

![](assets/98b754717e600d48b3327ff9d76a375c.jpeg)

**Configure mapping identifiers**

You can specify a mapping identifier to bind accounts. If the values of the identifier fields of the accounts are the same, the accounts are bound. In most cases, mapping identifiers are used to bind existing accounts. For example, you want to import users from DingTalk to IDaaS and specify a mapping identifier as shown in the following figure. If the enterprise email address of a DingTalk user zh\*\*\*@example.com is the same as the email address of an IDaaS account, the accounts are bound. If none of the existing IDaaS accounts have the same email address, an IDaaS account is created and bound to the DingTalk account. After the accounts are bound, the status and information of the accounts are synchronized.

![](assets/b35670b899b9036a8313d648050cfede.jpeg)

> **Note**
>
> Different mapping identifiers are supported by various IdPs. You can configure one of the fields as a mapping identifier based on your business requirements. You can also remove a mapping identifier or choose not to configure one.

**Configure mapping rules**

You can use one of the following methods to map fields.

- Select a field: Select a field from the synchronization source and use the field value as the value of the destination field. IDaaS provides different fields for different IdPs. If you cannot find a field that you require, you can specify an expression.

- Specify an expression: You can specify an expression to customize the value of a field and use the value as the value of a destination field. You can specify expressions for different scenarios. You can use the email prefix of DingTalk accounts as the IDaaS account name or use a field **that is not provided by IDaaS**. The following examples describe specific common expressions. The following examples describe specific common expressions.

  - Use fields that are not provided by IDaaS:

    - Position of users in DingTalk:  `idpUser.title`

    - Workplace of users in DingTalk:  `idpUser.work_place`

    - Head of department in DingTalk:  `idpOrganizationalUnit.org_dept_owner`

    - For more information about DingTalk fields, see DingTalk user fields and DingTalk department fields.

  - Use email prefixes as field values:

    - Email prefix of users in DingTalk: SubstringBefore(idpUser.email,"@")

    - User Principal Name (UPN) prefix of accounts in Active Directory (AD): SubstringBefore(idpUser.userPrincipalName,"@")

  - Fixed value: Trim("myString")

> **Note**
>
> The fields in IDaaS expressions are in the idp&lt;User/OrganizationUnit>.&lt;Field name in the IdP> format for synchronization to IDaaS, such as  `idpUser.userId` , or in the idp&lt;User/OrganizationUnit>.&lt;Field name in IDaaS> format for synchronization from IDaaS. For more information about the examples of expressions and the expression syntax, see Field expressions of advanced accounts.

If you do not want to map a field, click **Remove** in the Actions column. Then, the Mapping Rule of the field is changed to Disable Mapping, and the data of this field is not synchronized.

<a id="section-1-9"></a>

## 1.9. Introduction to cron expressions

This topic introduces the syntax of cron expressions used in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM), and how to use cron expressions. This helps you better configure cron jobs.

**What is a cron expression?**

A cron expression is a time expression used to configure cron jobs. It is a string that consists of six or seven fields separated by space characters. Each field indicates a time unit.

**Syntax**

1. Cron expressions use the following syntax:

   ```text
    Seconds Minutes Hours Day Month Week Year 
   ```

2. Valid values of each field

   | No. | Time unit | Valid value | Allowed special character |
   | --- | --- | --- | --- |
   | 1 | Seconds | 0 to 59 | - \* / |
   | 2 | Minutes | 0 to 59 | - \* / |
   | 3 | Hours | 0 to 23 | - \* / |
   | 4 | Day of month | 1 to 31 | - \* ? / L W C |
   | 5 | Month | 1 to 12 or JAN to DEC | JAN-DEC - \* / |
   | 6 | Day of week | 0 to 7 (both 0 and 7 indicate Sunday) or SUN to SAT | SUN-SAT - \* ? / L C # |
   | 7 (optional) | Year | Empty or 1970 to 2199 (Year is optional) | , - \* / |

**Special characters**

| Ch ara cte r | Definition | Description |
| --- | --- | --- |
| \* | Represents all values of a field. | If you set the Minutes field to an asterisk (\*), the job is run every minute. |
| ? | Represents all values of a field. You can use this character only in the Day and Week fields because their values affect each other. | If you want to schedule a job to run on the 20th day of each month, you can use the following cron expression: <code> 13 13 15 20 * ? </code>. If you set the Day field to a specific date, such as 20, you must set the Week field to a question mark (<code> ? </code>) instead of an asterisk (<code> * </code>).If you set the Week field to an asterisk (<code> * </code>), the job is run each day of the week instead of on the 20th day of each month. The values of the Week and Day fields affect each other. The expression is invalid. |
| - | Represents a range of values. | If you set the Minutes field to 5-20, the job is run every minute from the 5th minute to the 20th minute of an hour. |
| / | Represents the start time and the interval, which are separated by this character. The job is started at the specified start time and then run at the specified interval. | If you set the Minutes field to 5/20, the job is run at the 5th, 20th, 25th, and 45th minutes of an hour. |
| , | Represents a list of different values. | If you set the Minutes field to 5,20, the job is run at the 5th and 20th minutes of an hour. |
| L | Represents the last day or week.You can use this character only in the Day or Week field. | If you set the Week field to 5L, the job is run on the 5th day of the last week, which is the last Thursday of a month. |
| W | Represents the business days from Monday to Friday. You can use this character only in the Day field. The job is run on the business day nearest to the specified date. | Assume that you have set the Day field to 5W. If the 5th day of a month is Saturday, the job is run on the 4th day of the month, which is Friday, the nearest business day. If the 5th day of a month is Sunday, the job is run on the 6th day of the month, which is Monday. If the 5th day of a month is a business day, the job is run on that day. In addition, the nearest business day is limited to the current month. |
| LW | Represents the last business day of a month, which is the last Friday.You can use these characters together. |  |
| # | Represents the Nth occurrence of a day of the week in a month. You can use this character only in the Week field. | If you set the Week field to 4#2, the second Wednesday of a month is specified, where 4 indicates Wednesday and 2 indicates the second. |

**Examples**

> **Warning**
>
> A job is run at an interval that is specified by a cron expression in IDaaS identity providers (IdPs). We recommend that you specify **an interval of more than 1 hour**. This ensures that the frequency of data synchronization meets your expectations.

| Example | Description |
| --- | --- |
| <code>0 0 */2 * * ?</code> | The job is run every 2 hours |
| <code>0 0 2 1 * ?</code> | The job is run once at 2: 00 on the first day of each month. |
| <code>0 15 10 ? * MON-</code><br><code>FRI</code> | The job is run at 10:15 every day from Monday to Friday. |
| <code>0 0 23 * * ?</code> | The job is run once at 23:00 every day. |
| <code>0 0 1 * * ?</code> | The job is run once at 01:00 every day. |
| <code>0 0 1 1 * ?</code> | The job is run once at 01:00 on the first day of each month. |
| <code>0 0 23 L * ?</code> | The job is run once at 23:00 on the last day of each month. |
| <code>0 0 1 ? * L</code> | The job is run once at 01:00 on every Sunday. |
| <code>0 0 0,13,18,21 * *</code><br><code>?</code> | The job is run once at 00:00, 13:00, 18:00, and 21:00 every day. |
| <code>0 0 10,14,16 * *</code><br><code>?</code> | The job is run once at 10: 00, 14:00, and 16:00 every day. |
| <code>0 0 12 ? * WED</code> | The job is run once at 12:00 on each Wednesday. |
| <code>0 0 12 * * ?</code> | The job is triggered at 12:00 every day. |
| <code>0 15 10 ? * *</code> | The job is triggered at 10:15 every day. |
| <code>0 15 10 * * ?</code> | The job is triggered at 10:15 every day. |
| <code>0 15 10 * * ? *</code> | The job is triggered at 10:15 every day. |
| <code>0 15 10 * * ?</code><br><code>2025</code> | The job is triggered at 10:15 every day in 2025. |
| <code>0 15 10 15 * ?</code> | The job is triggered at 10:15 on the 15th day of every month. |
| <code>0 15 10 L * ?</code> | The job is triggered at 10:15 on the last day of every month. |
| <code>0 15 10 ? * 6L</code> | The job is triggered at 10:15 on the last Friday of every month. |
| <code>0 15 10 ? * 6L</code><br><code>2025-2026</code> | The job is triggered at 10:15 on the last Friday of every month from 2025 to 2026. |
| <code>0 15 10 ? * 6#3</code> | The job is triggered at 10:15 on the third Friday of every month. |

> **Note**
>
> In this example, all time fields, including the year field, can be modified on demand.

<a id="section-2"></a>

# 2.User portal

<a id="section-2-1"></a>

## 2.1. Portal page

This topic describes the features of the Identity as a Service (IDaaS) application portal and how to use the portal. This topic also describes the methods used to access the portal and the procedures for logging in to and logging out of applications.

**Features**

The application portal provides the following features:

1. **Application access**: provides an entry point for quickly accessing authorized applications.

2. **Account information management**: allows you to view and modify personal information and modify security information.

3. **Security center**: allows you to manage and configure multi-factor authentication.

4. **Self-service**: allows you to reset passwords.

**Methods for accessing the portal**

Log in to the IDaaS Console and find the desired IDaaS instance.

1. Click the URL in the **User Portal** column of the IDaaS instance.

2. To obtain the URL of the portal, click **Console** in the **Actions** column of the IDaaS instance. On the right side of the Quick Start page, view the URL in the **IDaaS Sign-In URL** section.

3. Click the URL to redirect to the login page and enter your username and password to log in to the application portal.

**Applications**

1. **Access an application.**

   <ol type="i">

   <li>

   On the Applications page, you can view the applications that the current IDaaS account is authorized to access. If this page is empty, contact the administrator to add an application and grant permissions on the application to you. For more information, see Create Application and Grant permissions on an application.

   ![](assets/7f49a07337de126caf12cc40c1db37a6.jpeg)

   </li>

   <li>

   If a large number of applications are displayed, you can perform a fuzzy search by

   </li>

   </ol>

   application name to quickly find the application that you want to access. .

   <ol type="i" start="3">

   <li>

   Click an application icon to access the application through Single Sign-On (SSO).

   </li>

   <li>

   The number of available application users varies depending on the following scenarios.

   | Scenario | Description |
   | --- | --- |
   | One and only one application user | Users can log in to the application through SSO without the need to perform additional operations. |
   | No application user | If IDaaS cannot authenticate the identity required for SSO, the "No application user found" message appears. In this case, you cannot log in to the application through SSO. .<br>You must contact the administrator to resolve this issue. In this scenario, you cannot add application users. |
   | Multiple application users | You can assume different roles when you use an IDaaS account to access an application. You can select multiple application users to assume different roles. .<br>During SSO (initiated by the IdP) to the portal, if multiple application users are available, you are redirected to the page where you can select an application user. Select an application user to access the application. |

   > **Note**
   >
   > If the SSO process is initiated by the application, you are redirected to the application instead of the portal after you are logged in. You are redirected to the portal page only after you log in to the portal from the Sign-in page. You can specify the application for SSO.

   </li>

   </ol>

2. **Log out of the application**.

   The following table describes scenarios where a logged-on IDaaS user logs out.

   | Scenario | Description |
   | --- | --- |
   | The session expires. | Configurable. For more information, see General settings. |
   | The session times out. | Configurable. For more information, see General settings. |
   | The user manually logs out. | In the IDaaS portal, you can also log out by clicking the Log Out button in the upper-right corner. |
   | The user closes the browser. | After the current browser is closed, your account is automatically logged out of the IDaaS portal. |

   In this case, you must log in again if you want to access any application.

<a id="section-2-2"></a>

## 2.2. Self-service

This topic describes the account management features available in the Identity as a Service (IDaaS) portal, including the basic information, extended information, security settings, and procedures and precautions for binding third-party accounts.

**Overview**

After you log in to the IDaaS portal, you can view and modify your personal information on the **My Account** page, such as the basic information and security settings. For more information about how to log in to the IDaaS portal, see IDaaS portal.

![](assets/803beff599728a3183771db5d86ccdd5.jpeg)

> **Note**
>
> The **My Account** page is unavailable in the IDaaS application on DingTalk. You can open this page only in a browser on your PC.

**Description**

Type

**Field**

**Description**

The username of the account that is used to log in to the portal. The username uniquely identifies the account and can be changed later.

> **Note**
>
> The initial username is left empty for an account that is imported from DingTalk. You must specify a username

Username

> when you create an account in IDaaS.

Basic information

The nickname or name of the user. You can click Change to

Display Name

change the display name.

The fields that are created on the **Account > Field**

Extended

/

**Management** page in the IDaaS console can be displayed

information

in this section.

We recommend that you specify this parameter. This parameter is required in scenarios such as login, password resetting, and two-factor authentication (2FA).

If you do not bind a mobile phone number or an email

Mobile Phone

address, you cannot perform 2FA by default. We

Number

recommend that you bind a mobile phone number or an email address before you enable Bind Two-factor Authentication for Logons. For more information, see Two-factor authentication.

Security

We recommend that you specify this parameter. This

information

parameter is required in scenarios such as login, password resetting, and 2FA.

If you do not bind a mobile phone number or an email

Email Address

address, you cannot perform 2FA by default. We recommend that you bind a mobile phone number or an email address before you enable Bind Two-factor Authentication for Logons. For more information, see Two-factor authentication.

Password

The administrator can determine the password complexity.

Bind external enterprise identities that can be used to log in to the IDaaS portal. You can bind and unbind accounts. Accounts imported from an identity provider (IdP) are bound to IDaaS by default and cannot be unbound.

> **Note**
>
> You cannot bind IDaaS that is automatically bound to

/

> an IdP to another IdP. For example, you cannot bind IDaaS bound to a DingTalk IdP to a WeCom IdP.

Bind Third-Party

> However, you can manually bind IDaaS to different

Account

> IdPs. For example, you can scan a QR code by using WeCom to log in to IDaaS and use OpenID Connect (OIDC)-supported IdP federated authentication to log in to IDaaS.

After the administrator enables 2FA based on one-time

Bind OTP

password (OTP), the user can use this field to bind OTP.

<a id="section-2-3"></a>

## 2.3. Access the IDaaS portal from the DingTalk console

This topic describes how platform employees access the Identity as a Service (IDaaS) portal from the DingTalk console.

**IDaaS and DingTalk integration overview**

The process of associating DingTalk accounts with IDaaS is the same as that of enabling DingTalk third-party applications.

In the process of enabling the IDaaS applications, the administrator specifies the DingTalk contacts that can access IDaaS applications. The accounts of the specified DingTalk contacts can be synchronized to IDaaS, or the accounts can be used to directly access the IDaaS portal from the DingTalk console.

**Associate IDaaS accounts**

All accounts that are imported from DingTalk to IDaaS do not need to be associated with IDaaS. They can be used to access the IDaaS portal from the DingTalk console.

IDaaS accounts that are not imported from DingTalk must be associated with a DingTalk user ID specified by the  `userId`  parameter before the accounts are used to access applications.

You must perform authentication by using a method other than logging in with a QR code. You can access the IDaaS portal only when your account is authenticated.

You do not need to associate the account again.

**Obtain mobile numbers or email addresses from DingTalk**

Accounts that are imported from DingTalk cannot be used to implement some key features of IDaaS, such as two-factor authentication and password resetting, if no mobile number or email address is available.

When you are redirected from the DingTalk console to the IDaaS portal, a message that **requests permissions** on your mobile number or email address is displayed.

After you agree to the request, IDaaS can obtain your mobile number or email address and automatically fill it for the IDaaS account.

<a id="section-2-4"></a>

## 2.4. Login by scanning DingTalk QR codes

This topic describes how to log in to accounts by scanning QR codes, which is a feature of Identity as a Service (IDaaS). Login by scanning QR codes improves security and convenience.

**Prerequisites**

Your account is bound to DingTalk by the IDaaS administrator, and the feature of login by scanning QR codes is enabled. For more information, see Associate IDaaS with DingTalk -outbound direction.

**Login by scanning DingTalk QR codes**

On the login page, select QR Scan Sign-In from Other Methods to go to the page that shows the DingTalk QR code. Use your DingTalk app to scan the QR code.

> **Note**
>
> Note: If QR Scan Sign-In is not displayed, your administrator must go to the login menu to check whether this feature is enabled.

**Possible results after you scan the QR code**

After you scan the QR code by using DingTalk, you may encounter one of the following situations.

1. **QR code login is available**

   When the DingTalk account that you use to log in is bound to IDaaS, the following page appears. After you confirm your login, you are logged in.

2. **IDaaS does not recognize your identity**

   For accounts that are not imported from DingTalk, you must manually bind the accounts to IDaaS to enable login with the QR code.

   After the QR code is scanned, the following page appears. You must select **Use Existing IDaaS User** to proceed to the IDaaS account authentication step.

   You must perform authentication by using a method other than QR Scan Sign-In. After you are authenticated, the DingTalk account is bound to the IDaaS account, and the login succeeds.

   You do not need to bind the account again.

<a id="section-2-5"></a>

## 2.5. General login page

Identity as a Service (IDaaS) provides a login page that allows users to use their IDaaS accounts to log in to the IDaaS user portal or the connected applications.

> **Note**
>
> Each IDaaS instance has a unique login URL, which can be viewed in Quick Start, Accounts, Sign-In, and other pages.

**Login process**

![](assets/27876a891b4f00394cbd96f9e957ad77.jpeg)

The following table describes the three steps in the preceding figure.

| No. | Step | Description |
| --- | --- | --- |
| 1 | Perform two-factor authentication (2FA) | Required only when password-based login is used. For more information, see Two-factor authentication. |
| 2 | Forcibly change the password | This feature will be available later. |
| 3 | Select an application user | Required when the service provider (SP) initiates single sign-on (SSO). After the login, you must select an application identity to initiate SSO. |

**Login page**

![](assets/49b0fd6b09764c5f43f460d569103d87.jpeg)

**Two-factor authentication page**

For more information, see Two-factor authentication.

**Select an application user**

You can assume different roles when you use an IDaaS account to access an application. You can select multiple application users to assume different roles. For more information, see Configure SAML application users.

For SP-initiated SSO, if the logged-in IDaaS account has multiple application users available, you must select one user to log in to the application.

![](assets/d66374d4ef646d3aa903d49a2587fd93.jpeg)

**Login exceptions**

| Security measure | Operation | Exception |
| --- | --- | --- |
| CAPTCHA verification | Password-based login | In a browser, after the login fails once, all logins by using the account name and password must be subject to CAPTCHA verification. |
| Account locking | Password-based login | If an account fails to log in 10 times consecutively within 5 minutes, the account will be locked.<br>If an account supports multiple login methods (such as by using the password and mobile number), the number of login failures by using different login methods are all counted.<br>An account can be unlocked in the following ways.<br>• An account that is locked is automatically unlocked after five minutes.<br>• An administrator can click Unlock in the Actions column on the Accounts page to unlock an account.<br>• An account will be automatically unlocked after you reset the password. (Not supported) |
| SMS or email<br>verification code | Login, 2FA, and password resetting | • You can request a verification code that is sent by email or SMS every 60 seconds. When you are waiting for a verification code that is sent by using one method (SMS or email), you can still request another verification code by using the other method.<br>• The same verification code can be entered for up to 3 times. If you enter an incorrect verification code for three consecutive times, the verification code becomes invalid. You must request another verification code. |

<a id="section-3"></a>

# 3.Accounts

<a id="section-3-1"></a>

## 3.1. Create an account or an organization

This topic describes how to create an account in the Identity as a Service (IDaaS) console. The following table describes the methods that you can use to create accounts.

| Method | Description |
| --- | --- |
| Import accounts from an identity provider (IdP) | You can import accounts from DingTalk, Active Directory (AD), OpenLDAP, and OpenID Connect (OIDC) IdPs. For more information, see IdPs. |
| Call API operations to import accounts | IDaaS provides API operations for account management. Developers can call these API operations to import accounts in batches. |
| Manually create accounts | Administrators can create accounts in the IDaaS console. |

After you import the accounts and organizations, you can manage them on the **Accounts** page.

![](assets/c24b7dfa1380e98f92e495b8c29886c9.jpeg)

<a id="section-3-2"></a>

## 3.2. Manage accounts

Identity as a Service (IDaaS) allows an administrator to view the details of an account and change the account status. .

Log in to the IDaaS console. In the left-side navigation pane, choose User > Accounts and Orgs. On the **Account** page, find the account that you want to manage and click the account name or click **Details** in the Actions column to go to the account details page.

> **Note**
>
> The information about the fields displayed on the account details page is not masked. If you have administrator permissions, you can view all information about the account except the password.

![](assets/9c5f72cbb0cc8f51c7c7f66f83371db4.jpeg)

**User information**

**Basic Information**

The key information you must specify when you create and modify an account.

**Other Information**

The metadata of the account, including the account type, the time when the account is created, and the information about the recent use of the account.

**Third-Party Bindings**

You can manage third-party accounts that are bound to the account. You can also view the binding information. If a user wants to bind their account to other third-party accounts, you can unbind the account from the current accounts as an administrator to allow the user to bind it to other accounts.

> **Note**
>
> If an account is imported from an identity provider (IdP) such as DingTalk or Active Directory (AD) by using data synchronization, the account cannot be manually unbound. If an account is bound to an OpenID Connect (OIDC) IdP or the account is manually bound to an IdP on the My Account page in the IDaaS console, the account can be manually unbound. For example, if you log in to an account and bind the account to DingTalk on the My Account page, you can manually unbind the account.

**OTP Bound**

An administrator can manually unbind a one-time password (OTP) from an account. This way, the account can be bound to another OTP in case of device loss or device change. Each account can be bound to only one OTP authenticator.

![](assets/25e0b25c85c1e4c56ff4aa573b46b9f6.jpeg)

**WebAuthn-registered authenticator**

An administrator can register a WebAuthn authenticator for an account or remove a WebAuthn authenticator from an account.

![](assets/1a44356bbd8da80a71b1b645e0383f83.jpeg)

**View accessible applications**

An administrator can view the applications that the current account is authorized to access.

**Change the status of the account**

In the upper-right corner of the account details page, you can click the buttons to perform the following operations:

- Reset the password

- Disable or enable the account

- Unlock the account

- Delete the account

For more information, see Account lifecycle. .

**Reset the password**

An administrator can reset the password of the specified account. The password must meet the complexity rules. You can click **Generate** to automatically generate a password that meets the complexity rules. You can also click Copy Password to copy the account name and new password and send them to your team members.

![](assets/0160f46aa23dae0712be51586836a258.jpeg)

.

<a id="section-3-3"></a>

## 3.3. Move an account

Identity as a Service (IDaaS) allows you to move an account from an organization to another.

Organizations of an account can be classified into the following types:

- Primary organization: the primary organization to which the account belongs.

- Secondary organization: the secondary organization to which the account belongs.

Generally, the primary organization indicates the position of an account in the organizational structure of an enterprise, and the secondary organizations are used to specify multiple parent organizations for an account. ,

An account inherits the permissions of its parent organizations. The parent organizations include the primary organization and secondary organizations. The primary organization and secondary organizations have no distinction in business logic in IDaaS.

**Specify multiple organizations when you create an account**

When you create an account, the current organization is specified as the primary organization of the account by default. The primary organization cannot be changed.

If you want to change the primary organization, select another organization before you create the account. Alternatively, you can move the account from the primary organization to another after the account is created.

Administrators can specify multiple secondary organizations for the account.

![](assets/d62e020aa52f3549b93a7e54b081b279.jpeg)

**Move an account**

After an account is created, you can move the account from the current primary organization to another and change the secondary organizations of the account.

![](assets/fc31417b949c39154bcef758223bc7ba.jpeg)

In the **Move User** panel, change the primary organization of the account or manage the secondary organizations of the account.

![](assets/33a385b5b5c49072950543950cec89f7.jpeg)

<a id="section-3-4"></a>

## 3.4. Account lifecycle

![](assets/3382cdc386fcaec33fc466407185c985.jpeg)

**Normal**

After an account is created, the account is in the normal state and can use all features.

**Disabled**

If an account is at risk or an employee is on a leave of absence, you can disable the account. You can enable or disable accounts only by using the console or API operations. Account data is not affected when an account is disabled. All features are unavailable to disabled accounts.

**Locked**

**Locked: If the same account fails to use the password to log in for a certain number of consecutive times within the limited time, the account will be locked for a certain period of time. Locked accounts cannot be used for login.**

Unlocked: An account can be unlocked in one of the following situations:

- The account is automatically unlocked when the lock expires.

- An administrator can click Unlock in the Actions column on the **Accounts** page to unlock the account.

<a id="section-3-5"></a>

## 3.5. Field management

This topic describes the field management feature of Identity as a Service (IDaaS), which allows you to view basic fields and configure permissions. This topic also describes how to create, configure, and use extended fields to help administrators flexibly manage user information fields.

**Basic fields**

**Introduction**

Basic fields are system-predefined fields that display the basic information of users, such as the username, email address, and phone number. This feature allows administrators to perform the following operations:

- View the basic fields predefined by the system.

- Configure how the fields are displayed in the user portal.

- Manage the edit permissions of users on specific fields.

**Procedure**

1. **Go to the basic field management page**

   <ol type="i">

   <li>

   Log in to the IDaaS console. Select an IDaaS instance and click **Console** in the Actions column.

   </li>

   <li>

   In the left-side navigation pane, choose **User > Extended Fields**.

   </li>

   </ol>

2. **View editable fields**

   <ol type="i">

   <li>

   On the Basic Fields tab, select **Editable Fields Only** above the list.

   </li>

   <li>

   Then, the list displays only fields that users can edit.

   </li>

   </ol>

3. **Introduction to columns of the basic field list**

   | Column | Description |
   | --- | --- |
   | Field Display Name | The display name of the field in the user interface. |
   | Field ID | The internal identifier of the field. |
   | Data Type | String. |
   | Required | Indicates whether the field is required. |
   | Unique | Indicates whether the field is unique. |
   | User Permissions | Indicates whether the field is invisible, visible, or editable to end users. |
   | Actions | Users can edit only the display name, email, and phone number fields. |

4. **Configure permissions on basic fields**

   <ol type="i">

   <li>

   Find an editable field in the basic field list.

   </li>

   <li>

   Click **Modify** in the Actions column. This button is available only for the Display Name,

   </li>

   </ol>

   Email Address, and Mobile Phone Number fields.

   <ol type="i" start="3">

   <li>

   In the panel that appears, configure user permissions on the field.

   </li>

   </ol>

   - Invisible: The field is invisible to users.

   - Visible: The field is visible to users.

   - Editable: Users are allowed to edit the field.

   <ol type="i" start="4">

   <li>

   Click **Confirm** to save the configuration.

   </li>

   </ol>

> **Note**
>
> Basic fields are system-predefined fields. You cannot delete or add basic fields.

**Extended fields**

**Introduction**

IDaaS allows administrators to create extended fields to store additional account attributes, such as fields that display the employee ID, birthday, and region. Administrators can create and use extended fields on the Extended Fields tab.

> **Note**
>
> Extended fields can be created only for accounts.

**Create an extended field**

Administrators can go to the **Extended Fields** tab and click **Create Field** to create extended fields. The following table describes the parameters for creating an extended field.

| Parameter | Description | Editable |
| --- | --- | --- |
| Field Display Name | The display name of the field. | Yes |
| Field ID | The unique identifier of the field. The identifier can contain lowercase letters and underscores (_). It must start with a lowercase letter. . | No |
| Field Type | The display mode of the field on a page. Valid values:<br>• Input Field<br>• Drop-down List<br>• Check Box | No |
| Field Type:<br>Input Field | If you select Input Field as Field Type, you must specify the following parameters:<br>• Data Type: the data type of the field. You can set the parameter to String or Numeric.<br>• Default Value: the default value that the system uses if no value is specified for the field. This parameter is similar to the <code> DEFAULT </code> parameter in a relational database. | Data Type: No<br>Default Value: Yes |
| Field Type:<br>Drop-down List | • Data Type: the data type of the field. You can set the parameter to String or Numeric.<br>• Data Item: defines key-value pairs for different options in the drop-down list.<br>• To ensure data compatibility, you cannot delete data items. You can only enable or disable data items. If you disable a data item, the data item is removed from the drop-down list. However, the existing data is not affected.<br>• Default Value: the default option for the field.Specify the key of the corresponding data item. | Data Type: No<br>Data Item:<br>• You can add data items.<br>• You can enable or disable data items.<br>• You cannot delete data items.<br>• You cannot modify the key of an option.<br>• You can modify the display name of an option.<br>Default Value: Yes<br>. |
| Field Type:<br>Check Box | Refer to Drop-down List. | Refer to Drop-down List. |
| Field Description | Optional.<br>The description that is shown below the field. | Yes |
| Required | If you select this check box, the field is required when you create or modify an account.<br>Note<br>Note: If you import account data from an existing identity provider (IdP) and select this check box when you create a field, you must add the corresponding field mappings on the <strong>IdPs</strong> page. Otherwise, data synchronization may fail. | No |
| Unique | Specifies whether the field is unique in the current instance. For example, you may select this check box when you create an employee ID field. | No |
| Encryption | To enhance security, IDaaS allows you to encrypt sensitive information before the information is stored in a database. | No |
| User Permissions | Administrators have full permissions on extended fields. In some scenarios, the permissions of users on an extended field must be limited.<br>You can use this parameter to grant the necessary permissions on the current extended field to users.Valid values:<br>• Invisible: The field is invisible to users.<br>• Visible: The field is visible to users but users cannot modify the value of the field.<br>• Editable: The field is visible to users, and users can modify the value of the field. | Yes |

**Specify the values of extended fields**

After you create and enable an extended field, the extended field is ready for use.

Administrators can go to the **Accounts and Orgs** page and click **Create User**. In the panel that appears, click the **Extended Fields** tab and specify the values of all extended fields.

**User self-service**

If you set User Permissions to Visible, users can view the extended field in their IDaaS application portal by performing the following operations: In the left-side navigation pane, click **My Account**. On the page that appears, view the extended fields and their values in the **Extended Information** section.

If you set User Permissions to Editable, users can click Change next to an extended field to modify the value of the field.

**Obtain extended fields**

The following table describes the methods that can be used by an application to obtain the extended fields of an account.

| Method | Description |
| --- | --- |
| Dev/OpenAPI | The application obtains the extended fields of the specified account for data synchronization and management. Developer API or OpenAPI can return all extended fields of the account without additional configurations. For more information, see the corresponding API operation in Developer Guide. |
| id_token or userinfo field for an OIDC-based SSO account | After OpenID Connect (OIDC)-based single sign-on (SSO) is performed, the application can obtain the extended fields of the current account.<br>By default, the extended fields are not returned in the SSO result.Administrators can configure the extended fields to be returned in the extended <code> id_token </code> field. The extended fields obtained from the <code> userinfo </code> field of OIDC are the same as those returned in the <code> id_token </code> field.<br>Configure an extended field in the following format: <code> user.customFieldMap.$Field key$.Field value </code>. |
| Attribute Statements field for an SAML SSO account | After Security Assertion Markup Language (SAML)-based SSO is performed, the application can obtain the extended fields of the current account.<br>By default, the extended fields are not returned in the SSO result.Administrators can configure the extended fields to be returned in the SAML Attribute Statements field. The extended fields are returned in the SAML response. |

<a id="section-3-6"></a>

## 3.6. Advanced expressions for account fields

This topic describes how to use advanced expressions for account fields in a built-in expression engine of Identity as a Service (IDaaS). This topic also provides detailed model fields, functions, and examples.

**Overview**

IDaaS has a built-in expression engine. In Security Assertion Markup Language (SAML) and OpenID Connect (OIDC) applications, you can use advanced expressions to add parameters to the response information. When an application requires additional parameters, and the parameters need to be converted, concatenated, or checked, you can use expressions to process and add the parameters.

Similarly, when you configure the mappings between fields on IDaaS and those from an identity provider (IdP), you can also use expressions to assign values to the fields.

This topic provides examples in the last section to help you understand what the expressions are used for and how to specify expressions.

The following figure shows a single sign-on (SSO) setting for OIDC applications. You can extend fields in the  `id_token`  to be returned. You can enter the advanced expression  `full_phone`  as the value of an extended field to obtain the required results.

![](assets/fa0093f04c87912b5ee5cf29fb8fe1fd.png)

For more information, see SAML 2.0 SSO and OIDC SSO.

An expression consists of the following two parts:

- Model: User that corresponds to an IDaaS account and AppUser that corresponds to an application account.

- Function: execution logic.

**Models**

1. **User**

The following fields are available in the User model. If you want to use one of the following fields in an expression, you can add the user. prefix to the field, such as  `user.username`  or  `user.lockExpireTime` .

| Field Display Name | Field ID | Data Type | Required | Unique | User Permiss ions | Description |
| --- | --- | --- | --- | --- | --- | --- |
| User ID | userId | String | No | Yes | Visible | The user ID. |
| Username | username | String | Yes | Yes | Visible | The username. |
| Display Name | displayName | String | No | No | Editable | The display name of the user. |
| Email Address | email | String | No | Yes | Editable | The email address. |
| Mobile Phone Number | phoneNumb er | Number | No | Yes | Editable | The mobile phone number. |
| Area Code | phoneRegion | Number | No | No | Editable | The country code of the mobile phone number. For example, the country code of China is 86 without 00 or +. |
| External ID | userExternal Id | String | No | Yes | Visible | The external ID of the user. |
| Source Type | userSourceT ype | String | No | No | Visible | The source of the user. Valid values:<br>• build_in<br>• ding_talk<br>• ad<br>• ldap<br>• we_com<br>• lark<br>• idp_auto_build |
| Source ID | userSourceId | String | No | No | Visible | The source ID. |
| Status | status | String | No | No | Visible | The status of the user. Valid values:<br>• enabled<br>• disabled |
| Descriptio n | description | String | No | No | Visible | The description. |
| User Expire Time | accountExpir eTime | Number | No | No | Visible | The time when the user account expires. The value is a UNIX timestamp. Unit: milliseconds. |
| User Register Time | registerTime | Number | No | No | Visible | The time when the user was registered. The value is a UNIX timestamp. Unit: milliseconds. |
| Password Expire Time | passwordEx pireTime | Number | No | No | Visible | The time when the password expires.The value is a UNIX timestamp.Unit: milliseconds. |
| Lock Expire Time | lockExpireTi me | Number | No | No | Visible | The time when the account is unlocked. The value is a UNIX timestamp. Unit: milliseconds. |
| Create Time | createTime | Number | No | No | Visible | The time when the account is created.The value is a UNIX timestamp.Unit: milliseconds. |
| Update Time | updateTime | Number | No | No | Visible | The time when the account was last updated. The value is a UNIX timestamp. Unit: milliseconds. |

2. **App User**

The following field is available in the AppUser model. If you want to use the following field in an expression, you can add the appUser. prefix to the field. The field is then referenced as  `appUser.username` .

| Field | Description |
| --- | --- |
| username | The username of the application account. |

3. **IdP User**

The IdP User model is used to synchronize data between IDaaS and an identity provider. For example, if you want to use the DingTalk workplace field in an expression, you can add the idpUser. prefix to the field. The field is then referenced as  `idpUser.work_place` .

For more information about the fields in the IdP model, see the documentation of the relevant IdP. For example, if the IdP is DingTalk, see the View user details topic of the DingTalk documentation.

> **Important**
>
> If you want to use an expression to bind IDaaS to an OIDC IdP, you must add the  `idpUser.` prefix to the sub, phoneNumber, and email fields in the  `id_token` , such as  `idpUser.sub` , and add the  `idpUser.rawUserInfo.` prefix to the remaining fields, such as `idpUser.rawUserInfo.aud` . For more information, see Bind IDaaS to an OIDC IdP.

**Functions**

The following table describes the available functions and the corresponding examples.

| Functi on | Definition | Description | Example |
| --- | --- | --- | --- |
| Append | Append(str1, str2,..., strn) | Concatenates input strings into a new string, which is the result of <code> str1+str2+... </code>. | • Input: <code> Append("str1", </code> <code>"@example.com") </code>.<br>• Output: <code> str1@example.com </code>. |
| Join | Join(source1, source2, ..., sourceN, separator) | Combines multiple source values into a string. The source values are separated by a delimiter (;). | • Input: <code> Join("str1", </code> <code>"str2", 123,"-") </code>.<br>• Output: <code> "str1-str2-</code><code>123" </code>. |
| Coalesc e | Coalesce(source1, source2, ..., sourceN, defaultValue) | Returns the first non-null value among the specified arguments. If all arguments are null, Coalesce returns NULL. A non-null argument is greater than 0 in length. | • Input: <code> Coalesce("", </code> <code>user.phoneRegion,</code> <code>"86") </code>.<br>• Output: If the country code of the mobile phone number is empty, <code> 86 </code> is returned. |
| IIF | IIF(condition, whenTrue, whenFalse) | Performs a ternary operation.The IIF function returns whenTrue if the condition evaluates to TRUE, and returns whenFalse if the condition evaluates to FALSE. | Example 1:<br>• Input: <code> IIF(true, 1, 2) </code>.<br>• Output: <code> 1 </code>.<br>Example 2:<br>• Input: <code> IIF(false, 1, </code><br><code>2) </code>.<br>• Output: <code> 2 </code>. |
| IsNull | IsNull(value) | Returns true if the value is null. | Example 1:<br>• Input: <code> IsNull(null) </code>.<br>• Output: <code> true </code>.<br>Example 2:<br>• Input: <code> IsNull("") </code>.<br>• Output: false. |
| IsNullOr Empty | IsNullOrEmpty(valu e) | Returns true if the value is null or an empty string. | Example 1:<br>• Input: <code>IsNullOrEmpty(user.email</code><code>) </code>.<br>• Output: If no email address is specified, <code> true </code> is returned.<br>Example 2:<br>• Input: <code> IsNullOrEmpty("") </code>.<br>• Output: <code> true </code>. |
| Now | Now() | Returns the current date and time in UTC in the yyyy-MM-dd'T'HH:mm:ssXXX format. | • Output: 2021-11 01T09:52:11Z. |
| StringR eplace | StringReplace("hell o $VariableName", "$VariableName", ReplaceString) | Replaces characters or substrings with other characters or substrings in the desired string. | • Input: <code>StringReplace("hello</code><br><code>$str", "$str",</code> <code>"world") </code>.<br>• Output: <code> hello world </code>. |
| Trim | Trim(source) | Removes all leading and trailing whitespace characters from the source string. | • Input: <code> Trim(" 123 ") </code>.<br>• Output: <code> 123 </code>. |
| TrimLef t | TrimLeft(source) | Removes whitespace characters from the left side of the source string. | • Input: <code> TrimLeft(" 123 </code> <code>") </code>.<br>• Output: <code> 123 </code>. |
| TrimRig ht | TrimRight(source) | Removes whitespace characters from the right side of the source string. | • Input: <code> TrimRight(" 123 </code> <code>") </code>.<br>• Output: <code> 123 </code>. |
| ToLowe r | ToLower(source) | Converts the source string to uppercase or lowercase. | • Input: <code> ToLower(" Abc </code> <code>") </code>.<br>• Output: <code> abc </code>. |
| ToUppe r | ToUpper(source) | Converts the source string to uppercase. | • Input: <code> ToUpper(" Abc </code> <code>") </code>.<br>• Output: <code> ABC </code>. |

<table>
  <tr>
    <td>Substri ng</td>
    <td>Substring(source, fromIndex, endIndex)</td>
    <td>Returns a substring of the source string. The index of the substring is in the [fromIndex, endIndex] format.<br>• source: The source string, which is required. The value of the source string can be of any data type supported by the syntax.<br>• fromIndex: Required. The value of this parameter must be of the integer type. If the value of this parameter is not of the integer type, null is returned.<br>• endIndex: Required. The value of this parameter must be of the integer type. If the value of this parameter is not of the integer type, null is returned.</td>
    <td>Example 1:<br>• Input: <code>Substring("0123456", 1,</code><br><code>5) </code>.<br>• Output: <code> 1234 </code>.<br>Example 2:<br>• Input: <code>Substring("0123456", -</code><code>1, 7) </code>.<br>• Output: <code> 0123456 </code>.<br>Example 3:<br>• Input: <code>Substring("0123456",</code> <code>"1", 5) </code>.<br>• Output: null.</td>
  </tr>
  <tr>
    <td>Substri ngBefor e</td>
    <td>SubstringBefore(so urce, subString)</td>
    <td>Returns the substring before the first string matched from left to right in the source string.If the string does not exist, null is returned.<br>Parameters:<br>• source: The source string, which is required. The value of the source string can be of any data type supported by the syntax.<br>• target: The string that you want to match, which is required. The value of the string can be of any data type supported by the syntax.<br>Return value: a value of the STRING data type.</td>
    <td>Example 1:<br>• Input: <code>SubstringBefore("test@ex</code> <code>ample@com", "@") </code>.<br>• Output: <code> "test" </code>.</td>
  </tr>
  <tr>
    <td>Array</td>
    <td>Array(source1, source2,...)</td>
    <td>Combines multiple values into an array. The value can be of the Object type.</td>
    <td>• Input: <code> Array(1, 2, 3) </code>.<br>• Output: <code> [1, 2, 3] </code>.</td>
  </tr>
  <tr>
    <td>ArrayAd d</td>
    <td>ArrayAdd(Array(), "test")</td>
    <td>Adds another array to an array.</td>
    <td>• Input: <code> ArrayAdd(Array(), </code> <code>"test") </code>.<br>• Output: <code> ["test"] </code>.</td>
  </tr>
  <tr>
    <td>ArrayM ap</td>
    <td>ArrayMap($ArrayOb ject, __item.ObjectPrope rty)</td>
    <td>Obtains the values of an attribute in an array and returns a new array that contains the obtained values.</td>
    <td>Obtains the IDs of the groups to which the user belongs.<br>• Input: <code>ArrayMap(user.groups,</code> <code>__item.groupId) </code>.<br>• Output: <code>["groupId1","groupId2","</code> <code>groupId3"] </code>.</td>
  </tr>
  <tr>
    <td>ArrayIn dex</td>
    <td>ArrayIndex(Array(), n)</td>
    <td>Obtains elements from an array at a specific index starting from 0.</td>
    <td>• Input: <code>ArrayIndex(Array(1,2,3),</code><br><code>0) </code>.<br>• Output: <code> 1 </code>.</td>
  </tr>
  <tr>
    <td>ArrayJoi n</td>
    <td>ArrayJoin(Array(), str)</td>
    <td>Concatenates the elements of an array into a string by using a specified delimiter.</td>
    <td>• Input: <code>ArrayJoin(Array(1,2,3),</code> <code>"-") </code>.<br>• Output: <code> "1-2-3" </code>.</td>
  </tr>
  <tr>
    <td>Object</td>
    <td>Object(key1, value1, key2, value2, ...)</td>
    <td>Creates an object by using a specified key-value pair.<br>The number of parameters can be 0 or an even number.</td>
    <td>• Input: <code> Object("key1", </code> <code>"value1", "key2",</code> <code>"value2") </code>.<br>• Output:<br><code>{"key1": "value1",</code><br><code>"key2": "value2"}</code></td>
  </tr>
  <tr>
    <td>ObjectI ndex</td>
    <td>ObjectIndex(user, "username")</td>
    <td>Specifies the value of an attribute of an object.</td>
    <td>The code <code> ObjectIndex(user, </code> <code>"username") </code> is equivalent to <code> user.username </code>.</td>
  </tr>
  <tr>
    <td>ObjectT oJsonSt ring</td>
    <td>ObjectToJsonString(user.groups)</td>
    <td>Converts an object into a JSON string.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Contain s</td>
    <td>Contains(str1,str2)</td>
    <td>Checks whether a string contains a specified substring.If the string contains a specified substring, true is returned.Otherwise, false is returned.</td>
    <td>Example 1:<br>• Input: <code> Contains("test", </code> <code>"t") </code>.<br>• Output: <code> true </code>.<br>Example 2:<br>• Input: <code> Contains("test", </code> <code>"a") </code>.<br>• Output: <code> false </code>.</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Or(true,false,...,true)</td>
    <td>Represents the OR operator and must contain at least two conditions. If a condition is evaluated as true, true is returned. If all specified conditions are evaluated as false, false is returned.</td>
    <td>Example 1:<br>• Input: <code> Or(true,false) </code>.<br>• Output: <code> true </code>.<br>Example 2:<br>• Input: <code> Or(true,true,false) </code>.<br>• Output: <code> true </code>.<br>Example 3:<br>• Input: <code> Or(false,false) </code>.<br>• Output: <code> false </code>.</td>
  </tr>
  <tr>
    <td>And</td>
    <td>And(true,false,...,tru e)</td>
    <td>Represents the AND operator and must contain at least two conditions. If all specified conditions are evaluated as true, true is returned. If a condition is evaluated as false, false is returned.</td>
    <td>Example 1:<br>• Input: <code> And(true,false) </code>.<br>• Output: <code> false </code>.<br>Example 2:<br>• Input: <code> And(true,true,false) </code>.<br>• Output: <code> false </code>.<br>Example 3:<br>• Input: <code> And(true,true,true) </code>.<br>• Output: <code> true </code>.</td>
  </tr>
  <tr>
    <td>xOr</td>
    <td>xOr(true,false,...,tru e)</td>
    <td>Represents the XOR operator and can contain only two conditions.<br>If both conditions are the same, false is returned.<br>If one condition is true and the other condition is false, true is returned.</td>
    <td>Example 1:<br>• Input: <code> xOr(true,false) </code>.<br>• Output: <code> true </code>.<br>Example 2:<br>• Input: <code> xOr(true,true) </code>.<br>• Output: <code> false </code>.<br>Example 3:<br>• Input: <code> And(false,false) </code>.<br>• Output: <code> false </code>.</td>
  </tr>
  <tr>
    <td>StartsW ith</td>
    <td>StartsWith(str1, str2)</td>
    <td>Checks whether a string starts with a specified prefix and can contain only two parameters.</td>
    <td>Example 1:<br>• Input: <code>StartsWith("test",</code> <code>"t") </code>.<br>• Output: <code> true </code>.<br>Example 2:<br>• Input: <code>StartsWith("test",</code> <code>"e") </code>.<br>• Output: <code> false </code>.</td>
  </tr>
  <tr>
    <td>Split</td>
    <td>Split("str1,str2,str3")</td>
    <td>Returns an array after the string is split.</td>
    <td>Example 1:<br>• Input: <code>Split("str1,str2,str3","</code><code>,") </code>.<br>• Output: <code> Array(str1,str2,str3) </code>.</td>
  </tr>
  <tr>
    <td>Equals</td>
    <td>Equals(str1,str2)</td>
    <td>Compares two strings to determine whether the strings are the same.<br>Equals(str1,str2)<br>The Equals(str1,str2,false) function is used to check whether two strings are the same while considering case sensitivity.<br>The Equals(str1,str2,true) function is used to check whether two strings are the same without considering case sensitivity.</td>
    <td>Example 1:<br>• Input: <code> Equals("test","Test") </code>.<br>• Output: <code> false </code>.<br>Example 2:<br>• Input: <code>Equals("test","Test",tru</code><br><code>e) </code>.<br>• Output: <code> true </code>.<br>Example 3:<br>• Input: <code>Equals("test","Test",fal</code> <code>se) </code>.<br>• Output: <code> false </code>.</td>
  </tr>
  <tr>
    <td>Current TimeMil lis</td>
    <td>CurrentTimeMillis()</td>
    <td>Returns the current UNIX timestamp. Unit: milliseconds.</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SamlArr ay</td>
    <td>SamlArray(Array())</td>
    <td>Converts an array into elements in a SAML response.Only SAML SSO is available.</td>
    <td>Input:<br><code>SamlArray(Array("group1","</code><br><code>group2"))</code><br>• SAML response output:<br><code>&lt;saml2:Attribute</code><br><code>Name="grouIdArray"</code><br><code>NameFormat="urn:oasis:name</code><br><code>s:tc:SAML:2.0:attrname-</code><br><code>format:unspecified"&gt;</code><br>&lt;saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xsi:type="xsd:string" &gt;<br>group1<br><code>&lt;/saml2:AttributeValue&gt;</code><br><code> &lt;saml2:AttributeValue </code>xm lns:xsi="http://www.w3.org/200 1/XMLSchema-instance" xsi:type="xsd:string"&gt;<br>group2<br><code>&lt;/saml2:AttributeValue&gt;</code><br>• Input: <code>SamlArray(Array("group1"</code><code>,"group2")) </code>.<br>• SAML response output:<br><code>&lt;/saml2:Attribute&gt;</code></td>
  </tr>
</table>

**Examples**

| Scenario | Sample expression |
| --- | --- |
| Append "@example.com" to a username. | <code>Append(user.username, "@example.com")</code> |
| Return the specified email address.<br>Return a mobile number if no email address is specified. | <code>Coalesce(user.email, user.phoneNumber)</code> |
| Use the default mobile phone number if no mobile phone number is specified. | <code>IIF(IsNullOrEmpty(user.phoneNumber), "1888888****",</code><br><code>user.phoneNumber)</code> |
| Concatenate the country code of a mobile phone number and the mobile phone number with a hyphen (-). | <code>Join(user.phoneRegion, user.phoneNumber, "-")</code> |
| Return a custom welcome message that contains the display name of a user. | <code>StringReplace("hello $DisplayName", "$DisplayName",</code><br><code>user.displayName)</code> |
| Replace the middle four digits of a mobile phone number with asterisks (\*). | <code>Append(</code><br><code>SubString(user.phoneNumber, 0, 4),</code><br><code>"****",</code><br><code>SubString(user.phoneNumber, 8, 10)</code><br>) |
| Extract the username from an email address. | <code>SubstringBefore(user.email, "@")</code> |
| Assemble the email field in the array format in SCIM specifications. | <code>Array(Object("email", user.email, "type", "work",</code><br><code>"primary", true))</code> |

Sample User model in JSON:

```json
{
  "customFieldMap": {
        "place": {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        "age": {
            "fieldName": "age",
            "fieldValue": "18"
        }
    },
    "identityProviderUserMap": {
        "idp_m2gngriuenktdkxxxxxx": {
            "identityProviderId": "idp_m2gngriuenktdkxxxxxx",
            "identityProviderType": "ding_talk",
            "identityProviderExternalId": "corp_1234xxxxxxx",
            "identityProviderUserId": "b2ed5fc0xxxxx"
        }
    },
    "organizationalUnits": [
        {
            "organizationalUnitId": "ou_sdfadtaaxxxxxx",
            "organizationalUnitName": "name_001",
            "primary": false
        },
        {
            "organizationalUnitId": "ou_werttxxxxxx",
            "organizationalUnitName": "name_002",
            "primary": true
        }
    ],
    "primaryOrganizationalUnitId": "ou_werttxxxxxx",
    "customFields": [
        {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        {
            "fieldName": "age",
            "fieldValue": "18"
        }
    ],
    "groups": [
        {
            "groupId": "group_jp6al4sn4n4wjgjxxxxxx",
            "groupName": "group1",
            "groupExternalId": "group_jp6al4sn4n4wjgjxxxxxx"
        },
        {
            "groupId": "group_vavikcxewkf5h3oxxxxxx",
            "groupName": "group2",
            "groupExternalId": "group_vavikcxewkf5h3oxxxxxx"
        }
    ],
  "userId": "user_x3zyd6cxxxxxxxxxxxxx",
  "username": "name_001",
  "displayName": "displayname_001",
  "passwordSet": true,
  "phoneRegion": "86",
  "phoneNumber": "333xxxx3333",
  "phoneNumberVerified": true,
  "email": "xxxxx@example.com",
  "emailVerified": true,
  "userExternalId": "b2ed5fc0xxxxxxxxxx",
  "userSourceType": "ding_talk",
  "userSourceId": "corp_1234xxxxxxx",
  "status": "enabled",
  "accountExpireTime": "-1",
  "passwordExpireTime": "-1",
  "registerTime": "1730454581598",
  "lockExpireTime": "-1",
  "createTime": "1730454582379",
  "updateTime": "1733479455307"
}
```

<a id="section-3-7"></a>

## 3.7. Manage organizations

In Identity as a Service (IDaaS), you can manage organizations by using a tree structure. The organizations in IDaaS are equivalent to the departments in DingTalk and organizational units (OUs) in Active Directory (AD). An administrator can import organization trees from existing systems, such as DingTalk and AD, into IDaaS.

An organization tree allows you to perform the following operations:

1. View and manage the actual organizational structure of your enterprise.

2. Grant a permission to an organization node. After you grant a permission to an organization node, all accounts that belong to the node have the permission.

3. Specify the scope of synchronization and synchronize the data of organizations or accounts that belong to a specific node to an external node or synchronize the data from external nodes to the destination node.

**Manage organizations**

Log on to the IDaaS console. On the Employee Identity and Access Management (EIAM) page, click the required instance. In the left-side navigation pane, choose **Accounts** > Accounts and Orgs. The organization tree is displayed on the left, and the accounts or child organizations that belong to the current organization are displayed on the right.

Click an organization in the **organization tree** on the left to manage the organization. By default, the root organization is selected, and the accounts and organizations that belong to the root organization are listed on the right.

After you switch to the organization list on the right, you can perform the following operations on the organizations:

- Create an organization.

- Modify or move an organization.

- Delete an organization.

**Create, modify, or move an organization**

Click **Create Organization**. In the dialog box that appears, select the parent organization for the organization you want to create, and enter an organization name to create the organization.

You can modify the organization name. To move an organization, select the parent organization to which you want to move the organization.

> **Important**
>
> By default, if an organization has child organizations or accounts, the organization cannot be deleted.
>
> If you want to delete an organization node and all child organizations and accounts that belong to the node, you can select Forcible Delete Subordinate Organizations and Users. After you click Confirm, all information about the current node and the child organizations and accounts that belong to the node are deleted. If you want to delete data that is imported by mistake, or delete test data before you use the production data, you can use this feature. You cannot restore deleted data. Proceed with caution. IDaaS dynamically analyzes a deletion operation based on your environment. If the deletion operation is considered risky, two-factor verification is required to ensure data security. The system sends a verification code to the phone number provided by the user. The user must enter the verification code to complete the verification before the user can delete the organization.

**Relationship between accounts and organizations**

An account must belong to only one organization node.

When you create an account, you can specify the organization node to which the account belongs. You can change the organization node of the account later.

<a id="section-3-8"></a>

## 3.8. Manage groups

In Identity as a Service (IDaaS), you can add accounts to a group to manage the permissions of the accounts in a centralized manner. Administrators can add accounts of the same position or role to a group and grant access permissions on an application to the accounts in the group. For example, administrators can grant the access permissions on the sales management system to sales staff in a group. In IDaaS, a group is parallel to an account and an organization. A group does not belong to an organization node. Administrators can add an account of a random organization node to a group.

On the **Group** page, administrators can perform the following basic group management operations.

- Create or modify a group.

- Manage members.

- Delete a group.

![](assets/2c7353e7bd0b8755e390556319d4a0c3.png)

**Create a group**

Administrators can specify a group name to create a group.

![](assets/9fa683a50f978c3dae9f80f475d2f759.png)

> **Note**
>
> The External ID parameter is optional. The external ID is the unique identifier of a group. If you do not specify an external ID, IDaaS automatically generates an external ID.

**Manage members**

After you create a group, you can add members to the group. On the Group page, find the group that you want to manage and click **Manage Members** in the Actions column. The group management page appears.

![](assets/fe2c36d0a1fef7586cfdcdcbe12cd885.png)

Click Add Member. In the Add Group Member dialog box, search for the account that you want to add to the group.

![](assets/096bd5ec0945b62e80c7713f24265b93.jpeg)

Click **Save**.

**Grant access permissions on an application by group**

This section describes how to grant the access permissions on an application to accounts in a group as an administrator.

On the Applications page, click the application that you want to access. On the page that appears, click the **Sign-In** tab and click the **Authorize** tab. Then, click **Authorize**. In the Authorize dialog box, click the Group tab. Search for the group to which you want to grant the access permissions on the application. Then, click **Confirm**.

![](assets/24d48ac49234b78335b8fb6e7ad23209.jpeg)

The members in the group can access the application.

**Delete a group**

Administrators can delete a group. After a group is deleted, IDaaS removes all members from the group, and permissions are revoked from the accounts in the group. However, the accounts are not deleted.

![](assets/e55146afd939b908a492e9e15dbea829.jpeg)

<a id="section-3-9"></a>

## 3.9. Synchronize accounts

This topic describes how to use Identity as a Service (IDaaS) to synchronize data and integrate upstream and downstream data.

IDaaS can be used as a downstream system or an upstream system. You can synchronize upstream accounts such as DingTalk and Active Directory (AD) accounts to IDaaS. You can also synchronize accounts from IDaaS to applications such as Alibaba Cloud-related and self-developed applications.

![](assets/98287bf241c2946b2be1cfb096799e1e.png)

IDaaS allows you to synchronize data in two directions:

- Inbound: Data is synchronized from stakeholders to IDaaS.

- Outbound: Data is synchronized from IDaaS to stakeholders.

The two-way data synchronization feature of IDaaS allows you to distribute data changes in AD or DingTalk to all stakeholders by using IDaaS.

**Inbound synchronization**

The following table describes the inbound synchronization methods that are supported by IDaaS.

| Inbound synchronization method | Source | Description |
| --- | --- | --- |
| Synchronization from identity providers (IdPs) | IdPs | IDaaS supports data synchronization from DingTalk, WeCom, AD, and OpenLDAP. For more information, see IdPs.<br>If you want to synchronize data from non-standard IdPs, such as self-developed Identity and Access Management (IAM) and HR systems, to IDaaS, contact the IDaaS team to learn how to synchronize data by using the connector service. |
| Synchronization by using lazy loading | Multiple types | If lazy loading or Just-in-Time (JIT) Provisioning is used, each account is synchronized to IDaaS the first time the account is used to log in to IDaaS.<br>IDaaS supports data synchronization from OIDC IdPs. Standard IdPs are supported, such as Okta and Azure AD. |
| File-based import | Unlimited | Accounts can be imported to IDaaS by using a CSV file. For more information, see Use a file to import or export data. |
| Synchronization by using Developer API operations | Applications | IDaaS provides Developer API operations to facilitate the integration with custom applications. For more information, see Developer Guide &gt; List of operations by <strong>function</strong>. |
| Synchronization by using API operations | Multiple types | IDaaS provides OpenAPI operations that can be used by developers to import multiple accounts at a time. For more information, see <strong>Developer</strong> <strong>Guide &gt; List of operations by function</strong>. |
| Synchronization based on the System for Cross-domain Identity Management (SCIM) protocol (not supported) | Applications | Some international applications support the SCIM protocol. |

**Outbound synchronization**

The following table describes the outbound synchronization methods that are supported by IDaaS.

| Outbound synchronization method | Destination | Description |
| --- | --- | --- |
| Synchronization to IdPs | Terms related to identity providers | IDaaS supports data synchronization to DingTalk, including DingTalk Standard and DingTalk Enterprise.<br>IDaaS does not support data synchronization to other IdPs such as AD, OpenLDAP, WeCom, and Lark. |
| File-based export | Unlimited | Accounts can be exported to a CSV file. For more information, see Use a file to import or export dataUse a file to import or export data. |
| Data push to applications by IDaaS | Applications | IDaaS can push data to applications in a fixed format.<br>• IDaaS can push data to applications by using event callbacks. For more information, see Synchronize accounts - IDaaS event callback.<br>• IDaaS can push data to applications over the SCIM protocol. For more information, see Synchronize IDaaS accounts to an application by using SCIM.<br>• Some applications in the marketplace provide fixed API operations for synchronization. The API operations can be pre-integrated with IDaaS for quick configuration and easy use. |
| Data fetch from IDaaS | Applications | Applications can call developer API operations to obtain information of multiple accounts and organizations at a time for synchronization. For more information, see <strong>Developer Guide &gt; List</strong> <strong>of operations by function</strong>. |

<a id="section-3-10"></a>

## 3.10. Import files and export data

This topic describes how to import a file to Identity as a Service (IDaaS) and export data from IDaaS.

**Scenarios**

| Category | Operation |
| --- | --- |
| Import | • Import accounts to IDaaS by using a file. You can import the files of accounts that are exported from IDaaS Enterprise Identity Access Management (EIAM) 1.0.<br>• Import organizations and groups to IDaaS by using a file. This feature will be available soon. |
| Export | • Export accounts to a file.<br>• Export organizations and groups to a file. This feature will be available soon. |

**Procedure**

Log in to the IDaaS console. On the EIAM page, click the required instance. In the left-side navigation pane, choose **Accounts > Accounts and Orgs**. On the page that appears, import or export data.

![](assets/0b315a093b6d515ed876cb0a7b2af201.png)

**Import accounts**

**Create an import task**

1. Choose **Import > Import Account**. In the Import Account panel, create an import task. You can import accounts by using a file of the IDaaS EIAM 2.0 Template type. If you want to import IDaaS EIAM 1.0 accounts, select IDaaS EIAM 1.0 Template. Make sure that files of the IDaaS EIAM 1.0 Template type and the IDaaS EIAM 2.0 Template type have the same organization path. Otherwise, you cannot import accounts. The files of the IDaaS EIAM 2.0 Template type must be in the CSV format, and the files of the IDaaS EIAM 1.0 Template type must be in the XLS format.

   ![](assets/7cff82c07ef1fc81743bb1dfedccd2c7.png)

   > **Note**
   >
   > - The IDaaS EIAM 2.0 template provides basic and extended fields.
   >
   >   The username and organizationalUnitPath basic fields are required. If you configure the phoneNumber field, you must also configure the phoneRegion field. The remaining fields are optional. You cannot delete the fields in the IDaaS EIAM 2.0 template. Otherwise, you cannot import accounts.
   >
   >   The extended field must be in the customFieldMap.Name of the extended field format. The format of the extended field is separately specified by the customer.
   >
   >   If the value of an optional field is empty, the field is skipped when the account information is updated. This way, existing field data is not affected.
   >
   > - You can obtain the organization path on the **Organization** tab of the **Accounts and Orgs** page.
   >
   >   ![](assets/99846c2c430738dce689069246c2a3f0.png)

2. Configure parameters, such as Initial Password and Select Unique Identifier, to complete the initialization settings of passwords and existing accounts.

   - Initial Password: After you import a file to create an account, you can set the Initial Password parameter to Do Not Configure Initial Password or Use Initial Password Policy. If you set the Initial Password parameter to Do Not Configure Initial Password, you can use password-free login methods such as DingTalk QR codes and text message verification codes. If you set the Initial Password parameter to Use Initial Password Policy, you must select Enable Password Initialization. Existing accounts in IDaaS are not affected.

   - Select Unique Identifier: If you import accounts by using a file, IDaaS accounts are created. You must select a value from the Select Unique Identifier drop-down list for the existing accounts in IDaaS. After you select a field, the IDaaS account information is updated if the field value exists in the file that you import. In this case, no account is created to ensure compatibility with existing data.

   - Description: You can view the description of the import task on the **Import Record** tab. We recommend that you configure this parameter to distinguish different import tasks.

3. Confirm the configurations and click **Import**.

   > **Important**
   >
   > You can only create and modify accounts. You cannot delete accounts.
   >
   > The import operation is irreversible. To prevent impacts on existing accounts, we recommend that you import a small amount of data to verify the import effect before you import the full data.

**View import records**

On the **Import Record** tab, you can view the import records in the last two years and download the file of the task details within seven days.

![](assets/53d999d6ba93befde3f9d927e7348d2c.jpeg)

**Export accounts**

**Create an export task**

Choose **Export > Export Account**. On the Create Task tab of the Export Account panel, configure the **Export Scope** and **Description** parameters. You can specify the **export scope** by selecting organizations and groups. You can export only data within the specified range.

![](assets/206458563453ee46af348e45aa01be69.jpeg)

**View export records**

On the **Export Records** tab, you can view export records in the last two years and download the file of the task details within seven days.

![](assets/78d95d82039a89b1fd277520fdd88b17.png)

<a id="section-4"></a>

# 4.Applications

<a id="section-4-1"></a>

## 4.1. Create Application

<a id="section-4-1-1"></a>

### 4.1.1. Application overview

In Identity as a Service (IDaaS), applications provide access to the systems and services of your businesses. You can implement single sign-on (SSO) for applications and synchronize accounts between IDaaS and your applications.

In IDaaS, applications are classified into the following types:

| Priority | Application type | Description |
| --- | --- | --- |
| 1 | Marketplace | The pre-integrated application templates provided by IDaaS. You can activate and access the applications from the application marketplace. More pre-integrated templates will be available in the IDaaS application marketplace. |
| 2 | Standard protocol | The third-party applications that are not provided in the application marketplace but support standard protocols such as Security Assertion Markup Language (SAML) and Open ID Connect (OIDC). After you configure the applications in a standardized way, you can use the applications. |
| 3 | Custom applications | The applications that are not provided in the application marketplace and do not support standard protocols, but can be developed and integrated by using the IDaaS standards. |
| 4 | <code>Later</code> <code>versions </code> that provide compatibility with legacy applications | For applications that do not fall within the preceding categories, IDaaS provides auto-population of passwords and stores passwords securely to implement SSO. |

If you want to connect an application to IDaaS for unified access and centralized account management, choose the application type based on the following flow chart.

![](assets/1c5bddce4730d3f42568e06da28be5dd.jpeg)

<a id="section-4-1-2"></a>

### 4.1.2. Application marketplace

**Application marketplace**

![](assets/86ae9c911f06aeb02e0fe770d1367a15.jpeg)

Identity as a Service (IDaaS) provides pre-integrated templates for common applications. You can search for and activate the templates that you require in the application marketplace and configure single sign-on (SSO) and synchronization.

> **Note**
>
> You cannot directly activate or purchase applications from the IDaaS application marketplace. The marketplace allows you only to connect identity systems of applications to IDaaS You must build or purchase the applications that you want to use from other channels.

If you want to add an application, check whether the application is pre-integrated in the marketplace first. Pre-integrated templates help you save a considerable amount of time in configuration.

In the left-side navigation page of the IDaaS console, click **Application**. On the Application page, click **Add Application** to go to the **Marketplace** tab. Then, search for the application that you want to add.

![](assets/e589d7b1793d2fb96985a8e6c4fe5a8e.jpeg)

<a id="section-4-1-3"></a>

### 4.1.3. 2. Standard protocols

Enterprise identity management systems use internationally accepted common identity management protocols. Mature enterprise software uses international standard protocols to make it easy for customers to integrate the software with their IdPs. In our case, IdP is Identity as a Service (IDaaS).

IDaaS allows you to configure single sign-on (SSO) for applications that support standard protocols.

image.png

**Benefits of using standard protocols**

Enterprise applications that use standard protocols have the following benefits:

- Higher maturity. Support for standard identity protocols demonstrates the maturity of an enterprise application.

- Wider applicability. Standard protocols enable the interoperability between account systems of an enterprise. An enterprise application that supports a set of standard protocols allows customers to choose the identity providers that are best suited to their needs.

- Higher security. Custom protocols involve security risks. International standard protocols undergo a strict process before they are released. Therefore, the protocols support a complete range of scenarios and ensure security.

> **Note**
>
> It takes a short time to integrate with standard protocols. If you are an enterprise application vendor and want to integrate your software with standard protocols, you can contact us. We will add your enterprise application to the IDaaS application marketplace to make it available for intended consumers.

**Standard protocols supported by IDaaS**

| Standard protocol | Description |
| --- | --- |
| OIDC | Released in 2014, OpenID Connect (OIDC) is an open authentication protocol that is built on top of the OAuth 2.0 authorization protocol. The OIDC protocol adds a layer of user authentication by issuing <code> id_token </code> in the JSON Web Token (JWT) format, and is applicable to both authentication and authorization scenarios. It provides the best configuration and integration experience among modern identity management systems. |
| SAML 2.0 | Released in 2005, Security Assertion Markup Language V2.0 (SAML 2.0) is still the most widely used SSO protocol in the world. Most mature enterprise applications support the SAML protocol. SAML 2.0 is an XML-based protocol and has poor adaptability in some edge scenarios for historical reasons. |
| OAuth 2.0 | Released in 2012, OAuth 2.0 (RFC 6749) is the most commonly used authorization protocol. The implementation of the OAuth 2.0 protocol is divided between Authorization Server (AS) and Resource Server (RS). As a lightweight and flexible protocol, OAuth 2.0 is used for scenarios such as login by using WeChat and login by scanning a QR code with DingTalk.<br>The capabilities of the OIDC protocol include the OAuth protocol. In IDaaS, you can use the OIDC protocol to replace the OAuth protocol. |

You can search for  `application_name`  SSO in the search engine or application documentation to check whether the application that you want to connect to IDaaS supports SSO standard protocols.

<a id="section-4-1-4"></a>

### 4.1.4. 3. Custom applications

An enterprise typically has a series of custom applications to support their business processes. Administrators can add custom applications to Identity as a Service (IDaaS) and connect the applications to IDaaS by performing the steps described in the IDaaS documentation.

image.png

**Integration levels of custom applications**

IDaaS allows you to integrate the identity system of a custom application of your enterprise with IDaaS at three levels. We recommend that you verify the integration requirements from top to bottom.

| Integration level | Description | Benefits |
| --- | --- | --- |
| Level 1: unified sign-in | Implement single sign-on (SSO). Integrate the Open ID Connect (OIDC) protocol to configure application accounts and grant access to the application. Allow enterprise accounts in IDaaS to log in to the application by using SSO. .<br>Development documentation: Configure SSO for custom applications. | An employee navigates through all applications by using one set of login credentials.<br>Unified authorization, management, and behavior audit. |
| Level 2: unified accounts | Implement account synchronization. Interface with the IDaaS synchronization API to eliminate identity silos. .<br>Development documentation: Configure account synchronization for custom applications. | All modifications to the account data are synchronized to IDaaS.This makes account management easy and improves productivity. |
| Level 3: unified permissions (not supported) | Implement permission hosting. Use the standard, flexible Role-Based Access Control (RBAC) model of IDaaS to host roles, menus, and features in applications in IDaaS for centralized permission management. | Realize fine-grained access control and standardize access permissions within the enterprise.<br>Reduce the cost for developing complex and costly permission systems for custom applications. |

<a id="section-4-2"></a>

## 4.2. Manage Applications

<a id="section-4-2-1"></a>

### 4.2.1. General configurations

Each application has some general configurations and feature-specific configurations. You can manage general configurations of applications on the General tab.

To access the **General** tab, click **Applications** in the menu, find the application that you want to manage, and then click **Manage**.

In the current version of Identity as a Service (IDaaS), administrators can enable or disable API operations and rotate secrets.

![](assets/b135e6968257488274f75de85d1d9da9.jpeg)

**API operations**

IDaaS provides a variety of API operations for each application. You can enable some API operations for an application so that the application can call these API operations to implement certain features. The following API operations are provided:

- API operations for single sign-on (SSO) based on OpenID Connect (OIDC)

- API operations for account synchronization

- API operations for permission management ( `coming soon` )

An application must exchange its  `client_id`  and  `client_secret`  configured on the General tab for an  `access_token`  to call these API operations.

> **Note**
>
> The  `client_id`  starts with "app_" and is about 26 characters in length. By default, the client_id is the same as the application ID. A  `client_secret`  is a random string that starts with  `CS`  and is between 44 and 46 characters in length.

In the current version of IDaaS, administrators can enable or disable API operations and rotate secrets.

**Secret rotation**

You can customize the interval of secret rotation for each application.

To make secret rotation easier, IDaaS allows you to configure at most two  `client_secrets` for an application and enable at least one client_secret.

During the rotation period, you can keep both of the  `client_secrets`  enabled. After you confirm that the old  `client_secret`  is no longer needed, you can delete the old client_secret.

![](assets/fc3734a6570de2fdf4c58d1325e3b245.png)

To ensure security, we recommend that you rotate secrets every three months or according to specific compliance requirements. The following steps show you how to rotate secrets:

1. Create a new  `client_secret` .

2. Replace the old  `client_secret`  with the new one.

3. Disable the old  `client_secret` . When you disable a client_secret, you will be prompted the last time when this  `client_secret`  was used. After you confirm that the client_secret is no longer used, you can disable it.

4. Verify whether the running of the application is affected.

5. After you confirm that the running of the application is not affected, you can delete the old  `client_secret` .

**Basic Information**

| Parameter | Description |
| --- | --- |
| ID | The ID of the application. The application ID is for reference only and cannot be changed. |
| Source | The template used to create the application. The source cannot be changed.<br>Valid values: Template Application, Standard Protocol, and Custom Applications. |
| Name | The display name of the application. |
| Application Icon | The icon of the application. The icon file must be in the PNG or JPG format and cannot exceed 1 MB in size. We recommend that you set the pixel aspect ratio to 256\*256. |

<a id="section-4-2-2"></a>

### 4.2.2. Configure SSO

This topic describes how to configure single sign-on (SSO) in Identity as a Service (IDaaS).

You must configure SSO before you can implement SSO.

This topic describes the following SSO configuration items that are common to all applications:

- SSO status

- Application account

- Authorized scope

For more information about the configuration steps, see the documentation for different application templates.

| Application template type | Protocol | References |
| --- | --- | --- |
| Pre-integrated templates in the application marketplace | SAML 2.0 | Create Application |
| Standard protocol - Security Assertion Markup Language (SAML) | SAML 2.0 | SAML 2.0 SSO |
| Standard protocol - Open ID Connect (OIDC) | OIDC | OIDC SSO |
| Custom applications | OIDC | Configure SSO for a custom application |

**SSO status**

image.png

After you create an application, all features of the application are disabled. To facilitate configuration, the SSO status is automatically changed to **Enabled**. You must click Save to allow the change to take effect.

Applications for which the SSO feature is disabled are not displayed in the user portal.

**Application account**

An application account is the unique identifier of a user in the application. When a user sends an SSO request to an application, IDaaS passes the application account to the application. Then, the application places the account in the logged-on state to implement SSO.

If accounts exist in the application, check whether the accounts are mapped to the accounts in IDaaS. If the accounts are not mapped to the accounts in IDaaS, perform batch synchronization for users or create accounts in the application in advance.

For SAML-based applications, you can configure application account rules in the applications. For more information, see Configure accounts for an SAML-based application.

image

For OIDC-based applications or custom applications, IDaaS passes relevant values in  `id_token` . For more information, see Rules for the values of the extended OIDC id_token fields.

**Authorized scope**

image.png

You can select one of the following options to specify the users who can access the application.

| Option | Description |
| --- | --- |
| All Users | All accounts in IDaaS can access the application without additional authorization. |
| Manually | You must specify the organizations and accounts that can access the application on the Authorize tab of the application. |

<a id="section-4-2-3"></a>

### 4.2.3. SAML 2.0 SSO

<a id="section-4-2-3-1"></a>

#### 4.2.3.1. Configuration of SAML 2.0-based SSO

The single sign-on (SSO) process requires interaction between Identity as a Service (IDaaS) and applications. You must configure SSO settings at both ends.

In this topic, the Security Assertion Markup Language 2.0 (SAML 2.0) protocol is used as an example to describe how to configure SSO.

> **Note**
>
> For more information about the SSO protocols supported by IDaaS, see 2. Standard protocols.

**Configuration in IDaaS**

**Upload an application configuration file**

Some applications allow you to download configuration information metadata on the SSO configuration page of the applications. In this case, you can directly upload the downloaded data to IDaaS. Some applications provide a public API that allows IDaaS to pull the configuration information metadata.

image.png

IDaaS obtains all information that is required to configure SSO and pre-populates the related form. You need to only confirm and save the pre-populated information.

**IDaaS parameters**

**Parameter**

**Description**

**Example**

https://signin.example.

The URL that directs

com/1021\*\*\*\*\*4813/sa

IDaaS where to send

ml/SSO

ACS URL

its SAML responses after IDaaS authenticates a user.

The globally unique identifier of the application in IDaaS. In most cases, the identifier is a URI that can be obtained from the application. If the

https://signin.example.

application has no

SP Entity ID

com/1021\*\*\*\*\*4813/sa

special requirements,

ml/SSO

you can set the value to the Assertion

Basic settings

Consumer Service

(required)

(ACS) URL.

The NameID parameter defined in the SAML protocol. For

App User

IDaaS User Username

more information, see Configure SAML application users.

For more information,

Authorize

All Users

see Configure SSO.

The address to which the application automatically redirects after a successful identity provider-initiated (IdP-initiated) SSO. In a SAML

Level-2 menu page in

response, the address

Default RelayState

the application

is passed to the

```text
 RelayState 
```

parameter. After the application reads the address, you are redirected to the address.

The format of the  `NameID`  parameter defined in a SAML response. The NameIDFormat

NameIDFormat

1.1 Unspecified

parameter is not specified for many applications. You do not need to modify this parameter.

The request

![](assets/54e18b41205a64a4e3076af228b0af0a.png)

`Redirect-POST`  is

Binding

```text
 Redirect-POST 
```

supported. You do not need to modify this parameter.

IDaaS signs all SAML

Sign Assertion

requests. You cannot

-

modify this parameter.

The asymmetric

Advanced settings

algorithm used to sign

(optional)

SAML requests. Only

Signing Algorithm

RSA-SHA256 is

RSA-SHA256

supported. You do not need to modify this parameter.

A SAML response can contain additional information about a user, such as the email and name attributes. For more information, see Rules for configuring SAML

Attribute Statements

-

Attribute Statements.

Specifies whether SSO can be initiated only

SSO Implemented By

from the application or

Application Only

from the portal and the application.

If the SSO Implemented By parameter is set to IDaaS & Application, you can specify this parameter. When you

IDaaS Sign-In URL

access the application

-

from the portal, you are redirected to this URL, and a SAML login request is automatically sent to IDaaS.

**Configuration in applications**

**Upload an IDaaS configuration file**

To facilitate application configuration, IDaaS allows you to download the configuration metadata with a few clicks.

image.png

When you configure SSO in some applications, you can directly upload the metadata. You can upload the configuration file that you downloaded in IDaaS or enter the metadata address in your application. You do not need to manually configure parameters.

**Application parameters**

You must specify IDaaS information in your application for integration.

IDaaS displays the information that may be required by the application on the SSO configuration page. This facilitates configuration. The following table describes the parameters.

| Parameter | Description | Example |
| --- | --- | --- |
| IDP Entity ID | The identifier of IDaaS in the application. You may need to enter the identifier on the SSO configuration page of the application. | https://xxxxx.aliyunidaas.com |
| IdP Sign-in URL | The SAML protocol supports service provider-initiated (SP-initiated) SSO. You may need to enter the URL on the SSO configuration page of the application. | https://xxxxx.aliyunidaas.com.c n/saml/idp/saml1 |
| <code>(Not supported)</code><br>SLO URL | The SAML protocol supports single logout (SLO). If you want to use this feature, you must enter the URL on the SSO configuration page of the application. | - |
| Certificate | The electronic signature in the SSO result sent by IDaaS. The application can use the required public key to verify the signature and check whether the result is sent by IDaaS. This helps ensure security. | -----BEGIN CERTIFICATE-----<br>MIIDEjCCAfqgAwIBAgIHAYnNmX 60izANBgkqhkiG9w0BAQsFADA pMRowGAYDVQQD..... |

<a id="section-4-2-3-2"></a>

#### 4.2.3.2. Configure accounts for an SAML-based application

When Security Assertion Markup Language (SAML) is used for single sign-on (SSO), the identity credentials of a user are passed to the  `NameID`  field of SAMLResponse or exist in other fields.

When you configure an application account, you need to specify the type of value to be used as the identity credentials of the account.

The most common choice is IDaaS Account Name or IDaaS Email.

**SSO configurations**

image.png

You can choose from the following four options.

| Option | Description |
| --- | --- |
| IDaaS Account | When a user initiates a single sign-on request to the current application, the IDaaS account information is used as the identity credentials of the application. If you select this option, make sure that the account for SSO has the same username in IDaaS and in the application. Otherwise, login may fail or an account mismatch may occur.<br>This is the most common configuration. This eliminates the need to configure a separate application account for each IDaaS account, saving time and effort.<br>Two sub-options are provided:<br>• IDaaS account name (Username)<br>• IDaaS email address (Email) |
| Application Username | An administrator must specify the application account that is used by each IDaaS account during the SSO to the current application. If this parameter is not specified, SSO cannot be performed.<br>For example, if the test_user account exists in IDaaS and you want to log in to the application as an administrator, you can configure the application account. For more information about how to configure application accounts, see the Add an application account section of this topic.<br>If the application has a small number of users, you can use this configuration to maximize flexibility.<br>One sub-option is provided: |
| Primary Application User | This option combines the advantages of the first two options. It allows administrators to configure application accounts and use the accounts in preference. For more information about how to configure application accounts, see the Add an application account section of this topic. By default, if no application account is configured, the IDaaS identity credentials are used.<br>Two sub-options are provided:<br>• Secondary IDaaS account name (Username)<br>• Secondary IDaaS email address (Email) |
| Expression | If the application account has specific rules, you can configure expressions.<br>For example, the application uses the email prefix of each account as the account name.<br>No sub-option is provided. Because expressions are complicated, contact the IDaaS team for configuration.<br>You can enter an expression rule. |

**Add an application account**

If you select **Application Account** or **Primary Application Account** from the Application Account drop-down list on the SSO tab, you can configure the identities used by different accounts when the accounts access the application.

Click the **Application Account > Add Application Account**. A dialog box appears.

image

Search for the IDaaS account you want to manage by entering a keyword such as admin, root, mobile number, or Jerry. After you find the IDaaS account, click the account and add an application account for the account. Click Save to complete the configuration.

> **Note**
>
> You can configure multiple application accounts for an IDaaS account. When a user initiates an SSO request, the user can select one of the configured application accounts to log in to the application.

<a id="section-4-2-3-3"></a>

#### 4.2.3.3. Rules for configuring SAML Attribute Statements

This topic describes the rules for configuring Security Assertion Markup Language (SAML) Attribute Statements and provides configuration examples.

**Rules for configuring SAML Attribute Statements**

Type

Value

Description

user.username

The username.

user.displayName

The display name.

The mobile phone number

user.phone (phased out)

that does not include the country code (phased out).

The mobile phone number

user.phoneNumber

that does not include the country code.

user.email

The email address.

The status of the user. Valid values:

user.status

- enabled

- disabled

The ID of the primary

user.primaryOrganizationalUnitId

organization to which the user belongs.

The information about the organization to which the user belongs.

ObjectToJsonString(user.organizationalUnits)

The value is a JSON array string.

Variable

The IDs of the organizations to which the user belongs.

ArrayJoin(ArrayMap(user.organizationalUnits,

The value is a JSON array

__item.organizationalUnitId), ",")

string.

The information about the group to which the account belongs.

ObjectToJsonString(user.groups)

The value is a JSON array string.

The IDs of the groups to which the account belongs.

ArrayJoin(ArrayMap(user.groups, __item.groupId), ",")

The value is a JSON array string.

The external IDs of the groups to which the account belongs.

ArrayJoin(ArrayMap(user.groups, __item.groupExternalId), ",")

The value is a JSON array string.

The information about all extended fields.

ObjectToJsonString(user.customFields)

The value is a JSON array string.

The value of an extended

user.customFieldMap.$fieldname$.fieldValue

field.

appUser.username

The application account.

Constant

Enclose constants in double quotation marks ("").

An advanced feature. You can flexibly concatenate and change values by using expressions.

Expression

For more information, see Advanced expressions for account fields.

**Examples of SAML expressions**

**Example: the user object.**

```text
{
  ...
  "customFieldMap": {
        "place": {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        "age": {
            "fieldName": "age",
            "fieldValue": "18"
        }
    },
    "identityProviderUserMap": {
        "idp_m2gngriuenktdkxxxxxx": {
            "identityProviderId": "idp_m2gngriuenktdkxxxxxx",
            "identityProviderType": "ding_talk",
            "identityProviderExternalId": "corp_1234xxxxxxx",
            "identityProviderUserId": "b2ed5fc0xxxxx"
        }
    },
    "organizationalUnits": [
        {
            "organizationalUnitId": "ou_sdfadtaaxxxxxx",
            "organizationalUnitName": "AD",
            "primary": false
        },
        {
            "organizationalUnitId": "ou_werttxxxxxx",
            "organizationalUnitName": "name_002",
            "primary": true
        }
    ],
    "primaryOrganizationalUnitId": "ou_werttxxxxxx",
    "customFields": [
        {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        {
            "fieldName": "age",
            "fieldValue": "18"
        }
    ],
    "groups": [
        {
            "groupId": "group_jp6al4sn4n4wjgjxxxxxx",
            "groupName": "group1",
            "groupExternalId": "group_jp6al4sn4n4wjgjxxxxxx"
        },
        {
            "groupId": "group_vavikcxewkf5h3oxxxxxx",
            "groupName": "group2",
            "groupExternalId": "group_vavikcxewkf5h3oxxxxxx"
        }
    ],
  ...
}
```

**SAML configuration example**

![](assets/789fa5fd834785f376ae41976f4d5594.png)

**Sample parsing result of SAML Attribute Statements**

1. The following SAML response is returned after the organizationalUnits field in Attribute Statements is parsed by using the ObjectToJsonString(user.organizationalUnits) expression:

   ```xml
   <saml2:Attribute Name="organizationalUnits" 
   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       
   [{"organizationalUnitId":"ou_sdfadtaaxxxxxx","organizationalUnitName":"AD","primary":fa
   e},
   {"organizationalUnitId":"ou_werttxxxxxx","organizationalUnitName":"name_002","primary":
   ue}]
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

2. The following SAML response is returned after the organizationalUnitIds field in Attribute Statements is parsed by using the ArrayJoin(ArrayMap(user.organizationalUnits, __item.organizationalUnitId), ",") expression:

   ```xml
   <saml2:Attribute Name="organizationalUnitIds" 
   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       ou_sdfadtaaxxxxxx,ou_werttxxxxxx
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

3. The following SAML response is returned after the groups field in Attribute Statements is parsed by using the ObjectToJsonString(user.groups) expression:

   ```xml
   <saml2:Attribute Name="groups" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       
   [{"groupId":"group_jp6al4sn4n4wjgjxxxxxx","groupName":"group1","groupExternalId":"group
   p6al4sn4n4wjgjxxxxxx"},
   {"groupId":"group_vavikcxewkf5h3oxxxxxx","groupName":"group2","groupExternalId":"group_
   vikcxewkf5h3oxxxxxx"}]
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

4. The following SAML response is returned after the groupIds field in Attribute Statements is parsed by using the ArrayJoin(ArrayMap(user.groups, __item.groupId), ",") expression:

   ```xml
   <saml2:Attribute Name="groupIds" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       group_jp6al4sn4n4wjgjxxxxxx,group_vavikcxewkf5h3oxxxxxx
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

5. The groupExternalIds field in id_token is parsed by using the ArrayMap(user.groups, __item.groupExternalId) expression:

   ```xml
   <saml2:Attribute Name="groupExternalIds" 
   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       group_jp6al4sn4n4wjgjxxxxxx,group_vavikcxewkf5h3oxxxxxx
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

6. The following SAML response is returned after the groupId field in Attribute Statements is parsed by using the SamlArray(ArrayMap(user.groups, __item.groupId)) expression:

   ```xml
   <saml2:Attribute Name="grouIdArray" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-
   instance"xsi:type="xsd:string">
       group_jp6al4sn4n4wjgjxxxxxx
     </saml2:AttributeValue>
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       group_vavikcxewkf5h3oxxxxxx
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

7. The following SAML response is returned after the customFields field in Attribute Statements is parsed by using the ObjectToJsonString(user.customFields) expression:

   ```xml
   <saml2:Attribute Name="customFields" 
   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-
   instance"xsi:type="xsd:string">
       [{"fieldName":"place","fieldValue":"beijing"},
   {"fieldName":"age","fieldValue":"18"}]
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

8. The following SAML response is returned after the age field in Attribute Statements is parsed by using the user.customFieldMap.age.fieldValue expression:

   ```xml
   <saml2:Attribute Name="age" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
     <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xsd:string">
       18
     </saml2:AttributeValue>
   </saml2:Attribute>
   ```

<a id="section-4-2-3-4"></a>

#### 4.2.3.4. Multi-relay state access

This topic describes the scenarios of the multi-relay state access feature and how to use the feature.

**Scenarios**

You can use the multi-relay state access feature to configure multiple relay states for a Security Assertion Markup Language (SAML) application. After successful single sign-on (SSO), you are redirected to different pages. In this topic, Alibaba Cloud RAM user-based SSO is used.

- After you initiate SSO from Identity as a Service (IDaaS), you are redirected to the homepage of the Alibaba Cloud Management Console.

- If users such as data analysts and project managers want to use Quick BI, they are redirected to the Quick BI console after they initiate SSO from IDaaS.

- If users such as R&D engineers want to use Alibaba Cloud DevOps, they are redirected to the Alibaba Cloud DevOps console after they initiate SSO from IDaaS.

> **Note**
>
> The multi-relay state access feature is available only for SAML applications that support standard protocols. If you use a template application such as User-based SSO for Alibaba Cloud in the marketplace, you must convert the template application into a standard application to use the feature.
>
> After you convert the template application into a standard application, you may need to configure additional parameters. This does not affect the SSO capability.

**Procedure**

Configure the **Default RelayState** and **Relay State** parameters in the Show Advanced Settings section for SAML applications that support standard protocols.

- Default RelayState: The URL of the page that is displayed after you click an application card in the IDaaS application portal and complete the SSO configuration. This parameter is optional. If you do not configure this parameter, the URL is determined by the application.

- Relay State: The multiple relay states that are displayed in the application card of the IDaaS application portal. After you click a card and complete the SSO configuration, you are redirected to the corresponding URL. You can configure this parameter only after you configure the Default Redirection URL parameter.

> **Note**
>
> After you configure the Default Redirection URL and Relay State parameters, the configurations take effect after you click Save. You do not need to update the identity provider (IdP) metadata on the application side.

**Example**

After you log in to the IDaaS application portal, the application card displays multiple relay states for applications for which the **Relay State** parameter is configured. You can directly click the application card to access the default redirection URL. You can also click the button in the lower part of the page to access the URLs of cloud services such as Quick BI and Alibaba Cloud DevOps.

<a id="section-4-2-4"></a>

### 4.2.4. OIDC SSO

<a id="section-4-2-4-1"></a>

#### 4.2.4.1. Configure SSO for an OIDC-based application

This topic describes how to configure single sign-on (SSO) based on OpenID Connect (OIDC).

> **Note**
>
> For more information about the SSO protocols supported by Identity as a Service (IDaaS), see 2. Standard protocols.

**OIDC grant types supported by IDaaS**

The following table describes the OIDC grant types supported by IDaaS. You can select more than one grant type.

| Grant type | Description |
| --- | --- |
| Client Credentials<br>client_credentials | The OIDC Client Credentials grant type permits an application to exchange its <code> client_id </code> and <code> client_secret </code> in IDaaS for an access token from the server to call the Developer APIs provided by IDaaS for the application.<br>You do not need to select the Client Credentials mode. If the application API is enabled, this mode is enabled. |
| Authorization Code<br>authorization_code | Authorization Code is the most widely used login mode for OIDC applications in IDaaS. An application delegates login to IDaaS and parses the <code> id_token </code> value returned by IDaaS to complete login verification. |
| Refresh Tokens<br>refresh_token | A refresh token is used to refresh the access token to extend the validity<br>![](assets/bc0bc385ecebde0a73879e62da706f23.png)<br>period of a session.<code>    </code> Refresh Tokens are usually used together with the Authorization Code grant type. |
| Device Flow<br>device | Device Flow is often used to connect non-web applications to IDaaS to implement SSO. Device Flow allows users to log in to the applications in a browser when a device is unable to display the IDaaS login page. |

For common enterprise web applications, we recommend that you select both the Authorization Code and Refresh Tokens grant types.

For non-web applications, we recommend that you select both the Device Flow and Refresh Tokens grant types.

> **Note**
>
> Other OIDC grant types are not supported by IDaaS.

**Configuration in IDaaS**

**Parameter**

**Description**

**Example**

Authorization

The grant type that you want to select

Code

Grant Types

for an application. You can select more

Refresh Tokens

than one grant type.

The whitelist of redirect URIs. This

Basic settings

http://www.xxxx/

parameter defines where users land

(required)

oidc/sso

after successful login or registration.

Redirect URIs

http://www.xxxx/

Each redirect URI must be

oidc/sso2

whitelisted.

For more information, see SSO

Authorize

All Users

overview.

The identity information of a logged-in user that can be obtained by using the user information endpoint. You can select more than one type of

openid

information.

scopes

email

- openid

scopes

profile

- email

- phone

- profile

This parameter is available if you select Authorization Code in Grant

By default, this

Types. If this parameter is enabled, the

PKCE

option is not

Authorization Code grant type uses a

selected.

more secure Proof Key for Code Exchange (PKCE) extension process.

This parameter is available only if

Code Challenge

PKCE is enabled. It specifies how a

-

code challenge is generated in the

Method

PKCE extension.

An access token is used to request IDaaS API operations.   By default,

Validity Period

the token is valid for 2 hours. After the

for for

2 hours

access token expires, users must use

access_token

the refresh token to renew the access token or log in again.

An  `ID token`  is used to authenticate a user. The token is in the JSON Web Token (JWT) format. An ID

Validity Period

token allows the application to

10 hours

for for id_token

authenticate a user by using a public key. After the ID token expires, users must use the refresh token to renew

Advanced

the ID token or log in again.

settings (optional)

A refresh token is used to obtain a new

![](assets/ed316c483557d5c906bfe247836e1f5b.png)

Validity Period

access token or a new ID token.

for for

30 days

After a  `refresh token`  expires,

refresh_token

users need to log in again.

You can extend the payload field of  `id_token`  to return non-sensitive user information. For more information, see Rules for the values of the extended OIDC id_token fields.

Extend id_token

-

> **Note**
>
> Note that fields added in payload are available to all users. Add fields as needed.

id_token

The asymmetric algorithm that is used to sign ID tokens. Only RSA-SHA256 is

RSA-SHA256

Signing

supported.

Algorithm

SSO

This parameter specifies whether SSO

Implemented By

is implemented by an application or on

Application Only

the IDaaS login page.

If you set the SSO Implemented By parameter to IDaaS & Application, you can enter an IDaaS login URL. If you want to access an application on the

IDaaS Sign-in

IDaaS login page, enter the URL of the

-

URL

page where SSO can be implemented. If the URL receives login requests, the requests are immediately redirected to the authorization endpoint.

**Configurations in the application**

OIDC allows applications to use a set of standard and open IDaaS API operations to complete login authentication.

The following table describes these API operations.

| Field | Description | Example |
| --- | --- | --- |
| Issuer | The source of the token specified by <code> id_token </code>. It is also the base URL of the following API operations. | https://xxxxx.aliyunidaas.com.cn/oidc1 |
| Discovery Endpoint<br>Discovery | The endpoint that is used to obtain metadata, such as a directory of endpoints, supported grant types, and parameters. The metadata is available to all users. | https://xxxxx.aliyunidaas.com.cn/oidc1/.well-known/openid-configuration |
| Authorization Endpoint<br>Authorization | The endpoint from which the application requests SSO. | https://xxxxx.aliyunidaas.com.cn/oidc/authorize |
| Token Endpoint<br>token | The <code> token </code> endpoint that the application uses to obtain an access token after the application receives an authorization <code> code </code>. | https://xxxxx.aliyunidaas.com.cn/oidc/t oken |
| Public Key Endpoint<br>JWKS | The JSON Web Key Set (JWKS) endpoint that is used to verify the ID token and complete SSO.<code>  </code> The public key cannot be rotated. | https://xxxxx.aliyunidaas.com.cn/oidc1/jwks |
| User Information Endpoint<br>Userinfo | The endpoint that is used to obtain basic user information by using an access token after login.<code>  </code> | https://xxxxx.aliyunidaas.com.cn/oidc1/userinfo |
| Single Logout Endpoint<br>SLO | The endpoint that is used to trigger single logout (SLO). | https://xxxxx.aliyunidaas.com.cn/oidc1/logout |

<a id="section-4-2-4-2"></a>

#### 4.2.4.2. Rules for the values of the extended OIDC id_token fields

This topic describes the rules for the values of the extended OpenID Connect (OIDC) id_token fields and provides configuration examples.

**Rules for the values of the extended id_token fields**

Type

Value

Description

user.username

The username.

user.displayName

The display name.

The mobile phone number that

user.phone (phased out)

does not include the country code (phased out).

The mobile phone number that

user.phoneNumber

does not include the country code.

user.email

The email address.

The status of the user. Valid values:

user.status

- enabled

- disabled

The ID of the primary

user.primaryOrganizationalUnitI

organization to which the user

d

belongs.

Variable

The information about the

user.organizationalUnits

organization to which the user belongs.

The IDs of all organizations to

ArrayMap(user.organizationalU

which the user belongs.

nits, __item.organizationalUnitId)

The value is a JSON array.

The information about the group to which the account

user.groups

belongs.

The value is a JSON array.

The IDs of the groups to which

ArrayMap(user.groups,

the account belongs.

__item.groupId)

The value is a JSON array.

The external IDs of the groups

ArrayMap(user.groups,

to which the account belongs.

__item.groupExternalId)

The value is a JSON array.

The information about all extended fields.

user.customFields

The value is a JSON array.

user.customFieldMap.$fieldnam

The value of an extended field.

e$.fieldValue

Constant

Constants are enclosed in double quotation marks ("").

An advanced feature. You can flexibly concatenate and change values by using expressions.

Expression

For more information, see Advanced expressions for account fields.

Example: the user object.

```text
{
  ...
  "customFieldMap": {
        "place": {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        "age": {
            "fieldName": "age",
            "fieldValue": "18"
        }
    },
    "identityProviderUserMap": {
        "idp_m2gngriuenktdkxxxxxx": {
            "identityProviderId": "idp_m2gngriuenktdkxxxxxx",
            "identityProviderType": "ding_talk",
            "identityProviderExternalId": "corp_1234xxxxxxx",
            "identityProviderUserId": "b2ed5fc0xxxxx"
        }
    },
    "organizationalUnits": [
        {
            "organizationalUnitId": "ou_sdfadtaaxxxxxx",
            "organizationalUnitName": "AD",
            "primary": false
        },
        {
            "organizationalUnitId": "ou_werttxxxxxx",
            "organizationalUnitName": "name_002",
            "primary": true
        }
    ],
    "primaryOrganizationalUnitId": "ou_werttxxxxxx",
    "customFields": [
        {
            "fieldName": "place",
            "fieldValue": "beijing"
        },
        {
            "fieldName": "age",
            "fieldValue": "18"
        }
    ],
    "groups": [
        {
            "groupId": "group_jp6al4sn4n4wjgjxxxxxx",
            "groupName": "group1",
            "groupExternalId": "group_jp6al4sn4n4wjgjxxxxxx"
        },
        {
            "groupId": "group_vavikcxewkf5h3oxxxxxx",
            "groupName": "group2",
            "groupExternalId": "group_vavikcxewkf5h3oxxxxxx"
        }
    ],
  ...
}
```

**Examples of OIDC expressions**

![](assets/2cd35ffdeeee5c73ac1e0a6029dfb7f3.png)

1. The organizationalUnits field in id_token is parsed by using the user.organizationalUnits expression.

   ```json
   [
     {
       "organizationalUnitId": "ou_sdfadtaaxxxxxx",
       "organizationalUnitName": "AD",
       "primary": false
     },
     {
       "organizationalUnitId": "ou_werttxxxxxx",
       "organizationalUnitName": "name_002",
       "primary": true
     }
   ]
   ```

2. The organizationalUnitIds field in id_token is parsed by using the ArrayMap(user.organizationalUnits, __item.organizationalUnitId) expression.

   ```json
   [
     "ou_sdfadtaaxxxxxx",
     "ou_werttxxxxxx"
   ]
   ```

3. The groups field in id_token is parsed by using the user.groups expression.

   ```json
   [
     {
       "groupId": "group_jp6al4sn4n4wjgjxxxxxx",
       "groupName": "group1",
       "groupExternalId": "group_jp6al4sn4n4wjgjxxxxxx"
     },
     {
       "groupId": "group_vavikcxewkf5h3oxxxxxx",
       "groupName": "group2",
       "groupExternalId": "group_vavikcxewkf5h3oxxxxxx"
     }
   ]
   ```

4. The groupIds field in id_token is parsed by using the ArrayMap(user.groups, __item.groupId) expression.

   ```json
   [
       "group_jp6al4sn4n4wjgjxxxxxx",
       "group_vavikcxewkf5h3oxxxxxx"
   ]
   ```

5. The groupExternalIds field in id_token is parsed by using the ArrayMap(user.groups, __item.groupExternalId) expression.

   ```json
   [
       "group_jp6al4sn4n4wjgjxxxxxx",
       "group_vavikcxewkf5h3oxxxxxx"
   ]
   ```

6. The customFields field in id_token is parsed by using the user.customFields expression.

   ```json
   [
       {
         "fieldName": "place",
         "fieldValue": "beijing"
       },
       {
         "fieldName": "age",
         "fieldValue": "18"
       }
   ]
   ```

7. The age field in id_token is parsed by using the user.customFieldMap.age.fieldValue expression.

   ```text
   18
   ```

**Rewrite rules for the extended id_token fields**

**Rules for default fields**

1. The following default fields **are not** rewritable:  `exp` ,  `nbf` ,  `iat` ,  `iss` ,  `jti` ,  `at_hash` ,  `c_hash` ,  `nonce` , and  `sid` .

2. The following fields **are** rewritable:  `sub` .

**Rules for user information fields**

Determine whether the following fields in id_token are rewritable based on the scope.

| Field | Scope | Condition under which the field is not rewritable |
| --- | --- | --- |
| email, email_verified | email | When the scope contains the email field and the value (user.email) is not empty. |
| phone_number, phone_number_verified | phone | When the scope contains the phone field and the value (user.phoneNumber) is not empty. |
| name, preferred_username, updated_at, locale | profile | When the scope contains the profile field. |
| instance_id, application_id | instance | When the scope contains the instance field. |

**Configuration suggestions**

1. Configure the scope of user information properly because it determines the fields that are rewritable.

2. To make specific fields rewritable, make sure that the fields are not contained in the scope or their values are empty.

<a id="section-4-2-4-3"></a>

#### 4.2.4.3. Login by using OIDC Device Flow

Among the authentication flows supported by OpenID Connect (OIDC), Device Flow allows all types of clients to complete the login process by using IDaaS.

Due to display limitations, devices may not have built-in login pages. The OIDC Device Flow separates the login process from devices by allowing users to log in through an external browser.

> **Note**
>
> This topic describes the applicable scenarios and processes of login by using the OIDC Device Flow. For more information about the APIs used in implementing the OIDC Device Flow, see API Reference.

The following figure shows the inter-system process.

![](assets/c6ed91117c631ae54f3d619aa45c313f.jpeg)

**Step 1: Prepare for login**

The preparation phase requires no actions from the user. The device interacts with IDaaS and obtains the  `user_code` ,  `device_code` , and verification_url.

The user_code and verification_url must be presented to the user. The user opens the verification_url in a browser and enters the user_code.

![](assets/ca36c14fe2be5200e0afde14fa6be553.jpeg)

> **Note**
>
> You can add the user password to the login URL in the {{verification_url}}?user_code= {{user_code}} format to provide a hyperlink or generate a QR code. In this way, the user can quickly access this URL without entering the  `user_code` .

After the preceding information is obtained, the device sends a polling request to IDaaS to obtain the login result.

**Step 2: Authorize the user to log in to the device in a browser**

After the verification_url is opened, the user will perform the operations in the following figures in sequence to complete the login.

![](assets/21f32171adc2121a31b909f00c606fa8.jpeg)

After the user is logged in, the user can go back to the device to check the login status. The polling request initiated by the device will return the authentication success message, which contains the  `id_token`  of the user.

You can use the JSON Web Key Set (JWKS) endpoint provided in the IDaaS OIDC application to obtain the public keys of the application, and use the public keys to verify the login status and obtain the user ID.

<a id="section-4-2-4-4"></a>

#### 4.2.4.4. M2M applications (machine-to-machine permission management)

Machine-to-machine (M2M) permission management is an identity management method that enables applications to communicate with one another without user involvement. Permissions are managed by Identity as a Service (IDaaS) and authenticated by gateway services to control access from caller applications to protected resources and prevent unauthorized access.

**Sample scenario**

In digital collaboration scenarios, if you need to expose some business system capabilities to third-party partners, such as outsourced teams, you need to establish an automated authorization mechanism based on machine identity.

The following solutions are available for implementing such an authentication mechanism:

- **Establish a partner access authentication system**: Each partner is assigned an independent machine identity through technical measures such as pre-shared keys and OAuth 2.0 client credentials.

- **Fine-grained permission management policies**: In the access control module of the API gateway, associate access permissions on non-critical business API operations with specific partner identities. For example, you can configure the system to allow only a specific development team to call data visualization-related API operations.

The M2M communication-based authorization mechanism not only ensures efficient interaction between automation systems, but also reduces data security risks by implementing identity authentication and permission isolation mechanisms. M2M authentication is especially suitable for system-to-system communication scenarios such as development collaboration and data dashboard building without user involvement.

**Features**

M2M permission management is an identity management method that enables applications to communicate with one another without user involvement. Permissions are managed by IDaaS and authenticated by gateway services to control access from caller applications to protected resources and prevent unauthorized access.

**Typical scenarios**

- Enterprises repose API services to outsourced teams or external systems. Fine-grained access control is required for authenticating caller identities.

- Enterprises access cloud resources of a cloud service provider, such as a multi-cloud environment, from a non-cloud environment.

**Typical customers**

- Customers who need to expose API services by using API gateways.

- All customers who need to access Apsara Stack resources without using AccessKey pairs, and customers whose assets are purchased from multiple cloud service providers. Such customers can use IDaaS in the on-premises development environment and a multi-cloud environment to access Apsara Stack resources without using AccessKey pairs.

**Key features**

- Credential management: The credentials that caller applications use to request  `access tokens`  are managed in IDaaS.

- Permission management: You can define caller applications and grant permissions to them.

- Pre-integrated gateways: IDaaS integrates with API Gateway to implement centralized application authentication.

**Terms**

| Term | Description |
| --- | --- |
| M2M | M2M applications manage permission for machine-to-machine communication. M2M permission allocation and authentication do not require user involvement and can interact with API Gateway to implement API access control and interact with Resource Access Management (RAM) to allow access without using AccessKey pairs.<br>Note<br>An M2M application can serve as a client or a server. |
| Client | The caller application (client in OAuth), which initiates access to protected resources. |
| Server | The callee application or protected resource (resource server in OAuth), which represents an external resource entity. |
| Audience identifier | The audience identifier defines the intended recipients of an access token.The audience identifier corresponds to the aud claim in JSON Web Token (JWT). This audience identifier cannot be modified. |

**Procedure**

This topic describes how to configure API Gateway. An M2M application can be used as a client or a resource server.

> **Note**
>
> We recommend that you configure an M2M application to serve as only one of these identities.

**API workflow**

1. The caller application verifies the identity and requests an  `access token` .

2. IDaaS returns the  `access token` , including the permission information.

3. The caller application uses the  `access token`  to access the destination application.

4. The callee application, API Gateway, or STS service verifies the validity of the  `token` .

5. The callee application, API Gateway, or STS service performs authentication, and allows or rejects the request.

6. A response is returned.

**Configure an application**

**Add an application**

1. Log in to the IDaaS console, find the IDaaS instance that you want to manage, and click Console in the Actions column.

2. In the left-side navigation pane, choose  `Application > Add Application > M2M Application > Add Application` .

3. In the **Application Name** field, enter a name for the application and click **Add**.

**View general settings**

On the **Application** page, click the application that you want to view, and then click the **General** tab. On this tab, you can view and manage the general settings of the application, including the **basic formation, credential settings, network scopes, and other application settings**.

> **Note**
>
> If you need to control the network scope of the caller application and ensure that calls are made only within a specific network scope, you can modify the **Client Network Zone** parameter. For more information about network scopes, see Network scopes.

**View application configurations**

To view the endpoints and configurations of a caller application, go to the  `Application > General > Application Settings`  For more information, see Call examples of M2M Client Token.

**Manage client permissions**

Choose **Application > Client Permission Management** to view the permissions granted to the application. You can add permissions and grant permissions to the callee application on the **Server Permission Control** tab.

**Manage server permissions**

1. Choose **Application > Server Permission Control** to configure the application as a callee application.

   > **Note**
   >
   > If it is your first time configuring the application as a caller application, you must add an audience identifier that defines the intended recipients of the access token. The audience identifier corresponds to the aud claim in JWT. The aud claim ensures that the token is only accepted by the protected service.
   >
   > **The audience identifier cannot be modified.**

2. After you turn on **Server Permission Control**, you can grant or revoke permissions for the caller application.

   > **Note**
   >
   > <ol type="i">
   >
   > <li>
   >
   > Permissions are recorded in IDaaS only as unique identifiers. You must manually maintain the mappings between permissions and resources, such as APIs and RAM roles.
   >
   > </li>
   >
   > <li>
   >
   > After you grant permissions to a caller application, the permissions are recorded in
   >
   > </li>
   >
   > </ol>
   >
   > the access token issued by IDaaS to the callee application.
   >
   > <ol type="i" start="3">
   >
   > <li>
   >
   > We recommend that you define the permission ID in the following format:
   >
   > </li>
   >
   > </ol>
   >
   > resource:action:limits. Example: user:read:all.
   >
   > <ol type="i" start="4">
   >
   > <li>
   >
   > The permission identifier must be unique on the same application.
   >
   > </li>
   >
   > </ol>

3. You can view or manage the permissions of the called applications, such as granting and revoking permissions, in the **Authorized Applications** section.

<a id="section-4-2-4-4-1"></a>

##### 4.2.4.4.1. Call examples of M2M Client Token

This topic provides examples on how to use an M2M client token in Employee Identity and Access Management (EIAM) of Identity as a Service (IDaaS) to obtain an access token in OAuth 2.0 client mode and call an API operation to implement authentication between systems.

**Call examples**

**Authentication method: client_secret_basic**

**Request method: POST**

**Header parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| Authorization | String | Basic Base64(clientId:clientS ecret)<br>The Base64-encoded client ID and client secret. | YXBwX201ZG9vemVzb m81Mmtxxxxxxxxx |
| Content-Type | String | The content type. Set the value to application/x-www-form-urlencoded. | application/x-www-form-urlencoded |

**Request parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| grant_type | String | The permission type.Set the value to client_credentials. | client_credentials |
| scope | String | The requested scope of permissions. The value is in the resourceServerIdentifi er+"\|"+scope format.<br>For example, if resourceServerIdentifi er is http://www.example.c om and scope is read:file,<br>the returned result is http://www.example.c om\|read:file.<br>You can obtain all authorized scopes by using the resource server identifier parameter. | http://aliyun.com\|read: file |
| client_id | string | The application ID. |  |

**Sample request**

```bash
curl --location --request POST 
'https://XXXX.aliyunidaas.com/api/v2/iauths_system/oauth2/token' 
--header 'Authorization:xxxxxxx
--header 'Content-Type: application/x-www-form-urlencoded' 
--data-urlencode 'grant_type=client_credentials'
--data-urlencode 'scope=http://www.example.com|read:file'
```

**Response parameters**

| Parameter | Type | Nullable | Description |
| --- | --- | --- | --- |
| access_token | String | No | The value of the access token. |
| expires_in | Long | No | The validity period of the token. Unit: seconds. |
| expires_at | Long | No | The time when the token expires. The value is a UNIX timestamp. Unit: seconds. |
| token_type | String | No | The type of the token. |

**Sample response**

```json
{
  "token_type": "Bearer",
  "access_token": 
"AT8csE2sepE4TT9j45xFgRGhEDyS3ovfZDF68Ac4aaQ7c4dBpUahD1cYSCFQbsfpM9ysSArv1pTszcGTZEJK11yG
2GKWd4cf33ZVGsgPfLwYDPX2ZRCUpThTaWoxtXCs9zeZzGwxjc5xtasaQMeuE8PuGeHg9SyMzKxJQVv9ubQhoFXjQ
PUotUms4R2M9SBLpWSCaGDf3oiJ5WCuGyMzJdrrdQeLSB7dU9P1iKbjxGWCmwaMLMkUWZBKsAeYi3xjJmpMsuLq38
KAV5bttwi8z8cafuweuNvwdjfZYCYvNbRAt1nB9Bxn9Q99rdpYawU3eH3UvzkvMYoJ5wtnGSsPJ9B7NHBkxxHUG",

  "expires_in": 3600,
  "expires_at": 1733710213
}
```

**Authentication method: client_secret_post**

**Request method: POST**

**Header parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| Content-Type | String | The content type. Set the value to application/x-www-form-urlencoded. | application/x-www-form-urlencoded |

**Request parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| grant_type | String | The permission type.Set the value to client_credentials. | client_credentials |
| client_id | String | The application ID. |  |
| client_secret | String | The application secret. |  |
| scope | String | The requested scope of permissions. The value is in the resourceServerIdentifi er+"\|"+scope format.<br>For example, if resourceServerIdentifi er is http://www.example.c om and scope is read:file,<br>the returned result is http://www.example.c om\|read:file.<br>You can obtain all authorized scopes by using the resource server identifier parameter. | http://aliyun.com\|read: file |

**Sample request**

```bash
curl --location --request POST 
'https://XXXX.aliyunidaas.com/api/v2/iauths_system/oauth2/token' 
--header 'Content-Type: application/x-www-form-urlencoded' 
--data-urlencode 'grant_type=client_credentials' 
--data-urlencode 'client_id=app_m5doozesno52kbqrqpw3XXXX' 
--data-urlencode 'client_secret=CS5v3F4Cy8hyDmFPJtAuyHDTUdR8i88GcgcXXXXX'
--data-urlencode 'scope=http://www.example.com|read:file'
```

**Sample response**

```json
{
  "token_type": "Bearer",
  "access_token": 
"AT8csE2sepE4TT9j45xFgRGhEDyS3ovfZDF68Ac4aaQ7c4dBpUahD1cYSCFQbsfpM9ysSArv1pTszcGTZEJK11yG
2GKWd4cf33ZVGsgPfLwYDPX2ZRCUpThTaWoxtXCs9zeZzGwxjc5xtasaQMeuE8PuGeHg9SyMzKxJQVv9ubQhoFXjQ
PUotUms4R2M9SBLpWSCaGDf3oiJ5WCuGyMzJdrrdQeLSB7dU9P1iKbjxGWCmwaMLMkUWZBKsAeYi3xjJmpMsuLq38
KAV5bttwi8z8cafuweuNvwdjfZYCYvNbRAt1nB9Bxn9Q99rdpYawU3eH3UvzkvMYoJ5wtnGSsPJ9B7NHBkxxHUG",

  "expires_in": 3600,
  "expires_at": 1733710213
}
```

**Authentication method: client_secret_jwt**

**Request method: POST**

**Header parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| Content-Type | String | The content type. Set the value to application/x-www-form-urlencoded. | application/x-www-form-urlencoded |

**Request parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| grant_type | String | The permission type.Set the value to client_credentials. | client_credentials |
| client_id | String | The application ID. |  |
| client_assertion_type | String | The client assertion type. Set the value to urn:ietf:params:oauth: client-assertion-type:jwt-bearer. |  |
| client_assertion | String | The signature issued by the client by using client_secret. The value is in the JSON Web Token (JWT) format. The signature algorithm is HS256.For more information, see Appendix 2. |  |

<table>
  <tr>
    <td>scope</td>
    <td>String</td>
    <td>The requested scope of permissions. The value is in the resourceServerIdentifi er+"|"+scope format.<br>For example, if resourceServerIdentifi er is http://www.example.c om and scope is read:file,<br>the returned result is http://www.example.c om|read:file.<br>You can obtain all authorized scopes by using the resource server identifier parameter.</td>
    <td>http://aliyun.com|read: file</td>
  </tr>
</table>

**Sample request**

```bash
curl --request POST \
  --url 'https://XXXX.aliyunidaas.com/api/v2/iauths_system/oauth2/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{clientId}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
  --data-urlencode 'client_assertion={{JwtToken}}'
  --data-urlencode 'scope=http://www.example.com|read:file'
```

**Sample response**

```json
{
  "token_type": "Bearer",
  "access_token": 
"AT8csE2sepE4TT9j45xFgRGhEDyS3ovfZDF68Ac4aaQ7c4dBpUahD1cYSCFQbsfpM9ysSArv1pTszcGTZEJK11yG
2GKWd4cf33ZVGsgPfLwYDPX2ZRCUpThTaWoxtXCs9zeZzGwxjc5xtasaQMeuE8PuGeHg9SyMzKxJQVv9ubQhoFXjQ
PUotUms4R2M9SBLpWSCaGDf3oiJ5WCuGyMzJdrrdQeLSB7dU9P1iKbjxGWCmwaMLMkUWZBKsAeYi3xjJmpMsuLq38
KAV5bttwi8z8cafuweuNvwdjfZYCYvNbRAt1nB9Bxn9Q99rdpYawU3eH3UvzkvMYoJ5wtnGSsPJ9B7NHBkxxHUG",

  "expires_in": 3600,
  "expires_at": 1733710213
}
```

**Authentication method: private_key_jwt**

**Request method: POST**

**Header parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| Content-Type | String | The content type. Set the value to application/x-www-form-urlencoded. | application/x-www-form-urlencoded |

**Request parameters**

| Parameter | Type | Description | Example |
| --- | --- | --- | --- |
| grant_type | String | The permission type. Set the value to client_credentials. | client_credentials |
| client_id | String | The application ID. |  |
| client_assertion_type | String | The client assertion type.Set the value to urn:ietf:params:oauth:clie nt-assertion-type:jwt-bearer. |  |
| client_assertion | String | The signature issued by the client by using the private key. The value is in the JWT format. The signature algorithm is RS256. For more information, see Appendix 1. |  |
| scope | String | The requested scope of permissions. The value is in the resourceServerIdentifier+ "\|"+scope format.<br>For example, if resourceServerIdentifier is http://www.example.com and scope is read:file,<br>the returned result is http://www.example.com\| read:file.<br>You can obtain all authorized scopes by using the resource server identifier parameter. | http://aliyun.com\|rea d:file |

**Sample request**

```bash
curl --request POST \
  --url 'https://XXXX.aliyunidaas.com/api/v2/iauths_system/oauth2/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{clientId}}' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
  --data-urlencode 'client_assertion={{JwtToken}}'
  --data-urlencode 'scope=http://www.example.com|read:file'
```

**Sample response**

```json
{
  "token_type": "Bearer",
  "access_token": 
"AT8csE2sepE4TT9j45xFgRGhEDyS3ovfZDF68Ac4aaQ7c4dBpUahD1cYSCFQbsfpM9ysSArv1pTszcGTZEJK11yG
2GKWd4cf33ZVGsgPfLwYDPX2ZRCUpThTaWoxtXCs9zeZzGwxjc5xtasaQMeuE8PuGeHg9SyMzKxJQVv9ubQhoFXjQ
PUotUms4R2M9SBLpWSCaGDf3oiJ5WCuGyMzJdrrdQeLSB7dU9P1iKbjxGWCmwaMLMkUWZBKsAeYi3xjJmpMsuLq38
KAV5bttwi8z8cafuweuNvwdjfZYCYvNbRAt1nB9Bxn9Q99rdpYawU3eH3UvzkvMYoJ5wtnGSsPJ9B7NHBkxxHUG",

  "expires_in": 3600,
  "expires_at": 1733710213
}
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
| --- | --- | --- | --- |
| 400 | invalid_request | Require parameter variable: grant_type | A required parameter is not specified in the request, the specified parameter value is invalid, or a parameter value is in an invalid format. |
| 400 | authentication_req uired | Authentication required, allowed authentication methods: \[client_secret_basic, client_secret_post, client_secret_jwt, private_key_jwt\] | The authentication method is invalid. The following authentication methods are supported:<br>client_secret_basic, client_secret_post, client_secret_jwt,<br>private_key_jwt |
| 400 | invalid_client_crede ntial | Invalid client_assertion, reasons(s): \[expired\] | The client assertion is invalid and the token is expired. |
| 400 | invalid_grant | Invalid or not supported grant_type: authorization_code | The type of the permission is not supported. |
| 400 | invalid_scope | Invalid scope: http://www.example.com\| read:file | The request scope is invalid or unknown. |
| 500 | internal_error | Unexpected internal error | An internal server error occurred. |

**Appendix 1: Use Java to generate a JWT signature based on the RS256 algorithm**

This appendix provides a complete example of using Java to generate a JWT signature based on the RS256 asymmetric encryption algorithm.

1. **Add Maven dependencies**

   ```xml
   <dependency>
       <groupId>io.jsonwebtoken</groupId>
       <artifactId>jjwt-api</artifactId>
       <version>0.11.5</version>
   </dependency>
   <dependency>
       <groupId>io.jsonwebtoken</groupId>
       <artifactId>jjwt-impl</artifactId>
       <version>0.11.5</version>
       <scope>runtime</scope>
   </dependency>
   <dependency>
       <groupId>io.jsonwebtoken</groupId>
       <artifactId>jjwt-jackson</artifactId>
       <version>0.11.5</version>
       <scope>runtime</scope>
   </dependency>
   ```

2. **Sample code in Java**

   ```java
   import io.jsonwebtoken.Jwts;
   import io.jsonwebtoken.SignatureAlgorithm;

   import java.security.Key;
   import java.util.Date;
   import java.util.HashMap;
   import java.util.Map;
   import java.util.UUID;

   /**
    * @author fei.chen
    * @date 2025-02-24 16:17
    */
   public class JwtGenerator {
       private static final String PRIVATE_KEY = "your-private-key"; // Replace the value with your key.

       // Enter the client ID (client_id) of the application.
       private static final String ISSUER = "your_client_id";

       // Enter the client ID (client_id) of the application.
       private static final String SUBJECT = "your_client_id";

       // Enter the token endpoint of the application.
       private static final String AUDIENCE = "your_token_endpoint";

       public static void main(String[] args) throws Exception {
           // The key.
           Key securityKey = RsaKeyConverter.getPrivateKeyFromString(PRIVATE_KEY);

           Map<String, Object> claims = new HashMap<>();
           claim. put("jti", UUID.randomUUID().toString()); // The anti-replay JWT ID.

           // Set a validity time, which cannot exceed 30 minutes.
           long expirationTime = 1000 * 60 * 30;
           Date expirationDate = new Date(System.currentTimeMillis() + expirationTime);

           // Generate a JWT.
           String jwt = Jwts.builder()
                   .setClaims(claims)
                   .setIssuedAt(new Date())
                   .setExpiration(expirationDate)
                   .setSubject(SUBJECT)
                   .setIssuer(ISSUER)
                   .setAudience(AUDIENCE)
                   .signWith(securityKey, SignatureAlgorithm.RS256)
                   .compact();

           System.out.println("Generated JWT token:");
           System.out.println(jwt);
       }
   }
   ```

   ```java
   import java.security.KeyFactory;
   import java.security.PrivateKey;
   import java.security.PublicKey;
   import java.security.spec.PKCS8EncodedKeySpec;
   import java.security.spec.X509EncodedKeySpec;
   import java.util.Base64;

   /**
    * @author fei.chen
    * @date 2025-02-24 16:51
    */
   public class RsaKeyConverter {

       public static PrivateKey getPrivateKeyFromString(String privateKeyStr) throws Exception {
           // Remove the PEM header and footer.
           String privateKeyPEM = privateKeyStr
                   .replace("-----BEGIN PRIVATE KEY-----", "")
                   .replace("-----END PRIVATE KEY-----", "")
                   .replaceAll("\\s +", ""); // Remove all whitespace characters.

           // Perform Base64 decoding.
           byte[] encoded = Base64.getDecoder().decode(privateKeyPEM);

           // Use PKCS8EncodedKeySpec to generate a private key.
           PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(encoded);
           KeyFactory keyFactory = KeyFactory.getInstance("RSA");
           return keyFactory.generatePrivate(keySpec);
       }

       public static PublicKey getPublicKeyFromString(String publicKeyStr) throws Exception {
           // Remove the PEM header and footer.
           String publicKeyPEM = publicKeyStr
                   .replace("-----BEGIN PUBLIC KEY-----", "")
                   .replace("-----END PUBLIC KEY-----", "")
                   .replaceAll("\\s +", ""); // Remove all whitespace characters.

           // Perform Base64 decoding.
           byte[] encoded = Base64.getDecoder().decode(publicKeyPEM);

           // Use OpenSSL to generate an RSA public key.
           X509EncodedKeySpec keySpec = new X509EncodedKeySpec(encoded);
           KeyFactory keyFactory = KeyFactory.getInstance("RSA");
           return keyFactory.generatePublic(keySpec);
       }
   }
   ```

**Appendix 2: Use Java to generate a JWT signature based on the HS256 algorithm**

This appendix provides a complete example of using Java to generate a JWT signature based on the HS256 signature algorithm.

1. **Add Maven dependencies**

   ```xml
   <dependency>
     <groupId>io.jsonwebtoken</groupId>
     <artifactId>jjwt-api</artifactId>
     <version>0.11.5</version>
   </dependency>
   <dependency>
     <groupId>io.jsonwebtoken</groupId>
     <artifactId>jjwt-impl</artifactId>
     <version>0.11.5</version>
     <scope>runtime</scope>
   </dependency>
   <dependency>
     <groupId>io.jsonwebtoken</groupId>
     <artifactId>jjwt-jackson</artifactId>
     <version>0.11.5</version>
     <scope>runtime</scope>
   </dependency>
   ```

2. **Sample code in Java**

   ```java
   public class JwtGenerator {

       private static final String SECRET_KEY = "your_secret_key"; // Replace the value with your key

       // Enter the client ID (client_id) of the application.
       private static final String ISSUER = "your_client_id";

       // Enter the client ID (client_id) of the application.
       private static final String SUBJECT = "your_client_id";

       // Enter the token endpoint of the application.
       private static final String AUDIENCE = "your_token_endpoint";

       public static String generateJwt() throws Exception {
           SecretKey secretKey = Keys.hmacShaKeyFor(SECRET_KEY.getBytes());

           Map<String, Object> claims = new HashMap<>();
           claim. put("jti", UUID.randomUUID().toString()); // The anti-replay JWT ID.

           // Set a validity time, which cannot exceed 30 minutes.
           long expirationTime = 1000 * 60 * 30;
           Date expirationDate = new Date(System.currentTimeMillis() + expirationTime);

           // Generate a JWT.
           String jwt = Jwts.builder()
                   .setClaims(claims)
                   .setIssuedAt(new Date())
                   .setExpiration(expirationDate)
                   .setSubject(SUBJECT)
                   .setIssuer(ISSUER)
                   .setAudience(AUDIENCE)
                   .signWith(secretKey, SignatureAlgorithm.HS256)
                   .compact();
           return jwt;
       }

       public static void main(String[] args) throws Exception{
           // Generate a JWT.
           String jwt = generateJwt();
           System.out.println("Generated JWT: " + jwt);
       }
   }
   ```

<a id="section-4-2-5"></a>

### 4.2.5. Configure SSO for custom applications

IDaaS greatly simplifies configurations and supports single sign-on (SSO) for custom applications.

**Configurations in IDaaS**

To configure SSO, you only need to enter the address for processing SSO requests in the Redirect URIs parameter in the Identity as a Service (IDaaS) console and use the default values for other parameters.

**Parameter**

**Description**

**Example**

The whitelist of redirect URIs. This parameter defines

http://www.xxxx/oidc/s

where users log in with

so

the  `redirect_uri`

Redirect URIs

http://www.xxxx/oidc/s

parameter. IDaaS

Basic Information

so2

redirects user requests

(required)

only after the redirect URI is on the whitelist.

For more information,

Authorize

All Users

see Configure SSO.

The identity information of a logged-in user that can be obtained by using the UserInfo endpoint. You can

openid,

select one or more types of user

scopes

email,

information.

and profile

- openid

- email

- phone

- profile

An access token is used to request IDaaS API operations.  Default value: 20 minutes. Minimum value: 5 minutes.

Validity Period for

Maximum value: 24

20 minutes

access_token

hours. If an access token expires, you must use a refresh token to renew the access token or log in again.

An ID token is used to authenticate a user. The token is in the JSON Web Token (JWT) format. An ID token allows the application to authenticate a user by using a public key.   After the ID

Validity Period for

10 hours

token expires, users

id_token

must use the refresh token to renew the ID token or log in again.

For more information about the format of an ID token, see Tokens

![](assets/30be047755d9086dc30b5407ed02209a.png)

in IDaaS.

A refresh token is used to obtain a new access

**Advanced Settings**

token or a new ID

**(optional)**

![](assets/fa52b83efd4eae45aa8fcdb4317a2dde.png)

token.     After a

Validity Period for

30 days

refresh token expires,

refresh_token

users need to log in again.

You can extend the payload field of  `id_token`  to return non-sensitive user information, without

-

Extend id_token

repeatedly calling the UserInfo endpoint. Note that fields added in payload are available to all users. Add fields as needed.

OIDC allows applications to implement SSO.

SSO Implemented By

IDaaS & Application

If you select IDaaS & Application, you must specify the IDaaS Sign-In URL parameter.

The URL of the page where SSO can be implemented. If the URL receives login

http://www.xxxx/oidc/l

IDaaS Sign-in URL

requests, the requests

ogin

are immediately redirected to the authorization endpoint.

The asymmetric algorithm that is used to sign ID tokens. Only

Signing Algorithm

SHA256

RSA-SHA256 is supported.

The whitelist of redirect URIs for applications when users log out of IDaaS.

Logout Redirect URIs

An application can

http://www.xxxx.com

initiate a single logout (SLO) request that contains this parameter.

**Configurations in the application**

OIDC allows applications to use a set of standard and open IDaaS API operations to complete login authentication.

The following table describes these API operations.

| Field | Description | Example |
| --- | --- | --- |
| Issuer | The source of the token specified by <code> id_token </code>. It is also the base URL of the following API operations. | https://xxxxx.aliyunidaas.com/o idc1 |
| Discovery endpoint<br>Discovery | The endpoint that is used to obtain metadata, such as a directory of endpoints, supported grant types, and parameters. The metadata is available to all users. | https://xxxxx.aliyunidaas.com/o idc1/.well-known/openid-configuration |
| Authorization endpoint<br>Authorization | The endpoint from which the application requests SSO. | https://xxxxx.aliyunidaas.com/o idc/authorize |
| Token endpoint<br>token | The <code> Token </code> endpoint that the application uses to obtain an access token after the application receives an authorization <code> code </code>. | https://xxxxx.aliyunidaas.com/o auth2/token |
| Revocation endpoint<br>Revocation | The endpoint that is used to revoke an issued token. | https://xxxxx.aliyunidaas.com/o auth2/revoke |
| JWKS endpoint<br>JWKS | The JSON Web Key Set (JWKS) endpoint that is used to verify the ID token and complete SSO.<code>  </code> The public key may be rotated. | https://xxxxx.aliyunidaas.com/o idc1/slo |
| UserInfo endpoint<br>Userinfo | The endpoint that is used to obtain basic user information by using an access token after login.<code>  </code> | https://xxxxx.aliyunidaas.com/o idc1/userinfo |
| SLO endpoint<br>SLO | The endpoint that is used to trigger SLO. | - |

For more information, see **Developer Guide > Configure SSO for custom applications**.

<a id="section-4-2-6"></a>

### 4.2.6. Advanced: SLO

Single logout (SLO) refers to the global logout initiated by an application. When you logged on to an application by implementing single sign-on (SSO) from Identity as a Service (IDaaS) and then want to log out, you can initiate a global logout on the application to terminate the application sessions as well as the primary IDaaS logon session. IDaaS implements SLO based on the OpenID Connect (OIDC) protocol. Currently, you can log out of only self-developed applications and OIDC applications by using SLO.

> **Note**
>
> SLO is a session management system for federated authentication. If your application requires your authentication for each logon regardless of whether a primary session exists, you can configure the  `prompt`  parameter in the authorization endpoint to prompt you to complete authentication upon each logon.

**Call the SLO endpoint**

When you request a logout, you need to initiate a redirect request to the **end session endpoint** provided by IDaaS after the application session is closed.

The administrator can obtain the end session endpoint by performing the following steps: Click the name of the application to go to the **application details** page, click the **Sign-In** tab and then the **SSO** subtab, and then find the end session endpoint in the **Application Settings** section in the lower part of the page.

![](assets/33e4fae948e2eecbfd811fdebd18f34c.jpeg)

Redirecting to this endpoint can trigger SLO. In this case, IDaaS is unable to determine whether the SLO request is valid and therefore requires you to confirm the logoff action.

> **Note**
>
> This manual logout process can be skipped. See the instructions below.

If a logged-on IDaaS session exists, IDaaS prompts you about the logout action and asks you to confirm logout, as shown in the following figure.

![](assets/77f9ae7a18d591909a650627a2c4561e.png)

If you confirm logout in the previous step, or no logged-on IDaaS session exists, the **Logged out** message appears, as shown in the following figure.

![](assets/77f9ae7a18d591909a650627a2c4561e.png)

**Automatic redirection upon logout**

If you want to be redirected to the application page instead of being prompted the "Logged out" message after SLO is complete, you can configure the **Logout Redirect URIs** field ( `post_logout_redirect_uris` ).

The administrator can click **Applications**, find this application in the application list, and then click **Manage** in the Actions column corresponding to the application. On the page that appears, click the **Sign-In** tab and then the **SSO** subtab. Click Show Advanced Settings, find the **Logout Redirect URIs** field, and then enter a complete URI for redirecting to the application.

Up to five **logout redirect URIs** can be configured as a whitelist. The value of the  `post_logout_redirect_uris`  parameter that is contained in the logout request sent to the SLO endpoint must be included in this whitelist for the redirection to take effect.

![](assets/f149647a31809ce14fea3ca6c21e4625.jpeg)

After the configuration is saved, you can include the  `post_logout_redirect_uris`  parameter in the request sent to the SLO endpoint to implement redirection upon logout.

**Automatic logout**

To log out and redirect to the application page without manual confirmation, include the  `id_token_hint`  parameter in the request sent to the SLO endpoint after you configure the **Logout Redirect URIs** field.

The following table describes the parameters supported by the SLO endpoint.

| Parameter | Req uire d | Description |
| --- | --- | --- |

<table>
  <tr>
    <td>id_token_hint</td>
    <td>No</td>
    <td>This parameter is required to implement automatic logout. It verifies whether a logout request is valid.<br>Pass the value of <code> id_token </code>, which is the same as the session ID and is issued by IDaaS during SSO.<br>Note<br>If it differs from the session ID in IDaaS, manually confirm the logout.<code>  </code> Even if it expires, do not manually confirm the logout because the value of <code> id_token </code> is the same as the session ID.<br>This limit is a security design in the OIDC protocol specifications to prevent malicious logout.</td>
  </tr>
  <tr>
    <td>post_logout_redirect_uris</td>
    <td>No</td>
    <td>This parameter is required when you want to implement automatic redirection upon logout.<br>Pass in an HTTPS URI for redirecting to the application upon logout. This URI must be preconfigured in the Logout Redirect URIs field on the application management page of IDaaS.</td>
  </tr>
  <tr>
    <td>state</td>
    <td>No</td>
    <td>A random string. If automatic redirection is configured and this parameter is passed to IDaaS, this parameter is returned to the application as a redirect parameter.<br>This parameter is used for security verification.</td>
  </tr>
</table>

The following example shows a request sent to the SLO endpoint:

```text
GET https://example.aliyunidaas.com/login/app/<application_id>/oauth2/logout
 ?id_token_hint=${id_token}
 &post_logout_redirect_uri=${post_logout_redirect_uri}
 &state=${state} 
```

**SLO flowchart**

![](assets/f149647a31809ce14fea3ca6c21e4625.jpeg)

> **Note**
>
> The SLO feature in IDaaS has the following limits:
>
> - IDaaS can implement SLO based on only OIDC.
>
> - IDaaS supports SLO initiated only by service providers (SPs).
>
> - IDaaS logs out only applications of the primary IDaaS logon session and does not log out other logged-on applications. In other words, global SLO is not implemented.

**References**

- OpenID Connect RP-Initiated Logout 1.0

<a id="section-4-2-7"></a>

### 4.2.7. Grant application permissions

You can grant permissions to access an application to organizations or accounts. Accounts that do not have the required permissions cannot access the application.

> **Note**
>
> You can set the Authorize parameter of the application to All Users in the SSO configuration of the IDaaS application. If you select All Users, you do not need to manage application permissions, and manual authorization is not applied. If you want to specify the authorization scope, set the Authorize parameter to Manually.

**Manage permissions**

You must be an administrator to manage permissions. Go to the Application page, click the name of the application that you want to manage, click **Sign-In**, and then click the **Authorize** tab. Then, you can view the permissions and grant permissions to or revoke permissions from accounts or organizations.

> **Note**
>
> After you grant permissions to an organization, all accounts under the organization have permissions. IDaaS does not record the permissions of individual accounts under the organization. You can choose **User > Accounts and Orgs** in the left-side navigation pane, click the account that you want to view, and click the **Permissions** tab to check whether the account has permissions.

image.png

**Grant permissions**

Click Authorize. The Authorize dialog box appears.

image.png

Search for the IDaaS organization or account in the dialog box. Select the organization or account to which you want to grant permissions.

Confirm the selected organization or account and click Confirm.

<a id="section-4-2-8"></a>

### 4.2.8. Synchronize accounts - IDaaS event callbacks

You can synchronize organizations and accounts between Identity as a Service (IDaaS) and applications. For more information, see Synchronize accounts. IDaaS allows you to synchronize all IDaaS accounts to an application at one time. IDaaS can also send notifications on incremental changes.

**Synchronize accounts**

Go to the **Provisioning** tab, turn on Provision IDaaS Accounts to Application, and configure the **Synchronization Scope** parameter.

![](assets/1b9fb4e2d5687d44bae5a2151eec8220.jpeg)

After you configure the **Synchronization Scope** parameter, the application can obtain the organization and account information from the specified IDaaS node.

**Configure push parameters**

Click the **Synchronize IDaaS Users on Application** tab.

IDaaS supports the following application synchronization modes:

- Shortcut mode: the event callback mode defined by IDaaS. This mode is recommended for most applications.

- System for Cross-domain Identity Management (SCIM) mode: This mode is suitable for applications supporting SCIM clients. For more information, see Synchronize IDaaS accounts to an application by using SCIM.

![](assets/ab0765784ef47507faeb168101a06604.jpeg)

Configure the basic push parameters. The following table describes the parameters.

| Parameter | Description | Example |
| --- | --- | --- |
| Synchronization Scope | The organization that you want to synchronize. If you perform this operation by using an API operation, you can synchronize data of only the selected organization. | Alibaba Cloud IDaaS |
| Public Key Endpoint | The synchronization request contains a signature. The receiver must obtain the public key from IDaaS and verify the synchronization request. | None |
| Outbound IP Address | Add the outbound IP address of IDaaS to the whitelist of the application to ensure that IDaaS requests can be received as expected. | None |
| URL for Receiving Synchronization Requests | The URL that is used to receive synchronization requests.<br>The URL must follow the rules in Developer Guide and serve multiple purposes including connection testing, account reception, and organization reception. For more information, see <strong>Developer Guide &gt; Overview</strong>. | https://www.example.com/accounts/provisio n |
| Encryption | If you select this option, service data is encrypted by using a key and then transmitted. If you need to transmit data over the Internet, we recommend that you select this option to ensure secure data transmission. | The option is cleared. |
| Encryption Key | The key that is used to encrypt service data.<br>The key can be generated by IDaaS or manually specified. | <code>2fdc67ca538cc9500b</code><br><code>cad6518390feb937b58e</code><br><code>9102b00bffb30a292112</code><br><code>fdf626</code> |
| Password Synchronization | If you select this option, plaintext passwords are passed in the data of a specific event. The following events are supported:<br>• Create User<br>• Change Account Password (changing or resetting the password)<br>If you select Service Data Encryption at the same time, passwords and service data are encrypted during transmission. | The option is cleared. |

After you configure the push parameters, you can subscribe to change events to receive notifications when events occur.

![](assets/7b7a6b51c971924949ba0eef413bea1d.jpeg)

> **Note**
>
> IDaaS defines more than 10 types of account and organization change events. The events are classified into incremental change events and full change events. For more information, see **Developer Guide > Contact events**.

After the configuration is complete, you can perform the following operations only if Provision IDaaS Accounts to Application is turned on.

- Click **Test Connectivity** to verify that the connection is valid, the network access is stable, and the request can be processed as expected.

- Click **Push Now** to initiate a full synchronization task.

![](assets/873b7816d1e06a7829adfa3a92cdad2e.jpeg)

To receive event requests sent from IDaaS, you must complete the integration steps in **Developer Guide > Overview**.

<a id="section-4-2-9"></a>

### 4.2.9. Synchronize IDaaS accounts to an application by using SCIM

This topic describes how to use System for Cross-domain Identity Management (SCIM) to synchronize accounts from Employee Identity and Access Management (EIAM) of Identity as a Service (IDaaS) to an application. With SCIM, enterprises can efficiently synchronize user and organization data to third-party applications, which simplifies identity management and improves O&M efficiency. This topic describes the procedure, API operation calls, and usage notes to help enterprises quickly integrate identity information across systems.

**Usage notes**

- You cannot synchronize organizations to downstream applications by using SCIM in IDaaS EIAM.

- IDaaS EIAM supports both group and account synchronization. However, whether groups and accounts can be synchronized to downstream applications depends on the integration capabilities of the applications. You can synchronize only accounts to Resource Access Management (RAM) and synchronize accounts and groups to CloudSSO by using SCIM in IDaaS.

- Field values in RAM are not case-sensitive. When you synchronize accounts to RAM or CloudSSO by using SCIM, the values of the account fields are converted to lowercase letters before the accounts are synchronized. This prevents data conflicts.

**Procedure**

On the **Provisioning** tab of the **Application** page, administrators can set the Push Mode parameter to SCIM Protocol. This way, accounts can be synchronized to a SCIM-enabled application by using SCIM.

To synchronize accounts from IDaaS to an application by using SCIM, you must configure both IDaaS and the application. The following table describes the topics related to how to synchronize accounts to RAM or CloudSSO. If you want to synchronize accounts to other applications by using SCIM, refer to the corresponding topic.

The method for configuring SCIM-based account synchronization is similar to that for configuring the event callback-based shortcut mode. You need to first specify the synchronization scope and configure the SCIM client parameters.

![](assets/704638115f2b1e587d76d9a2c9bda02a.jpeg)

The following table describes the parameters.

| Parameter | Description |
| --- | --- |
| Outbound IP Address | Add the outbound IP address of IDaaS to the whitelist of the application to ensure that IDaaS requests can be received as expected. |
| SCIM Base URL | Specify the address of the client that receives SCIM-based synchronization requests. |
| Grant Type | The API authentication method may vary based on the SCIM client. You can set the Grant Type parameter to <strong>OAuth 2.0 Client Credentials</strong> or <strong>Bearer Token</strong> <strong>Mode</strong> based on the SCIM client.<br>For example, RAM supports OAuth 2.0 Client Credentials to authenticate SCIM requests. The following figure shows the configuration example.<br>![](assets/7232384eeb7409943f2c0033d3334676.jpeg) |
| Operation | Administrators can subscribe to the change events they want to follow to get notified immediately.<br>When a change occurs in IDaaS, IDaaS automatically synchronizes the change to the application.<br>![](assets/306615e3d1de821acb59372206da5f1d.jpeg)<br>Note<br>Events of API operation calls are synchronized in both full and incremental synchronization modes. |
| Full Scope | If you turn on the Synchronize switch, you can synchronize only the data selected in the Full Scope section and the data within the synchronization scope of the application to downstream applications. For example, if you select Account in the Full Scope section, you can synchronize only accounts.<br>![](assets/0cd5a959ab578f82c30ad7daa5edc32c.jpeg)<br>Note<br>This parameter takes effect only for full data synchronization. |
| Field Mapping | This parameter displays the field mappings involved in SCIM-based synchronization.<br>![](assets/9c22bfed560fa7fc701b2241d865dc0e.jpeg) |

After you save the configuration, we recommend that you click **Test Connectivity** to check whether the configuration is valid.

You can click Push Now to synchronize all accounts within the specified synchronization scope to the application based on your business requirements.

**References**

- RFC7643: System for Cross-domain Identity Management: Core Schema

- RFC7644: System for Cross-domain Identity Management: Protocol

<a id="section-4-2-10"></a>

### 4.2.10. Synchronize data from an application to IDaaS by using SCIM

You can synchronize accounts and groups between Identity as a Service (IDaaS) and applications by using the System for Cross-domain Identity Management (SCIM) protocol. In the synchronization process, IDaaS serves as the SCIM server. The SCIM protocol standardizes data sharing principles and API definitions between identity systems. This enhances the interoperability between identity systems.

**Prerequisites**

- IDaaS is activated, and you are logged in to the Alibaba Cloud IDaaS console.

- SCIM is supported by upstream identity providers (IdPs), and all required configurations and information are prepared.

**Step 1: Add an application**

1. Log in to the IDaaS console and click **Console** in the Actions column of the desired IDaaS instance.

2. In the left-side navigation pane, click **Application > Add Application**.

3. Create a **standard protocol** or **custom application** and click **Add Application**.

4. In the dialog box that appears, specify the **name of the application** and click **Add**.

**Step 2: Synchronize accounts between IDaaS and applications**

1. In the application list, find the created application and click the application name to go to the details page of the application.

2. Click the **Provisioning** tab and configure the **Provisioning Scope** parameter.

3. Click the **Synchronize Application to IDaaS** tab and select a value from the **Synchronization Scope** drop-down list.

> **Note**
>
> By default, you can synchronize accounts only between IDaaS and custom and standard protocol applications.

**Step 3: Configure SCIM parameters**

1. On the **Synchronize Application to IDaaS** tab, configure the following parameters.

2. Configure the following parameters as prompted:

   - **Bearer Token:** used for identity authentication. You can use a bearer token to access protected resources without the need to repeatedly provide login credentials. You can use a bearer token in the same way as a proxy token in a custom domain name. You can add up to two bearer tokens and must manually enable at least one. You must disable a bearer token before you delete it. A bearer token is part of the credential management module and is on the same level as the client ID and secret. To ensure a bearer token’s security, specify its validity period upon adding it.

     > **Note**
     >
     > After you click **Add Bearer Token**, the **Specify Validity Period** dialog box appears. By default, the Validity Period of Bearer Token parameter is set to 365 days. You can change this value. The system automatically displays the new value. The validity period of a bearer token ranges from 1 to 1095 days (3 years). If the specified value exceeds the limit, the **The validity period must be at least 1 day and can be up to 3 years. Select a valid period.** error message appears.

   - **SCIM Base URL:** provides the base path for accessing synchronization requests of the SCIM client. Example: https://example.aliyunidaas.com.

   - **Configure SCIM Operation Permission:** allows you to manage supported SCIM operations. After you click **Authorize**, you are redirected to the **IDaaS API** page.

3. Turn on **IDaaS API**. In the **SCIM API Permissions** section, select the required **scenarios** for which you want to enable the corresponding API operations. Then, click **Save**.

4. Click **Save**.

**Fields that can be synchronized**

**User:**

<table>
  <tr>
    <th>SCIM Field</th>
    <th>IDaaS Field</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>id</td>
    <td>userId</td>
    <td>The unique ID of the user.</td>
  </tr>
  <tr>
    <td>userName</td>
    <td>username</td>
    <td>The username.</td>
  </tr>
  <tr>
    <td>displayName</td>
    <td>displayName</td>
    <td>The display name of the user.</td>
  </tr>
  <tr>
    <td>phoneNumbers [type eq "work"]</td>
    <td>phoneNumber</td>
    <td>The mobile phone number of the user.<br>Numbers that include the country code must start with a plus sign (+).<br>You can add only one mobile phone number, and it must be of the work type.</td>
  </tr>
  <tr>
    <td>phoneRegion</td>
    <td>phoneRegion</td>
    <td>The country or region code of the mobile phone number.<br>If you do not configure this field and the number includes the country code, the code is truncated.<br>If you specify a value that differs from the country code of the number, an error is reported.<br>If you configure this field and the number does not include the country code, the default value 86 is used.</td>
  </tr>
  <tr>
    <td>emails [type eq "work"]</td>
    <td>email</td>
    <td>The email address of the user. You can add only one email address, and it must be of the work type.</td>
  </tr>
  <tr>
    <td>externalId</td>
    <td>userExternalId</td>
    <td>The external ID of the user.</td>
  </tr>
  <tr>
    <td>active</td>
    <td>status</td>
    <td>The status of the user. Valid values:<br>true: The user is enabled.<br>false: The user is disabled.</td>
  </tr>
  <tr>
    <td>password</td>
    <td>password</td>
    <td>The password displayed in plaintext. If the format is incorrect, an error is reported.</td>
  </tr>
  <tr>
    <td rowspan="2">urn:ietf:params:scim:sch emas:extension:enterpris e:2.0:User<br>• organization</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>organizationId</td>
    <td>The ID of the organization to which the account belongs.<br>If you do not configure this field, the account is assigned to the synchronization target.<br>If you specify an organization, the account is assigned to the specified organization.</td>
  </tr>
</table>

**Group:**

<table>
  <tr>
    <th>SCIM Field</th>
    <th>IDaaS Field</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>id</td>
    <td>groupId</td>
    <td>The unique ID of the group.</td>
  </tr>
  <tr>
    <td>displayName</td>
    <td>groupName</td>
    <td>The name of the group.</td>
  </tr>
  <tr>
    <td>externalId</td>
    <td>groupExternalId</td>
    <td>The external ID of the group.</td>
  </tr>
  <tr>
    <td rowspan="4">members<br>• type<br>• value<br>• $ref</td>
    <td>-</td>
    <td>The group member.</td>
  </tr>
  <tr>
    <td>-</td>
    <td>The type of the group member. Set the value to User.</td>
  </tr>
  <tr>
    <td>userId</td>
    <td>The unique ID of the user.</td>
  </tr>
  <tr>
    <td>-</td>
    <td>The complete URL of the member.</td>
  </tr>
</table>

<a id="section-4-2-11"></a>

### 4.2.11. Open API operations

Identity as a Service (IDaaS) provides open API operations to application developers. .

You can call these API operations to synchronize accounts and organizations to IDaaS and manage the lifecycle of employees, including onboarding, offboarding, and transfer. .

The IDaaS administrator has full management permissions on applications. The administrator can specify whether to expose the API operations and manage the permissions on the API operations.

**Enable or disable API operations**

You can enable or disable API operations for the specified application on the **IDaaS API** tab.

image.png

After you enable an API operation, provide the  `client_id`  and  `client_secret`  obtained from the General tab to application developers. After permissions are granted, the application developers can call the API operation.

**Manage permissions on API operations**

The administrator can manage permissions on the API operations of an application.

> **Note**
>
> The Developer API operations in IDaaS are different from Alibaba Cloud OpenAPI and depend on the key of the application in IDaaS. The permissions to call these API operations are managed in the IDaaS console. Permissions to call the Developer API operations are not managed by Resource Access Management (RAM).

In the **IDaaS API** tab, you can select scenarios to enable the API operations corresponding to the selected scenarios.

image.png

**Data permissions**

You can configure the **Synchronization Scope** parameter on the Provisioning tab to limit the scope of available data.

image.png

Only data within the specified synchronization scope can be queried or used to create resources by calling API operations. .

You can manage the synchronization scope on the Provisioning tab.

**Development and integration**

For more information, see **Developer Guide > Application development APIs**. .

<a id="section-4-2-12"></a>

### 4.2.12. Management permissions on Apsara Stack applications

Apsara Stack Identify as a Service (IDaaS) is committed to providing secure identity services for the Apsara Stack ecosystem. Therefore, stable IDaaS services and application configurations are important to customers.

Guided by the principle that the user who creates a resource must manage and destroy the resource, the lifecycle of application resources is managed in cloud services. Operations including application creation, configuration, management, and deletion are performed in cloud services. Applications cannot be managed in IDaaS.

For example, Apsara Stack services are prioritized and displayed as ecosystem partners in the marketplace. These services cannot be created in IDaaS and must be created in the corresponding consoles. Then, you can bind these services to IDaaS instances by using the user management feature to create applications in IDaaS. The following figure shows how Robotic Process Automation (RPA) is displayed in the IDaaS marketplace.

The lifecycle of a cloud service application is managed in the cloud service, and different permissions are required for using different API operations and features. When a regular user attempts to perform unauthorized operations on the application of a cloud service, the  `InvalidOperation.ResourceManagedByCloudProduct`  error code is returned.

The following table describes the permissions required for calling API operations.

| Operation description | OpenAPI | Can be called by your Apsara Stack tenant account | Can be called by using the cloud service that hosts the application |
| --- | --- | --- | --- |
| Updates the name and logo of the application. | UpdateApplicationInfo | No | Yes |
| Updates the description of the application. | UpdateApplicationDescription | Yes | Yes |
| Deletes the application. | DeleteApplication | No | Yes |
| Enables the application. | EnableApplication | No | Yes |
| Disables the application. | DisableApplication | No | Yes |
| Enables Single Sign-On (SSO) for the application. | EnableApplicationSso | No | Yes |
| Configures SSO for the application. | SetApplicationSsoConfig | No | Yes |
| Disables SSO for the application. | DisableApplicationSso | No | Yes |
| Sets the account synchronization scope for the application. | SetApplicationProvisioningSco pe | No | Yes |
| Configures account synchronization for the application. | SetApplicationProvisioningCo nfig | No | Yes |
| Disables account synchronization for the application. | DisableApplicationProvisionin g | No | Yes |
| Enables account synchronization for the application. | EnableApplicationProvisioning | No | Yes |
| Disables Developer API operations for the application. | DisableApplicationApiInvoke | No | Yes |
| Enables Developer API operations of the application. | EnableApplicationApiInvoke | No | Yes |
| Configures the scope of Developer API operations that the application can call. | SetApplicationGrantScope | No | Yes |
| Creates a client secret for the application. | CreateApplicationClientSecret | No | Yes |
| Deletes the client secret of the application. | DeleteApplicationClientSecret | No | Yes |
| Queries the client secret of the application. | ObtainApplicationClientSecret | No | Yes |
| Enables the client secret of the application. | EnableApplicationClientSecret | No | Yes |
| Disables the client secret of the application. | DisableApplicationClientSecre t | No | Yes |
| Other operations related to the application and read-only operations. | - | Yes | Yes |

<a id="section-4-3"></a>

## 4.3. Configurations of common applications

<a id="section-4-3-1"></a>

### 4.3.1. Configure 2FA for establishing SSL-VPN connections in Alibaba Cloud

This topic describes how to configure Identity as a Service (IDaaS)-based two-factor authentication (2FA) for establishing SSL-VPN connections in Alibaba Cloud.

**Scenarios**

After you enable 2FA, the system verifies your client based on two factors when the client establishes an SSL-VPN connection. The client must pass SSL client certificate authentication and the username and password authentication of an IDaaS account, an Active Directory (AD) account, or a Lightweight Directory Access Protocol (LDAP) account. The SSL-VPN connection is established only after the client passes the 2FA. This improves the security of SSL-VPN connections. This topic describes how to establish an SSL-VPN connection between a client and a virtual private cloud (VPC) after the client passes the 2FA to allow the client to access the resources in the VPC.

![](assets/c3fca84eb53955ae4d7b39e0d03e1ef5.jpeg)

The preceding figure shows the scenario of the example used in this topic. A company uses IDaaS to manage and maintain employee accounts and permissions. The company has created a VPC in Alibaba Cloud. Applications are deployed on Elastic Compute Service (ECS) instances in the VPC. To meet business requirements, the company wants to allow employees on business trips to remotely access resources that are deployed in the VPC after the employees pass IDaaS authentication.

In this case, the company can create a VPN gateway and enable the SSL-VPN and 2FA features. After a client passes the SSL client certificate authentication and the username and password authentication of IDaaS, the client can establish an SSL-VPN connection to access resources in the VPC in a secure manner.

**Step 1: Add an application in the IDaaS console**

1. Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Security** > **Identity and O&M Security** > **IDaaS**.

![](assets/61e11a93214cf73ca70a40f12bd149d4.jpeg)

2. On the IDaaS page, find an instance and click **Console** in the Actions column.

![](assets/4356cc8ae91f2e615927de1c5b6c1461.jpeg)

3. In the left-side navigation pane, click **Application**. On the Application page, click **Add Application** to go to the **Marketplace** tab. Then, search for **Alibaba Cloud - SSL VPN** and click **Add Application**.

4. In the dialog box that appears, confirm the application name and click **Add**.

   image

5. On the Sign-In tab, grant permissions to accounts to access the application.

   image

   If all IDaaS accounts in your instance need to use the application, select **All Users** from the Authorize drop-down list to authorize all accounts to access the application.

   If you want to grant permissions to specific IDaaS accounts, select **Manually** from the Authorize drop-down list and grant permissions to the accounts on the **Authorize** tab.

   image

**Step 2: Create an SSL server**

1. Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** > **Networking** > **Virtual Private Cloud**.

2. In the left-side navigation pane, choose **VPN Gateways**.

3. In the top navigation bar, select the organization in which you want to create an SSL server.

4. On the **SSL Servers** page, click **Create SSL Server**.

   image

5. On the **Create SSL Server** page, configure the following parameters for the SSL server and click **Submit**:

   - **Name**: Enter a name for the SSL server.

   - **VPN Gateway**: Select the SSL VPN application that you created in Step 1 from the drop-down list.

   - **Local CIDR Block**: Enter the CIDR block that your client needs to access over an SSL-VPN connection. In this example, **192.168.1.0/24** is used.

   - **Client CIDR Block**: Enter the CIDR block that your client uses to connect to the SSL server. In this example, **10.0.0.0/24** is used.

     image

   - **Advanced Settings**: Select **Configure** and configure the following parameters:

     - **Protocol**: Select the protocol for an SSL-VPN connection. Valid values: UDP and TCP. In this example, the default value is used.

     - **Port**: Specify the port used by an SSL-VPN connection. In this example, the default value is used.

     - **Encryption Algorithm**: Select the encryption algorithm for an SSL-VPN connection. Supported encryption algorithms include AES-128-CBC, AES-192-CBC, and AES-256-CBC. In this example, the default value is used.

     - **Compressed**: Specify whether to compress the data that is transmitted over an SSL-VPN connection. In this example, the default value is used.

     - **Two-factor Authentication**: Turn on Two-factor Authentication, select the required IDaaS instance, and then select the application that you created in Step 1.

       image

**Step 3: (Optional) Configure AD or LDAP authentication**

> **Note**
>
> By default, you can use the username and password of an IDaaS account for 2FA. You can also configure Active Directory (AD) authentication. After you complete the configuration, SSL-VPN connections support AD authentication. If you use only the username and password of an IDaaS account for authentication, skip this step.

1. On the **IdPs** page of the IDaaS console, click Bind AD or Bind OpenLDAP to add an authentication source based on your business requirements.

   image

   For more information about how to add an authentication source, see Connect an AD as an inbound identity provider and Connect to OpenLDAP - Inbound.

2. On the **Applications** page of the IDaaS console, find the application that you created in Step 1 and click **Manage** in the Actions column.

   image

3. On the page that appears, click the **Sign-In** tab. On the **SSO** subtab, select the type of authentication source that you want to use from the **IdPs** drop-down list.

   image

**Step 4: Create and download an SSL client certificate**

Create and download an SSL client certificate based on the configurations of the SSL server.

1. Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **ProductsNetworkingVirtual Private Cloud**.

2. In the left-side navigation pane, choose **VPN Gateways > SSL Clients**.

3. In the top navigation bar, select the region in which you want to create an SSL client.

4. On the **SSL Clients** page, click **Create SSL Client**.

5. On the **Create SSL Client Certificate** page, configure the following parameters and click **Submit**:

   - **Name**: Enter a name for the SSL client certificate.

   - **SSL Server**: Select the SSL server that you created in Step 2.

   image

6. On the **SSL Clients** page, find the SSL client certificate that you create and click **Download** in the Actions column.

   image

**Step 5: Configure an OpenVPN client**

To configure an OpenVPN client for Windows, perform the following operations:

1. Download and install OpenVPN. Internet access is required for the downloading.

2. Decompress the downloaded SSL client certificate package and copy the SSL client certificate to the OpenVPN\\config directory.

   In this example, the certificate is copied to C:\\Program Files\\OpenVPN\\config. You need to copy the certificate to the directory in which OpenVPN is installed.

   image

3. Start OpenVPN and enter the username and password for authentication.

   客户端验证账号密码

<a id="section-5"></a>

# 5.Login

<a id="section-5-1"></a>

## 5.1. General settings

This topic describes the login methods supported by Identity-as-a-Service Enterprise Identity Access Management (EIAM IDaaS), including passwords, test message verification codes, logins from other third-party applications such as WeChat and DingTalk, and multi-factor authentication (MFA). This helps administrators flexibly configure enterprise-class authentication policies to improve account security.

**Login methods**

1. **Three built-in login methods of IDaaS**

   | Login method | Description |
   | --- | --- |
   | Login by using the IDaaS account password | By default, this login method is enabled.<br>Users log in with their account usernames and passwords stored in IDaaS.Users who do not have an account username or password cannot log in by using this method. For example, an account that is recently imported from DingTalk and does not have an account username or password in IDaaS cannot use this login method. |
   | Test message verification code | This method is disabled by default and can be manually enabled.<br>To use this login method, the user must associate a mobile phone number with their account.<br>Users can view the text message, but cannot modify the text message.<br>No text message fee is charged by the current version. |
   | Web Authentication (WebAuthn) | Users can use their hardware identity to log in with security and convenience based on the WebAuthn protocol.<br>For more information, see WebAuthn login. |

2. **Add a login method**

   Other login methods provided in IDaaS must be enabled based on the Identity Provider (IdP) configuration. When an administrator adds an IdP, a login capability may be automatically added as a login method.

   When you enable this feature for the first time, the corresponding login method is automatically created.

   For example, if Sign-In with QR Code is disabled on the IdPs page, the QR Code (DingTalk) login method is also disabled on the Authentication Methods tab.

3. **Disable a login method**

   After a login method is disabled, it becomes unavailable and is not displayed on the login page.

**Login settings**

1. **Configure basic settings for IDaaS login**

2. **The following table describes the parameters.**

   <ol type="i">

   <li>

   **Skip Logon Page**: After this feature is enabled, only one login method is available. The login method must be based on the OpenID Connect (OIDC) authentication protocol or Lark login. When users access the login page of IDaaS, they can directly redirect to the login page for authentication.

   <ol type="a">

   <li>

   **Validation rules when you save the configuration.** If multiple login methods are enabled, the following message appears:

   ![](assets/7def6ec0ebdb20792660821fbcb141bb.jpeg)

   In this case, the configuration cannot be saved. If only one login method is enabled, the configuration is saved.

   </li>

   <li>

   **Prompts of IdP conflicts.** If you attempt to enable multiple login methods on the **IdPs** page or in the **Sign In > General > Authentication Methods** tab when the **Skip Logon Page** feature is enabled, the following message appears:

   ![](assets/b3961b535ac95cca326eba089134432f.jpeg)

   > **Note**
   >
   > The login page is skipped only when both of the following conditions are met: Only one of the Lark or OIDC authentication sources is enabled, and the Skip Logon Page feature is enabled. Otherwise, the Skip Logon Page feature does not take effect even if it is enabled.

   </li>

   </ol>

   </li>

   <li>

   **PC Primary Authentication Method**: the default login method of IDaaS displayed on the PC. Users can switch to another login method.

   </li>

   <li>

   **Prioritized Authentication Method for Mobile Apps**: the default login method of IDaaS displayed on the mobile app. Users can switch to another login method.

   </li>

   <li>

   **Session Validity Period**: the session persistence period for browser login. After the session persistence period ends, the user needs to log in again. This is a security mechanism. In this example, the session persistence period is set to 8 hours.

   </li>

   <li>

   **Idle Session Timeout Period**: the idle session timeout period. After the timeout period ends, the user needs to complete authentication again. This is to prevent unauthorized access. In this example, the idle session timeout period is set to 2 hours.

   </li>

   </ol>

<a id="section-5-2"></a>

## 5.2. Authentication configuration

<a id="section-5-2-1"></a>

### 5.2.1. 2FA

This topic describes the two-factor authentication (2FA) feature and how to bind 2FA methods to users when they log in to Identity as a Service (IDaaS).

**Configure 2FA**

IDaaS supports 2FA. To ensure security and meet compliance requirements, users are required to complete 2FA after logging in with a password. For your security, 2FA is enabled by default.

**Modes**

IDaaS supports the following modes of 2FA.

| Mode | Scenario | Description |
| --- | --- | --- |
| Intelligent (recommend ed) | If the system detects the following high-risk login behaviors, the intelligent mode is automatically triggered to improve account security:<br>1. Login from a uncommonly used geographic location. For example, a user based in Beijing logs in from a foreign country or an uncommonly used CIDR block.<br>2. Login from a uncommonly used device For example, a user logs in from an uncommonly used mobile phone, an uncommonly used browser, or a new account.<br>3. High-risk operations. For example, a user attempts to gain sensitive permissions, such as console administrator permissions, or frequently changes account security settings, such as repeated password resets.<br>4. Risks detected by system security policies. For example, the system detects proxies or VPN services in the login environment or successful login after multiple login failures. | IDaaS Enterprise Identity Access Management (EIAM) decides whether 2FA is required based on the context. This mode ensures security and provides smooth user experience. |
| Always | 1. Security-sensitive business systems.<br>2. Scenarios in which regulatory compliance check is required at each login.<br>3. Privileged accounts such as administrator accounts. | 2FA is required for each login. |

**2FA methods**

IDaaS supports various 2FA methods. Administrators can enable multiple 2FA methods at the same time.

| Method | Description |
| --- | --- |
| One-time password (OTP) | A user uses the Alibaba Cloud app or other common OTP apps, such as Google Authenticator, to generate a 6-digit code to complete 2FA.<br>A user can bind an OTP app to the account on the Account page in the IDaaS console.<br>An administrator can unbind an OTP app from an account. For more information, see Account details. |
| Text message verification code | A text message that contains a 6-digit verification code is sent to the mobile number of an IDaaS EIAM user. This method is unavailable for accounts that are not associated with a mobile phone number.<br>Text messages are free of charge.<br>You can view the content of text messages that are sent by IDaaS EIAM on the Branding &gt; SMS Gateway tab. For more information, see SMS gateway. |
| Email verification code | An email that contains a 6-digit verification code is sent to the email address of an IDaaS EIAM user. This method is unavailable for accounts that are not associated with an email address.<br>You can view the email content on the Branding &gt; Email Template page. For more information, see Email template. |
| WebAuthn | The WebAuthn authenticator is used as a second factor to implement hardware-level secure and convenient authentication.<br>For more information, see WebAuthn login. An administrator can register a WebAuthn authenticator for an account or remove a WebAuthn authenticator from an account. |

> **Note**
>
> An IDaaS EIAM user must bind at least one 2FA method to the account to complete 2FA. We recommend that you enable 2FA for logins or make sure that all IDaaS users can use at least one method to complete 2FA. For more information, see Bind a 2FA method at login.

After 2FA is enabled, all IDaaS EIAM users can use the feature. Users can choose a method to complete 2FA. The following figure shows an example.

**Bind a 2FA method at login**

After you enable 2FA for logins, users can bind available 2FA methods to their accounts during logins if the specified binding conditions are met.

**Binding conditions**

Users can bind 2FA methods to their accounts during logins only if the accounts meet all the enabled binding conditions.

| Condition | Description |
| --- | --- |
| No Two-factor Authentication Method in Use | This condition is met if an account is not bound to any of the enabled two-factor authentication methods. For example, if the text message verification code method is enabled but an account is associated only with an email address, this condition is met. |
| No Successful Logon Record | Only accounts with no successful login records can be bound to two-2FA methods. We recommend that you enable this condition to reduce the risk of account theft. You can also enable this condition after 2FA methods are bound to all existing users. |
| Account Exists for Less Than n Days | A new account can be bound to 2FA methods only after a specific period of time. We recommend that you enable this condition to reduce the risk of account theft. |

**Available 2FA methods**

If a user meets the enabled binding conditions, the user can bind available 2FA methods to the account.

In the following example, both the SMS (text message verification code) and email methods are enabled for the IAAS EIAM instance, but only SMS is enabled as the available 2FA method.

In this case, if the account of a user is not associated with a mobile number and an email address, the user can bind a mobile number but not an email address as the 2FA method to the account during logins.

<a id="section-5-2-2"></a>

### 5.2.2. WebAuthn login

This topic describes how to configure and enable Web Authentication (WebAuthn) authentication in Enterprise Identity Access Management (EIAM) of Identity as a Service (IDaaS). WebAuthn provides a more secure and convenient password-free login experience. This topic describes the benefits of WebAuthn authentication and configuration procedure to help administrators quickly integrate WebAuthn authentication with their EIAM system.

**Feature overview**

WebAuthn is a component of Fast Identity Online (FIDO) 2.0. WebAuthn implements password-free login to web pages by providing the optimal experience and hardware-level security. WebAuthn allows users to log in to a website by using the native device encryption and biometric authentication capabilities of a PC.

The following types of authenticators are supported:

- Cross-platform authenticator (also known as roaming authenticator): an external authenticator that is used across different devices, such as YubiKey.

- Platform authenticator: the native authenticator of a browser, such as macOS Touch ID or Windows Hello.

**Demo**

Users can log in by entering only the username. Users do not need to enter the password. The following video shows how to register the device information for WebAuthn.

![](assets/00d696f041f0abd96d367535f96693da.png)

**Register the authenticator**

Before users log in by using an authenticator, users must bind the authenticator to their accounts.

Go to the **My Account** page. Find **WebAuthn Authenticator** in the **Security Information** section and click Manage. In the Manage WebAuthn Authenticator panel, register an authenticator.

![](assets/00d696f041f0abd96d367535f96693da.png)

The registration process requires 1 minute to complete. After you click Register New Authenticator, complete the configurations as prompted.

After the registration is complete, the enabled authenticator can be used for login. Users can also manage the registered authenticators.

> **Note**
>
> Administrators cannot manage the authenticators of users. Each user can individually register and manage an authenticator.

**Applicable scenarios**

**Scenario 1: Password-free login**

WebAuthn can be used for password-free login. This is one of the most common and convenient scenarios in which WebAuthn is used.

On the IDaaS login page, a user enters a username and selects a WebAuthn authentication method for verification. The user is logged in to the application after the user passes the authentication. This method can be used to log in to all web applications. The following flowchart shows the process.

![](assets/00d696f041f0abd96d367535f96693da.png)

On the **General** tab of the **Sign-In** page, the WebAuthn authenticator method is displayed in the **Authentication Methods** section. By default, this method is disabled. You must enable the method before you can use the method.

![](assets/7cdac4c49d6b63166ed03fa278c8f855.png)

After you enable the method, the WebAuthn login option is available on the login page. Then, the user can log in by using WebAuthn. The following figure shows an example on how to use macOS Touch ID for login.

![](assets/f15f3e05f7f92c42d57ac7daed81ca6d.png)

IDaaS obtains information about the registered authenticator of a specific account. If the authenticator is not registered, an error occurs and the authenticator cannot be used.

**Scenario 2: Multi-factor authentication (MFA)**

WebAuthn can be used for MFA. This is also one of the most common and most secure scenarios in which WebAuthn is used.

If MFA is enabled, users must be re-authenticated after they enter a username and password. Users can use a WebAuthn authenticator for secure login. The following flowchart shows the process.

![](assets/3ec992c3cd24dd7c14327842090b2024.png)

On the **Authentication Configuration** tab of the **Sign-In** page, click the Two-Factor Authentication tab. Turn on Two-factor Authentication, select **WebAuthn**, and then click Save.

![](assets/19608a90d8e55613b45c2d37767377f4.png)

Then, users must be re-authenticated after they enter a username and password on the login page. If users registered a WebAuthn authenticator, users can use WebAuthn to complete identity authentication in a quick and secure manner. The following figure shows an example on how to use macOS Touch ID for MFA.

![](assets/ebb4165dd74c09df5a0fd461fe1cb541.png)

<a id="section-5-2-3"></a>

### 5.2.3. CAPTCHA verification

Completely Automated Public Turing Test to Tell Computers and Humans Apart (CAPTCHA) verification is a two-factor authentication (2FA) mechanism provided by Identity as a Service (IDaaS) to distinguish between humans and bots or attackers. CAPTCHA verification effectively blocks malicious behaviors, such as brute-force attacks, spam registration, and brushing, to improve system security. This topic describes how to configure and enable CAPTCHA verification.

**Feature overview**

You can configure CAPTCHA verification on the **Sign In > Authentication Configuration** tab. CAPTCHA verification supports the following features:

- **Intelligent verification**: CAPTCHA verification can intelligently distinguish between humans and bots.

- **Multiple verification methods**: Multiple interactive methods are supported, such as slider CAPTCHA, CAPTCHA puzzles, and image CAPTCHA.

- **Flexible configuration**: You can adjust the verification policy and severity based on your business scenario.

**Procedure**

1. **Go to the CAPTCHA Verification page**

1. Log in to the IDaaS Console and find the IDaaS instance that you want to manage.

2. In the left-side navigation pane, **Sign In** and go to the **Authentication Configuration** page.

3. Click the **CAPTCHA Verification** tab.

   2. **Enable CAPTCHA verification**

1. **Enable CAPTCHA verification**: Select **Enable CAPTCHA Verification** to enable this feature.

2. **Select a verification method.** Select a **verification method** that is suitable for your business scenario.

   - **Puzzle CAPTCHA**: Users must combine the image fragments to the correct position.

   - **Image Restoration**: Users must use the slider to restore out-of-order images.

3. **Save the configurations.** After you configure and enable CAPTCHA verification, click **Save** to apply the configurations.

**Usage notes**

- Before you enable CAPTCHA verification, familiarize yourself with the characteristics and applicable scenarios of CAPTCHA verification.

- Select an appropriate CAPTCHA verification method based on your actual business requirements to balance security and user experience.

- Regularly check the configurations and status of CAPTCHA verification to ensure that it operates effectively under the latest security requirements.

<a id="section-5-3"></a>

## 5.3. Password policies

Apsara Stack Identity as a Service (IDaaS) allows administrators to centrally manage password policies to enhance account security. This topic describes the password policy management feature of IDaaS, including password complexity, initial password, password expiration, password history, forgotten password, and high-risk password detection.

**Overview of password policies**

IDaaS allows administrators to centrally manage the following password policies:

- Password complexity

- Initial password

- Password expiration

- Password history

- Forgotten password

- High-risk password detection

**Password complexity**

Passwords are one of the weakest components in network security. A stronger password means higher security.

On the **Password Policy** tab of the **Sign-In** page, IDaaS provides five complexity templates from which you can choose based on different scenarios. The following table describes the five complexity templates.

| Complexity template | Password requirement |
| --- | --- |
| Unrestricted | A minimum of four characters. |
| Simple | A minimum of six characters. It must contain lowercase letters and digits. |
| Common | A minimum of eight characters. It must contain uppercase letters, lowercase letters, and digits. |
| Recommended | A minimum of 10 characters. It must contain uppercase letters, lowercase letters, digits, and special characters. It cannot contain the account name. |
| Complex | A minimum of 16 characters. It must contain uppercase letters, lowercase letters, digits, and special characters. It cannot contain the account name, display name (pinyin), mobile phone number, or email prefix. |

If you are an administrator, you can select one of the templates and change the configuration on demand, or directly customize the complexity configuration. After you complete the configuration, click Save for the configuration to take effect. .

The changed complexity rules do not affect existing passwords, but apply to new passwords.

> **Important**
>
> According to the latest regulations of China Telecom, from May 20, 2025, if text messages sent to mobile phone numbers of China Telecom contain the following information, the text messages may probably be blocked.
>
> - Links or IP addresses
>
> - Contact information, such as mobile phone numbers, landline numbers, or customer service phone numbers.
>
> Due to these regulations, the password field must not contain links (short URLs or HTTP strings) or contact information. This ensures that text messages that contain usernames and passwords are not blocked.

**Initial password**

When an account is imported from an identity provider (IdP), its password in the IdP cannot be obtained in most cases. IDaaS can initialize the passwords for newly imported accounts and notify users to complete the new user login operation.

- **Enable Password Initialization**: By default, this feature is disabled. Administrators can enable this feature.

- **Initialization Method**: If you are an administrator, when you synchronize an account from an IdP to IDaaS and no password is available, you can set Initialization Method to Randomly Generated and Sent to User. This way, IDaaS randomly generates a new password that meets the complexity rules and sends it to users by text message or email.

- **Force Change upon First Login**: This feature forces users to change their passwords when logging in with the randomly generated passwords before they can access the system.

**Password expiration**

Administrators can set the password validity period and create a policy to handle expired passwords.

**Expiration Reminder**

If you are an administrator, you can enable Expiration Reminder and set Expiration Reminder Method to Reminder upon Login. IDaaS reminds users to change their passwords each time they log in to IDaaS N days before their passwords expire. When users are reminded upon login, they can change the password immediately or ignore the reminder.

**Actions to take upon password expiration**

IDaaS provides the following three policies to limit user login upon password expiration:

- **Forbid Login**: a strict policy. If a password expires, the password cannot be used and the password change process cannot be triggered. The user can only use other methods to log in and then change the password or initiate a password reset process. If no other login methods are enabled, the user is unable to log in and can only contact the administrator to reset the password. To avoid this situation, we recommend that you enable Expiration Reminder or configure Forcibly Request Password Change Before Expire.

- **Forcibly Request Password Change**: a balanced policy. If a password expires, the user can still use the password to log in to IDaaS but must change the password before the user can access the portal or an application.

- **Remind User to Change Password**: a loose policy. If a password expires, the user is reminded to change the password each time the user logs in to IDaaS, but the user can always ignore the reminder.

> **Note**
>
> Password expiration only affects user login and does not affect the status of an account.

**Password History**

IDaaS allows administrators to enable historical password detection. After this feature is enabled, when a user changes the password, IDaaS forbids the user from using a new password that is the same as one of the previous N passwords.

**Forgotten password**

Users may forget their passwords when they log in to IDaaS. IDaaS allows users to set a new password on their own.

- **Enable Forgot Password**: By default, this feature is disabled.

- To enable this feature, administrators can go to the **Sign-in > Password Policy > Forgot Password** tab and select **Show Forgot Password**. After this feature is enabled, the **Forgot Password** link is displayed on the password-based login page.

- To reset the password, click **Forgot Password**, choose **SMS Authentication**, **Email Authentication**, **OTP-based Dynamic Verification**, or **WebAuthn Verification** to complete identity authentication, and specify a new password that meets the complexity rules.

  > **Note**
  >
  > If your account is not configured with a mobile phone number or email address, and is not bound with a one-time password (OTP) or WebAuthn, you cannot reset the password. In this case, contact the administrator to reset the password.

**High-risk password detection**

IDaaS maintains a database that contains a great number of compromised passwords. When users change the password, a security check is triggered on the new password, and the check result is displayed on the same page. This feature is enabled by default and cannot be disabled. It is not displayed in the console. The following figure shows a prompt of password detection.

If users are prompted that the new password has been found in a security leak, this password may be exploited by attackers. We recommend that you do not use this password in this case.

<a id="section-6"></a>

# 6.Logs

<a id="section-6-1"></a>

## 6.1. Management operations

This topic describes the operations that administrators can perform on the Manage tab of the Log page in the Identity as a Service (IDaaS) console. On this tab, administrators can view, search, and manage logs of system management operations for auditing and troubleshooting.

**Introduction**

IDaaS generates logs of key operations performed by administrators and users. The retention period of the logs is 180 days. Within the retention period, administrators can view and search logs in order to audit, trace, and analyze management operations.

**Procedure**

1. Log in to the IDaaS console and click **Console** in the Actions column of the desired IDaaS instance. In the left-side navigation pane, click **Log** and then click the **Management** tab.

2. **Select a time range**. You can select a time range to search logs above the list.

   <ol type="i">

   <li>

   Enter the start time and end time.

   </li>

   <li>

   Alternatively, select a time range from the drop-down list, such as Last 7 Days, Last 30

   </li>

   </ol>

   Days, Last 3 Years, or Last 6 Months.

3. **Configure Advanced Search**.

   You can specify the following filter conditions to search for specific records:

   <ol type="i">

   <li>

   **Operator Type**: Select an operator type, such as IDaaS Account, IDaaS Application, RAM User, or RAM Role.

   </li>

   <li>

   **Object Type**: Select an object type, such as Account, Organization, User Group, IdPs, or Application.

   </li>

   <li>

   **Event Type**: Select an event type, such as Application, Authorization, or Authentication.

   </li>

   <li>

   **Event Result**: Select an event result, such as Successful/Skipped or Failed.

   </li>

   </ol>

4. **Perform a search**.

   <ol type="i">

   <li>

   After you specify the filter conditions, click **Search**.

   </li>

   <li>

   To clear all filter conditions, click **Reset**.

   </li>

   <li>

   You can select **Hide After Search** to automatically hide the Advanced Search section

   </li>

   </ol>

   after you perform a search.

5. **View log details**.

   The search result is displayed in a table that consists of the following columns.

   <ol type="i">

   <li>

   **Time**: the time when the operation was performed.

   </li>

   <li>

   **Operator**: the account that was used to perform the operation.

   </li>

   <li>

   **Event Type**: the type of the operation.

   </li>

   <li>

   **Object**: the object on which the operation was performed.

   </li>

   <li>

   **Event Result**: the result of the operation.

   </li>

   </ol>

   Click a log entry to view the detailed information.

<a id="section-6-2"></a>

## 6.2. User behavior

The log module of Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) can record user behavior in details, which helps enterprises monitor and manage user behavior. This topic describes how to query and manage logs on the User Behavior tab of the log module.

**Introduction**

- **User behavior records**: record the key information about user behavior, including the behavior, time, object, and result.

- **Purpose of logs**: help administrators monitor, audit, and manage user behavior in order to identify abnormal behavior, troubleshoot issues, and conduct security audit.

- **Log query and filtering**: allows you to filter logs from multiple dimensions, such as time range or operator.

- **Log display**: displays detailed logs in a table, including the time, operator, event type, and other key information.

- **Log export**: allows you to export logs to Simple Log Service.

**Procedure**

1. **Go to the log module**

   <ol type="i">

   <li>

   Log in to the IDaaS console.

   </li>

   <li>

   On the page that appears, find the desired IDaaS instance.

   </li>

   <li>

   Click **Console** in the Actions column of the instance. In the left-side navigation pane,

   </li>

   </ol>

   click **Log** and then click the **User** tab.

2. **Specify query conditions**

   On the **User Behavior** tab, you can set multiple query conditions to filter logs.

   - **Time range**: Select a time range. You can select last 7 days, last 30 days, last 3 months, or last 6 months or specify a custom time range.

   - **Advanced Search**

     - **Operator Type**: You can select an operator type, such as IDaaS Account, IDaaS Application, RAM User, or RAM Role.

     - **Event Type**: You can select an event type, such as All Event Types, Add Account to Organization, or Register Authenticator.

     - **Object Type**: You can select an object type, such as Account, Organization, User Group, IdPs, or application.

     - **Event Result**: You can select an event result, such as Successful/Skipped or Failed.

3. **Perform a search**

   <ol type="i">

   <li>

   After you specify the filter conditions, click **Search**.

   </li>

   <li>

   To clear all filter conditions, click **Reset**.

   </li>

   <li>

   You can select **Hide After Search** to automatically hide the Advanced Search section

   </li>

   </ol>

   after you perform a search.

4. **View log details**

   The search result is displayed in a table that consists of the following columns.

   <ol type="i">

   <li>

   **Time**: the time when the event occurred.

   </li>

   <li>

   **Operator**: the ID or name of the user who performed the operation.

   </li>

   <li>

   **Event Type**: the type of the operation, such as basic authentication or CAPTCHA verification.

   </li>

   <li>

   **Object**: the object on which the operation was performed, such as User Portal and Password.

   </li>

   <li>

   **Event Result**: the result of the operation, such as Successful or Failed.

   </li>

   </ol>

   Click a log entry to view the details.

<a id="section-6-3"></a>

## 6.3. Synchronization logs

Synchronization logs are a special type of logs. Identity as a Service (IDaaS) records and displays synchronization logs.

The following table describes scenarios in which operations are recorded as synchronization logs, management logs, or user logs.

<table>
  <tr>
    <td></td>
    <td>Inbound</td>
    <td>Outbound</td>
  </tr>
  <tr>
    <td>Recorded as synchronization logs</td>
    <td>Synchronization from an identity provider (IdP)</td>
    <td>• Pushed by IDaaS to an application<br>• Pushed by IDaaS to an IdP (not supported)</td>
  </tr>
  <tr>
    <td>Not recorded as synchronization logs but as management logs or user logs</td>
    <td>• OpenAPI<br>• Developer API (not supported)<br>• System for Cross-domain Identity Management (SCIM) API (not supported)<br>• Lazy loading (not supported)</td>
    <td>Pulled by an application from IDaaS</td>
  </tr>
</table>

> **Note**
>
> Specific operations may be recorded as synchronization logs and management or user logs.

**Task execution**

A task is a collection of synchronization logs.

When an operation involves synchronization of multiple data entries, IDaaS aggregates the batch of synchronization results into a task. This way, you can quickly view the execution status and results.

![](assets/8582d60f4c27568abed4d8873e7e4786.png)

**Events that trigger task records**

| Trigger module | Events that require task records | Events that require only logs |
| --- | --- | --- |
| IdPs<br>IdP | • Batch import (timed/manual) from an IdP<br>• One-time full synchronization to an IdP (not supported) | • Synchronization of a single data change from an IdP to IDaaS<br>• Synchronization of a single data change from IDaaS to an IdP |
| Applications | Synchronization of accounts to an application at a time | Synchronization of a single data change in IDaaS |
| Accounts | Manually triggered synchronization of organizations or accounts (not supported) | - |

**Synchronization task status**

| Status | Description |
| --- | --- |
| Successful | All synchronization requests in this batch are successful. |
| Failed | All synchronization requests in this batch failed due to network issues. |
| Partially Succeeded | Specific requests in this batch failed. You can view the details. |
| Running | Synchronization tasks are still running. The task list is refreshed every five seconds. |
| Initial State | An exception occurs during execution, which causes the synchronization tasks to fail. In this case, you can re-trigger the synchronization tasks. This is a rare exception. |

**Log details**

Administrators can view the status and details of each synchronization request and search for data.

![](assets/c6c3ff8e612ae2fb9ed2dad0ffe75641.png)

If a synchronization request fails to be executed, you can view the cause of the failure. After troubleshooting, you can handle this exception in two ways:

- Manually change the data. Go to the corresponding system and manually change the data to be synchronized this time.

- Push the data again. Push the data again at the synchronization source. Make sure that data duplication does not occur.

<a id="section-7"></a>

# 7.Branding

<a id="section-7-1"></a>

## 7.1. Branding

This topic describes how to configure branding information in the Identity as a Service (IDaaS) console, including enterprise information, login page style, text, terms of service, and default redirect settings.

**Overview**

The branding feature allows you to manage the system default brand and configure the enterprise information and login page.

**Default brand**

- Quantity limit: The system provides one built-in brand, which cannot be deleted.

- Effective scope: The brand supports access only to the default domain name.

- Supported configurations:

  - **Enterprise information**: including the **enterprise logo**, **web page favicon**, and **enterprise name**.

  - **Login page**: the **terms of service** and **default redirect settings**.

- Page limits: The **Style Settings** and **Text Settings** tabs are not displayed in the console. You can modify only the preceding basic information.

**Configure enterprise information**

1. In the **Enterprise** section of the desired brand, click **Configure**.

2. Configure enterprise information.

   <ol type="i">

   <li>

   **Enterprise Icon**: Upload an enterprise logo to be displayed on the login page and portal page. The file must be in the PNG or JPG format and cannot exceed 1 MB in size. We recommend that you set the pixel aspect ratio to 256\*256.

   </li>

   <li>

   **Favicon**: The enterprise favicon is displayed on the Login Page and Portal Page browser tabs. The file must be in the PNG format. We recommend that you use a square image whose pixel aspect ratio to 32\*32.

   </li>

   <li>

   **Enterprise Name**: Enter an enterprise name that is 1 to 64 characters in length. You can set an enterprise name for different languages.

   </li>

   <li>

   **Preview**: In the upper-right corner of the page, select **PC** or **Mobile** to preview the configurations in real time.

   </li>

   </ol>

3. Publish the configurations. Click **Save and Publish** at the bottom of the page to immediately apply the configurations.

**Configure the login page**

**Style settings**

1. Go to the **Login Page Configuration** tab.

   Click **Branding** in the left-side navigation pane and find the brand that you want to manage. On the Branding page, find the brand that you want to configure and click **Configure** in the **Login Page Configuration** section.

   ![](assets/22e93b1813c28d1c84e9703c8b4a7fc1.jpeg)

2. **Configure the style settings**.

   - **Enterprise Icon**: Select Large, Medium, Small, or Left, Center, or Right for the enterprise logo.

   - **Enterprise Name**: Select Left, Center, or Right for the enterprise name.

   - **Page Background**:

     - Select **Background Color** and select a background color in the color picker.

     - Select **Image Background**. You can follow the instructions on the page to configure a background image. For example, **Full Screen, Center, Tile, Stretch, Fit to Screen**.

   - **Login Form Position**: Select **Left**, **Center**, or **Right**.

3. Preview and text the configurations.

   - Click **Save**. In the right-side **Preview** section, select **PC** or **Mobile** to preview the configurations.

   - Click **Login Experience** to open the login page and text the configurations in an interactive manner.

   - To restore the style to the pre-modification style, click **Restore Configuration**.

4. Save and publish the configurations.

   - In the lower-left corner of the page, click **Save** to save the configurations as a draft.

   - To make the configurations take effect for users, click **Publish**.

**Text settings**

![](assets/dd14e1b37a09d703fec38ccf538ada63.jpeg)

1. Go to the **Login Page Configuration** tab.

   Click **Branding** in the left-side navigation pane and find the brand that you want to manage. On the Branding page, find the brand that you want to configure and click **Configure** in the **Login Page Configuration** section.

2. **Select a language.**

   Select a language from the **Select Language** drop-down list, such as **Simplified Chinese (zh-Hans-CN)** or **English (en-US)**.

   > **Note**
   >
   > You can configure a set of text and style settings for each language. After you switch the language, you can configure and save the text separately.

3. Configure the **enterprise name**. You can set the font weight and font size, and select a suitable display style.

4. Configure the **username and password** tip. Enter a placeholder tip in each of the fields next to **Username and Password**:

   - Enter a username placeholder. Example: Enter a username, a mobile phone number, or an email address.

   - Enter a password placeholder. Example: Enter a password.

   - You can configure a font style for the texts, such as the font weight and font size.

5. **Insert a custom URL**. The custom link is displayed at the specified location on the login page to redirect users to an external page.

   - **Link Name**: the text that you want to display as the URL. For example, you can enter Help Center or Forgot Password.

   - **Link URL**: Enter a complete URL. The URL must start with https://.

**Terms of service**

![](assets/3636fd0180b1e69a5809e587bdf5f40d.jpeg)

1. Go to the **Login Page Configuration** tab.

   Click **Branding** in the left-side navigation pane and find the brand that you want to manage. On the Branding page, find the brand that you want to configure and click **Configure** in the **Login Page Configuration** section.

2. Select the terms of service that you want to display.

   In the **Custom Privacy Policy** section, select a term of service from the **Select Policy** drop-down list. If the drop-down list is empty, click **Custom Privacy Policy** to add a term.

3. Publish the configurations.

   Click **Save and Publish** at the bottom of the page to immediately apply the configurations.

**Default redirect**

![](assets/e9a93a60af8d56a470b8ebc1ae93183d.jpeg)

1. Go to the **Login Page Configuration** tab.

   Click **Branding** in the left-side navigation pane and find the brand that you want to manage. On the Branding page, find the brand that you want to configure and click **Configure** in the **Login Page Configuration** section.

2. Select the default application to which you want to redirect users.

   <ol type="i">

   <li>

   Click the Search icon on the right of the **Default Redirection Application** field.

   </li>

   <li>

   In the list that appears, select the application that you want to use as the default redirect

   </li>

   </ol>

   destination, such as MyApp and IDaaS Application Portal.

3. Save the configurations.

   Click **Save** in the lower-left corner to save the configurations.

<a id="section-7-2"></a>

## 7.2. Custom terms

**Overview**

The custom term feature allows you to display terms, such as terms of service and privacy policy, on the login page of Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). When a user is logged in, the user is considered to have agreed to the relevant terms. This feature helps you meet the enterprise compliance requirements.

**Preparations**

We recommend that you prepare the following items before you configure custom terms.

| Item | Description |
| --- | --- |
| Terms | You need to prepare a reminder for terms and one or more links to the terms that users must agree to. |
| An IDaaS instance | You can use the custom term capability only after you create an IDaaS instance. |

**Enable the custom term feature**

Log in to the IDaaS console. On the page that appears, click Console in the Actions column of the desired instance. In the left-side navigation pane, click **Branding** and click the **Custom Privacy Policy** tab. Then, you can enable the custom term feature.

![](assets/8e839f75a0ea319201eb183d7c27c243.png)

Enter a reminder and one or more names and links for the terms. Then, click **Confirm**.

![](assets/8c57403e04f87e08ddedb68c6e9087e5.png)

After custom terms are added, the terms are displayed on the login page of IDaaS EIAM. If a user is logged in, the user is considered to have agreed to the terms.

![](assets/ebecabed6a25de6724b4bbeff4f845ba.jpeg)

**View terms and revoke acceptance of terms**

After a user is logged in, the user can view the accepted terms on the My Account page of IDaaS Application Portal. A user can revoke acceptance of terms. After the user revokes acceptance of the terms, the user immediately logs off from IDaaS EIAM.

> **Note**
>
> IDaaS EIAM manages only the acceptance of terms and the revocation of acceptance of terms. If you want to clear the relevant data, such as the mobile number and email of a user, after the user revokes acceptance of terms, you can check the audit logs and clear the data as an administrator.

**View the audit logs of terms**

After a user revokes acceptance of terms, the administrator can view the revocation record on the User tab of the Log page of the IDaaS instance.

<a id="section-7-3"></a>

## 7.3. SMS gateway

After an SMS gateway is configured in IDaaS, user-specific operations trigger the sending of SMS messages to implement secure, efficient, and compliant authentication and notification features. This topic describes how to configure an SMS gateway.

**Supported channel service providers**

| Supported channel service provider | SMS sending scope |
| --- | --- |
| Alibaba Cloud SMS(to Chinese Mainland) | Chinese mainland |
| Alibaba Cloud SMS(to regions outside Chinese Mainland) | Outside the Chinese mainland |

**Usage notes**

If a username in a message to be sent contains a period symbol (.), the system automatically replaces the period (.) with an asterisk (\*) for security reasons.

**Step 1: Add an SMS gateway**

1. In the left-side navigation pane, click **Branding**. On the page that appears, click the **SMS Gateway** tab.

2. Click **Add SMS Gateway**. In the dialog box that appears, enter a gateway name, and then click **Confirm**.

   image

**Step 2: Configure channel management**

1. Find the gateway that you want to manage and click **Edit** in the **Actions** column.

2. In the panel that appears, click **Create**. In the **Create Channel** dialog box, configure the following parameters and click **Confirm**.

   | Parameter | Description |
   | --- | --- |
   | Channel Name | The name of the channel. |
   | Channel Service Provider | Valid values: <strong>Alibaba Cloud SMS(to Chinese Mainland)</strong> and <strong>Alibaba</strong> <strong>Cloud SMS(to regions outside Chinese Mainland)</strong>.<br>Important<br>• This parameter cannot be modified after submission. Proceed with caution<br>• If you have users in the Chinese mainland and outside the Chinese mainland, you need to configure the two channels. |
   | Scope | This parameter is used to distinguish channels for sending SMS messages. |

3. Configure the parameters for the channel. In this example, the **Channel Service Provider** parameter is set to **Alibaba Cloud SMS(to Chinese Mainland)**.

   > **Note**
   >
   > If you set the **Channel Service Provider** parameter to **Alibaba Cloud SMS(to regions outside Chinese Mainland)**, pay attention to the following configuration differences:
   >
   > - On the **Channel Configuration** tab, you do not need to configure the signature, but you need to configure **SenderID**. **SenderID** must be consistent with the configuration in the SMS gateway. Otherwise, messages fail to be sent.
   >
   > - You do not need to configure data on the **Gateway Template** tab.

   <ol type="i">

   <li>

   On the **Channel Configuration** tab, configure the following parameters.

   | Parameter | Description |
   | --- | --- |
   | Enable | Specifies whether to enable the channel. |
   | AccessKey ID | The AccessKey ID of the SMS service provider, which is used to identify a user. |
   | AccessKey Secret | The AccessKey secret of the SMS service provider, which is used to verify the identity of a user. |
   | SMS Endpoint | The SMS endpoint. Example: example.aliyuncs.com. |
   | Signature | The signature that has been filed in the SMS gateway. |
   | Network Access Endpoint | Important<br>If a paid instance is released upon expiration or unsubscribed, IDaaS EIAM automatically deletes the related dedicated endpoint. If you need to use a public endpoint or another dedicated endpoint, you must switch the endpoint.<br>If an IDaaS instance uses a dedicated endpoint, the IDaaS instance is provided with a dedicated and custom private outbound IP address and a public outbound IP address. |

   We recommend that you click **Send a text message to the test mobile number** to conduct a test before you click **Save**.

   </li>

   <li>

   On the **Gateway Template** tab, configure the parameters.

   </li>

   </ol>

   Configure the **Text Message Language** and **Template Code** parameters for your SMS scenario. The following SMS scenarios are supported: OTP via SMS, OTP via SMS (2FA), Phone-Number Change Verification, Authentication via SMS, Initialize Password, and Password Reset by Administrator.

   - **Text Message Language**: **Simplified Chinese (zh-Hans-CN)** and **English (en-US)** are supported.

   - **Template Code**: the unique identifier of the SMS template that is approved by the SMS service provider.

<a id="section-7-4"></a>

## 7.4. Email gateways

This topic describes how to configure and use a custom email gateway.

**Overview**

Identity as a Service (IDaaS) allows you to add custom email gateways to your instance. This way, you can configure email templates in different languages and send email notifications that contain enterprise brand information to users.

**Terms**

| Term | Description |
| --- | --- |
| initial email gateway | The email gateway that is built in your IDaaS instance. You cannot modify the configurations of this email gateway. |
| custom email gateway | The email gateway that you add to your IDaaS instance. To add a custom gateway, activate an email gateway service such as Alibaba Cloud Direct Mail. |
| default email gateway | The email gateway that is used by your IDaaS instance to send email notifications to users. The default email gateway can be the initial email gateway or a custom email gateway. |

**Preparations**

To facilitate the configuration process, we recommend that you make the following preparations before you configure a custom email gateway.

| Item | Description |
| --- | --- |
| Email gateway | You need to activate an email gateway service such as Alibaba Cloud Direct Mail to send emails to users. In addition, you need to create an email domain name and sender address in advance for sending emails. |
| Create an instance | Create an IDaaS instance. |

**Add a custom email gateway**

Log in to the IDaaS console. On the page that appears, click Console in the Actions column of the desired instance. In the left-side navigation pane, click **Branding**. On the Branding page, click the **Email Template** tab. On the tab, click **Add Custom Email Gateway**.

![](assets/98805ef189c512757b52bb4a9fbff1f5.png)

In the Add Custom Email Gateway panel, specify the information of the custom email gateway. Some information must be obtained from your email gateway service.

- Gateway Service Provider: the email protocol. Set the value to SMTP. Simple Mail Transfer Protocol (SMTP) is a commonly used protocol for sending emails.

- Display Name: the name of the email gateway, which is displayed only in the IDaaS console.

- SMTP Endpoint: the endpoint of the SMTP service, which is obtained from your email gateway service. In most cases, the value is a domain name. For example, the SMTP endpoint of Alibaba Cloud Direct Mail is xxxx.aliyun.com.

- Port Number: the port number of the SMTP service, which is obtained from your email gateway service. Commonly used ports include 25, 80, and 465. Port 465 uses SSL for encrypted communication. Obtain the port number from your email gateway service.

- Enable SSL Encryption: specifies whether to enable SSL encryption. If you enable SSL encryption, connection security is improved. To enable SSL encryption, you must specify a dedicated port number.

- SMTP Account and SMTP Password: the account and password that are used to access your SMTP email gateway. Typically, the account is the email address prefix or email address of the sender.

- Sender Email Address: the email address of the sender. Example: xxxx@example.com.

- Sender Name: the name of the sender, which can be the name of your enterprise or brand. This parameter is optional. If you do not configure this parameter, the email prefix of the sender is used.

![](assets/6af8074b86a36e8665d28a58fe9cf4c0.png)

Click **Test Sending**. In the dialog box that appears, enter the email address of the recipient and click **Confirm** to send a test email.

![](assets/f7fb522334022134f9e4882ca2b1793c.jpeg)

If the test email is successfully sent, the configurations of the custom email gateway are valid.

![](assets/dea8808b217a0cce2e3b808467c0d530.jpeg)

Click **Confirm**. The custom email gateway is added.

![](assets/6e1fa0b2fd0971e6e09bc8deb93846f6.png)

> **Important**
>
> If the status of the custom email gateway is Available, the email gateway features of the instance are ready for use. However, this does not mean that the custom email gateway can send emails. You must check whether the custom email gateway can properly work.

**Manage a custom email gateway**

Click **Manage** in the Actions column of the custom email gateway to go to the management page.

On the **Gateway Configuration** tab, you can modify the configuration of the custom email gateway, such as the endpoint of the SMTP service.

On the **Email Template** tab, you can configure the email language, subject, and content for each scenario.

- Email Language: the language of the email. The email subject and content in each scenario can be displayed in various languages. This enables an instance to send email notifications in different languages to users. Currently, only Chinese and English are supported. To use other languages, submit a ticket.

- Email Theme: the title of the email.

- Email Content: the content of the email. You can configure only the content but not the style of the email.

![](assets/eb6e8801e76ce6ce4c5cff97ecb2f6dc.png)

**Change the default email gateway**

After you specify an email gateway as the default email gateway, IDaaS sends emails to users through this email gateway.

![](assets/34036cb4e22f1f884fb7ad24b89c70f3.png)

> **Important**
>
> If you specify a custom email gateway as the default email gateway and the custom email gateway becomes unavailable due to reasons such as instance expiration, IDaaS automatically switches to the initial email gateway.

**Remove a custom email gateway**

IDaaS allows you to remove custom email gateways. After you remove a gateway, the configuration of the gateway is cleared and cannot be restored.

<a id="section-8"></a>

# 8.Other configurations

<a id="section-8-1"></a>

## 8.1. Network endpoints

Network endpoints implement network access for Identity as a Service (IDaaS) instances. This topic describes endpoints and how to configure and use endpoints in IDaaS.

**Dedicated endpoints of IDaaS**

A dedicated endpoint is an exclusive endpoint for an Employee Identity and Access Management (EIAM) instance. The dedicated endpoint of an EIAM instance is an elastic network interface (ENI) of a virtual private cloud (VPC). You can configure security group rules or network settings for the ENI. This way, the EIAM instance can access a private network or access the Internet by using the dedicated endpoint.

- **Dedicated access to a private network**

  After an IDaaS instance connects to your Apsara Stack VPC over a private network, you can synchronize the data of Active Directory (AD) domains, Lightweight Directory Access Protocol (LDAP) servers, and applications, and enable the AD authentication and LDAP authentication features, without the need to enable Internet-facing ports. The following sections describe network access in different scenarios. In the following examples, an AD domain server is used.

  <table>
    <tr>
      <td>The AD domain server and ENI belong to the same Apsara Stack VPC</td>
      <td></td>
      <td>If your AD domain server and the ENI of your EIAM instance belong to the same Apsara Stack VPC, you must implement access control by using the following method:<br>Configure the security group to which the AD domain server belongs to allow access from the IP address of the ENI.</td>
    </tr>
    <tr>
      <td>The AD domain server and ENI belong to different Apsara Stack VPCs</td>
      <td></td>
      <td>If your AD domain server and the ENI of your EIAM instance belong to different Apsara Stack VPCs, you must implement access control by using the following methods:<br>• Connect the two Apsara Stack VPCs by using a Cloud Enterprise Network (CEN) instance.<br>• Configure the security group to which the AD domain server belongs to allow access from the IP address of the ENI.</td>
    </tr>
    <tr>
      <td>The AD domain server belongs to a data center or a third-party cloud service provider</td>
      <td></td>
      <td>If the AD domain server belongs to a data center or a third-party cloud service platform, you must implement access control by using the following methods:<br>• Connect the Apsara Stack VPC to the data center or cloud service platform to which the AD domain server belongs by using a leased line, such as a VPN gateway.<br>• Configure the firewall of the AD domain server to allow access from the IP address of the ENI.</td>
    </tr>
  </table>

- **Dedicated access to the Internet**

  After an EIAM instance connects to your Apsara Stack VPC over a private network, you can associate an Elastic IP Address (EIP) with the ENI of the EIAM instance or associate an Internet NAT gateway with your Apsara Stack VPC. This way, the EIAM instance can use a public IP address to access the Internet. You can specify the public IP address as the trusted IP address in WeCom to meet your requirements for WeCom access.

<a id="section-8-2"></a>

## 8.2. Network scopes

This topic introduces network scopes and describes how to configure network scopes.

**Overview**

You can use the network scope feature to dynamically adjust the IP addresses of certain features, such as conditional access, without the need to modify other configurations.

**Add a network scope**

Log in to the Identity as a Service (IDaaS) console and choose **Branding > CIDR Block > Add CIDR Block**.

Only the classic network is supported. You can add IPv4 and IPv6 addresses or CIDR blocks. You must enter at least one IPv4 or IPv6 address or CIDR block.

![](assets/a3fd704ec13bae538b7b17f351073030.png)

**Delete a network scope**

> **Important**
>
> You can delete a network scope that is no longer required. You cannot restore the network scope after you delete it. When you delete a network scope, the system checks whether it is in use. If the network scope is in use, you cannot delete it.

![](assets/694e2a00d11f292b9499ec6a6541ed75.png)

<a id="section-9"></a>

# 9.Use Cases

<a id="section-9-1"></a>

## 9.1. Synchronize AD domain data to DingTalk

This topic describes how to automatically synchronize identity data from an Active Directory (AD) domain to DingTalk.

IDaaS can fully synchronize identity data from AD to DingTalk: **When the user or organization data of AD changes, the DingTalk contact data automatically updates.** With this capability, enterprises can use AD as a traditional identity control source and automatically synchronize identity data to DingTalk and other downstream applications. Changes are synchronized among all identity management systems.

1. **Create an IDaaS instance**

1. Log in to the Apsara Uni-manager Management Console.   In the top navigation bar, choose Security > Identity and O&M Security > IDaaS to go to the IDaaS console.

   ![](assets/6eb8f2a07988f17a7d204e9731f74ada.png)

2. Click Create Instance, enter an instance name, specify resource configurations, and then click Create.

   ![](assets/7cc65b226b77d626e11eec796edef0c8.jpeg)

   2. **Synchronize account data from AD to IDaaS**

**Step 1: Bind IDaaS to AD**

1. Find the IDaaS instance and click Console in the Actions column.

2. On the Quick Start page, click Bind AD.

3. In the Connect To AD panel, enter the AD domain information.

   - **Display Name**: the name that is displayed to a user when the user logs in to and uses IDaaS.

   - **Server Address**: the address of the server where AD resides. In most cases, AD uses 127.0.0.1:389 and port 389. Port 636 is used if LDAPS or StartTLS is enabled.

   - **LDAPS/StartTLS**: specifies whether to enable StartTLS. We recommend that you enable LDAPS or StartTLS to improve connection security. For more information about how to enable LDAPS or StartTLS, see  `AD security configuration` .

   - **Outbound IP**: If you want only IDaaS to request the AD server, add the IP address of IDaaS to the IP whitelist of the AD on the server.

   - **Administrator Account**: the AD administrator account used by IDaaS to read AD information for data synchronization or delegated authentication. The account must have at least read permissions. Enter the value in the User Principal Name (UPN) format such as example@example.com, or the Distinguished Name (DN) format such as cn=admin, ou=technical department, dc=example, dc=com.

   - **Administrator Password**: the logon password of the administrator account.

**Step 2: Select a scenario**

In this step, configure the features that you want to use.

- **Synchronization Direction**: The data of the AD user or organization selected as the synchronization source is imported to the IDaaS destination node. **Source Node**: Enter the DN of the AD node as the source node. In most cases, the DN of the AD root node is dc=example, dc=com (your domain). **If ou in the source is AD_Test-0730, enter ou=AD_Test-0730,dc=idsmanager,dc=cn.**

- **Incremental Synchronization**: IDaaS listens to the data of AD users or organizations, and synchronizes data updates from AD to IDaaS every 10 minutes.

  - You can configure mapping identifiers in the Field Mapping step of an IDaaS account to a field of an AD user. For example, you can match the Mobile Phone Number field of an IDaaS account against the Mobile Phone Number field of an AD user. If the matching is successful and the AD user is updated, the IDaaS account is also updated from the AD user. If the matching fails, an IDaaS account is created by using the information about the AD user.

  - When incremental synchronization is performed for the first time, full data synchronization is automatically performed.

  - Failure to import a single data entry does not affect the import of other data entries.

  - You can view the failure information in the synchronization log.

  - You must enable AD Recycle Bin to receive messages about deletion events in AD. For more information about how to enable this feature, see  `Incremental synchronization` .

- **Delegated Authentication**: If this feature is enabled, a user can log in to IDaaS by using an AD username and password.

- **Automatic Password Update**: When a user attempts to log in to IDaaS by using AD delegated authentication, if the password of the IDaaS account is empty, the password is automatically updated to the password of the AD user. The AD password must meet the requirements specified in the password policies of IDaaS. Otherwise, the IDaaS password cannot be automatically updated to the AD password.

Advanced settings

- **User/Organization ObjectClass**: You can use ObjectClass to define a type of object as a user or organization. For example, the object whose ObjectClass is user in the query result is considered a user. In most cases, no modification is required.

- **User Sign-in ID**: When a user attempts to log in to IDaaS by using AD delegated authentication, IDaaS uses the attributes to query the user in AD and matches the password. If the password is correct, the user is allowed to log in to IDaaS. You can separate multiple attributes with commas (,). In this case, these attributes are in the OR relationship. This indicates that the user can use one of the attributes to log in to IDaaS. Make sure that multiple attributes correspond to the same AD user. Otherwise, the user cannot log in to IDaaS.

**Step 3: Configure field mapping**

You can configure field mappings to use specific fields of an IDaaS account as the fields of an AD user. For example, if you want to use the name of an IDaaS account as the mobile phone number of an AD user, you must configure a field mapping.

If you confirm that the configuration of field mapping is correct, select Save and Push. In this case, all AD data selected in Step 3 is synchronized to IDaaS. If you are not sure whether the configuration of field mapping is correct, select Save Only. You can modify the configuration in Modify Settings > Field Mapping of this identity provider later.

**Step 4: Start the synchronization**

In Step 4, click Save and Push, or select Save Only and then click Push/Pull Now on the IdPs page.

After the synchronization is completed, you can view the synchronized accounts on the Account tab.

3. **Synchronize data from IDaaS to DingTalk**

**Step 1: Bind IDaaS to DingTalk**

In the left-side navigation pane, click Quick Start or IdPs. On the page that appears, click Bind DingTalk, and select Outbound from the drop-down list.

**Step 2: Create an application**

In the Create Application step, configure the following parameters.

- **Display Name**: the name that is displayed to a user when the user logs in to and uses IDaaS.

- **CorpId**: You can obtain the ID on the Home tab of DingTalk Platform.

- **AppKey/AppSecret**

  Create an application on the DingTalk Open Platform - In-house Enterprise Development page.

  Obtain the **AppKey/AppSecret** on the application details page.

  Configure the **callback domain name** and **application homepage URL** in DingTalk.

- **Callback Domain**: Enter the URL in **Logon and Sharing - Callback Domain** on the application details page. You must configure this parameter before you can log in to IDaaS by scanning a QR code with DingTalk.

- **Application Homepage URL**: Enter the URL in **Logon and Sharing - Callback Domain** on the application details page. After you configure this parameter, when a user clicks the application in the DingTalk console, the user can log in to the IDaaS application by using single sign-on (SSO). You can set Privacy Level for the application in Version Management and Publishing.

- If you want only IDaaS to request DingTalk, enter the following server IP addresses in the IP Address field in the Development Information section: 112.124.239.96, 112.124.239.101, 112.124.XXX.XXX, 112.124.XXX.XX, 112.124.XXX.XX, 112.124.XXX.XX, 112.124.XXX.XXX, 112.124.XXX.XXX, 112.124.XXX.XXX, and 112.124.239.10.

**Step 3 Grant permissions**

On DingTalk Open Platform - In-house Enterprise Development, go to the application details page. On the Permissions page, grant all permissions on contacts and application management, and set the authorization scope to all employees.

After you grant permissions, click Next in IDaaS. IDaaS verifies whether the application has the permissions to manage DingTalk Contacts. If yes, the configuration is complete.

**Step 4: Select a scenario**

In this step, configure the features that you want DingTalk to support.

- **Synchronization Direction**: The data of the IDaaS account or organization selected as the source node is imported to the DingTalk destination node. Set the destination node to the ID of the DingTalk department. The department ID is displayed when you edit the department in the DingTalk Admin Console. The default ID of the DingTalk root department is 1.

- **Incremental Synchronization**: If this feature is enabled, all data updates of the IDaaS account or organization are synchronized to DingTalk Contacts in real time. When an IDaaS account is exported to DingTalk, IDaaS matches the account to the DingTalk user based on the mapping identifiers specified in the "Configure field mapping" step. You can define the mapping rules in Field Mapping. If the matching is successful, the existing IDaaS account is updated. Otherwise, an IDaaS account is created.

- **Sign-In with QR Code**: If this feature is selected, the DingTalk QR Code Login option is provided and enabled in the Login menu. Users can log in to IDaaS by scanning the provided QR code with DingTalk.

> **Note**
>
> We recommend that you test the synchronization by using the data of a small number of accounts or in a non-production environment. This prevents the data of DingTalk from being affected by improper configuration.

**Step 5: Configure field mapping**

You can configure field mapping to bind the accounts or organizations in IDaaS to the DingTalk users or departments. You can also use some data of an IDaaS account as the data of a DingTalk user. For example, you can use the display name of an IDaaS account as the name of the DingTalk user.

By default, IDaaS allows you to customize field values such as the DingTalk name, mobile number, email address, title, and employee number. You can add other fields, such as workplace, based on your business requirements.

- **Field Name**: This parameter is displayed only in IDaaS.

- **Field Identifier**: You must use a DingTalk field name which is unique for the current identity provider. In the preceding figure, the field identifier of workplace is work_place.

If you confirm that the configuration of field mapping is correct, select Save and Push. In this case, all IDaaS data selected in Step 3 is synchronized to DingTalk. If you are not sure whether the configuration of field mapping is correct, select Save Only. You can modify the configuration in Modify Configuration > Field Mapping of this identity provider later.

After data is synchronized, if an employee has not joined the DingTalk enterprise, a user synchronization error may be reported. To solve this issue, invite the user to the DingTalk organization.

**Note:**

- **If you want to use an IDaaS account to log in to a DingTalk Enterprise account, the userid of the DingTalk user must be the same as the userid of the IDaaS account.**

- **If the mobile phone number of the user is not associated with their DingTalk account, a text message is sent, as shown in the following figure.**

<a id="section-9-2"></a>

## 9.2. Log in to applications from DingTalk through SSO

This topic describes how to integrate applications in Identity as a Service (IDaaS) with the DingTalk console to implement application Single Sign-On (SSO).

**Scenarios**

IDaaS supports standard authentication protocols such as Security Assertion Markup Language (SAML) and OpenID Connect (OIDC), allowing users to quickly log in to hundreds of applications through SSO. This topic describes how to integrate an IDaaS application with the DingTalk console. The application is already configured with SSO. This way, users can log in to the application through SSO.

**Procedure**

**Step 1: Create a DingTalk IdP**

Before you start, you need to create a DingTalk identity provider (IdP) to map account data in IDaaS to user data in DingTalk. To do this, you can use the following methods:

- Synchronize account data from DingTalk to IDaaS. For more information, see Connect to a DingTalk first-party application.

- Synchronize data from IDaaS to DingTalk. For more information, see Synchronize data from IDaaS to DingTalk.

We recommend that you specify QR code-based login as the default login method of DingTalk. After a user clicks an application in the DingTalk console, the user is automatically logged in. Otherwise, users need to manually switch from the IDaaS login page to the DingTalk login page or log in to IDaaS before they can automatically log in to applications in the DingTalk console.

**Step 2: Create an application in IDaaS**

Add an application in IDaaS and configure SSO for the application. In this topic, Apsara Stack user-based SSO is used.

**Step 3: Grant permissions to access the application**

Grant accounts the permissions to access the application. You can select All Users or Manually for the Authorize parameter on the **SSO** tab. If you select Manually for the Authorize parameter, you must grant permissions by account or organization on the **Authorize** tab. An account can access the application only after the account is granted the required permissions.

If you added an SAML application such as Resource Access Management (RAM), you can configure the **Application User** parameter on the **SSO** tab. When a user sends an SSO request to the application, IDaaS passes the username of the IDaaS account or the username of the application account to the application. Then, the application uses the username to match the corresponding account for SSO. Therefore, if the application has existing accounts, we recommend that you check whether the accounts are mapped to the accounts in IDaaS. If the accounts are not mapped, we recommend that you create accounts in the application in advance.

**Step 4: Generate the application endpoint**

Generate the endpoint of the application in the following format: https://{IDaaS user portal address}/login/go/{IDaaS application ID}

You can obtain the IDaaS user portal address from the  `instance list`  in the IDaaS console, as shown in the following figure.

You can obtain the ID of the application from the **Application** page of the instance in the IDaaS console, as shown in the following figure.

The generated endpoint is as follows:

https://bm6sxxxx.aliyunidaas.com/login/go/app_mmhsgpkmsxxxxxxxxxxxxxxxx

**Step 5: Create an application in DingTalk**

Go to DingTalk Open Platform and find **Enterprise Internal Applications** below **Application Development**.

Specify the basic information of the application. This topic takes Alibaba Cloud as an example.

Specify the endpoint of the application generated in Step 2 on the **Development Management** page of the DingTalk application, as shown in the following figure. The PC address is optional. Users can log in to the application in the DingTalk PC console only after the PC address is specified.

**Step 6: Grant permissions to access the DingTalk application**

After you test the DingTalk application, release the application.

After the application is released, you can set the visibility scope of the application. You can authorize all employees, specific employees, or only administrators to access the application. The **Specific Employees** option allows you to grant access permissions by user, organization, or role.

After you grant permissions, administrators can set an application portal for specific employees or all employees. Employees can also add their portals in the console. After a user clicks the icon of the application in the DingTalk console, the user is automatically logged in.

During the auto login process, IDaaS finds the corresponding IDaaS account based on the DingTalk account of the user, and then matches it with the application account. This way, the user is able to log in to the application through SSO.

<a id="section-9-3"></a>

## 9.3. Use an AD or OpenLDAP account to log in to a third-party application

This topic describes how to use Identity as a Service (IDaaS) to log in to a third-party application by using an Active Directory (AD) account.

**Scenarios**

IDaaS supports data synchronization with AD domains and delegated authentication. This allows you to log in to hundreds of applications by using an AD or OpenLDAP account.

To achieve the preceding goals, you must synchronize an AD account to IDaaS and add an application that supports single sign-on (SSO) to IDaaS<strong>.</strong> This configuration allows your enterprise account to log in to a third-party application by using an AD account.

> **Note**
>
> This topic describes a scenario in which Apsara Stack user-based SSO is the third-party application. All IDaaS features that are used are provided free of charge.
>
> In actual scenarios, whether a feature is free of charge depends on whether the third-party application template is free of charge.

**Procedure**

**Step 1. Create an IDaaS instance**

Before you configure an application, you must create an IDaaS instance.

**Step 2. Synchronize an AD account to IDaaS**

To implement login by using an AD account or an OpenLDAP account, you must first synchronize the account to IDaaS. In this topic, an AD account is used. You can synchronize other accounts based on your business requirements.

For more information about how to synchronize an AD account to IDaaS, see Connect IDaaS to AD.

For more information about how to synchronize an OpenLDAP account to IDaaS, see Connect IDaaS to OpenLDAP.

> **Important**
>
> Make sure that Delegated Authentication is turned on.

After the synchronization is complete, you can view the synchronized account on the Accounts page.

**Step 3: Add an application in IDaaS**

Add an application in IDaaS and configure SSO for the application. In this topic, Apsara Stack user-based SSO is used.

For more information about how to configure and use Apsara Stack user-based SSO, see Apsara Stack user-based SSO.

> **Note**
>
> When you associate a Resource Access Management (RAM) user, specify the username of the AD account that is synchronized to IDaaS as the username of the IDaaS account, and use the username of the RAM user as the username of the application account.

**Step 4: Grant application permissions**

Grant accounts the permissions to access the application. You can select All Users or Manually for the Authorize parameter on the **SSO** tab. If you select Manually for the Authorize parameter, you must grant permissions by account or organization on the **Authorize** tab. An account can access the application only after the account is granted access permissions.

If you added an SAML application such as Resource Access Management (RAM), you can configure the Application User parameter on the SSO tab. IDaaS passes the username of the IDaaS account or the username of the application account to the application. Then, the application uses the username to match the corresponding account for login. If existing accounts are available, make sure that they correspond to IDaaS accounts. If they do not correspond to IDaaS accounts, you must create accounts in the application in advance.

**Step 5. Configure a login method**

1. In the IDaaS console, click **Sign-In**.

2. Enable AD delegated authentication.

3. Optional. Configure the default login method.

   If you want to designate an AD account as the default login method, set the Primary Authentication Method parameter to AD Account Login.

**Step 6: Initiate SSO**

**Service provider-initiated (SP-initiated) SSO**

1. Go to the RAM user login page, enter the username of your RAM user, and then click **Next**.

2. Click **Login with Organization Account**. You are redirected to the login page of IDaaS.

3. If you designate an AD account as the default login method, enter the corresponding username and password. Otherwise, click the AD icon.

**Identity provider-initiated (IdP-initiated) SSO**

1. Access the IDaaS user portal.

2. If you designate an AD account as the default login method, enter the corresponding username and password. Otherwise, click the AD icon.

3. In the IDaaS application portal, click the application icon to log in to the application.

<a id="section-9-4"></a>

## 9.4. Use AD, LDAP, or IDaaS accounts to log in to DingTalk Enterprise

This topic describes how to use Identity as a Service (IDaaS) to synchronize account data and organization data from Active Directory (AD) or a Lightweight Directory Access Protocol (LDAP) service to DingTalk Enterprise and use the AD, LDAP, or IDaaS account to log in to DingTalk Enterprise.

**Scenarios**

If you are a user of DingTalk Enterprise, IDaaS Employee Identity and Access Management (EIAM) of Alibaba Cloud provides standard features for the following scenarios:

- Data synchronization: synchronizes account data and organization data such as AD and LDAP accounts to the DingTalk Enterprise, and automatically changes the DingTalk contacts to maintain consistency between upstream and downstream data.

- Single sign-on (SSO): allows users to log in to DingTalk Enterprise by using AD, LDAP, or IDaaS accounts. To implement this feature, you need to activate the dedicated account module for DingTalk Enterprise.

- Login-free for applications: implements login-free for DingTalk by integrating IDaaS-supported applications with the DingTalk console.

In addition, the private deployment of IDaaS EIAM supports in-depth integration with services and systems:

- In-depth integration with DingTalk Enterprise: allows you to integrate with the identity system with DingTalk Enterprise. For example, you can integrate with the login status, password, and role data of DingTalk Enterprise and implement Kerberos or API authentication.

- Complex identity management: If you use multiple identity systems, such as human resource (HR), office automation (OA), and identity and access management (IAM) systems, and require streamlining and governance, IDaaS EIAM helps you manage these complex identities.

- Other scenarios: IDaaS EIAM also supports custom service capabilities, fully delivered services, deployment in a private network, and communication establishment within a private network by using zero-trust components.

**Workflow**

When you use an AD, LDAP, or IDaaS account to log in to DingTalk Enterprise, DingTalk Enterprise serves as an application in IDaaS. The IDaaS account is used to log in to DingTalk Enterprise. Therefore, you can use the authentication capabilities of IDaaS, including multiple login methods, two-factor authentication (2FA), password policies, and login pages. The following figure shows how an AD user logs in to DingTalk Enterprise.

**Administrator configuration procedure**

The following procedure is applicable to Alibaba Cloud IDaaS EIAM.

Before you start, you must create an IDaaS instance.

**Step 1: Synchronize existing identity data to IDaaS**

If your identity provider (IdP) uses a standard protocol supported by IDaaS, you can synchronize upstream identity data with IDaaS identity data after simple configurations.

- For more information about how to synchronize account data from AD to IDaaS, see Connect IDaaS to AD.

- For more information about how to synchronize account data from OpenLDAP to IDaaS, see Connect IDaaS to OpenLDAP.

If you use an HR, OA, IAM, or self-managed application, you can select different solutions as appropriate.

- If you want to develop and implement your application independently, you can connect to the Developer API of the IDaaS application and import identity data to IDaaS.

- If you want the IDaaS team to handle the deployment, two private deployment solutions are available:

  - Private deployment of the synchronization component: If you have a single identity system, use the IDaaS synchronization component Connector. After this component is deployed in your private network, you can synchronize data to IDaaS.

  - Private deployment of IDaaS: If your identity system is complex and requires streamlining and governance, choose private deployment of IDaaS. Private deployment of IDaaS supports in-depth, flexible integration with your system and custom features.

**Step 2: Synchronize IDaaS identity data to DingTalk Enterprise**

After IDaaS identity data is synchronized to DingTalk Enterprise, the upstream identity data, such as AD and LDAP data, of the enterprise can interact with the contact data of DingTalk Enterprise. Data update can be synchronized to both the upstream system and DingTalk Enterprise.

For more information about how to synchronize data from IDaaS to DingTalk, see Connect DingTalk to IDaaS-outbound direction.

When you connect DingTalk to IDaaS in the outbound direction, take note of the following DingTalk Enterprise configurations:

1. When you create a DingTalk application, select **DingTalk Enterprise**.

2. The  `userid`  field is used for login to DingTalk Enterprise. When you **map fields**, we recommend that you map the userid to the IDaaS userId or username field. For more information, see the "Create an application in IDaaS" step in this topic.

**Step 3: Create an application in IDaaS**

IDaaS is pre-integrated with DingTalk Enterprise. You can configure SSO for DingTalk Enterprise after simple configurations.

**Step 4: Configure a login method**

IDaaS supports various login methods, including AD, LDAP, IDaaS username and password, and IDaaS text message verification. In addition, IDaaS supports 2FA and password policies. For more information, see General settings, 2FA, and Password policies.

> **Note**
>
> The DingTalk login method is not displayed on the DingTalk mobile app.

If you want users to log in by using an AD or LDAP account, you can customize the settings of the AD or LDAP IdP. Configure the  `userPrincipalName` ,  `sAMAccountName` ,  `uid` , and  `mail`  field to specify the login username.

You can also personalize the IDaaS login page, which is displayed when users log in to DingTalk Enterprise. For more information, see Branding.

**User login procedure**

After the administrator completes the preceding steps, users can log in to DingTalk Enterprise by using their AD, LDAP, or IDaaS accounts. The login method is supported for the desktop client, mobile app, and web client of DingTalk Enterprise.

1. **Click Dedicate Account Login**

Open the desktop client of DingTalk Enterprise and click **Dedicated Account Login**.

2. **Enter the organization code**

Enter the organization code and click **Next** to go to the IDaaS login page. For more information about how to obtain the organization code, click the link below the button.

3. **Enter the account password**

On the IDaaS login page, enter the account password. The administrator can set the default login method. As shown in the following figure, the default login method is the AD account of the enterprise. You can also switch to another login method. Click **Log In**. You may need to complete 2FA in IDaaS.

4. **Bind a mobile phone number**

At your first login, you need to bind your mobile phone number to DingTalk Enterprise. Then, you can log in to DingTalk Enterprise and use its features.

<a id="section-9-5"></a>

## 9.5. Use Alibaba Cloud IDaaS to synchronize account data from DingTalk, WeCom, Feishu, AD, and other IdPs to Alibaba Cloud RAM

Alibaba Cloud Identity as a Service (IDaaS) supports data synchronization by using the System for Cross-domain Identity Management (SCIM) protocol. You can use IDaaS to synchronize existing enterprise account data from sources such as DingTalk, Feishu, and Active Directory (AD) to Alibaba Cloud Resource Access Management (RAM). For more information, see IdPs. This topic describes how to synchronize account data from AD to RAM by using the SCIM protocol. You can refer to this topic to synchronize account data from other identity providers (IdPs).

1. **Create an IDaaS instance**

1. Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose Security > Identity and O&M Security > IDaaS to go to the IDaaS console.

   ![](assets/6eb8f2a07988f17a7d204e9731f74ada.png)

2. On the page that appears, click Create Instance. In the Create Instance panel that appears, configure the Instance ID/Description, Users, Applications, and Authentications parameters, and click OK to create an IDaaS instance.

   ![](assets/7cc65b226b77d626e11eec796edef0c8.jpeg)

   2. **Synchronize account data from AD to IDaaS**

In the example, IDaaS is connected to AD. You can connect IDaaS to other IdPs based on your business requirements.

- For more information about how to synchronize account data from DingTalk to IDaaS, see Connect IDaaS to DingTalk first-party application.

- For more information about how to synchronize account data from WeCom to IDaaS, see Connect WeCom to IDaaS.

- For more information about how to synchronize account data from Feishu to IDaaS, see Connect IDaaS to Feishu.

- For more information about how to synchronize account data from AD to IDaaS, see Connect IDaaS to AD.

- For more information about how to synchronize account data from OpenLDAP to IDaaS, see Connect IDaaS to OpenLDAP.

- For more information about how to synchronize account data from international IdPs, such as Okta and Azure, to IDaaS, see Connect IDaaS to an OIDC IdP.

> **Note**
>
> If you want to use AD delegated authentication to implement login, you must turn on Delegated Authentication when you connect IDaaS to AD. For more information, see Use an AD or OpenLDAP account to log in to a third-party application.

After the synchronization is complete, you can view the synchronized accounts on the Accounts page.

3. **Synchronize account data from IDaaS to RAM**

After you synchronize accounts to IDaaS, you can synchronize the accounts to RAM by using the SCIM protocol.

**Step 1: Create an OAuth application in the RAM console**

Grant permissions to the OAuth application and create an application secret.

**Step 2: Configure SCIM synchronization in IDaaS**

**Step 3: Synchronize accounts**

After you click **Push Now**, the accounts within the specified synchronization scope are synchronized to RAM.

<a id="section-9-6"></a>

## 9.6. Synchronize accounts and groups to CloudSSO by using SCIM in Alibaba Cloud IDaaS

This topic describes how to synchronize accounts and groups to CloudSSO by using System for Cross-domain Identity Management (SCIM) in Alibaba Cloud Identity as a Service (IDaaS). This enables the automatic management of identities.

**Step 1: Enable SCIM synchronization in the CloudSSO console**

1. Log in to the  `CloudSSO console`  by using your Alibaba Cloud account.

2. In the left-side navigation pane, click **Settings**.

   ![](assets/fb4a4d65137b22ed3a8c4bc6ffbb3bc9.jpeg)

3. On the User Setting tab of the Settings page, turn on the switch in the **SCIM-based User Synchronization Configuration** section to enable SCIM synchronization.

   ![](assets/94e4cbfcca9e4d4b7385eedb3e3ed96d.jpeg)

4. Click Generate Key.

   The SCIM credential is displayed only once. Copy the SCIM credential and keep it confidential. The SCIM credential is the value of the Bearer Token Mode parameter in IDaaS.

![](assets/36429af31344cd98cbcf010e6b8d998e.jpeg)

**Step 2: Configure SCIM synchronization in IDaaS**

1. Log in to the IDaaS console. On the EIAM page, click the required instance. In the left-side navigation pane, click **Applications**. On the Applications page, click **Add Application** to go to the **Marketplace** tab. Then, search for **Alibaba CloudSSO** and click Add Application.

   ![](assets/9142e669e84d4e62620da697639dc0a3.jpeg)

2. Go to the Provisioning tab and turn on Provision IDaaS Accounts to Application.

   ![](assets/7ff3b2dedef6cfe0908bd291ac3ed8b3.jpeg)

3. Select a synchronization scope and click **Save**.

   ![](assets/7ef7a8b368875284c968616f3096cddd.jpeg)

4. Enter the key information.

   ![](assets/62fe61140588bc1fe4746ec1269cf487.png)

   **Bearer Token**: The value of this parameter is the SCIM credential that you copied in Step 1.

   > **Note**
   >
   > If you require more flexibility in the configuration, you can use a standard SCIM template. You can configure more parameters in a standard SCIM template.
   >
   > ![](assets/91fc6f1de5f3321eefac35988d5421c1.jpeg)

5. Configure the Operation and Field Mapping parameters.

   <ol type="i">

   <li>

   **Operation**: Administrators can subscribe to the change events that they want to follow to receive instant push notifications. When a change occurs on the accounts within the specified synchronization scope in IDaaS, IDaaS automatically synchronizes the change to the application.

   </li>

   <li>

   **Field Mapping**: This parameter displays the field mappings involved in SCIM-based synchronization. You can modify the field mappings based on your business requirements.

   </li>

   </ol>

   ![](assets/4367ee1ae6b63e1fd4208eb9e50e2aed.jpeg)

6. Test the connection.

   After you save the configuration, we recommend that you click **Test Connectivity** to check whether the configuration is valid.

   ![](assets/29c84c82502914ea7ba716642592bbee.jpeg)

   You can click **Push Now** to synchronize all accounts within the specified synchronization scope to CloudSSO based on your business requirements.

   ![](assets/5f573ac29e9675415775d014f10471f0.jpeg)

**Step 3: Synchronize accounts**

After you click **Push Now**, the accounts within the specified synchronization scope are synchronized to CloudSSO.

![](assets/7aca092fa6e9a1b7934525c3fdec4342.jpeg)

If the accounts in the specified synchronization scope are synchronized to CloudSSO, you can go to the **Log > Provisioning > Tasks** page to view synchronization logs.

![](assets/c1e8f0d260b26a89eb0c3102765554c9.png)

<a id="section-9-7"></a>

## 9.7. Synchronize accounts to RAM by using SCIM in Apsara Stack IDaaS

This topic describes how to synchronize accounts to Resource Access Management (RAM) by using System for Cross-domain Identity Management (SCIM) in Apsara Stack Identity as a Service (IDaaS). This enables automated management of identities.

**Prerequisites**

1. Your Apsara Stack tenant account or RAM user has permissions to create an OAuth application.

2. Your Apsara Stack tenant account or RAM user has permissions to authorize only server applications within the account.

**Step 1: Create and authorize an OAuth application in the RAM console**

1. Log in to the  `RAM console`  by using your Apsara Stack tenant account.

2. In the left-side navigation pane, choose **OAuth Preview > Enterprise Application > Create Application**.

3. Specify **Application Name** and **Display Name**. Set Application Type to **Server Application** and click **Create Application**.

4. Click the name of the application. On the **OAuth Scope** tab, click **Add OAuth Scope**. In the **Add OAuth Scope** dialog box, select /acs/scim and click **OK**.

5. Authorize the OAuth application. On the **OAuth Scope** tab, click **Authorize**. On the Authorize Application page, select **Cross-Domain Identity Management** and click **Authorize**.

6. On the **Application Secret** tab, click **Create Secret**. Then, the system automatically generates an application key pair, which consists of **AppSecretId** and **AppSecretValue**.

7. After the key pair is generated, click **Download Key** to download the key pair. Then, click **Close** to close the current page.

   > **Important**
   >
   > The key pair is displayed only on this page. After you close the page, you can no longer view the key pair again. Proceed with caution.

**Step 2: Configure SCIM synchronization in IDaaS**

1. Log in to the IDaaS console and click Console in the Actions column of the desired instance. In the left-side navigation pane, click **Application**. On the page that appears, click **Add Application** to go to the **Marketplace** tab. Then, search for **Alibaba Cloud User-Based SSO** and click **Add Application**.

2. Go to the **Provisioning** tab, specify the synchronization scope, and click **Save**.

3. Turn on **Provision IDaaS Accounts to Application**.

4. Configure basic parameters.

   <ol type="i">

   <li>

   Specify  `client_id`  and  `client_secret` **.**

   <ol type="a">

   <li>

   Log in to the  `RAM console` . In the left-side navigation pane, choose **Integrations > OAuth Preview**.

   </li>

   <li>

   Find the application that is used for SCIM synchronization and click its name to go to the details page.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   In the **Basic Information** section of the details page, you can view **Application ID, which is client_id**.

   </li>

   <li value="500">

   **AppSecretValue** displays the **client_secret** generated in Step 1.

   </li>

   </ol>

   </li>

   <li>

   Operation<strong>:</strong> Administrators can subscribe to specified change events, such as user

   </li>

   </ol>

   creation, update, and deletion. When a change occurs in IDaaS, the system automatically triggers synchronization and pushes the change to the destination application in real time.

   <ol type="i" start="3">

   <li>

   Full Scope: If you select this option, the corresponding data is pushed to the application

   </li>

   </ol>

   after you click Push Now.

5. Field Mapping<strong>:</strong> You can customize SCIM field mappings and modify attribute matching rules on demand. After you modify the mappings, click **Save** to ensure that data is accurately synchronized.

6. After you complete the configuration, click **Save**. We recommend that you click **Test Connectivity** to check whether the configuration is valid.

   You can click Push Now to synchronize all accounts within the specified synchronization scope to RAM based on your business requirements.

**Step 3: Synchronize data in IDaaS**

After you click **Push Now**, the accounts within the specified synchronization scope are synchronized to RAM.

![](assets/92681edef593fe7c81a2049230bc370b.jpeg)

<a id="section-9-8"></a>

## 9.8. Use IDaaS to log in to Apsara Stack DevOps from IdPs such as AD, DingTalk, and WeCom

This topic describes how to use Identity as a Service (IDaaS) to log in to Apsara Stack DevOps by using a user that belongs to an identity provider (IdP), such as DingTalk, WeCom, Lark, Active Directory (AD), OpenLDAP, Okta, or Microsoft Entra ID (formerly Azure AD).

**Overview**

IDaaS is a cloud-native, cost-effective, convenient, and standard identity and permission management system designed for enterprise users.

You can connect IDaaS to multiple upstream IdPs. This way, you can log in to a downstream application, such as Apsara Stack DevOps, by initiating single sign-on (SSO) as an IdP user and achieve the following synchronizations:

- **Data synchronization**: Synchronize data of the upstream IdP user to IDaaS and then from IDaaS to the downstream application.

- **Authentication synchronization**: Log in to IDaaS and then the downstream application by using the IdP user.

For more information about the IdPs supported by IDaaS, see IdPs.

**Examples**

**Access an application from the IDaaS application portal**

**Access the URL of Apsara Stack DevOps**

**Procedure**

**Step 1. Create an IDaaS instance**

1. Log in to the Apsara Uni-manager Management Console.   In the top navigation bar, choose Security > Identity and O&M Security > IDaaS to go to the IDaaS console.

   ![](assets/6eb8f2a07988f17a7d204e9731f74ada.png)

2. Click Create Instance, enter an instance name, specify resource configurations, and then click Create.

   ![](assets/7cc65b226b77d626e11eec796edef0c8.jpeg)

**Step 2. Bind IDaaS to the IdP**

You can bind IDaaS to multiple standard upstream IdPs. You can also bind IDaaS to non-standard IdPs, such as self-managed data centers, by using private Connector components. For more information about how to bind IDaaS to different IdPs, see the following topics:

- Bind a DingTalk first-party application to IDaaS

- Connect WeCom to IDaaS

- Connect IDaaS to Lark

- Connect IDaaS to AD

- Connect IDaaS to OpenLDAP

- Bind IDaaS to an OIDC IdP

- Bind IDaaS to Okta

- Bind IDaaS to Microsoft Entra ID (FKA Azure AD)

**Step 3. Configure Apsara Stack DevOps SSO**

To initiate SSO to Apsara Stack DevOps, you must map your IDaaS account to the Resource Access Management (RAM) user of your Apsara Stack tenant account. This way, you can access Apsara Stack DevOps as the RAM user. For more information, see Alibaba Cloud DevOps SSO.

> **Important**
>
> Apsara Stack DevOps SSO is based on Apsara Stack user-based SSO. You can configure only one IdP for user-based SSO within each Apsara Stack tenant account. After you configure Apsara Stack DevOps SSO in an IDaaS instance, you can access the resources of the Apsara Stack tenant account to which the instance belongs only by initiating SSO from the instance.
>
> If you enabled user-based SSO for your Apsara Stack account, we recommend that you evaluate the impacts of SSO and modify the SSO settings on demand, such as using a non-production account to test SSO and making sure that the production account cannot use user-based SSO. This ensures that Apsara Stack DevOps SSO does not affect your workloads.

**Step 4: Synchronize data to Apsara Stack DevOps**

Apsara Stack DevOps users must be synchronized from RAM. You can synchronize accounts in IDaaS to RAM and then synchronize the RAM users to Apsara Stack DevOps. For more information, see the following topics:

- Synchronize accounts in IDaaS to RAM: Synchronize accounts to RAM by using SCIM in Apsara Stack IDaaS.

- Synchronize RAM users to Apsara Stack DevOps: Add RAM users.

<a id="section-9-9"></a>

## 9.9. Configure Alibaba Cloud API Gateway

This topic describes how to use Alibaba Cloud API Gateway and machine-to-machine (M2M) technology to manage third-party access permissions. This method enables efficient, secure, and automated communication between systems.

**Prerequisites**

You have an M2M application server and client in Identity as a Service (IDaaS).

**Overview**

To implement M2M authentication for your API operations and ensure that callers are trusted and their permissions are controlled, you need to follow the following three steps:

1. Register your API operations with Alibaba Cloud API Gateway.

2. Grant permissions to your M2M client.

3. Configure plug-ins in API Gateway to associate the API operations to be protected with the permission scopes of your M2M client.

**Procedure**

**Register API operations with API Gateway**

1. Log in to the  `API Gateway`  console. In the left-side navigation pane, choose **Manage APIs > API Groups**. Click **Create Group**.

2. Choose **Backend Services** in the menu, and click **Create Backend Service** to register your business endpoint with Alibaba Cloud API Gateway. This simplifies the management of the API operations for your business.

   <ol type="i">

   <li>

   Attach your business endpoint to the backend service that you created.

   </li>

   </ol>

3. After you create the backend service, manage the API operations within the backend service.

   <ol type="i">

   <li>

   Find the backend service that you created, and click **Create API** in the Actions column. The Create API page appears.

   </li>

   <li>

   In the Basic Information step, set Security Authentication to **No Authentication** for this

   </li>

   </ol>

   example. Then, click Next.

   <ol type="i" start="3">

   <li>

   In the Define API Request step, specify the **Request Path** and **HTTP Method**

   </li>

   </ol>

   parameters.

   <ol type="i" start="4">

   <li>

   When you define the backend service for the API operation, enter the actual request path. When a caller calls the API operation by using the specified request path, the request is mapped to the actual backend path.

   </li>

   <li>

   Select the response ContentType and complete the API operation creation.

   </li>

   </ol>

4. After you create the API operation, debug it in the console to verify that it is available and runs as expected.

   <ol type="i">

   <li>

   Prepare the debugging environment. Select an environment and publish the API operation.

   </li>

   <li>

   Debug the API operation in the staging environment by sending a request. In this

   </li>

   </ol>

   example, the result meets expectations. This indicates that the API operation is available.

**Grant permissions to the M2M client**

In the  `IDaaS console` , navigate to your **M2M application**. In the authorized applications section, find your **M2M application** and grant it the required permission scopes. In this example, the user:read:one permission scope is granted to the client.

**Configure API Gateway plug-ins**

Configure gateway plug-ins to implement request authentication and authorization. This process associates the M2M permission scopes with API Gateway. You need to create two gateway plug-ins: a **JWT Authentication** plug-in and a **Parameter Access Control** plug-in.

**Create a JWT Authentication plug-in**

- Log in to the  `API Gateway console` . In the left-side navigation pane, choose **Manage APIs > Plugins**. On the Plugin List page, click Create Plugin and set Plug-in Type to **JWT Authentication**.

- Enter the script configuration. The JSON Web Key (JWK) information in the script must match the public key of the M2M server. In the  `IDaaS console` , navigate to your **M2M application**. In the **Application Settings** section, copy the URL of the **Public Key Endpoint**. Open the URL in a browser to view the public key information. The following figure shows the public key information for this example.

  <table>
    <tr>
      <td>Public key endpoint in the console</td>
      <td>Public key content displayed in the browser</td>
    </tr>
  </table>

  Replace the jwk section in the following script with the JWT public key information that you retrieved.

  <table>
    <tr>
      <td>Script configuration before replacement<br><code>---</code><br><code>parameter: id_token         # Obtain</code><br><code>the JWT from the specified parameter,</code><br><code>which corresponds to the API</code><br><code>operation parameter.</code><br><code>parameterLocation: query    # The</code><br><code>location from which the JWT is read.</code><br><code>Valid values: query and header. This</code><br><code>parameter is optional if Request Mode</code><br><code>for the bound API is set to Map</code><br><code>(Filter Out Unknown Parameters) or</code><br><code>Map (Pass-through Unknown Parameters).</code><br><code>This parameter is required if Request</code><br><code>Mode for the bound API is set to</code><br><code>Pass-through.</code><br><code>bypassEmptyToken: false      #</code><br><code>Specifies whether to forward requests</code><br><code>that do not include tokens to backend</code> <code>services without verification.</code><br><code>claimParameters:           # The</code><br><code>claims to be converted into</code><br><code>parameters. API Gateway maps JWT</code><br><code>claims to backend parameters.</code><br><code>- claimName: aud           # The name</code><br><code>of the JWT claim, which can be public</code><br><code>or private.</code><br><code>parameterName: aud     # The name of</code><br><code>the backend parameter, to which the</code><br><code>JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>- claimName: scope             # The</code><br><code>name of the JWT claim, which can be</code><br><code>public or private.</code><br><code>parameterName: scope       # The</code><br><code>name of the backend parameter, to</code><br><code>which the JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>- claimName: client_id             #</code><br><code>The name of the JWT claim, which can</code><br><code>be public or private.</code><br><code>parameterName: client_id       # The</code><br><code>name of the backend parameter, to</code><br><code>which the JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>preventJtiReplay: false    # Specifies</code><br><code>whether to enable the anti-replay</code><br><code>check for jti. Default value: false.</code><br><code>#</code><br><code># The following content needs to be</code><br><code>replaced.</code><br><code>jwk:</code><br><code>kty: RSA</code><br><code>e: AQAB</code><br><code>use: sig</code><br><code>kid: O8fpdhrViq2zaaaBEWZITz  # If</code><br><code>only one JWK is configured, kid is</code><br><code>optional. If the JWT includes a kid,</code><br><code>API Gateway checks the consistency of</code><br><code>kid.</code><br><code>alg: RS256</code> <code>n:</code><br><code>qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-</code><br><code>9do7w9X1uKFXAnqfto4TepSNuYU2bA_-</code><br><code>tzSLAGBsR-</code><br><code>BqvT6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrf</code><br><code>SPEoNU-</code><br><code>0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr-</code><br><code>9FPGy8NCoIO4MfLXzJ3mJ7xqgIZp3NIOGXz-</code><br><code>GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXR</code><br><code>V84tIZpFVh2lmRh0h8ImK-</code><br><code>vI42dwlD_hOIzayL1Xno2R0T-d5AwTSdnep7g-</code><br><code>Fwu8-</code><br><code>sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ</code></td>
      <td>Script configuration after replacement<br><code>---</code><br><code>parameter: id_token         # The</code><br><code>parameter from which the JWT is read.</code><br><code>It corresponds to a parameter in an</code><br><code>API request.</code><br><code>parameterLocation: query    # The</code><br><code>location from which the JWT is read.</code><br><code>Valid values: query and header. This</code><br><code>parameter is optional if Request Mode</code><br><code>for the bound API is set to Map</code><br><code>(Filter Out Unknown Parameters) or</code><br><code>Map (Pass-through Unknown</code><br><code>Parameters). This parameter is</code><br><code>required if Request Mode for the</code><br><code>bound API is set to Pass-through.</code><br><code>bypassEmptyToken: false      #</code><br><code>Specifies whether to forward requests</code><br><code>thatdonotincludetokenstobackend</code> <code>that do not include tokens to backend</code><br><code>services without verification.</code><br><code>claimParameters:           # The</code><br><code>claims to be converted into</code><br><code>parameters. API Gateway maps JWT</code><br><code>claims to backend parameters.</code><br><code>- claimName: aud           # The name</code><br><code>of the JWT claim, which can be public</code><br><code>or private.</code><br><code>parameterName: aud     # The name of</code><br><code>the backend parameter, to which the</code><br><code>JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>- claimName: scope             # The</code><br><code>name of the JWT claim, which can be</code><br><code>public or private.</code><br><code>parameterName: scope       # The</code><br><code>name of the backend parameter, to</code><br><code>which the JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>- claimName: client_id             #</code><br><code>The name of the JWT claim, which can</code><br><code>be public or private.</code><br><code>parameterName: client_id       # The</code><br><code>name of the backend parameter, to</code><br><code>which the JWT claim is mapped.</code><br><code>location: query          # The</code><br><code>location of the backend parameter, to</code><br><code>which the JWT claim is mapped. Valid</code><br><code>values: query, header, path, and</code><br><code>formData.</code><br><code>preventJtiReplay: false    # Specifies</code><br><code>whether to enable the anti-replay</code><br><code>check for jti. Default value: false.</code><br><code>#</code><br><code># Public key in the JWK</code><br><code>jwk:</code><br><code>kty: RSA</code><br><code>e: AQAB</code><br><code>use: sig</code><br><code>kid:</code><br><code>AUTHSKEY7Ph6QS83xkN76oRwvZsJT68ejJ4PdAX</code><br><code>mk     # If only one JWK is</code><br><code>configured, kid is optional. If the</code><br><code>JWT includes a kid, API Gateway</code><br><code>checks the consistency of kid.</code><br><code>alg: RS256</code> <code>n:</code><br><code>i1tIYhXvfilaJi8kaIS8EpgsnDp6G4c1lEg2qRD</code><br><code>_-</code><br><code>1lY8jOIWAVcetq89itl7rjFJ9gmbKGBMJoutaxG</code><br><code>HtbAkY0aINkg1_n_0NnNTZDt2UC1UNJaZh12bkY</code><br><code>yubRLA_t6JS8PVSr5bpse1SErvDiumqU9CjxBUC</code><br><code>d4K8R0ALxOwup6yY5gVT4Juia1bEVGPlJ-</code><br><code>RnuMvXXbVmwuklKTiWNfBFw1lCDPftfzKVEDTXt</code><br><code>4VphAWOT-CyZKJ8hcYiTnd_VaAYxjMQSCxmE-</code><br><code>utrdXGhyDUaQobs0myvD2eJfzcSWG-</code><br><code>qOTC7Hin8bvXIQ_v9BkJO3D6uoLpB14XQozWVTX</code><br><code>aPTIw</code></td>
    </tr>
  </table>

**Create a parameter-based access control plug-in**

- Set Plug-in Type to **Parametric Access Control**.

- Enter the script content to implement access control. The following script uses a condition to implement a verification policy.

  <table>
    <tr>
      <td>The script on the right uses the clientId and scope for verification as an example.<br>condition: "$clientId = 'app_m7hfgn66xkyyxlhpkiw5kjen hy' and $scope like '%user:read:one%'"<br><strong>clientId</strong> is the application ID of the M2M client.<br><strong>scope</strong> is the permission scope of the M2M client. Replace these two parameters based on your business requirements.</td>
      <td><code>---</code><br><code>#</code><br><code># In this example, the API request path is</code><br><code>/{userId}/...</code><br><code># JWT authentication is enabled for the API</code><br><code>request. Two claims, userId and userType, are</code><br><code>available in the JWT.</code><br><code># The following plug-in verification conditions</code><br><code>apply:</code><br><code># - If userType is set to admin, requests in all</code><br><code>paths are allowed.</code><br><code># - If userType is set to user, only requests with</code><br><code>the /{userId} path are allowed.</code><br><code>parameters:</code><br><code>scope: "Token:scope"</code><br><code>clientId: "Token:client_id"</code><br><code>#</code><br><code># Rules are defined based on the preceding</code><br><code>parameters. For each API request, the plug-in</code><br><code>checks the rules in sequence. If a condition in a</code><br><code>rule is met, the result is true and the action</code><br><code>that is specified by ifTrue is performed. If a</code><br><code>condition in a rule is not met, the result is</code><br><code>false and the action that is specified by ifFalse</code><br><code>is performed.</code><br><code># The action ALLOW indicates that the request is</code><br><code>allowed. The action DENY indicates that the</code><br><code>request is denied and an error code is returned to</code><br><code>the client.</code><br><code># If neither the ALLOW nor DENY action is</code><br><code>performed, the plug-in proceeds to check the next</code><br><code>condition.</code><br><code>rules:</code><br><code>- name: checkScope</code><br><code>condition: "$clientId =</code><br><code>'app_m7hfgn66xkyyxlhpkiw5kjenhy' and $scope like</code><br><code>'%user:read:one%'"</code><br><code>ifFalse: "DENY"</code><br><code>statusCode: 403</code><br><code>errorMessage: "No permission by client id:</code><br><code>${clientId}"</code><br><code>responseHeaders:</code><br><code>Content-Type: application/json</code><br><code>X-IDaaS-clientId: ${clientId}</code><br><code>X-IDaaS-scope: ${scope}</code><br><code>responseBody: &#124;</code><br><code>&lt;Reason&gt;No permission by client id:</code><br><code>${clientId}&lt;/Reason&gt;</code></td>
    </tr>
  </table>

**Bind the plug-ins to the API operation**

After you create the two plug-ins, bind them to the API operation. This creates a mapping between the permission scope and the API operation. In this example, this binding allows the user:read:one permission scope to control access to the hello API operation.

- For each of the two plug-ins, click **Bind API** in the Actions column to bind the plug-in to the API operation.

**Verification and usage**

After you complete the preceding procedure, obtain an authorization token from the M2M server. The caller then uses this token to access business API operations.

**Obtain a token**

Use the  `client_secret_post authentication method`  to obtain a token. Perform the following steps:

- Copy the Issuer URL of the M2M server.

- Enter the client_secret, client_id, grant_type, and scope request parameters. Send a request to the Issuer URL.

  <table>
    <tr>
      <td>client_secret is the application secret of the M2M client.<br>client_id is the application ID of the M2M client.<br>grant_type is the fixed at client_credentials.<br>scope is the audience identifier of the M2M server plus the permission scope. In this example, scope is https://xxxx.aliyunidaas.com|user:read:one.</td>
      <td></td>
    </tr>
  </table>

**Debug the API operation**

- Use the second-level domain of the group as the request URL. You can find this domain in the group details.

- The input parameters are the token location and token parameter identifier that you defined in the JWT Authentication plug-in. In this example, the input parameter key is id_token, and the value is the token that you retrieved in the previous step.

- The request returns the expected result. This indicates that the M2M client has permissions to access the hello API operation.

**References**

- For more information about the features of M2M applications, see M2M applications (machine-to-machine permission management).

- For information about how to use Alibaba Cloud Resource Access Management (RAM) to implement access without an AccessKey pair, see Use RAM to configure AccessKey-free access.

<a id="section-9-10"></a>

## 9.10. Use RAM to configure AccessKey-free access

This topic describes how to use Identity as a Service (IDaaS) together with Resource Access Management (RAM) to configure AccessKey-free access for a Machine-to-Machine (M2M) application and obtain a Security Token Service (STS) token.

**Prerequisites**

- An M2M application is configured. For more information, see  `M2M applications (machine-to-machine permission management)` .

**Create an OIDC IdP**

1. In the left-side navigation pane, choose **Integrations > SSO**.

2. On the **Role-based SSO** tab, click the **OIDC** tab. Then, click **Add IdP**.

3. On the **Create IdP** page, configure the following parameters.

   | Parameter | Description |
   | --- | --- |
   | IdP Name | The name must be unique within an Apsara Stack tenant account. |
   | Issuer URL | The URL of the issuer that is provided by an external identity provider (IdP). The URL of the issuer must start with <code> https </code> and be a valid URL. The URL cannot contain query parameters that follow a question mark (<code> ? </code>), logon information that is identified by at signs (<code> @ </code>), or a fragment that is identified by number signs (<code> # </code>). |
   | Fingerprint | The fingerprint that is generated based on the HTTPS certificate of an external IdP. You can use a fingerprint to prevent the URL of the issuer from being hijacked or tampered with.<br>After you specify a valid value for <strong>Issuer URL</strong>, you can click <strong>Obtain</strong> <strong>Fingerprint</strong>. Apsara Stack will calculate the fingerprint. We recommend that you calculate the fingerprint on your computer. For example, you can <code> use OpenSSL to calculate the fingerprint </code>. Then, you can compare the calculation result with the calculation result provided by Apsara Stack. If the calculation results are different, the URL of the issuer may have been attacked. Make sure that you enter a valid fingerprint.<br>Note<br>If you want to rotate the certificate of your IdP, we recommend that you generate the fingerprint of the new certificate and add the fingerprint to the OIDC IdP that you created in the RAM console before the rotation. After at least one day, rotate the certificate. You can delete the previous fingerprint after you obtain an STS token. |
   | Client IDs | The ID that is generated for an application when you register the application in the external IdP. When you apply for an OIDC token from an external IdP, you must use a client ID. The client ID is specified in the <code> aud </code> field of the OIDC token that is issued. When you create an OIDC IdP, you must configure the client ID. If you want to use the OIDC token to obtain an STS token, Apsara Stack checks whether the client ID that is specified in the <code> aud </code> field is the same as the client ID that you configured in the OIDC IdP. You can assume a RAM role only when the client IDs are the same.<br>If multiple clients need to access Apsara Stack resources, you can configure multiple client IDs. You can configure a maximum of 50 client IDs. |
   | Earliest Issuance Time Allowed | The time limit on an OIDC token. If an OIDC token is issued earlier than the time limit, the OIDC token cannot be used to obtain an STS token.<br>Default value: 12 hours. Valid values: 1 to 168 hours. |
   | Remarks | The description of the OIDC IdP. |

4. Click **Create IdP**.

**Create an OIDC IdP role**

1. Log in to the RAM console and choose **Roles > Create Role > Identity Provider > Switch to Policy Editor**.

   ![](assets/e4083d765e2182c9292958162186d2c1.png)

2. In the editor, follow the steps shown in the following figure to add an **IdP**.

   ![](assets/b6864b0dd00ae0978b080f485a751fb8.png)

3. In the **Add principal** dialog box, select the IdP that you created from the **Identity Provider** drop-down list and click **OK**.

   ![](assets/75aa20c240c53df71050ae3b29cb321b.jpeg)

4. After the IdP is added, the following iss and aud conditions are generated by default. You can modify or delete both conditions or add other conditions.

   ![](assets/c534e2ea5d2972019372545f5a310445.jpeg)

5. The following example demonstrates how to add a sub condition. You can add other conditions as needed. After you complete the configuration, click **OK**.

   > **Note**
   >
   > - **Value**: Enter the value of **ResourceServer Identifier** of the M2M application server. For more information about how to add M2M applications and view audience identifiers, see  `M2M applications (machine-to-machine permission management)` .
   >
   > - For more information about conditional expressions, see  `Policy elements` .
   >
   > - RAM OIDC supports only three conditions: **oidc:iss**, **oidc:aud**, and **oidc:sub**.

   ![](assets/c38a764736cbb13060c2753075576c0c.jpeg)

6. Click **OK** in the lower part of the page. In the Create Role dialog box that appears, enter the name of the role that you want to create and click **OK**.

   ![](assets/0adf725dc333f86a494963cb81bfdcc7.jpeg)

**Grant permissions to the role**

You can click **Grant Permission** on the page shown in the following figure to grant permissions to the role that you created.

![](assets/406faff0479d86cf4d8479b6c33b4b86.jpeg)

**Obtain an M2M token**

**Use curl**

- Replace the following placeholder parameters with the configuration of your application. Then, run the curl command to obtain the token.

  ```bash
  # Replace <app_issuer_endpoint>, <YOUR_APP_CLIENT_ID>, <YOUR_APP_CLIENT_SECRET>, and 
  <YOUR_SERVER_AUD_IDENTIFIER> with the actual values specified for the M2M application. 
  #
  # <YOUR_SERVER_ISSUER_ENDPOINT>: the issuer. View Endpoint in Resources Server Application > General Configuration > Issuer and replace it. 
  # <YOUR_APP_CLIENT_ID>: the client ID. View client_id in Client Application > General
  Configuration > Credential Management and replace it. 
  # <YOUR_APP_CLIENT_SECRET>: The secret of the client. View client_secret in Client Application > General Configuration > Credential Management and replace it. 
  # <YOUR_SERVER_AUD_IDENTIFIER>: the server audience identifier. View the audience identifier in Resources Server Application > General Configuration > Permission Application > Audience Identifier and replace it. 
  #
  curl --location --request POST 
  'https://<YOUR_SERVER_ISSUER_ENDPOINT>.aliyunidaas.com/api/v2/iauths_system/oauth2/toke
  \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<YOUR_APP_CLIENT_ID>' \
    --data-urlencode 'client_secret=<YOUR_APP_CLIENT_SECRET>' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'scope=<YOUR_SERVER_AUD_IDENTIFIER>|.all'
  ```

- The following figure shows the result when the token is obtained successfully.

  ![](assets/fc7c3880ea60646855807daacf0d4caf.png)

**use Postman**

- As shown in the following figure, replace the parameters with the configuration of your application and then send a request through Postman to obtain a token.

  ![](assets/b9002ade14eae61f0bc9602e3f05f13f.jpeg)

**Use the M2M token to obtain an STS token to assume the RAM role**

> **Note**
>
> For more information about STS, see  `What is STS?` .

**Obtain the STS token by calling an API operation**

- Log in to OpenAPI Explorer and find the  `AssumeRoleWithOIDC`  API operation.

  > **Note**
  >
  > For more information about the **AssumeRoleWithOIDC** operation, refer to API Reference.

- Specify the request parameters and click **Submit Request** to obtain the STS token.

  > **Important**
  >
  > - OIDCProviderArn: Go to the **Basic Information** page of the OIDC IdP role that you created and obtain the ARN from the **Trust Policy**.
  >
  > - RoleArn: Go to the **Basic Information** page of the OIDC IdP role that you created and obtain the **ARN**.
  >
  > - OIDCToken: Enter the M2M token that you obtained.
  >
  > - RoleSessionName: This is a user-defined field that does not have special requirements. It is used only as a role identifier.

<a id="section-9-11"></a>

## 9.11. Synchronize users or groups from Azure AD to IDaaS by using SCIM

This topic describes how to synchronize users from Azure Active Directory (Azure AD) to Identity as a Service (IDaaS) by using System for Cross-domain Identity Management (SCIM). This helps you automate user management and reduces manual operations.

**Prerequisites**

1. An Azure AD tenant is created and is granted the administrator permissions.

2. An Azure AD administrator account and an IDaaS administrator account are created, and the accounts have the required permissions.

**Step 1: Configure SCIM synchronization in IDaaS**

1. Log in to the IDaaS console and create a **standard protocol** or **custom** application or select an existing application.

2. On the Applications page, find the application that you want to manage and click the application name to go to the details page of the application. On the **Provisioning** tab, click the **Synchronize Application to IDaaS** tab.

3. On the **Synchronize Application to IDaaS** tab, configure the Bearer Token, SCIM Base URL, and Configure SCIM Operation Permission fields. Bearer Token is used for identity authentication, SCIM Base URL is the address for receiving SCIM-based synchronization requests, and Configure SCIM Operation Permission allows you to manage supported SCIM API operations.

4. Select the supported SCIM API operations.

**Step 2: Enable SCIM synchronization in Azure AD**

1. Use the administrator account to log in to Azure AD.

2. In the top search box of the homepage, search for **Microsoft Entra ID** and click it.

3. **Create an application.**

   <ol type="i">

   <li>

   On the **Overview** page, click **Create your own application > to create an application**.

   </li>

   <li>

   Enter an application name, select **Integrate any other application you don't find in the gallery (Non-gallery)**, and click **Create**.

   </li>

   </ol>

4. **Grant permissions.**

   <ol type="i">

   <li>

   On the details page of the created application, click **Assign users and groups**.

   </li>

   <li>

   On the **Users and groups** page, click **Add user/group**.

   <ol type="a">

   <li>

   **Assign users to the application.** In the **Users** pane, select the users that you want to synchronize and click **Select >** to assign the users to the application.

   </li>

   <li>

   **Assign a group to the application.** Click the **Groups** tab and select the group to be synchronized. Click **Select >** to assign the group to the application.

   </li>

   </ol>

   </li>

   </ol>

5. In the left-side navigation pane, click **Overview (Preview)**.

   <ol type="i">

   <li>

   Create a configuration and click **Connect your application**. Configure the following parameters:

   <ol type="a">

   <li>

   **Tenant URL**: Enter the value of **SCIM Base URL** provided by IDaaS.

   </li>

   <li>

   **Secret token**: Enter the value of **Bearer Token** generated by IDaaS.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   Click Test connection. Make sure that Azure AD can connect to IDaaS. If the test is passed, the following message is displayed: **Connection test for xxx was successful**. Then, click **Create**.

   > **Important**
   >
   > Make sure that open API operations are enabled in IDaaS.

   </li>

   </ol>

   </li>

   </ol>

6. Configure **attribute mappings**. Click **Edit attributes**.

   <ol type="i">

   <li>

   Click **Provision Azure Active Directory Users** to configure attribute mappings for users. Retain only the required attribute mappings and delete all other attribute mappings. Then, click **Save** in the upper-left corner.

   > **Important**
   >
   > Custom fields in Azure AD **cannot be synchronized** to IDaaS extended fields.

   </li>

   </ol>

7. On the application details page, click **Start provisioning** to enable auto synchronization. The default provisioning interval is fixed, which is 40 minutes. To manually trigger a synchronization, click **Provision on demand**.

**Step 3: Verify the synchronization results**

1. Log in to the IDaaS console.

2. On the **User > Accounts and Orgs** page, click the **Account and Organization** tabs to check whether the users and group are synchronized. The **Source** of users synchronized from Azure AD is automatically marked as **SCIM Import**.

3. On the **Account > Organization** tab, view the group synchronized from Azure AD.

After you perform the preceding steps, you can synchronize users in Azure AD to IDaaS by using SCIM to automate user management. If you encounter issues during synchronization, contact your account manager or technical support.

<a id="section-9-12"></a>

## 9.12. Synchronize users or groups from Okta to IDaaS by using SCIM

To reduce maintenance and management costs, enterprises can synchronize existing accounts in their internal systems to the cloud based on a set of rules. You can synchronize users or groups from Okta to Apsara Stack Identity as a Service (IDaaS) by using Cross-domain Identity Management (SCIM) and security authorization of Open Authorization (OAuth) applications.

**Prerequisites**

1. **Required permissions**:

   - Your IDaaS account has the administrator permissions.

   - Your Okta account has the super administrator permissions.

2. **Environment preparation**

   - SCIM 2.0 provisioning is enabled for your Okta instance.

   - An IDaaS instance that has access to relevant networks is created.

**Step 1: Create and authorize an application in IDaaS**

1. Log in to the IDaaS console and create a **standard protocol** or **custom** application or select an existing application.

2. On the Applications page, find the application that you want to manage and click the application name to go to the details page of the application. On the **Provisioning** tab, click the **Synchronize Application to IDaaS** tab.

3. On the Synchronize Application to IDaaS tab, configure the **Bearer Token**, **SCIM Base URL**, and Configure SCIM Operation Permission fields. Bearer Token is used for identity authentication, SCIM Base URL is the address for receiving SCIM-based synchronization requests, and Configure SCIM Operation Permission allows you to manage supported SCIM API operations.

4. For more information about how to select grant types for the SCIM API, see Synchronize IDaaS accounts to an application by using SCIM.

**Step 2: Configure SCIM synchronization in Okta**

1. **Create an Okta application**.

2. **Enable SCIM provisioning**. In the application you created, click the **General** tab and click **Edit** in the upper-right corner of the page. Then, select **Enable SCIM provisioning**. Click **Save**.

3. **Start the provisioning**. Click the **Provisioning** tab.

   <ol type="i">

   <li>

   **Configure an SCIM connection.** In the SCIM Connection section, click Edit and configure the following parameters:

   <ol type="a">

   <li>

   **SCIM connector base URL**: Enter the **SCIM Base URL** provided by IDaaS.

   </li>

   <li>

   **Unique identifier field for users**: Enter userName.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   **Supported provisioning actions**: Select **Push New Users**, **Push Profile Updates**, and **Push Groups** for the Supported provisioning actions parameter.

   </li>

   <li value="500">

   **Authentication Mode**: Select **HTTP Header** from the drop-down list.

   </li>

   </ol>

   <ol type="a" start="5">

   <li>

   **Authorization**: Enter the **Bearer Token** provided by IDaaS.

   ![](assets/1278e7f48152968a4143ff7d3388fc24.jpeg)

   </li>

   <li>

   **Test the connectivity of the connection**. Click **Test Connector Configuration**. If the connection is established, the **Connector Configured successfully** message appears. Then, click **Save**.

   </li>

   </ol>

   </li>

   <li>

   **Synchronize with the IDaaS application.**

   <ol type="a">

   <li>

   In the Provisioning to App section of the To App page, select the required options. Select **Sync Okta Password** based on your business requirements. If this option is not selected, password changes in Okta will not be synchronized to IDaaS. Click **Save**.

   </li>

   <li>

   Map attributes. You can use the attribute mapping feature to push user configuration data to the IDaaS application. This way, you can automatically configure and update user account fields.

   ![](assets/df47fd2eab35d734fc169e050be076e0.jpeg)

   <ol type="a">

   <li>

   You can select **Go to Profile Editor** to open the standard profile editor for the selected application, or select **Force Sync** to immediately synchronize the changes of the application to Okta.

   </li>

   <li>

   Click the rightmost <img src="assets/1275344d82aab705afa338afa63788ca.png" width="11" alt=""> icon. **Retain only the attribute mappings shown in the**

   **following figure** and delete all other attribute mappings.

   ![](assets/a4e60ad543f3f7962b115afa0676a149.jpeg)

   > **Important**
   >
   > Attributes that do not exist in the Okta user configuration cannot be mapped.

   </li>

   </ol>

   <ol type="i" start="100">

   <li>

   To adjust field mappings, click the <img src="assets/177994b3a5dff512e4c260657a672e11.png" width="18" alt=""> icon. After you complete the configurations,

   click **Save**. This step is optional.

   ![](assets/6dfb49f2094efffaea21e237d3fd8c9f.jpeg)

   </li>

   </ol>

   </li>

   </ol>

   </li>

   </ol>

4. **Synchronize users**. To assign users to the application, click the **Assignments** tab, choose **Assign** > **Assign to People**, select users, and then click **Assign**. Modify related attributes based on your business requirements. Then, click **Save and Go Back** and select the users that you want to synchronize.

5. **Synchronize user groups**. Click the **Push Groups** tab and select the method to search for groups. In this example, **Find groups by name** is selected. Enter the name of a group and click **Save**. If **Push Status** changes from **Pushing** to **Active**, the group is synchronized.

   > **Important**
   >
   > Make sure that Okta and IDaaS use the same password policies. You can configure IDaaS policies to match that of Okta or modify Okta policies to match that of IDaaS. This ensures consistent password security.

**Step 3: Verify the synchronization results**

1. Go back to the IDaaS console and check whether the user information is synchronized.

2. Go to the User or Group page to view the synchronized users or groups. **Source** for the synchronized users or groups is automatically displayed as **SCIM Import**.

After you perform the preceding steps, you can synchronize users or user groups in Okta to Alibaba Cloud IDaaS for centralized identity management. This solution reduces manual operations and improves management efficiency and security. If you need further assistance, contact your account manager or technical support.

<a id="section-9-13"></a>

## 9.13. Use IDaaS to implement user-based SSO and role-based SSO for Grafana

This topic describes how to use Identity as a Service (IDaaS) to implement user-based and role-based single sign-on (SSO) for Grafana. The following procedure shows how to deploy a Docker environment, create and configure an OIDC application in IDaaS, configure OAuth in Grafana to integrate with IDaaS, map roles, and verify SSO. This topic helps you quickly connect Grafana to IDaaS to implement secure and convenient identity authentication and permission management in IDaaS.

1. **Install Grafana**

**Step 1: Prepare the environment**

```bash
# Check the Docker version and verify that it is installed.
docker --version
```

**Step 2: Obtain the Grafana image**

```bash
# Pull the Grafana 9.3.2 image.
docker pull grafana/grafana:9.3.2
```

**Step 3: Configure the Grafana data directory and initialization file**

1. **Create a Grafana directory and configure permissions**

   ```bash
   # Create a Grafana directory and grant permissions.
   mkdir -p /opt/grafana/{data,plugins,config} && \
   chmod -R 777 /opt/grafana/{data,plugins,config}
   ```

2. **Prepare the configuration file**

   ```bash
   # Create a temporary container that stores and automatically cleans up the configuration file.
   docker run --rm --name grafana-tmp -d -p 3000:3000 grafana/grafana:9.3.2 && \
   docker cp grafana-tmp:/etc/grafana/grafana.ini /opt/grafana/config/grafana.ini && \
   docker stop grafana-tmp

   # Modify the configuration file based on your business requirements.
   # vim /opt/grafana/config/grafana.ini
   ```

**Step 4: Start the container**

```bash
docker run -d \ # Start the container.
    --name grafana \                                                # Name the container 
grafana.
    --restart unless-stopped: The container automatically restarts unless manually stopped.
    -p 3000:3000 \                                                  # Map port 3000 of th
e container to port 3000 of the host.
    --user "$(id -u):$(id -g)" \                                    # Run with the 
permissions of the current user to enhance security.
    -v /etc/localtime:/etc/localtime:ro \                           # Synchronize host t
ime configuration (read-only).
    -v /opt/grafana/data:/var/lib/grafana \                         # Persist Grafana da
ta.
    -v /opt/grafana/plugins:/var/lib/grafana/plugins \              # Persist the storag
e plug-in.
    -v /opt/grafana/config/grafana.ini:/etc/grafana/grafana.ini \   # Use a custom configuration file.
    -e GF_SECURITY_ADMIN_PASSWORD=<your password> \                 # Set a password.
    -e GF_PATHS_CONFIG=/etc/grafana/grafana.ini \                   # Specify the config
uration file path.
    -e GF_PATHS_DATA=/var/lib/grafana \                             # Specify the data d
irectory path.
    -e GF_PATHS_PLUGINS=/var/lib/grafana/plugins \                  # Specify the plug-i
n directory.
    grafana/grafana:9.3.2                                           # Use a specified ima
ge version.
```

**Step 5: Verify the service**

Visit the Grafana login page. Enter  `http:// Server IP address: Port number` , such as http://192.168.1.100:3000, in the address bar of your browser. Enter the registered email address or the username and password, and click **Log in**.

2. **Create an OIDC application in IDaaS**

To create an application of the standard OIDC protocol in IDaaS, perform the following steps:

1. Log in to the IDaaS console, find the Employee Identity and Access Management (EIAM) instance, and click Console in the Actions column.

2. In the left-side navigation pane, click **Application**. On the Application page, click **Add Application**.

3. Click the **Standard Protocols** tab and click **Add Application** in the OIDC card.

4. In the **Add Application - OIDC** dialog box, enter an application name and click **Add** to create an application.

5. Go to the details page of the OIDC application and choose **Sign In > SSO > Redirect URI**.

   Set **Redirect URI** to  `http://${***********}/login/generic_oauth` . Replace the value enclosed by the braces ({}) with the actual service address, such as a domain name or an IP address.

6. Click **Show Advanced Settings**, select the **scope of user information** that you want to obtain, and then click Save.

7. Go to the **Log In > Authorize** tab, click the **Authorize**, grant permissions to the user that you created, and then click **Confirm**.

After you complete the preceding steps, you must record the **client_id, client_secret, authorization endpoint, token endpoint, and user information endpoint** of the current application. This information is required when you configure SSO. Make sure that this information is properly preserved, because it is the key information for establishing a trusted relationship between Grafana applications and IDaaS.

3. **Configure OAuth in Grafana to integrate with IDaaS**

**Configuration in IDaaS EIAM**

You need to obtain two pieces of key information from IDaaS and configure the information in Grafana.

1. Obtain **client_id** and **client_secret**. On the **General** tab, view and record your **client_id** and **client_secret**.

2. **Obtain the request endpoint.** Go to the **Log In > SSO** tab. In the lower part of the tab, you can view the following fields:

   - **Authorization Endpoint**

   - **Token Endpoint**

   - **User Information Endpoint**

3. On the **Sign-In > SSO** tab, set the **Redirect URI** parameter to the Grafana URI.

4. On the **Sign-In > SSO** tab, enter the expression ArrayMap(user.groups, __item.groupName) in the **Extend id_token** field.

**Configuration in Grafana**

1. **Modify the Grafana configurations**

   > **Important**
   >
   > Make sure that the **token endpoint** (token_url) and the **user information endpoint** (api_url) are connected to the application server.

   <ol type="i">

   <li>

   **Go to the directory of the Grafana configuration file**

   ```bash
   cd /opt/grafana/config
   ```

   </li>

   <li>

   **Modify the grafana.ini configuration file**. Find the generic_oauth field and modify the value as shown in the following sample code. You do not need to modify other fields. For more information, see Configure Generic OAuth authentication.

   ```text
   # generic_oauth configuration.
   [auth.generic_oauth]
   # Whether to enable general OAuth authentication. Set the value to true.
   enabled = true  
   # The display name, which will be displayed on the login button.
   name = AliCloud IDaaS 
   # Whether to allow new users to register through OAuth.
   allow_sign_up = true          
   # The client identifier obtained from IDaaS. This field is required.
   client_id =app_******
   # The client key obtained from IDaaS. The client key is sensitive information, which must be kept confidential.
   client_secret =CS4gno67**********h3V5uNYp3W1CQW767WZ7ewjZKehe
   # The IDaaS authorization endpoint that is used for user authentication and authorization requests.
   auth_url =https://of5mhrcn.aliyunidaas.com/login/app/app_******/oauth2/authorize
   # The IDaaS token endpoint, which is used to obtain the access token (access_token) 
   and ID token (id_token).
   token_url =https://eiam-api-cn-
   hangzhou.aliyuncs.com/v2/idaas_******/app_******/oauth2/token
   # The IDaaS user information endpoint that is used to obtain the basic information about a user.
   api_url =https://eiam-api-cn-
   hangzhou.aliyuncs.com/v2/idaas_******/app_******/oauth2/userinfo
   # The JMEpath that is used to obtain email addresses.
   email_attribute_path=data.email
   # The required permission scope.
   scopes = openid,profile,email,phone

   # To map a user role in IDaaS to a Grafana role, add the following configurations:
   role_attribute_path = contains(roles[*], 'admin') && 'GrafanaAdmin' || 
   contains(roles[*], 'editor') && 'Editor' || 'Viewer'
   # Allow IDaaS administrators to be mapped as Grafana superusers.
   allow_assign_grafana_admin = true

   [server]
   # Replace root_url with the actual address, because the redirect_uri for authorization callbacks is the Grafana address.
   root_url =http://60.***.***.144:3000
   ```

   > **Important**
   >
   > - You can replace **role_attribute_path** based on your business requirements. For more information, see Configure role mapping.
   >
   > - All values that contain \*\*\*\*\*\* need to be replaced by the actual values obtained from IDaaS.

   </li>

   <li>

   **Role mapping (role_attribute_path) rules:**

   - `roles[*]` : The array named  `roles`  that is extracted from the user attributes. In most cases, the array contains a list of user roles returned by OAuth or LDAP.

   - `contains(roles[*], 'admin')` : Checks whether the  `roles`  array contains an element whose value is  `'admin'` .

   - If the  `roles`  array contains  `'admin'` , the user role is set to  `'GrafanaAdmin'` , which indicates Grafana super administrators.

   - If the  `roles`  array does not contain  `'admin'`  but contains  `'editor'` , the user role is set to  `'Editor'` , which has editor permissions.

   - If the  `roles`  array does not contain  `'admin'`  or  `'editor'` , the user role is set to  `'Viewer'` , which has viewer permission.

   </li>

   </ol>

2. **Restart the Grafana service.** Save the configuration changes and restart the Grafana service to make sure that the changes are applied.

   ```bash
   docker restart grafana
   ```

   4. **Verify SSO for Grafana**

1. **User-based SSO**

   On the Grafana login page, click **Sign in with AllCloud IDaaS**. If you are not logged in to your IDaaS account, the system automatically redirects you to the IDaaS login page. After you pass identity verification, you are automatically logged in to the Grafana system.

   > **Important**
   >
   > If the SSO login option is not displayed, you must confirm that **IDaaS** is correctly enabled as an identity provider (IdP) in the Grafana configuration file.

2. **Role-based SSO**

   Create different role groups in IDaaS and add the users to be authorized to the groups.

   <ol type="i">

   <li>

   Assign different roles to the users in IDaaS, such as  `admin` ,  `editor` ,**,**  `viewer` .

   </li>

   <li>

   Authorize the group to the OIDC application created in IDaaS.

   </li>

   <li>

   Use users with different roles to log in to Grafana through SSO.

   </li>

   <li>

   Check whether the user permissions are as expected:

   - **Admin**: The Grafana super administrator can manage data sources and users.

   - **Editor**: Editors can create and modify dashboards, but cannot manage users.

   - **Viewer**: Viewers can only view the dashboard.

   </li>

   <li>

   If the role mappings are not as expected, check the  `role_attribute_path`  configuration in  `grafana.ini`  to ensure that the expression matches the role attributes returned by IDaaS.

   </li>

   </ol>

> **Important**
>
> Grafana uses the OAuth 2.0 protocol to implement SSO. However, only SSO processes that are initiated by Grafana service providers (SPs) are supported. SSO processes that are initiated by IdPs are not supported. Before you use the SSO feature, make sure that your IDaaS account username is the same as the Grafana username. Otherwise, you need to associate the accounts in IDaaS or create a corresponding user in Grafana.

<a id="section-9-14"></a>

## 9.14. Log in to IDaaS applications from Lark by using SSO

This topic describes how to integrate enterprise custom application of Lark with Identity as a Service (IDaaS) applications to enable single sign-on (SSO) login from Lark custom applications to IDaaS.

**Prerequisites**

Make sure that the following requirements are met before you start:

- Enterprise Identity Access Management (EIAM) of IDaaS is activated.

- A Lark account is created and has administrator permissions.

- SAML 2.0 or OAuth 2.0 integration is supported by the application.

**Procedure**

**Step 1: Add an application in IDaaS**

Add an application in IDaaS and configure SSO for the application. In this topic, Apsara Stack user-based SSO is used.

1. Log in to the IDaaS console and click **Console** in the Actions column of the desired IDaaS instance.

2. In the left-side navigation pane, click **Application**. On the Application page, click **Add Application** to go to the Marketplace tab. Then, search for Alibaba Cloud - SSO.

3. On the **General** tab, obtain the **ID**. This ID is used to concatenate the homepage URL to WeCom SSO.

4. Go to the **Sign In > SSO** tab.

   <ol type="i">

   <li>

   **SSO**: Make sure that SSO is in the **Enabled** state.

   <ol type="i" start="2">

   <li>

   Alibaba Cloud Account ID: Enter the ID of your Apsara Stack tenant account.

   </li>

   <li>

   : Select the application account. If the account is not available, select the IDaaS account.

   </li>

   </ol>

   </li>

   <li value="4">

   **Authorize**: Select All Users.

   </li>

   <li>

   **Application Settings**: Download the **IdP metadata** and upload it to **SSO > User SSO > Metadata Document** in the Resource Access Management (RAM) console. After you complete the configuration, click **Save**.

   </li>

   </ol>

5. Verify whether SSO works as expected. Access the portal URL, and click the Apsara Stack user-based SSO icon to log in to Apsara Stack from IDaaS. The SSO request is initiated from the IdP. For more information, see Configure Apsara Stack user-based SSO.

**Step 2: Create a custom application on Lark Open Platform**

1. Log in to Lark Open Platform and go to the **Developer Console > Custom App > Create Custom App** page.

2. After you enter the basic information about the application, such as the application name, application description, and application logo, click **Create**.

3. Add application capabilities. On the application details page, choose **Add Features > By Feature** and click **Add**.

4. Configure a web application.

   On the **Web Applications** page, modify the **web application configuration**. The URL of the desktop homepage and mobile homepage must be concatenated with the application URL in the following format:

   ```text
   https://{IDaaS portal URL}/login/go/{IDaaS application ID}
   # Example: https://of5*****.aliyunidaas.com/login/go/app_nbryes3eewn*************** 
   ```

   <ol type="i">

   <li>

   For more information about how to obtain the URL of the IDaaS portal, see IDaaS portal.

   </li>

   <li>

   For more information about how to obtain the ID of an IDaaS application, see Obtain the

   </li>

   </ol>

   application ID.

5. Permission Management: Grant required permissions on the application contact list. For more information, see Permission management.

> **Important**
>
> After you modify the configurations of the Lark application, make sure that the modifications are published. Otherwise, the modifications do not take effect. You can publish the modifications in the Lark console by clicking **Create Version**.

**Step 3: Verify whether you can log in to the IDaaS application from Lark through SSO**

1. Click the Lark application in the Lark console.

   > **Note**
   >
   > If the application is not displayed in the console, you can search for the application by name and click Add to Favorites to add it.

2. If you are logged in, you will directly enter the application page without the need to re-enter your username or password.

**References**

- Connect IDaaS to Lark

- Apsara Stack user-based SSO

<a id="section-9-15"></a>

## 9.15. Log in to IDaaS applications in WeCom through SSO

This topic describes how to log in to an Identity as a Service (IDaaS) application in WeCom through single sign-on (SSO). The procedure in this topic describes how to create an application in IDaaS, create an application in WeCom and configure a homepage address, and verify SSO.

**Prerequisites**

Make sure that the following requirements are met before you start:

- Apsara Stack IDaaS is activated.

- A WeCom account is created and has administrator permissions.

- SAML 2.0 or OAuth 2.0 integration is supported by the application.

**Procedure Step 1: Create an application in IDaaS**

> **Note**
>
> In this topic, Secure Access Service Edge (SASE) is used as an example.

1. Log in to the IDaaS console and click **Console** in the Actions column of the desired IDaaS instance.

2. In the left-side navigation pane, click **Application**. On the Application page, click **Add Application** to go to the **Add Application** tab. Then, search for Alibaba Cloud - SASE.

3. On the **General** tab, obtain the **ID**. This ID is used to concatenate the homepage URL to WeCom SSO.

4. Go to the **Sign In > SSO** tab.

   <ol type="i">

   <li>

   **SSO**: Make sure that SSO is in the **Enabled** state.

   <ol type="i" start="2">

   <li>

   : Select the application account. If the account is not available, select the IDaaS account.

   </li>

   </ol>

   </li>

   <li value="3">

   **Authorize**: Select All Users.

   </li>

   <li>

   **Application Settings**: Download the IdP metadata and upload it as an SAML meta-configuration file to complete the SSO settings.

   </li>

   <li>

   After you complete the configuration, click **Save**. For more information, see Configure SSO for Alibaba Cloud SASE.

   </li>

   </ol>

**Step 2: Create an application in the WeCom admin console**

1. Log in to the WeCom admin console. Choose **Application Management > Applications > Self-built** and create an application.

2. Enter the application information.

   <ol type="i">

   <li>

   **Application Logo**: Upload the application logo. We recommend that you use a JPG or PNG image with a size of 750 × 750 within 1 MB.

   </li>

   <li>

   **Application Name**: Enter the name to be displayed for the application on the platform.

   </li>

   <li>

   **Application Description**: Briefly describe the features and applicable scenarios of the application.

   </li>

   <li>

   **Visibility**: Select the departments or members who can use the application. After you complete the configuration, click **Create Application**.

   </li>

   </ol>

3. On the application details page, set the homepage URL of the application.

   <ol type="i">

   <li>

   Click **Settings** to go to the **Set Workbench Application Homepage** page.

   </li>

   <li>

   Select the **Web** option and click **Configure Mobile And Desktop Separately**.

   </li>

   <li>

   Enter a mobile URL and a desktop URL. Concatenate the URL and application URL.

   </li>

   </ol>

   Format:

   ```text
   https://{IDaaS portal URL}/login/go/{IDaaS application ID}
   # Example: https://of5*****.aliyunidaas.com/login/go/app_nbryes3eewn*************** 
   ```

   <ol type="a">

   <li>

   For more information about how to obtain the URL of the IDaaS portal, see Access to the IDaaS portal.

   </li>

   <li>

   For more information about how to obtain the ID of an IDaaS application, see Step 1 of this topic.

   </li>

   </ol>

   <ol type="i" start="4">

   <li>

   Select the option that enables users to enter the homepage through the WeChat plugin. When a member clicks the application in the WeCom admin console, the member enters the configured homepage. After you complete the configuration, click **OK**.

   </li>

   </ol>

**Step 3: Verify SSO**

1. In the WeCom admin console, click the created application.

2. If you are logged in, you will directly enter the application page without the need to re-enter your username or password.

<a id="section-9-16"></a>

## 9.16. Configure SSO for AI Coding Assistant Lingma

This topic describes how to use Identity as a Service (IDaaS) and Apsara DevOps Enterprise Edition to configure single sign-on (SSO) for AI Coding Assistant Lingma. The procedure in this topic shows how to create an OpenID Connect (OIDC) application, create an Apsara DevOps Enterprise Edition instance, and bind the OIDC application to IDaaS.

**Step 1: Create an OIDC application in IDaaS**

1. Log in to the IDaaS console. On the page that appears, find the desired IDaaS Employee **Identity and Access Management (EIAM)** instance. Click **Console** in the Actions column of the instance.

2. In the left-side navigation pane, click **Application**. On the Application page, click **Add Application** and then click the **Standard Protocols** tab.

3. On the General tab, obtain the **client_id** and **client_secret**, which are required for binding the application to IDaaS<strong>.</strong>

4. Go to the **Sign In > SSO** tab.

   <ol type="i">

   <li>

   Turn on SSO.

   </li>

   <li>

   Enter the callback URL that is used in Step 3 in the Redirect URIs field.

   </li>

   <li>

   Authorize: Select All Users.

   </li>

   <li>

   In the Application Settings section, obtain the issuer, which is required for binding the application to IDaaS<strong>.</strong> After you complete the configuration, click Save.

   </li>

   </ol>

**Step 2: Create an Apsara DevOps Enterprise Edition instance and configure the network**

> **Note**
>
> To manage AI Coding Assistant Lingma Enterprise Dedicated Edition, you need to use Apsara DevOps. To create an instance, you must have an Apsara Stack tenant account or a Resource Access Management (RAM) user who has administrative permissions. The RAM user must have the  `AliyunRDCFullAccess`  policy.

1. Create an Apsara DevOps Enterprise Edition instance.

   <ol type="i">

   <li>

   Log in to the  `Apsara DevOps console`  and click Enterprise Edition in the menu bar.

   </li>

   <li>

   Click to go to the buy page and specify the following parameters:

   - Region: Select a region for the instance.

   - Purchase Method: Select New Instance Purchase.

   - Instance Name: the name of the Enterprise Edition instance. The name can contain letters, digits, and hyphens (-).

   - Instance Identity: A public or private endpoint is automatically generated based on the instance identity. For security reasons, Internet and private network access are disabled by default when the instance is created. You must configure network access on the instance details page after the instance is created.

   - Specifications: The default edition is Enterprise Edition, which cannot be modified.

   - Number of Licenses: By default, the minimum number of licenses is 100. You can add more licenses based on your business requirements.

   - Subscription Duration: Select a subscription duration. You can select 1 month, 3 months, 6 months, 1 year, 2 years, or 3 years.

   - root Account Password: The initial password for the root account to log in to the Enterprise Edition instance. You can change the password on the instance details page.

   </li>

   <li>

   After you make the purchase, go back to the console. If the Enterprise Edition instance is

   </li>

   </ol>

   not displayed, refresh the page. The status of the Enterprise Edition instance is displayed in the Enterprise Edition instance list.

2. Configure the network.

   > **Note**
   >
   > For security reasons, Internet and private network access are disabled by default after an Enterprise Edition instance is created. You need to configure network settings after the instance status changes to In Use.

   <ol type="i">

   <li>

   Select the Enterprise Edition instance and click **Name/Enterprise ID** to view its details, including the current network status.

   </li>

   <li>

   In the Access Network Configuration section, click **Go to Modify**.

   </li>

   <li>

   On the Network Configuration tab, click **Modify Configuration**. Select **Use Public**

   </li>

   </ol>

   **Network Access** or **Use VPC Access**.

   <ol type="a">

   <li>

   Configure access to the Internet

   <ol type="a">

   <li>

   Select Use Public Network Access.

   </li>

   <li>

   For security reasons, you must configure an IP address whitelist when you enable Internet access.

   | Example | Description |
   | --- | --- |
   | 127.0.0.1 | Allows access only from the local host. |
   | 0.0.0.0/0 | Allows access from all IP addresses. |
   | 10.10.10.0/24. | Allows access only from 10.10.10.0/24. |

   > **Note**
   >
   > To add multiple IP addresses, separate them with commas (,). Do not add spaces before or after the commas (,). The Internet whitelist supports a maximum of 20 IP addresses or CIDR blocks. The configurations take effect after about 5 minutes.

   </li>

   </ol>

   </li>

   <li>

   Configure network access over a VPC

   <ol type="a">

   <li>

   Select Use VPC Access.

   </li>

   <li>

   Create an endpoint: If no endpoint is available, configure the parameters to create one. If you do not have permissions to configure a virtual private cloud (VPC), grant the required permissions as prompted.

   </li>

   </ol>

   </li>

   </ol>

3. After you complete the network settings, find the Enterprise Edition instance and click **Enter Enterprise** in the Actions column.

4. You are redirected to the AI Coding Assistant Lingma login page. Enter the login  `username and password`  and click **Log In**.

**Step 3: Bind the OIDC application to IDaaS**

Enterprise administrators can configure and manage OIDC integration configurations on the **Third-party Integration** page. In the OIDC section, click Add Configuration.

1. Configure an OIDC client.

   <ol type="i">

   <li>

   **Redirect URIs**: Add the URI to the OIDC application created in IDaaS.

   </li>

   <li>

   **Client ID**: Enter the client_id obtained in Step 1 on the General tab.

   </li>

   <li>

   **Client Secret**: Enter the client_secret obtained in Step 1 on the General tab.

   </li>

   <li>

   **Issuer URL**: Enter the issuer obtained in Step 1 in the Application Settings section.

   </li>

   </ol>

   Click **Next**.

2. Bind accounts and map attributes.

   <ol type="i">

   <li>

   **Unique Account Identifier**: Enter the OIDC user attribute that uniquely identifies the account. The user attribute cannot be modified after this configuration is submitted.

   </li>

   <li>

   **Account Binding Method**: Four account binding methods are available:

   - Automatically bind accounts with the same email address.

   - Automatically bind accounts with the same login account.

   - Automatically bind accounts with the same phone number.

   - Automatically bind accounts with the same employee ID.

   Make sure that the attribute field for the selected method is unique and exists. AI Coding Assistant Lingma uses this field to match accounts. The following figure shows an example of automatically binding accounts that use the same email address:

   <ol type="i" start="3">

   <li>

   Configure user attribute mapping. Map the required fields, such as Name, Logon Account,

   </li>

   </ol>

   and Mailbox.

   > **Note**
   >
   > The login account and the attribute field used for account binding must be unique and specified.

   </li>

   </ol>

   Click **Next**.

3. Enables the service.

   <ol type="i">

   <li>

   Turn on SSO. After you enable SSO, users can redirect from the AI Coding Assistant Lingma login page to the OIDC login page. Then, users can log in to AI Coding Assistant Lingma through the OIDC application.

   </li>

   <li>

   Modify the OIDC display name and display icon. AI Coding Assistant Lingma displays the

   </li>

   </ol>

   new OIDC display name and icon.

   <ol type="i" start="3">

   <li>

   Advanced Settings: Allow users to create an AI Coding Assistant Tongyi Lingma account

   </li>

   </ol>

   at login. By default, the system prioritizes binding an existing account during login. If you select this option, a new AI Coding Assistant Tongyi Lingma account is created for the user if no existing account can be bound.

   After you complete all configurations, click **Save Configuration**.

   4. **Verify SSO for AI Coding Assistant Tongyi Lingma**

After **SSO** is enabled, the OIDC login option is displayed on the Apsara DevOps login page. After users click the OIDC icon, they are redirected to the OIDC login page. Users whose OIDC accounts are associated with Apsara Stack DevOps accounts can log in to Apsara Stack DevOps by using their OIDC login credentials.
