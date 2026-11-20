Alibaba Cloud  
Apsara Stack  
Database Backup  
Developer Guide  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.API reference](#section-1)
    - [1.1. List of operations by function](#section-1-1)
    - [1.2. Backup schedule](#section-1-2)
        - [1.2.1. CreateBackupPlan](#section-1-2-1)
        - [1.2.2. ConfigureBackupPlan](#section-1-2-2)
        - [1.2.3. DescribeBackupPlanList](#section-1-2-3)
        - [1.2.4. StartBackupPlan](#section-1-2-4)
        - [1.2.5. StopBackupPlan](#section-1-2-5)
        - [1.2.6. ModifyBackupObjects](#section-1-2-6)
        - [1.2.7. ModifyBackupSourceEndpoint](#section-1-2-7)
        - [1.2.8. ModifyBackupPlanName](#section-1-2-8)
        - [1.2.9. ModifyBackupStrategy](#section-1-2-9)
        - [1.2.10. DescribeRestoreRangeInfo](#section-1-2-10)
        - [1.2.11. DescribeBackupPlanBilling](#section-1-2-11)
    - [1.3. Backup task](#section-1-3)
        - [1.3.1. DescribeFullBackupList](#section-1-3-1)
        - [1.3.2. DescribeIncrementBackupList](#section-1-3-2)
    - [1.4. Restore task](#section-1-4)
        - [1.4.1. CreateRestoreTask](#section-1-4-1)
        - [1.4.2. StartRestoreTask](#section-1-4-2)
        - [1.4.3. DescribeRestoreTaskList](#section-1-4-3)
    - [1.5. Backup gateway](#section-1-5)
        - [1.5.1. DescribeBackupGatewayList](#section-1-5-1)
    - [1.6. Backup set download](#section-1-6)
        - [1.6.1. DescribeBackupSetDownloadTaskList](#section-1-6-1)
        - [1.6.2. Configures download rules for backup sets.](#section-1-6-2)
        - [1.6.3. CreateFullBackupSetDownload](#section-1-6-3)
        - [1.6.4. CreateIncrementBackupSetDownload](#section-1-6-4)
    - [1.7. Others](#section-1-7)
        - [1.7.1. Queries the standard error information of a DBS task.](#section-1-7-1)
        - [1.7.2. DescribeNodeCidrList](#section-1-7-2)
        - [1.7.3. DescribePreCheckProgressList](#section-1-7-3)
        - [1.7.4. PhysicalDeleteResource](#section-1-7-4)
        - [1.7.5. LogicalDeleteResource](#section-1-7-5)
        - [1.7.6. DescribeOssStsToken](#section-1-7-6)
        - [1.7.7. DescribeBackupInstances](#section-1-7-7)
        - [1.7.8. ConfigureDuplicaitonBackupPlan](#section-1-7-8)
        - [1.7.9. CheckResource](#section-1-7-9)
- [2.SDK reference](#section-2)
    - [2.1. SDK overview](#section-2-1)
    - [2.2. Use DBS SDK for Java based on Maven dependencies](#section-2-2)
    - [2.3. Obtains an AccessKey pair](#section-2-3)

<a id="section-1"></a>

# 1.API reference

<a id="section-1-1"></a>

## 1.1. List of operations by function

The following tables list the API operations that are available for use in Database Backup (DBS).

**Backup schedule**

| Operation | Description |
| --- | --- |
| CreateBackupPlan | Creates a backup schedule |
| ConfigureBackupPlan | Configures a backup schedule |
| StartBackupPlan | Starts a backup schedule |
| StopBackupPlan | Stops a backup schedule |
| DescribeBackupPlanList | Queries backup schedules |
| ModifyBackupObjects | Modifies backup objects |
| ModifyBackupSourceEndpoint | Modifies the information about a backup source |
| ModifyBackupPlanName | Changes the name of a backup schedule |
| ModifyBackupStrategy | Modifies the backup time settings |
| DescribeRestoreRangeInfo | Queries the details of time ranges to which you can restore data |
| DescribeBackupPlanBilling | Queries the billing information of a backup schedule |

**Backup task**

| Operation | Description |
| --- | --- |
| DescribeFullBackupList | Queries full backup tasks |
| DescribeIncrementBackupList | Queries incremental backup tasks |

**Restore task**

| Operation | Description |
| --- | --- |
| CreateRestoreTask | Creates a restore task |
| StartRestoreTask | Starts a restore task |
| DescribeRestoreTaskList | Queries restore tasks |

**Backup gateway**

| Operation | Description |
| --- | --- |
| DescribeBackupGatewayList | Queries backup gateways |

**Backup set download**

| Operation | Description |
| --- | --- |
| DescribeBackupSetDownloadTa skList | Queries backup set download tasks |
| ModifyBackupSetDownloadRule s | Configures download rules for backup sets |
| CreateFullBackupSetDownload | Creates a full backup set download task |
| CreateIncrementBackupSetDow nload | Creates an incremental backup set download task |

**Others**

| Operation | Description |
| --- | --- |
| DescribeJobErrorCode | Queries the standard error information of a DBS task |
| DescribeNodeCidrList | Queries the CIDR blocks of nodes on which DBS is running |
| DescribePreCheckProgressList | Queries the precheck progress of items |

<a id="section-1-2"></a>

## 1.2. Backup schedule

<a id="section-1-2-1"></a>

### 1.2.1. CreateBackupPlan

Creates a backup schedule.

**Request header**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Region | Strin g | Quer y | No | cn-hangzhou | The region where Database Backup (DBS) is activated. |
| InstanceCl ass | Strin g | Quer y | Yes | micro | The specification of the backup schedule. Valid values:<br>• small<br>• large |
| DatabaseT ype | Strin g | Quer y | Yes | MySQL | The type of the database engine. Valid values:<br>• MySQL<br>• MSSQL<br>• Oracle<br>• MongoDB<br>• Redis |
| BackupMet hod | Strin g | Quer y | Yes | logical | The backup method of the backup schedule.Valid values:<br>• <strong>logical</strong>: logical backup<br>• <strong>physical</strong>: physical backup |
| Period | Strin g | Quer y | No | Month | Specifies whether to use yearly subscription or monthly subscription. |
| UsedTime | Integ er | Quer y | No | 1 | The subscription duration. |
| PayType | Strin g | Quer y | No | prepay | The billing method. If you call this operation in Apsara Stack, set the value to prepay. |
| DatabaseR egion | Strin g | Quer y | No | cn-hangzhou | The region where the database is deployed. |
| StorageRe gion | Strin g | Quer y | No | cn-hangzhou | The region where the data is stored. |
| InstanceTy pe | Strin g | Quer y | No | RDS | The type of the database instance. Valid values:<br>• RDS<br>• DDS<br>• Kvstore<br>• PolarDB<br>• <strong>Other</strong>: a database instance that is connected by using an IP address and a port number specified in the IP address:Port number format |
| StorageTy pe | Strin g | Quer y | No | None | This parameter is not publicly available. |
| FromApp | Strin g | Quer y | No | OpenAPI | The source of the request. The value is automatically set to OpenAPI and does not need to be changed.Default value: OpenAPI. |
| ClientToke n | Strin g | Quer y | No | KJSAHKJFHKJSHFKASHFKJ ADFHKD\*\*\*\* | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OwnerId | Strin g | Quer y | No | None | This parameter is not publicly available. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7BCF6D62-885F-5A4A-91A1-679760E7\*\*\*\* | The request ID. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| BackupPlanId | String | dbsrhahrsu2\*\*\*\* | The ID of the backup schedule. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| OrderId | String | 21437345592\*\*\*\* | The order ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: The operation is successful.<br>• <strong>false</strong>: The operation failed. |
| ErrCode | String | Param.NotFound | The error code. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateBackupPlan
&InstanceClass=micro
&DatabaseType=MySQL
&BackupMethod=logical
&<Common request parameters>
```

Sample success responses

`JSON`  format

```json
{
 "RequestId":"7BCF6D62-885F-5A4A-91A1-679760E7****",
 "HttpStatusCode":200,
 "BackupPlanId":"dbsrhahrsu2****",
 "ErrMessage":"The specified parameter %s value is not valid.",
 "OrderId":"21437345592****",
 "Success":true,
 "ErrCode":"Param.NotFound"
}
```

`XML`  format

```xml
<RequestId>7BCF6D62-885F-5A4A-91A1-679760E7****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbsrhahrsu2****</BackupPlanId>
<ErrMessage>The specified parameter %s value is not valid.</ErrMessage>
<OrderId>21437345592****</OrderId>
<Success>true</Success>
<ErrCode>Param.NotFound</ErrCode>
```

Dbs

2019-03-06

Creates a backup schedule

<a id="section-1-2-2"></a>

### 1.2.2. ConfigureBackupPlan

Configures a Database Backup (DBS) backup schedule.

**Usage notes**

> **Note**
>
> In most cases, if you initiate a request to configure a backup schedule, DBS requires approximately five seconds to respond to your request.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ConfigureBacku pPlan | The operation that you want to perform. Set the value to <strong>ConfigureBackupPlan</strong>. |
| BackupPlanId | String | Yes | dbstooi0\*\*\*\*\*\*\* | The ID of the backup schedule. |
| BackupPlanNam e | String | Yes | dbstooi0\*\*\*\*\*\*\* | The name of the backup schedule. |
| SourceEndpointI nstanceType | String | Yes | rds | The location of the database. Valid values:<br>• RDS<br>• ECS<br>• <strong>Express</strong>: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.<br>• <strong>Agent</strong>: The database is connected to DBS over a DBS backup gateway.<br>• <strong>DDS</strong>: The database is an ApsaraDB for MongoDB (MongoDB) database.<br>• <strong>Other</strong>: The database is connected to DBS by using the IP address and port of the database. |
| SourceEndpoint Region | String | No | cn-hangzhou | The ID of the region where the database is deployed.<br>Note<br>If you specify <strong>RDS</strong>, <strong>ECS</strong>, <strong>DDS</strong>, <strong>Express</strong>, or <strong>Agent</strong> as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointI nstanceID | String | No | rm-uf6wjk5xxxxxxx xxx | The ID of the database instance.<br>Note<br>If you specify <strong>RDS</strong>, <strong>ECS</strong>, <strong>DDS</strong>, or <strong>Express</strong> as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointI P | String | No | rm-uf6wjk5xxxxxxx.mysql.rds.aliyun cs.com | The endpoint of the database.<br>Note<br>If you specify <strong>Express</strong>, <strong>Agent</strong>, or <strong>Other</strong> as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointP ort | Integer | No | 3306 | The port of the database.<br>Note<br>If you specify <strong>ECS</strong>, <strong>Express</strong>, <strong>Agent</strong>, or <strong>Other</strong> as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpoint DatabaseName | String | No | testRds | The name of the database.<br>Note<br>If the database runs the <strong>PostgreSQL</strong> engine or <strong>MongoDB</strong> engine, you must specify this parameter. |
| SourceEndpoint UserName | String | No | testRds | The username of the database account.<br>Note<br>If the database runs the <strong>Redis</strong> engine or if the database is connected to DBS over a DBS backup gateway and runs the MSSQL engine, this parameter is optional. In other cases, you must specify this parameter. |
| SourceEndpointP assword | String | No | testPassword | The password of the database account.<br>Note<br>If the database runs the <strong>Redis</strong> engine or if the database is connected to DBS over a DBS backup gateway and runs the MSSQL engine, this parameter is optional. In other cases, you must specify this parameter. |
| BackupGatewayI d | Long | No | 23313123312 | The ID of the backup gateway.<br>Note<br>If you set the value of SourceEndpointInstanceType to <strong>Agent</strong>, you must specify this parameter. |
| OSSBucketName | String | No | TestOssBucket | The name of the Object Storage Service (OSS) bucket.<br>Note<br>By default, the system automatically generates a name for the OSS bucket. |
| BackupObjects | String | No | \[{"DBName":"Nam e of the database that you want to back up", "SchemaName": "Name of the schema that you want to back up", "TableIncludes": \[{"TableName":"N ame of the table that you want to back up" }\], "TableExcludes": \[{"TableName":" Name of the table that you want to exclude during the backup" }\] } \] | The objects that you want to back up. |
| BackupPeriod | String | No | Monday | The full backup cycle. Valid values:<br>• Monday<br>• Tuesday<br>• Wednesday<br>• Thursday<br>• Friday<br>• Saturday<br>• Sunday |
| BackupStartTim e | String | No | 14:22 | The start time of the full backup.Specify the value in the HH:mmZ format (UTC). |
| EnableBackupLo g | Boolean | No | true | Specifies whether to enable the incremental log backup feature. Valid values:<br>• true<br>• false |
| BackupRetentio nPeriod | Integer | No | 730 | The number of days for which the backup data is retained. Valid values: 0 to 1825. Default value: 730. |
| DuplicationInfre quentAccessPeri od | Integer | No | 180 | The number of days after which the storage class of the backup data is changed to <strong>Infrequent Access (IA)</strong>.Default value: 180. |
| DuplicationArchi vePeriod | Integer | No | 365 | The number of days after which the storage class of the backup data is changed to <strong>Archive</strong>. Default value: 365. |
| SourceEndpoint OracleSID | String | No | test | The system ID (SID) of the Oracle database. If the database runs the <strong>Oracle</strong> engine, you must specify this parameter. |
| BackupStorageT ype | String | No | system | The built-in storage type.<br>Note<br>If you deploy your business in Apsara Stack, use the default value <strong>system</strong>. The default value specifies that the system stores backup data in the built-in OSS buckets of DBS. |
| BackupSpeedLi mit | Long | No | 262144 | The I/O limit for the disk. Unit: KB/s. |
| BackupStrategy Type | String | No | simple | The full backup cycle. Valid values:<br>• <strong>simple</strong>: scheduled backup. If you specify this value as the value of <strong>BackupStrategyType</strong>, you must specify <strong>BackupPeriod</strong> and <strong>BackupStartTime</strong>.<br>• <strong>manual</strong>: manual backup. |
| CrossAliyunId | String | No | XXX | This parameter is not supported. |
| CrossRoleName | String | No | XXX | This parameter is not supported. |
| AutoStartBackup | Boolean | No | true | Specifies whether to enable the backup feature. |
| RegionId | String | No | cn-hangzhou | The ID of the region. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbstooi01ex\*\*\*\* | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | F1FB49D4-B504-47F1-9F43-D7EAB33F\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ConfigureBackupPlan
&BackupPlanId=dbstooi0*******
&BackupPlanName=dbstooi0*******
&SourceEndpointInstanceType=rds
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>F1FB49D4-B504-47F1-9F43-D7EAB33F****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbstooi01ex****</BackupPlanId>
<ErrMessage>The specified parameter %s value is not valid.</ErrMessage>
<Success>true</Success>
<ErrCode>Param.NotFound</ErrCode>
```

`JSON`  format

```json
{
    "RequestId": "F1FB49D4-B504-47F1-9F43-D7EAB33F****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbstooi01ex****",
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
}
```

<a id="section-1-2-3"></a>

### 1.2.3. DescribeBackupPlanList

Queries backup schedules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeBackup PlanList | The operation that you want to perform. Set the value to <strong>DescribeBackupPlanList</strong>. |
| BackupPlanId | String | No | dbstooi01ex\*\*\*\* | The ID of the backup schedule that you want to query. Separate multiple IDs with commas (,). |
| Region | String | No | cn-hangzhou | The region where DBS is activated.<br>Note<br>If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be an integer that is greater than or equal to 0. Default value: 0. |
| BackupPlanNam e | String | No | test123 | The name of the backup schedule. |
| BackupPlanStatu s | String | No | wait | The status of the backup schedule.Valid values:<br>• <strong>wait</strong>: The backup schedule is not configured.<br>• <strong>init</strong>: The backup schedule is not started and fails to pass the precheck.<br>• <strong>Running</strong>: The backup schedule is running.<br>• <strong>stop</strong>: The backup schedule failed.<br>• <strong>pause</strong>: The backup schedule is paused.<br>• <strong>locked</strong>: The backup schedule is locked.<br>• <strong>check_pass</strong>: The backup schedule passes the precheck. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ASDASDASDSAD ASFCZXVZ | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The response code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupPlanDe tail |  | The details of the backup schedules. |
| BackupPlanDe tail |  |  |  |
| BackupGatewa yId | Long | 827362187368736 | The ID of the backup gateway. |
| BackupMethod | String | logical | The method that is used to generate the backup set. Valid values:<br>• <strong>logical</strong>: logical backup<br>• <strong>physical</strong>: physical backup |
| BackupObjects | String | \[ {\\"DBName\\":\\"Nam e of the database that you want to back up\\", \\"SchemaName\\":\\" Name of the schema that you want to back up\\", \\"TableIncludes\\": \[{\\"TableName\\":\\"Na me of the table that you want to back up\\" }\], \\"TableExcludes\\": \[{\\"TableName\\":\\"Na me of the table that you want to exclude during the backup\\" }\] } \] | The objects that are backed up. |
| BackupPeriod | String | Monday | The full backup cycle. Valid values:<br>• Monday<br>• Tuesday<br>• Wednesday<br>• Thursday<br>• Friday<br>• Saturday<br>• Sunday |
| BackupPlanCr eateTime | Long | 1582527713000 | The time when the backup schedule was created. |
| BackupPlanId | String | dbstooi01e\*\*\*\* | The ID of the backup schedule. |
| BackupPlanNa me | String | test123 | The name of the backup schedule. |
| BackupPlanSta tus | String | init | The status of the backup schedule. Valid values:<br>• <strong>wait</strong>: The backup schedule is not configured.<br>• <strong>init</strong>: The backup schedule is not started and fails to pass the precheck.<br>• <strong>Running</strong>: The backup schedule is running.<br>• <strong>stop</strong>: The backup schedule failed.<br>• <strong>pause</strong>: The backup schedule is paused.<br>• <strong>locked</strong>: The backup schedule is locked.<br>• <strong>check_pass</strong>: The backup schedule passes the precheck. |
| BackupRetenti onPeriod | Integer | 365 | The number of days for which the backup data is retained. Valid values: 0 to 1825. |
| BackupSetDow nloadDir | String | \*/test/test123 | The server directory to which the backup set is downloaded. |
| BackupSetDow nloadFullDataF ormat | String | SQL | The format in which the full backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON |
| BackupSetDow nloadGatewayI d | Long | 123123 | The ID of the backup gateway that is used to download backup sets. |
| BackupSetDow nloadIncremen tDataFormat | String | SQL | The format in which the incremental backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON |
| BackupSetDow nloadTargetTy pe | String | agent | The type of the destination server to which the backup set is downloaded.<br>The value is <strong>agent</strong>, which indicates a server on which a backup gateway is installed. |
| BackupStartTi me | String | 14:22 | The start time of the full backup. The time is displayed in the<strong>_HH:mm_</strong> format.Example: <strong>_14:22_</strong>. |
| BackupStorag eType | String | simple | The day of each week when the full backup task runs. Valid values:<br>• <strong>simple</strong>: scheduled backup. If you set the value to <strong>simple</strong>, you must also specify <strong>BackupPeriod</strong> and <strong>BackupStartTime</strong>.<br>• <strong>manual</strong>: manual backup<br>Note<br>Default value: <strong>simple</strong>. |
| BeginTimesta mpForRestore | Long | 1554560477000 | The beginning of the time range during which the database can be restored. |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | This parameter is not supported. |
| CrossRoleNam e | String | test123 | This parameter is not supported. |
| DuplicationArc hivePeriod | Integer | 365 | The number of days after which the storage class of the backup data is changed to <strong>Archive</strong>. |
| DuplicationInfr equentAccess Period | Integer | 180 | The number of days after which the storage class of the backup data is changed to <strong>Infrequent Access (IA)</strong>. |
| EnableBackup Log | Boolean | true | Indicates whether incremental log backup is enabled. Valid values:<br>• true<br>• false |
| EndTimestamp ForRestore | Long | 1554560477000 | The end of the time range during which the database can be restored. |
| ErrMessage | String | can not connect to oracle instance orcl with user dbs | The error message returned about the precheck. |
| InstanceClass | String | micro | The specifications of the backup schedule.Valid values:<br>• micro<br>• small<br>• medium<br>• large |
| OSSBucketNa me | String | dbs-backup-1857XXXXX489 | The name of the Object Storage Service (OSS) bucket. |
| OSSBucketReg ion | String | cn-hangzhou | The region of the OSS bucket. |
| OpenBackupS etAutoDownlo ad | Boolean | true | Indicates whether the automatic backup set download feature is enabled. Valid values:<br>• true<br>• false |
| SourceEndpoin tDatabaseNam e | String | test | The name of the database. |
| SourceEndpoin tInstanceID | String | test | The ID of the database instance. |
| SourceEndpoin tInstanceType | String | RDS | The location of the database. Valid values:<br>• RDS<br>• ECS<br>• <strong>Express</strong>: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.<br>• <strong>Agent</strong>: The database is connected to DBS over a DBS backup gateway.<br>• <strong>DDS</strong>: The database is a MongoDB database.<br>• <strong>Other</strong>: The database is connected to DBS by using the IP address and port of the database. |
| SourceEndpoin tIpPort | String | 100.\*.\*.10:33204 | The endpoint of the database. |
| SourceEndpoin tOracleSID | String | test | The system ID (SID) of the Oracle database. |
| SourceEndpoin tRegion | String | cn-hangzhou | The ID of the region where the database is deployed. |
| SourceEndpoin tUserName | String | test | The username of the database account. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 4F1888AC-1138-4995-B9FE-D2734F61\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 100 | The total number of backup schedules. |
| TotalPages | Integer | 4 | The total number of pages returned. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanList
&BackupPlanId=dbstooi01ex****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<PageSize>30</PageSize>
<RequestId>4F1888AC-1138-4995-B9FE-D2734F61****</RequestId>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>1</TotalElements>
<Items>
    <BackupPlanDetail>
        <BackupPlanName>dbXXXXX7ltj</BackupPlanName>
        <BackupMethod>logical</BackupMethod>
        <BackupPlanCreateTime>1583000</BackupPlanCreateTime>
        <BackupPeriod>MONDAY</BackupPeriod>
        <BackupObjects>[     {         "DBName":"Name of the database that you want to b
ack up",         "SchemaName":"Name of the schema that you want to back up",         "Ta
bleIncludes":[{             "TableName":"Name of the table that you want to back up"    
}],         "TableExcludes":[{             "TableName":"Name of the table that you want 
to exclude during the backup"         }]     } ]</BackupObjects>
        <SourceEndpointInstanceID>rm-bp1p8XXXXXv8pxe</SourceEndpointInstanceID>
        <InstanceClass>medium</InstanceClass>
        <OSSBucketRegion>cn-hangzhou</OSSBucketRegion>
        <SourceEndpointRegion>cn-hangzhou</SourceEndpointRegion>
        <SourceEndpointIpPort>100.X.X.10:33204</SourceEndpointIpPort>
        <DuplicationArchivePeriod>365</DuplicationArchivePeriod>
        <OSSBucketName>dbs-backup-1857XXXXX489</OSSBucketName>
        <BackupPlanStatus>init</BackupPlanStatus>
        <BackupStartTime>14:22</BackupStartTime>
        <EnableBackupLog>true</EnableBackupLog>
        <BackupPlanId>dbXXXXXx7ltj</BackupPlanId>
        <BackupRetentionPeriod>730</BackupRetentionPeriod>
        <SourceEndpointInstanceType>RDS</SourceEndpointInstanceType>
        <SourceEndpointUserName>test</SourceEndpointUserName>
        <DuplicationInfrequentAccessPeriod>180</DuplicationInfrequentAccessPeriod>
    </BackupPlanDetail>
</Items>
<TotalPages>1</TotalPages>
<Success>true</Success>
```

`JSON`  format

```json
{
 "PageSize": 30,
 "RequestId": "4F1888AC-1138-4995-B9FE-D2734F61****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "Items": {
  "BackupPlanDetail": [
   {
    "BackupPlanName": "dbXXXXX7ltj",
    "BackupMethod": "logical",
    "BackupPlanCreateTime": 1583000,
    "BackupPeriod": "MONDAY",
    "BackupObjects": "[     {         \"DBName\":\"Name of the database that you want 
to back up\",         \"SchemaName\":\"Name of the schema that you want to back up\",  
\"TableIncludes\":[{             \"TableName\":\"Name of the table that you want to 
back up\"         }],         \"TableExcludes\":[{             \"TableName\":\"Name of t
he table that you want to exclude during the backup\"         }]     } ]",
    "SourceEndpointInstanceID": "rm-bp1p8XXXXXv8pxe",
    "InstanceClass": "medium",
    "OSSBucketRegion": "cn-hangzhou",
    "SourceEndpointRegion": "cn-hangzhou",
    "SourceEndpointIpPort": "100.X.X.10:33204",
    "DuplicationArchivePeriod": 365,
    "OSSBucketName": "dbs-backup-1857XXXXX489",
    "BackupPlanStatus": "init",
    "BackupStartTime": "14:22",
    "EnableBackupLog": true,
    "BackupPlanId": "dbXXXXXx7ltj",
    "BackupRetentionPeriod": 730,
    "SourceEndpointInstanceType": "RDS",
    "SourceEndpointUserName": "test",
    "DuplicationInfrequentAccessPeriod": 180
   }
  ]
 },
 "TotalPages": 1,
 "Success": true
}
```

<a id="section-1-2-4"></a>

### 1.2.4. StartBackupPlan

Starts a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | StartBackupPlan | The operation that you want to perform. Set the value to <strong>StartBackupPlan</strong>. |
| BackupPlanId | String | Yes | dbstooi01\*\*\*\*\*\* | The ID of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbstooi01\*\*\*\*\*\* | The ID of the backup schedule. |
| CreatedFullBa ckupsetId | String | dbs1hvb0wwwe\*\*\* \* | The ID of the full backup set. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartBackupPlan
&BackupPlanId=dbstooi01******
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbstooi01******</BackupPlanId>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01******",
 "Success": true
}
```

<a id="section-1-2-5"></a>

### 1.2.5. StopBackupPlan

Stops a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | StopBackupPlan | The operation that you want to perform. Set the value to <strong>StopBackupPlan</strong>. |
| BackupPlanId | String | Yes | dbstooi01\*\*\*\* | The ID of the backup schedule. |
| StopMethod | String | Yes | ALL | The operation scope. Valid values:<br>• <strong>ALL</strong>: stops the backup schedule, full data backup tasks, incremental log backup tasks, and restore tasks.<br>• <strong>PLAN</strong>: stops only the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbs1h\*\*\*\*usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StopBackupPlan
&BackupPlanId=dbstooi01****
&StopMethod=ALL
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbs1h****usfa</BackupPlanId>
<Success>true</Success>
```

`JSON`  format

```json
{
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbs1h****usfa",
    "Success": true
}
```

<a id="section-1-2-6"></a>

### 1.2.6. ModifyBackupObjects

Modifies the backup objects of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyBackupOb jects | The operation that you want to perform. Set the value to <strong>ModifyBackupObjects</strong>. |
| BackupObjects | String | Yes | \[ {"DBName":"17x xx92xxxx374", "SchemaName": "gy9xnj8xxxxxx", "TableIncludes": \[{"TableName":"te st1" }\], "TableExcludes": \[{"TableName":"te st2" }\] } \] | The objects that you want to back up. For more information, see Additional description of request <strong>parameters</strong>. |
| BackupPlanId | String | Yes | dbs1h\*\*\*\*usfa | The ID of the backup schedule whose backup objects you want to modify.You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Additional description of request parameters**

The backup objects that are defined in a JSON string in the following format:

```json
[
    {
        "DBName":"Name of the database that you want to back up",
        "SchemaName":"Name of the schema that you want to back up",
        "TableIncludes":[{
         "TableName":"Name of the table that you want to back up"
        }],
        "TableExcludes":[{
            "TableName":"Name of the table that you want to exclude during the backup"
        }]
    }
]
```

- If you specify only the  `DBName`  parameter and do not specify lower levels of objects, all objects in the database are backed up.

- If you specify the  `DBName`  parameter and some lower levels of objects, only the specified objects are backed up by default. You can use the following regular expressions to define different object names:

  A period ( `.` ) matches any single character except  `\r or \n` .

  An asterisk ( `*` ) matches zero or more occurrences of a subexpression which occurs before.  `h.llo`  matches strings such as  `hllo`  and  `heeeello` .

  A question mark ( `?` ) matches zero or one occurrence of a subexpression which occurs before.  `h.?llo`  matches  `hllo`  and  `hello` , but does not match  `haello` .

  The character class  `[characters]`  matches any character included in the braces. For example,  `h[aello]`  matches  `hallo`  and  `hello` .

  The negative character set  `[^characters]`  does not match any character included in the braces. For example,  `h[^ae]llo`  matches  `hcllo`  and  `hdllo` , but does not match  `hallo`  or  `hello` .

  The character range  `[character1-character2]`  matches any character included in the range from  `character1 to character2` , such as  `[0-9]`  and  `[a-z]` .

> **Note**
>
> The  `SchemaName`  and  `NewSchemaName`  parameters are used only for MS SQL databases. The  `DBName`  and  `NewDBName`  parameters are used to define the names of other databases.

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbs1h\*\*\*\*usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | true | Indicates whether a precheck is triggered.If true is returned, you must call the StartBackupPlan operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupObjects
&BackupObjects=[ { "DBName":"17xxx92xxxx374", "SchemaName":"gy9xnj8xxxxxx", "TableIncludes":[{ "TableName":"test1" }], "TableExcludes":[{ "TableName":"test2" }] } ]
&BackupPlanId=dbs1h****usfa
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbs1h****usfa</BackupPlanId>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "Success": true
}
```

<a id="section-1-2-7"></a>

### 1.2.7. ModifyBackupSourceEndpoint

Modifies the information about a data source

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyBackupSo urceEndpoint | The operation that you want to perform. Set the value to <strong>ModifyBackupSourceEndpoint</strong>. |
| BackupPlanId | String | Yes | dbs1h\*\*\*\*usfa | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| SourceEndpointI nstanceType | String | Yes | RDS | The location of the database. Valid values:<br>• RDS<br>• ECS<br>• <strong>Express</strong>: a database that is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.<br>• <strong>Agent</strong>: a database that is connected to DBS over a DBS backup gateway.<br>• <strong>DDS</strong>: an ApsaraDB for MongoDB (MongoDB) database.<br>• <strong>Other</strong>: a database that is connected to DBS by using the IP address and port of the database. |
| SourceEndpoint Region | String | No | cn-hangzhou | The region where the database is deployed.<br>Note<br>If you specify RDS, ECS, DDS, Express, or Agent as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointI nstanceID | String | No | rm-bp1p8c29479jvX XXX | The ID of the database instance.<br>Note<br>If you specify RDS, ECS, DDS, or Express as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointI P | String | No | 100.\*.\*.10:3320 4 | The endpoint of the database.<br>Note<br>If you specify Express, Agent, or Other as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpointP ort | Integer | No | 3306 | The port of the database.<br>Note<br>If you specify ECS, Express, Agent, or Other as the value of SourceEndpointInstanceType, you must specify this parameter. |
| SourceEndpoint DatabaseName | String | No | test | The name of the database.<br>Note<br>• If the database runs the <strong>PostgreSQL</strong> engine or <strong>MongoDB</strong> engine, you must specify this parameter.<br>• If you specify <strong>Agent</strong> as the value of SourceEndpointInstan <strong>ceType</strong> and the database is an SQL Server database, you must specify this parameter. |
| SourceEndpoint UserName | String | No | test | The username of the database account.<br>Note<br>If you specify <strong>Agent</strong> as the value of SourceEndpointInstanceType and the database is an <strong>SQL</strong> <strong>Server</strong> database or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| SourceEndpointP assword | String | No | test | The password of the database account.<br>Note<br>If you specify <strong>Agent</strong> as the value of SourceEndpointInstanceType and the database is an <strong>SQL</strong> <strong>Server</strong> database or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| BackupGatewayI d | Long | No | 21321323213 | The ID of the backup gateway. If you specify <strong>Agent</strong> as the value of <strong>SourceEndpointInstanceType</strong>, you must specify this parameter. |

<table>
  <tr>
    <td>BackupObjects</td>
    <td>String</td>
    <td>No</td>
    <td>[{"DBName":"Nam e of the database that you want to back up", "SchemaName": "Name of the schema that you want to back up", "TableIncludes": [{"TableName":"N ame of the table that you want to back up" }], "TableExcludes": [{"TableName":" Name of the table that you want to exclude during the backup" }] } ]</td>
    <td>The objects that you want to back up. If you specify Agent as the value of SourceEndpointInstanceType, this parameter is optional. In other cases, you must specify this parameter.</td>
  </tr>
  <tr>
    <td>SourceEndpoint OracleSID</td>
    <td>String</td>
    <td>No</td>
    <td>test</td>
    <td>The system ID (SID) of the Oracle database. If the database is an Oracle database, you must specify this parameter.</td>
  </tr>
  <tr>
    <td>CrossAliyunId</td>
    <td>String</td>
    <td>No</td>
    <td>2xxx7778xxxxxx xxxx</td>
    <td>The user ID of the account that is used to perform backups accounts.</td>
  </tr>
  <tr>
    <td>CrossRoleName</td>
    <td>String</td>
    <td>No</td>
    <td>test123</td>
    <td>The name of the Resource Access Management (RAM) role that is used to perform backups across accounts.</td>
  </tr>
  <tr>
    <td>RegionId</td>
    <td>String</td>
    <td>No</td>
    <td>cn-hangzhou</td>
    <td>The region ID.</td>
  </tr>
  <tr>
    <td>ClientToken</td>
    <td>String</td>
    <td>No</td>
    <td>ETnLKlblzczshOT UbOCzxxxxxxx</td>
    <td>The client token that is used to ensure the idempotence of the request.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbs1h\*\*\*\*usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | false | Indicates whether a precheck is triggered.Valid values:<br>• true<br>• false<br>Note<br>If true is returned, you must call the <strong>StartBackupPlan</strong> operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSourceEndpoint
&BackupPlanId=dbs1h****usfa
&SourceEndpointInstanceType=RDS
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbs1h****usfa</BackupPlanId>
<NeedPrecheck>false</NeedPrecheck>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "NeedPrecheck": false,
 "Success": true
}
```

<a id="section-1-2-8"></a>

### 1.2.8. ModifyBackupPlanName

Changes the name of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyBackupPl anName | The operation that you want to perform. Set the value to <strong>ModifyBackupPlanName</strong>. |
| BackupPlanId | String | Yes | dbstooi0\*\*\*\* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| BackupPlanNam e | String | Yes | dbstooi0\*\*\*\* | The name of the backup schedule.You can call the <strong>DescribeBackupPlanList</strong> operation to query the name of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbstooi0\*\*\*\* | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupPlanName
&BackupPlanId=dbstooi0****
&BackupPlanName=dbstooi0****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbstooi0****</BackupPlanId>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi0****",
 "Success": true
}
```

<a id="section-1-2-9"></a>

### 1.2.9. ModifyBackupStrategy

Modifies the backup time of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyBackupStr ategy | The operation that you want to perform. Set the value to <strong>ModifyBackupStrategy</strong>. |
| BackupPeriod | String | Yes | Monday | The full backup cycle. Valid values:<br>• Monday<br>• Tuesday<br>• Wednesday<br>• Thursday<br>• Friday<br>• Saturday<br>• Sunday |
| BackupPlanId | String | Yes | dbstooi01\*\*\*\* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| BackupStartTim e | String | No | 14:22 | The start time of the full backup.Specify the value in the HH:mmZ format in UTC. |
| BackupStrategy Type | String | No | simple | The full backup policy. Valid values:<br>• <strong>simple</strong>: scheduled backup. If you specify this value as the value of BackupStrategyType, you must also specify BackupPeriod and BackupStartTime.<br>• <strong>manual</strong>: manual backup.<br>Note<br>Default value: simple. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbstooi01\*\*\*\* | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | false | Indicates whether a precheck is triggered.Valid values:<br>• true<br>• false<br>Note<br>If true is returned, you must call the <strong>StartBackupPlan</strong> operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupStrategy
&BackupPeriod=Monday
&BackupPlanId=dbstooi01****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbstooi01****</BackupPlanId>
<NeedPrecheck>false</NeedPrecheck>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01****",
 "NeedPrecheck": false,
 "Success": true
}
```

<a id="section-1-2-10"></a>

### 1.2.10. DescribeRestoreRangeInfo

Queries the details of time ranges to which you can restore data in a specified backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRestore RangeInfo | The operation that you want to perform. Set the value to DescribeRestoreRangeInfo. |
| BackupPlanId | String | Yes | dbstooi0\*\*\*\* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| BeginTimestamp ForRestore | Long | Yes | 1554560477000 | The beginning of the time range to which you can restore data. Set the value to 1554560477000. |
| EndTimestampF orRestore | Long | Yes | 1554560477000 | The end of the time range to which you can restore data. Set the value to 1554560477000. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
| RecentlyRestore | Boolean | No | true | Specifies whether to query the most recent point in time to which you can restore data. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of DBSRecoverRa nge |  | The details of the time range to which you can restore data. |
| DBSRecoverRa nge |  |  |  |
| BeginTimesta mpForRestore | Long | 1554560477000 | The beginning of the time range to which you can restore data, such as 1554560477000. |
| EndTimestamp ForRestore | Long | 1554560477000 | The end of the time range to which you can restore data, such as 1554560477000. |
| FullBackupList | Array of FullBackupDet ail |  | If you set RangeType to point, this parameter is returned. The value of this parameter describes information about all backup points in the time range. The details of the backup point. |
| FullBackupDet ail |  |  |  |
| BackupSetId | String | dbs1hvb\*\*\*\*\* | The ID of the backup set. |
| EndTime | Long | 1554560477000 | The time when the full backup ended, such as 1554560477000. |
| StartTime | Long | 1554560477000 | The time when the full backup started, such as 1554560477000. |
| RangeType | String | point | The type of the time range to which you can restore data.<br>• <strong>point</strong>: The time range contains discrete points in time at which full backups were performed.<br>• <strong>range</strong>: The time range is a period of time for which continuous backup was performed. You can specify any point in time in the time range to restore data. |
| SourceEndpoin tInstanceID | String | rm-bp1p8c\*\*\*\*\* | The ID of the database instance. |
| SourceEndpoin tInstanceType | String | rm-bp1p8c\*\*\*\*\* | The location of the database instance. |
| RequestId | String | 7A851299-A739-4801-B4BC-FC30A535\*\*\*\* | The request ID. |
| Success | Boolean | false | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreRangeInfo
&BackupPlanId=dbstooi0****
&BeginTimestampForRestore=1554560477000
&EndTimestampForRestore=1554560477000
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<HttpStatusCode>200</HttpStatusCode>
<RequestId>7A851299-A739-4801-B4BC-FC30A535****</RequestId>
<Items>
    <DBSRecoverRange>
        <BeginTimestampForRestore>1554560477000</BeginTimestampForRestore>
        <EndTimestampForRestore>1554560477000</EndTimestampForRestore>
        <FullBackupList>
            <FullBackupDetail>
                <BackupSetId>dbs1hvb*****</BackupSetId>
                <EndTime>1554560477000</EndTime>
                <StartTime>1554560477000</StartTime>
            </FullBackupDetail>
        </FullBackupList>
        <RangeType>point</RangeType>
        <SourceEndpointInstanceID>rm-bp1p8c*****</SourceEndpointInstanceID>
        <SourceEndpointInstanceType>rm-bp1p8c*****</SourceEndpointInstanceType>
    </DBSRecoverRange>
</Items>
```

`JSON`  format

```json
{
    "HttpStatusCode": 200, 
    "RequestId": "7A851299-A739-4801-B4BC-FC30A535****", 
    "Items": {
        "DBSRecoverRange": {
            "BeginTimestampForRestore": 1554560477000, 
            "EndTimestampForRestore": 1554560477000, 
            "FullBackupList": [
                {
                    "FullBackupDetail": {
                        "BackupSetId": "dbs1hvb*****", 
                        "EndTime": 1554560477000, 
                        "StartTime": 1554560477000
                    }
                }
            ], 
            "RangeType": "point", 
            "SourceEndpointInstanceID": "rm-bp1p8c*****", 
            "SourceEndpointInstanceType": "rm-bp1p8c*****"
        }
    }
}
```

<a id="section-1-2-11"></a>

### 1.2.11. DescribeBackupPlanBilling

Queries the billing information of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeBackup PlanBilling | The operation that you want to perform. Set the value to <strong>DescribeBackupPlanBilling</strong>. |
| BackupPlanId | String | Yes | dbssl67c7mx\*\*\* \* | The ID of the backup gateway. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup gateway. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether the storage type is displayed. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | InvalidParameter | The error code. |
| ErrMessage | String | This backupPlan can't support this action | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Item | Struct |  | The billing information of the backup schedule. |
| BuyChargeTyp e | String | PREPAY | The billing method of the instance. Valid values:<br>• PREPAY<br>• POSTPAY |
| BuyCreateTim estamp | Long | 1634700238000 | The timestamp that indicates when the instance was purchased. |
| BuyExpiredTi mestamp | Long | 1716220800000 | The expiration time of the instance.<br>Note<br>This parameter is available only if you set BuyChargeType to PREPAY. |
| BuySpec | String | small | The instance type. |
| ContStorageSi ze | Long | 60391430 | The size of the built-in storage for storing incremental backup data. |
| FullStorageSiz e | Long | 450 | The size of the built-in storage for storing full backup data. |
| IsExpired | Boolean | false | Indicates whether the instance has expired.<br>Note<br>This parameter is available only if you set BuyChargeType to PREPAY. |
| IsFreeBytesUnl imited | Boolean | false | Indicates whether the instance has no backup traffic limit. |
| PaiedBytes | Long | 0 | The total paid backup traffic in the current month. |
| QuotaEndTime stamp | Long | 1640966400000 | The timestamp that indicates when the billing cycle of free backup traffic ends. |
| QuotaStartTim estamp | Long | 1638288000000 | The timestamp that indicates when the billing cycle of free backup traffic starts. |
| TotalFreeBytes | Long | 858993459200 | The total free backup traffic in the current month.<br>Note<br>This parameter is available only if you set BuyChargeType to PREPAY and the value of IsFreeBytesUnlimited is false. |
| UsedFullBytes | Long | 0 | The paid full backup traffic in the current month. |
| UsedIncremen tBytes | Long | 35389201 | The paid incremental backup traffic in the current month. |
| RequestId | String | B38B76CB-DCA0-5B84-A4D6-7BDC7FBF\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanBilling
&BackupPlanId=dbssl67c7mx****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<Item>
    <IsExpired>false</IsExpired>
    <BuyExpiredTimestamp>1716220800000</BuyExpiredTimestamp>
    <FullStorageSize>450</FullStorageSize>
    <BuyCreateTimestamp>1634700238000</BuyCreateTimestamp>
    <IsFreeBytesUnlimited>false</IsFreeBytesUnlimited>
    <ContStorageSize>60391430</ContStorageSize>
    <BuySpec>small</BuySpec>
    <BuyChargeType>PREPAY</BuyChargeType>
</Item>
<RequestId>B38B76CB-DCA0-5B84-A4D6-7BDC7FBF****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<Success>true</Success>
```

`JSON`  format

```json
{
    "Item": {
        "IsExpired": false,
        "BuyExpiredTimestamp": 1716220800000,
        "FullStorageSize": 450,
        "BuyCreateTimestamp": 1634700238000,
        "IsFreeBytesUnlimited": false,
        "ContStorageSize": 60391430,
        "BuySpec": "small",
        "BuyChargeType": "PREPAY"
    },
    "RequestId": "B38B76CB-DCA0-5B84-A4D6-7BDC7FBF****",
    "HttpStatusCode": 200,
    "Success": true
}
```

<a id="section-1-3"></a>

## 1.3. Backup task

<a id="section-1-3-1"></a>

### 1.3.1. DescribeFullBackupList

Queries full backup tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeFullBac kupList | The operation that you want to perform. Set the value to <strong>DescribeFullBackupList</strong>. |
| BackupPlanId | String | Yes | dbstooi01\*\*\*\* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether to return the storage class.<br>Note<br>Default value: true. |
| BackupSetId | String | No | 1ibh2f5u\*\*\*\* | The ID of the backup set. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of FullBackupFile |  | The details of the full backup task. |
| FullBackupFile |  |  |  |
| BackupObjects | String | \[{\\"DBName\\":\\"tes t\\"}\] | The objects that are backed up. |
| BackupSetExpi redTime | Long | 1646813439000 | The point in time when the backup set expired, such as 1554560477000. |
| BackupSetId | String | 1ibh2f5u\*\*\*\* | The ID of the backup set. |
| BackupSize | Long | 151 | The size of the backup set. |
| BackupStatus | String | finish | The status of the full backup task. Valid values:<br>• <strong>schedule</strong>: The backup task is being initialized.<br>• <strong>running</strong>: The backup task is running.<br>• <strong>finish</strong>: The backup task is completed.<br>• <strong>stop</strong>: The backup schedule failed.<br>• <strong>pause</strong>: The backup task is paused. |
| CreateTime | Long | 1583740896000 | The start time of the task, such as 1554560477000. |
| EndTime | Long | 1583741465000 | The end time of the backup, such as 1554560477000. |
| ErrMessage | String | NULL | The error message. |
| FinishTime | Long | 1583741466000 | The end time of the task, such as 1554560477000. |
| SourceEndpoin tIpPort | String | 100.X.X.10:33204 | The endpoint of the database. |
| StartTime | Long | 1583741439000 | The start time of the backup, such as 1554560477000. |
| StorageMetho d | String | Standard | The storage class. Valid values:<br>• <strong>Standard</strong>: The storage class is Standard.<br>• <strong>IA</strong>: The storage class is Infrequent Access (IA).<br>• <strong>Archive</strong>: The storage class is Archive.<br>• <strong>UNKNOWN</strong>: The storage class is unknown. This value is returned because the task is not completed. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 636BC118-6080-4119-A6B5-C199CEC1\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 1 | The total number of full backup tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeFullBackupList
&BackupPlanId=dbstooi01****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>636BC118-6080-4119-A6B5-C199CEC1****</RequestId>
<PageSize>30</PageSize>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>1</TotalElements>
<TotalPages>1</TotalPages>
<Items>
    <FullBackupFile>
        <SourceEndpointIpPort>100.X.X.10:33204</SourceEndpointIpPort>
        <StorageMethod>Standard</StorageMethod>
        <BackupObjects>[{"DBName":"test_y"}]</BackupObjects>
        <EndTime>1583741465000</EndTime>
        <FinishTime>1583741466000</FinishTime>
        <BackupSize>151</BackupSize>
        <CreateTime>1583740896000</CreateTime>
        <StartTime>1583741439000</StartTime>
        <BackupSetExpiredTime>1646813439000</BackupSetExpiredTime>
        <BackupSetId>1ibh2f5u****</BackupSetId>
        <BackupStatus>finish</BackupStatus>
    </FullBackupFile>
</Items>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "636BC118-6080-4119-A6B5-C199CEC1****",
 "PageSize": 30,
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "TotalPages": 1,
 "Items": {
  "FullBackupFile": [
   {
    "SourceEndpointIpPort": "100.X.X.10:33204",
    "StorageMethod": "Standard",
    "BackupObjects": "[{\"DBName\":\"test_y\"}]",
    "EndTime": 1583741465000,
    "FinishTime": 1583741466000,
    "BackupSize": 151,
    "CreateTime": 1583740896000,
    "StartTime": 1583741439000,
    "BackupSetExpiredTime": 1646813439000,
    "BackupSetId": "1ibh2f5u****",
    "BackupStatus": "finish"
   }
  ]
 },
 "Success": true
}
```

<a id="section-1-3-2"></a>

### 1.3.2. DescribeIncrementBackupList

Queries incremental backup tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeIncrem entBackupList | The operation that you want to perform. Set the value to <strong>DescribeIncrementBackupList</strong>. |
| BackupPlanId | String | Yes | dbsqdss5tmh\*\*\* \* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to obtain the ID of the backup schedule. |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether to return the storage class.<br>Note<br>Default value: true. |
| StartTimestamp | Long | No | 1570701361528 | The start time of the backup. |
| EndTimestamp | Long | No | 1570701361528 | The end time of the backup. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of IncrementBac kupFile |  | The details of the incremental backup task. |
| IncrementBac kupFile |  |  |  |
| BackupSetExpi redTime | Long | 1710468872000 | The point in time when the backup set expired, such as 1554560477000. |
| BackupSetId | String | mysql-bin.00\*\*\*\* | The ID of the backup set. |
| BackupSetJobI d | String | 1hv5g9wk4\*\*\*\* | The ID of the backup task. |
| BackupSize | Long | 412032 | The size of the backup set. |
| BackupStatus | String | COMPLETED | The status of the incremental backup task.Valid values:<br>• <strong>INIT</strong>: The backup task is being initialized.<br>• <strong>FILLING</strong>: The backup task is running.<br>• <strong>COMPLETED</strong>: The backup task is completed.<br>• <strong>UNCOMPLETED</strong>: The backup task is not completed. |
| EndTime | Long | 1647396866000 | The end time of the backup, such as 1554560477000. |
| SourceEndpoin tIpPort | String | 172.XX.103.1:43XX | The endpoint of the database. |
| StartTime | Long | 1647375263000 | The start time of the backup, such as 1554560477000. |
| StorageMetho d | String | Standard | The storage class. Valid values:<br>• <strong>Standard</strong>: The storage class is Standard.<br>• <strong>IA</strong>: The storage class is Infrequent Access (IA).<br>• <strong>Archive</strong>: The storage class is Archive.<br>• <strong>UNKNOWN</strong>: The storage class is unknown. This value is returned because the task is not completed. |
| PageNum | Integer | 0 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 8D26CA51-35B8-5155-8818-F40C2F27\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 138 | The total number of incremental backup tasks. |
| TotalPages | Integer | 5 | The total number of pages. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeIncrementBackupList
&BackupPlanId=dbsqdss5tmh****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>8D26CA51-35B8-5155-8818-F40C2F27****</RequestId>
<PageSize>30</PageSize>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>138</TotalElements>
<TotalPages>5</TotalPages>
<Items>
    <IncrementBackupFile>
        <SourceEndpointIpPort>172.XX.103.1:43XX</SourceEndpointIpPort>
        <EndTime>1647396866000</EndTime>
        <BackupSetJobId>1hv5g9wk4****</BackupSetJobId>
        <BackupSize>412032</BackupSize>
        <StartTime>1647375263000</StartTime>
        <BackupSetExpiredTime>1710468872000</BackupSetExpiredTime>
        <BackupSetId>mysql-bin.00****</BackupSetId>
        <BackupStatus>COMPLETED</BackupStatus>
    </IncrementBackupFile>
</Items>
<Success>true</Success>
```

`JSON`  format

```json
{
    "RequestId": "8D26CA51-35B8-5155-8818-F40C2F27****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 138,
    "TotalPages": 5,
    "Items": {
        "IncrementBackupFile": [
            {
                "SourceEndpointIpPort": "172.XX.103.1:43XX",
                "EndTime": 1647396866000,
                "BackupSetJobId": "1hv5g9wk4****",
                "BackupSize": 412032,
                "StartTime": 1647375263000,
                "BackupSetExpiredTime": 1710468872000,
                "BackupSetId": "mysql-bin.00****",
                "BackupStatus": "COMPLETED"
            }
        ]
    },
    "Success": true
}
```

<a id="section-1-4"></a>

## 1.4. Restore task

<a id="section-1-4-1"></a>

### 1.4.1. CreateRestoreTask

Creates a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateRestoreTa sk | The operation that you want to perform. Set the value to <strong>CreateRestoreTask</strong>. |
| BackupPlanId | String | Yes | dbs1hvb0ww\*\*\* \* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| DestinationEndp ointInstanceTyp e | String | Yes | RDS | The location of the database. Valid values:<br>• RDS<br>• ECS<br>• <strong>Express</strong>: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.<br>• <strong>Agent</strong>: The database is connected to DBS over a DBS backup gateway.<br>• <strong>DDS</strong>: The database is an ApsaraDB for MongoDB (MongoDB) database.<br>• <strong>Other</strong>: The database is connected to DBS by using the IP address and port of the database. |
| RestoreTaskNam e | String | Yes | test | The name of the restore task. |
| DestinationEndp ointRegion | String | No | 100.X.X.10:3320 4 | The region where the database is deployed.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to <strong>RDS</strong>, <strong>ECS</strong>, <strong>DDS</strong>, <strong>Express</strong>, or <strong>Agent</strong>, you must specify this parameter. |
| DestinationEndp ointInstanceID | String | No | rm-bp1p8c29\*\*\*\*\* | The ID of the database instance.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to <strong>RDS</strong>, <strong>ECS</strong>, <strong>DDS</strong>, or <strong>Express</strong>, you must specify this parameter. |
| DestinationEndp ointIP | String | No | rm-bpXXXXX9jv8px ero.mysql.rds.ali yuncs.com | The endpoint of the database.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to <strong>Express</strong>, <strong>Agent</strong>, or <strong>Other</strong>, you must specify this parameter. |
| DestinationEndp ointPort | Integer | No | 3306 | The port of the database.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to <strong>Express</strong>, <strong>Agent</strong>, <strong>Other</strong>, or <strong>ECS</strong>, you must specify this parameter. |
| DestinationEndp ointDatabaseNa me | String | No | test | The name of the database.<br>Note<br>If the database runs the <strong>PostgreSQL</strong> engine or <strong>MongoDB</strong> engine, you must specify this parameter. |
| DestinationEndp ointUserName | String | No | test | The username of the database account.<br>Note<br>If the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| DestinationEndp ointPassword | String | No | Test | The password of the database account.<br>Note<br>If the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| BackupGatewayI d | Long | No | 43123424 | The ID of the backup gateway.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to <strong>Agent</strong>, you must specify this parameter. |
| RestoreObjects | String | No | \[ {"DBName":"Nam e of the database that you want to use for restoration", "NewDBName":" Name of the destination database that you want to restore", "SchemaName": "Name of the schema that you want to use for restoration", "NewSchemaNa me":"Name of the destination schema that you want to restore"}\] | The objects that are involved in restoration.<br>Note<br>If you set DestinationEndpointInstance <strong>Type</strong> to Agent, this parameter is optional. In other cases, you must specify this parameter. |
| RestoreTime | Long | No | 1554560477000 | The point in time when you want the restore task to run. |
| BackupSetId | String | No | dbs1hvb0wXXX XX | The ID of the full backup set that is used to restore data. This parameter is mutually exclusive with RestoreTime. |
| DestinationEndp ointOracleSID | String | No | test | The system ID (SID) of the Oracle database.<br>Note<br>If the database is an Oracle database, you must specify this parameter. |
| RestoreDir | String | No | test | If you set DestinationEndpointInstanceTyp <strong>e</strong> to Agent and the backup object of the backup schedule is a MySQL database, you must specify this parameter. |
| RestoreHome | String | No | test | The program directory of the database. |
| Stages | String | No | XXX | This parameter is not required. |
| DuplicateConflic t | String | No | failure | The method that is used to process objects with the same name. Valid values:<br>• <strong>failure</strong> (default): The restore task fails if the system detects objects with the same name.<br>• <strong>renamenew</strong>: The restore task renames objects with the same name starting from the second occurrence. |
| CrossAliyunId | String | No | XXX | This parameter is not supported. |
| CrossRoleName | String | No | XXX | This parameter is not supported. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | InvalidParameterV alid | The error code. |
| ErrMessage | String | Need one of the parameter: \[RestoreTime, BackupSetId\] -&gt; \[RestoreTime, BackupSetId\] | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | 60AF7C5D-EF4D-4D48-8FD5-C0823FDF\*\*\*\* | The request ID. |
| RestoreTaskId | String | s102h\*\*\*\*\* | The ID of the restore task. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateRestoreTask
&BackupPlanId=dbs1hvb0ww****
&DestinationEndpointInstanceType=RDS
&RestoreTaskName=test
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RestoreTaskId>s102h*****</RestoreTaskId>
<RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RestoreTaskId": "s102h*****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
}
```

<a id="section-1-4-2"></a>

### 1.4.2. StartRestoreTask

Starts a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | StartRestoreTas k | The operation that you want to perform. Set the value to <strong>StartRestoreTask</strong>. |
| RestoreTaskId | String | Yes | s102h7rf\*\*\*\* | The ID of the restore task. You can call the <strong>CreateRestoreTask</strong> operation to query the ID of the restore task. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | 60AF7C5D-EF4D-4D48-8FD5-C0823FDF\*\*\*\* | The request ID. |
| RestoreTaskId | String | s102h7rf\*\*\*\* | The ID of the restore task. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartRestoreTask
&RestoreTaskId=s102h7rf****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RestoreTaskId>s102h7rf****</RestoreTaskId>
<RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RestoreTaskId": "s102h7rf****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
}
```

<a id="section-1-4-3"></a>

### 1.4.3. DescribeRestoreTaskList

Queries restore tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRestore TaskList | The operation that you want to perform. Set the value to <strong>DescribeRestoreTaskList</strong>. |
| BackupPlanId | String | No | dbssl67c7mx\*\*\* \* | The ID of the backup schedule. |
| RestoreTaskId | String | No | s102h7rf\*\*\*\* | The ID of the restore task. Separate multiple IDs with commas (,). |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of RestoreTaskD etail |  | The details of the backup schedules. |
| RestoreTaskD etail |  |  |  |
| BackupGatewa yId | Long | 0 | The ID of the backup gateway. |
| BackupPlanId | String | dbssl67c7mx\*\*\*\* | The ID of the backup schedule. |
| BackupSetId | String | 1jy2oe65x\*\*\*\* | The ID of the full backup set that is used in the restore task. |
| ContinuousRes toreProgress | Integer | 100 | The restore progress of the incremental log files. |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | The user ID of the account that is used to perform backups across Alibaba Cloud accounts. |
| CrossRoleNam e | String | test123 | The name of the Resource Access Management (RAM) role that is used to perform backups across Alibaba Cloud accounts. |
| DestinationEn dpointDatabas eName | String | test | The name of the database. |
| DestinationEn dpointInstance ID | String | rm-uf6d8gt9vwvrc\*\*\*\* | The ID of the database instance. |
| DestinationEn dpointInstance Type | String | RDS | The location of the database. Valid values:<br>• RDS<br>• ECS<br>• <strong>Express</strong>: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.<br>• <strong>Agent</strong>: The database is connected to DBS over a DBS backup gateway.<br>• <strong>DDS</strong>: The database is an ApsaraDB for MongoDB (MongoDB) database.<br>• <strong>Other</strong>: The database is connected to DBS by using the IP address and port of the database. |
| DestinationEn dpointIpPort | String | 127.XX.0.1:33XX | The endpoint of the database. |
| DestinationEn dpointOracleSI D | String | test | The system ID (SID) of the Oracle database. |
| DestinationEn dpointRegion | String | cn-hangzhou | The region where the database is deployed. |
| DestinationEn dpointUserNa me | String | test | The username of the database account. |
| ErrMessage | String | NULL | The error message. |
| FullDataRestor eProgress | Integer | 100 | The restore progress of the full backup data. |
| FullStruAfterR estoreProgress | Integer | 100 | The progress of schema restore after full data restore. |
| FullStruforeRe storeProgress | Integer | 100 | The progress of schema restore before full data restore. |
| RestoreDir | String | 100.X.X.10:33204 | The path to which you want to restore data. |
| RestoreObject s | String | \[{\\"DBName\\":\\"test\\ " } \] | The objects that you want to restore. |
| RestoreStatus | String | running | The status of the restore task. Valid values:<br>• <strong>init</strong>: The restore task is not started or does not pass the precheck.<br>• <strong>Running</strong>: The restore task is running.<br>• <strong>stop</strong>: The restore task fails.<br>• <strong>pause</strong>: The restore task is paused.<br>• <strong>check_pass</strong>: The restore task passes the precheck. |
| RestoreTaskCr eateTime | Long | 1554560477000 | The time when the restore task was created. |
| RestoreTaskFi nishTime | Long | 1554560477000 | The time when the restore task was completed. |
| RestoreTaskId | String | 1jefy7ewt\*\*\*\* | The ID of the restore task. |
| RestoreTaskN ame | String | cbs34s6\*\*\*\* | The name of the restore task. |
| RestoreTime | Long | 1636567334000 | The point in time when the restore task was executed. |
| PageNum | Integer | 0 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 1A999262-DB3F-5368-AA6E-61AFDA8E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 2 | The total number of restore tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreTaskList
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>1A999262-DB3F-5368-AA6E-61AFDA8E****</RequestId>
<PageSize>30</PageSize>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>2</TotalElements>
<TotalPages>1</TotalPages>
<Items>
    <RestoreTaskDetail>
        <RestoreDir/>
        <FullStruAfterRestoreProgress>0</FullStruAfterRestoreProgress>
        <FullStruforeRestoreProgress>0</FullStruforeRestoreProgress>
        <BackupSetId>1jy2oe65x****</BackupSetId>
        <RestoreStatus>check_pass</RestoreStatus>
        <DestinationEndpointInstanceType>RDS</DestinationEndpointInstanceType>
        <RestoreTime>1636567334000</RestoreTime>
        <DestinationEndpointRegion>cn-hangzhou</DestinationEndpointRegion>
        <FullDataRestoreProgress>0</FullDataRestoreProgress>
        <RestoreTaskId>1jefy7ewt****</RestoreTaskId>
        <DestinationEndpointIpPort>127.XX.0.1:33XX</DestinationEndpointIpPort>
        <DestinationEndpointUserName/>
        <RestoreObjects>[{"DBName":"rds1_wyp","NewDBName":"rds1_wyp"}]</RestoreObjects>
        <RestoreTaskName>cbs34s6****</RestoreTaskName>
        <BackupPlanId>dbssl67c7mx****</BackupPlanId>
        <RestoreTaskCreateTime>1636623886000</RestoreTaskCreateTime>
        <BackupGatewayId>0</BackupGatewayId>
    </RestoreTaskDetail>
    <RestoreTaskDetail>
        <RestoreDir/>
        <FullStruAfterRestoreProgress>100</FullStruAfterRestoreProgress>
        <FullStruforeRestoreProgress>100</FullStruforeRestoreProgress>
        <BackupSetId>sl67c7mx****</BackupSetId>
        <RestoreStatus>finish</RestoreStatus>
        <DestinationEndpointInstanceType>RDS</DestinationEndpointInstanceType>
        <RestoreTime>1634720897000</RestoreTime>
        <DestinationEndpointRegion>cn-shanghai</DestinationEndpointRegion>
        <FullDataRestoreProgress>100</FullDataRestoreProgress>
        <RestoreTaskId>vbhy7r7o****</RestoreTaskId>
        <ContinuousRestoreProgress>100</ContinuousRestoreProgress>
        <DestinationEndpointIpPort>172.XX.0.1:46XX</DestinationEndpointIpPort>
        <DestinationEndpointUserName>rdsdt_dbsacct</DestinationEndpointUserName>
        <RestoreObjects>[{"DBName":"rds1_wyp","NewDBName":"rds1_wyp"}]</RestoreObjects>
        <RestoreTaskName>cbs4225****</RestoreTaskName>
        <BackupPlanId>dbssl67c7mx****</BackupPlanId>
        <RestoreTaskCreateTime>1634721021000</RestoreTaskCreateTime>
        <BackupGatewayId>0</BackupGatewayId>
        <DestinationEndpointInstanceID>rm-uf6d8gt9vwvrc****
</DestinationEndpointInstanceID>
        <RestoreTaskFinishTime>1634721478000</RestoreTaskFinishTime>
    </RestoreTaskDetail>
</Items>
<Success>true</Success>
```

`JSON`  format

```json
{
    "RequestId": "1A999262-DB3F-5368-AA6E-61AFDA8E****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 2,
    "TotalPages": 1,
    "Items": {
        "RestoreTaskDetail": [
            {
                "RestoreDir": "",
                "FullStruAfterRestoreProgress": 0,
                "FullStruforeRestoreProgress": 0,
                "BackupSetId": "1jy2oe65x****",
                "RestoreStatus": "check_pass",
                "DestinationEndpointInstanceType": "RDS",
                "RestoreTime": 1636567334000,
                "DestinationEndpointRegion": "cn-hangzhou",
                "FullDataRestoreProgress": 0,
                "RestoreTaskId": "1jefy7ewt****",
                "DestinationEndpointIpPort": "127.XX.0.1:33XX",
                "DestinationEndpointUserName": "",
                "RestoreObjects": "
[{\"DBName\":\"rds1_wyp\",\"NewDBName\":\"rds1_wyp\"}]",
                "RestoreTaskName": "cbs34s6****",
                "BackupPlanId": "dbssl67c7mx****",
                "RestoreTaskCreateTime": 1636623886000,
                "BackupGatewayId": 0
            },
            {
                "RestoreDir": "",
                "FullStruAfterRestoreProgress": 100,
                "FullStruforeRestoreProgress": 100,
                "BackupSetId": "sl67c7mx****",
                "RestoreStatus": "finish",
                "DestinationEndpointInstanceType": "RDS",
                "RestoreTime": 1634720897000,
                "DestinationEndpointRegion": "cn-shanghai",
                "FullDataRestoreProgress": 100,
                "RestoreTaskId": "vbhy7r7o****",
                "ContinuousRestoreProgress": 100,
                "DestinationEndpointIpPort": "172.XX.0.1:46XX",
                "DestinationEndpointUserName": "rdsdt_dbsacct",
                "RestoreObjects": "
[{\"DBName\":\"rds1_wyp\",\"NewDBName\":\"rds1_wyp\"}]",
                "RestoreTaskName": "cbs4225****",
                "BackupPlanId": "dbssl67c7mx****",
                "RestoreTaskCreateTime": 1634721021000,
                "BackupGatewayId": 0,
                "DestinationEndpointInstanceID": "rm-uf6d8gt9vwvrc****",
                "RestoreTaskFinishTime": 1634721478000
            }
        ]
    },
    "Success": true
}
```

<a id="section-1-5"></a>

## 1.5. Backup gateway

<a id="section-1-5-1"></a>

### 1.5.1. DescribeBackupGatewayList

Queries backup gateways.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeBackup GatewayList | The operation that you want to perform. Set the value to <strong>DescribeBackupGatewayList</strong>. |
| Region | String | Yes | cn-hangzhou | The region where DBS is activated.<br>Note<br>If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
| Identifier | String | No | 7213527653217 | The unique identifier of the backup gateway. Separate multiple identifiers with commas (,). |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be 0 or a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupGatewa y |  | The details of the backup gateways. |
| BackupGatewa y |  |  |  |
| BackupGatewa yCreateTime | Long | 1554560477000 | The time when the backup gateway was created. |
| BackupGatewa yId | String | 2321313\*\*\* | The ID of the backup gateway. |
| BackupGatewa yStatus | String | ONLINE | The status of the backup gateway. Valid values:<br>• ONLINE<br>• OFFLINE<br>• STOPPED<br>• UPGRADING |
| DisplayName | String | test | The display name of the backup gateway. |
| Identifier | String | sgdsaj\*\*\*\* | The unique identifier of the backup gateway. |
| LastHeartbeat Time | Long | 1554560477000 | The time when the last heartbeat was reported. |
| Region | String | cn-hangzhou | The region ID of the backup gateway. |
| SourceEndpoin tHostname | String | test | The name of the host on which the backup gateway is installed. |
| SourceEndpoin tInternetIP | String | XX.XX.XX.XX | The public IP address of the host on which the backup gateway is installed. |
| SourceEndpoin tIntranetIP | String | XX.XX.XX.XX | The private IP address of the host on which the backup gateway is installed. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 46361705-8531-492F-807E-A97E482D\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 0 | The total number of backup gateways. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupGatewayList
&Region=cn-hangzhou
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<PageSize>30</PageSize>
<RequestId>46361705-8531-492F-807E-A97E482D****</RequestId>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>0</TotalElements>
<Items>
</Items>
<TotalPages>0</TotalPages>
<Success>true</Success>
```

`JSON`  format

```json
{
 "PageSize": 30,
 "RequestId": "46361705-8531-492F-807E-A97E482D****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 0,
 "Items": {
  "BackupGateway": []
 },
 "TotalPages": 0,
 "Success": true
}
```

<a id="section-1-6"></a>

## 1.6. Backup set download

<a id="section-1-6-1"></a>

### 1.6.1. DescribeBackupSetDownloadTaskList

Queries backup set download tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeBackup SetDownloadTas kList | The operation that you want to perform. Set the value to DescribeBackupSetDownloadTas <strong>kList</strong>. |
| BackupPlanId | String | No | dbssl67c7mx\*\*\* \* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| BackupSetDownl oadTaskId | String | No | dbstooi01e\*\*\*\*\* | The ID of the backup set download task. |
| PageSize | Integer | No | 30 | The number of entries per page.Valid values: 30, 50, and 100.<br>Note<br>Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupSetDow nloadTaskDeta il |  | The details of the backup schedules. |
| BackupSetDow nloadTaskDeta il |  |  |  |
| BackupGatewa yId | Long | 123 | The backup gateway that is used to download the backup set. This parameter is available only if you set BackupSetDownloadWay to auto. |
| BackupPlanId | String | sl67c7mx\*\*\*\* | The ID of the backup schedule. |
| BackupSetCod e | String | 1h7zrxja0\*\*\*\* | The code of the backup set.<br>• Full: the code is the same as the ID of the backup set.<br>• Incremental: the code is the same as the name of the backup set. |
| BackupSetDat aFormat | String | CSV | The format in which the backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON |
| BackupSetDat aSize | Long | 151 | The size of the data in the backup set. |
| BackupSetDbT ype | String | MySQL | The type of the database engine. |
| BackupSetDow nloadCreateTi me | Long | 1641545488000 | The time when the backup set download task was created. |
| BackupSetDow nloadDir | String | dbs_test | The server directory to which the backup set is downloaded. This parameter is available only if you set BackupSetDownloadWay to auto. |
| BackupSetDow nloadFinishTi me | Long | 1641545557000 | The time when the backup set download was completed. |
| BackupSetDow nloadInternetU rl | String | //dbs-137XXX-cn-hangzhou-1hr5cpbtm\*\*\*\*.oss -cn-hangzhou.XXX.com/example345 | The public download URL of the backup set. This parameter is available only if you set BackupSetDownloadWay to manual and the conversion is completed. |
| BackupSetDow nloadIntranetU rl | String | //dbs-137XXX-cn-hangzhou-1hr5cpbtm\*\*\*\*.oss -cn-hangzhou-internal.XXX.com/e xample123 | The internal download URL of the backup set. This parameter is available only if you set BackupSetDownloadWay to manual and the conversion is completed. |
| BackupSetDow nloadStatus | String | finish | The status of the backup set download task. Valid values:<br>• <strong>init</strong>: The backup set download task is initialized.<br>• <strong>warning</strong>: An alert is reported for the backup set download task.<br>• <strong>catched</strong>: An exception occurred in the backup set download task.<br>• <strong>running</strong>: The backup set download task is running.<br>• failed: The backup set download task failed.<br>• <strong>finish</strong>: The backup set download task is completed. |
| BackupSetDow nloadTargetTy pe | String | agent | The type of the destination server to which the backup set is downloaded. This parameter is available only if you set BackupSetDownloadWay to auto.<br>Note<br>A value of agent indicates a server on which a backup gateway is installed. |
| BackupSetDow nloadTaskId | String | sl9gpu86\*\*\* | The ID of the backup set download task. |
| BackupSetDow nloadTaskNam e | String | 1h7zrxja0\*\*\*\*-ManualFull | The name of the backup set download task. |
| BackupSetDow nloadWay | String | manual | The method in which the backup set is downloaded. Valid values:<br>• <strong>manual</strong>: The backup set is manually downloaded.<br>• <strong>auto</strong>: The backup set is automatically downloaded. |
| BackupSetId | String | 1h7zrxja0\*\*\*\* | The ID of the source backup set. |
| BackupSetJobT ype | String | cbs_backup_sub_fu ll | The type of the backup set download task.Valid values:<br>• <strong>cbs_backup_sub_full</strong>: logical full backup set download<br>• <strong>cbs_backup_sub_cont</strong>: logical incremental backup set download |
| ErrMessage | String | java.lang.IndexOut OfBoundsException. | The error message. |
| PageNum | Integer | 0 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | FB9C5B62-15CA-5B72-B0F5-F0BDD165\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |
| TotalElements | Integer | 1 | The total number of backup set download tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupSetDownloadTaskList
&BackupPlanId = dbssl67c7mx****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>FB9C5B62-15CA-5B72-B0F5-F0BDD165****</RequestId>
<PageSize>30</PageSize>
<PageNum>0</PageNum>
<HttpStatusCode>200</HttpStatusCode>
<TotalElements>1</TotalElements>
<TotalPages>1</TotalPages>
<Items>
    <BackupSetDownloadTaskDetail>
        <BackupSetDbType>MySQL</BackupSetDbType>
        <BackupSetDownloadCreateTime>1641545488000</BackupSetDownloadCreateTime>
        <BackupSetDownloadTaskName>1h7zrxja0****-ManualFull</BackupSetDownloadTaskName>
        <BackupSetDownloadWay>manual</BackupSetDownloadWay>
        <BackupSetCode>1h7zrxja0****</BackupSetCode>
        <BackupSetId>1h7zrxja0****</BackupSetId>
        <BackupSetDownloadStatus>finish</BackupSetDownloadStatus>
        <BackupSetDownloadIntranetUrl>//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.oss-cn-hangzhou-internal.XXX.com/example123</BackupSetDownloadIntranetUrl>
        <BackupSetDownloadInternetUrl>//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.oss-cn-hangzhou.XXX.com/example345</BackupSetDownloadInternetUrl>
        <BackupSetDownloadTaskId>sl9gpu86***</BackupSetDownloadTaskId>
        <BackupSetDownloadFinishTime>1641545557000</BackupSetDownloadFinishTime>
        <BackupSetJobType>cbs_backup_sub_full</BackupSetJobType>
        <BackupSetDataFormat>CSV</BackupSetDataFormat>
        <BackupPlanId>sl67c7mx****</BackupPlanId>
        <BackupSetDataSize>151</BackupSetDataSize>
    </BackupSetDownloadTaskDetail>
</Items>
<Success>true</Success>
```

`JSON`  format

```json
{
    "RequestId": "FB9C5B62-15CA-5B72-B0F5-F0BDD165****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 1,
    "TotalPages": 1,
    "Items": {
        "BackupSetDownloadTaskDetail": [
            {
                "BackupSetDbType": "MySQL",
                "BackupSetDownloadCreateTime": 1641545488000,
                "BackupSetDownloadTaskName": "1h7zrxja0****-ManualFull",
                "BackupSetDownloadWay": "manual",
                "BackupSetCode": "1h7zrxja0****",
                "BackupSetId": "1h7zrxja0****",
                "BackupSetDownloadStatus": "finish",
                "BackupSetDownloadIntranetUrl": "//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.
oss-cn-hangzhou-internal.XXX.com/example123",
                "BackupSetDownloadInternetUrl": "//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.
oss-cn-hangzhou.XXX.com/example345",
                "BackupSetDownloadTaskId": "sl9gpu86***",
                "BackupSetDownloadFinishTime": 1641545557000,
                "BackupSetJobType": "cbs_backup_sub_full",
                "BackupSetDataFormat": "CSV",
                "BackupPlanId": "sl67c7mx****",
                "BackupSetDataSize": 151
            }
        ]
    },
    "Success": true
}
```

<a id="section-1-6-2"></a>

### 1.6.2. Configures download rules for backup sets.

You can call the ModifyBackupSetDownloadRules operation to enable, modify, or disable the automatic download feature.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyBackupSe tDownloadRules | The operation that you want to perform. Set the value to <strong>ModifyBackupSetDownloadRules</strong>. |
| BackupPlanId | String | Yes | dbstooi01\*\*\*\* | The ID of the backup schedule. You can call the <strong>DescribeBackupPlanList</strong> operation to query the ID of the backup schedule. |
| OpenAutoDownl oad | Boolean | No | false | Specifies whether to enable the automatic download feature. Default value: false. |
| BackupGatewayI d | Long | No | 123123123 | The ID of the backup gateway that is used to download the backup set. |
| FullDataFormat | String | No | CSV | The format in which the full backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON<br>Note<br>Default value: <strong>CSV</strong>. |
| IncrementDataF ormat | String | No | Native | The format in which the incremental backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON<br>Note<br>Default value: <strong>Native</strong>. |
| BackupSetDownl oadDir | String | No | test | The server directory to which the backup set is downloaded. |
| BackupSetDownl oadTargetType | String | No | agent | The type of the destination server to which the backup set is downloaded.<br>Note<br>Default value: <strong>agent</strong>. The default value specifies that a backup gateway is installed. |
| BackupSetDownl oadTargetTypeL ocation | String | No | local | The type of the destination directory to which the backup set is downloaded. If the automatic download feature is enabled, you must specify this parameter. Valid values:<br>• local<br>• nas<br>• ftp<br>• minio<br>Note<br>Default value: <strong>local</strong>. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupPlanId | String | dbstooi01e\*\*\*\* | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Description**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSetDownloadRules
&BackupPlanId=dbstooi01****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupPlanId>dbstooi01e****</BackupPlanId>
<Success>true</Success>
```

`JSON`  format

```json
{
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupPlanId": "dbstooi01e****",
  "Success": true
}
```

<a id="section-1-6-3"></a>

### 1.6.3. CreateFullBackupSetDownload

Creates and starts a full backup set download task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateFullBacku pSetDownload | The operation that you want to perform. Set the value to <strong>CreateFullBackupSetDownload</strong>. |
| BackupSetId | String | Yes | dbs1hv\*\*\*\*\* | The ID of the full backup set. You can call the DescribeBackupSetDownloadTas <strong>kList</strong> operation to query the ID of the full backup set. |
| BackupSetDataF ormat | String | No | SQL | The format in which the full backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON<br>Note<br>Default value: <strong>CSV</strong>. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupSetDow nloadTaskId | String | dbstooi01e\*\*\*\*\* | The ID of the backup set download task. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateFullBackupSetDownload
&BackupSetId=dbs1hv*****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId>
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<ErrMessage>The specified parameter %s value is not valid.</ErrMessage>
<Success>true</Success>
<ErrCode>Param.NotFound</ErrCode>
```

`JSON`  format

```json
{
    "BackupSetDownloadTaskId": "dbstooi01e*****",
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
}
```

<a id="section-1-6-4"></a>

### 1.6.4. CreateIncrementBackupSetDownload

Creates and starts an incremental backup set download task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateIncrement BackupSetDownl oad | The operation that you want to perform. Set the value to CreateIncrementBackupSetDownl <strong>oad</strong>. |
| BackupSetId | String | Yes | dbstooi01e\*\*\*\*\* | The ID of the incremental backup set.You can call the DescribeBackupSetDownloadTas <strong>kList</strong> operation to query the ID of the incremental backup set. |
| BackupSetName | String | Yes | test | The name of the incremental backup set. |
| BackupSetDataF ormat | String | No | Native | The format in which the incremental backup set is downloaded. Valid values:<br>• Native<br>• SQL<br>• CSV<br>• JSON<br>Note<br>Default value: Native. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BackupSetDow nloadTaskId | String | dbstooi01e\*\*\*\*\* | The ID of the backup set download task. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC-455A-85FE-45F0B22E\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateIncrementBackupSetDownload
&BackupSetId=dbstooi01e*****
&BackupSetName=test
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId>
<Success>true</Success>
```

`JSON`  format

```json
{
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupSetDownloadTaskId": "dbstooi01e*****",
  "Success": true
}
```

<a id="section-1-7"></a>

## 1.7. Others

<a id="section-1-7-1"></a>

### 1.7.1. Queries the standard error information of a DBS task.

You can call the DescribeJobErrorCode operation to query the standard error information of a Database Backup (DBS) task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeJobError Code | The operation that you want to perform. Set the value to <strong>DescribeJobErrorCode</strong>. |
| TaskId | String | Yes | dbstooi0\*\*\*\* | The ID of the full backup or restore task. |
| Language | String | No | en | The language of the error message.Valid values: <strong>en</strong> and <strong>cn</strong>.<br>Note<br>Default value: <strong>en</strong>. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Item | Struct |  | The item for which the error is reported. |
| ErrorCode | String | failed | The error code. |
| ErrorMessage | String | Describe preCheck progress failed. | The standard error message. |
| JobId | String | tooi0\*\*\*\* | The ID of the full backup or restore task. |
| JobState | String | init | The task status. |
| JobType | String | testId | The ID of the internal DBS task type. |
| Language | String | en | The language of the error message. |
| RequestId | String | 1FC2F86D-AFF4-4ED9-BB25-ADDE196C\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeJobErrorCode
&TaskId=dbstooi0****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<Item>
    <Language>en</Language>
    <JobId>tooi0****</JobId>
</Item>
<RequestId>1FC2F86D-AFF4-4ED9-BB25-ADDE196C****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<Success>true</Success>
```

`JSON`  format

```json
{
 "Item": {
  "Language": "en",
  "JobId": "tooi0****"
 },
 "RequestId": "1FC2F86D-AFF4-4ED9-BB25-ADDE196C****",
 "HttpStatusCode": 200,
 "Success": true
}
```

<a id="section-1-7-2"></a>

### 1.7.2. DescribeNodeCidrList

Queries the CIDR blocks of nodes on which DBS is running.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeNodeCi drList | The operation that you want to perform. Set the value to <strong>DescribeNodeCidrList</strong>. |
| Region | String | Yes | cn-hangzhou | The region where DBS is activated.<br>Note<br>If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| InternetIPs | List | "10.X.X.0/24" | The public CIDR blocks. |
| IntranetIPs | List | "10.X.X.0/24" | The internal CIDR blocks. |
| RequestId | String | 5B352E69-E7B1-4EA7-BB8E-29FFE969\*\*\*\* | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeNodeCidrList
&Region=cn-hangzhou
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>5B352E69-E7B1-4EA7-BB8E-29FFE969****</RequestId>
<InternetIPs>
    <InternetIP>118.X.X.0/24</InternetIP>
    <InternetIP>47.X.X.0/24</InternetIP>
</InternetIPs>
<HttpStatusCode>200</HttpStatusCode>
<IntranetIPs>
    <IntranetIP>10.X.X.0/24</IntranetIP>
    <IntranetIP>10.X.X.0/24</IntranetIP>
    <IntranetIP>10.X.X.0/24</IntranetIP>
</IntranetIPs>
<Success>true</Success>
```

`JSON`  format

```json
{
 "RequestId": "5B352E69-E7B1-4EA7-BB8E-29FFE969****",
 "InternetIPs": {
  "InternetIP": [
   "118.X.X.0/24",
   "47.X.X.0/24"
  ]
 },
 "HttpStatusCode": 200,
 "IntranetIPs": {
  "IntranetIP": [
   "10.X.X.0/24",
   "10.X.X.0/24",
   "10.X.X.0/24"
  ]
 },
 "Success": true
}
```

<a id="section-1-7-3"></a>

### 1.7.3. DescribePreCheckProgressList

Queries the precheck progress of a backup schedule or a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribePreChe ckProgressList | The operation that you want to perform. Set the value to <strong>DescribePreCheckProgressList</strong>. |
| BackupPlanId | String | No | dbstooi01\*\*\*\* | The ID of the backup schedule. |
| RestoreTaskId | String | No | dbasdsa\*\*\*\* | The ID of the restore task. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ErrCode | String | Param.NotFound | The error code. |
| Items | Array of PreCheckProgr essDetail |  | The details of the precheck progress. |
| PreCheckProgr essDetail |  |  |  |
| BootTime | Long | 1583734969000 | The start time of the precheck, such as 1554560477000. |
| ErrMsg | String | java.lang.RuntimeE xception: Could not find any schema...... | The error message. |
| FinishTime | Long | 1583734969000 | The end time of the precheck, such as 1554560477000. |
| Item | String | CHECK_OTHER | The name of the precheck item. |
| JobId | String | uvk8f6fx\*\*\*\* | The ID of the job for the precheck item. |
| Names | String | CHECK_OTHER | The name of the group to which the precheck item belongs. |
| OrderNum | String | 10 | The sequence number of the precheck item. |
| State | String | warning | The progress of the precheck item. Valid values:<br>• <strong>init</strong>: The item is initialized.<br>• <strong>warning</strong>: An alert is reported.<br>• <strong>catched</strong>: An exception occurred.<br>• <strong>running</strong>: The precheck is in progress.<br>• failed: The precheck failed.<br>• <strong>finish</strong>: The precheck is completed. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| Progress | Integer | 100 | The progress of the precheck task. Valid values: 0 to 100. |
| RequestId | String | C4A45FE1-A903-470D-B113-F12A4DF9\*\*\*\* | The request ID. |
| Status | String | failed | The status of the precheck. Valid values:<br>• <strong>running</strong>: The precheck is in progress.<br>• failed: The precheck failed.<br>• <strong>finish</strong>: The precheck is completed. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values:<br>• <strong>true</strong>: successful<br>• <strong>false</strong>: failed |

**Examples**

Sample requests

```text
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribePreCheckProgressList
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<Status>failed</Status>
<Progress>20</Progress>
<RequestId>C4A45FE1-A903-470D-B113-F12A4DF9****</RequestId>
<HttpStatusCode>200</HttpStatusCode>
<Items>
    <PreCheckProgressDetail>
        <Names>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</Names>
        <Item>CHECK_MYSQL_PASSOWRD_FORMAT</Item>
        <OrderNum>90</OrderNum>
        <State>init</State>
        <BootTime>1583734969000</BootTime>
        <JobId>uvk8f6fx****</JobId>
    </PreCheckProgressDetail>
</Items>
<ErrMessage>java.lang.RuntimeException: Could not find any schema ......</ErrMessage>
<Success>true</Success>
```

`JSON`  format

```json
{
 "Status": "failed",
 "Progress": 20,
 "RequestId": "C4A45FE1-A903-470D-B113-F12A4DF9****",
 "HttpStatusCode": 200,
 "Items": {
  "PreCheckProgressDetail": [
   {
    "Names": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL",
    "Item": "CHECK_MYSQL_PASSOWRD_FORMAT",
    "OrderNum": "90",
    "State": "init",
    "BootTime": 1583734969000,
    "JobId": "uvk8f6fx****"
   }
  ]
 },
 "ErrMessage": "java.lang.RuntimeException: Could not find any schema ......",
 "Success": true
}
```

<a id="section-1-7-4"></a>

### 1.7.4. PhysicalDeleteResource

Physically deletes resources from Database Backup.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| RegionId | Strin g | Query | No | cn-hangzhou | The ID of the region. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the operation. |
| Pk | Strin g | Query | Yes | 259258662544\*\*\*\*\*\* | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | Bid |
| Hid | Long | Query | Yes | 1001 | The unique ID. |
| Country | Strin g | Query | Yes | CN | The country. The default value is CN. |
| TaskIdenti fier | Strin g | Query | Yes | 001 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retry_count": 3, "timeout": 60, "priority": "high"} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | \*\*\*\*\* | This parameter is left empty if the request is successful. An error message is returned if the request fails. |

**Returned Data**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| Interrupt | Boolean | false | Indicates whether the task was interrupted. |
| Invoker | String | admin | The invoker of the operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | The request ID. |
| Hid | Long | 123456 | The unique ID. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | ExampleValue | The task identifier. |
| TaskExtraData | String | {"retry_count": 3, "timeout": 60, "priority": "high"} | The extra data for the task. |
| GmtWakeup | String | 08:00 | The wakeup time. |
| Success | Boolean | true | The returned status.<br>• Success: true.<br>• false: The request failed. |
| Message | String | success | The additional information. |

**Examples**

Request example

```text
http(s)://[Endpoint]/?Action=PhysicalDeleteResource
&Invoker=admin
&Pk=259258662544******
&Bid=26842
&Hid=1001
&Country=CN
&TaskIdentifier=001
&TaskExtraData={"retry_count": 3, "timeout": 60, "priority": "high"}
&GmtWakeup=
&<Common request parameters>
```

Response example

`JSON`  format

```json
{
 "GmtWakeup":"",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"ExampleValue",
 "Message":"success",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 60, \"priority\": \"high\"}",
 "Country":"China",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
}
```

<a id="section-1-7-5"></a>

### 1.7.5. LogicalDeleteResource

Logically deletes a specified resource in Database Backup.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Locati on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the API operation. |
| Pk | Strin g | Query | Yes | 259258662544\*\*\*\*\*\* | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | Bid |
| Hid | Long | Query | Yes | 9999 | The unique ID. |
| Country | Strin g | Query | Yes | CN | The country. The default value is CN. |
| TaskIdenti fier | Strin g | Query | Yes | EX12345 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retryCount": 3, "timeout": 60} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | \*\*\*\*\* | If the request is successful, this parameter is empty. If the request fails, an error message is returned. |

**Response data**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| Interrupt | Boolean | false | Indicates whether the task was interrupted. |
| Invoker | String | admin | The invoker of the API operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | Request ID |
| Hid | Long | 123456 | The unique ID. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | example_value | The task identifier. |
| TaskExtraData | String | {"retryCount": 3, "timeout": 60} | The extra data for the task. |
| GmtWakeup | String | 07:30 | The wakeup time. |
| Success | Boolean | true | The status that is returned.<br>• Success: true.<br>• failed: false |
| Message | String | success | The additional information. |

**Examples**

Sample request

```text
http(s)://[Endpoint]/?Action=LogicalDeleteResource
&Invoker=admin
&Pk=259258662544******
&Bid=26842
&Hid=9999
&Country=CN
&TaskIdentifier=EX12345
&TaskExtraData={"retryCount": 3, "timeout": 60}
&GmtWakeup=
&<Common request parameters>
```

Sample response `JSON`  format

```json
{
 "GmtWakeup":"07:30",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"example_value",
 "Message":"success",
 "TaskExtraData":"{\"retryCount\": 3, \"timeout\": 60}",
 "Country":"China",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
}
```

<a id="section-1-7-6"></a>

### 1.7.6. DescribeOssStsToken

Returns a Security Token Service (STS) token for secure access to Object Storage Service (OSS).

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| BackupPla nId | Strin g | Query | No | dbstooi01xxxx | The ID of the backup schedule. To obtain this parameter, call the DescribeBackupPlanList operation. |
| Identifier | Strin g | Query | No | temperature | The identifier of the event to query.<br>• For weak verification, you can view the device's event Identifier under the product's feature definition in the console, or call QueryThingModel and view the identifier in the returned Thing Specification Language model.<br>• identifier For no verification: Use the same custom identifier that the device uses to report the event. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| Resource OwnerId | Long | Query | No | 345678912345 | This is a system parameter related to authentication. Do not specify this parameter. |

**Returned Data**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| Success | Boolean | true | The return status.<br>• The operation was successful.<br>• Failed: false. |
| Message | String | success | Additional information. |
| Code | String | 200 | The status of the API call or a POP error code. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| AccessKeyId | String | 0wNEpMMlzy7s\*\*\*\* | The AccessKey ID. |
| AccessKeySecr et | String | lml2H\*\*\*\*\*\* | The AccessKey secret. |
| SecurityToken | String | \*\*\*\*\*\*\*\* | The STS security token. |
| OssPrefix | String | test-prefix/hello-prefix | The prefix for the OSS object. This prefix, along with the bucket name and path format, forms the full path of the delivered file. For example, <code> test-prefix </code> or <code> test/prefix </code>. The prefix can contain forward slashes (/) as separators. Each part of the prefix must meet the following requirements:<br>1. Contains only uppercase letters, lowercase letters, digits, underscores (_), hyphens (-), and periods (.).<br>2. Is no more than 253 characters long.<br>3. Starts with a letter or a digit. |
| EnvMode | String | Production | The environment type. A value of \`Production\` indicates the production environment, which provides live services. |
| ClientType | String | 1 | The client type. |

**Examples**

Sample request

```text
http(s)://[Endpoint]/?Action=DescribeOssStsToken
&Common request parameters
```

Sample response

`JSON`  format

```json
{
 "SecurityToken":"********",
 "ClientType":"1",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "AccessKeyId":"0wNEpMMlzy7s****",
 "EnvMode":"Production",
 "AccessKeySecret":"lml2H******",
 "HttpStatusCode":200,
 "OssPrefix":"test-prefix/hello-prefix",
 "Code":"200",
 "Success":true
}
```

<a id="section-1-7-7"></a>

### 1.7.7. DescribeBackupInstances

Queries a list of database backup instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| BackupPla nId | Strin g | Query | No | dbstooi01xxxx | The ID of the backup schedule. Call the DescribeBackupPlanList operation to obtain the value of this parameter. |
| Resource OwnerId | Long | Query | No | 345678912345 | A system parameter for authentication. You do not need to specify this parameter. |
| Resource RegionId | Strin g | Query | No | cn-hangzhou | The region where the resource resides. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page.<br>Default value: 10. |

**Returned data**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| BackupInstanc es | Array | \["backup1", "backup2", "backup3"\] | Specifies a list of names or identifiers for a group of backup instances, used to record or manage multiple backup replicas. |
| -Id | String | 1 | The ID of the role. |
| -Name | String | test | Metric name. |
| -JobId | String | 72dcd26b-f12d-4c27-b3af-18f6aed5\*\*\*\* | The ID of the asynchronous task. |
| -RegionId | String | cn-hangzhou | The region ID. |
| -PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go. Prepaid: subscription. |
| -CreateTime | String | 2022 | The time when the instance was created. |
| -ExpireTime | String | 2018-08-24T09:55:41Z | The expiration time. |
| -DbType | String | MySQL | The database type. |
| -ConnectionStr | String | jdbc:mysql://localh ost:3306/mydb? user=root&amp;passwo rd=123456 | A connection string to the local MySQL database \`mydb\` with the username \`root\` and password \`123456\`. |
| -OssBucket | String | liveBucket\*\*\*\* | The name of the OSS bucket. |
| -Status | String | 1 | The status. |
| RequestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The request ID. |
| Success | Boolean | true | The status that is returned.<br>• Success: true.<br>• Failed: false. |
| Message | String | success | Additional information. |
| TotalBackupIn stanceCount | Integer | 5 | Indicates that the current system contains a total of five backup instances. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample request

```text
http(s)://[Endpoint]/?Action=DescribeBackupInstances
&<Common request parameters>
```

Sample response

`JSON`  format

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "TotalBackupInstanceCount":5,
 "PageSize":10,
 "PageNumber":1,
 "BackupInstances":[
  {
   "Status":"1",
   "CreateTime":"2022",
   "OssBucket":"liveBucket****",
   "Id":"1",
   "RegionId":"cn-hangzhou",
   "PayType":"Postpaid",
   "ConnectionStr":"jdbc:mysql://localhost:3306/mydb?user=root&password=123456",
   "ExpireTime":"2018-08-24T09:55:41Z",
   "JobId":"72dcd26b-f12d-4c27-b3af-18f6aed5****",
   "DbType":"MySQL",
   "Name":"test"
  }
 ],
 "TotalPages":1,
 "Success":true
}
```

<a id="section-1-7-8"></a>

### 1.7.8. ConfigureDuplicaitonBackupPlan

Configures a database replication backup schedule.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Bid | Strin g | Query | Yes | 26842 | The business ID. |
| Database Type | Strin g | Query | Yes | MySQL | The type of the database. Valid values:<br>• MySQL<br>• Oracle<br>• PostgreSQL<br>• SQLServer |
| StorageRe gion | Strin g | Query | Yes | cn-hangzhou | The storage region.<br><em>This parameter is</em> <em>required if you set</em> <strong><em>PayType</em></strong> <em> to</em> <strong><em>postpay</em></strong><em>.</em> |
| Database Region | Strin g | Query | Yes | cn-hangzhou | The region of the database.<br><em>This parameter is</em> <em>required if you set</em> <strong><em>PayType</em></strong> <em> to</em> <strong><em>postpay</em></strong><em>.</em> |
| BackupPla nName | Strin g | Query | Yes | dbstooi0\*\*\*\*\*\*\* | The name of the backup schedule. |
| SourceEn dpointInst anceID | Strin g | Query | Yes | rm-bp1imrtn6fq7h\*\*\*\* | The ID of the database instance. You can call the DescribeBackupPlanList operation to obtain the value of this parameter.<br><em>This parameter is</em> <em>required if</em> <strong><em>SourceEndpoint</em></strong><em>.</em><strong><em>InstanceType</em></strong> <em>is set to </em><strong><em>RDS</em></strong><em>,</em> <strong><em>ECS</em></strong><em>, </em><strong><em>DDS</em></strong><em>, or</em> <strong><em>Express</em></strong><em>.</em> |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| Resource OwnerId | Long | Query | Yes | 345678912345 | A system parameter for authentication. Do not specify this parameter. |

**Returned data**

| Parameter Name | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The request ID. |
| Success | Boolean | true | The returned status.<br>• The operation was successful.<br>• The operation did not fail. |
| Message | String | success | Additional information. |
| BackupPlanId | String | dbs1h\*\*\*\*usfa | The ID of the backup schedule. |

**Examples**

Request example

```text
http(s)://[Endpoint]/?Action=ConfigureDuplicationBackupPlan
&Bid=26842
&DatabaseType=MySQL
&StorageRegion=cn-hangzhou
&DatabaseRegion=cn-hangzhou
&BackupPlanName=dbstooi0*******
&SourceEndpointInstanceID=rm-bp1imrtn6fq7h****
&ResourceOwnerId=345678912345
&<Common request parameters>
```

Response example

`JSON`  format

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "BackupPlanId":"dbs1h****usfa",
 "Success":true
}
```

<a id="section-1-7-9"></a>

### 1.7.9. CheckResource

Checks the availability and status of resources in Database Backup.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
| --- | --- | --- | --- | --- | --- |
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the operation. |
| Pk | Strin g | Query | Yes | 259258662544\*\*\*\*\*\* | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | The bid. |
| Hid | Long | Query | Yes | 1001 | The unique identification number. |
| Country | Strin g | Query | Yes | CN | The country. Default value: CN. |
| TaskIdenti fier | Strin g | Query | Yes | 001 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retry_count": 3, "timeout": 60} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | \*\*\*\*\* | If the request is successful, this parameter is empty. If the request fails, an error message is returned. |
| Level | Long | Query | No | 1 | The level. |
| Url | Strin g | Query | No | https://img.alicdn.com/tf s/TB1Wo7eXAvoK1RjSZF DXXXY3pXa-2512-3509.jpg | • Specify either this parameter or the body parameter. Do not specify both or leave both empty.<br>• The image URL. The URL cannot exceed 2,048 characters in length and cannot be a Base64-encoded string. |
| Prompt | Strin g | Query | No | I do not understand what you mean. Please say it again. | The prompt message. |

**Response parameters**

| Parameter name | Type | Example | Description |
| --- | --- | --- | --- |
| Interrupt | Boolean | false | Indicates whether the task is interrupted. |
| Invoker | String | admin | The invoker of the operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | The request ID. |
| Hid | Long | 123456 | The unique identification number. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | USER_LOGIN | The task identifier. |
| TaskExtraData | String | {"retry_count": 3, "timeout": 300} | The extra data for the task. |
| GmtWakeup | String | 08:00 | The wakeup time. |
| Success | Boolean | true | Returns the status.<br>• The operation was successful.<br>• failed: false |
| Message | String | success | The additional information. |
| Level | Long | 0 | The level. Valid values include FATAL, ERROR, WARNING, and CRITICAL. |
| Url | String | http://temp-testbucket.oss-cn-shanghai.aliyuncs.com/aivideocensor/\*\*\*\*.jpg | The URL of the video screenshot. |
| Prompt | String | OK | The prompt message. |

**Examples**

Request example

```text
http(s)://[Endpoint]/?Action=CheckResource
&Invoker=admin
&Pk=259258662544******
&Bid=26842
&Hid=1001
&Country=CN
&TaskIdentifier=001
&TaskExtraData={"retry_count": 3, "timeout": 60}
&GmtWakeup=
&<Common request parameters>
```

Successful response example

`JSON`  format

```json
{
 "GmtWakeup":"08:00",
 "Hid":"",
 "TaskIdentifier":"USER_LOGIN",
 "Message":"success",
 "Interrupt":false,
 "Success":true,
 "Url":"http://temp-testbucket.oss-cn-shanghai.aliyuncs.com/aivideocensor/****.jpg",
 "Invoker":"admin",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 300}",
 "Country":"China",
 "Level":0,
 "Prompt":"OK",
 "Pk":"1728240534507590",
 "Bid":"26842"
}
```

<a id="section-2"></a>

# 2.SDK reference

<a id="section-2-1"></a>

## 2.1. SDK overview

**Latest SDK version**

1.0.13

**Supported languages**

- PHP

  - Composer: https://packagist.org/packages/alibabacloud/sdk

  - Code of DBS SDK for PHP: https://github.com/aliyun/openapi-sdk-php

- Python

  - PyPI: https://pypi.org/project/aliyun-python-sdk-dbs/

  - Code of DBS SDK for Python: https://github.com/aliyun/aliyun-openapi-python-sdk

- Java

  - Maven: https://oss.sonatype.org/#nexus-search;quick~aliyun-java-sdk-dbs

  - Code of DBS SDK for Java: https://github.com/aliyun/aliyun-openapi-java-sdk

- C++

  Code of DBS SDK for C++: https://github.com/aliyun/aliyun-openapi-cpp-sdk

- Go

  Code of DBS SDK for Go: https://github.com/aliyun/aliyun-openapi-java-sdk

- C#

  - Nuget: https://www.nuget.org/packages/aliyun-net-sdk-dbs/

  - Code of DBS SDK for C#: https://github.com/aliyun/aliyun-openapi-java-sdk

<a id="section-2-2"></a>

## 2.2. Use DBS SDK for Java based on Maven dependencies

Database Backup (DBS) SDK for Java includes two core kits: aliyun-java-sdk-core and aliyun-java-sdk-dbs. The aliyun-java-sdk-core kit automatically routes requests to the DBS endpoint. The aliyun-java-sdk-dbs kit consists of related classes of all DBS features. You can use the latest versions of the two kits in the current Maven repository.

**Maven configuration**

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dbs</artifactId>
    <version>1.0.11</version>
</dependency>
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.4.0</version>
</dependency>
```

**Initialize a client**

```text
// Use the profile to declare the AccessKey ID, AccessKey secret, and the region of the
DBS backup schedule.
IClientProfile profile = DefaultProfile.getProfile("cn-hangzhou", "accsessKeyId", "accessSecret");
// Use the profile to initialize a client object.
IAcsClient client = new DefaultAcsClient(profile);
```

**Example of calling the CreateBackupPlan operation**

```text
// Declare a request object.
CreateBackupPlanRequest req = new CreateBackupPlanRequest();
// Configure the request parameters. For example, to call the CreateBackupPlan operation, you must configure the Region, DatabaseType, 
InstanceClass, BackupMethod, Period, and UsedTime parameters.
req.setRegion("cn-hangzhou");
req.setDatabaseType("MySQL");
req.setInstanceClass("small");
req.setBackupMethod("logical");
req.setPeriod("Month");
req.setUsedTime(1);
// Receive the response to the request by using the client.
CreateBackupPlanResponse response = client.getAcsResponse(req);
// Call the GET method in the response to retrieve the returned parameter values, such as the backup schedule ID.
String backupPlanId=response.getBackupPlanId();
```

<a id="section-2-3"></a>

## 2.3. Obtains an AccessKey pair

You can obtain the AccessKey pair on the Apsara Stack console.

**Obtain an AccessKey pair of a department**

Follow these steps:

1. Log on to the Apsara Stack console as an administrator.

2. In the top navigation bar, click the <img src="assets/97a46dd0885358a10097e085ed2f2e9f.png" width="24" alt=""> icon, and then choose **User Center > Department**

   **Management**.

3. Select a department and click **Create AccessKey** to obtain an AccessKey pair of this department.

   > **Note**
   >
   > The AccessKey pair is automatically allocated to a level-1 department. The
   >
   > sub-departments use the same AccessKey pair as their level-1 department.

**Obtain an AccessKey pair of a personal account**

Follow these steps:

1. Log on to the Apsara Stack console as an administrator.

2. In the upper-right corner of the Web page, click your avatar and select **Personal Information**.

   The system displays your AccessKey ID.

3. Click **Show** under **AccessKey Secret** to view the AccessKey Secret.
