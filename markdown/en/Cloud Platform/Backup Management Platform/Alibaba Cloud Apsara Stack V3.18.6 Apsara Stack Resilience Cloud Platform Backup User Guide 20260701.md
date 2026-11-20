Alibaba Cloud  
Apsara Stack  
Apsara Stack Resilience  
Cloud Platform Backup User  
Guide  
Product Version: V3.18.6  
Document Version: 20260701

**Table of Contents**

- [1.Go to the platform backup management page](#section-1)
- [2.Platform backup archive storage](#section-2)
    - [2.1. Create a platform backup archive storage](#section-2-1)
    - [2.2. Manage a platform backup archive storage](#section-2-2)
- [3.Configure platform backup archiving](#section-3)
    - [3.1. Configure miniRDS backup](#section-3-1)
    - [3.2. Configure PANGU master backup](#section-3-2)
    - [3.3. Configure opsDNS backup](#section-3-3)
    - [3.4. Configure DNS product backup](#section-3-4)
    - [3.5. Configure in-cloud OSS bucket backup](#section-3-5)
- [4.View platform backup archiving records](#section-4)

<a id="section-1"></a>

# 1.Go to the platform backup management page

This topic describes how to go to the platform backup management page in the Apsara Uni-manager Operations Console.

**Prerequisites**

- The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator.

  The endpoint of the Apsara Uni-manager Operations Console is in the following format: *regi on-id*.ops.console.*intranet-domain-id*.

- A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.

2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the ENTER key.

   ![](assets/9a170d3462a995734d5c308b15bd4e44.jpeg)

   > **Note**
   >
   > You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.

   > **Note**
   >
   > - Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator.
   >
   > - If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.
   >
   > - The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
   >
   >   To enhance security, your password must meet the following requirements:
   >
   >   - The password contains uppercase and lowercase letters.
   >
   >   - The password contains digits.
   >
   >   - The password contains at least one of the following special characters: ! @ # $ %
   >
   >   - The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On**.

5. In the top navigation bar, click **System Config**.

6. In the left-side navigation pane, click **Platform Backup Management**.

<a id="section-2"></a>

# 2.Platform backup archive storage

<a id="section-2-1"></a>

## 2.1. Create a platform backup archive storage

This topic describes how to create a storage for cloud platform backups.

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Storage**.

3. Click **Create Storage**.

4. Configure the parameters that are described in the following table.

   | Parameter | Description |
   | --- | --- |
   | Storage Name | Enter a name for the custom storage. Example: Storage 1. |
   | Protocol Type | Select a protocol based on your business requirements. Valid values:<br>• <strong>OSS</strong>: the object storage service provided by Apsara Stack.<br>• <strong>Amazon S3</strong>: the object storage service provided by Amazon Web Services (AWS). |
   | Address | • If the <strong>Protocol Type</strong> parameter is set to <strong>OSS</strong>, enter an OSS endpoint.<br>• If the <strong>Protocol Type</strong> parameter is set to <strong>Amazon S3</strong>, enter an Amazon S3 endpoint. |
   | AccessKey ID/Username | • If the <strong>Protocol Type</strong> parameter is set to <strong>OSS</strong>, enter an AccessKey ID or a username of OSS.<br>• If the <strong>Protocol Type</strong> parameter is set to <strong>Amazon S3</strong>, enter an AccessKey ID or a username of Amazon S3. |
   | AccessKey Secret/Password | • If the <strong>Protocol Type</strong> parameter is set to <strong>OSS</strong>, enter an AccessKey secret or a password of OSS.<br>• If the <strong>Protocol Type</strong> parameter is set to <strong>Amazon S3</strong>, enter an AccessKey secret or a password of Amazon S3. |
   | Bucket/Storage Path | • If the <strong>Protocol Type</strong> parameter is set to <strong>OSS</strong>, enter a storage path of OSS.<br>• If the <strong>Protocol Type</strong> parameter is set to <strong>Amazon S3</strong>, enter a storage path of Amazon S3. |
   | Storage Space | Specify the storage capacity. Unit: GB. |
   | Alert Threshold | Specify the threshold for reporting alerts. If the percentage of used storage space exceeds the threshold, an alert is reported. |

5. Click **OK**.

<a id="section-2-2"></a>

## 2.2. Manage a platform backup archive storage

This topic describes how to view the details of, modify, and delete a platform backup archive storage.

**Prerequisites**

A platform backup archive storage is created.

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Storage**.

3. On the Archive Storage page, perform operations based on your business requirements.

   - View the details of a storage: Find the platform backup archive storage that you want to view and click Details in the Actions column.

   - Modify a storage:

     - Find the platform backup archive storage that you want to modify and click **Edit** in the **Actions** column. You can modify the values of parameters except **Protocol Type**.

     - Click **OK**.

   - Delete a storage:

     - Find the platform backup archive storage that you want to delete and click **Delete** in the **Actions** column.

     - In the message that appears, click **OK**.

<a id="section-3"></a>

# 3.Configure platform backup archiving

<a id="section-3-1"></a>

## 3.1. Configure miniRDS backup

This topic describes how to configure a backup policy for miniRDS.

**Prerequisites**

- A backup archive storage is created. For more information, see .

- A database instance is created.

  > **Note**
  >
  > By default, the dbaas_db, perf_db, dukang_db, bak_db, robot_db, kmsdata, kmsdata_tiangong, idccrypto_data, os_meta, oss_chiji, ummak, account, location, diamond, schedulerx, ram_slave_proxy, subaccount, ram_master, and hsmidcdatabase instances can be backed up.

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Config**.

3. Click the **MiniRDS Backup** tab.

4. Configure the backup policy. The following table describes the parameters.

   > **Note**
   >
   > The preset backup policy is used. You need to only specify storage settings.

   | Parameter | Description |
   | --- | --- |
   | Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
   | Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.

6. Click **Add Backup Instance**.

7. Select the database instances that you want to back up, and then click **OK**.

<a id="section-3-2"></a>

## 3.2. Configure PANGU master backup

This topic describes how to configure a backup policy for the PANGU master.

**Prerequisites**

- A backup archive storage is created. For more information, see .

- A PANGU cluster is deployed.

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Config**.

3. Click the **PANGU Master Backup** tab.

4. Configure the backup policy. The following table describes the parameters.

   > **Note**
   >
   > The preset backup policy is used. You need to only specify storage settings.

   | Parameter | Description |
   | --- | --- |
   | Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
   | Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.

<a id="section-3-3"></a>

## 3.3. Configure opsDNS backup

This topic describes how to configure a backup policy for opsDNS.

**Prerequisites**

A backup archive storage is created. For more information, see .

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Config**.

3. Click the **opsDns** tab.

4. Configure the backup policy. The following table describes the parameters.

   **Section**

   **Parameter**

   **Description**

   Select the backup archive storage created

   **Archive Storage**

   in advance from the drop-down list.

   **Storage Settings**

   Specify the number of days to retain the

   **Retention**

   backup archive data. Enter a positive

   **Period (Days)**

   integer.

   **Backup Start At**

   Select the time when the backup starts.

   - **Daily Backup**: The backup is performed every few days.

   **Cycle Type**

   - **Hourly Backup**: The backup is performed every few hours, such as every hour or every four hours.

   **Backup Policy**

   Specify the interval between two

   **Interval**

   consecutive backups. Enter a positive integer.

5. Click **Save**.

<a id="section-3-4"></a>

## 3.4. Configure DNS product backup

This topic describes how to configure a backup policy for the DNS product.

**Prerequisites**

A backup archive storage is created. For more information, see .

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Config**.

3. Click the **DNS Product Backup** tab.

4. Configure the backup policy. The following table describes the parameters.

   **Section**

   **Parameter**

   **Description**

   Select the backup archive storage created

   **Archive Storage**

   in advance from the drop-down list.

   Specify the number of days to retain the

   **Retention**

   backup archive data. Enter a positive

   **Period (Days)**

   integer.

   **Storage Settings**

   **Backup Start At**

   Select the time when the backup starts.

   <table>
     <tr>
       <td rowspan="2">Backup Policy</td>
       <td>Cycle Type</td>
       <td>• <strong>Daily Backup</strong>: The backup is performed every few days.<br>• <strong>Hourly Backup</strong>: The backup is performed every few hours, such as every hour or every four hours.</td>
     </tr>
     <tr>
       <td>Interval</td>
       <td>Specify the interval between two consecutive backups. Enter a positive integer.</td>
     </tr>
   </table>

5. Click **Save**.

<a id="section-3-5"></a>

## 3.5. Configure in-cloud OSS bucket backup

This topic describes how to configure a backup policy for in-cloud Object Storage Service (OSS) buckets.

**Prerequisites**

A backup archive storage is created. For more information, see .

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Config**.

3. Click the **In-cloud OSS Bucket Backup** tab.

4. Configure the backup policy. The following table describes the parameters.

   > **Note**
   >
   > The preset backup policy is used. You need to only specify storage settings.

   | Parameter | Description |
   | --- | --- |
   | Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
   | Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.

<a id="section-4"></a>

# 4.View platform backup archiving records

This topic describes how to view the archive details after the backup is archived.

**Prerequisites**

Platform backup is archived.

**Procedure**

1. Go to the platform backup management page. For more information, see .

2. In the left-side navigation pane, choose **Platform Backup Management > Platform Backup Records**.

3. On the Archiving Details page, view the backup archive details.

   > **Note**
   >
   > Archive details are not displayed one week after the backup is deleted.
