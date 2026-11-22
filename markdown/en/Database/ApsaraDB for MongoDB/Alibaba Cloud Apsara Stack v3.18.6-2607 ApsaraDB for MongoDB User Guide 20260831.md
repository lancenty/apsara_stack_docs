Alibaba Cloud  
Apsara Stack  
ApsaraDB for MongoDB  
User Guide  
Product Version: v3.18.6-2607  
Document Version: 20260831

**Table of Contents**

- [1.Kernel version release notes](#section-1)
- [2.Precautions](#section-2)
- [3.Log in to the ApsaraDB for MongoDB console](#section-3)
- [4.Instance types](#section-4)
    - [4.1. Replica set instance types](#section-4-1)
    - [4.2. Sharded cluster instance types](#section-4-2)
- [5.Quick start](#section-5)
    - [5.1. Use ApsaraDB for MongoDB](#section-5-1)
    - [5.2. Create an instance](#section-5-2)
        - [5.2.1. Create a replica set instance](#section-5-2-1)
        - [5.2.2. Create a sharded cluster instance](#section-5-2-2)
    - [5.3. Reset a password](#section-5-3)
    - [5.4. Configure a whitelist](#section-5-4)
    - [5.5. Connect to an instance](#section-5-5)
        - [5.5.1. Use DMS to log on to an ApsaraDB for MongoDB instance](#section-5-5-1)
        - [5.5.2. Use the mongo shell to connect to an ApsaraDB for MongoDB instance](#section-5-5-2)
        - [5.5.3. Introduction to connection strings and URIs](#section-5-5-3)
            - [5.5.3.1. Overview of replica set instance connections](#section-5-5-3-1)
            - [5.5.3.2. Overview of sharded cluster instance connections](#section-5-5-3-2)
- [6.Instance management](#section-6)
    - [6.1. Create an instance](#section-6-1)
        - [6.1.1. Create a replica set instance](#section-6-1-1)
        - [6.1.2. Create a sharded cluster instance](#section-6-1-2)
    - [6.2. View the details of an ApsaraDB for MongoDB instance](#section-6-2)
    - [6.3. Restart an instance](#section-6-3)
    - [6.4. Change the configurations of a replica set instance](#section-6-4)
    - [6.5. Change the configurations of a sharded cluster instance](#section-6-5)
        - [6.5.1. Add a mongos node](#section-6-5-1)
        - [6.5.2. Add a shard node](#section-6-5-2)
        - [6.5.3. Change the configurations of one or more mongos nodes](#section-6-5-3)
        - [6.5.4. Change shard node configurations](#section-6-5-4)
        - [6.5.5. Change the configurations of a Configserver node](#section-6-5-5)
    - [6.6. Change the name of an instance](#section-6-6)
    - [6.7. Upgrade the MongoDB version of an instance](#section-6-7)
    - [6.8. Switch node roles](#section-6-8)
    - [6.9. Migrate an instance across multiple zones](#section-6-9)
    - [6.10. Release an ApsaraDB for MongoDB instance](#section-6-10)
    - [6.11. Primary/secondary failover](#section-6-11)
        - [6.11.1. Configure a primary/secondary switchover for a replica set instance](#section-6-11-1)
        - [6.11.2. Configure a primary/secondary failover for a sharded cluster instance](#section-6-11-2)
    - [6.12. View monitoring data](#section-6-12)
    - [6.13. Recycle bin](#section-6-13)
- [7.Account management](#section-7)
    - [7.1. Create an account](#section-7-1)
    - [7.2. Reset the password](#section-7-2)
    - [7.3. Lock an account](#section-7-3)
- [8.Parameter configuration](#section-8)
    - [8.1. Set instance parameters](#section-8-1)
    - [8.2. Use parameter templates](#section-8-2)
- [9.Backup and restoration](#section-9)
    - [9.1. Data backup](#section-9-1)
        - [9.1.1. Configure automatic backup](#section-9-1-1)
        - [9.1.2. Manually back up an ApsaraDB for MongoDB instance](#section-9-1-2)
    - [9.2. Download a backup file](#section-9-2)
    - [9.3. Data restoration](#section-9-3)
        - [9.3.1. Restore backup data to a new ApsaraDB for MongoDB instance by point in time](#section-9-3-1)
        - [9.3.2. Restore backup data to a new ApsaraDB for MongoDB instance by backup point](#section-9-3-2)
        - [9.3.3. Restore data to the current ApsaraDB for MongoDB instance](#section-9-3-3)
- [10.Cloud Monitor](#section-10)
    - [10.1. View performance metrics](#section-10-1)
    - [10.2. Alert history](#section-10-2)
    - [10.3. Alert rules](#section-10-3)
        - [10.3.1. Create an alert rule](#section-10-3-1)
        - [10.3.2. Manage alert rules](#section-10-3-2)
- [11.Database connections](#section-11)
    - [11.1. Modify a public or internal endpoint of an ApsaraDB for MongoDB instance](#section-11-1)
    - [11.2. Use DMS to log on to an ApsaraDB for MongoDB instance](#section-11-2)
    - [11.3. Use the mongo shell to connect to an ApsaraDB for MongoDB instance](#section-11-3)
    - [11.4. Apply for a public endpoint](#section-11-4)
    - [11.5. Release a public endpoint](#section-11-5)
    - [11.6. Apply for an endpoint for a shard or ConfigServer node](#section-11-6)
    - [11.7. Release the connection string of a shard or Configserver node](#section-11-7)
    - [11.8. Overview of replica set instance connections](#section-11-8)
    - [11.9. Overview of sharded cluster instance connections](#section-11-9)
- [12.Data security](#section-12)
    - [12.1. Configure a whitelist for an ApsaraDB for MongoDB instance](#section-12-1)
    - [12.2. Create or delete a whitelist](#section-12-2)
    - [12.3. Enable the audit log feature](#section-12-3)
    - [12.4. Configure SSL encryption](#section-12-4)
    - [12.5. Configure TDE for an ApsaraDB for MongoDB instance](#section-12-5)
    - [12.6. Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode](#section-12-6)
- [13.Tag management](#section-13)
    - [13.1. Add or create tags](#section-13-1)
    - [13.2. Filter instances by tag](#section-13-2)
    - [13.3. Remove or delete a tag](#section-13-3)
- [14.Zone-disaster recovery](#section-14)
    - [14.1. Create a dual-zone replica set instance](#section-14-1)
    - [14.2. Create a dual-zone sharded cluster instance](#section-14-2)
- [15.AI capability](#section-15)
    - [15.1. One-click migration](#section-15-1)
        - [15.1.1. Migrate data between MongoDB databases](#section-15-1-1)
    - [15.2. AI-native MCP service](#section-15-2)
- [16.CloudDBA](#section-16)
    - [16.1. Quick diagnostics](#section-16-1)
    - [16.2. Performance trends](#section-16-2)
    - [16.3. Real-time performance](#section-16-3)
    - [16.4. Session management](#section-16-4)
    - [16.5. Storage analysis](#section-16-5)
    - [16.6. Slow query logs](#section-16-6)
- [17.Appendix](#section-17)
    - [17.1. Authorize a tenant organization to access SLB](#section-17-1)

<a id="section-1"></a>

# 1.Kernel version release notes

This topic describes the kernel version releases of ApsaraDB for MongoDB.

> **Note**
>
> For detailed updates and version differences, see the **ApsaraDB RDS** section in ***Hotfix Version Release Notes***.

v3.18.6r-rds-hotfeature-SP006 provides the following latest kernel versions for ApsaraDB for MongoDB:

<table>
  <tr>
    <th>Product</th>
    <th>Version</th>
    <th>Minor kernel version</th>
    <th>Build time</th>
  </tr>
  <tr>
    <td rowspan="9">MongoDB</td>
    <td>8.0</td>
    <td>9.0.10</td>
    <td>20260519</td>
  </tr>
  <tr>
    <td>7.0</td>
    <td>8.0.16</td>
    <td>20260514</td>
  </tr>
  <tr>
    <td>6.0</td>
    <td>7.0.26</td>
    <td>20260514</td>
  </tr>
  <tr>
    <td>5.0</td>
    <td>6.0.25</td>
    <td>20260514</td>
  </tr>
  <tr>
    <td>4.2</td>
    <td>4.0.36</td>
    <td>20260416</td>
  </tr>
  <tr>
    <td>4.0</td>
    <td>3.0.45</td>
    <td>20260518</td>
  </tr>
  <tr>
    <td>3.6</td>
    <td>2.0.4</td>
    <td>20181212</td>
  </tr>
  <tr>
    <td>3.4</td>
    <td>1.1.12</td>
    <td>1887438</td>
  </tr>
  <tr>
    <td>3.0</td>
    <td>0.5.3</td>
    <td>1837938</td>
  </tr>
</table>

<a id="section-2"></a>

# 2.Precautions

Before you begin to use ApsaraDB for MongoDB, you must familiarize yourself with the precautions and limits of the service.

To ensure the stability and security of ApsaraDB for MongoDB instances, take note of the limits described in ApsaraDB for MongoDB limits.

Table 1. ApsaraDB for MongoDB limits

| Operation | Limits |
| --- | --- |
| Scale out nodes | • When a replica set instance is created, three nodes are added.<br>• ApsaraDB for MongoDB provides a primary node, a secondary node, and a hidden node for each replica set instance. The primary and secondary nodes provide services, and the hidden node is invisible to you.<br>• You cannot scale out secondary nodes. |
| Restart instances | You must restart an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console or by calling the API operation. |

<a id="section-3"></a>

# 3.Log in to the ApsaraDB for MongoDB console

This topic describes how to log on to the ApsaraDB for MongoDB console.

**Prerequisites**

- The URL of the console that is obtained from the deployment personnel.

- A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.

2. On the login page, enter your username and password.

   You can obtain the username and password that are used to log in to the Apsara Uni-manager Management Console from the operations administrator.

   > **Note**
   >
   > - **First login**
   >
   >   The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
   >
   > - **Forgotten password**
   >
   >   If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.

4. If multi-factor authentication (MFA) is enabled for your account, perform the following operations based on your login scenario:

   - You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator.

     <ol type="a">

     <li>

     On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device.

     </li>

     <li>

     Enter the username and password again as in Step 2 and click **Log On**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Enter the six-digit MFA code and click **Authentication**.

     </li>

     </ol>

   - You have enabled and bound MFA:

     Enter the six-digit MFA code and click **Authentication**.

     > **Note**
     >
     > For more information about how to bind and enable MFA, see **Security Center** > **MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.

5. In the top navigation bar, choose **Products** > **Database Services** > **ApsaraDB for MongoDB**.

<a id="section-4"></a>

# 4.Instance types

<a id="section-4-1"></a>

## 4.1. Replica set instance types

This topic describes the available instance types of replica set instances in ApsaraDB for MongoDB.

**Instance types**

| Instance type | Characteristics | Scenario |
| --- | --- | --- |
| Dedicated instance type | • A dedicated cluster occupies all allocated compute resources such as CPU cores.<br>• The cluster does not share compute resources with other clusters that run on the same server. This improves the reliability and stability of the cluster. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| General-purpose instance type | • Idle compute resources such as CPUs are shared among clusters that run on the same server.<br>• Resource sharing allows you to deploy a large number of clusters at low costs. | Scenarios in which cost-effectiveness is prioritized. |

**Supported specifications (MongoDB 5.0 to 8.0)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specificati ons</th>
    <th>Specification code</th>
    <th>Maximum connections</th>
    <th>Maximum IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="5"></td>
    <td>2 cores, 4 GB</td>
    <td>dds.mongo.2x.lar ge.c</td>
    <td>3,000</td>
    <td>8,000</td>
    <td rowspan="5">10 to 3,000</td>
  </tr>
  <tr>
    <td>2 cores, 8 GB</td>
    <td>dds.mongo.4x.lar ge.c</td>
    <td>3,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mongo.2x.xla rge.c</td>
    <td>6,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.mongo.4x.xla rge.c</td>
    <td>6,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td colspan="4"></td>
  </tr>
  <tr>
    <td rowspan="6">General-purpose</td>
    <td colspan="4"></td>
    <td rowspan="6"></td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mongo.2x.2xl arge.c</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mongo.4x.2xl arge.c</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.mongo.2x.4xl arge.c</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mongo.4x.4xl arge.c</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.mongo.2x.8xl arge.c</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td rowspan="10">Dedicated</td>
    <td>2 cores, 8 GB</td>
    <td>dds.mongo.4x.lar ge.d</td>
    <td>5,000</td>
    <td>8,000</td>
    <td rowspan="2">250 to 3,000</td>
  </tr>
  <tr>
    <td>2 cores, 16 GB</td>
    <td>dds.mongo.8x.lar ge.d</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mongo.2x.xla rge.d</td>
    <td>8,000</td>
    <td>8,000</td>
    <td rowspan="3">500 to 3,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.mongo.4x.xla rge.d</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 32 GB</td>
    <td>dds.mongo.8x.xla rge.d</td>
    <td>12,000</td>
    <td>9,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mongo.2x.2xl arge.d</td>
    <td>12,000</td>
    <td>8,000</td>
    <td rowspan="3">1,000 to 3,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mongo.4x.2xl arge.d</td>
    <td>16,000</td>
    <td>9,000</td>
  </tr>
  <tr>
    <td>8 cores, 64 GB</td>
    <td>dds.mongo.8x.2xl arge.d</td>
    <td>16,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.mongo.2x.4xl arge.d</td>
    <td>16,000</td>
    <td>9,000</td>
    <td rowspan="2"></td>
  </tr>
  <tr>
    <td colspan="4"></td>
  </tr>
  <tr>
    <td rowspan="9"></td>
    <td colspan="4"></td>
    <td rowspan="9">2,000 to 3,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mongo.4x.4xl arge.d</td>
    <td>32,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>dds.mongo.8x.4xl arge.d</td>
    <td>32,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.mongo.2x.8xl arge.d</td>
    <td>32,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>32 cores, 128 GB</td>
    <td>dds.mongo.4x.8xl arge.d</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>dds.mongo.8x.8xl arge.d</td>
    <td>96,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 128 GB</td>
    <td>dds.mongo.2x.16x large.d</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>64 cores, 256 GB</td>
    <td>dds.mongo.4x.16x large.d</td>
    <td>128,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 512 GB</td>
    <td>dds.mongo.8x.16x large.d</td>
    <td>128,000</td>
    <td>144,000</td>
  </tr>
</table>

**Supported specifications (MongoDB 3.0 to 4.2)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specifica tions</th>
    <th>Specification code</th>
    <th>Maximum connections</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="6">General-purpose</td>
    <td>1 core, 2 GB</td>
    <td>dds.mongo.mid</td>
    <td>200</td>
    <td>800</td>
    <td rowspan="6">10 to 2,000</td>
  </tr>
  <tr>
    <td>2 cores, 4 GB</td>
    <td>dds.mongo.standar d</td>
    <td>400</td>
    <td>1,600</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mongo.large</td>
    <td>1,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mongo.xlarge</td>
    <td>2,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mongo.2xlarge</td>
    <td>4,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td colspan="4"></td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td colspan="4"></td>
    <td rowspan="2"></td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mongo.4xlarge</td>
    <td>8,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td rowspan="5">Dedicated</td>
    <td>2 cores, 16 GB</td>
    <td>mongo.x8.medium</td>
    <td>2,500</td>
    <td>4,500</td>
    <td>250</td>
  </tr>
  <tr>
    <td>4 cores, 32 GB</td>
    <td>mongo.x8.large</td>
    <td>5,000</td>
    <td>9,000</td>
    <td>500</td>
  </tr>
  <tr>
    <td>8 cores, 64 GB</td>
    <td>mongo.x8.xlarge</td>
    <td>10,000</td>
    <td>18,000</td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>mongo.x8.2xlarge</td>
    <td>20,000</td>
    <td>36,000</td>
    <td>2,000</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>mongo.x8.4xlarge</td>
    <td>40,000</td>
    <td>72,000</td>
    <td>2,000</td>
  </tr>
  <tr>
    <td>Physical machine (dedicated)</td>
    <td>60 cores, 440 GB</td>
    <td>dds.mongo.2xmon opolize</td>
    <td>100,000</td>
    <td>100,000</td>
    <td>3,000</td>
  </tr>
</table>

<a id="section-4-2"></a>

## 4.2. Sharded cluster instance types

This topic describes the available instance types of sharded cluster instances in ApsaraDB for MongoDB.

**Instance types**

| Instance type | Characteristics | Scenario |
| --- | --- | --- |
| Dedicated instance type | • A dedicated cluster occupies all allocated compute resources such as CPU cores.<br>• The cluster does not share compute resources with other clusters that run on the same server. This improves the reliability and stability of the cluster. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| General-purpose instance type | • Idle compute resources such as CPUs are shared among clusters that run on the same server.<br>• Resource sharing allows you to deploy a large number of clusters at low costs. | Scenarios in which cost-effectiveness is prioritized. |

**MongoDB specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specific ations</th>
    <th>Specific ation code</th>
    <th>CPU cores</th>
    <th>Memory (GB)</th>
    <th>Maximu m connecti ons</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="5">General-purpose</td>
    <td>2 cores, 4 GB</td>
    <td>dds.mon gos.2x.la rge.c</td>
    <td>2</td>
    <td>4</td>
    <td>3,000</td>
    <td>1,600</td>
    <td rowspan="9"></td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mon gos.2x.xl arge.c</td>
    <td>4</td>
    <td>8</td>
    <td>6,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mon gos.2x.2x large.c</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.mon gos.2x.4x large.c</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.mon gos.2x.8x large.c</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td rowspan="4"></td>
    <td>2 cores, 8 GB</td>
    <td>dds.mon gos.4x.la rge.d</td>
    <td>2</td>
    <td>8</td>
    <td>5,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td>2 cores, 16 GB</td>
    <td>dds.mon gos.8x.la rge.d</td>
    <td>2</td>
    <td>16</td>
    <td>8,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mon gos.2x.xl arge.d</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="12">Dedicate d</td>
    <td colspan="6"></td>
    <td rowspan="12"></td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.mon gos.4x.xl arge.d</td>
    <td>4</td>
    <td>16</td>
    <td>8,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>4 cores, 32 GB</td>
    <td>dds.mon gos.8x.xl arge.d</td>
    <td>4</td>
    <td>32</td>
    <td>12,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mon gos.2x.2x large.d</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mon gos.4x.2x large.d</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>8 cores, 64 GB</td>
    <td>dds.mon gos.8x.2x large.d</td>
    <td>8</td>
    <td>64</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.mon gos.2x.4x large.d</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mon gos.4x.4x large.d</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>dds.mon gos.8x.4x large.d</td>
    <td>16</td>
    <td>128</td>
    <td>32,000</td>
    <td>25,600</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.mon gos.2x.8x large.d</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>32 cores, 128 GB</td>
    <td>dds.mon gos.4x.8x large.d</td>
    <td>32</td>
    <td>128</td>
    <td>96,000</td>
    <td>25,600</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>dds.mon gos.8x.8x large.d</td>
    <td>32</td>
    <td>256</td>
    <td>96000</td>
    <td>51,200</td>
  </tr>
</table>

**Supported specifications (MongoDB 3.4 to 4.2)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specific ations</th>
    <th>Specific ation code</th>
    <th>CPU cores</th>
    <th>Memory (GB)</th>
    <th>Maximu m connecti ons</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="6">General-purpose</td>
    <td>1 core, 2 GB</td>
    <td>dds.mon gos.mid</td>
    <td>1</td>
    <td>2</td>
    <td>1,000</td>
    <td>1,000</td>
    <td rowspan="12">10 to 2,000</td>
  </tr>
  <tr>
    <td>2 cores, 4 GB</td>
    <td>dds.mon gos.stand ard</td>
    <td>2</td>
    <td>4</td>
    <td>2,000</td>
    <td>2,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mon gos.large</td>
    <td>4</td>
    <td>8</td>
    <td>4,000</td>
    <td>4,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mon gos.xlarg e</td>
    <td>8</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mon gos.2xlar ge</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mon gos.4xlar ge</td>
    <td>16</td>
    <td>64</td>
    <td>16,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td rowspan="6"></td>
    <td>2 cores, 8 GB</td>
    <td>dds.mon gos.4x.la rge.d</td>
    <td>2</td>
    <td>8</td>
    <td>5,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td>2 cores, 16 GB</td>
    <td>dds.mon gos.8x.la rge.d</td>
    <td>2</td>
    <td>16</td>
    <td>8,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.mon gos.2x.xl arge.d</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>3,200</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.mon gos.4x.xl arge.d</td>
    <td>4</td>
    <td>16</td>
    <td>8,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>4 cores, 32 GB</td>
    <td>dds.mon gos.8x.xl arge.d</td>
    <td>4</td>
    <td>32</td>
    <td>12,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="10">Dedicate d</td>
    <td colspan="6"></td>
    <td rowspan="10"></td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.mon gos.2x.2x large.d</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>6,400</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.mon gos.4x.2x large.d</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>8 cores, 64 GB</td>
    <td>dds.mon gos.8x.2x large.d</td>
    <td>8</td>
    <td>64</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.mon gos.2x.4x large.d</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.mon gos.4x.4x large.d</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>dds.mon gos.8x.4x large.d</td>
    <td>16</td>
    <td>128</td>
    <td>32,000</td>
    <td>25,600</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.mon gos.2x.8x large.d</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>12,800</td>
  </tr>
  <tr>
    <td>32 cores, 128 GB</td>
    <td>dds.mon gos.4x.8x large.d</td>
    <td>32</td>
    <td>128</td>
    <td>96,000</td>
    <td>25,600</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>dds.mon gos.8x.8x large.d</td>
    <td>32</td>
    <td>256</td>
    <td>96,000</td>
    <td>51,200</td>
  </tr>
</table>

**Shard specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specific ations</th>
    <th>Specific ation code</th>
    <th>CPU cores</th>
    <th>Memory (GB)</th>
    <th>Maximu m connecti ons</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="9">General-purpose</td>
    <td>2 cores, 4 GB</td>
    <td>dds.shar d.2x.larg e.c</td>
    <td>2</td>
    <td>4</td>
    <td>3,000</td>
    <td>8,000</td>
    <td rowspan="13"></td>
  </tr>
  <tr>
    <td>2 cores, 8 GB</td>
    <td>dds.shar d.4x.larg e.c</td>
    <td>2</td>
    <td>8</td>
    <td>3,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.shar d.2x.xlar ge.c</td>
    <td>4</td>
    <td>8</td>
    <td>6,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.shar d.4x.xlar ge.c</td>
    <td>4</td>
    <td>16</td>
    <td>6,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.shar d.2x.2xla rge.c</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.shar d.4x.2xla rge.c</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.shar d.2x.4xla rge.c</td>
    <td>16</td>
    <td>64</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.shar d.4x.4xla rge.c</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.shar d.2x.8xla rge.c</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td rowspan="4"></td>
    <td>2 cores, 8 GB</td>
    <td>dds.shar d.4x.larg e.d</td>
    <td>2</td>
    <td>8</td>
    <td>5,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>2 cores, 16 GB</td>
    <td>dds.shar d.8x.larg e.d</td>
    <td>2</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.shar d.2x.xlar ge.d</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="14">Dedicate d</td>
    <td colspan="6"></td>
    <td rowspan="14">10 to 3,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.shar d.4x.xlar ge.d</td>
    <td>4</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 32 GB</td>
    <td>dds.shar d.8x.xlar ge.d</td>
    <td>4</td>
    <td>32</td>
    <td>12,000</td>
    <td>9,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.shar d.2x.2xla rge.d</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.shar d.4x.2xla rge.d</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>9,000</td>
  </tr>
  <tr>
    <td>8 cores, 64 GB</td>
    <td>dds.shar d.8x.2xla rge.d</td>
    <td>8</td>
    <td>64</td>
    <td>16,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.shar d.2x.4xla rge.d</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>9,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.shar d.4x.4xla rge.d</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>dds.shar d.8x.4xla rge.d</td>
    <td>16</td>
    <td>128</td>
    <td>32,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.shar d.2x.8xla rge.d</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>32 cores, 128 GB</td>
    <td>dds.shar d.4x.8xla rge.d</td>
    <td>32</td>
    <td>128</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>dds.shar d.8x.8xla rge.d</td>
    <td>32</td>
    <td>256</td>
    <td>96,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 128 GB</td>
    <td>dds.shar d.2x.16xl arge.d</td>
    <td>64</td>
    <td>128</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="3"></td>
    <td colspan="6"></td>
    <td rowspan="3"></td>
  </tr>
  <tr>
    <td>64 cores, 256 GB</td>
    <td>dds.shar d.4x.16xl arge.d</td>
    <td>64</td>
    <td>256</td>
    <td>128,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 512 GB</td>
    <td>dds.shar d.8x.16xl arge.d</td>
    <td>64</td>
    <td>512</td>
    <td>128,000</td>
    <td>144,000</td>
  </tr>
</table>

**Supported specifications (MongoDB 3.4 to 4.2)**

**Maximu**

**Specific**

**Storage**

**Instance**

**Specific**

**CPU**

**Memory**

**m**

**ation**

**IOPS**

**capacity**

**type**

**ations**

**cores**

**(GB)**

**connecti**

**code**

**(GB)**

**ons**

1 core, 2

dds.shar

1

2

500

1,000

GB

d.mid

dds.shar

2 cores,

d.standar

2

4

1,000

2,000

4 GB

d

4 cores,

dds.shar

4

8

3,000

4,000

8 GB

d.large

General-

10 to

purpose

2,000

8 cores,

dds.shar

8

16

5,000

8,000

16 GB

d.xlarge

8 cores,

dds.shar

8

32

8,000

14,000

32 GB

d.2xlarge

16 cores,

dds.shar

16,000

16,000

16

64

64 GB

d.4xlarge

dds.shar

2 cores,

d.sn8.xla

2

16

2,500

4,500

10 to 250

16 GB

rge.3

dds.shar

4 cores,

d.sn8.2xl

4

32

5,000

9,000

10 to 500

32 GB

arge.3

dds.shar

8 cores,

10 to

d.sn8.4xl

8

64

10

18,000

64 GB

1,000

arge.3 dds.shar

16 cores,

10 to

d.sn8.8xl

16

128

20,000

36,000

128 GB

2,000

arge.3

dds.shar

32 cores,

d.sn8.16x

32

256

40,000

72,000

256 GB

large.3

dds.shar

2 cores,

d.4x.larg

2

8

5,000

8,000

8 GB

e.d

dds.shar

2 cores,

d.8x.larg

2

16

8,000

8,000

16 GB

e.d

dds.shar

4 cores,

d.2x.xlar

4

8

8,000

8,000

8 GB

ge.d

dds.shar

4 cores,

d.4x.xlar

4

16

8,000

8,000

16 GB

ge.d

dds.shar

4 cores,

d.8x.xlar

4

32

12,000

9,000

32 GB

ge.d

dds.shar

8 cores,

d.2x.2xla

8

16

12,000

8,000

16 GB

rge.d

Dedicate d

dds.shar

8 cores,

d.4x.2xla

8

32

16,000

9,000

32 GB

rge.d

dds.shar

8 cores,

d.8x.2xla

8

64

16,000

18,000

64 GB

rge.d

10 to 3,000

16 cores,

dds.shar

32 GB

d.2x.4xla

16

32

16,000

9,000

rge.d

dds.shar

16 cores,

d.4x.4xla

16

64

32,000

18,000

64 GB

rge.d

<table>
  <tr>
    <td rowspan="8"></td>
    <td colspan="6"></td>
    <td rowspan="8"></td>
  </tr>
  <tr>
    <td>16 cores, 128 GB</td>
    <td>dds.shar d.8x.4xla rge.d</td>
    <td>16</td>
    <td>128</td>
    <td>32,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 64 GB</td>
    <td>dds.shar d.2x.8xla rge.d</td>
    <td>32</td>
    <td>64</td>
    <td>32,000</td>
    <td>18,000</td>
  </tr>
  <tr>
    <td>32 cores, 128 GB</td>
    <td>dds.shar d.4x.8xla rge.d</td>
    <td>32</td>
    <td>128</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>32 cores, 256 GB</td>
    <td>dds.shar d.8x.8xla rge.d</td>
    <td>32</td>
    <td>256</td>
    <td>96,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 128 GB</td>
    <td>dds.shar d.2x.16xl arge.d</td>
    <td>64</td>
    <td>128</td>
    <td>96,000</td>
    <td>36,000</td>
  </tr>
  <tr>
    <td>64 cores, 256 GB</td>
    <td>dds.shar d.4x.16xl arge.d</td>
    <td>64</td>
    <td>256</td>
    <td>128,000</td>
    <td>72,000</td>
  </tr>
  <tr>
    <td>64 cores, 512 GB</td>
    <td>dds.shar d.8x.16xl arge.d</td>
    <td>64</td>
    <td>512</td>
    <td>128,000</td>
    <td>144,000</td>
  </tr>
</table>

**ConfigServer specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specific ations</th>
    <th>Specific ation code</th>
    <th>CPU cores</th>
    <th>Memory (GB)</th>
    <th>Maximu m connecti ons</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="4">General-purpose</td>
    <td>2 cores, 4 GB</td>
    <td>dds.cs.2x.large.c</td>
    <td>2</td>
    <td>4</td>
    <td>3,000</td>
    <td>8,000</td>
    <td rowspan="4"></td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.cs.2x.xlarge.c</td>
    <td>4</td>
    <td>8</td>
    <td>6,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.cs.2x.2xlarge.c</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td colspan="6"></td>
    <td rowspan="8">20 to 2,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.cs.2x.4xlarge.c</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td rowspan="6">Dedicate d</td>
    <td>4 cores, 8 GB</td>
    <td>dds.cs.2x.xlarge.d</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB</td>
    <td>dds.cs.4x.xlarge.d</td>
    <td>4</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.cs.2x.2xlarge.d</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.cs.4x.2xlarge.d</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB</td>
    <td>dds.cs.2x.4xlarge.d</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.cs.4x.4xlarge.d</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
</table>

**Supported specifications (MongoDB 3.4 to 4.2)**

<table>
  <tr>
    <th>Instance type</th>
    <th>Specific ations</th>
    <th>Specific ation code</th>
    <th>CPU cores</th>
    <th>Memory (GB)</th>
    <th>Maximu m connecti ons</th>
    <th>IOPS</th>
    <th>Storage capacity (GB)</th>
  </tr>
  <tr>
    <td rowspan="5">General-purpose</td>
    <td>1 core, 2 GB</td>
    <td>dds.cs.mi d</td>
    <td>1</td>
    <td>2</td>
    <td>8,000</td>
    <td>8,000</td>
    <td rowspan="5"></td>
  </tr>
  <tr>
    <td>2 cores, 4 GB</td>
    <td>dds.cs.st andard</td>
    <td>2</td>
    <td>4</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 8 GB</td>
    <td>dds.cs.lar ge</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB</td>
    <td>dds.cs.xl arge</td>
    <td>8</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td colspan="6"></td>
  </tr>
  <tr>
    <td rowspan="3"></td>
    <td colspan="6"></td>
    <td rowspan="9">20 to 2,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB</td>
    <td>dds.cs.2x large</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB</td>
    <td>dds.cs.4x large</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
  <tr>
    <td rowspan="6">Dedicate d</td>
    <td>4 cores, 8 GB (dedicate d)</td>
    <td>dds.cs.2x.xlarge.d</td>
    <td>4</td>
    <td>8</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>4 cores, 16 GB (dedicate d)</td>
    <td>dds.cs.4x.xlarge.d</td>
    <td>4</td>
    <td>16</td>
    <td>8,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 16 GB (dedicate d)</td>
    <td>dds.cs.2x.2xlarge.d</td>
    <td>8</td>
    <td>16</td>
    <td>12,000</td>
    <td>8,000</td>
  </tr>
  <tr>
    <td>8 cores, 32 GB (dedicate d)</td>
    <td>dds.cs.4x.2xlarge.d</td>
    <td>8</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 32 GB (dedicate d)</td>
    <td>dds.cs.2x.4xlarge.d</td>
    <td>16</td>
    <td>32</td>
    <td>16,000</td>
    <td>14,000</td>
  </tr>
  <tr>
    <td>16 cores, 64 GB (dedicate d)</td>
    <td>dds.cs.4x.4xlarge.d</td>
    <td>16</td>
    <td>64</td>
    <td>32,000</td>
    <td>16,000</td>
  </tr>
</table>

<a id="section-5"></a>

# 5.Quick start

<a id="section-5-1"></a>

## 5.1. Use ApsaraDB for MongoDB

This topic is a quick start guide to basic usage operations for ApsaraDB for MongoDB, such as creating an instance, configuring a whitelist, and connecting to an instance. Flowcharts are used to describe the basic procedures in ApsaraDB for MongoDB, and guide you to create an ApsaraDB for MongoDB instance.

![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/22085955fe47c52d04c1ff603afa3fb9.jpeg)

- Create a replica set instance

  An instance is a virtual database server on which you can create and manage multiple databases.

- Configure a whitelist for an ApsaraDB for MongoDB instance

  After you create an ApsaraDB for MongoDB instance, you need to configure a whitelist for the instance to allow external devices to access the instance.

  A whitelist can enhance access security for ApsaraDB for MongoDB instances. We recommend that you update the whitelist on a regular basis. The normal services of the instance are not affected if you configure a whitelist.

- Use the mongo shell to connect to an ApsaraDB for MongoDB instance

  After you create an instance and configure a whitelist, you can use the mongo shell to connect to the instance.

<a id="section-5-2"></a>

## 5.2. Create an instance

<a id="section-5-2-1"></a>

### 5.2.1. Create a replica set instance

This topic describes how to create a replica set instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set instance List** page, click **+ Create an instance** in the upper-left corner.

4. On the **Create a MongoDB instance** page, configure the parameters described in the following table.

   **Section**

   **Parameter**

   **Description**

   The organization where you

   **Organization**

   want to deploy the instance.

   **Basic configuration**

   The resource set where you

   **Resource Set**

   want to deploy the instance.

   The region where you want to

   **Region**

   deploy the instance.

   - **Single Zone**: The primary, secondary, and hidden nodes are deployed in one zone.

   - **Dual Availability Zones**: The primary, secondary, and hidden nodes are deployed in two zones to meet the

   **Deployment Method**

   requirements of zone-disaster recovery.

   - **Three available areas**: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone-disaster recovery.

   Select a primary zone for the instance.

   > **Note**

   **Primary Availability Zone**

   > If you select dual zones, the instance supports zone-disaster recovery across two data centers.

   **Area**

   The zone in which the secondary instance is deployed.

   > **Note**
   >
   > This parameter is required

   **Secondary Availability**

   > only when you select

   **Zone**

   > **Dual Availability Zones** or **Three available areas** for the Deployment Method parameter.

   Select the third availability zone of the instance.

   > **Note**

   **Third Availability Zone**

   > This parameter is required only when you select **Three available areas** for the Deployment Method parameter.

   The chip architecture of the host where you want to deploy the instance.

   > **Note**

   **Chip Architecture**

   > If you do not have permissions to select an option, contact the operations administrator to grant permissions to your account.

   The database engine of the

   **Database Engine**

   instance. Set the value to **MongoDB**.

   The database engine version of the instance. Valid values:

   - 8.0

   - 7.0

   - 6.0

   **Database Version**

   - 5.0

   - 4.2

   - 4.0

   - 3.4

   - 3.0

   The number of active-standby nodes in the replica set

   **Number of primary and**

   instance. Configure this

   **standby nodes**

   parameter based on your business requirements.

   The number of read-only nodes in the replica set

   **Number of read-only nodes**

   instance. Configure this parameter based on your business requirements.

   The instance type of the instance. Valid values:

   - **General-Purpose**: Instances of this type exclusively use the

   **Specification Configuration**

   allocated memory and I/O resources, while CPU and storage resources are shared with other general-purpose instances on the same server.

   - **Dedicated**: Instances of this type exclusively use CPU, memory, storage, and

   **Specification Type**

   I/O resources. Performance remains stable over time and is not affected by the behavior of other instances on the same server.

   - **Exclusive Physical Machine**: Instances of this type are the highest-tier dedicated instances, also referred to as dedicated host instances. All resources of a physical server are exclusively allocated to a single instance.

   The node specifications of the instance. Select an option based on your actual needs.

   **Node Specifications**

   You can log in to the ApsaraDB for MongoDB console to view the detailed specifications.

   The storage space of the instance. This space contains the space for data, system files, log files, and transaction

   **Storage Space (GB)**

   files. For more information, see **Replica set instance types** in **ApsaraDB for MongoDB Product Introduction**.

   The network type of the instance. Valid values:

   - **Classic Network**: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service.

   - **Proprietary Network**: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables,

   **Network Type**

   CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type.

   > **Note**
   >
   > If you select the **Proprietary Network** network type, you must specify the **Private network vpc** and **Switch vswitch** parameters.

   **Network**

   The VPC where you want to deploy the instance. If no VPCs are available, click **Create a VPC** to the right of the drop-down list.

   **Private network vpc**

   > **Note**
   >
   > If **Network Type** is set to **Proprietary Network**, you must specify this parameter.

   The vSwitch in the VPC. If no vSwitches are available, click **Create a switch** to the right of the drop-down list.

   **Switch vswitch**

   > **Note**
   >
   > If **Network Type** is set to **Proprietary Network**, you must specify this parameter.

   <table>
     <tr>
       <td rowspan="4">Password Settings</td>
       <td>Instance Name</td>
       <td>The name of the instance. The name must meet the following requirements:<br>• It must start with a letter.<br>• It can contain digits, letters, underscores (_), and hyphens (-).<br>• It must be 2 to 256 characters in length.</td>
     </tr>
     <tr>
       <td>Set Password</td>
       <td>The time when you want to set the password. Valid values:<br>• <strong>Set up now</strong>: immediately sets the login password.<br>• <strong>Set up after creation</strong>: sets the login password after instance creation. For more information, see Reset a password.</td>
     </tr>
     <tr>
       <td>Login password</td>
       <td>The password used to log in to the instance. The password must meet the following requirements:<br>• It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters:<br>! # $ % ^ &amp; * ( ) _ + =<br>• It must be 8 to 32 characters in length.<br>Note<br>If <strong>Set Password</strong> is set to <strong>Set up now</strong>, this parameter is required.</td>
     </tr>
     <tr>
       <td>Confirm password</td>
       <td>Enter the password again. The password that you enter must be the same as that in Login password.<br>Note<br>If <strong>Set Password</strong> is set to <strong>Set up now</strong>, this parameter is required.</td>
     </tr>
   </table>

5. Click **Submit**.

<a id="section-5-2-2"></a>

### 5.2.2. Create a sharded cluster instance

This topic describes how to create a sharded cluster instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click **+ Create an instance**.

4. On the **Create a MongoDB instance - Sharding** page, configure the parameters described in the following table.

   **Section**

   **Parameter**

   **Description**

   **Organization**

   The organization where you want to deploy the instance.

   **Basic configuration**

   **Resource Set**

   The resource set where you want to deploy the instance.

   **Region**

   The region where you want to deploy the instance.

   - **Single Availability Zone**: The primary, secondary, and hidden nodes are deployed in one zone.

   - **Dual Availability Zones**: The primary, secondary, and

   **Deployment**

   hidden nodes are deployed in two zones to meet the

   **method**

   requirements of zone-disaster recovery.

   - **Three Availability Zones**: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone-disaster recovery.

   Select a primary zone for the instance.

   **Primary**

   > **Note**

   **Availability Zone**

   > If you select dual-zone, the instance supports zone-disaster recovery across two data centers.

   **Region**

   The zone in which the secondary instance is deployed.

   **Secondary**

   > **Note**

   **Availability**

   > This parameter is required only when you select **Dual**

   **Zone**

   > **Availability Zones** or **Three Availability Zones** for the Deployment method parameter.

   Select the third availability zone for the instance.

   **Third**

   > **Note**

   **Availability Zone**

   > This parameter is required only when you select **Three Availability Zones** for the Deployment method parameter.

   The chip architecture of the host where you want to deploy the instance.

   **Chip**

   > **Note**

   **architecture**

   > If you do not have permissions to select a chip architecture, contact the operations administrator to grant permissions to your account.

   **Database**

   The database engine of the instance. Set the value to

   **engine**

   **MongoDB**.

   **Specification Configuration**

   The database engine version of the instance. Valid values:

   - 8.0

   - 7.0

   - 6.0

   **Database version**

   - 5.0

   - 4.2

   - 4.0

   - 3.4

   The network type of the instance. Valid values:

   - **Classic Network**: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service.

   - **Virtual Private Network**: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR

   **Network type**

   blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type.

   > **Note**
   >
   > If you select the **Virtual Private Network** network type, you must specify the **Virtual Private Cloud (VPC)** and **Switch vswitch** parameters.

   - **IPv4**: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks.

   - **Dual-Stack (IPv4/IPv6)**: assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance.

   **IP Type**

   > **Note**
   >
   > - To configure this parameter, you must enable IPv6 first. For more information, see the "Enable IPv6 for ApsaraDB for MongoDB" topic in **O&M Guide**.
   >
   > - If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB.

   The VPC where you want to deploy the instance. If no VPCs are available, click **Create a VPC** to the right of the drop-down list.

   **Virtual Private Cloud (VPC)**

   > **Note**
   >
   > If **Network type** is set to **Virtual Private Network**, this parameter is required.

   The vSwitch in the VPC. If no vSwitches are available, click **Create a switch** to the right of the drop-down list.

   **Switch vswitch**

   > **Note**
   >
   > If **Network type** is set to **Virtual Private Network**, this parameter is required.

   Add IPv4 addresses that are allowed to access the ApsaraDB for MongoDB instance.

   > **Note**

   **IPv4 Whitelist**

   **Network**

   > We recommend that you use private CIDR blocks defined in RFC 1918 for the VPC, such as 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16.

   Add IPv6 addresses that are allowed to access the ApsaraDB for MongoDB instance.

   > **Note**
   >
   > Take note of the following requirements when you add addresses to the IPv6 whitelist:
   >
   > - An IPv6 address consists of eight segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0000:0000:0000:0000:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once.
   >
   > - The prefix length must be specified, which is an integer from 0 to 128, following a forward slash (/). Example: 2001:db8::/32.
   >
   > - fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address.
   >
   > - ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments.
   >
   > - fe80::/10 is a link-local address similar to IPv4

   **IPv6 Whitelist**

   > addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it.

   The specifications of the mongos node. You can log in to

   **Mongos**

   the ApsaraDB for MongoDB console to view the detailed

   **specification**

   specifications.

   **Mongos specification**

   The number of mongos nodes. You can select 2 to 32

   **Quantity**

   **configuration**

   mongos nodes.

   **Custom name**

   The custom name of the mongos node.

   **for mongos**

   The specifications of the shard. You can log in to the

   **Shard**

   ApsaraDB for MongoDB console to view the detailed

   **specification**

   specifications.

   The storage space of the shard. This space stores data,

   **Storage Space**

   system files, log files, and transaction files. For more

   **Shard**

   **(GB)**

   information, see **Sharded cluster instance types** in

   **specification**

   ApsaraDB for MongoDB Product Introduction.

   **configuration**

   **Quantity**

   The number of shards. You can select 2 to 32 shards.

   **Shard custom**

   The custom name of the shard.

   **name**

   **Configserver**

   The specifications of the ConfigServer component. Set the

   **specification**

   value to **1 vCPU, 2 GB**.

   **Configserver**

   **Disk Space**

   The storage space of the ConfigServer component. Set the

   **specification**

   **(GB)**

   value to 20.

   **configuration**

   **Custom name for**

   The custom name of the ConfigServer component.

   **configserver**

   The name of the instance. The name must meet the following requirements:

   - It must start with a letter.

   **Instance Name**

   - It can contain digits, letters, underscores (_), and hyphens (-).

   - It must be 2 to 256 characters in length.

   The time when you want to set the password. Valid values:

   - **Set up now**: immediately sets the login password.

   **Set a password**

   - **Set After Creation**: sets the password after the instance is created. For more information, see Reset a password.

   **Password**

   The password used to log in to the instance. The password

   **Setup**

   must meet the following requirements:

   - It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters:

   **Login**

   ! # $ % ^ & \* ( ) _ + =

   **password**

   - It must be 8 to 32 characters in length.

   > **Note**
   >
   > If **Set a password** is set to **Set up now**, this parameter is required.

   Enter the password again. The password that you enter must be the same as that in Login password.

   **Confirm**

   > **Note**

   **password**

   > If **Set a password** is set to **Set up now**, this parameter is required.

5. Click **Submit**.

<a id="section-5-3"></a>

## 5.3. Reset a password

This topic describes how to reset the password of an account in the ApsaraDB for MongoDB console. For data security purposes, we recommend that you change the password of your account on a regular basis.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Accounts**.

5. Find the account for which you want to change the password and click **Reset Password** in the **Operation** column.

6. In the **Reset account password** dialog box, configure the following parameters.

   | Parameter | Description |
   | --- | --- |
   | New Password | • The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:<br>! # $ % ^ &amp; \* ( ) _ + - =<br>• The password must be 8 to 32 characters in length.<br>• You must not use keywords such as Admin or Password. |
   | Confirm new password | Enter the password again. The password you enter must be the same as that in New Password. |

7. Click **OK**.

<a id="section-5-4"></a>

## 5.4. Configure a whitelist

This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or CIDR blocks to an instance whitelist to allow access from those addresses. This improves database security and stability. Proper configuration of whitelists can enhance the security of access to ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis.

**Background information**

- The system creates a default whitelist for each instance. This whitelist can be modified or cleared but cannot be deleted.

- After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the **default** whitelist of the instance. The IP address 127.0.0.1 indicates that no IP addresses are allowed to access the instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.

5. Click **Add a whitelist Group** above the list.

6. In the **New name adding list groups (up to 50 groups supported)** panel, configure parameters.

   | Parameter | Description |
   | --- | --- |
   | Group name | The group name must be 2 to 32 characters in length. It can contain lowercase letters, digits, and underscores (_) and must start with a lowercase letter and end with a lowercase letter or a digit. |
   | Type | You can select <strong>IPv4</strong> or <strong>IPv6</strong>. |
   | Whitelist within a group | • Take note of the following requirements when you add IP addresses to the whitelist:<br>• Separate multiple IP addresses with commas (,). A maximum of 1,000 unique IP addresses can be added.<br>• You can specify IP addresses in the following formats:<br>• IPv4: 10.23.12.24 (specific IPv4 address) or 10.23.12.24/24 (CIDR block with a prefix length ranging from 1 to 32).<br>• IPv6: 2001:db8::1 (specific IPv6 address) or 2001:db8::/32 (CIDR block with a prefix length ranging from 1 to 128).<br>Note<br>If you enter a CIDR block whose prefix length is 0, such as 0.0.0.0/0 or ::/0, all IP addresses are allowed to access the instance. This poses a high security risk.Proceed with caution.Examples<br>• Allow a single IPv6 address: 2001:db8:85a3::8a2e:370:7334<br>• Allow an IPv6 CIDR block: 240e:390:a100::/44<br>• Allow all IP addresses (high risk): ::/0 or 0.0.0.0/0 |
   | Import file (.txt) | You can import IP addresses in batches. |
   | Load the private IP addresses of ECS instances | i. Select <strong>Import ECS Internal IP Address</strong>.<br>ii. Select IP addresses based on your business requirements.<br>Note<br>To find the Elastic Compute Service (ECS) instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |

7. Click **OK**.

<a id="section-5-5"></a>

## 5.5. Connect to an instance

<a id="section-5-5-1"></a>

### 5.5.1. Use DMS to log on to an ApsaraDB for MongoDB instance

You can use Data Management (DMS) to log on to an ApsaraDB for MongoDB instance.

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the upper-right corner of the page, click **Log On**.

   > **Note**
   >
   > For a sharded cluster instance, you must also select a mongos node.

   Log on to the **DMS** console.

5. In the **Login instance** dialog box, configure the parameters described in the following table.

   | Parameter | Description |
   | --- | --- |
   | Database Type | The database engine of the instance. By default, this parameter is set to the database engine of the instance that you want to access. |
   | Instance Region | The region where the instance is deployed. By default, this parameter is set to the region where the current instance is deployed. |
   | Connection string address | The connection string of the instance. By default, this parameter is set to the connection string of the current instance. |
   | Database Name | The name of the database. By default, this parameter is set to admin. |
   | Database Account | The account used to connect to the database. By default, this parameter is set to root. |
   | Database Password | The password of the account used to connect to the database. |

6. Click **Login**.

   > **Note**
   >
   > You can select **Remember password** to eliminate the need to manually
   >
   > enter the password again the next time you log on to the database.

<a id="section-5-5-2"></a>

### 5.5.2. Use the mongo shell to connect to an ApsaraDB for MongoDB instance

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by MongoDB. You can install MongoDB on your client and use the mongo shell to connect to an ApsaraDB for MongoDB instance.

**Prerequisites**

- The version of MongoDB that you install on your client is the same as that of your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about how to install MongoDB, see Install MongoDB.

  > **Note**
  >
  > You can select a MongoDB version corresponding to your client version in
  >
  > the upper-left corner of the page.

- The IP address of your client is added to an IP address whitelist of your ApsaraDB for MongoDB instance. For more information, see Configure a whitelist.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, find the instance that you want to manage and click the ID of the instance.

4. In the left-side navigation pane, click **Database Connections** to obtain the endpoints.

   > **Note**
   >
   > - If the instance is a replica set instance, obtain the endpoint or connection string URI of a node.
   >
   > - If the instance is a sharded cluster instance, obtain the endpoint or connection string URI of a mongos node.
   >
   > For more information about endpoints, see Overview of replica set instance connections or Overview of sharded cluster instance connections.

5. Connect to a database of the instance from your client on which the mongo shell is installed.

   - If the instance is a replica set instance, the following methods are available:

     - High-availability (HA) connection (recommended)

       You can use a connection string URI to connect to both the primary and secondary nodes in the instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched.

       Command syntax:

       ```text
       mongo "<ConnectionStringURI>"
       ```

       > **Note**
       >
       > - The connection string URI must be enclosed in a pair of double quotation marks ("").
       >
       > - &lt;ConnectionStringURI>: the connection string URI of the instance.
       >
       >   You must replace  `****`  in the connection string URI with the database password. For more information about how to specify a database password, see Reset the password.

       Example:

       ```text
       mongo "mongodb://root:****@dds-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717,dds-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
       *"
       ```

     - Single-node connection

       In most cases, you can directly connect to the primary node or a secondary or read-only node. If the primary node fails, the system automatically switches to a secondary node and the secondary node becomes the primary node. This affects the read and write operations of your application.

       Command syntax:

       ```text
       mongo --host <host> -u <username> -p --authenticationDatabase <database>
       ```

       > **Note**
       >
       > - &lt;host>: the endpoint of the primary or secondary node.
       >
       > - &lt;username>: the username used to log on to a database of the instance. The initial username is **root**.
       >
       > - &lt;database>: the name of the database corresponding to the username for which authentication is enabled. If the username is root, enter admin.

       Example:

       ```text
       mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticationDatabase admin
       ```

       When the  `Enter password:`  message is displayed, enter the password of the username and press the Enter key. If you forget the password of the root account, you can reset the password. For more information, see Reset the password.

       > **Note**
       >
       > The password characters are masked when you enter the password.

   - If the instance is a sharded cluster instance, the following methods are available:

     - HA connection (recommended)

       You can use a connection string URI to connect to a database of the instance. If one mongos node fails, the system switches to another mongos node to ensure the HA of the connection.

       Command syntax:

       ```text
       mongo "<ConnectionStringURI>"
       ```

       > **Note**
       >
       > - The connection string URI must be enclosed in a pair of double quotation marks ("").
       >
       > - &lt;ConnectionStringURI>: the connection string URI of the instance.
       >
       >   You must replace  `****`  in the connection string URI with the database password. For more information about how to specify a database password, see Reset the password.

       Example:

       ```text
       mongo "mongodb://root:****@s-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
       ```

     - Mongos node connection Command syntax:

       ```text
       mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
       ```

       > **Note**
       >
       > - &lt;mongos_host>: the endpoint of a mongos node in the instance.
       >
       > - &lt;username>: the username used to log on to a database of the instance. The initial username is **root**.
       >
       > - &lt;database>: the name of the database corresponding to the username for which authentication is enabled. If the username is root, enter admin.

       Example:

       ```text
       mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticationDatabase admin
       ```

<a id="section-5-5-3"></a>

### 5.5.3. Introduction to connection strings and URIs

<a id="section-5-5-3-1"></a>

#### 5.5.3.1. Overview of replica set instance connections

ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node and use a connection string URI to connect to both of them. For high availability (HA), we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections.

**Prerequisites**

A whitelist is configured for the instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**Obtain connection strings**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Database Connections** to obtain connection strings.

**Description of connection strings**

| Item | Description |
| --- | --- |
| Connection address type | • Classic network endpoint: Classic network connection is a type of internal connection, and classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists.<br>• VPC endpoint: Virtual Private Cloud (VPC) connection is a type of internal connection, and VPC endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and higher performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance.<br>• Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |
| Role | • Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance.<br>• Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance.<br>• Connection string URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and HA. |
| Connection string | The connection string of a primary or secondary node is in the following format:<br><code>&lt;host&gt;:&lt;port&gt;</code><br>• &lt;host&gt;: the endpoint used to connect to the instance.<br>• &lt;port&gt;: the port number used to connect to the instance. |
| Connection string URI | A connection string URI is in the following format:<br><code>mongodb://[username:password@]host1[:port1][,host2[:port2],...</code><br><code>[,hostN[:portN]]][/[database][?options]]</code><br>• mongodb://: the prefix of a connection string URI.<br>• username:password@: the username and password used to log on to a database of the instance. You must separate them with a colon (:).<br>• hostX:portX: the endpoint and port number used to connect to the instance.<br>• /database: the name of the database corresponding to the username if authentication is enabled.<br>• options: the additional options that are used to connect to the instance.<br>Note We recommend that you use the URI to connect to the instance in a production environment. This way, when a node fails, the read and write operations of your application are not affected by the failover. |

**Related topics**

- Use the mongo shell to connect to an ApsaraDB for MongoDB instance

<a id="section-5-5-3-2"></a>

#### 5.5.3.2. Overview of sharded cluster instance connections

ApsaraDB for MongoDB sharded cluster instances support both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node and use a connection string URI to connect to multiple mongos nodes. For high availability (HA), we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections.

**View connection strings**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Sharded Cluster Instances** page, click the ID of the instance whose connection strings you want to view.

4. In the left-side navigation pane, click **Database Connections** to view connection strings.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/b29c9820621692aad42dadb422352163.png)

**Description of connection strings**

| Item | Description |
| --- | --- |
| Connection address type | • Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists.<br>• VPC endpoint: Virtual Private Cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance.<br>• Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |
| Mongos node ID | The connection string of a mongos node is in the following format:<br><code>&lt;host&gt;:&lt;port&gt;</code><br>• &lt;host&gt;: the endpoint used to connect to the instance.<br>• &lt;port&gt;: the port number used to connect to the instance.<br>Note During routine tests, you can use a connection string to directly connect to a mongos node. |
| Connection string URI | A connection string URI is in the following format:<br><code>mongodb://[username:password@]host1[:port1][,host2[:port2],...</code><br><code>[,hostN[:portN]]][/[database][?options]]</code><br>• mongodb://: the prefix of a connection string URI.<br>• username:password@: the username and password used to log on to the instance.You must separate them with a colon (:).<br>• hostX:portX: the endpoint and port number used to connect to the instance.<br>• /database: the name of the database corresponding to the username if authentication is enabled.<br>• options: the additional options that are used to connect to the instance.<br>Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads.If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |

<a id="section-6"></a>

# 6.Instance management

<a id="section-6-1"></a>

## 6.1. Create an instance

<a id="section-6-1-1"></a>

### 6.1.1. Create a replica set instance

This topic describes how to create an ApsaraDB for MongoDB replica set instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances List** page, click **Create an instance** in the upper-left corner.

4. On the **Create MongoDB Instance** page, configure the following parameters.

   **Category**

   **Parameter**

   **Description**

   Select the organization to

   **Organization**

   which the instance belongs.

   **Basic Configuration**

   Select the resource set to

   **Resource Set**

   which the instance belongs.

   Select the region where the

   **Region**

   instance resides.

   - **Single-Zone**: The primary node, secondary node, and hidden node reside in the same availability zone.

   - **Dual-Zone**: The primary node, secondary node, and hidden node reside in two different availability zones

   **Deployment Method**

   to meet zone-disaster recovery requirements.

   - **Multi-Zone**: The primary node, secondary node, and hidden node reside in three different availability zones to meet zone-disaster recovery requirements.

   Select athe primary availability zone for the instance.

   **Region**

   > **Note**
   >
   > If you select a dual-zone deployment, the instance

   **Primary Zone**

   > supports zone-disaster recovery across two data centers.

   Select the availability zone for the secondary node of the instance.

   > **Note**

   **Secondary Zone**

   > Configure this option only when you select **Dual-Zone** or **Multi-Zone** as the deployment method.

   Select the third availability zone for the instance.

   > **Note**

   **Third Zone**

   > Configure this option only when you select **Multi-Zone** as the deployment method.

   Select the chip architecture of the host to which the instance belongs.

   > **Note**

   **Chip Architecture**

   > If you receive an unauthorized prompt when selecting this configuration, contact the operations administrator to authorize your account.

   The value is fixed to

   **Database Engine**

   **MongoDB**.

   Select the database version for the instance from the following options:

   - 8.0

   - 7.0

   - 6.0

   **Database Version**

   - 5.0

   - 4.2

   - 4.0

   - 3.4

   - 3.0

   Select the number of nodes for the replica set instance based on your business

   **Primary and Secondary**

   requirements.

   **Node Count**

   Select the number of read-only

   **Specification Configuration**

   **Number of Read-Only**

   nodes for the replica set

   **Nodes**

   instance based on your business requirements.

   ApsaraDB for MongoDB instances support the following three specification types:

   - **General-Purpose**: The instance has dedicated memory and I/O resources, but shares CPU and storage resources with other general-purpose instances on the same physical machine.

   - **Dedicated**: The instance has fully dedicated CPU,

   **Specification Type**

   memory, storage, and I/O resources. It delivers consistently stable performance and remains unaffected by the behavior of other instances on the same physical machine.

   - **Exclusive Physical Machine**: The top-tier dedicated instance type, also known as the dedicated host type. It exclusively occupies all resources of an entire physical machine.

   Select the node specification as needed. For specific

   **Node Specification**

   specification parameters, see the console.

   The storage capacity of the instance includes data space, system file space, log file space, and transaction file

   **Storage Capacity (MB)**

   space. For more information, see **Replica set instance specifications in** ***ApsaraDB for MongoDB Product Over view***.

   ApsaraDB for MongoDB instances support the following network types:

   - **Classic Network**: Cloud services on the classic network do not isolate network traffic. They rely solely on their own security groups or allowlist policies to block unauthorized access.

   - **Virtual Private Cloud**: A Virtual Private Cloud (VPC) helps you build an isolated

   **Network Type**

   network environment on Alibaba Cloud. You can customize the route table, IP address range, and gateway of your VPC. We recommend that you select VPC for enhanced security.

   > **Note**
   >
   > After you select **VPC**, you must select the corresponding **VPC** and **vSwitch**.

   - **IPv4**: Assigns only IPv4 addresses. This option applies to pure IPv4 network environments.

   - **IPv4/IPv6 Dual-Stack**: Assigns both IPv4 and IPv6 addresses. This option applies to hybrid network scenarios that require simultaneous access from IPv4 and IPv6 clients. After enabling this option, you must configure an IPv6 allowlist to control access from IPv6 addresses.

     > **Note**
     >
     > - To configure this parameter, you must enable the IPv6 switch. For more information, see the section on

   **IP Type**

   > enabling the MongoDB IPv6 switch in the ***O& M Guide***.
   >
   > - If the system prompts an unauthorized access, see Authorize a tenant organization to access SLB.

   Select your VPC. If you have not created a VPC, click **Create VPC** next to the VPC drop-down list to create one.

   **Virtual Private Cloud (VPC**)

   > **Note**
   >
   > This parameter is required

   **Network**

   > when you set **Network Type** to **Virtual Private Cloud**.

   Select a vSwitch in the VPC. If you have not created a vSwitch, click **Create Switch** next to the vSwitch drop-down list to create one.

   **Switch (vSwitch)**

   > **Note**
   >
   > You must specify this parameter when you set **Network Type** to **Virtual Private Cloud**.

   Add IPv4 addresses to allow these IP addresses to access the MongoDB instance.

   > **Note**
   >
   > We recommend that you use RFC private network

   **IPv4 Whitelist**

   > addresses as the CIDR blocks of the VPC, such as 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.

   Add IPv6 addresses to allow these IP addresses to access the MongoDB instance.

   > **Note**
   >
   > The IPv6 allowlist supports the following address formats:
   >
   > - An IPv6 address consists of eight groups of four hexadecimal digits separated by colons (:). Example: 2001:0db8:0000:0 000:0000:0000:00 00:0001. You can use the abbreviated form, such as 2001:db8::1, where consecutive zero segments are replaced with :: (only once).

   **IPv6 Whitelist**

   > - Append a prefix length (a slash followed by an integer from 0 to
   >
   >   128. to specify an
   >
   >   IP address range. Example: 2001:db8::/32.
   >
   > - fc00::/7: Unique Local Address (ULA), similar to the IPv4 192.168 address range. This format is for private network use only. (Recommended)
   >
   > - ::/0: This address represents all IPv6 addresses. We do not recommend this format for production environments.
   >
   > - fe80::/10: Link-Local Address, similar to the IPv4 169.254.x.x range. This format enables automatic configuration and direct communication for devices on a local network. We do not recommend this format.

   Customize the instance name of the MongoDB database according to the following rules:

   - The name must start with a letter.

   **Instance Name**

   - The name can contain digits,letters, underscores (_), and hyphens (-).

   - The name must be 2 to 256 characters in length.

   Select one of the following methods to set the login password for the MongoDB database:

   - **Set Immediately**: Set the login password for the MongoDB database

   **Set Password**

   immediately.

   - **Set After Creation**: Set the login password for the MongoDB database after the instance is created. For more information, see Reset a password.

   Set the login password for the MongoDB database according to the following requirements:

   - The password must contain at least three of the following character types:

   **Password Settings**

   uppercase letters, lowercase letters, digits, and special characters. Supported special characters:

   !#$%^&\*()_+=

   - The password must be 8 to 32 characters in length.

   **Logon Password**

   > **Note**
   >
   > This parameter is required when you set **Set Password** to **Set Immediately**.

   Enter the password again. Make sure that the two passwords match.

   > **Note**

   **Confirm Password**

   > This parameter is required when you set **Set Password** to **Set Immediately**.

5. Before you create the instance, check the overall configuration of the instance in the **Configuration Overview** panel on the right side of the page to ensure that the configuration meets your requirements.

   If your quota is insufficient, click **Manage** to configure the quota. For more information, see the **Quota management** section in the ***Apsara Uni-manager Management Console U ser Guide***.

6. Click **Submit**.

<a id="section-6-1-2"></a>

### 6.1.2. Create a sharded cluster instance

This topic describes how to create a sharded cluster instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click **+ Create an instance**.

4. On the **Create a MongoDB instance - Sharding** page, configure the parameters described in the following table.

   **Section**

   **Parameter**

   **Description**

   **Organization**

   The organization where you want to deploy the instance.

   **Basic configuration**

   **Resource Set**

   The resource set where you want to deploy the instance.

   **Region**

   The region where you want to deploy the instance.

   - **Single Availability Zone**: The primary, secondary, and hidden nodes are deployed in one zone.

   - **Dual Availability Zones**: The primary, secondary, and hidden nodes are deployed in two zones to meet the

   **Deployment**

   requirements of zone-disaster recovery.

   **method**

   - **Three Availability Zones**: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone-disaster recovery.

   Select a primary zone for the instance.

   **Region**

   > **Note**

   **Primary**

   > If you select dual-zone, the instance supports zone-

   **Availability**

   > disaster recovery across two data centers.

   **Zone**

   The zone in which the secondary instance is deployed.

   **Secondary**

   > **Note**

   **Availability**

   > This parameter is required only when you select **Dual**

   **Zone**

   > **Availability Zones** or **Three Availability Zones** for the Deployment method parameter.

   Select the third availability zone for the instance.

   **Third**

   > **Note**

   **Availability**

   > This parameter is required only when you select

   **Zone**

   > **Three Availability Zones** for the Deployment method parameter.

   The chip architecture of the host where you want to deploy the instance.

   **Chip**

   > **Note**

   **architecture**

   > If you do not have permissions to select a chip architecture, contact the operations administrator to grant permissions to your account.

   **Database**

   The database engine of the instance. Set the value to

   **engine**

   **MongoDB**.

   **Specification Configuration**

   The database engine version of the instance. Valid values:

   - 8.0

   - 7.0

   - 6.0

   **Database version**

   - 5.0

   - 4.2

   - 4.0

   - 3.4

   The network type of the instance. Valid values:

   - **Classic Network**: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service.

   - **Virtual Private Network**: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR

   **Network type**

   blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type.

   > **Note**
   >
   > If you select the **Virtual Private Network** network type, you must specify the **Virtual Private Cloud (VPC)** and **Switch vswitch** parameters.

   - **IPv4**: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks.

   - **Dual-Stack (IPv4/IPv6)**: assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance.

   **IP Type**

   > **Note**
   >
   > - To configure this parameter, you must enable IPv6 first. For more information, see the "Enable IPv6 for ApsaraDB for MongoDB" topic in **O&M Guide**.
   >
   > - If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB.

   The VPC where you want to deploy the instance. If no VPCs are available, click **Create a VPC** to the right of the drop-down list.

   > **Note**

   **Virtual Private Cloud (VPC)**

   > If **Network type** is set to **Virtual Private Network**, this parameter is required.

   The vSwitch in the VPC. If no vSwitches are available, click **Create a switch** to the right of the drop-down list.

   **Switch vswitch**

   > **Note**
   >
   > If **Network type** is set to **Virtual Private Network**, this parameter is required.

   Add IPv4 addresses that are allowed to access the

   **Network**

   ApsaraDB for MongoDB instance.

   > **Note**

   **IPv4 Whitelist**

   > We recommend that you use private CIDR blocks defined in RFC 1918 for the VPC, such as 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16.

   Add IPv6 addresses that are allowed to access the ApsaraDB for MongoDB instance.

   > **Note**
   >
   > Take note of the following requirements when you add addresses to the IPv6 whitelist:
   >
   > - An IPv6 address consists of eight segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0000:0000:0000:0000:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once.
   >
   > - The prefix length must be specified, which is an integer from 0 to 128, following a forward

   **IPv6 Whitelist**

   > slash (/). Example: 2001:db8::/32.
   >
   > - fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address.
   >
   > - ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments.
   >
   > - fe80::/10 is a link-local address similar to IPv4 addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it.

   The specifications of the mongos node. You can log in to

   **Mongos**

   the ApsaraDB for MongoDB console to view the detailed

   **specification**

   specifications.

   **Mongos specification**

   The number of mongos nodes. You can select 2 to 32

   **Quantity**

   **configuration**

   mongos nodes.

   **Custom name**

   The custom name of the mongos node.

   **for mongos**

   The specifications of the shard. You can log in to the

   **Shard**

   ApsaraDB for MongoDB console to view the detailed

   **specification**

   specifications.

   The storage space of the shard. This space stores data,

   **Storage Space**

   system files, log files, and transaction files. For more

   **(GB)**

   information, see **Sharded cluster instance types** in ApsaraDB for MongoDB Product Introduction.

   **Shard specification configuration**

   **Quantity**

   The number of shards. You can select 2 to 32 shards.

   **Shard custom**

   The custom name of the shard.

   **name**

   **Configserver**

   The specifications of the ConfigServer component. Set the

   **specification**

   value to **1 vCPU, 2 GB**.

   **Configserver**

   **Disk Space**

   The storage space of the ConfigServer component. Set the

   **specification**

   **(GB)**

   value to 20.

   **configuration**

   **Custom name for**

   The custom name of the ConfigServer component.

   **configserver**

   The name of the instance. The name must meet the following requirements:

   - It must start with a letter.

   **Instance Name**

   - It can contain digits, letters, underscores (_), and hyphens (-).

   - It must be 2 to 256 characters in length.

   The time when you want to set the password. Valid values:

   - **Set up now**: immediately sets the login password.

   **Set a password**

   - **Set After Creation**: sets the password after the instance is created. For more information, see Reset a password.

   The password used to log in to the instance. The password must meet the following requirements:

   - It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters:

   **Password**

   **Login**

   ! # $ % ^ & \* ( ) _ + =

   **Setup**

   **password**

   - It must be 8 to 32 characters in length.

   > **Note**
   >
   > If **Set a password** is set to **Set up now**, this parameter is required.

   Enter the password again. The password that you enter must be the same as that in Login password.

   **Confirm**

   > **Note**

   **password**

   > If **Set a password** is set to **Set up now**, this parameter is required.

5. Click **Submit**.

<a id="section-6-2"></a>

## 6.2. View the details of an ApsaraDB for MongoDB instance

This topic describes how to view the details of an ApsaraDB for MongoDB instance, such as the basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. Go to the basic information page by using one of the following methods:

   - Find the instance that you want to view and click its ID to go to the **Basic Information** page. Then, you can view the details of the instance.

   - Click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="10" alt=""> in the **Actions** column corresponding to the instance that you want to view and

     select **Manage** to go to the **Basic Information** page. Then, you can view the details of the instance.

<a id="section-6-3"></a>

## 6.3. Restart an instance

This topic describes how to restart an instance when instance connections reach the upper limit or your instances have performance issues. This topic describes how to restart an ApsaraDB for MongoDB instance.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. Click **Restart Instance** in the upper-right corner.

   > **Note**
   >
   > - When an ApsaraDB for MongoDB instance is restarted, all its connections are closed. Plan your operations in advance before you restart an ApsaraDB for MongoDB instance.
   >
   > - You can also find the instance that you want to restart, click
   >
   >   in the **Actions**
   >
   >   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">
   >
   >   column, and then select **Restart**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/9100064aac0eb0398104860aeb753997.png)

5. In the **Restart Instance** message, click **OK**.

<a id="section-6-4"></a>

## 6.4. Change the configurations of a replica set instance

This topic describes how to change the configurations of an ApsaraDB for MongoDB instance. You can upgrade or downgrade an ApsaraDB for MongoDB instance to meet your business requirements.

**Prerequisites**

The instance is a replica set instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances** page, click the ID of an instance, or click

   in the **Actions**

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   column corresponding to the instance and select **Manage**.

4. In the upper-right corner of the Specification Information section of the page that appears, click **Change Configuration** to go to the **Modify Instance** page.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/2fcdf33f59c466ccdb487a25fc3921e3.png)

   > **Note**
   >
   > You can also click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="10" alt=""> in the **Actions** column corresponding to the instance
   >
   > and select **Change Configuration** on the **Replica Set Instances** page to go to the **Modify Instance** page.

5. On the **Modify Instance** page, change the instance configurations.

   You can change the values of the following parameters:

   - **Node Type**

   - **Node Specification**

   - **Storage Capacity (GB)**

6. Click **Submit**.

<a id="section-6-5"></a>

## 6.5. Change the configurations of a sharded cluster instance

<a id="section-6-5-1"></a>

### 6.5.1. Add a mongos node

This topic describes how to add a mongos node to an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

- If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

- When mongos nodes are added, your business keeps running without interruption.

- Typically, mongos nodes are added within 5 minutes. The time required to add mongos nodes is not dependent on the number of mongos nodes being added.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of an instance, or click

   in

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   the **Operation** column corresponding to the instance and select **Manage**.

4. In the **Mongos List** section of the page that appears, click **Add Mongos**.

5. In the **MongoDB sharded cluster add node** panel, click **Add a new item**, and configure the **Specifications** and **Quantity** parameters.

6. Click **Submit**.

<a id="section-6-5-2"></a>

### 6.5.2. Add a shard node

This topic describes how to add a shard node to an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

- If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

- When shard nodes are added, no transient connections occur and business keeps running without interruption.

- Typically, shard nodes are added within 5 minutes. The time required to add shard nodes does not depend on the number of shard nodes that are being added.

- The specifications of the new shard node must be higher than or equal to the highest specifications among all the shard nodes in the sharded cluster instance.

  For example, if the largest storage capacity among all the shard nodes in a sharded cluster instance is 10 GB, the storage capacity of the new shard node must be greater than or equal to 10 GB.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of an instance, or click

   in

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   the **Operation** column corresponding to the instance and select **Manage**.

4. In the **Shard List** section, click **Add Shard**.

5. On the **Add Nodes to MongoDB Sharded Cluster** page, configure the **Specifications**, **Username**, and **Password** parameters. Then, click **Confirm Password**.

   > **Note**
   >
   > - When you change the value of the **Storage Capacity (GB)** parameter, make sure that the new storage capacity that you specify is greater than or equal to the largest storage capacity among all the shard nodes in the sharded cluster instance.
   >
   > - The specifications of the new shard node must be higher than or equal to the highest specifications among all the shard nodes in the sharded cluster instance. For example, if the largest storage capacity among all the shard nodes in the sharded cluster instance is 10 GB, the storage capacity of the new shard node must be greater than or equal to 10 GB.

6. Click **Submit**.

<a id="section-6-5-3"></a>

### 6.5.3. Change the configurations of one or more mongos nodes

This topic describes how to change the configurations of one or more mongos nodes in an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

- During a configuration change, one or two transient connections may occur. Each transient connection lasts about 30 seconds. To prevent a configuration change from interrupting your workloads, we recommend that you change configurations at a time that has minimal impact on your business.

- The amount of time required to perform a configuration change depends on factors such as the network conditions, task queue status, and data size. We recommend that you change the configurations of a sharded cluster instance during off-peak hours and make sure that your application can automatically reconnect to the instance.

- If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of an instance, or click

   in

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   the **Operation** column corresponding to the instance and select **Manage**.

4. In the **Mongos List** section of the page that appears, change the configurations of one or more mongos nodes based on your business requirements.

   - Change the configurations of a mongos node

     Find the mongos node that you want to manage and click the

     icon in the

     **Actions** column. Then, select **Change Configuration**.

   - Change the configurations of multiple mongos nodes

     <ol type="a">

     <li>

     In the **Mongos List** section of the page that appears, select the mongos nodes that you want to manage.

     </li>

     <li>

     In the upper-left corner of the **Mongos List** section, click **Batch Reconfigure**.

     </li>

     </ol>

5. In the **MongoDB sharded cluster configuration node** panel, configure the **Specification configuration** parameter.

6. Click **Submit**.

<a id="section-6-5-4"></a>

### 6.5.4. Change shard node configurations

This topic describes how to change the configurations of one or more shard nodes in an ApsaraDB for MongoDB sharded cluster instance, such as the specification and storage capacity.

**Precautions**

- During a configuration change, one or two transient connections may occur, each lasting approximately 30 seconds. You can set the effective time of the change as needed to avoid impact on your business.

  > **Warning**
  >
  > When you change only the storage capacity, the system performs different operations based on whether the local host has sufficient storage resources.
  >
  > - Sufficient: The system scales out storage locally without cross-host migration or switchover. No transient connections occur during the change, and the task takes effect immediately without waiting for the maintenance window.
  >
  > - Insufficient: The system must perform cross-host migration and switchover. Transient connections occur during the change, and the task takes effect within the specified effective time.

- The completion time of a configuration change depends on multiple factors such as network conditions, task queue, and data volume. We recommend that you perform configuration changes during off-peak periods and make sure that your applications have an automatic reconnection mechanism.

- If the minor version of your database is expired or not in the maintenance list, the system automatically upgrades the minor version to the latest version to deliver better performance and stability.

- The storage capacity that you select during a configuration change must be greater than or equal to the storage capacity currently occupied by the shard node.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of an instance, or click

   in

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   the **Operation** column corresponding to the instance and select **Manage**.

4. In the **Shard List** section, change the configurations of one or more shard nodes as needed.

   - Change the configurations of one shard node

     Click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/2c6465f63839a65bed842daccde123ca.png" width="10" alt=""> in the **Operation** column of the target shard node row and select **Change**

     **Configurations**.

   - Change the configurations of multiple shard nodes

     <ol type="a">

     <li>

     In the **Shard List** section, select the target shard nodes.

     </li>

     <li>

     Click **Batch Change Configurations** in the upper-left corner of the **Shard List** section.

     </li>

     </ol>

5. On the **Change Shard Node Configurations for MongoDB Sharded Cluster** page, set the **Specifications,** **Storage Capacity**, and **Number of Replicas**.

6. Click **Submit**.

<a id="section-6-5-5"></a>

### 6.5.5. Change the configurations of a Configserver node

This topic describes how to change the configurations of a Configserver node in an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

- During a configuration change, one or two transient connections may occur. Each transient connection lasts about 30 seconds. To prevent a configuration change from interrupting your workloads, we recommend that you change configurations at a time that has minimal impact on your business.

- The amount of time required to perform a configuration change depends on factors such as the network conditions, task queue status, and data size. We recommend that you change the configurations of a sharded cluster instance during off-peak hours and make sure that your application can automatically reconnect to the instance.

- If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of an instance, or click

   in

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   the **Operation** column corresponding to the instance and select **Manage**.

4. In the **ConfigServer List** section of the page that appears, find the Configserver node that

   you want to manage and click the

   icon in the **Actions** column. Then, select

   **Change Configuration**.

5. In the **MongoDB sharded cluster configuration node** panel, configure the **ConfigServer specification** and **Disk space (GB)** parameters.

6. Click **Submit**.

<a id="section-6-6"></a>

## 6.6. Change the name of an instance

This topic describes how to change the name of an ApsaraDB for MongoDB instance to facilitate management.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. Click **Edit** to the right of **Instance Name**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/9e1b11c3ea64569b8028d68ed4d114c6.png)

   > **Note**
   >
   > - The name must start with a letter. The name cannot start with http:// or https://.
   >
   > - The name can contain letters, underscores (_), hyphens (-), and digits.
   >
   > - The name must be 2 to 128 characters in length.

5. Click **OK**.

<a id="section-6-7"></a>

## 6.7. Upgrade the MongoDB version of an instance

ApsaraDB for MongoDB allows you to upgrade the MongoDB version of your instance. This topic describes how to upgrade the MongoDB version of your instance.

**Usage notes**

- Nodes in an instance are upgraded in turn. An instance is automatically restarted two or three times during an upgrade. We recommend that you perform the upgrade during off-peak hours or make sure that your application can automatically reconnect to the instance.

- The balancer of a sharded cluster instance is disabled during an upgrade and is enabled after the upgrade.

- The amount of time required to upgrade the MongoDB version of an instance is related to the data volume of databases in the instance. We recommend that you schedule your upgrade task during off-peak hours.

- You cannot downgrade the MongoDB version of an instance after you upgrade it.

**MongoDB versions available for upgrades**

The following table lists the MongoDB versions to which ApsaraDB for MongoDB instances of different architectures and versions can be upgraded.

<table>
  <tr>
    <th>Instance architecture</th>
    <th>MongoDB version before upgrade</th>
    <th>MongoDB version after upgrade</th>
  </tr>
  <tr>
    <td rowspan="4">Replica set instances</td>
    <td>MongoDB 4.2</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>MongoDB 4.0</td>
    <td>MongoDB 4.2</td>
  </tr>
  <tr>
    <td>MongoDB 3.4</td>
    <td>MongoDB 4.0 or MongoDB 4.2</td>
  </tr>
  <tr>
    <td>MongoDB 3.0</td>
    <td>MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2</td>
  </tr>
  <tr>
    <td rowspan="3">Sharded cluster instances</td>
    <td>MongoDB 4.2</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>MongoDB 4.0</td>
    <td>MongoDB 4.2</td>
  </tr>
  <tr>
    <td>MongoDB 3.4</td>
    <td>MongoDB 4.0 or MongoDB 4.2</td>
  </tr>
</table>

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. Find the instance that you want to manage and click the ID of the instance.

4. In the upper-right corner of the **Specification Information** section of the page that appears, click **Upgrade Database** and select the version to which you want to upgrade the instance.

5. In the **Upgrade Database** message, click **OK**.

<a id="section-6-8"></a>

## 6.8. Switch node roles

You can switch the node roles of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console based on your business deployment.

**Typical scenario**

When an Elastic Compute Service (ECS) instance and an ApsaraDB for MongoDB instance are connected in the same zone over an internal network, the latency is minimal. If they are connected across different zones, the latency increases and the performance of the ApsaraDB for MongoDB instance and your business is affected.

![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/700eb896fbe226c11f8c85f1a98bca08.png)

In this example, the ECS instance to which the application belongs is in Zone 2. If the primary node of the ApsaraDB for MongoDB instance is in Zone 1, the ECS instance needs to connect to the primary node across zones.

To optimize the business deployment architecture, you can switch roles between the primary and secondary nodes. In this example, you can change the role of the node in Zone 2 to primary and the role of the node in Zone 1 to secondary. The ECS and ApsaraDB for MongoDB instances can be connected in the same zone.

**Precautions**

- Each time you switch node roles, the instance may experience a transient connection of up to 30 seconds. Perform this operation during off-peak hours or make sure that your application can automatically re-establish a connection.

- Each time you switch node roles, only the node roles are changed and the zones and role IDs of nodes remain unchanged.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Service Availability**.

5. On the **Service Availability** page, perform the subsequent operations based on the corresponding instance architecture.

   - Replica set instances

     <ol type="a">

     <li>

     Click **Switch Role** in the upper-right corner of the page.

     </li>

     <li>

     In the **Switch Role** panel, select the node for which you want to switch the role.

     ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/82689887764a74fc3caf9ad3271b41c3.png)

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Click **OK**.

     </li>

     </ol>

   - Sharded cluster instances

     > **Note**
     >
     > For sharded cluster instances, you can manage only the zone distribution
     >
     > of shard and Configserver nodes.

     <ol type="a">

     <li>

     In the upper-right corner of the **Zone Distribution for Shards** or **Zone Distribution for Configservers** section, click **Switch Role**.

     </li>

     <li>

     In the **Switch Role** panel, select the node for which you want to switch the role.

     ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/24f0100ce10b10e979376df4609b45eb.png)

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Click **OK**.

     </li>

     </ol>

<a id="section-6-9"></a>

## 6.9. Migrate an instance across multiple zones

This topic describes how to migrate an ApsaraDB for MongoDB instance to a different zone within the same region. After an ApsaraDB for MongoDB instance is migrated to a different zone, the attributes, specifications, and connection addresses of the instance remain unchanged.

**Prerequisites**

- The ApsaraDB for MongoDB instance is a replica set instance or sharded cluster instance that runs MongoDB 4.2 or earlier.

- Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance.

- The source zone and the destination zone belong to the same region.

- If the instance is deployed in a virtual private cloud (VPC), make sure that a vSwitch is created in the destination zone before you start migration. For more information, see **Create a VPC** and **Create a vSwitch** in **VPC User Guide**.

- The ApsaraDB for MongoDB instance does not have a public endpoint. If you have applied for a public endpoint, you must release the public endpoint before you migrate the ApsaraDB for MongoDB instance to a different zone. For more information about how to release a public endpoint, see Release a public endpoint.

**Precautions**

- If the ApsaraDB for MongoDB instance resides in a VPC, the destination zone must also belong to the same VPC.

- The amount of time that is required for the migration varies based on factors such as the network conditions, task queue state, and data volume. We recommend that you migrate the instance during off-peak hours.

- During the migration, you may experience transient connections that last about 30 seconds. Make sure that your application is configured to automatically reconnect to the ApsaraDB for MongoDB instance.

- After the migration, the virtual IP addresses (VIPs) of the ApsaraDB for MongoDB instance change. A sample VIP is 172.16.88.60. If your application is connected to the ApsaraDB for MongoDB instance by using an original VIP after the migration, the application disconnects from the instance.

  > **Note**
  >
  > We recommend that you connect your application to the ApsaraDB for
  >
  > MongoDB instance by using a connection string URI of the instance to ensure high availability. For more information, see Overview of replica set instance connections and Overview of sharded cluster instance connections.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the **Basic Information** section, click **Change Zone**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/1db07a14e8557fea4f6c55684a52b018.png)

5. In the **Migrate Instance to Other Zone** panel, configure the parameters based on the network type of the instance.

   - Migrate an ApsaraDB for MongoDB instance in a VPC to a different zone

     ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/f73055aa243a0e1106be2d9bc4004c36.png)

     | Parameter | Description |
     | --- | --- |
     | Migrate To | Select the destination zone. |
     | Select a vSwitch | Select the destination vSwitch. |
     | Migration Time | Select the time when you want to start the migration. Valid values:<br>• <strong>Switch Immediately after Migration</strong>: The migration immediately starts after you configure the parameters.<br>• <strong>Switch within Maintenance Window</strong>: The migration starts during the specified period. You can click <strong>Edit</strong> to the right of <strong>Switch within</strong> <strong>Maintenance Window</strong> to change the period. |

   - Migrate an ApsaraDB for MongoDB instance in the classic network to a different zone

     ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/302c878e019338f26b7809f0c98a9c47.png)

     | Parameter | Description |
     | --- | --- |
     | Migrate To | Select the destination zone. |
     | Migration Time | Select the time when you want to start the migration. Valid values:<br>• <strong>Switch Immediately after Migration</strong>: The migration immediately starts after you configure the parameters.<br>• <strong>Switch within Maintenance Window</strong>: The migration starts during the specified period. You can click <strong>Edit</strong> to the right of <strong>Switch within</strong> <strong>Maintenance Window</strong> to change the period. |

6. Read the prompt and select the check box.

7. Click **Submit**.

<a id="section-6-10"></a>

## 6.10. Release an ApsaraDB for MongoDB instance

This topic describes how to manually release an ApsaraDB for MongoDB instance to meet your business needs.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. On the page that appears, click **Release** in the lower-right corner of the **Basic Information** section.

   > **Note**
   >
   > You can also click
   >
   > in the **Actions** column corresponding to the instance
   >
   > <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">
   >
   > and select **Release**.

5. In the **Release Instance** message, click **OK**.

   > **Warning**
   >
   > After you release an ApsaraDB for MongoDB instance, data in the
   >
   > instance can no longer be recovered. Proceed with caution.

<a id="section-6-11"></a>

## 6.11. Primary/secondary failover

<a id="section-6-11-1"></a>

### 6.11.1. Configure a primary/secondary switchover for a replica set instance

By default, an ApsaraDB for MongoDB replica set instance consists of three nodes. ApsaraDB for MongoDB provides connection strings for you to connect to the primary node and a secondary node. The other secondary node is hidden as a backup to ensure high availability (HA). If a node fails, the HA system of ApsaraDB for MongoDB automatically triggers a primary/secondary switchover to ensure the availability of the instance. You can also manually trigger a primary/secondary switchover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills.

**Prerequisites**

The instance is in the **Running** state.

**Background information**

After a primary/secondary switchover is triggered for a replica set instance, the system switches roles between the primary and secondary nodes in the instance.

**Precautions**

Each time you trigger a primary/secondary switchover for an instance, the instance may experience a transient connection of up to 30 seconds. Make sure that your applications can automatically re-establish a connection.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** page, click the ID of an instance, or click

   in the **Actions**

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   column corresponding to the instance and select **Manage**.

3. In the **Node List** section, click **Failover**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/e34fc68e3dbba33ca755448e07a2494a.png)

4. In the **Failover** message, click **OK**.

5. The instance state changes to **Switching Role**. When the instance state changes to **Running**, the switchover is successful.

   > **Note**
   >
   > - The switchover operation is complete in about 1 minute.
   >
   > - After the switchover operation, you must use the connection string of the new primary node to connect to the instance if your original connection uses the connection string of the original primary node. This is because the original primary node becomes a secondary node that has no write permissions after the switchover. For more information, see Overview of replica set instance connections.

<a id="section-6-11-2"></a>

### 6.11.2. Configure a primary/secondary failover for a sharded cluster instance

By default, each shard or Configserver node of a sharded cluster instance consists of three nodes. If a node fails, the high availability system of ApsaraDB for MongoDB automatically triggers a primary/secondary failover to ensure the availability of the shard or Configserver node. You can also manually trigger a primary/secondary failover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills.

**Prerequisites**

The instance is in the **Running** state.

**Background information**

After a primary/secondary failover is triggered, the system switches roles between the primary and secondary nodes in a shard node.

**Precautions**

Each time you trigger a primary/secondary failover for an instance, the instance may experience a transient connection of up to 30 seconds. We recommend that you perform this operation during off-peak hours and ensure that your applications can automatically re-establish a connection.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the **Shard List** or **ConfigServer List** section, click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/2c42747ff0594c8f986d07e3af2f3cc4.png" width="3" alt=""> in the **Actions** column

   corresponding to the node for which you want to perform failover and select **Failover**.

   > **Note**
   >
   > You can separately trigger a primary/secondary failover for each shard
   >
   > node. The failover operation takes effect only for the current shard node and does not affect other shard nodes of the same sharded cluster instance.

5. In the **Failover** message, click **OK**.

   > **Note**
   >
   > The failover operation is complete in about one minute.

<a id="section-6-12"></a>

## 6.12. View monitoring data

This topic describes the performance metrics provided by ApsaraDB for MongoDB to check the status of ApsaraDB for MongoDB instances. You can view instance monitoring data in the ApsaraDB for MongoDB console.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Monitoring Data**.

5. On the page that appears, specify a time range to view the monitoring data.

   Instance monitoring data is collected every 300 seconds.

   | Metric | Description |
   | --- | --- |
   | CPU utilization | cpu_usage: the CPU utilization of the instance. |
   | Memory usage | mem_usage: the memory usage of the instance. |
   | IOPS usage | The IOPS of the instance. The following items are included:<br>• data_iops: the IOPS of the data disk.<br>• log_iops: the IOPS of the disk that stores logs. |
   | IOPS usage percentage | iops_usage: the ratio of the IOPS used by the instance to the maximum IOPS allowed. |
   | Disk usage | The total disk space used by the instance. The following items are included:<br>• ins_size: the total space used.<br>• data_size: the disk space used by data files.<br>• log_size: the disk space used by log files. |
   | Disk usage percentage | disk_usage: the ratio of the total disk space used by the instance to the maximum disk space that can be used. |
   | QPS | The queries per second (QPS) of the instance. The following items are included:<br>• The number of insert operations.<br>• The number of query operations.<br>• The number of delete operations.<br>• The number of update operations.<br>• The number of getMore operations.<br>• The number of command operations. |
   | Connections | current_conn: the number of current connections to the instance. |
   | Cursors | The number of cursors used by the instance. The following items are included:<br>• total_open: the number of cursors that are opened.<br>• timed_out: the number of cursors that timed out. |
   | Network traffic | The network traffic of the instance. The following items are included:<br>• bytes_in: the inbound network traffic.<br>• bytes_out: the outbound network traffic.<br>• num_requests: the number of requests that are processed. |
   | Read/write queues | The length of the queues that are waiting for global locks for the instance.The following items are included:<br>• gl_cq_total: the length of the queue that is waiting for both global read and write locks.<br>• gl_cq_readers: the length of the queue that is waiting for global read locks.<br>• gl_cq_writers: the length of the queue that is waiting for global write locks. |
   | WiredTiger | The cache metrics of the WiredTiger engine used by the instance. The following items are included:<br>• bytes_read_into_cache: the amount of data that is read into the cache.<br>• bytes_written_from_cache: the amount of data that is written from the cache to the disk.<br>• maximum_bytes_configured: the size of the maximum available disk space that is configured. |
   | Primary/secondary replication latency | repl_lag: the latency in data synchronization between the primary and secondary nodes of the instance. |

<a id="section-6-13"></a>

## 6.13. Recycle bin

The recycle bin of ApsaraDB for MongoDB is used to retain released ApsaraDB for MongoDB instances. You can rebuild or destroy instances in the **recycle bin**.

After an ApsaraDB for MongoDB instance is released, it is retained in the recycle bin for seven days before the instance is released from the recycle bin. After the instance is released from the recycle bin, the instance data cannot be restored. Proceed with caution.

**Rebuild an instance**

> **Note**
>
> Only **released** ApsaraDB for MongoDB instances can be **rebuilt**.

1. Log on to the ApsaraDB for MongoDB console

2. In the left-side navigation pane, click **Recycle Bin**.

3. Find the instance that you want to rebuild and click **Reconstruction Recovery** in the **Operation** column.

4. On the **MongoDB Clone Instance** page, configure the **Availability Zone**, **Specification Type**, **Node Specifications**, and **Storage space** parameters and the parameters in the **Network**, and **Password Settings** sections.

5. Click **Submit**.

**Destroy an instance**

> **Warning**
>
> After an ApsaraDB for MongoDB instance is destroyed, the instance data is cleared and cannot be restored.

1. Log on to the ApsaraDB for MongoDB console

2. In the left-side navigation pane, click **Recycle Bin**.

3. Find the instance that you want to destroy and click **Destroy immediately** in the **Operation** column.

4. In the message that appears, click **OK**.

<a id="section-7"></a>

# 7.Account management

<a id="section-7-1"></a>

## 7.1. Create an account

This topic describes how to create an account for an ApsaraDB for MongoDB instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Accounts**.

5. Click **Create Account** in the upper part of the page.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/ffdb4a8e67e407c80900eb9597c81f83.jpeg)

6. In the **Create Account** panel, enter the account name and password, and grant database permissions to the account based on your business requirements.

7. Click **OK**.

> **Note**
>
> After you create the account, you can reset the password, modify permissions, or delete the account in the account list.

<a id="section-7-2"></a>

## 7.2. Reset the password

This topic describes how to reset the password of an account in the ApsaraDB for MongoDB console. For data security purposes, we recommend that you change the password of your account on a regular basis.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Accounts**.

5. Find the account for which you want to change the password and click **Reset Password** in the **Operation** column.

6. In the **Reset account password** dialog box, configure the following parameters.

   | Parameter | Description |
   | --- | --- |
   | New Password | • The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:<br>! # $ % ^ &amp; \* ( ) _ + - =<br>• The password must be 8 to 32 characters in length.<br>• You must not use keywords such as Admin or Password. |
   | Confirm new password | Enter the password again. The password you enter must be the same as that in New Password. |

7. Click **OK**.

<a id="section-7-3"></a>

## 7.3. Lock an account

You can lock and unlock database accounts in the console.

**Prerequisites**

If your business ends or changes, you can lock unnecessary privileged accounts and standard accounts in the console.

**Lock an account**

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the target instance.

3. In the left-side navigation pane, click **Accounts**.

4. In the **Operation** column of the target account, click **Lock**.

5. In the pop-up dialog box, click **OK**.

**Unlock an account**

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the target instance.

3. In the left-side navigation pane, click **Accounts**.

4. In the **Operation** column of the target account, click **Unlock**.

5. In the pop-up dialog box, click **OK**.

<a id="section-8"></a>

# 8.Parameter configuration

<a id="section-8-1"></a>

## 8.1. Set instance parameters

You can view and modify the values of certain parameters and query the parameter modification history in the ApsaraDB for MongoDB console.

**Precautions**

- When you modify a parameter value, refer to the **Modifiable Parameter Values** column on the parameter list page.

- Some parameters require you to restart the instance after they are modified. For more information, see the **Restart Required** column on the **Parameter List** page in the console. Perform this operation during off-peak hours and ensure that your application has a reconnection mechanism.

**Modify parameter values**

1. Log on to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the target instance.

4. In the navigation pane on the left, choose **Parameter Settings > Parameter List**.

5. Click **Batch Modify**. On the **Modify Parameters** page, select the target parameter and modify its value.

6. Click **OK**.

**View parameter modification history**

1. Log on to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the target instance.

4. In the navigation pane on the left, choose **Parameter Settings > Modification History**.

5. On the modification history page, select a time range and click **OK**.

**Parameter descriptions**

**Replica set parameter descriptions**

| Parameter name | Default value | Recomm ended value | Confirm restart? | Value range | Parameter description | Applicable versions and notes |
| --- | --- | --- | --- | --- | --- | --- |
| auditLog.au thSuccess | true | true | A restart is not required. | true\|false | Specifies whether to audit successful authenticatio n operations for CRUD operations and commands. | 3.0+ (3.4, 3.6, 4.0, 4.2) |
| auditLog.op Filter | admin,sl ow | admin,slo w | No restart is required. | <code>.*</code> | An audit log filter option.You can specify the operation types to audit. It supports any combination of <code>auth,admin</code><br><code>,slow,insert</code><br><code>,update,dele</code><br><code>te,command,q</code> <code>uery,pbwm </code>, or <code> all </code> /<code> off </code>. The \`all\` and \`off\` values cannot be used with other combinations. | All 3.0+ versions |
| auditLog.vip Only | true | true | A restart is not required. | true\|false | Specifies whether to audit only the CRUD operations and commands that are connected through a virtual IP address (VIP). | 3.0+ (3.4 to 4.2) |
| net.compre ssion.compr essors | snappy,z std,zlib | snappy,zst d,zlib | A restart is required. | snappy\|zlib\| zstd\|snappy,zstd,zlib\|dis abled | Sets the network compression algorithm for mongod or mongos. | 5.0 to 7.0 Earlier versions (3.4 to 4.2) support only \`snappy \| disabled\` or \`snappy \| zlib\`. |
| net.listenBa cklog | 511 | 511 | A restart is required. | \[511-1023\] | The length of the TCP backlog queue. | 3.4 to 7.0 (Renamed from <code>net.tcpBa</code> <code>cklog </code> to <code>net.liste</code> <code>nBacklog </code>) |
| net.serviceE xecutor | synchro nous | synchrono us | A restart is required. | synchronou s\|adaptive | Determines the threading and execution model used by mongod or mongos. | 4.0 to 4.2 (This parameter is not available in version 3.4.) |
| net.tls.mod e | disabled | disabled | A restart is required. | disabled\|all owTLS\|pref erTLS\|requir eTLS | The TLS mode for network connections. | 5.0 to 7.0 (Replaces <code>net.ssl.m</code> <code>ode </code>) |
| net.ssl.mod e | disabled | disabled | Requires a restart | disabled\|all owSSL | SSL/TLS mode setting (old name). | 3.4 to 4.2 (Replaced by <code>net.tls.m</code> <code>ode </code>) |

<table>
  <tr>
    <td>operationPr ofiling.mode</td>
    <td>off</td>
    <td>off</td>
    <td>A restart is not required.</td>
    <td>off|slowOp| all</td>
    <td>The database performance profiling level: <code> off </code>: disabled.<code> slowOp </code>: records slow operations.<code> all </code>: records all operations.</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>operationPr ofiling.slow OpThreshol dMs</td>
    <td>100</td>
    <td>100</td>
    <td>A restart is not required.</td>
    <td>[0-65536]</td>
    <td>The threshold in milliseconds for a query to be considered "slow" by the database.The default value is 100 ms.</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>replication.e nableMajorit yReadConc ern</td>
    <td>true</td>
    <td>true</td>
    <td>You need to restart.</td>
    <td>true|false</td>
    <td>Specifies whether to enable support for majority read concern.</td>
    <td>4.0 to 4.2 (Enabled by default and cannot be disabled in versions 5.0 and later.)</td>
  </tr>
  <tr>
    <td>replication.o plogGlobalI d</td>
    <td>false</td>
    <td>A number, such as 4617</td>
    <td>You need to restart.</td>
    <td><code> .* </code> (any string or number)</td>
    <td>The global ID (GID). The default value is the replSetName.This parameter is used for two-way synchronizati on scenarios.</td>
    <td>3.0+ (3.4 to 7.0)</td>
  </tr>
  <tr>
    <td>replication.o plogGlobalI dEnabled</td>
    <td>false</td>
    <td>false</td>
    <td>A restart is required.</td>
    <td>true|false</td>
    <td>When enabled, GID is used to support two-way synchronizati on.</td>
    <td>3.0+ (3.4 to 7.0)</td>
  </tr>
  <tr>
    <td>replication.o plogSizeMB</td>
    <td>1024</td>
    <td>Modifiable</td>
    <td>No restart is required.</td>
    <td>[1024-107374182 4]</td>
    <td>The maximum size of the oplog table in MB.</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>rsconf.write ConcernMaj orityJournal Default</td>
    <td>true</td>
    <td>true</td>
    <td>No restart is required.</td>
    <td>true|false</td>
    <td>Specifies whether to require that the journal is persisted when the write concern is `majority`.</td>
    <td>5.0 to 7.0 (Dynamic setting is not supported in 4.x versions.)</td>
  </tr>
  <tr>
    <td>security.aut horization</td>
    <td>enabled</td>
    <td>enabled</td>
    <td>A restart is required.</td>
    <td>enabled|dis abled</td>
    <td>Specifies whether to enable role-based access control (RBAC).</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>security.jav ascriptEnabl ed</td>
    <td>true</td>
    <td>true</td>
    <td>A restart is required.</td>
    <td>true|false</td>
    <td>Specifies whether to allow the execution of JavaScript scripts, such as <code> $where </code> and `mapReduce`.</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>setParamet er.cursorTi meoutMillis</td>
    <td>600000</td>
    <td>600000</td>
    <td>No restart is required.</td>
    <td>[1-214748364 7]</td>
    <td>The timeout period for idle cursors in milliseconds.The default value is 10 minutes.Cursors that are idle for longer than this period are automatically purged by MongoDB.</td>
    <td>All 3.0+ versions</td>
  </tr>
  <tr>
    <td>setParamet er.enableFlo wControl</td>
    <td>true</td>
    <td>true</td>
    <td>A restart is not required.</td>
    <td>true|false</td>
    <td>Specifies whether to enable the flow control mechanism for replica sets. This prevents secondary nodes from lagging too far behind.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.flowContr olTargetLag Seconds</td>
    <td>10</td>
    <td>10</td>
    <td>No restart is required.</td>
    <td>[1-600]</td>
    <td>The target maximum majority commit lag in seconds when flow control is enabled.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.internalQ ueryMaxBlo ckingSortMe moryUsage Bytes</td>
    <td>3355443 2</td>
    <td>33554432</td>
    <td>A restart is not required.</td>
    <td>[33554432-268435456]</td>
    <td>The maximum amount of memory in bytes that can be used for the sorting stage of a query.The default value is 32 MB.</td>
    <td>5.0 to 7.0 (Equivalent to <code>internalQ</code><br><code>ueryExecMa</code><br><code>xBlockingS</code><br><code>ortBytes</code> in versions 3.4 to 4.2)</td>
  </tr>
  <tr>
    <td>setParamet er.internalQ ueryExecMa xBlockingSo rtBytes</td>
    <td>3355443 2</td>
    <td>33554432</td>
    <td>A restart is not required.</td>
    <td>[33554432-268435456]</td>
    <td>The maximum amount of memory in bytes that can be used for the sorting stage of a query.The default value is 32 MB.</td>
    <td>3.4 to 4.2 (Renamed to <code>internalQ</code><br><code>ueryMaxBlo</code><br><code>ckingSortM</code><br><code>emoryUsage</code> <code>Bytes </code> in versions 5.0 and later)</td>
  </tr>
  <tr>
    <td>setParamet er.logicalSe ssionRefres hMillis</td>
    <td>300000</td>
    <td>300000</td>
    <td>A restart is required.</td>
    <td>[60000-1800000]</td>
    <td>The interval in milliseconds at which the logical session cache refreshes the primary session store.The default value is 5 minutes.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.maxInde xBuildMemo ryUsageMeg abytes</td>
    <td>200</td>
    <td>200</td>
    <td>A restart is not required.</td>
    <td>[50-200]</td>
    <td>The maximum total memory in MB that can be consumed by all index creation processes on a single collection.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.maxNum ActiveUserI ndexBuilds</td>
    <td>3</td>
    <td>3</td>
    <td>A restart is not required.</td>
    <td>[1-5]</td>
    <td>The maximum number of concurrent user-initiated index builds on the primary node.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.maxSessi ons</td>
    <td>1000000</td>
    <td>1000000</td>
    <td>A restart is required.</td>
    <td>[1000-1000000]</td>
    <td>The maximum number of sessions that can be cached.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.maxTran sactionLock RequestTim eoutMillis</td>
    <td>5</td>
    <td>5</td>
    <td>A restart is not required.</td>
    <td>[0-60]</td>
    <td>The timeout in milliseconds for a transaction to acquire a lock.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>setParamet er.mirrorRe ads</td>
    <td>{samplin gRate: 0.01, maxTim eMS: 5000 }</td>
    <td>{samplingR ate: 0.01, maxTime MS: 5000}</td>
    <td>A restart is not required.</td>
    <td><code>.*</code> (object format)</td>
    <td>Specifies whether to enable Mirrored Reads and sets the sample rate and maximum running time.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.oplogFetc herUsesExh aust</td>
    <td>true</td>
    <td>true</td>
    <td>A restart is required.</td>
    <td>true|false</td>
    <td>Specifies whether to enable stream replication, which uses exhaust sockets to continuously pull the oplog.</td>
    <td>5.0 to 7.0 (Improves replication efficiency)</td>
  </tr>
  <tr>
    <td>setParamet er.replWrite rThreadCou nt</td>
    <td>16</td>
    <td>16</td>
    <td>A restart is required.</td>
    <td>[1-256]</td>
    <td>The number of write threads for applying the oplog in parallel. This affects replication throughput.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.tcmalloc Aggressive MemoryDec ommit</td>
    <td>0</td>
    <td>0</td>
    <td>No restart is required.</td>
    <td>0|1</td>
    <td>Specifies whether to enable aggressive memory reclamation for tcmalloc, which releases unused memory back to the operating system.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.tcmalloc ReleaseRat e</td>
    <td>1</td>
    <td>1</td>
    <td>No restart is required.</td>
    <td>[1-10]</td>
    <td>Controls the rate at which tcmalloc releases memory to the operating system. A higher value indicates a faster rate.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.transacti onLifetimeLi mitSeconds</td>
    <td>60</td>
    <td>60</td>
    <td>A restart is not required.</td>
    <td>[1-300]</td>
    <td>The total lifecycle timeout for a transaction in seconds. This prevents transactions from being suspended for a long time.</td>
    <td>5.0 to 7.0</td>
  </tr>
  <tr>
    <td>setParamet er.vpcAuth Mode</td>
    <td>false</td>
    <td>false</td>
    <td>A restart is not required.</td>
    <td>true|false</td>
    <td>The switch for VPC authenticatio n mode. This is used in specific cloud environments.</td>
    <td>4.0 to 4.2 (Specific to earlier versions)</td>
  </tr>
  <tr>
    <td>storage.oplo gMinRetenti onHours</td>
    <td>0</td>
    <td>0</td>
    <td>A restart is not required.</td>
    <td>[0.00-720.00]</td>
    <td>The minimum retention period for the oplog in hours. This ensures that delayed secondary nodes can still sync.</td>
    <td>5.0 to 7.0 (This parameter is not available in 4.x versions.)</td>
  </tr>
  <tr>
    <td>storage.wire dTiger.colle ctionConfig.blockCompr essor</td>
    <td>snappy</td>
    <td>snappy</td>
    <td>A restart is required.</td>
    <td>snappy|zlib| zstd|none</td>
    <td>The block compression algorithm for the WiredTiger storage engine. This takes effect only for new collections.</td>
    <td>5.0 to 7.0 (4.x versions support `snappy`/`z lib`.)</td>
  </tr>
  <tr>
    <td>systemLog.l ogRotateSiz eMB</td>
    <td>100</td>
    <td>100</td>
    <td>No restart is required.</td>
    <td>[1-214748364 7]</td>
    <td>The minimum size in MB for rotating system logs (`mongod.log `/`mongos.lo g`).</td>
    <td>3.4+ (3.0 to 4.2)</td>
  </tr>
</table>

**Sharded cluster parameter descriptions**

| Parameter name | Default value | Recomme nded value | Restart | Value range | Parameter description and versions |
| --- | --- | --- | --- | --- | --- |
| auditLog.authS uccess | true | true | A restart is required. | true\|false | Specifies whether the audit log records successful authentication events. Versions: 3.4+ (4.0, 4.2, 5.0, 6.0, 7.0) |
| auditLog.opFilt er | admin,slow | admin,slow | No restart is required. | <code> .* </code> (such as auth,admin,s low,... or all/off) | Filters the operation types for the audit log. You can use any combination of <code>auth,admin,slow,</code><br><code>insert,update,dele</code><br><code>te,command,query,p</code> <code>bwm </code>, or use <code> all </code>/<code> off </code>.Versions: 3.4+ (Universal) |
| auditLog.vipOn ly | true | true | A restart is required. | true\|false | Specifies whether to allow only virtual IP address (VIP) access to the audit log feature. Versions: 3.4+ (4.0, 4.2, 5.0, 6.0, 7.0) |
| net.compressi on.compressor s | snappy | snappy,zst d,zlib | A restart is required. | snappy\|zlib\|z std\|snappy,zs td,zlib\|disabl ed | Sets the network communication compression algorithm for mongod/mongos.Versions: 4.2+ (4.2, 5.0, 6.0, 7.0).Versions 4.2 and earlier support only \`snappy\|zlib\|disable d\`. |
| net.listenBackl og | 511 | 511 | Restart required | \[511-1023\] | The length of the TCP connection queue (backlog).This is used for the size of the accept queue. Versions: 3.4+ (Universal) |
| net.serviceExe cutor | synchrono us | adaptive (Recomme nded for high concurrenc y) | A restart is required. | synchronous\| adaptive | Specifies the threading model used by mongod/mongos: <code>synchronous</code> (synchronous), <code>adaptive</code> (adaptive, dynamic threads). Versions: 4.0+ (4.0, 4.2).Deprecated in versions 5.0 and later. |
| net.ssl.mode | disabled | requireSSL (Recomme nded for production) | You must restart. | disabled\|allo wSSL | The SSL connection mode. Allows or disables SSL only.Versions: 3.4+ (3.4, 4.0, 4.2). Replaced by TLS-related parameters starting from version 5.0. |
| net.tls.mode | disabled | requireTLS (Recomme nded for production) | A restart is required. | disabled\|allo wTLS\|preferT LS\|requireTL S | The TLS encrypted connection mode.Replaces SSL.<code>requireTLS</code> forces the use of TLS. Versions: 5.0+ (5.0, 6.0, 7.0) |
| security.forbid AdminDB | true | true | No restart is required. | true\|false | Specifies whether to prohibit users from writing to the admin database of a sharded cluster. This prevents accidental operations on the admin database.Versions: 3.4+ (Universal) |
| operationProfili ng.slowOpThre sholdMs | 100 | 100 to 500 (as needed) | A restart is not required. | \[0-65536\] | The threshold for slow queries in milliseconds. The profiler considers queries that exceed this time as slow queries. A value of 0 records all queries.Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.cursorTimeout Millis | 600000 | 300000 to 600000 | No restart is required. | \[1-2147483647\] | The timeout period for idle cursors in milliseconds.MongoDB automatically purges idle cursors that time out. The default is 10 minutes. Versions: 3.4+ (Universal) |
| setParameter.l ogicalSessionR efreshMillis | 300000 | 300000 | A restart is required. | \[60000-1800000\] | The refresh interval for the logical session cache in milliseconds. This controls the frequency of session cleanup. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.maxSessions | 1000000 | 500000 to 1000000 | A restart is required. | \[1000-1000000\] | The maximum number of cachable sessions (logical sessions). This affects memory usage. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.r eadHedgingMo de | on | on (Recomme nded for high availability) | A restart is not required. | on\|off | Specifies whether to enable Hedged Reads. When reading from a replica set, requests are sent to multiple nodes in parallel, and the fastest response is used.This improves read availability.Versions: 5.0+ (5.0, 6.0, 7.0) |
| setParameter.ShardingTaskE xecutorPoolHo stTimeoutMS | 300000 | 300000 | A restart is not required. | \[60000-3600000\] | The timeout in milliseconds before mongos gives up on the connection pool for a shard host.Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.ShardingTaskE xecutorPoolMa xConnecting | 2 | 2 to 8 (depending on the network) | No restart is required. | \[1-32\] | The maximum number of concurrent connections during the initialization of a shard connection pool. This controls the speed of connection establishment.Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.ShardingTaskE xecutorPoolMa xSize | 32767 | 1000 to 5000 (commonly used in practice) | A restart is not required. | \[1-32767\] | The maximum number of connections in each shard connection pool. This prevents resource exhaustion.Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.ShardingTaskE xecutorPoolMi nSize | 1 | 1 to 10 | No restart is required. | \[1-256\] | The minimum number of connections in each shard connection pool (keepalive connections).Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.t cmallocAggres siveMemoryDe commit | 0 | 0 (disabled by default) | A restart is not required. | \[0-1\] | Specifies whether to enable aggressive memory reclamation for tcmalloc, which releases unused memory to the OS.Enabling this may reduce memory usage but can affect performance.Versions: 5.0+ (5.0, 6.0, 7.0) |
| setParameter.t cmallocReleas eRate | 1 | 2 to 5 (balanced) | No restart is required. | \[1-10\] | The rate at which tcmalloc releases memory to the operating system. A higher value indicates a faster rate. A value that is too high may cause frequent allocation and release.Versions: 5.0+ (5.0, 6.0, 7.0) |
| setParameter.vpcAuthMode | false | false | A restart is not required. | true\|false | Specifies whether to enable VPC internal network authentication mode. This is used in specific cloud environments.Versions: 4.0+ (4.0, 4.2). Not mentioned in later versions. It may have been integrated into other features. |

<a id="section-8-2"></a>

## 8.2. Use parameter templates

When you configure multiple clusters that contain one or more parameters with the same settings, you can use parameter templates to manage and quickly apply parameters to clusters. This improves the efficiency of parameter management and cluster configuration.

**Create a parameter template**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Parameter Template**. On the page that appears, click **Create a parameter Template** and configure the parameters. The following table describes the parameters.

   | Parameter | Description |
   | --- | --- |
   | Template name | Enter a name for the parameter template. The name must meet the following requirements:<br>• The name must start with a letter, can contain digits and underscores (_), and cannot contain Chinese characters.<br>• It must be 8 to 64 characters in length. |
   | Organizati on | Select an organization. |
   | Resource Set | Select a resource set. |
   | Instance Architectu re Type | Select the type of the destination instance. |
   | Database engine | Set the value to MongoDB. |
   | Database version | Select a database engine version. |
   | Descriptio n | Enter a description for the parameter template to facilitate management. The description can be 0 to 200 characters in length. |
   | Add configurati on | After you click <strong>Add configuration</strong>, the system adds a parameter line to the list. You can specify <strong>Parameter name</strong> and configure <strong>Configuration value</strong> based on <strong>Description</strong> and <strong>Modifiable parameter values</strong>. You can also view the information about whether a cluster restart is required and the default parameter value on the page.<br>Note<br>• To add another parameter, click <strong>Add configuration</strong> again.<br>• To delete a parameter, you can click <strong>Delete</strong> on the right of the parameter. |

3. Click **OK**.

**Apply a parameter template**

> **Important**
>
> If a restart is required, we recommend that you apply the parameter template during off-peak hours and make sure that your application is configured to automatically reconnect to the cluster.

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Parameter Template**. On the page that appears, find the parameter template that you want to apply and click **Apply to an instance** in the **Operation** column.

3. In the **Apply to an instance** panel, select the clusters to which you want to apply the

   parameter template and click the <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/755429035c761e93d0759e527ecc415a.jpeg" width="26" alt=""> icon to move them to the right list. You can view the

   differences between the parameter values in the template and the parameter values in the clusters in the **Parameter comparison** section.

   > **Note**
   >
   > When you apply a parameter template to multiple clusters, take note of the following items:
   >
   > - Check whether the parameters are applicable to these clusters. Proceed with caution.
   >
   > - A parameter template can be applied to up to 10 clusters at a time. To apply a parameter template to more than 10 clusters, you can apply it in batches.

4. Click **OK**.

**Clone a parameter template**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Parameter Template**. On the page that appears, find the parameter template that you want to copy and click **Clone** in the **Operation** column. In the Clone panel, configure the parameters. The following table describes the parameters.

3. 

   | Parameter | Description |
   | --- | --- |
   | Template name | The name of the parameter template. By default, the name is in the original template name_clone format. You can rename the template. The name must meet the following requirements:<br>• The name must start with a letter, can contain digits and underscores (_), and cannot contain Chinese characters.<br>• It must be 8 to 64 characters in length. |
   | Description | Enter a description for the parameter template to facilitate management. The description can be 0 to 200 characters in length. |
   | Add configuration | By default, the parameters are the same as those in the original template. You can modify the parameters based on your business requirements.<br>Note<br>• To add a parameter, click <strong>Add configuration</strong>.<br>• To modify the value of a parameter, enter the value in the <strong>Configuration value</strong> field on the right of the parameter.<br>• To delete a parameter, you can click <strong>Delete</strong> on the right of the parameter. |

4. Click **OK**.

**Delete a parameter template**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Parameter Template**. On the page that appears, find the parameter template that you want to delete and click **Delete** in the **Operation** column.

3. Click **OK**.

<a id="section-9"></a>

# 9.Backup and restoration

<a id="section-9-1"></a>

## 9.1. Data backup

<a id="section-9-1-1"></a>

### 9.1.1. Configure automatic backup

This topic describes how to configure automatic backup for an ApsaraDB for MongoDB instance. ApsaraDB for MongoDB can automatically back up data based on the default backup policy or the backup policy that you specify.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Backup and Restoration**.

5. In the upper-left corner of the page, click **Backup Settings**.

6. In the **Backup Settings** panel, configure the following parameters.

   | Parameter | Description |
   | --- | --- |
   | Retention Period (Days) | The retention period from 7 to 730 days. If the data volume is large, change the retention period from 30 days to 7 days. This way, storage space can be released promptly to efficiently reduce the storage usage and costs of Object Storage Service (OSS). |
   | Backed Up At | The period of time during which you want to back up data. We recommend that you back up data during off-peak hours. |
   | Day of Week | The days of a week on which you want to back up data. You can select multiple days. |

7. Click **OK**.

<a id="section-9-1-2"></a>

### 9.1.2. Manually back up an ApsaraDB for MongoDB instance

This topic describes how to manually back up an ApsaraDB for MongoDB instance. ApsaraDB for MongoDB supports both automatic backup and manual backup. You can configure a backup policy for the system to automatically back up your ApsaraDB for MongoDB instance based on the backup cycle you specify.

**Backup methods**

- Physical backup: This method backs up physical database files of an ApsaraDB for MongoDB instance. Compared with logical backup, physical backup provides faster data backup and restoration.

- Logical backup: The mongodump tool is used to store operation records of databases in a logical backup file. Logical backup restores data in the form of playback commands during restoration.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the upper-right corner of the page, click **Back up Instance**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/143babd26aff28b9c5900912341b0adf.png)

5. In the **Back up Instance** panel, select a backup method from the **Backup Method** drop-down list and then click **OK**.

<a id="section-9-2"></a>

## 9.2. Download a backup file

ApsaraDB for MongoDB allows you to download backup files that can be used to restore databases. This topic describes how to download a backup file in the ApsaraDB for MongoDB console.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Backup and Restoration**.

5. On the page that appears, click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/2c42747ff0594c8f986d07e3af2f3cc4.png" width="3" alt=""> in the **Actions** column corresponding to a backup file and

   select **Download**.

6. In the **Download Backup** dialog box, click **Copy** next to the download URL and then click **OK**.

7. Select an appropriate method to download the backup file based on your business environment. You can run the **wget** command, or paste the copied download URL into the address bar of your browser and press the Enter key to download the backup file.

<a id="section-9-3"></a>

## 9.3. Data restoration

<a id="section-9-3-1"></a>

### 9.3.1. Restore backup data to a new ApsaraDB for MongoDB instance by point in time

ApsaraDB for MongoDB allows you to create an instance at a point in time when the current instance is running and restore the backup data at that point in time to the new instance. This method is suitable for data restoration and verification.

**Limits**

Only points in time from the last seven days can be selected.

**Precautions**

- Individual databases can be restored only from physical backups. If your instance runs a MongoDB version earlier than 4.0 and the total number of collections and indexes in your instance exceeds 10,000, physical backups may fail.

- The amount of time required to restore data of individual databases varies based on factors such as the data volume, task queue state, and network conditions. When the state of the new instance changes to **Running**, the restoration is complete.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the left-side navigation pane, click **Backup and Recovery**.

5. Select the databases that you want to restore.

   <ol type="i">

   <li>

   On the **Backup and Recovery** page, click **Create Instance By Time Point**.

   </li>

   <li>

   In the **Create Instance By Time Point** panel, specify the following parameters.

   </li>

   </ol>

   | Parameter | Description |
   | --- | --- |
   | Select recovery time point | Selects a point in time from which you want to restore data. Points in time from the last seven days can be selected.<br>Note The point in time you select must be earlier than the current time and later than the time when the source instance was created. |
   | Select databases to recover | • <strong>All Databases</strong>: All databases in the source instance are restored.<br>• <strong>Select Databases</strong>: Only selected databases are restored.<br>You can directly select the databases that you want to restore or click <strong>Enter Databases</strong> to enter the names of the databases that you want to restore.<br>Note<br>• If you enter the names of the databases, separate the names with commas (,).<br>• By default, all databases are restored for sharded cluster instances. You can skip this step if the instance is a sharded cluster instance.<br>• If the instance is a sharded cluster instance, do not select the latest point in time (usually the latest hour). Otherwise, the restoration will fail. |

   <ol type="i" start="3">

   <li>

   Click **OK**.

   </li>

   </ol>

6. On the **Clone ApsaraDB for MongoDB instance** page, configure the parameters of the new instance. For more information, see Create a replica set instance or Create a sharded cluster instance.

   > **Note**
   >
   > - If the instance is a replica set instance, the storage capacity of the new instance must be greater than or equal to that of the source instance.
   >
   > - If the instance is a sharded cluster instance, the following requirements must be met:
   >
   >   - The number of shard nodes in the new instance must be equal to that in the source instance.
   >
   >   - The storage capacity of each shard node in the new instance must be greater than or equal to that in the source instance.

7. Click **Submit**.

<a id="section-9-3-2"></a>

### 9.3.2. Restore backup data to a new ApsaraDB for MongoDB instance by backup point

ApsaraDB for MongoDB allows you to restore data to a new ApsaraDB for MongoDB instance by backup point. This method is suitable for data restoration and verification.

**Prerequisites**

The instance is a replica set instance.

**Limits**

Only backup points from the last seven days can be selected.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances** page, click the ID of an instance, or click

   in the **Actions**

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   column corresponding to the instance and select **Manage**.

4. In the left-side navigation pane, click **Backup and Recovery**.

5. Select the databases that you want to restore.

   <ol type="i">

   <li>

   Find the backup file that you want to use for data restoration. Choose

   > **Create**

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Instance from Backup Point** in the **Actions** column.

   </li>

   <li>

   In the **Create Instance from Backup Point** panel, select the databases that you want

   </li>

   </ol>

   to restore.

   - **All Databases**: All databases in the source instance are restored.

   - **Select Databases**: Only selected databases are restored.

     You can directly select the databases that you want to restore or click **Enter Databases** to enter the names of the databases that you want to restore.

     > **Note**
     >
     > If you enter the names of the databases, separate the names with
     >
     > commas (,).

   <ol type="i" start="3">

   <li>

   Click **OK**.

   </li>

   </ol>

6. On the **Clone ApsaraDB for MongoDB instance** page, configure the parameters of the new instance. For more information, see Create a replica set instance or Create a sharded cluster instance.

   > **Note**
   >
   > The storage capacity of the new instance must be greater than or equal to
   >
   > that of the source instance.

7. Click **Submit**.

<a id="section-9-3-3"></a>

### 9.3.3. Restore data to the current ApsaraDB for MongoDB instance

Data restoration minimizes the data loss caused by accidental changes. This topic describes how to restore data to the current ApsaraDB for MongoDB instance.

**Prerequisites**

The instance is a replica set instance with three nodes.

**Background information**

- The time required to restore database data varies based on factors such as the data volume, task queue status, and network conditions. When the state of the instance changes to **Running**, the restoration is complete.

- If you restore data to your current instance, all existing data is overwritten and cannot be restored. Proceed with caution.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** page, click the ID of an instance, or click

   in the **Actions**

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   column corresponding to the instance and select **Manage**.

3. In the left-side navigation pane, click **Backup and Recovery**.

4. On the **Backup and Recovery** page, find the backup set that you want to manage and click the <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/2c42747ff0594c8f986d07e3af2f3cc4.png" width="3" alt=""> icon. Then, select Data Rollback.

   > **Note**
   >
   > If the MongoDB version has been upgraded, the backup files of the original
   >
   > instance that runs an earlier version cannot be used to restore data to the new instance.

5. In the **Data Restoration** message, click **OK**.

   > **Note**
   >
   > The instance state becomes **Restoring from Backup** after you click **OK**.
   >
   > You can click **Refresh** in the upper-right corner of the **Backup and Recovery** page to update the instance state. The restoration is complete when the instance state changes to **Running**.

<a id="section-10"></a>

# 10.Cloud Monitor

<a id="section-10-1"></a>

## 10.1. View performance metrics

PolarDB for MySQL V2.0 provides rich performance metrics and second-level monitoring frequency, which allow you to easily track the status of clusters and address operational challenges.

**View the dashboard**

1. Log in to the PolarDB for MySQL V2.0 console.

2. On the **Instances Using Local Disks** page, find the cluster that you want to manage and click its ID.

3. In the left-side navigation pane, click **CloudMonitor**.

4. You can view metrics related to **computing resources**, **disks**, **networks**, **deadlocks**, and **read-only instances**. View performance metrics

**View monitoring information**

1. Log in to the PolarDB for MySQL V2.0 console.

2. In the left-side navigation pane, click **CloudMonitor**.

3. In the **time granularity** drop-down list, select **1 Minute** or **1 Hour** (default value) as the data collection interval.

<a id="section-10-2"></a>

## 10.2. Alert history

After an alert is triggered, you can view its history. You can also export and download the alert history for local data analytics.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.

2. On the **Instance List** page, click the ID of the instance.

3. In the navigation pane on the left, click **Cloud Monitor** and choose **Alert Service** > **Alert History**.

4. (Optional) On the **Alert History** page, filter the alert history by **Rule ID**, **Rule Name**, **Alert Level**, and time.

5. On the Alert History page, you can perform the following tasks.

   | Task | Procedure |
   | --- | --- |
   | View alert history | In the <strong>Alert History</strong> list, view the <strong>Product Name</strong>, <strong>Affected</strong> <strong>Instance</strong>, <strong>Time</strong>, <strong>Rule Name</strong>, <strong>Status</strong>, <strong>Level</strong>, and <strong>Notification</strong> <strong>Recipient</strong>. Click the rule name to view the details of the alert rule.<br>Note<br>By default, you can query alert history data from the last 2 days. |
   | Export alert history | i. On the <strong>Alert History</strong> page, click<img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/a7de886b243b51870606212f4f1d2809.png" width="22" alt="">in the upper-right<br>corner.<br>ii. In the <strong>Export Task</strong> dialog box, set <strong>Time Range</strong> and <strong>Task</strong> <strong>Name</strong>. Then, click <strong>OK</strong>. |

<a id="section-10-3"></a>

## 10.3. Alert rules

<a id="section-10-3-1"></a>

### 10.3.1. Create an alert rule

Create an alert rule that triggers alerts for a cloud service based on specified metric thresholds and promptly notifies relevant users.

**Background information**

During its effective period, an alert rule checks at a default detection frequency if a metric exceeds the specified threshold. If a metric exceeds the threshold and becomes abnormal, an alert is sent to the specified alert contacts or other alert processing platforms.

> **Note**
>
> The minimum alert detection frequency is once per minute.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.

2. On the **Instance List** page, click the ID of the instance.

3. In the navigation pane on the left, click **CloudMonitor**, and then choose **Alert Service** > **Alert Rules**.

4. Above the list, click **Create Alert Rule**.

5. In the **Create Alert Rule** panel, set the parameters as needed.

   | Parameter | Description |
   | --- | --- |
   | Cloud Service Selection | This is set by default and does not need to be selected. |
   | Resource Scope | The scope of resources associated with the alert rule. The following types are supported. The available scope types may vary by cloud service.<br>• <strong>Instance</strong>: Select one or more target instances from the resource set of the current organization.<br>• <strong>Resource Set</strong>: Select a target resource set in the current organization and region.<br>• <strong>Application Group</strong>: Select an application group in the current organization and region.<br>• <strong>All Resources</strong>: This option is not supported by default. |
   | Resource Selection | Based on the selected <strong>Resource Scope</strong>, select a specific resource instance, resource set, or application group. |
   | Alert Rule Description | The main body of the alert rule. The rule is triggered when monitoring data meets the alert conditions.<br>To set the rule description:<br>i. Click <strong>Create Alert Rule</strong>.<br>ii. In the <strong>Create Alert Rule</strong> panel, set the <strong>Rule Name</strong>, <strong>Metric Dimension</strong>, <strong>Monitoring Metric</strong>, <strong>Threshold, AndAlert Level</strong>.<br>Note<br>The Metric Dimension parameter is displayed only when Resource Scope is set to <strong>Instance</strong>.<br>iii. Click <strong>Confirm</strong>. |
   | Mute For | The interval at which to resend an alert notification if the alert is not resolved.Valid values: <strong>5 Minutes</strong>, <strong>15 Minutes</strong>, <strong>30 Minutes</strong>, <strong>1 Hour</strong>, <strong>3 Hours</strong>, <strong>6 Hours</strong>, <strong>12 Hours</strong>, and <strong>24 Hours</strong>.<br>When a metric exceeds the alert threshold, an alert is triggered. If the metric continues to exceed the threshold during the mute period, no more alert notifications are sent. If the metric has not recovered after the mute period, CloudMonitor sends another alert notification.<br>For example, if <strong>Mute For</strong> is set to <strong>12 Hours</strong>, CloudMonitor sends another alert notification if the metric that exceeded the threshold has not recovered 12 hours after the first alert was triggered. |
   | Effective Period | The period during which the alert rule is active. The rule only checks if monitoring data exceeds the alert threshold during this period. |
   | Alert Callback | A webhook address that receives alert messages pushed by CloudMonitor through POST requests.<br>Note<br>The webhook address must be a domain name accessible to CloudMonitor.Only the HTTP protocol is supported. You cannot enter an IP address. |
   | No Data Handling Method | The method for handling alerts when there is no monitoring data.<br>• Do Nothing<br>• Send No-data Alert |
   | Alert Contact | Select the user group or user to whom alert messages are sent.<br>The default alert contact group for an Alibaba Cloud account is an empty group.You can use it to test the validity of an alert rule. |

6. Click **OK**.

**Rule description parameters**

| Parameter | Description |
| --- | --- |
| Rule Name | Enter a name for the alert rule. |
| Monitoring Metric | From all the metrics available for the selected cloud service, select the target metric. For more information about the metrics for each cloud service, see the relevant monitoring documentation. |
| Metric Dimension | Refers to dimensions other than the instance ID. This parameter is displayed only when Resource Scope is set to <strong>Instance</strong>. |
| <strong>Threshold</strong> <strong>And</strong> Alert Level (unit: %) | • The alert levels are <strong>Critical</strong>, <strong>Warning</strong>, and <strong>Info</strong>.<br>• The aggregation method for monitoring data can be <strong>Average</strong>, <strong>Minimum</strong>, or <strong>Maximum</strong>.<br>• You can set the monitoring data epoch to <strong>1 Consecutive Epoch</strong>, <strong>5</strong> <strong>Consecutive Epochs</strong>, <strong>10 Consecutive Epochs</strong>, <strong>15 Consecutive Epochs</strong>, <strong>30</strong> <strong>Consecutive Epochs</strong>, or <strong>60 Consecutive Epochs</strong>.<br>• The comparison operator between the actual monitoring data and the alert threshold. Supported operators include “<strong>&gt;</strong>”, “ <strong>&gt;=</strong>”, “<strong>&lt;</strong>”, “<strong>&lt;=</strong> ”, “<strong>=</strong>”, “<strong>!=</strong>”, “<strong>Day-on-day Increase</strong>”, “<strong>Day-on-day Decrease</strong>”, “<strong>Period-on-period</strong> <strong>Increase”</strong>, <strong>“period-on-period Decrease”</strong>, <strong>“increase From Last Period”</strong>, and <strong>“decrease From Last Period”</strong>. You can also set a threshold and the number of times it must be met to trigger an alert. |

**Example configuration**

This example creates an alert rule named "example" for an Elastic Compute Service (ECS) instance to monitor its CPU utilization. The rule triggers a Critical alert if the maximum CPU utilization is greater than or equal to 70% for three occurrences within five detection periods.

The following figure shows the rule description configuration for this scenario.

![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/d23ed31c0cdf79631e71a22370a9f932.jpeg)

<a id="section-10-3-2"></a>

### 10.3.2. Manage alert rules

From the list of alert rules, you can modify, enable, disable, and delete rules.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.

2. On the **Instance List** page, click the ID of the instance.

3. In the navigation pane on the left, click **Cloud Monitor** and then choose **Alert Service** > **Alert Rules**.

4. Find the desired alert rule and perform the required operation.

   | Task | Procedure |
   | --- | --- |
   | View alert rule details | In the <strong>Operation</strong> column of the target alert rule, click <strong>Details</strong> to view the rule details on the <strong>Alert Rule/Alert History/Faulty Resources</strong> panel. |
   | Check rule validity | In the <strong>Validity</strong> column of the target alert rule, click <strong>Click To Inspect</strong>. The inspection result is displayed in the Validity column.<br>Note<br>• If the inspection result is abnormal, click <strong>Detection Result</strong>. In the panel that appears, view the results for <strong>Alert Rule Execution</strong> <strong>Anomaly Detection</strong>, <strong>Alert Rule Load Detection</strong>, <strong>Invalid Alert</strong> <strong>Rule Detection</strong>, and <strong>Alert Rule Callback Detection</strong>.<br>• Click <strong>Re-detect</strong> to check the rule validity again. |
   | View rule execution records | In the <strong>Rule Execution Record</strong> column of the target alert rule, click <strong>View</strong> <strong>Rule Execution Record</strong>. On the <strong>Alert Rule Execution Record</strong> panel, filter the execution records by time range. |
   | Modify an alert rule | i. In the <strong>Operation</strong> column of the target alert rule, click <strong>Edit.</strong><br>ii. On the <strong>Modify Alert Rule</strong> panel, modify the alert rule. For more information about the configuration parameters, see Create an alert rule.<br>iii. After you finish the modification, click <strong>OK</strong>. |
   | Disable an alert rule | Disable alert rules when you manually stop a cloud product for maintenance or an upgrade. This prevents unnecessary alert notifications.<br>Note<br>Before disabling an alert rule, make sure that its <strong>Status</strong> is <strong>Normal</strong>.<br>• Disable a single rule<br>a. In the <strong>Operation</strong> column of the target alert rule, click the<img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/e6a0428d0f12bfe0c352c71ec18fafa1.png" width="14" alt="">icon, and then click <strong>Disable.</strong><br>b. In the <strong>Disable Alert Rule</strong> dialog box, click <strong>OK.</strong><br>• Disable rules in a batch<br>a. Select the check boxes next to the target alert rules, and then click <strong>Disable</strong> in the lower-left corner of the list.<br>b. In the <strong>Disable Alert Rule</strong> dialog box, click <strong>OK</strong>. |
   | Enable an alert rule | After you finish the maintenance or upgrade of a cloud product, re-enable the disabled alert rules.<br>Note<br>Before enabling an alert rule, make sure that its <strong>Status</strong> is <strong>Disabled</strong>.<br>• Enable a single rule<br>a. In the <strong>Operation</strong> column of the target alert rule, click <strong>Enable.</strong><br>b. In the <strong>Enable Alert Rule</strong> dialog box, click <strong>OK.</strong><br>• Enable rules in a batch<br>a. Select the check boxes next to the target alert rules, and then click <strong>Enable</strong> in the lower-left corner of the list.<br>b. In the <strong>Enable Alert Rule</strong> dialog box, click <strong>OK</strong>. |
   | Delete an alert rule | • Delete a single rule<br>a. In the Operation column of the target alert rule, click the<img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/e6a0428d0f12bfe0c352c71ec18fafa1.png" width="14" alt="">icon, and then click <strong>Delete</strong>.<br>b. In the <strong>Delete Alert Rule</strong> dialog box, click <strong>OK</strong>.<br>• Delete rules in a batch<br>a. Select the check boxes next to the target alert rules, and then click Delete in the lower-left corner of the list.<br>b. In the <strong>Delete Alert Rule</strong> dialog box, click <strong>OK</strong>. |

<a id="section-11"></a>

# 11.Database connections

<a id="section-11-1"></a>

## 11.1. Modify a public or internal endpoint of an ApsaraDB for MongoDB instance

This topic describes how to modify a public or internal endpoint of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console.

**Limits**

| Architecture | Limits |
| --- | --- |
| Replica set instance | You can modify only the public and internal endpoints of primary and secondary nodes. |
| Sharded cluster instance | You can modify only the public and internal endpoints of mongos nodes. |

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the instance whose endpoint you want to modify.

4. In the left-side navigation pane, click **Database Connection**.

5. In the **Internal Connections** or **Public Connections** section, click **Update Connection String**.

6. In the **Update Connection String** panel, specify a new endpoint.

   > **Note**
   >
   > Only the prefix of the endpoint can be modified. You must comply with the
   >
   > following rules when you modify the prefix:
   >
   > - The prefix must start with a lowercase letter.
   >
   > - The prefix must start or end with a lowercase letter or digit.
   >
   > - The prefix must be 8 to 64 characters in length and can contain lowercase letters, digits, and hyphens (-).

7. Click **OK**.

**What to do next**

After you modify the public or internal endpoint, you must connect a client or an application to your ApsaraDB for MongoDB instance by using the new endpoint.

<a id="section-11-2"></a>

## 11.2. Use DMS to log on to an ApsaraDB for MongoDB instance

You can use Data Management (DMS) to log on to an ApsaraDB for MongoDB instance.

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the upper-right corner of the page, click **Log On**.

   > **Note**
   >
   > For a sharded cluster instance, you must also select a mongos node.

   Log on to the **DMS** console.

5. In the **Login instance** dialog box, configure the parameters described in the following table.

   | Parameter | Description |
   | --- | --- |
   | Database Type | The database engine of the instance. By default, this parameter is set to the database engine of the instance that you want to access. |
   | Instance Region | The region where the instance is deployed. By default, this parameter is set to the region where the current instance is deployed. |
   | Connection string address | The connection string of the instance. By default, this parameter is set to the connection string of the current instance. |
   | Database Name | The name of the database. By default, this parameter is set to admin. |
   | Database Account | The account used to connect to the database. By default, this parameter is set to root. |
   | Database Password | The password of the account used to connect to the database. |

6. Click **Login**.

   > **Note**
   >
   > You can select **Remember password** to eliminate the need to manually
   >
   > enter the password again the next time you log on to the database.

<a id="section-11-3"></a>

## 11.3. Use the mongo shell to connect to an ApsaraDB for MongoDB instance

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by ApsaraDB for MongoDB. You can install it on your client or in an Elastic Compute Service (ECS) instance.

**Prerequisites**

- The version of the mongo shell is the same as that of your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about the installation procedure, see Install MongoDB.

  > **Note**
  >
  > You can select a MongoDB version corresponding to your client version in
  >
  > the upper-left corner of the page.

- The IP address of your client is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Database Connections** to view connection strings.

   > **Note**
   >
   > - Replica set instances: View the connection string or connection string URI of a node.
   >
   > - Sharded cluster instances: View the connection string or connection string URI of a mongos node.
   >
   > For more information about connection strings, see Overview of replica set instance connections or Overview of sharded cluster instance connections.

5. Connect to a database of the instance from your client or ECS instance where the mongo shell is installed.

   - Replica set instances

     - High-availability connection (recommended)

       You can use a connection string URI to connect to both the primary and secondary nodes of the instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched.

       Command syntax:

       ```text
       mongo "<ConnectionStringURI>"
       ```

       > **Note**
       >
       > - The connection string URI must be enclosed in a pair of double quotation marks ("").
       >
       > - &lt;ConnectionStringURI>: the **connection string URI** of the instance.
       >
       >   You must replace  `****`  in the **connection string URI** with the database password. For more information about how to set a database password, see Reset a password.

       Example:

       ```text
       mongo "mongodb://root:****@dds-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717,dds-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
       *"
       ```

     - Single-node connection

       In most cases, you can directly connect to the primary, secondary, or read-only node. When the primary node fails, the system automatically switches to the secondary node and the secondary node becomes the primary node. This affects the read and write operations of your application.

       Command syntax:

       ```text
       mongo --host <host> -u <username> -p --authenticationDatabase <database>
       ```

       > **Note**
       >
       > - &lt;host>: the endpoint used to log on to the primary or secondary node.
       >
       > - &lt;username>: the username used to log on to a database of the instance. The initial username is **root**.
       >
       > - &lt;database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin as the database name.

       Example:

       ```text
       mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticationDatabase admin
       ```

       When  `Enter password:`  is displayed, enter the password of the username and press the Enter key. If you forget the password of the root username, you can reset the password. For more information, see Reset a password.

       > **Note**
       >
       > The password characters are not displayed when you enter the
       >
       > password.

   - Sharded cluster instances

     - High-availability connection (recommended)

       You can use a connection string URI to connect to a database of the instance. If one mongos node fails, another mongos node takes over business to ensure the high availability of the connection.

       Command syntax:

       ```text
       mongo "<ConnectionStringURI>"
       ```

       > **Note**
       >
       > - The connection string URI must be enclosed in a pair of double quotation marks ("").
       >
       > - &lt;ConnectionStringURI>: the **connection string URI** of the instance.
       >
       >   You must replace  `****`  in the **connection string URI** with the database password. For more information about how to set a database password, see Reset a password.

       Example:

       ```text
       mongo "mongodb://root:****@s-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
       **********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
       ```

     - Mongos node connection Command syntax:

       ```text
       mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
       ```

       > **Note**
       >
       > - &lt;mongos_host>: the endpoint used to log on to a mongos node.
       >
       > - &lt;username>: the username used to log on to a database of the instance. The initial username is **root**.
       >
       > - &lt;database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin as the database name.

       Example:

       ```text
       mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticationDatabase admin
       ```

<a id="section-11-4"></a>

## 11.4. Apply for a public endpoint

This topic describes how to apply for a public endpoint for an ApsaraDB for MongoDB instance when you want to connect to the instance over the Internet.

**Background information**

ApsaraDB for MongoDB instances support Virtual Private Cloud (VPC), classic network, and public endpoints. The following table describes these endpoints.

| Endpoint | Description |
| --- | --- |
| VPC endpoint | • A VPC is an isolated network that provides higher security and performance than the classic network.<br>• By default, an ApsaraDB for MongoDB comes with a VPC endpoint. You can connect to the VPC endpoint for higher security and performance. |
| Classic network endpoint | Cloud services deployed in the classic network are not isolated from each other.Unauthorized access can be blocked only by using security groups or whitelists. |
| Public endpoint | • Your ApsaraDB for MongoDB instance is at risk when you connect to it over the Internet. For this reason, ApsaraDB for MongoDB does not provide public endpoints by default.<br>• If you want to connect to an ApsaraDB for MongoDB instance from a device outside Alibaba Cloud, such as an on-premise device, you must apply for a public endpoint. |

**Apply for a public endpoint for a replica set instance**

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set instance List** page, find the instance that you want to manage and click the ID of the instance.

3. In the left-side navigation pane, click **Database Connections**.

4. In the **Public Connections** section, apply for an IPv4 address or apply for an IPv4 address and an IPv6 address.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/0a3f6738aa939b0424e570bf91a40c56.jpeg)

5. In the message that appears, click **OK**.

   > **Note**
   >
   > - Apply for an IPv4 address: This option is suitable for IPv4 networks.
   >
   > - Apply for an IPv4 address and an IPv6 address: This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance.
   >
   > - If you want to connect to a replica set instance by using a public endpoint, you must add the public IP address of your client to the whitelist of the instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

After you submit the application, the replica set instance generates public endpoints for both the primary and secondary nodes and a connection string URI for establishing high-availability connections. For more information, see Overview of replica set instance connections.

**Apply for a public endpoint for a sharded cluster instance**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, click **Database Connections**.

5. In the **Public Connections** section, click **Apply for Public Connection String**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/89c93bd26bba9a5d459b16673482ba43.jpeg)

6. In the **Apply for Public Connection String** pane, specify **Node Type**, **Node ID**, and **Apply for IP type** and click **OK**.

7. **Optional:** If you want to apply for multiple public endpoints for the nodes in the sharded cluster instance, repeat the preceding steps.

   > **Note**
   >
   > To apply for public endpoints for multiple nodes in the instance consecutively, you must wait until the state of the instance changes to **Running**.

**References**

- To ensure data security, we recommend that you release public endpoints if you no longer need them. For more information, see Release a public endpoint.

- Before you connect to a database over the Internet, we recommend that you enable SSL encryption. For more information, see Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode.

<a id="section-11-5"></a>

## 11.5. Release a public endpoint

To ensure data security, you can release public endpoints that are no longer needed in the ApsaraDB for MongoDB console.

**Precautions**

- You can release one or more public endpoints of the mongos nodes for a sharded cluster instance.

- After a public endpoint is released for an instance or node, you cannot connect to the instance or node by using the public endpoint.

- After the public endpoint is released, we recommend that you delete the corresponding public IP address from the whitelist to ensure data security. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**Release a public endpoint for a replica set instance**

> **Note**
>
> After the public endpoint of a replica set instance is released, the public
>
> endpoints of the primary and secondary nodes are released.

1. Log in to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** page, click the ID of an instance.

3. In the left-side navigation pane, click **Database Connections**.

4. In the **Public Connections** section, click **Release Public Connection String**.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/f50939d964b21bf80556fa867b528890.png)

5. In the **Release Public Connection String** message, click **OK**.

**Release a public endpoint for a sharded cluster instance**

> **Note**
>
> - You can release one or more public endpoints of the mongos, shard, and Configserver nodes for a sharded cluster instance.
>
> - After the public endpoint of a shard or Configserver node is released, the public endpoints of the primary and secondary nodes are released.

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Database Connections**.

5. In the **Public Connections** section, find the mongos node for which you want to release the public endpoint.

6. Click **Release** in the **Actions** column.

   > **Note**
   >
   > You can repeat this step to release the public endpoints of other nodes as
   >
   > needed. To release the public endpoint of another node in the instance, you must wait until the public endpoint of the current node is released or the state of the current instance becomes **Running**.

7. In the **Release Public Connection String** message, click **OK**.

8. <strong>Optional:</strong>You can repeat this step to release the public endpoints of multiple nodes in a sharded cluster instance.

   > **Note**
   >
   > To release the public endpoint of another node in the instance, you must
   >
   > wait until the state of the instance becomes **Running**.

<a id="section-11-6"></a>

## 11.6. Apply for an endpoint for a shard or ConfigServer node

A sharded cluster instance consists of mongos, shard, and Configserver nodes. Typically, you need only to connect to a mongos node to read and write data. If you want to read oplog data from a shard node or read configuration information from a Configserver node when you perform specific operations such as data synchronization between clusters, you must apply for an endpoint for the corresponding node first.

**Prerequisites**

A sharded cluster instance is created.

**Usage notes**

- After you submit an application, two endpoints are allocated to each node, one for the primary node and the other for the secondary node.

- The network type of an endpoint for which you want to apply must be the same as that of the current mongos node.

- You cannot modify the endpoint that is allocated to a shard or ConfigServer node.

- The endpoint allocated can only be used to access the node over the internal network. If you want to access the node over the Internet, you can apply for a public endpoint. For more information, see Apply for a public endpoint.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the left-side navigation pane, click **Database Connections**.

5. Click **Apply for Shard\\Configserver Endpoint**.

6. In the dialog box that appears, apply for an endpoint for the shard or Configserver node.

   | Parameter | Description |
   | --- | --- |
   | Node Type | • <strong>Shard</strong>: shard node<br>• <strong>CS</strong>: ConfigServer node |
   | Apply for IP type | • <strong>IPv4</strong>: Apply for an IPv4 address. This option is suitable for IPv4 networks.<br>• <strong>IPv4v6</strong>: Apply for an IPv4 address and an IPv6 address. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. |
   | Select Node ID | Select a check box corresponding to the ID of the node for which you want to apply for an endpoint. |
   | Account Name | The account name must be 4 to 16 characters in length, and can contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter.<br>Note<br>• You must set the account and password only when you <strong>apply for</strong> <strong>an endpoint for a shard or Configserver node</strong> for the first time. The account and password are required for all shard and Configserver nodes.<br>• The account has only permissions to read data. |
   | Account Password | • The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters.The following special characters are supported:<br>!@#$%^&amp;\*()_+=<br>• The password must be 8 to 32 characters in length.<br>Note<br>If you forget your password, you can reset the password. For more information, see Reset the password. |
   | Confirm Password | Enter the account password again. |

7. Click **OK**.

8. Wait until the instance state changes from **Creating Connection** to **Running**.

**Node types**

After you **apply for an endpoint for a shard or Configserver node**, you can view the endpoint on the **Database Connections** page. The following table describes node types.

| Node type | Description |
| --- | --- |
| DB | A shard node. |
| CS | A ConfigServer node. |
| Mongos | A mongos node. |

**References**

If you no longer need the endpoints of shard or ConfigServer nodes, you can release the endpoints. For more information about how to release an endpoint, see Release the connection string of a shard or Configserver node.

<a id="section-11-7"></a>

## 11.7. Release the connection string of a shard or Configserver node

When you no longer need to connect to a shard or Configserver node, you can release its connection string.

**Precautions**

- This operation applies to sharded cluster instances only.

- The connection string of a mongos node cannot be released.

- After the connection string of a shard or Configserver node is released, the connection strings of the primary and secondary nodes are released and you cannot use this connection string to connect to the released node. Proceed with caution.

- This operation releases the internal connection string of the node. If the node also has a public connection string and the connection string is no longer needed, you can Release a public endpoint.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the left-side navigation pane, click **Database Connection**.

5. Find the node and click **Release** in the **Actions** column.

   > **Note**
   >
   > **db** indicates a shard node. **cs** indicates a Configserver node.

6. In the dialog box that appears, click **OK**.

7. Wait until the instance status changes from **Releasing Network Connection** to **Running**.

<a id="section-11-8"></a>

## 11.8. Overview of replica set instance connections

ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node, and use a connection string URI to connect to both of them. For high availability, we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections.

**Prerequisites**

A whitelist is configured for the replica set instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

**View connection strings**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances** page, click the ID of an instance.

4. In the left-side navigation pane, click **Database Connections** to view connection strings.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/cdd0f8d3e408ad55afefa880d0f36359.png)

**Description of connection strings**

| Item | Description |
| --- | --- |
| Connection address type | • Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Apsara Stack services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists.<br>• VPC endpoint: Virtual private cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and higher performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance. |
| Role | • Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance.<br>• Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance.<br>• Connection String URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and high availability. |
| Connection string | The connection string of a primary or secondary node is in the following format:<br><code>&lt;host&gt;:&lt;port&gt;</code><br>• &lt;host&gt;: the endpoint used to connect to the replica set instance.<br>• &lt;port&gt;: the port number used to connect to the replica set instance. |

<table>
  <tr>
    <td>Connection string URI</td>
    <td>A connection string URI is in the following format:<br><code>mongodb://[username:password@]host1[:port1][,host2[:port2],...</code><br><code>[,hostN[:portN]]][/[database][?options]]</code><br>• mongodb://: the prefix of the connection string URI.<br>• username:password@: the username and password used to log on to the replica set instance. You must separate them with a colon (:).<br>• hostX:portX: the endpoint and port number used to connect to the replica set instance.<br>• /database: the name of the database corresponding to the username if authentication is enabled.<br>• ?options: the additional options that are used to connect to the replica set instance.<br>Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. This way, when a node fails, the read and write operations of your application are not affected as a result of the failover.</td>
  </tr>
</table>

**Related topics**

- Use the mongo shell to connect to an ApsaraDB for MongoDB instance

<a id="section-11-9"></a>

## 11.9. Overview of sharded cluster instance connections

ApsaraDB for MongoDB sharded cluster instances support both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node and use a connection string URI to connect to multiple mongos nodes. For high availability (HA), we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections.

**View connection strings**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Sharded Cluster Instances** page, click the ID of the instance whose connection strings you want to view.

4. In the left-side navigation pane, click **Database Connections** to view connection strings.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/b29c9820621692aad42dadb422352163.png)

**Description of connection strings**

| Item | Description |
| --- | --- |
| Connection address type | • Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists.<br>• VPC endpoint: Virtual Private Cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance.<br>• Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |
| Mongos node ID | The connection string of a mongos node is in the following format:<br><code>&lt;host&gt;:&lt;port&gt;</code><br>• &lt;host&gt;: the endpoint used to connect to the instance.<br>• &lt;port&gt;: the port number used to connect to the instance.<br>Note During routine tests, you can use a connection string to directly connect to a mongos node. |
| Connection string URI | A connection string URI is in the following format:<br><code>mongodb://[username:password@]host1[:port1][,host2[:port2],...</code><br><code>[,hostN[:portN]]][/[database][?options]]</code><br>• mongodb://: the prefix of a connection string URI.<br>• username:password@: the username and password used to log on to the instance.You must separate them with a colon (:).<br>• hostX:portX: the endpoint and port number used to connect to the instance.<br>• /database: the name of the database corresponding to the username if authentication is enabled.<br>• options: the additional options that are used to connect to the instance.<br>Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads.If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |

<a id="section-12"></a>

# 12.Data security

<a id="section-12-1"></a>

## 12.1. Configure a whitelist for an ApsaraDB for MongoDB instance

This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or CIDR blocks that you use for database access to a whitelist of this instance. This improves database security and stability. Proper configuration of whitelists can enhance access security of ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis.

**Background information**

- The system creates a default whitelist for each instance. This whitelist can be modified or cleared but cannot be deleted.

- After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the **default** whitelist of this instance. The IP address 127.0.0.1 indicates that no IP addresses are allowed to access this instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.

5. On the page that appears, use one of the following methods to add IP addresses to a whitelist:

   - Manually modify a whitelist

     <ol type="a">

     <li>

     Click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt=""> in the **Actions** column corresponding to a whitelist and select **Manually**

     **Modify**.

     </li>

     <li>

     In the Manually Modify panel, enter IP addresses or CIDR blocks in the **IP White List** field.

     > **Note**
     >
     > - Separate multiple IP addresses with commas (,). A maximum of 1,000 different IP addresses can be added.
     >
     >   Supported formats are 0.0.0.0/0, IP addresses such as 10.23.12.24, or CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits.
     >
     > - If the IP address whitelist is empty or contains only  `0.0.0.0/0` , all devices are granted access. This poses risks to your ApsaraDB for MongoDB instance. We recommend that you add only the IP addresses or CIDR blocks of your own web servers to the whitelist.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Click **OK**.

     </li>

     </ol>

   - Load internal IP addresses of ECS instances

     <ol type="a">

     <li>

     Click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt=""> in the **Actions** column corresponding to a whitelist and select **Import ECS**

     **Intranet IP**.

     </li>

     <li>

     In the **Import ECS Intranet IP** panel, select the IP addresses that you want to add to

     the IP address whitelist and click <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/233e3f2c21f8fb696a90e02f68ea9383.png" width="46" alt=""> to add these IP addresses to the whitelist.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Click **OK**.

     </li>

     </ol>

<a id="section-12-2"></a>

## 12.2. Create or delete a whitelist

This topic describes how to create or delete a whitelist. Whitelists consist of the IP addresses allowed to access specific databases.

**Background information**

If your business involves multiple applications and you need to create a whitelist for each of them, you can sort the IP addresses of the applications into different whitelists.

**Create a whitelist**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the navigation pane on the left, choose **Data Security > Whitelist Settings**.

5. Click **Create Whitelist**.

6. In the **Create Whitelist** panel, specify **Group Name** and **IP Whitelist** and click **OK**.

   | Parameter | Description |
   | --- | --- |
   | Group Name | You can customize the group name based on the following rules.<br>• Start with a lowercase letter.<br>• End with a letter or a digit.<br>• Contain only lowercase letters, digits, and underscores (_).<br>• Be 2 to 32 characters in length. |

   <table>
     <tr>
       <td>IP Whitelist</td>
       <td>Enter the IP addresses or CIDR blocks to add. Both IPv4 and IPv6 whitelists are supported.<br>Note<br>• Separate multiple IP addresses with a comma (,). You can add up to 1,000 unique IP addresses.<br>A whitelist can include IP addresses such as 0.0.0.0/0 and 10.23.12.24 or CIDR blocks such as 10.23.12.24/24. /24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32.<br>• Setting the whitelist to 0.0.0.0/0 removes all IP address restrictions. This creates a high security risk for your database.We recommend that you grant access only to the public IP addresses or CIDR blocks of your web servers.<br>• You can import and export IP lists in text format.</td>
     </tr>
   </table>

**Delete a whitelist**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the navigation pane on the left, choose **Data Security > Whitelist Settings**.

5. For the target whitelist group, click **Delete Whitelist Group** in the **Actions** column.

   > **Note**
   >
   > You cannot delete the **default** group.

6. In the **Delete Whitelist Group** message, click **OK**.

<a id="section-12-3"></a>

## 12.3. Enable the audit log feature

You can view the statement execution logs, operational logs, and error logs of an instance in the ApsaraDB for MongoDB console. This helps you locate and analyze faults.

**Usage notes**

- Audit logs are retained for seven days. Expired logs are deleted.

- If you disable the audit log feature for an instance, saved logs are deleted.

- If you enable the audit log feature for an instance for the first time, the **admin** and **slow** operation types are selected by default.

- If you disable the audit log feature for an operation type, the system stops collecting logs related to this operation type. However, the collected logs are still retained.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the ID of the instance that you want to manage.

4. In the left-side navigation pane, choose **Data Security > Audit Logs**.

5. In the upper-left corner of the page, click **Enable Audit Log**.

6. In the **Enable Audit Log** message, click **OK**.

   After the audit log feature is enabled, you can query audit logs by **time range**, **keyword**, and **database name**. In addition, you can perform the following operations:

   - **Sort SQL statements in descending order of duration (recommended)**

     - Feature description: The system intelligently aggregates and sorts SQL statements that occupy the most resources in descending order of duration.

     - Benefits: This feature helps O&M engineers quickly locate slow SQL statements, optimize indexes, and fine-tune SQL statements. It ensures the stability of your system in high-concurrency scenarios.

     - How to perform: On the Audit Logs page, select the **Sort by Top SQL time-consuming** check box and click Search to view the SQL statements.

   - **Create an export task**: You can export audit log files.

   - **View the list of exported files**: You can view audit log files in a list.

   - **Disable audit logs**: After you disable this feature, the system stops collecting database operation information and deletes all saved audit logs.

   - **Audit log filter setting**: You can modify the types of operations to be audited. The following table describes the operation types available in different architectures.

     **Instance type**

     **Audit type**

     **Operation type**

     - **admin**: O&M operations

     - **slow**: slow queries

     - **query:**: queries

     Replica set instance

     **db**

     - **insert**: insert operations

     - **update**: update operations

     - **delete**: delete operations

     - **command**: all commands

     - **admin**: O&M operations

     - **slow**: slow queries

     - **query:**: queries

     **db**

     - **insert**: insert operations

     - **update**: update operations

     - **delete**: delete operations

     - **command**: all commands

     Sharded cluster instance

     - **admin**: O&M operations

     - **slow**: slow queries

     **mongos**

     - **insert**: insert operations

     - **update**: update operations

     - **delete**: delete operations

<a id="section-12-4"></a>

## 12.4. Configure SSL encryption

This topic describes how to enable Secure Sockets Layer (SSL) encryption for an instance to enhance connection security. After you enable SSL encryption, you must install SSL certificates that are issued by certificate authorities (CAs) on your application. SSL encryption can encrypt connections at the transport layer to improve data security and ensure data integrity. This topic describes the operations related to SSL encryption.

**Prerequisites**

A replica set instance is created.

**Impacts**

When you enable or disable SSL encryption or renew SSL certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your applications can automatically reconnect to the instance.

> **Note**
>
> When an instance is restarted, all its nodes are restarted in turn and each node experiences a temporary disconnection of approximately 30 seconds. If the instance houses more than 10,000 collections, the temporary disconnection lasts even longer.

**Usage notes**

- You can download SSL certificate files only from the ApsaraDB for MongoDB console.

- After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary. For example, you can enable SSL encryption when you connect to an ApsaraDB for MongoDB instance over the Internet.

  > **Note**
  >
  > In most cases, connections that are established to the internal endpoint of your instance are secure and do not require SSL encryption.

- After you enable SSL encryption for an instance, both SSL and non-SSL connections are supported.

**Method 1**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set instance List** page, find the instance that you want to manage and click the ID of the instance.

4. In the left-side navigation pane, choose **Data Security > SSL**.

5. Perform operations described in the following table based on your business requirements.

   > **Note**
   >
   > When you enable or disable SSL encryption or renew SSL certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your applications can automatically reconnect to the instance.

   | Operation | Prerequisites | Procedure |
   | --- | --- | --- |
   | Enable SSL encryption | SSL encryption is in the <strong>Disabled</strong> state. | i. Turn on <strong>SSL Status</strong>.<br>ii. In the <strong>Restart Instance</strong> message, click <strong>OK</strong>. |
   | Renew an SSL certificate | SSL encryption is in the <strong>Enabled</strong> state. | i. Click <strong>Update Certificate</strong>.<br>ii. In the <strong>Restart Instance</strong> message, click <strong>OK</strong>. |
   | Download an SSL certificate | SSL encryption is in the <strong>Enabled</strong> state. | Click <strong>Download Certificate</strong> to download the SSL certificate to your on-premises machine. |
   | Disable SSL encryption | SSL encryption is in the <strong>Enabled</strong> state. | i. Turn off <strong>SSL Status</strong>.<br>ii. In the <strong>Restart Instance</strong> message, click <strong>OK</strong>. |

**Method 2**

> **Note**
>
> The following procedure applies only to ApsaraDB for MongoDB V8.0 and V7.0.

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set instance List** page, find the instance that you want to manage and click the ID of the instance.

4. In the left-side navigation pane, choose **Data Security > SSL**.

5. On the right side of the page, configure the parameters.

   | Parameter | Description |
   | --- | --- |
   | Select Configuration Mode | • <strong>Simple Mode</strong>: You do not need to configure a client certificate. This mode is suitable for basic SSL encryption scenarios.<br>• <strong>Complete Mode</strong>: You need to configure access control lists (ACLs) and certificates.This mode is suitable for scenarios that require higher security. |
   | Select Certificate Type | Select the source of the SSL certificate. We recommend that you use a certificate hosted in the cloud for better security and convenience. |
   | Select Connection String to Protect | Select a database endpoint that requires SSL encryption. You can select an internal endpoint. |

6. Click **Enable SSL Encryption**.

   > **Note**
   >
   > - The result of the operation is displayed after a short period of time.
   >
   > - You can also click **Modify Expiry** or **Download CA Certificate** to perform the corresponding operation.
   >
   >   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/09505941bb057d7fca0859f6ac64538f.jpeg)

<a id="section-12-5"></a>

## 12.5. Configure TDE for an ApsaraDB for MongoDB instance

You can use transparent data encryption (TDE) to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to the disk and is decrypted when it is read from the disk to the memory. TDE does not increase the sizes of data files. You do not need to modify your application to use TDE. To improve data security, you can enable TDE for an instance in the ApsaraDB for MongoDB console to encrypt instance data.

**Prerequisites**

The MongoDB version of the instance is 4.0.

> **Note**
>
> Before you enable TDE, you can create an instance that runs MongoDB 4.0 to
>
> test the compatibility between your application and the database version. You can release the instance after the test is complete.

**Impacts**

- When you enable the TDE feature, your instance is restarted and a transient connection occurs. We recommend that you enable the TDE feature during off-peak hours and make sure that your application can automatically reconnect to the instance.

- TDE increases the CPU utilization of your instance.

**Usage notes**

- You cannot disable TDE after it is enabled.

- You can enable TDE for an instance and disable encryption for a collection.

  > **Note**
  >
  > If you have specific requirements, you can disable encryption for a
  >
  > collection when you create the collection. For more information, see the Disable encryption for a specified collection section of this topic.

- After you enable TDE, only new collections are encrypted. Existing collections are not encrypted.

- Key Management Service (KMS) generates and manages the keys used by TDE. ApsaraDB for MongoDB does not provide keys or certificates required for encryption.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** page, find the instance that you want to manage.

3. Click the ID of the instance. You can also click the

   icon in the **Actions** column

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   corresponding to the instance and then select **Manage** to go to the **Basic Information** page.

4. In the left-side navigation pane, choose **Data Security > TDE**.

5. Turn on TDE Status to enable TDE.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/7dca3416c85dd698f0cef75cda5176fe.png)

6. In the **Restart Instance** message, select **Use Automatically Generated Key** or **Use Custom Key**.

7. In the message that appears, click **OK**. The instance state changes to **Modifying TDE**. After the state changes to **Running**, TDE is enabled.

**Disable encryption for a specified collection**

After you enable TDE, all new collections are encrypted. When you create a collection, you can perform the following steps to disable encryption for the collection:

1. Use the mongo shell to connect to an ApsaraDB for MongoDB database. For more information, see Use the mongo shell to connect to an ApsaraDB for MongoDB instance.

2. Run the following command to create a collection and disable encryption for the collection:

   ```text
   db.createCollection("<collection_name>",{ storageEngine: { wiredTiger: { 
   configString: "encryption=(name=none)" } } })
   ```

   > **Note**
   >
   > &lt;collection_name>: the name of the collection.

   Examples

   ```text
   db.createCollection("customer",{ storageEngine: { wiredTiger: { configString: "encryption=(name=none)" } } })
   ```

<a id="section-12-6"></a>

## 12.6. Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB database in Secure Sockets Layer (SSL) encryption mode. SSL encryption can encrypt network connections at the transport layer to improve data security and ensure data integrity.

**Prerequisites**

- The instance is a replica set instance that runs MongoDB 4.0 or 4.2.

- The mongo shell of the required version is installed on the on-premises server or Elastic Compute Service (ECS) instance from which you want to connect to the database. For more information about how to install the mongo shell, see Install MongoDB.

- SSL encryption is enabled for the instance. For more information, see Configure SSL encryption for an ApsaraDB for MongoDB instance.

- The IP address of the on-premises server or ECS instance is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist.

**Usage notes**

After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary.

**Procedure**

An on-premises server with a Linux operating system is used in the following example.

1. Download the SSL CA certificate. For more information, see Configure SSL encryption for an ApsaraDB for MongoDB instance.

2. Decompress the package and upload the certificate files to the on-premises server or the ECS instance on which the mongo shell is installed.

   > **Note**
   >
   > In this example, the .pem file is uploaded to the /root/sslcafile/ directory of
   >
   > the on-premises server.

3. On the on-premises server or the ECS instance, run the following command to connect to a database of the ApsaraDB for MongoDB instance:

   ```text
   mongo --host <host> -u <username> -p --authenticationDatabase <database> --ssl --sslC
   AFile <sslCAFile_path> --sslAllowInvalidHostnames
   ```

   > **Note**
   >
   > - If you want to connect to a database of the ApsaraDB for MongoDB instance over an internal network, make sure that the ApsaraDB for MongoDB instance has the same network type as the ECS instance. If the network type is Virtual Private Cloud (VPC), make sure that the two instances are in the same VPC.
   >
   > - &lt;host>: the endpoint of the primary node or a secondary node in a replica set instance or a mongos node in a sharded cluster instance. For more information, see Overview of replica set instance connections or Overview of sharded cluster instance connections.
   >
   > - &lt;username>: the database account of the ApsaraDB for MongoDB instance. The initial account is root.
   >
   > - &lt;database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin.
   >
   > - &lt;sslCAFile_path>: the path of the SSL CA certificate files.

   Example:

   ```text
   mongo --host dds-bpxxxxxxxx-pub.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticationDatabase admin --ssl --sslCAFile /root/sslcafile/ApsaraDB-CA-Chain.pem  --sslAllowInvalidHostnames
   ```

4. When Enter password: is displayed, enter the password for the database account and press the Enter key.

   > **Note**
   >
   > - The password characters are masked when you enter the password.
   >
   > - If you forget the password of the root user, you can reset the password. For more information, see Reset the password for an ApsaraDB for MongoDB instance.

<a id="section-13"></a>

# 13.Tag management

<a id="section-13-1"></a>

## 13.1. Add or create tags

You can add tags to one or more instances and filter the instances by tag.

**Prerequisites**

An ApsaraDB for MongoDB instance is created.

**Limits**

A maximum of 20 tags can be added to an instance.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. Find the instance to which you want to add tags, move the pointer over the tag column, and

   then click the <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/d7298f91f48c4416cbaf24a397240378.png" width="16" alt=""> icon.

4. In the **Edit Tags** dialog box, click **Add**.

5. Enter a tag key and a tag value in the fields below **Tag Key** and **Tag Value**.

   If you want to add an existing tag, click the corresponding field and select an existing tag key and tag value from the drop-down list.

6. Click **OK**.

<a id="section-13-2"></a>

## 13.2. Filter instances by tag

After you add tags to ApsaraDB for MongoDB instances, you can filter the instances by tag in the instance list to quickly find the instances of a specified category.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Instance List** page, click **Advanced Filter**.

4. On the right side of **Filter by Tag**, select a **tag key** and a **tag value** from the drop-down list.

5. Click **Search**.

<a id="section-13-3"></a>

## 13.3. Remove or delete a tag

When a tag is no longer required in an ApsaraDB for MongoDB instance, you can remove the tag from the instance. If the tag is not added to other instances, the tag is deleted.

**Usage notes**

- You can remove up to 20 tags at a time.

- If you remove a tag from all instances to which the tag is added, the tag is automatically deleted.

- Removing a tag does not affect the normal operation of the instance. After all tags of the instance are removed, the instance cannot be filtered by tag.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. Find the instance to which you want to add tags, move the pointer over the tag column, and

   then click the <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/d7298f91f48c4416cbaf24a397240378.png" width="16" alt=""> icon.

4. In the **Edit Tags** dialog box, click the <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/65a9b9e0396406daa76e69116ddb843a.png" width="16" alt=""> icon next to the tag that you want to delete.

5. Click **OK**.

<a id="section-14"></a>

# 14.Zone-disaster recovery

<a id="section-14-1"></a>

## 14.1. Create a dual-zone replica set instance

This topic describes how to create a dual-zone replica set instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the reliability and availability of your replica set instance. This solution deploys the three nodes of a replica set instance across two different zones within one region. The components in these zones exchange data over an internal network. When one of the two zones becomes unavailable due to unexpected events such as a power or network failure, the high-availability (HA) system switches services over to another zone.

**Deployment policies**

The primary, secondary, and hidden nodes of a replica set instance are deployed in two different zones within one region.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances**.

3. On the **Replica Set Instances** page, click **Create Instance**.

4. On the **Create ApsaraDB for MongoDB Instance** page, configure parameters.

   > **Note**
   >
   > - For the **Zone** parameter, you must select dual zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region.
   >
   > - For more information, see Procedure.

5. Click **Submit**.

<a id="section-14-2"></a>

## 14.2. Create a dual-zone sharded cluster instance

This topic describes how to create a dual-zone sharded cluster instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the high availability (HA) of your sharded cluster instances. This solution deploys the components of a sharded cluster instance across two different zones within the same region. The components in these zones exchange data over an internal network. If one zone becomes unavailable due to uncontrollable circumstances, the HA system automatically switches business over to the other zone to ensure service continuity of the sharded cluster instance.

**Deployment policies**

The components of a sharded cluster instance are deployed across two different zones within one region.

- Mongos nodes are evenly deployed across all data centers. At least two mongos nodes are deployed at a time, with each in one zone. Each new mongos node added later is deployed to one of the zones in turn.

- The primary, secondary, and hidden nodes in each shard node are not deployed to the two zones in sequence. The deployment of these nodes may change when manual switchover or HA failover between primary and secondary nodes is triggered.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Sharded Cluster Instances**.

3. On the **Sharded Cluster Instances** page, click **Create Instance**.

4. On the **Create ApsaraDB for MongoDB Sharded Cluster Instance** page, configure the required parameters.

   > **Note**
   >
   > - For the **Zone** parameter, you must select two zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region.
   >
   > - For more information, see Create a replica set instance.

5. Click **OK**.

<a id="section-15"></a>

# 15.AI capability

<a id="section-15-1"></a>

## 15.1. One-click migration

<a id="section-15-1-1"></a>

### 15.1.1. Migrate data between MongoDB databases

After you create an ApsaraDB for MongoDB instance, you can use Data Transmission Service (DTS) to migrate data to the ApsaraDB for MongoDB instance. You only need to change the service address after the migration.

**Supported source and destination databases**

**Source instance**

**Destination**

**version**

**instance version**

3.0

8.0

3.0

3.4

8.0

4.0

8.0

4.0

4.2

8.0

8.0

5.0

5.0

8.0

6.0

6.0

8.0

7.0

7.0

8.0

8.0

8.0

8.0

3.0

7.0

3.0

3.4

7.0

4.0

7.0

4.0

7.0

4.2

7.0

5.0

5.0

7.0

6.0

6.0

7.0

3.0

6.0

6.0

3.0

3.4

6.0

4.0

6.0

4.0

4.2

6.0

5.0

5.0

6.0

3.0

5.0

5.0

3.0

3.4

5.0

4.0

5.0

4.0

4.2

5.0

3.0

4.2

3.0

3.4

4.2

4.0

4.0

4.2

4.0

3.0

4.0

3.0

3.4

4.0

**Prerequisites**

Replica-to-replica migration:

- A source ApsaraDB for MongoDB replica set instance and a destination ApsaraDB for MongoDB replica set instance are created.

- A whitelist is created for the source instance and destination instance. The IP address 0.0.0.0/0 is added to the whitelist.

- The data migration information, including the business database, account, and password, is prepared.

- Whether the ports of the source and destination instances are the same is determined if you want to change the database connection address. The connection address cannot be changed if the source database and destination database are on the same instance.

- The available storage space of the destination ApsaraDB for MongoDB instance is 10% larger than the total size of the data in the source ApsaraDB for MongoDB instance.

Shard--to-shard migration (conditional support):

- A source ApsaraDB for MongoDB replica set instance and a destination ApsaraDB for MongoDB sharded cluster instance are created.

- A whitelist is created for the source instance and destination instance. The IP address 0.0.0.0/0 is added to the whitelist.

- The data migration information, including the business database, account, and password, is prepared.

- Shard connection between the source and destination instances is enabled.

- The source and destination clusters have the same number of mongos nodes.

- Only the mongos addresses are changed. The connection addresses between the shards and configserver node remain unchanged.

- Whether the ports of the source and destination instances are the same is determined if you want to change the database connection address. The connection address cannot be changed if the source database and destination database are on the same instance.

**Usage notes**

| Category | Description |
| --- | --- |
| Limits on the source database | • Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases.<br>• The collections to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records.<br>• If you select collections as the objects to be migrated and you need to edit collections in the destination database, such as renaming collections, up to 1,000 collections can be migrated in a single data migration task. If you run a task to migrate more than 1,000 collections, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the collections or configure a task to migrate the entire database.<br>• The size of a single data entry in the source database cannot exceed 16 MB.Otherwise, the data migration task fails. |

<table>
  <tr>
    <td>Other limits</td>
    <td>• DTS cannot migrate data from the admin or local database.<br>• If a primary or unique key conflict occurs when DTS writes data to the destination collection, DTS skips the corresponding data write statement and retains the existing data in the destination collection.<br>• DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the <code> REVOKE </code> statement to revoke the write permissions from the accounts that DTS uses to access the destination database. Otherwise, the data in the source database overwrites the data in the destination instance after the failed data migration task is resumed.<br>• You must use the <code> db.$table_name.aggregate([{ $count:"myCount"}]) </code> syntax to query the return value of a count operation on the destination ApsaraDB for MongoDB database.</td>
  </tr>
</table>

**Compatibility changes of MongoDB major versions**

The following table describes the compatibility changes of MongoDB major versions.

| Version | Description |
| --- | --- |
| MongoDB 8.0 | • We recommend that you do not use the <code> tcmallocAggressiveMemoryDecommit </code> parameter.<br>• The <code> tcmallocReleaseRate </code> parameter specifies the memory release rate.By default, ApsaraDB for MongoDB uses a value of 10 MB/s.<br>• If <code> null </code> is used as a query condition, MongoDB does not match <code> undefined </code> values.<br>• We recommend that you do not use index filters.<br>• We recommend that you do not use <code> timeField </code> as the shard key for time series sets.<br>• We recommend that you do not use the <code> cleanupOrphaned </code> command.<br>• The <code> compact </code> command cannot be executed concurrently in the same set.<br>• Before you upgrade to MongoDB 8.0, you must rename or delete any non-time-series set named <code> system.buckets </code>, if such a set exists. |

<table>
  <tr>
    <td>MongoDB 7.0</td>
    <td>• When you upgrade the major version of an instance to MongoDB 7.0, no compatibility issues exist.<br>• If you want to downgrade an instance from MongoDB 7.0 to an earlier major version, you must remove the features supported by MongoDB 7.0, such as the following items:<br>• Remove all <code> columnar indexes </code>.<br>• Unregister the cluster parameters specified by the <code> setClusterParameter </code> command.<br>• Remove all collections that are created with the <code> encryptedFields </code> option.<br>• Remove all <code> compound wildcard indexes </code>.</td>
  </tr>
  <tr>
    <td>MongoDB 6.0</td>
    <td>• If the memory used by an aggregation pipeline exceeds 100 MB, data is written to temporary files on disk by default.<br>If you use a version earlier than MongoDB 6.0, you must use the <code> { </code><code>allowDiskUse: true } </code> syntax to write data to temporary files on disk.<br>• If you specify <code> * </code> in the <code> dropIndexes </code> command, you can drop all indexes except <code> _id </code> and the shard key index.<br>• The mongo shell is deprecated. Use mongosh instead.<br>• Operators, such as <code> $explain </code>, <code> $hint </code>, <code> $max </code>, and <code> $maxTimeMS </code>, are deprecated.<br>• If the <code> expireAfterSeconds </code> parameter of a time-to-live (TTL) index is set to <code> NaN </code>, it is treated as <code> 0 </code>, which may immediately remove expired documents.<br>• The <code> SCRAM-SHA-1 </code> mechanism is deprecated.<br>• The <code> reIndex </code> command and the corresponding <code> reIndex() </code> method are deprecated.</td>
  </tr>
  <tr>
    <td>MongoDB 5.0</td>
    <td>• The <code> read concern </code> level of secondary nodes is changed from <code> available </code> to <code> local </code>.<br>• The default <code> write concern </code> level is changed from <code> 1 </code> to <code> majority </code>.<br>• The <code> db.collection.ensureIndex() </code> method is deprecated. You can use the <code> db.collection.createIndex() </code> method instead.<br>• The parameters of the <code> saslStart </code> and <code> saslContinue </code> commands are strictly validated and not supported by the MongoDB driver for Go (<code> mgo </code>).The <code> saslContinue </code> command contains only the <code> conversationId </code> and <code> payload </code> parameters, whereas <code> mgo </code> has an additional <code> mechanism </code> parameter.<br>• The <code> geoSearch </code> command is deprecated.</td>
  </tr>
  <tr>
    <td>MongoDB 4.4</td>
    <td>• The <code> force </code> option is no longer supported by the <code> compact </code> command.<br>• The <code> geoSearch </code> command is deprecated.<br>• You can create indexes on both the primary and secondary databases to reduce the latency caused by index creation. This way, when an index is being created, the secondary database can still access the latest data.</td>
  </tr>
  <tr>
    <td>MongoDB 4.2</td>
    <td>• The <code> geoNear </code> command is deprecated. Use the <code> $geoNear </code> <code>(aggregation) </code> command instead.<br>• The <code> repairDatabase </code> command is deprecated.<br>• The <code> cloneCollection </code> command is deprecated. Use the <code> mongoexport </code> and <code> mongoimport </code> tools instead.<br>• The <code> afterClusterTime </code> read concern option is deprecated.<br>• Drivers that are compatible with MongoDB 4.2 or later enable retryable writes by default.<br>• The <code> group </code>, <code> copydb </code>, and <code> clone </code> commands are deprecated.</td>
  </tr>
  <tr>
    <td>MongoDB 4.0</td>
    <td>• The <code> reIndex </code> command obtains a global exclusive (W) lock and blocks other operations until an index is rebuilt.<br>• The <code> copydb </code> and <code> clone </code> commands are deprecated.</td>
  </tr>
  <tr>
    <td>MongoDB 3.6</td>
    <td>• The use of the <code> aggregate </code> command without the cursor option to return a single document is deprecated. Unless you include the explain option, you must specify the <code> cursor </code> option. You can use the <code> cursor </code> option to specify a <code> batch </code> size.<br>• In MongoDB 3.6 and later versions, the query for <code> $type: "array" </code> returns documents where the field itself is an array. In versions earlier than MongoDB 3.6, the query for $type: "array" returns documents where the field itself is an array that contains at least one element of the array type.<br>• The following changes to array ordering are added:<br>• The optional <code> sort </code> option is added to the <code> find </code> command to provide the ordering of results.<br>• <code> $sort </code> in the <code> $sort(aggregation) </code> stage has a memory limit of 100 MB.<br>• If an update operation involves multiple fields, the fields are added in lexicographical order.<br>• The <code> snapshot </code> query option is deprecated.</td>
  </tr>
  <tr>
    <td>MongoDB 3.4</td>
    <td>• The <code> group </code> command is deprecated. Use the <code> db.collection.aggregate() </code> or <code> db.collection.mapReduce() </code> method instead.<br>• The <code> $in </code> expression is used in an <code> update </code> operation with the <code> upsert </code> option set to true to determine whether matching documents exist.<br>Example:<br><code>db.c.drop()</code><br><code>db.c.update({a:{$in:[1]}},{$addToSet:{a:2}},{upsert:true}) // A</code><br><code>document cannot be inserted in MongoDB 3.4, but can be inserted</code><br><code>in MongoDB major versions earlier than 3.4.</code><br><code>db.c.update({a:{$elemMatch:{$in:[2]}}},{$addToSet:{a:2}},</code><br><code>{upsert:true}) // A document can be successfully inserted in</code><br><code>MongoDB 3.4.</code></td>
  </tr>
</table>

**Required account permissions**

<table>
  <tr>
    <th>Database</th>
    <th>Database and schema migration</th>
    <th>Full data migration</th>
    <th>Incremental data migration</th>
  </tr>
  <tr>
    <td>Source instance</td>
    <td colspan="2">Read permissions on the database to be migrated and the config database.</td>
    <td>Read permission on the source database, the admin database, and the local database</td>
  </tr>
  <tr>
    <td>Destination instance</td>
    <td colspan="3">The dbAdminAnyDatabase permission, the read and write permissions on the destination database, and the read permissions on the local database.</td>
  </tr>
</table>

**Use DTS to migrate data**

**Procedure**

1. Log in to the **ApsaraDB for MongoDB console**.

2. In the left-side navigation pane, choose **AI Capabilities > Intelligent Migration**. On the Data Migration page, click **To migrate** and configure the source and destination databases.

   | Section | Parameter | Description |
   | --- | --- | --- |
   | N/A | Task Name | The name of the migration task. DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |

   The region in which the source ApsaraDB for MongoDB instance

   **Instance**

   resides. The region is the source region that you selected when

   **Region**

   you created the data migration task. You cannot change the value of this parameter.

   **Replicate Data Across**

   Specifies whether to migrate data between instances that

   **Alibaba**

   belong to different Alibaba Cloud accounts. Select **No**.

   **Cloud Accounts**

   Select **Replica Set** or **Sharded Cluster**.

   > **Note**

   **Architecture**

   > If you select Sharded Cluster, you must apply for shards for both the source and destination instances.

   **Source Database**

   **Instance ID**

   The ID of the source instance.

   The name of the authentication database in which the database account is created.

   **Authenticati**

   > **Note**

   **on Database**

   > If you want to use the root account, enter admin in the Database Name field.

   The account of the source database. The account must have the

   **Database**

   read permissions on the source database, admin database, and

   **Account**

   local database.

   **Database**

   The password of the database account.

   **Password**

   The region in which the destination ApsaraDB for MongoDB

   **Instance**

   instance resides. The region is the destination region that you

   **Region**

   selected when you created the data migration task. You cannot change the value of this parameter.

   **Architecture**

   Select **Replica Set** or **Sharded Cluster**.

   **Instance ID**

   The ID of the destination ApsaraDB for MongoDB instance.

   The name of the authentication database in which the database account is created.

   **Authenticati**

   > **Note**

   **on Database**

   > If you want to use the root account, enter admin in the Database Name field.

   The account of the destination database. The account must have

   **Database**

   the read permissions on the destination database, admin

   **Account**

   database, and local database.

   **Database**

   The password that is used to access the database.

   **Password**

3. In the lower part of the page, click **Test Connectivity and Proceed**.

4. Select the objects to be migrated and the migration types. The following table describes the parameters.

   | Parame ter | Description |
   | --- | --- |
   | Task Stages | • To perform only full data migration, select <strong>Schema Migration</strong> and <strong>Full Data</strong> <strong>Migration</strong>.<br>• To ensure service continuity during data migration, select <strong>Schema Migration</strong>, <strong>Full</strong> <strong>Data Migration</strong>, and <strong>Incremental Data Migration</strong>.<br>Note<br>If <strong>Incremental Data Migration</strong> is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
   | Process ing Mode of Conflict ing Tables | • <strong>Precheck and Report Errors</strong>: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started.<br>• <strong>Ignore Errors and Proceed</strong>: skips the precheck for identical table names in the source and destination databases.<br>Warning<br>If you select <strong>Ignore Errors and Proceed</strong>, data inconsistency may occur, and your business may be exposed to potential risks.<br>• If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database.<br>• If the source and destination databases have different table schemas, only specific columns are migrated, or the data migration task fails. |
   | Source Objects | Select one or more objects in the <strong>Available</strong> section and add the objects to the <strong>Selected</strong> section.<br>Note<br>• You can use the navigation tree to search for one or more objects.<br>• You can select tables or databases as the objects to be migrated. |
   | Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged.<br>Note<br>• To select the SQL operations performed on a specific database or table, right-click the object in the <strong>Selected Objects</strong> section. In the dialog box that appears, select the SQL operations that you want to migrate.<br>• If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

5. Click **Next: Advanced Settings** to configure advanced settings. The following table describes the parameters.

   | Parameter | Description |
   | --- | --- |
   | Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes.Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails.<br>Note<br>If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
   | Configure ETL | Select <strong>Yes</strong> or <strong>No</strong> based on your business requirements. |

6. In the lower part of the page, click **Next: Precheck and Start Task**.

   > **Important**
   >
   > - Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
   >
   > - If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

7. Wait until **Success Rate** displays 100% and then click **Back**.

   > **Note**
   >
   > If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

**Switch to the endpoint of the destination database**

Select a successful record from the migration result list and click **Migrate Endpoint** to switch to the endpoint of the destination database. After you update the DNS record, clients may still be connected to the source database due to the caching mechanism. You need to close the connections to the source database.

<a id="section-15-2"></a>

## 15.2. AI-native MCP service

The MongoDB AI-native MCP (Model Context Protocol) service provides a standard, secure, and efficient protocol for large models to access your database. By using MCP, AI applications can directly query data, execute SQL, or manage database instances without complex coding, accelerating the development of AI-native use cases such as Retrieval-Augmented Generation (RAG), intelligent operations, and data-driven Q&A.

**Access**

On the **MongoDB console > AI Capability > AI-native MCP service** page, you can explore and use various MCP integration methods to efficiently connect your AI applications to your databases.

**Integration methods**

The MCP service offers three flexible integration methods to meet different needs, from quick trials to production-ready integrations.

| Method | Use case | Details |
| --- | --- | --- |
| ApsaraCopilot-Managed Mode (Recommended for beginners) | Ideal for users who want to quickly test AI and database integration scenarios without deployment or development. | 1. Log on to the ApsaraCopilot platform.<br>2. On the home page, select the <strong>MCP Service</strong> entry.<br>3. The system automatically loads available MCP agents and services.<br>4. Select the required functional module. |
| AI Gateway-managed mode (Recommended for production integration) | Ideal for enterprise-level AI application integration. Alibaba Cloud hosts the backend services, which you can use immediately after activation. | 1. Log on to the AI Gateway console.<br>2. Navigate to <strong>Service Management</strong> &gt; <strong>MCP</strong> <strong>Service</strong>.<br>3. The system automatically loads available MCP agents and services.<br>4. Activate the required MCP services, such as the Mongo MCP Server and Mongo Management MCP services. |
| Self-deployment (For on-premises or custom scenarios) | Designed for users who require on-premises deployment, custom logic, or integration with their own agent or RPA systems. | 1. Download the MCP service package.<br>2. Deploy the package on an ECS instance, a container, or a non-cloud server.<br>3. Embed the MCP service as a backend service in your AI application, agent, or RPA workflow.<br>4. Call MCP functions through a RESTful API or SDK. |

**Supported MCP services**

You can access supported MCP services from the console.

![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/b29e16688196cf700b5055ea54676ece.jpeg)

**Mongo MCP Server**

- Overview: The Mongo MCP Server provides AI-native data management capabilities for MongoDB. This service offers a suite of tools for manipulating and querying data in MongoDB, enabling external applications, such as AI model agents, to access the database.

- Core functions:

  - `list_collections` : Lists all collections.

  - `find_tool` : Executes a query to find documents.

**Mongo Management MCP**

- Overview: The Mongo Management MCP provides native interfaces for ApsaraCopilot. It allows you to open the MCP service within ApsaraCopilot to enhance instance operations and management.

- Core functions:

  - `sql_query` : Runs SQL queries.

  - `execute_sql` : Executes SQL statements.

<a id="section-16"></a>

# 16.CloudDBA

<a id="section-16-1"></a>

## 16.1. Quick diagnostics

ApsaraDB for MongoDB supports the quick diagnostics feature. This feature performs diagnostics on instance status within a specified period of time to help you evaluate the health status of the instance from multiple aspects, such as slow query logs, tablespaces, and performance trends and quickly identify instance anomalies.

**Perform quick diagnostics**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the left-side navigation pane, choose **CloudDBA > One-click diagnosis**.

5. Click **Create Reports**.

6. In the **Create Reports** dialog box, specify a time range for which you want the system to perform diagnostics and then click **Confirmation**.

   > **Note**
   >
   > The time range cannot exceed one day. If you specify a shorter time range for diagnostics, more detailed statistics are collected in the diagnostic report.

7. Refresh the Diagnostic Report page to view the progress of the diagnostics task. After the diagnostic report is created, click **View Report** in the **Actions** column.

**Automatically generate diagnostic reports**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance, or click

   in the **Actions** column corresponding to the instance and select

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   **Manage**.

4. In the left-side navigation pane, choose **CloudDBA > One-click diagnosis**.

5. Click **Auto generating Report Settings**.

6. In the **Auto-generating Diagnostic Report Settings** dialog box, specify a time at which you want the system to automatically generate diagnostic reports.

   > **Note**
   >
   > Only **Scheduled Trigger** is supported.

7. Click **OK**.

**Diagnostic report details**

| Module | Description |
| --- | --- |
| Score | The instance's health score. If the score is not full, you can click <strong>Deduction Details</strong> to view specific deduction information. |
| Basic Instance Information | Displays the instance ID, specifications, database type, analysis node, region, and the name of the database being analyzed. |
| Summary | Displays key performance metrics: CPU utilization, memory usage, connections, disk usage, and IOPS usage. |
| Slow SQL Query | Displays the 10 statements with the longest execution time. |
| Tablespace | Displays the five tables that occupy the most space. |
| Performance Trend | Displays performance trends for CPU utilization, connections, memory usage, disk usage, and IOPS usage. |
| Download | Click <strong>Download</strong> in the navigation pane on the left to download the diagnostic report. |

<a id="section-16-2"></a>

## 16.2. Performance trends

This topic describes how to view performance trends in specific ranges, compare performance trends, and customize charts to view performance trends on an ApsaraDB for MongoDB instance.

**Go to the Performance page**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, choose **CloudDBA > Performance Trends**.

> **Note**
>
> For more information about performance trends, see **Performance trends**
>
> in **Database Autonomy Service User Guide**.

<a id="section-16-3"></a>

## 16.3. Real-time performance

This topic describes how to view real-time performance data of an ApsaraDB for MongoDB instance, such as read/write latency, queries per second (QPS), operations, connections, and network traffic.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, find the instance that you want to manage and click the ID of instance.

4. In the left-side navigation pane, choose **CloudDBA > Real-time Performance**.

**Page overview**

On the Real-time Performance page, you can click the Real-time Charts or Mongostat tab to view performance data. When you refresh the **Real-time Performance** page, the data on the Real-time Charts and Mongostat tabs is refreshed and **Available Refreshes** is reset in the upper-right corner.

- Real-time Charts tab

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/74b0a3165a68c1ec75486b53318ef8f3.png)

  By default, content on the **Real-time Charts** tab is displayed when you go to the Real-time Performance page. Line charts on the tab are refreshed every 5 seconds to provide up-to-date performance trends.

  > **Note**
  >
  > You can move the pointer over <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/77c23b484941e8abac59c412d165d153.png" width="22" alt=""> next to a performance metric to view
  >
  > the details of the metric.

- Mongostat

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/0b7325ffe086d83323fa504936587d70.png)

  Click the **Mongostat** tab to view Mongostat command outputs. A new line of real-time performance data is added every 5 seconds. The tab can contain up to 999 lines of data.

  > **Note**
  >
  > For more information about Mongostat command outputs, see mongostat.

<a id="section-16-4"></a>

## 16.4. Session management

The instance sessions feature allows you to view the statistics for sessions between an ApsaraDB for MongoDB instance and clients in real time. These statistics include clients, commands that were run, and connection duration. You can also close abnormal sessions based on your business requirements.

**View instance sessions**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, choose **CloudDBA > Sessions**.

   - If you turn on **Auto Refresh**, the system updates session data on the page every 5 seconds.

   - By default, the system displays only active sessions. You can turn on **Display All** to view all sessions.

   - In the **Session Statistics** section, you can view information about sessions in the **Overview**, **Statistics by Client**, and **Statistics by Namespace** charts.

**Terminate instance sessions**

> **Warning**
>
> To prevent unexpected results, we recommend that you do not terminate
>
> system-level sessions.

1. In the **Instance Sessions** section, select the session that you want to terminate.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/e5c26faeed631fccde689a910dfefdaa.png)

2. Click **Kill Selected**.

3. In the message that appears, click **OK**.

<a id="section-16-5"></a>

## 16.5. Storage analysis

This topic describes how to view storage analysis information, such as the information in the **Storage Overview**, **Exceptions**, **Storage Trend**, **Tablespaces**, and **Data Space** sections. The information helps you identify and resolve exceptions in the database storage to ensure database stability.

**Prerequisites**

The database version of the ApsaraDB for MongoDB instance is 4.0 or 4.2.

**Procedure**

1. Log in to the ApsaraDB for MongoDB console.

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances**.

3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an instance.

4. In the left-side navigation pane, choose **CloudDBA > Storage Analysis**.

5. In the upper-right corner, click **Re-analyze**. Then, wait until the analysis is complete.

6. Click the **Storage Overview** or **Data Space** tab to view analysis results.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/be16445505d80e7cd006940aded6e956.png)

   - For more information about the Storage Overview tab, see Storage Overview tab.

   - For more information about the Data Space tab, see Data Space tab.

**Storage Overview tab**

This tab contains four sections: **Storage**, **Exceptions**, **Storage Trend**, and **Tablespaces**.

- **Storage** section

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/97332b08b149a7e186ee73e1fd89669a.png)

  | Item | Description |
  | --- | --- |
  | Exception | The number of storage exceptions that are identified in the instance.ApsaraDB for MongoDB can identify the following types of exceptions:<br>• More than 90% of the storage capacity is used.<br>• The available physical storage space may be exhausted within seven days.<br>• A single collection contains more than 10 indexes. |
  | Avg Daily Increase in Last Week | The average daily increase of storage usage in the instance over the last seven days. Formula: (Size of available storage space at the time of collection - Size of available storage space seven days ago)/7.<br>Note<br>• This increase indicates the average daily increase over the last seven days at the time of collection.<br>• This parameter is suitable for scenarios in which the traffic volume remains stable. The value of this parameter is inaccurate in the event of abrupt storage changes that are caused by operations such as batch import, deletion of historical data, instance migration, or instance recreation. |
  | Available Days of Storage | The number of days during which storage space is available in the instance. Formula: Size of available storage space/Average daily increase over the last seven days.<br>Note<br>• 90+ indicates that the storage space is sufficient for more than 90 days of usage.<br>• This parameter is suitable for scenarios in which the traffic volume remains stable. The value of this parameter is inaccurate in the event of abrupt storage changes that are caused by operations such as batch import, deletion of historical data, instance migration, or instance recreation. |
  | Used Storage | The amount of storage space that is used in the instance to the total storage space. |

- **Exceptions** section

  Information about detected storage exceptions. You can resolve the exceptions based on the information in this section.

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/333b99c6cd84e1a32fbd997809840b96.png)

- **Storage Trend** section

  Changes in storage usage over the last week, such as changes in **used storage**, **data space**, and **log space**.

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/ad60e78bb7945022fb9882fa17434e4f.png)

- **Tablespaces** section

  Information about all tables, such as the database name, storage engine, and collection storage.

  ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/86162ed14c5350f44e687ee64bb51384.png)

  > **Note**
  >
  > You can click the name of a collection to view its indexes.

**Data Space tab**

The Data Space tab shows the total storage space and tablespace information of each database.

> **Note**
>
> - You can click the name of a data space to view its tablespace information.
>
> - You can click the name of a collection to view its indexes.

![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/d896c8fb4160178f62269decb37e8850.png)

<a id="section-16-6"></a>

## 16.6. Slow query logs

ApsaraDB for MongoDB allows you to identify, analyze, and track slow query logs and perform a diagnostics on the logs so that you can create indexes to make better use of instance resources.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console.

2. On the **Replica Set Instances** page, find the instance that you want to manage.

3. Click the ID of the instance. You can also click the

   icon in the **Actions** column

   <img src="en-mongodb-user-guide-v3.18.6-2607-20260831.assets/394036bb0d490cabb4f8f97c497e0511.png" width="15" alt="">

   corresponding to the instance and then select **Manage** to go to the **Basic Information** page.

4. In the left-side navigation pane, choose **CloudDBA > Slow Query Logs**.

   > **Note**
   >
   > By default, slow query logs generated in the last 15 minutes are displayed in the trend chart. You can also specify a time range and click **Search** to view the corresponding slow query logs. The maximum time range that you can specify is one day.

5. View details of slow query logs by using one of the following methods:

   Method 1:

   <ol type="i">

   <li>

   Click the **Slow Log Details** tab in the lower part of the page.

   </li>

   <li>

   On the **Slow Log Details** tab, select the database that you want to query.

   </li>

   </ol>

   > **Note**
   >
   > If the request content of the database is hidden, you can move the pointer over the corresponding **Request Content** column and view the complete content.

   Method 2:

   <ol type="i">

   <li>

   In the Slow Log Trend chart, click a point in time. Then, you can view the statistics of the slow query logs generated at the point in time on the **Slow Log Statistics** tab.

   ![](en-mongodb-user-guide-v3.18.6-2607-20260831.assets/64cf0c0c3606cc13458887b26aaa6e5e.png)

   </li>

   <li>

   On the **Slow Log Statistics** tab, click **Sample** in the **Actions** column.

   </li>

   </ol>

   In the **Slow Log Sample** dialog box, you can view details of the slow query log.

   > **Note**
   >
   > If the request content of the database is hidden, you can move the pointer over the corresponding **Request Content** column and view the complete content.

**Export slow query logs**

You can click **Export Slow Log** on the **Slow Log Statistics** tab to save the log data to your computer.

<a id="section-17"></a>

# 17.Appendix

<a id="section-17-1"></a>

## 17.1. Authorize a tenant organization to access SLB

This topic describes how to grant a tenant organization the permissions to access Server Load Balancer (SLB) and helps you efficiently resolve related issues.

> **Important**
>
> If you need to create and use IPv6 addresses for your business, you must ensure that the current tenant organization has explicitly granted database services the permissions to access SLB. If such permissions are not granted, IPv6 addresses cannot be created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the left-side navigation pane, click **Service-linked Roles**.

4. On the Service-linked Roles page, click **Create Service-linked Role** in the upper-left corner.

   Select **Server Load Balancer** for the **Service Name** parameter, and select the organization to which you want to grant permissions for the **Authorized Organization Name** parameter.

5. Click **OK**.
