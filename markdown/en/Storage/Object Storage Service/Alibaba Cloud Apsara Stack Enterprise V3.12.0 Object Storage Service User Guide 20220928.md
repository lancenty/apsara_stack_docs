Alibaba Cloud  
Apsara Stack Enterprise  
Object Storage Service  
User Guide  
Product Version: V3.12.0  
Document Version: 20220928

**Table of Contents**

- [1.What is OSS?](#section-1)
- [2.Usage notes](#section-2)
- [3.Quick start](#section-3)
    - [3.1. Log on to the OSS console](#section-3-1)
    - [3.2. Create buckets](#section-3-2)
    - [3.3. Upload objects](#section-3-3)
    - [3.4. Obtain object URLs](#section-3-4)
- [4.Buckets](#section-4)
    - [4.1. View bucket information](#section-4-1)
    - [4.2. Delete buckets](#section-4-2)
    - [4.3. Modify bucket ACLs](#section-4-3)
    - [4.4. Configure static website hosting](#section-4-4)
    - [4.5. Configure hotlink protection](#section-4-5)
    - [4.6. Configure logging](#section-4-6)
    - [4.7. Configure CORS](#section-4-7)
    - [4.8. Manage lifecycle rules](#section-4-8)
    - [4.9. Configure storage quota](#section-4-9)
    - [4.10. Configure cluster-disaster recovery](#section-4-10)
    - [4.11. Configure CRR](#section-4-11)
    - [4.12. Access OSS through custom domain names](#section-4-12)
- [5.Objects](#section-5)
    - [5.1. Search for objects](#section-5-1)
    - [5.2. Configure object ACL](#section-5-2)
    - [5.3. Create folders](#section-5-3)
    - [5.4. Delete objects](#section-5-4)
    - [5.5. Manage parts](#section-5-5)

<a id="section-1"></a>

# 1.What is OSS?

Object Storage Service (OSS) is a secure, cost-effective, and highly reliable cloud storage service provided by Alibaba Cloud. It enables you to store a large amount of data in the cloud.

OSS is an immediately available storage solution that has unlimited storage capacity. Compared with user-created server storage, OSS has outstanding advantages in reliability, security, cost-effectiveness, and data processing capabilities. OSS enables you to store and retrieve a variety of unstructured data objects, such as texts, images, audios, and videos over the network at any time.

OSS is an object storage service based on key-value pairs. Files uploaded to OSS are stored as objects in buckets. You can obtain the content of an object based on the object key.

In OSS, you can:

- Create a bucket and upload objects to the bucket.

- Obtain an object URL from OSS to share or download the object.

- Modify the attributes or metadata of a bucket or an object, and configure ACL for the bucket or the object.

- Perform basic and advanced operations in the OSS console.

- Perform basic and advanced operations by using SDKs or calling RESTful API operations in your application.

<a id="section-2"></a>

# 2.Usage notes

Before you use OSS, you must understand the following content:

To allow other users to use all or part of OSS features, you must create RAM users and grant permissions to the users by configuring RAM policies.

Before you use OSS, you must also understand the following limits.

| Item | Limit |
| --- | --- |
| Bucket | • You can create up to 100 buckets.<br>• After a bucket is created, its name and region cannot be modified. |
| Upload objects | • Objects larger than 5 GB cannot be uploaded by using the following modes: console upload, simple upload, form upload, or append upload. To upload an object that is larger than 5 GB, you must use multipart upload. The size of an object uploaded by using multipart upload cannot exceed 48.8 TB.<br>• If you upload an object that has the same name of an existing object in OSS, the new object will overwrite the existing object. |
| Delete objects | • Deleted objects cannot be recovered.<br>• You can delete up to 100 objects at a time in the OSS console.To delete more than 100 objects at a time, you must call an API operation or use an SDK. |
| Lifecycle | You can configure up to 1,000 lifecycle rules for each bucket. |

<a id="section-3"></a>

# 3.Quick start

<a id="section-3-1"></a>

## 3.1. Log on to the OSS console

This topic describes how to log on to the OSS console.

Prerequisites

- Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff.

- A browser is available. We recommend that you use the Google Chrome browser.

Procedure

1. In the address bar, enter the URL used to access the ASCM console. Press Enter.

2. Enter your username and password.

   Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

   Note

   The first time that you log on to the Apsara Uni-manager Management Console,

   you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:

   - Uppercase or lowercase letters

   - Digits

   - Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Login to go to the ASCM console homepage.

4. In the top navigation bar, choose Products > Object Storage Service.

<a id="section-3-2"></a>

## 3.2. Create buckets

Objects uploaded to OSS are stored in a bucket. Create a Bucket before you upload any objects to OSS.

Context

The attributes of a bucket include the region, ACL, and other metadata.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click Create Bucket if no buckets are available. In the Create OSS Bucket dialog box that appears, configure parameters.

   Note

   In the left-side navigation pane, click the + icon next to Buckets if buckets exist.

   The Create OSS Bucket dialog box appears.

   The following table describes the parameters used to create a bucket.

   Parameters

   | Parameter | Description |
   | --- | --- |
   | Organization | Select an organization from the drop-down list for the bucket. |
   | Resource Set | Select a resource set from the drop-down list for the bucket. |
   | Region | Select a region from the drop-down list for the bucket.<br>Note<br>• The region of a bucket cannot be changed after the bucket is created.<br>• If you want to access OSS from your ECS instance over the internal network, select the region where your ECS instance is deployed. |
   | Cluster | Select a cluster for the bucket. Two OSS clusters can be deployed in Apsara Stack. |
   | Bucket Name | Enter the name of the bucket.<br>Note<br>• The bucket name must comply with the naming conventions.<br>• The bucket name must be globally unique among all the existing buckets in Alibaba Cloud OSS.<br>• The bucket name cannot be changed after the bucket is created. |
   | Storage Class | Currently, only Standard buckets are supported. |
   | Capacity | Set the capacity of the bucket:<br>• Unlimited: The capacity is unlimited.<br>• Custom: Select this option to set the capacity of the bucket. Valid values: 0 to 2000000. Unit: TB. |
   | Access Control List (ACL) | Set the ACL of the bucket. The following options are available:<br>• Private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access objects in the bucket without authorization.<br>• Public Read: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users can only read objects in the bucket.<br>• Public Read/Write: Any users, including anonymous users can read and write objects in the bucket. Fees incurred by such operations are paid by the owner of the bucket. Exercise caution when you configure this option.<br>Note After a bucket is created, you can modify its ACL. For more information, see Modify bucket ACLs. |
   | Server-side Encryption | Configure server-side encryption:<br>• No: Server-side encryption is not performed.<br>• AES256: OSS server-side encryption uses AES256 to encrypt each object in the bucket with a different data key. CMKs used to encrypt data keys are rotated regularly.<br>• SM4: OSS server-side encryption uses SM4 to encrypt each object in the bucket with a different data key. CMKs used to encrypt data keys are rotated regularly. |

3. Click Submit.

<a id="section-3-3"></a>

## 3.3. Upload objects

After you create a bucket, you can upload objects to it.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

You can upload an object of any format to a bucket. You can use the OSS console to upload an object up to 5 GB in size. To upload an object larger than 5 GB, use an SDK or call an API operation.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to which you want to upload objects to go to the bucket details page.

3. Click the Files tab.

4. Click Upload. The Upload dialog box appears.

5. In the Upload To section, set the directory to which the object will be uploaded.

   - Current: Objects are uploaded to the current folder.

   - Specified: Objects are uploaded to the specified folder. OSS creates the specified folder automatically and uploads the object to it.

     Note

     For more information about folders, see Create folders.

6. In the File ACL section, select the ACL of the object to upload. By default, an object inherits the ACL of the bucket to which it belongs.

7. Drag and drop one or more objects to upload to the Upload field, or click Upload to select one or more objects to upload.

   Note

   - If the uploaded object has the same name as an existing object in the bucket, the existing object will be overwritten.

   - During object upload, do not refresh or close the page. Otherwise, the upload queue will be interrupted and cleared.

   - The name of the uploaded object must comply with the following conventions:

     - The name can contain only UTF-8 characters.

     - The name is case-sensitive.

     - The name must be 1 to 1,023 bytes in length.

     - The name cannot start with a forward slash (/) or backslash (\\).

8. After the object is uploaded, refresh the Files tab to view the uploaded object.

<a id="section-3-4"></a>

## 3.4. Obtain object URLs

You can obtain the URL of an object uploaded to a bucket. This URL can be used to share or download the object.

Prerequisites

- A bucket is created. For more information about how to create a bucket, see Create buckets.

- Objects are uploaded to the bucket. For more information about how to upload objects, see Upload objects.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket that stores the target object to go to the bucket details page.

3. Click the Files tab. The list of objects appears.

4. Click the name of the target object. In the Preview dialog box that appears, click Copy File URL under the URL field. You can also choose More > Copy File URL in the Actions column corresponding to the object. In the dialog box that appears, click Copy.

   You can send the URL to other users so that they can view or download the object.

<a id="section-4"></a>

# 4.Buckets

<a id="section-4-1"></a>

## 4.1. View bucket information

You can view the details of created buckets in the OSS console.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the target bucket.

3. On the bucket details page that appears, click the Overview tab. View the bucket domain names and basic settings.

<a id="section-4-2"></a>

## 4.2. Delete buckets

You can delete buckets in the OSS console.

Prerequisites

All objects and parts stored in the bucket are deleted. For more information about how to delete objects and parts, see Delete objects and Manage parts.

Warning

Deleted objects, parts, and buckets cannot be recovered. Exercise caution when

you delete objects, parts, and buckets.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of a bucket to go to the bucket details page.

3. On the bucket details page that appears, click Delete Bucket in the upper right corner. In the message that appears, click OK.

<a id="section-4-3"></a>

## 4.3. Modify bucket ACLs

You can modify the access control list (ACL) of a bucket in the OSS console to control access to the bucket.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

OSS provides ACL to control access to buckets. By default, the ACL of a bucket is private when you create the bucket. You can modify the ACL of a bucket after the bucket is created.

OSS provides ACL for buckets. The following ACLs are available for a bucket:

- Private: Only the owner or authorized users of the bucket can read and write the object.

- Public read: Only the owner or authorized users of this bucket can write the object. Other users, including anonymous users can only read the object.

- Public read/write: Any users, including anonymous users can read and write the object. Fees incurred by such operations are paid by the owner of the bucket. Exercise caution when you configure this option.

  Warning

  If you set ACL to public read or public read/write, other users can directly read the

  data in the bucket without authentication, resulting in security risks. For data security reasons, we recommend that you set the bucket ACL to private.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket for which you want to modify ACL to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Access Control List (ACL) section.

4. Click Configure. Modify the bucket ACL.

5. Click Save.

<a id="section-4-4"></a>

## 4.4. Configure static website hosting

You can configure static website hosting in the OSS console so that users can access the static website by using the bucket domain name.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

Static website hosting is not enabled if the default pages are not specified.

After the default homepage is configured, the default homepage is displayed if you access the root domain name of the static website or any URL that ends with a forward slash (/) under this domain name.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of a bucket to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Static Pages section.

4. Click Configure. Configure the following parameters:

   - Default Homepage: Specify the name of the index document that links to the index page. The index page functions similar to index.html. Only HTML objects in the root folder can be used. The default homepage is disabled if you do not specify this parameter.

   - Default 404 Page: Specify the name of the error document that links to the error page displayed when the requested resource does not exist. Only HTML, JPG, PNG, BMP, or WebP objects in the root folder can be used. Default 404 Page is disabled if you do not specify this parameter.

5. Click Save.

<a id="section-4-5"></a>

## 4.5. Configure hotlink protection

You can configure hotlink protection for a bucket in the OSS console to prevent unauthorized domain names from accessing the data in your bucket.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

OSS provides hotlink protection to prevent other domain names from accessing your data in OSS. You can configure the Referer field in the HTTP header to implement hotlink protection. You can configure a Referer whitelist for a bucket and configure whether to allow access requests that have an empty Referer field in the OSS console. For example, you can add  `http://www.aliyun.com`  to the Referer whitelist for a bucket named *oss-example*. Then, requests whose Referer field is set to `http://www.aliyun.com`  can access the objects in the *oss-example* bucket.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Hotlink Protection section.

4. Click Configure. Configure the following parameters:

   - Referer Whitelist: Add URLs to the whitelist. Referers are typically in URL format. Separate multiple Referers with break lines. You can use question marks (?) and asterisks (\*) as wildcard characters.

   - Allow Empty Referer: Specify whether to allow requests whose Referer field is empty. If you do not allow empty Referers, only HTTP or HTTPS requests which include the corresponding Referer field value can access the objects in the bucket.

5. Click Save.

<a id="section-4-6"></a>

## 4.6. Configure logging

You can enable or disable bucket logging in the OSS console.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

You can store access logs in the current bucket or in a new bucket.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to go to the bucket details page.

3. On the bucket details page that appears, click the Basic Settings tab. Find the Logging section.

4. Click Configure. Turn on Logging. Select Destination Bucket and set Log Prefix.

   - Destination Bucket: Select the name of the bucket in which access logs are to be stored from the drop-down list. You must be the owner of the selected bucket and the bucket must be in the same region as the bucket for which logging is enabled.

   - Log Prefix: Enter the prefix and folder where the access logs are stored. If you specify *log/&lt;Tar getPrefix>*, the access logs are stored in the *log/* directory.

5. Click Save.

<a id="section-4-7"></a>

## 4.7. Configure CORS

You can configure cross-origin resource sharing (CORS) in the OSS console to enable cross-origin access.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

OSS provides CORS over HTML5 to implement cross-origin access. When OSS receives a cross-origin request (or an OPTIONS request) for a bucket, OSS reads the CORS rules of the bucket and checks the relevant permissions. OSS matches the rules one by one. When OSS finds the first match, OSS returns a corresponding header. If no match is found, OSS does not include any CORS header in the response.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Cross-Origin Resource Sharing (CORS) section. Click Configure.

4. Click Create Rule. In the Create Rule dialog box that appears, configure the following parameters.

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Sources | Yes | Specifies the sources from which you want to allow cross-origin requests. You can configure multiple origins and separate them with break lines. Each origin can contain only one asterisk (\*) wildcard. If Sources is set to asterisk (\*), all cross-origin requests are allowed. |
   | Allowed Methods | Yes | Specifies the cross-origin request methods that are allowed. |
   | Allowed Headers | No | Specifies the allowed headers in a cross-origin request. Allowed headers are case-insensitive.You can configure multiple headers and separate them with break lines. Each allowed header can contain only one asterisk (\*) wildcard. Set this parameter to an asterisk (\*) if there are no special requirements. |
   | Exposed Headers | No | Specifies the list of headers that can be exposed to the browser. The headers are the response headers that allow access from an application such as XMLHttpRequest in JavaScript. No asterisk (\*) wildcards are allowed. |
   | Cache Timeout (Seconds) | No | Specifies the time the browser can cache the response to a preflight (OPTIONS) request to a specific resource. |

   Note

   You can configure up to 10 rules for each bucket.

5. Click OK.

<a id="section-4-8"></a>

## 4.8. Manage lifecycle rules

You can define and manage lifecycle rules for a bucket in the OSS console.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

You can define a rule for a full set or a subset by specifying the prefix keyword of objects in a bucket. A rule applies to all objects that match the rule. You can manage lifecycle rules to perform operations, such as object management and automatic part deletion.

Notice

- If an object matches a rule, data of the object is deleted within two days from the effective date.

- Data that is deleted based on a lifecycle rule cannot be recovered. Configure a rule only when necessary.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to go to the bucket details page.

3. Click the Basic Settings tab. Find the Lifecycle section. Click Configure.

4. Click Create Rule. In the Create Rule dialog box that appears, configure the following parameters:

   - Status: Configure the status of the rule: Enabled or Disabled.

   - Applied To: You can select Files with Specified Prefix or Whole Bucket. Files with Specified Prefix indicates that this rule applies to objects whose names contain a specified prefix. Whole Bucket indicates that this rule applies to all objects in the bucket.

     Note

     If you select Files with Specified Prefix, you can configure multiple lifecycle

     rules that have different prefixing configurations for objects. If you select Whole Bucket, only one lifecycle rule can be configured. In addition, if you have created a rule that has Files with Specified Prefix configured, you cannot create another rule that has Whole Bucket configured for the same bucket.

   - Prefix: If you set Applied To to Files with Specified Prefix, you must enter the prefix of the objects to which to apply the rule. If you want to match objects whose names start with img, enter *img*.

   - File Lifecycle: Configure operations to perform on expired objects. You can select Validity Period (Days), Expiration Date, or Disabled.

     - Validity Period (Days): Specify the number of days within which parts can be retained after they are last modified. After the validity period, expired parts are deleted. If you set Validity Period (Days) to 30, objects that are last modified on January 1, 2016 are scanned for by the backend application and deleted on January 31, 2016.

     - Expiration Date: Specify the date before which parts that are last modified expire and the operation to perform on these parts after they expire. If you select Delete and set Expiration Date to 2012-12-21, the backend application scans for objects that are last modified before December 21, 2012 and delete those objects.

     - Disabled: The automatic object deletion function is not enabled.

   - Delete: If you select Validity Period (Days) or Expiration Date for File Lifecycle, you can select Delete to delete objects based on the validity period or expiration time. If you select Disabled, the rule becomes invalid.

   - Part Lifecycle: Configure the delete operation to perform on expired parts. You can select Validity Period (Days), Expiration Date, or Disabled.

     - Validity Period (Days): Specify the number of days within which parts can be retained after they are last modified. After the validity period, expired parts are deleted. If you set Validity Period (Days) to 30, the backend application scans for parts that are last modified before January 1, 2016 and deletes them on January 31, 2016.

     - Expiration Date: Specify the date before which parts that are last modified expire and the operation to perform on these parts after they expire. If you set Expiration Date to 2012-12-21, parts that are last modified before this date are scanned for and deleted by the backend application.

     - Disabled: The automatic part deletion function is not enabled.

   - Delete: If you select Validity Period (Days) or Expiration Date for Part Lifecycle, you can select Delete to delete parts based on the validity period or expiration time. If you select Disabled, the rule becomes invalid.

     Notice

     In each lifecycle rule, you must configure at least object lifecycle or part lifecycle.

     In other words, you must select Delete or configure conversion actions for object lifecycle or select Delete for part lifecycle.

5. Click OK.

<a id="section-4-9"></a>

## 4.9. Configure storage quota

You can specify the storage quota of a bucket in the OSS console to limit the bucket size. You can specify the storage quota of a bucket when you create the bucket. You can also configure the storage quota of a created bucket. This topic describes how to configure the storage quota of a created bucket.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

After a storage quota is configured for a bucket, if the bucket size exceeds the quota, write operations, including PutObject, MultipartUpload, CopyObject, PostObject, AppendObject, cannot be performed on the bucket. Before configuring the quota of a bucket, ensure that it does not affect your business.

Notice

In general, OSS takes one hour to determine whether the bucket size exceeds the

quota. In some cases, more than one hour is required for OSS to detect that the bucket size exceeds the quota.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket for which you want to configure storage quota to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Storage Quota section.

4. Click Configure. Turn on Storage Quota and set the Storage Quota value.

   - Units: TB or GB.

   - Valid values: -1 to 2000000

   The default value is -1, indicating that the bucket size is not limited.

5. Click Save.

<a id="section-4-10"></a>

## 4.10. Configure cluster-disaster recovery

In cluster-disaster recovery mode, buckets with the same name are replicated. Cluster-based disaster recovery is automatically enabled based on configurations made when the cluster is created. In other words, after a primary bucket is created, a secondary bucket with the same name is automatically created. Information stored in the primary bucket is automatically synchronized to the secondary bucket. By default, this function is enabled.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of a bucket for which you want to configure cluster-disaster recovery to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Cluster-disaster Recovery section.

4. Click Configure. Turn on or turn off Cluster-disaster Recovery.

5. Click Save.

<a id="section-4-11"></a>

## 4.11. Configure CRR

Cross-region replication (CRR) enables the automatic and asynchronous (near real-time) replication of objects across buckets in different OSS regions. Operations such as the creation, overwriting, and deletion of objects can be synchronized from the source bucket to the destination bucket.

Prerequisites

The steps described in Create buckets are performed or a bucket is created in the region.

Context

This feature meets the requirements of geo-disaster recovery or data replication. Objects in the destination bucket are extra replicas of objects in the source bucket. They have the same object names, object content, and object metadata such as the creation time, owner, user metadata, and object ACL.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of a bucket for which you want to configure CRR to go to the bucket details page.

3. On the bucket details page, click the Basic Settings tab. Find the Cross-Region Replication section.

4. Click Enable. In the Cross-Region Replication dialog box that appears, configure the parameters described in the following table.

   | Parameter | Description |
   | --- | --- |
   | Source Region | The region where the current bucket is located. |
   | Source Bucket | The name of the current bucket. |
   | Destination Region | Select the region where the destination bucket is located. The source and destination buckets for CRR must be located in different regions. Data cannot be synchronized between buckets located within the same region. |
   | Destination Bucket | Select the destination bucket. The two buckets with CRR enabled cannot synchronize data with other buckets. If you synchronize data from Bucket A to Bucket B, neither Bucket A nor Bucket B can synchronize data with other buckets. |
   | Applied To | Select the source data to synchronize.<br>• All Files in Source Bucket: synchronizes all objects from the source bucket to the destination bucket.<br>• Files with Specified Prefix: synchronizes the objects whose names contain the specified prefix from the source bucket to the destination bucket. For example, if you have a folder named <em>management/</em> in the root folder of a bucket and a subfolder named <em>abc/</em> in <em>management/</em>, when you want to synchronize objects in the <em>abc/</em> subfolder, enter <em>management/abc/</em>as the prefix. You can specify up to five prefixes. |
   | Operations | Select the synchronization policy.<br>• Add/Change: synchronizes only added or changed data from the source bucket to the destination bucket.<br>• Add/Delete/Change: synchronizes all data changes such as the creation, overwriting, and deletion of objects from the source bucket to the destination bucket. |
   | Replicate Historical Data | Specify whether to synchronize historical data before you enable CRR.<br>• Yes: synchronizes historical data to the destination bucket.<br>Notice When historical data is synchronized, objects in the source bucket may overwrite objects in the destination bucket if these objects have the same name. Before you select this option, ensure that the data is consistent.<br>• No: synchronizes only objects that you want to upload or update after CRR is enabled to the destination bucket. |

5. Click OK.

   Note

   - After the configuration is complete, it may take three to five minutes for CRR to take effect. Synchronization information is displayed after the source bucket is synchronized.

   - In CRR, data is asynchronously (near real-time) replicated. It takes several minutes to several hours for the data to be replicated to the destination bucket based on the amount of data.

<a id="section-4-12"></a>

## 4.12. Access OSS through custom domain names

You can bind a custom domain name to your bucket and add a CNAME record that points to the public endpoint of your bucket. After the CNAME record is added, you are directed to your bucket when you access the custom domain name.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Step 1: Bind the custom domain name to the bucket

You can use OSS SDK for Java to bind the custom name to the bucket. For the sample code, visit Bind custom domain name.

Step 2: Configure the CNAME record

The domain name of Alibaba Cloud is used as an example to show how to configure the CNAME record.

1. Log on to the DNS console.

2. On the Manage DNS page, click Configure in the Actions column corresponding to the target domain name.

3. On the DNS Settings page, click Add Record. In the Add Record dialog box, configure parameters listed in the following table.

   | Parameter | Description |
   | --- | --- |
   | Type | Select the type of the record to direct requests.<br>In this example, select <em>CNAME</em>. |
   | Host | Enter the host record based on the prefix of the domain name.Examples:<br>• If the domain name is www.aliyun.com, enter www.<br>• If the domain name is aliyun.com, enter @.<br>• If the domain name is abc.aliyun.com, enter abc.<br>• If the domain is a second-level domain such as a.aliyun.com or b.aliyun.com, enter an asterisk (\*). |
   | ISP Line | Select the ISP line used to resolve the domain name.<br>We recommend that you select <em>Default</em> to allow the system to select the optimal line. |
   | Value | Enter the value of the record based on the selected record type.<br>In this example, enter the public endpoint of the bucket. |
   | TTL | Select the update interval of the record. In this example, select the default value. |

4. Click OK.

   Note

   A new CNAME record takes effect immediately. It takes up to 72 hours for the

   modified CNAME record to take effect.

Verify CNAME status

After a CNAME record is configured, the period required for the record to take effect varies with different DNS providers. You can run the ping or lookup command to access the added domain name. If the access is directed to the bucket endpoint, the CNAME configuration has taken effect.

<a id="section-5"></a>

# 5.Objects

<a id="section-5-1"></a>

## 5.1. Search for objects

You can search buckets or folders for objects whose names contain a specified prefix in the OSS console.

Prerequisites

- A bucket is created. For more information about how to create a bucket, see Create buckets.

- Objects are uploaded to the bucket. For more information about how to upload objects, see Upload objects.

Context

When you search for objects based on a prefix, search strings are case-sensitive and cannot contain forward slashes (/). The search range is limited to the root directory of the current bucket or the objects in the current folder (excluding subfolders and the objects in them).

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the bucket to go to the bucket details page.

3. Click the Files tab.

4. On the right side of the Files tab, enter the prefix to search in the search box and press Enter or click the search icon to search for related objects.

   The names of the objects and folders that are stored in the current folder and match the prefix are listed.

   Note

   To search for objects in a specified folder, open the folder and enter the prefix in

   the search box. The names of objects and subfolders in the folder that match the prefix are listed.

<a id="section-5-2"></a>

## 5.2. Configure object ACL

You can configure the ACL of an object in the OSS console to control access to the object.

Prerequisites

- A bucket is created. For more information about how to create a bucket, see Create buckets.

- Objects are uploaded to the bucket. For more information about how to upload objects, see Upload objects.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the target bucket to go to the bucket details page.

3. Click the Files tab.

4. On the Files tab, click the name of the target object. The Preview dialog box appears.

5. Click Set ACL on the right side of File ACL. The Set ACL dialog box appears.

   The ACLs that you can select are described as follows:

   - Inherited from Bucket: The ACL of each object is the same as that of the bucket.

   - Private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization.

   - Public Read: Only the owner or authorized users of this bucket can write objects in the bucket. Other users, including anonymous users can only read objects in the bucket.

   - Public Read/Write: Any users, including anonymous users can read and write objects in the bucket. Fees incurred by such operations are paid by the owner of the bucket. Configure this option only when necessary.

     Note

     You can also choose More > Set ACL in the Actions column corresponding to the

     target object to open the Set ACL dialog box.

6. Click OK.

<a id="section-5-3"></a>

## 5.3. Create folders

You can create a folder in a bucket in the OSS console.

Prerequisites

A bucket is created. For more information about how to create a bucket, see Create buckets.

Context

OSS does not use traditional folders. All elements are stored as objects. A folder is an object whose size is 0 and has a name that ends with a forward slash (/). A folder is used to sort objects of the same type and process them at a time. The OSS console displays objects that end with a forward slash (/) as folders. These objects can be uploaded and downloaded. You can use OSS folders in the OSS console the way you use folders in Windows.

Note

The OSS console displays any objects whose names end with a forward slash (/) as

folders, regardless of whether these objects contain data. You can download these objects only by calling an API operation or by using an SDK.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the target bucket to go to the bucket details page.

3. Click the Files tab. On the page that appears, click Create Folder.

4. In the Create Folder dialog box that appears, enter the folder name.

   The folder name must comply with the following conventions:

   - ThenamecancontainonlyUTF-8charactersThenamecannotcontainemojis

   - The name can contain only UTF8 characters. The name cannot contain emojis.

   - The name cannot start with a forward slash (/) or backslash (\\). The name cannot contain consecutive forward slashes (/). You can use forward slashes (/) in a folder name to quickly create a subfolder.

   - A subfolder cannot contain two consecutive periods (*..*) in its name.

   - The folder name must be 1 to 254 characters in length.

5. Click OK.

<a id="section-5-4"></a>

## 5.4. Delete objects

You can delete uploaded objects in the OSS console.

Context

You can delete one or more objects at a time. A maximum of 100 objects can be deleted at a time. You can use SDKs or call an API operation to delete a specific object or more than 100 objects.

Notice

Deleted objects cannot be recovered. Exercise caution when you delete objects.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the target bucket to go to the bucket details page.

3. Click the Files tab.

4. Select one or multiple objects that you want to delete in the object list, and choose Batch Operation > Delete.

   You can also choose More > Delete in the Actions column corresponding to the target object.

5. In the message that appears, click OK.

<a id="section-5-5"></a>

## 5.5. Manage parts

When you upload an object in multipart upload mode, the object is split into several smaller parts. After all of the parts are uploaded to the OSS server, you can call CompleteMultipartUpload to combine them into a complete object. We recommend that you delete unnecessary parts on a regular basis.

Context

Parts are generated in multipart upload tasks and cannot be read until they are combined into a complete object. To save storage space in the bucket, you can configure lifecycle rules to manage unnecessary parts that are generated when multipart upload tasks fail. For more information, see Manage lifecycle rules.

Procedure

1. Log on to the OSS console.

2. In the left-side navigation pane, click the name of the target bucket to go to the bucket details page.

3. Click the Files tab. On the page that appears, click Parts.

4. In the Parts dialog box that appears, delete parts.

   - To delete all parts in the bucket, select all parts and click Delete All.

   - To delete specified parts, select the parts that you want to delete and click Delete.

5. In the message that appears, click OK.
