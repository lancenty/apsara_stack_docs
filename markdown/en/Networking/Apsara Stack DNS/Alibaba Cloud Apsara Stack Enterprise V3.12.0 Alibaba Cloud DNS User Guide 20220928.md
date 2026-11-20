Alibaba Cloud  
Apsara Stack Enterprise  
Alibaba Cloud DNS  
User Guide  
Product Version: V3.12.0  
Document Version: 20220928

**Table of Contents**

- [1.What is Apsara Stack DNS?](#section-1)
- [2.User roles and permissions](#section-2)
- [3.Log on to the Apsara Stack DNS console](#section-3)
- [4.Internal DNS resolution management](#section-4)
    - [4.1. Global internal domain names](#section-4-1)
        - [4.1.1. Overview](#section-4-1-1)
        - [4.1.2. View an internal domain name](#section-4-1-2)
        - [4.1.3. Add a domain name](#section-4-1-3)
        - [4.1.4. Add a description for a domain name](#section-4-1-4)
        - [4.1.5. Delete a domain name](#section-4-1-5)
        - [4.1.6. Delete multiple domain names](#section-4-1-6)
        - [4.1.7. Configure DNS records](#section-4-1-7)
        - [4.1.8. View a resolution policy](#section-4-1-8)
    - [4.2. Global forwarding configurations](#section-4-2)
        - [4.2.1. Global forwarding domain names](#section-4-2-1)
            - [4.2.1.1. Overview](#section-4-2-1-1)
            - [4.2.1.2. View global forwarding domain names](#section-4-2-1-2)
            - [4.2.1.3. Add a domain name](#section-4-2-1-3)
            - [4.2.1.4. Add a description for a domain name](#section-4-2-1-4)
            - [4.2.1.5. Modify the forwarding configurations of a domain name](#section-4-2-1-5)
            - [4.2.1.6. Delete a domain name](#section-4-2-1-6)
            - [4.2.1.7. Delete multiple domain names](#section-4-2-1-7)
        - [4.2.2. Global default forwarding configurations](#section-4-2-2)
            - [4.2.2.1. Enable default forwarding](#section-4-2-2-1)
            - [4.2.2.2. Modify default forwarding configurations](#section-4-2-2-2)
            - [4.2.2.3. Disable default forwarding](#section-4-2-2-3)
    - [4.3. Global recursive resolution](#section-4-3)
        - [4.3.1. Enable global recursive resolution](#section-4-3-1)
        - [4.3.2. Disable global recursive resolution](#section-4-3-2)
- [5.PrivateZone (DNS Standard Edition only)](#section-5)
    - [5.1. Tenant internal domain name](#section-5-1)
        - [5.1.1. View a domain name](#section-5-1-1)
        - [5.1.2. Add a domain name](#section-5-1-2)
        - [5.1.3. Bind an organization to a VPC](#section-5-1-3)
        - [5.1.4. Unbind a domain name from a VPC](#section-5-1-4)
        - [5.1.5. Add a description for a domain name](#section-5-1-5)
        - [5.1.6. Delete a domain name](#section-5-1-6)
        - [5.1.7. Delete multiple domain names](#section-5-1-7)
        - [5.1.8. Configure DNS records](#section-5-1-8)
        - [5.1.9. View a resolution policy](#section-5-1-9)
    - [5.2. Tenant forwarding configurations](#section-5-2)
        - [5.2.1. Tenant forwarding domain names](#section-5-2-1)
            - [5.2.1.1. View a tenant forwarding domain name](#section-5-2-1-1)
            - [5.2.1.2. Add a tenant forwarding domain name](#section-5-2-1-2)
            - [5.2.1.3. Bind an organization to a VPC](#section-5-2-1-3)
            - [5.2.1.4. Unbind a domain name from a VPC](#section-5-2-1-4)
            - [5.2.1.5. Modify the forwarding configurations of a domain name](#section-5-2-1-5)
            - [5.2.1.6. Add a description for a tenant forwarding domain name](#section-5-2-1-6)
            - [5.2.1.7. Delete a tenant forwarding domain name](#section-5-2-1-7)
            - [5.2.1.8. Delete multiple tenant forwarding domain names](#section-5-2-1-8)
        - [5.2.2. Tenant default forwarding configurations](#section-5-2-2)
            - [5.2.2.1. View default forwarding configurations](#section-5-2-2-1)
            - [5.2.2.2. Add a default forwarding configuration](#section-5-2-2-2)
            - [5.2.2.3. Bind an organization to a VPC](#section-5-2-2-3)
            - [5.2.2.4. Unbind a domain name from a VPC](#section-5-2-2-4)
            - [5.2.2.5. Modify a default forwarding configuration](#section-5-2-2-5)
            - [5.2.2.6. Add a default forwarding configuration](#section-5-2-2-6)
            - [5.2.2.7. Delete a default forwarding configuration](#section-5-2-2-7)
            - [5.2.2.8. Delete multiple default forwarding configurations](#section-5-2-2-8)
- [6.Internal Global Traffic Manager (internal GTM Standard Edition only)](#section-6)
    - [6.1. Scheduling instance management](#section-6-1)
        - [6.1.1. Scheduling instances](#section-6-1-1)
            - [6.1.1.1. Create a scheduling instance](#section-6-1-1-1)
            - [6.1.1.2. Modify a scheduling instance](#section-6-1-1-2)
            - [6.1.1.3. Configure a scheduling instance](#section-6-1-1-3)
                - [6.1.1.3.1. Create an access policy for a scheduling instance](#section-6-1-1-3-1)
                - [6.1.1.3.2. Modify the access policy of a scheduling instance](#section-6-1-1-3-2)
                - [6.1.1.3.3. Delete the access policy of a scheduling instance](#section-6-1-1-3-3)
            - [6.1.1.4. Delete a scheduling instance](#section-6-1-1-4)
        - [6.1.2. Address Pool](#section-6-1-2)
            - [6.1.2.1. Create an address pool](#section-6-1-2-1)
            - [6.1.2.2. Modify the configurations of an address pool](#section-6-1-2-2)
            - [6.1.2.3. Delete an address pool](#section-6-1-2-3)
        - [6.1.3. Scheduling Domain](#section-6-1-3)
            - [6.1.3.1. Create a scheduling domain](#section-6-1-3-1)
            - [6.1.3.2. Add a description for a scheduling domain](#section-6-1-3-2)
            - [6.1.3.3. Delete a scheduling domain](#section-6-1-3-3)
    - [6.2. Data synchronization management](#section-6-2)
        - [6.2.1. Data Synchronization Link](#section-6-2-1)
            - [6.2.1.1. Standalone node on the Data Synchronization Link tab](#section-6-2-1-1)
            - [6.2.1.2. Master node on the Data Synchronization Link tab](#section-6-2-1-2)
            - [6.2.1.3. Slave node on the Data Synchronization Link tab](#section-6-2-1-3)
        - [6.2.2. Link Change Messages](#section-6-2-2)

<a id="section-1"></a>

# 1.What is Apsara Stack DNS?

Apsara Stack DNS is a service that runs on Apsara Stack to resolve domain names. You can configure rules to map domain names to IP addresses. Apsara Stack DNS then distributes domain name requests from clients to cloud resources, business systems on your internal networks, or the business resources of Internet service providers (ISPs).

Apsara Stack DNS provides DNS resolution in VPCs. You can perform the following operations on your VPC by using Apsara Stack DNS:

- Access other ECS instances deployed in your VPC.

- Access cloud service instances provided by Apsara Stack.

- Access custom enterprise business systems.

- Access Internet services and businesses.

- Establish network connections between DNS and user-created DNS over a leased line.

- Manage internal domain names.

- Manage DNS records of internal domain names.

- Manage forwarding configurations.

- Manage recursive resolution configurations.

<a id="section-2"></a>

# 2.User roles and permissions

| Role | Permission |
| --- | --- |
| System administrator | A user of this role has read, write, and execute permissions on all level-1 organization resources, global resources, and system configurations. |
| Level-1 organization administrator | A user of this role has read, write, and execute permissions on level-1 organization resources to which the user belongs, but does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Lower-level organization administrator | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Resource user | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Other roles | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |

<a id="section-3"></a>

# 3.Log on to the Apsara Stack DNS console

This topic describes how to log on to the Apsara Stack DNS console by using Google Chrome.

Prerequisites

- Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff.

- We recommend that you use Google Chrome.

Procedure

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.

2. Enter your username and password.

   Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

   Note

   The first time that you log on to the Apsara Uni-manager Management Console,

   you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:

   - Uppercase or lowercase letters

   - Digits

   - Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.

4. In the top navigation bar, choose Products > Networking > Apsara Stack DNS.

<a id="section-4"></a>

# 4.Internal DNS resolution management

Internal DNS resolution management allows you to manage global internal domain names, global forwarding configurations, and global recursive resolution configurations that you have created in Apsara Stack.

<a id="section-4-1"></a>

## 4.1. Global internal domain names

<a id="section-4-1-1"></a>

### 4.1.1. Overview

All the operations of this feature require administrator privileges.

<a id="section-4-1-2"></a>

### 4.1.2. View an internal domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. In the Domain Name search box, enter the domain name that you want to view.

4. Click Search.

   The search result is displayed.

<a id="section-4-1-3"></a>

### 4.1.3. Add a domain name

This topic describes how to add a domain name in the Apsara Stack Cloud Management (ASCM) console.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Click Add Domain Name.

4. In the dialog box that appears, enter Global Internal Domains.

5. Click OK.

<a id="section-4-1-4"></a>

### 4.1.4. Add a description for a domain name

This topic describes how to add a description for a domain name in the Apsara Stack Cloud Management (ASCM) console.

Context

You can add a description for a domain name for easy identification. For example, you can add a hostname or internal system information to describe a domain name.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select

   Description.

4. In the dialog box that appears, enter a description.

5. Click OK.

<a id="section-4-1-5"></a>

### 4.1.5. Delete a domain name

This topic describes how to delete a domain name in the Apsara Stack Cloud Management (ASCM) console.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete.

4. In the message that appears, click OK.

<a id="section-4-1-6"></a>

### 4.1.6. Delete multiple domain names

This topic describes how to delete multiple domain names at a time in the Apsara Stack Cloud Management (ASCM) console.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Select the domain names that you want to delete and click Delete in the upper-right corner.

4. In the message that appears, click OK.

<a id="section-4-1-7"></a>

### 4.1.7. Configure DNS records

This topic describes how to configure DNS records in the Apsara Stack Cloud Management (ASCM) console.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Configure

   DNS Records.

4. In the upper-right corner of the Configure DNS Records page, click Add DNS Record.

5. Perform the following operations as needed:

   - Add a description for a DNS record

     Select the DNS record for which you want to add a description, click <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> in the Actions column,

     and then select Description from the shortcut menu. In the dialog box that appears, enter a description and click OK.

   - Delete a DNS record

     Select the DNS record that you want to delete, click <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> in the Actions column, and then select

     Delete from the shortcut menu. In the message that appears, click OK.

   - Modify a DNS record

     Select the DNS record that you want to modify, click <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> in the Actions column, and then select

     Modify from the shortcut menu. In the dialog box that appears, set the required parameters and click OK.

   - Delete DNS records in batches

     Select the DNS records that you want to delete and click Delete in the upper-right corner. In the message that appears, click OK.

<a id="section-4-1-8"></a>

### 4.1.8. View a resolution policy

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Configure

   DNS Records.

4. On the page that appears, select the domain name for which you want to configure DNS records, and click Weight in the Resolution Policy column.

5. On the page that appears, view the details of Resolution Policy.

<a id="section-4-2"></a>

## 4.2. Global forwarding configurations

<a id="section-4-2-1"></a>

### 4.2.1. Global forwarding domain names

<a id="section-4-2-1-1"></a>

#### 4.2.1.1. Overview

All operations on global forwarding domain names require system administrator permissions.

Apsara Stack DNS forwards specific domain names to other DNS servers for resolution.

Apsara Stack DNS can forward requests with or without recursion.

- In the mode of forwarding without recursion, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails.

- In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used.

<a id="section-4-2-1-2"></a>

#### 4.2.1.2. View global forwarding domain names

This topic describes how to view forwarding domain names in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Forwarding Domains.

3. In the Domain Name search box, enter the target domain name and click Search.

<a id="section-4-2-1-3"></a>

#### 4.2.1.3. Add a domain name

This topic describes how to add a domain name in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Forwarding Domains.

3. Click Add Domain Name.

4. In the dialog box that appears, configure parameters such as *Domain Name*, *Forwarding Mode*, and *Forwarder IP Addresses*. Then, click OK.

<a id="section-4-2-1-4"></a>

#### 4.2.1.4. Add a description for a domain name

This topic describes how to add a description for a domain name in the ASCM console. This operation requires administrator privileges.

Context

You can add a description for a domain name for identification. For example, you can describe a domain name by using a hostname or internal system information.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Global Forwarding Settings > Global Forwarding Domains.

3. Select the domain name for which you want to add a description, click <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> in the Actions column,

   and then select Description from the shortcut menu.

4. In the dialog box that appears, enter a description and click OK.

<a id="section-4-2-1-5"></a>

#### 4.2.1.5. Modify the forwarding configurations of a domain name

This topic describes how to modify the forwarding configurations of a domain name in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Modify.

4. In the dialog box that appears, change the value of *Forwarding Mode* or *Forwarder IP Addresses*, and click OK.

<a id="section-4-2-1-6"></a>

#### 4.2.1.6. Delete a domain name

This topic describes how to delete a domain name in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete.

4. In the message that appears, click OK.

<a id="section-4-2-1-7"></a>

#### 4.2.1.7. Delete multiple domain names

This topic describes how to delete multiple domain names at a time in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Forwarding Domains.

3. Select one or more domain names that you want to delete and click Delete in the upper-right corner of the domain name list.

4. In the message that appears, click OK.

<a id="section-4-2-2"></a>

### 4.2.2. Global default forwarding configurations

<a id="section-4-2-2-1"></a>

#### 4.2.2.1. Enable default forwarding

This topic describes how to enable default forwarding in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Default Forwarding.

3. Click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column and select Enable.

4. In the dialog box that appears, configure *Forwarding Mode* and *Forwarder IP Addresses*. Then, click OK.

   Make sure that Enable Default Forwarding is set to ON.

<a id="section-4-2-2-2"></a>

#### 4.2.2.2. Modify default forwarding configurations

This topic describes how to modify default forwarding configurations in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Default Forwarding.

3. Click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column and select Modify.

4. In the dialog box that appears, configure *Forwarding Mode* and *Forwarder IP Addresses*. Then, click OK.

<a id="section-4-2-2-3"></a>

#### 4.2.2.3. Disable default forwarding

This topic describes how to disable default forwarding in the Apsara Stack Cloud Management (ASCM) console. This operation requires administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Internal Domains > Global Forwarding Settings > Global Default Forwarding.

3. Click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column and select Disable.

4. In the message that appears, click OK.

<a id="section-4-3"></a>

## 4.3. Global recursive resolution

<a id="section-4-3-1"></a>

### 4.3.1. Enable global recursive resolution

Prerequisites

You have administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. Choose Internal Domains > Global Recursive Resolution.

3. Click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column and select Enable.

4. In the dialog box that appears, click OK.

<a id="section-4-3-2"></a>

### 4.3.2. Disable global recursive resolution

Prerequisites

You have administrator permissions.

Procedure

1. Log on to the Apsara Stack DNS console.

2. Choose Internal Domains > Global Recursive Resolution.

3. Click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column and select Disable.

4. In the dialog box that appears, click OK.

<a id="section-5"></a>

# 5.PrivateZone (DNS Standard Edition only)

The PrivateZone feature allows you to create VPC-specific tenant domain names. You can bind the domain names to VPCs as required to achieve tenant isolation.

<a id="section-5-1"></a>

## 5.1. Tenant internal domain name

<a id="section-5-1-1"></a>

### 5.1.1. View a domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. In the Domain Name search box, enter the domain name that you want to view.

4. Click Search.

   The search result is displayed.

<a id="section-5-1-2"></a>

### 5.1.2. Add a domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Click Add Domain Name.

4. In the dialog box that appears, set *Tenant Internal Domain Name*.

5. Click OK.

<a id="section-5-1-3"></a>

### 5.1.3. Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. To ensure that the DNS forwarding configurations take effect, you must bind the organization of domain names to a VPC.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and select Associate VPCs.

4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to the list of VPCs Selected, and then click OK.

<a id="section-5-1-4"></a>

### 5.1.4. Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name and click the number in the VPCs Associated column.

4. On the VPCs Associated page, find the target VPC, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and

   then select Disassociate.

   Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

<a id="section-5-1-5"></a>

### 5.1.5. Add a description for a domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select

   Description.

4. In the dialog box that appears, enter a description.

5. Click OK.

<a id="section-5-1-6"></a>

### 5.1.6. Delete a domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete.

4. In the message that appears, click OK.

<a id="section-5-1-7"></a>

### 5.1.7. Delete multiple domain names

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Select one or more domain names that you want to delete and click Delete in the upper-right corner.

4. In the message that appears, click OK.

<a id="section-5-1-8"></a>

### 5.1.8. Configure DNS records

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Configure

   DNS Records.

4. In the upper-right corner of the Configure DNS Records page, click Add DNS Record.

5. In the Add DNS Record dialog box, configure *Host*, *Type*, *TTL*, *Resolution Policy*, and *Record Set*. Then, click OK.

   The following tables describe the types of DNS records.

   - A record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique IPv4 addresses, each in a separate row.<br>Make sure that the IPv4 addresses are valid.<br>Example:<br>• 192.168.1.1<br>• 192.168.1.2<br>• 192.168.1.3 |
     | Weight | You can enter up to 100 unique IPv4 addresses, each in a separate row.<br>Format:<br>• \[IPv4 address\] \[Weight\] (The IPv4 address and weight are separated with a space.)<br>• Make sure that the IPv4 addresses are valid.<br>• The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight.<br>Example:<br>• 192.168.1.1 20<br>• 192.168.1.1 30<br>• 192.168.1.1 50 |

   - AAAA record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique IPv6 addresses, each in a separate row.<br>Make sure that the IPv6 addresses are valid.<br>Example:<br>• 2400:3200::6666<br>• 2400:3200::6688<br>• 2400:3200::8888 |
     | Weight | You can enter up to 100 unique IPv6 addresses, each in a separate row.<br>Format:<br>• \[IPv6 address\] \[Weight\] (The IPv6 address and weight are separated with a space.)<br>• Make sure that the IPv6 addresses are valid.<br>• The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight.<br>Example:<br>• 2400:3200::6666 20<br>• 2400:3200::6688 20<br>• 2400:3200::8888 60 |

   - CNAME record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter only one domain name.<br>The domain name must be a fully qualified domain name (FQDN) that ends with a dot (.). It must be 1 to 255 characters in length.<br>Example: www.example.com. |
     | Weight | You can enter up to 100 unique domain names, each in a separate row.<br>Format:<br>• \[Domain name\] \[Weight\] (The domain name and weight are separated with a space.)<br>• The domain name must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length.<br>• The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight.<br>Example:<br>• www1.example.com. 20<br>• www2.example.com. 20<br>• www3.example.com. 60 |

   - MX record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter 100 unique email server hostnames, each in a separate row.<br>Format:<br>• \[Priority\] \[Email server hostname\] (The priority and hostname are separated with a space.)<br>• The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority.<br>• The email server hostname must be an FQDN that ends with a period (.).It must be 1 to 255 characters in length.<br>Example:<br>• 10 mailserver1.example.com.<br>• 20 mailserver2.example.com. |

   - TXT record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique character strings, each in a separate row.<br>A string must be 1 to 255 characters in length. No row can be left blank.<br>Example: "v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all" |

   - PTR record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique domain names, each in a separate row.<br>The DNS server address must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length.<br>Example:<br>• www1.example.com.<br>• www2.example.com.<br>• www3.example.com. |

   - SRV record

     <table>
       <tr>
         <td>Resolution policy</td>
         <td>Formatting rule</td>
       </tr>
     </table>

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique application server hostnames, each in a separate row.<br>Format:<br>• \[Priority\] \[Weight\] \[Port number\] \[Application server hostname\] (Every two items are separated with a space.)<br>• The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority.<br>• The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight.<br>• The port number is an integer ranging from 0 to 65535. It indicates the TCP or UDP port used for network communications.<br>• The application server hostname must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length.<br>Example:<br>• 1 10 8080 www1.example.com.<br>• 2 20 8081 www2.example.com. |

   - NAPTR record

     <table>
       <tr>
         <td>Resolution policy</td>
         <td>Formatting rule</td>
       </tr>
     </table>

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique NAPTR record values, each in a separate row.<br>Format:<br>• \[Serial number\] \[Priority\] \[Flag\] \[Service information\] \[Regular expression\] \[Substitute domain name\] (Every two items are separated with a space.)<br>• The serial number is an integer ranging from 0 to 999. A smaller value indicates a higher priority.<br>• The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority. If two records have the same serial number, the one with a higher priority takes effect first.<br>• The flag value can be left blank or be a character from A to Z, a to z, or 0 to 9. It is not case-sensitive and must be enclosed in double quotation marks ("").<br>• The service information can be left blank or be a string of 1 to 32 characters. It must start with a letter and be enclosed in double quotation marks ("").<br>• The regular expression can be left blank or be a string of 1 to 255 characters enclosed in double quotation marks ("").<br>• The substitute domain name must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length.<br>Example:<br>• 100 50 "S" "Z3950+I2L+I2C" "" _z3950._tcp.example.com.<br>• 100 50 "S" "RCDS+I2C" "" _rcds._udp.example.com.<br>• 100 50 "S" "HTTP+I2L+I2C+I2R" "" _http._tcp.example.com. |

   - CAA record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique CAA records, each in a separate row.<br>Format:<br>• \[Certificate authority flag\] \[Certificate property tag\] \[Authorization information\] (Every two items are separated with a space.)<br>• The certification authority flag is an integer ranging from 0 to 255.<br>• The certificate property tag can be issue, issuewild, or iodef.<br>• The authorization information must be 1 to 255 characters in length and enclosed in double quotation marks ("").<br>Example:<br>• 0 issue "caa.example.com"<br>• 0 issuewild ";"<br>• 0 iodef "mailto:example@example.com" |

   - NS record

     | Resolution policy | Formatting rule |
     | --- | --- |
     | None | You can enter up to 100 unique DNS server addresses, each in a separate row.<br>The DNS server address must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Wildcard domain names are not allowed.<br>Example:<br>• ns1.example.com.<br>• ns2.example.com. |

6. After you add DNS records, perform the following operations as required:

   - Add a description for a DNS record.

     Find the target DNS record, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select

     Description. In the dialog box that appears, enter a description and click OK.

   - Delete a DNS record.

     Find the target DNS record, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete. In

     the message that appears, click OK.

   - Modify a DNS record.

     Find the target DNS record, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Modify. In

     the dialog box that appears, modify the required parameters and click OK.

   - Delete multiple DNS records.

     Select the DNS records that you want to modify and click Delete in the upper-right corner. In the message that appears, click OK.

<a id="section-5-1-9"></a>

### 5.1.9. View a resolution policy

This topic describes how to view the details of a resolution policy.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Internal Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Configure

   DNS Records.

4. View the resolution policy in the DNS Records list.

<a id="section-5-2"></a>

## 5.2. Tenant forwarding configurations

<a id="section-5-2-1"></a>

### 5.2.1. Tenant forwarding domain names

<a id="section-5-2-1-1"></a>

#### 5.2.1.1. View a tenant forwarding domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. In the Domain Name search box, enter the domain name that you want to view.

4. Click Search.

   The search result is displayed.

<a id="section-5-2-1-2"></a>

#### 5.2.1.2. Add a tenant forwarding domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Click Add Domain Name.

4. In the dialog box that appears, configure parameters such as *Domain Name*, *Forwarding Mode*, and *Forwarder IP Addresses*.

   | Parameter | Description |
   | --- | --- |
   | Domain Name | The domain name, which must meet the following formatting rules:<br>• The domain name must be 1 to 255 characters in length. This includes the period (.) at the end of the domain name.<br>• The domain name can contain multiple domain name segments that are separated with periods (.). A domain name segment must be 1 to 63 characters in length. It cannot contain consecutive periods (.) or be left blank.<br>• The domain name can only contain letters (a to z, A to Z), digits (0 to 9), hyphens (-), and underscores (_).<br>• The domain name must start with a letter, digit, or underscore (_) and end with a letter, digit, or period (.).<br>• The domain name is not case-sensitive. The system saves the domain name in lowercase letters.<br>• The period (.) at the end of the domain name is optional. The system adds a period (.) to the end of the domain name. |
   | Forwarding Mode | For both domain name-based forwarding and default forwarding, the following two forwarding modes are supported:<br>• Forward All Requests without Recursion: forwards DNS requests to the target DNS server. If the target DNS server cannot resolve the domain names, a message is returned to the DNS client indicating that the query failed.<br>• Forward All Requests with Recursion: A specified DNS server is preferentially used to resolve domain names. If the specified DNS server cannot resolve the domain names, the local DNS is used instead. If you enter internal IP addresses in the Forwarder IP Addresses field, unexpected results may occur during recursive resolution. For example, a domain name used for internal network services may be resolved to a public IP address. |
   | Forwarder IP Addresses | A list of destination IP addresses.<br>Note Multiple IP addresses are separated with semicolons (;). |

5. Click OK.

<a id="section-5-2-1-3"></a>

#### 5.2.1.3. Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. You must bind the organization of domain names to a VPC before the DNS forwarding configurations can take effect.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Associate

   VPCs.

4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to the list of VPCs Selected, and then click OK.

<a id="section-5-2-1-4"></a>

#### 5.2.1.4. Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Find the target domain name and click the number in the VPCs Associated column.

4. On the VPCs Associated page, find the target VPC, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and

   then select Disassociate.

   Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

<a id="section-5-2-1-5"></a>

#### 5.2.1.5. Modify the forwarding configurations of a domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Modify.

4. In the dialog box that appears, change the value of Forwarding Mode or Forwarder IP Addresses.

5. Click OK.

<a id="section-5-2-1-6"></a>

#### 5.2.1.6. Add a description for a tenant forwarding domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select

   Description.

4. In the dialog box that appears, enter a description.

5. Click OK.

<a id="section-5-2-1-7"></a>

#### 5.2.1.7. Delete a tenant forwarding domain name

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Find the target domain name, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete.

4. In the message that appears, click OK.

<a id="section-5-2-1-8"></a>

#### 5.2.1.8. Delete multiple tenant forwarding domain names

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Forwarding Domains.

3. Select one or more domain names that you want to delete and click Delete in the upper-right corner.

4. In the message that appears, click OK.

<a id="section-5-2-2"></a>

### 5.2.2. Tenant default forwarding configurations

<a id="section-5-2-2-1"></a>

#### 5.2.2.1. View default forwarding configurations

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

<a id="section-5-2-2-2"></a>

#### 5.2.2.2. Add a default forwarding configuration

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Click Add Settings.

4. In the dialog box that appears, configure parameters such as *Forwarding Mode* and *Forwarder IP A ddresses*.

   | Parameter | Description |
   | --- | --- |
   | Forwarding Mode | For both domain name-based forwarding and default forwarding, the following two forwarding modes are available:<br>• Forward All Requests without Recursion: Only a specified DNS server is used to resolve domain names. If the specified DNS server cannot resolve the domain names, a message is returned to the DNS client to indicate that the query failed.<br>• Forward All Requests with Recursion: A specified DNS server is preferentially used to resolve domain names. If the specified DNS server cannot resolve the domain names, a local DNS server is used instead. If you enter internal IP addresses in the Forwarder IP Addresses field, unexpected results may occur during recursive resolution. For example, a domain name used for internal network services may be resolved to a public IP address. |
   | Forwarder IP Addresses | A list of destination IP addresses.<br>Note Multiple IP addresses are separated with semicolons (;). |

5. Click OK.

<a id="section-5-2-2-3"></a>

#### 5.2.2.3. Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. You must bind the organization of domain names to a VPC before the DNS forwarding configurations can take effect.

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Find the target organization, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Associate

   VPCs.

4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to the list of VPCs Selected, and then click OK.

<a id="section-5-2-2-4"></a>

#### 5.2.2.4. Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Find the target domain name and click the number in the VPCs Associated column.

4. On the VPCs Associated page, find the target VPC, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and

   then select Disassociate.

   Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

<a id="section-5-2-2-5"></a>

#### 5.2.2.5. Modify a default forwarding configuration

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Find the target organization, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Modify.

4. In the dialog box that appears, change the value of Forwarding Mode or Forwarder IP Addresses.

5. Click OK.

<a id="section-5-2-2-6"></a>

#### 5.2.2.6. Add a default forwarding configuration

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Find the target organization, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select

   Description.

4. In the dialog box that appears, enter Description.

5. Click OK.

<a id="section-5-2-2-7"></a>

#### 5.2.2.7. Delete a default forwarding configuration

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Find the target organization, click the <img src="assets/1ac4c6a56b9f77d1e8198f228aa1ea94.png" width="25" alt=""> icon in the Actions column, and then select Delete.

4. In the dialog box that appears, click OK.

<a id="section-5-2-2-8"></a>

#### 5.2.2.8. Delete multiple default forwarding configurations

Prerequisites

You have the permissions of a system administrator or level-1 organization administrator.

Procedure

1. Log on to the Apsara Stack DNS console.

2. In the left-side navigation pane, choose Forwarding Configurations > Tenant Forwarding Settings > Tenant Default Forwarding.

3. Select one or more domain names that you want to delete and click Delete in the upper-right corner.

4. In the message that appears, click OK.

<a id="section-6"></a>

# 6.Internal Global Traffic Manager (internal GTM Standard Edition only)

Internal Global Traffic Manager (GTM) supports multi-cloud disaster recovery for domain names of customers. This feature manages traffic loads between multiple Apsara Stack networks.

<a id="section-6-1"></a>

## 6.1. Scheduling instance management

<a id="section-6-1-1"></a>

### 6.1.1. Scheduling instances

The Scheduling Instance page displays all existing scheduling instances. You can create, delete, modify, and configure scheduling instances on this page. You must associate an address pool and a scheduling domain with the instance.

<a id="section-6-1-1-1"></a>

#### 6.1.1.1. Create a scheduling instance

After you create a scheduling instance, you can associate the scheduling instance with a scheduling domain and address pool.

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Instance.

2. Click Create Scheduling Instance in the upper-right corner of the list.

3. In the dialog box that appears, enter information of the scheduling instance and click OK.

<a id="section-6-1-1-2"></a>

#### 6.1.1.2. Modify a scheduling instance

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Instance.

2. Find the target instance and click Modify in the Actions column.

3. Modify the configurations of the instance and click OK.

<a id="section-6-1-1-3"></a>

#### 6.1.1.3. Configure a scheduling instance

This topic describes how to add and delete a scheduling instance and modify the configurations of a scheduling instance.

<a id="section-6-1-1-3-1"></a>

##### 6.1.1.3.1. Create an access policy for a scheduling instance

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Instance. Find the target scheduling instance and click Configure in the Actions column. On the Access Policy Configuration page, click Create Access Policy in the upper-right corner of the page.

2. In the dialog box that appears, enter the required information and click OK.

<a id="section-6-1-1-3-2"></a>

##### 6.1.1.3.2. Modify the access policy of a scheduling instance

1. On the Access Policy Configuration page, find the target access policy and click Modify in the Actions

column.

2. In the dialog box that appears, modify the configurations and click OK.

<a id="section-6-1-1-3-3"></a>

##### 6.1.1.3.3. Delete the access policy of a scheduling instance

1. On the Access Policy Configuration page, find the target access policy and click Delete in the Actions

column.

2. In the dialog box that appears, click OK after you verify that the displayed information is correct.

<a id="section-6-1-1-4"></a>

#### 6.1.1.4. Delete a scheduling instance

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Instance.

2. Find the target instance and click Delete in the Actions column.

3. In the dialog box that appears, click OK.

Note: After you delete the instance, its configuration data is also deleted.

<a id="section-6-1-2"></a>

### 6.1.2. Address Pool

The Address Pool tab allows you to manage address pools. The address pools are classified into three types: IPv4 address pool, IPv6 address pool, and CNAME address pool. You can associate a new scheduling instance with a specific address pool. You can also add weights to address pools.

<a id="section-6-1-2-1"></a>

#### 6.1.2.1. Create an address pool

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Address Pool.

2. Click Create Address Pool in the upper-right corner of the address pool list.

3. In the dialog box that appears, enter information of the address pool and click OK.

<a id="section-6-1-2-2"></a>

#### 6.1.2.2. Modify the configurations of an address pool

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Address Pool.

2. Find the target address pool and click Modify in the Actions column.

3. In the dialog box that appears, modify the configurations and click OK.

<a id="section-6-1-2-3"></a>

#### 6.1.2.3. Delete an address pool

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Address Pool.

2. Find the target address pool and click Delete in the Actions column.

3. In the dialog box that appears, click OK after you verify that the displayed information is correct.

<a id="section-6-1-3"></a>

### 6.1.3. Scheduling Domain

The Scheduling Domain tab allows you to add, delete, modify, and query scheduling domains.

You can log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances > Scheduling Domain to view the scheduling domain list.

<a id="section-6-1-3-1"></a>

#### 6.1.3.1. Create a scheduling domain

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Domain. Then, click Create Scheduling Domain in the upper-right corner of the scheduling domain list.

2. In the dialog box that appears, enter the custom domain name and click OK.

<a id="section-6-1-3-2"></a>

#### 6.1.3.2. Add a description for a scheduling domain

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Domain.

2. Find the target scheduling domain and click Edit in the Actions column.

3. In the dialog box that appears, add a description in the Edit field and click OK.

<a id="section-6-1-3-3"></a>

#### 6.1.3.3. Delete a scheduling domain

1. Log on to the Apsara Stack DNS console and choose Recursion Configurations > Scheduling Instances

> Scheduling Domain.

2. Find the target scheduling domain and click Delete in the Actions column.

3. In the dialog box that appears, click OK after you verify that the displayed information is correct.

<a id="section-6-2"></a>

## 6.2. Data synchronization management

Data synchronization management is used to synchronize Global Traffic Manager (GTM) data between clouds.

<a id="section-6-2-1"></a>

### 6.2.1. Data Synchronization Link

The Data Synchronization Link tab displays local system information, information of the cluster nodes between which data synchronization has been established, and their primary/secondary relationships.

<a id="section-6-2-1-1"></a>

#### 6.2.1.1. Standalone node on the Data Synchronization Link tab

Services can be switched over between Global Traffic Manager (GTM) nodes. If GTM is deployed in standalone mode, you must add slave nodes because two or more nodes are required for a switchover.

1. On the Data Synchronization Link tab, click Add Slave Node in the Data Synchronization Cluster

section.

2. In the dialog box that appears, enter two IP addresses of the slave node that you want to add. Enter

one IP address in each row.

3. Click OK. Then, wait for the confirmation of the slave node.

<a id="section-6-2-1-2"></a>

#### 6.2.1.2. Master node on the Data Synchronization Link tab

You can switch the master node to the slave node and add slave nodes for the master node.

1. To add a slave node, click Add Slave Node in the Data Synchronization Cluster section on the Data

Synchronization Link tab.

2. To switch the master node to the slave node, click Switch to Slave.

3. In the dialog box that appears, click OK after you verify that the displayed information is correct.

<a id="section-6-2-1-3"></a>

#### 6.2.1.3. Slave node on the Data Synchronization Link tab

You can switch the standalone node to the slave node or the master node.

<a id="section-6-2-2"></a>

### 6.2.2. Link Change Messages

The Link Change Messages tab displays the status of each node in a Global Traffic Manager (GTM) cluster, which can be To Be Processed, Accepted, or Rejected.

You can log on to the Apsara Stack DNS console and choose Recursion Configurations > Data Synchronization > Link Change Messages to view the status of each cluster node.

The Link Change Messages tab displays the node status and the link change messages of the following node types:

Standalone node

Master node

Slave node
