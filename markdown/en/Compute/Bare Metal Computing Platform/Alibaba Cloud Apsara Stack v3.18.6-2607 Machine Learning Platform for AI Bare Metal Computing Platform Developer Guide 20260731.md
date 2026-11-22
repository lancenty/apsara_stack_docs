Alibaba Cloud  
Apsara Stack  
Machine Learning Platform for  
AI  
Bare Metal Computing  
Platform Developer Guide  
Product Version: v3.18.6-2607  
Document Version: 20260731

**Table of Contents**

- [1.Development overview](#section-1)
- [2.Preparations](#section-2)
- [3.Obtain an AccessKey](#section-3)
- [4.Call API operations by using generic calls](#section-4)
- [5.API reference](#section-5)
    - [5.1. Cluster management](#section-5-1)
        - [5.1.1. Bare metal - intelligent computing cluster](#section-5-1-1)
            - [5.1.1.1. CreateBmcpCluster](#section-5-1-1-1)
            - [5.1.1.2. ListBmcpMachineType](#section-5-1-1-2)
            - [5.1.1.3. ListBmcpCluster](#section-5-1-1-3)
            - [5.1.1.4. DescribeBmcpCluster](#section-5-1-1-4)
            - [5.1.1.5. AddBmcpClusterInstances](#section-5-1-1-5)
            - [5.1.1.6. ListAvailableBmcpInstance](#section-5-1-1-6)
            - [5.1.1.7. DeleteBmcpClusterInstances](#section-5-1-1-7)
            - [5.1.1.8. DeleteBmcpCluster](#section-5-1-1-8)
        - [5.1.2. ACK - intelligent computing cluster](#section-5-1-2)
            - [5.1.2.1. CreateAckCluster](#section-5-1-2-1)
            - [5.1.2.2. ListAckCluster](#section-5-1-2-2)
            - [5.1.2.3. DescribeAckCluster](#section-5-1-2-3)
            - [5.1.2.4. AddAckClusterInstances](#section-5-1-2-4)
            - [5.1.2.5. ListAckClusterInstances](#section-5-1-2-5)
            - [5.1.2.6. ListAckClusterNodePool](#section-5-1-2-6)
            - [5.1.2.7. DeleteAckClusterInstances](#section-5-1-2-7)
            - [5.1.2.8. ModifyAckClusterDeletionProtection](#section-5-1-2-8)
            - [5.1.2.9. ListAckInstanceType](#section-5-1-2-9)
            - [5.1.2.10. ListApps](#section-5-1-2-10)
            - [5.1.2.11. DescribeApp](#section-5-1-2-11)
            - [5.1.2.12. GetOssStsToken](#section-5-1-2-12)
            - [5.1.2.13. UploadCustomApp](#section-5-1-2-13)
            - [5.1.2.14. ListCustomApps](#section-5-1-2-14)
            - [5.1.2.15. DescribeCustomApp](#section-5-1-2-15)
            - [5.1.2.16. DeleteCustomApp](#section-5-1-2-16)
            - [5.1.2.17. InstallAiInstanceResource](#section-5-1-2-17)
            - [5.1.2.18. UnInstallAiInstanceResource](#section-5-1-2-18)
            - [5.1.2.19. InstallAiApplication](#section-5-1-2-19)
            - [5.1.2.20. UpgradeAiApplication](#section-5-1-2-20)
            - [5.1.2.21. UnInstallAiApplication](#section-5-1-2-21)
            - [5.1.2.22. ListInstanceTypeDiskCategory](#section-5-1-2-22)
            - [5.1.2.23. ListAckClusterEcsWorkerInstances](#section-5-1-2-23)
            - [5.1.2.24. DescribeAckClusterLogs](#section-5-1-2-24)
            - [5.1.2.25. GetClusterNamespaces](#section-5-1-2-25)
            - [5.1.2.26. ListHistoryEvent](#section-5-1-2-26)
            - [5.1.2.27. ListReStartEvent](#section-5-1-2-27)
            - [5.1.2.28. DeleteAckCluster](#section-5-1-2-28)
        - [5.1.3. Bare metal – supercomputing cluster](#section-5-1-3)
            - [5.1.3.1. CreateEhpcCluster](#section-5-1-3-1)
            - [5.1.3.2. ListEhpcCluster](#section-5-1-3-2)
            - [5.1.3.3. DescribeEhpcCluster](#section-5-1-3-3)
            - [5.1.3.4. AddEhpcClusterInstances](#section-5-1-3-4)
            - [5.1.3.5. DeleteEhpcClusterInstances](#section-5-1-3-5)
            - [5.1.3.6. DeleteEhpcCluster](#section-5-1-3-6)
        - [5.1.4. Converged computing cluster](#section-5-1-4)
            - [5.1.4.1. CreateBFICluster](#section-5-1-4-1)
            - [5.1.4.2. ListBFICluster](#section-5-1-4-2)
            - [5.1.4.3. DescribeBFICluster](#section-5-1-4-3)
            - [5.1.4.4. ExpandBFICluster](#section-5-1-4-4)
            - [5.1.4.5. ShrinkBFICluster](#section-5-1-4-5)
            - [5.1.4.6. DeleteBFICluster](#section-5-1-4-6)
        - [5.1.5. ListInstance](#section-5-1-5)
        - [5.1.6. GetVswitchSwitchMethod](#section-5-1-6)
        - [5.1.7. ClusterDryRun](#section-5-1-7)
        - [5.1.8. TagResources](#section-5-1-8)
        - [5.1.9. RetryFailedInstance](#section-5-1-9)
    - [5.2. Storage management](#section-5-2)
        - [5.2.1. CreateCpfsClientCluster](#section-5-2-1)
        - [5.2.2. DescribeCpfsClientClusterType](#section-5-2-2)
        - [5.2.3. MountFilesystem](#section-5-2-3)
        - [5.2.4. UnmountFilesystem](#section-5-2-4)
        - [5.2.5. DeleteCpfsClientCluster](#section-5-2-5)
    - [5.3. EVPC](#section-5-3)
        - [5.3.1. CreateEvpc](#section-5-3-1)
        - [5.3.2. ListEvpc](#section-5-3-2)
        - [5.3.3. ListEvpcConnections](#section-5-3-3)
        - [5.3.4. ModifyEvpc](#section-5-3-4)
        - [5.3.5. DeleteEvpc](#section-5-3-5)
    - [5.4. Security group](#section-5-4)
        - [5.4.1. CreateSecurityGroup](#section-5-4-1)
        - [5.4.2. ListSecurityGroup](#section-5-4-2)
        - [5.4.3. ModifySecurityGroup](#section-5-4-3)
        - [5.4.4. DeleteSecurityGroup](#section-5-4-4)
        - [5.4.5. AddSecurityGroupRule](#section-5-4-5)
        - [5.4.6. ListSecurityGroupRule](#section-5-4-6)
        - [5.4.7. ModifySecurityGroupRule](#section-5-4-7)
        - [5.4.8. DeleteSecurityGroupRule](#section-5-4-8)
        - [5.4.9. AddSecurityGroupInstance](#section-5-4-9)
        - [5.4.10. ListSecurityGroupInstance](#section-5-4-10)
        - [5.4.11. DeleteSecurityGroupInstance](#section-5-4-11)
    - [5.5. Key pair](#section-5-5)
        - [5.5.1. CreateKeyPair](#section-5-5-1)
        - [5.5.2. ListKeyPair](#section-5-5-2)
        - [5.5.3. ConfigKeyPair](#section-5-5-3)
        - [5.5.4. UnbindKeyPair](#section-5-5-4)
        - [5.5.5. DeleteKeyPair](#section-5-5-5)
    - [5.6. Elastic cache acceleration](#section-5-6)
        - [5.6.1. CreateEdaCluster](#section-5-6-1)
        - [5.6.2. DeleteEdaCluster](#section-5-6-2)
    - [5.7. Data distribution](#section-5-7)
        - [5.7.1. ListMP2pTask](#section-5-7-1)
        - [5.7.2. CreateMP2pTask](#section-5-7-2)
        - [5.7.3. DeleteMP2pTask](#section-5-7-3)
    - [5.8. Node management](#section-5-8)
        - [5.8.1. DiagnoseQuery](#section-5-8-1)
        - [5.8.2. TaskQuery](#section-5-8-2)
        - [5.8.3. DiagnosePoint](#section-5-8-3)
    - [5.9. Auto-healing event tickets](#section-5-9)
        - [5.9.1. ListOrder](#section-5-9-1)
        - [5.9.2. GetOrderDetail](#section-5-9-2)
        - [5.9.3. UpdateOrder](#section-5-9-3)
    - [5.10. Recycle bin](#section-5-10)
        - [5.10.1. ListRecycleBMCPMachine](#section-5-10-1)
        - [5.10.2. RevertMachine](#section-5-10-2)
        - [5.10.3. ReleaseMachine](#section-5-10-3)

<a id="section-1"></a>

# 1.Development overview

Before you use Bare Metal Computing Platform (BMCP) features, you must understand the productservice names and API versions that are required for different features, as well as the complete workflow. This helps you correctly integrate with and call BMCP.

**Feature call description**

Before you use BMCP API operations to implement a specific feature, you must understand the differences in service names and API versions that are required to call the API operations of different BMCP features.

| ProductService name | API version |
| --- | --- |
| EasyAI | 2023-11-01 |

**Workflow**

![](en-bare-metal-computing-developer-guide-v3.18.6-2607-20260731.assets/5092402f5a4e4b856bf3b6ce9cfd602d.png)

**Make an API call**

Call the API by

SDK

The following table describes the call workflow.

<table>
  <tr>
    <th>Stage</th>
    <th>Operatio n</th>
    <th>Description</th>
  </tr>
  <tr>
    <td rowspan="3">Preparatio ns</td>
    <td>Obtain an AccessKe y</td>
    <td>When you call a cloud service API operation, you must provide multiple header parameters, including x-acs-regionid (the region ID), x-acs-organizationid (the organization ID), x-acs-resourcegroupid (the resource group ID), and x-acs-instanceid (the cloud service resource ID).</td>
  </tr>
  <tr>
    <td>Obtain an AccessKe y</td>
    <td>When you call a BMCP API operation, you must use the endpoint of the BMCP business domain. You can obtain the endpoint from an Alibaba Cloud on-site O&amp;M engineer or obtain it by yourself.</td>
  </tr>
  <tr>
    <td>Obtain an AccessKe y</td>
    <td>Obtain an AccessKey, configure the access credentials as environment variables. Configuring access credentials as environment variables prevents sensitive information from being hardcoded in your code and improves security.</td>
  </tr>
  <tr>
    <td>Formal call</td>
    <td>Call API operation s by using generic calls</td>
    <td>Call RPC-style API operations by using generic calls.</td>
  </tr>
</table>

<a id="section-2"></a>

# 2.Preparations

Before you use an SDK to call Bare Metal Computing Platform (BMCP) API operations, you must obtain the access credentials, common headers, and endpoint.

**Obtain common header parameters**

When you call an Apsara Stack API operation, you must provide multiple header parameters. The following table describes the common header parameters.

**Descriptio**

**Name**

**Example**

**How to obtain**

**n**

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose

**x-acs-**

The ID of

cn-\*\*\*\*\*\*\*\*-d01

**Resource Management** > **Region**

**regionid**

the region.

**Management**.

4. Click the name of the target organization.

5. View the region ID in the **Region List** section on the right.

The ID of the

**x-acs-**

org-

organization

**organizatio**

10385eca88860a

to which the

**nid**

d8\*\*\*\*\*\*\*\*

> **Important**

resource belongs.

> You must obtain these parameters if you use a personal AccessKey pair. You do not need to obtain them if you use an organization AccessKey pair.

1. Log on to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

The ID of

3. In the left-side navigation pane, choose

the resource

**Resource Management** > **Organization**

**x-acs-**

rs-

group to

**Management**.

**resourcegr**

10385eca8c100a

which the

**oupid**

bc\*\*\*\*\*\*\*\*

resource

4. Click the name of the target organization and

belongs.

view the organization ID in the **Basic Information** section.

5. On the **Resource Group List** tab, view the resource group ID in the **Resource Group Name/ID** column.

You can also obtain the organization ID and resource group ID by calling API operations. For more information, see the *GetOrganizationList and ListResourceGroup* topics in *Apsara Uni-manager Development Guide*.

<table>
  <tr>
    <td>x-acs-instanceid</td>
    <td>The ID of the resource on which you want to perform the operation.</td>
    <td>bmcp-bpnopt****</td>
    <td>You can obtain the resource ID from the cloud service instance list in the Apsara Uni-manager Management Console.<br>1. Log on to the Apsara Uni-manager Management Console.<br>2. In the top navigation bar, choose <strong>Products</strong> &gt; Computing &gt; Bare Metal Computing <strong>Platform (BMCP)</strong>.<br>3. In the left-side navigation pane, click <strong>Cluster</strong> <strong>Management</strong> and <strong>Node Management</strong>.<br>4. View the resource ID, such as a cluster ID or a node ID, in the corresponding resource list.</td>
  </tr>
</table>

> **Note**
>
> For cloud service resource instance API operations that return lists, the response includes the ResourceGroupName (the resource group name), ResourceGroup (the resource group ID), DepartmentName (the organization name), and Department (the organization ID) parameters by default.

**Obtain the endpoint**

1. Log on to the Apsara Uni-manager Operations Console.

2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure Management > O&M Tools**.

3. On the **Service Registration Variable Dashboard** page, obtain the endpoint of the required service based on the feature that you want to use.

   <ol type="i">

   <li>

   Select **Service** and enter **easyAIControllerService**.

   </li>

   <li>

   In the **Service Registration** column of the **easyAIControllerService** service, click the

   </li>

   </ol>

   <img src="en-bare-metal-computing-developer-guide-v3.18.6-2607-20260731.assets/9a918ed188405c606c39c2fc9194550b.jpeg" width="24" alt=""> icon, and then click the displayed information.

   <ol type="i" start="3">

   <li>

   In the **Registration Variables** dialog box, view the value of **EasyAIPopDomain**, which

   </li>

   </ol>

   is the  `Endpoint` .

**Configure access credentials**

Obtain an AccessKey, configure the access credentials as environment variables. This section uses an AccessKey pair as an example.

| Method | Variable name | Description |
| --- | --- | --- |
| Use an AccessKey pair | ALIBABA_CLOUD_ACCESS_KEY _ID and ALIBABA_CLOUD_ACCESS_KEY _SECRET | Use a personal AccessKey pair or an organization AccessKey pair. |
| Use Security Token Service (STS) temporary access credentials | ALIBABA_CLOUD_ACCESS_KEY _ID, ALIBABA_CLOUD_ACCESS_KEY _SECRET, and ALIBABA_CLOUD_SESSION_TO KEN | An AccessKey ID obtained from STS starts with STS, for example, <code> STS.**************** </code>.Use the temporary identity credentials that are obtained from STS, which include an AccessKey ID, an AccessKey secret, and a security token. |

> **Important**
>
> After the configuration is complete, restart or refresh the build and runtime environment, including the IDE, command-line interface, other desktop applications, and background services, to ensure that the latest system environment variables are loaded.

**Linux**

1. Run the following command in the command-line interface to append the environment variable settings to the  `~/.bashrc`  file.

   ```bash
   echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
   echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
   ```

2. Run the following command to apply the changes.

   ```text
   source ~/.bashrc
   ```

3. Run the following command to check whether the environment variables take effect.

   ```bash
   echo $ALIBABA_CLOUD_ACCESS_KEY_ID
   echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
   ```

**macOS**

1. Run the following command in the terminal to view the default shell type.

   ```bash
   echo $SHELL
   ```

2. Perform operations based on the default shell type.

   **Zsh**

   <ol type="i">

   <li>

   Run the following command to append the environment variable settings to the  `~/.zshrc`  file.

   ```bash
   echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc
   echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
   ```

   </li>

   <li>

   Run the following command to apply the changes.

   ```text
   source ~/.zshrc
   ```

   </li>

   <li>

   Run the following command to check whether the environment variables take effect.

   ```bash
   echo $ALIBABA_CLOUD_ACCESS_KEY_ID
   echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
   ```

   </li>

   </ol>

   **Bash**

   <ol type="i">

   <li>

   Run the following command to append the environment variable settings to the  `~/.bash_profile`  file.

   ```bash
   echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile
   echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
   ```

   </li>

   <li>

   Run the following command to apply the changes.

   ```text
   source ~/.bash_profile
   ```

   </li>

   <li>

   Run the following command to check whether the environment variables take effect.

   ```bash
   echo $ALIBABA_CLOUD_ACCESS_KEY_ID
   echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
   ```

   </li>

   </ol>

**Windows**

**CMD**

1. Run the following command in CMD.

   ```text
   setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
   setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
   ```

2. Run the following command to check whether the environment variables take effect.

   ```bash
   echo %ALIBABA_CLOUD_ACCESS_KEY_ID%
   echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
   ```

**PowerShell**

1. Run the following command in PowerShell.

   ```text
   [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", 
   "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
   [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", 
   "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
   ```

2. Run the following command to check whether the environment variables take effect.

   ```text
   [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", 
   [EnvironmentVariableTarget]::User)
   [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", 
   [EnvironmentVariableTarget]::User)
   ```

<a id="section-3"></a>

# 3.Obtain an AccessKey

If your application is deployed and runs in a highly secure and stable environment isolated from external attacks, requires long-term access to the service, and requires infrequent credential rotation, you can use an AccessKey pair (consisting of an AccessKey ID and an AccessKey Secret) to initialize the credential provider.

**Background information**

> **Warning**
>
> The AccessKey pair of a personal account is a restricted AccessKey pair that is managed by the permission system of the Apsara Uni-manager Management Console. In contrast, an organization AccessKey pair has broader permissions, and administrators must verify the security of the operations.

The Apsara Uni-manager Management Console provides both personal and organization AccessKey pairs. (Note that only operations administrators and first-level organization administrators can obtain an organization AccessKey pair.) We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and related cloud services.

> **Note**
>
> If you use the AccessKey pair of a personal account, you must add the following parameters to the request header: x-acs-regionid (the region ID), x-acs-organizationid (the organization ID), x-acs-resourcegroupid (the resource group ID), and x-acs-instanceid (the cloud service resource ID). For specific operations, see the preparations topic of each service.

**Obtain the AccessKey pair of a personal account**

1. Log in to the Apsara Uni-manager Management Console.

2. In the upper-right corner of the console, click the profile picture of the current user and then click **User Information**.

3. In the **AccessKey** section, view the AccessKey information of your personal account.

   > **Note**
   >
   > The AccessKey ID and AccessKey Secret are the credentials that you use to access cloud resources. They grant full permissions of the account. Keep them secure.

**Obtain an organization AccessKey pair**

1. Log in to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprises**.

3. In the left-side navigation pane, choose **Resources > Organizations**.

4. In the organization structure, click the name of the target first-level organization.

5. Click **Manage AccessKey Pairs**.

6. In the dialog box that appears, view the organization AccessKey information.

<a id="section-4"></a>

# 4.Call API operations by using generic calls

Bare Metal Computing Platform (BMCP) API operations do not provide SDKs. As an alternative, you can use generic calls. This topic illustrates how to call Remote Procedure Call (RPC)-style API operations via generic calls, with sample code provided for various programming languages.

**Background information**

Generic calls that allow you to call any API operation have the following benefits:

- Lightweight: You need to install only the Alibaba Cloud core SDK, without the need for individual cloud service SDKs.

- Simple: You need to construct only a generic request parameter object and then use a generic request client to call a generic function to initiate the request. The response is also returned in a generic format.

To initiate a generic call, you must obtain the values of the following parameters from the API reference of the corresponding service:

- domain: the service endpoint

- version: the version of the API operation, in the YYYY-MM-DD format. For BMCP, the product name is EasyAI and the API version is 2023-11-01.

- Operation information: the name of the operation that you want to call. You must obtain the `Action`  parameter and specify the API name in the request.

  For example, to call the  `DescribeBmcpCluster`  operation by using the Java SDK, use  `setAction("DescribeBmcpCluster")`  to specify the API name.

> **Note**
>
> Replace the variables in the sample code in this topic with actual values. Do not retain the angle brackets (<>) in your final code.

**Java example**

**Install the core SDK**

Add the following dependency to the pom.xml file to install the core SDK.

```xml
<dependency>
     <groupId>com.aliyun</groupId>
     <artifactId>aliyun-java-sdk-core</artifactId>
     // You can select a version.
     <version>[(4.0.0,5.0.0)]</version>
</dependency>
```

**Complete example**

The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace  `<your_region_id>`  with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace  `<bmcpDomain>`  with the endpoint of BMCP<strong>.</strong> Configure the other variables as needed.

```java
import com.aliyuncs.CommonRequest;
import com.aliyuncs.CommonResponse;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.profile.DefaultProfile;
public class Sample {
  public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    DefaultProfile profile = DefaultProfile.getProfile(
      // Your region ID.
      "<your-region-id>",
      // Obtain the AccessKey ID of the RAM user from an environment variable.
      System.getenv("AccessKey"),
      // Obtain the AccessKey secret of the RAM user from an environment variable.
      System.getenv("AccessKeySecret"));
    IAcsClient client = new DefaultAcsClient(profile);
    // Create an API request and set the parameters.
    CommonRequest request = new CommonRequest();
    request.setSysDomain("<bmcpDomain>");
    request.setSysProduct("EasyAI");
    request.setSysVersion("2023-11-01");
    request.setSysAction("DescribeBmcpCluster");
    request.setSysMethod(MethodType.POST);
    request.setProtocol(com.aliyuncs.http.ProtocolType.HTTP);
    request.putQueryParameter("ClusterId", "bmcp-bpnopt****");
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

**Python example**

**Install the core SDK**

Run the following command in the terminal to install the core SDK.

```bash
pip install aliyun-python-sdk-core
```

**Complete example**

The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace  `<your_region_id>`  with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace  `<bmcpDomain>`  with the endpoint of BMCP<strong>.</strong> Configure the other variable parameters as needed.

```python
# coding=utf-8

import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class Sample:

    @staticmethod
    def main():
        region_id = "<your_region_id>"
        bmcp_domain = "<bmcpDomain>"
        cluster_id = "bmcp-bpnopt****"

        client = AcsClient(
            os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"],
            os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"],
            region_id,
            verify=False
        )

        request = CommonRequest()
        request.set_domain(bmcp_domain)
        request.set_product("EasyAI")
        request.set_version("2023-11-01")
        request.set_action_name("DescribeBmcpCluster")
        request.set_method("POST")
        request.set_protocol_type("HTTP")

        request.add_body_params("ClusterId", cluster_id)

        response = client.do_action_with_exception(request)
        print(response.decode("utf-8"))


if __name__ == "__main__":
    Sample.main()
```

**Go example**

**Install the core SDK**

Run the following command in the terminal to install the core SDK.

```text
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Complete example**

The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace  `<your_region_id>`  with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace  `<bmcpDomain>`  with the endpoint of BMCP<strong>.</strong> Configure the other variable parameters as needed.

```go
package main

import (
 "fmt"
 "os"

 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
)

func main() {
 RegionId := "<your_region_id>"
 bmcpDomain := "<bmcpDomain>"

 client, err := sdk.NewClientWithAccessKey(
  RegionId,
  os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
  os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
 )
 if err != nil {
  panic(err)
 }

 request := requests.NewCommonRequest()
 request.Domain = bmcpDomain
 request.Product = "EasyAI"
 request.Version = "2023-11-01"
 request.ApiName = "DescribeBmcpCluster"
 request.Method = "POST"
 request.Scheme = "http"

 request.QueryParams["ClusterId"] = "bmcp-bpnopt****"

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

## 5.1. Cluster management

<a id="section-5-1-1"></a>

### 5.1.1. Bare metal - intelligent computing cluster

<a id="section-5-1-1-1"></a>

#### 5.1.1.1. CreateBmcpCluster

Create a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The cluster name. The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The cluster description.The description must be 0 to 1000 characters in length. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The login password of the machines in the cluster.<br>The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.Supported special characters: ()\`~!@#$%^&amp;\*-_+=\|{} \[\]:;'&lt;&gt;,.?/. |
| AddBmsIns tanceList | Json | Quer y | No | null | This parameter is deprecated. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | \[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\*", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\*" } \] | The list of parameters for requesting bare metal servers.<br>This parameter is required when ClusterArchType is set to managed. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the available zone. |

<table>
  <tr>
    <td>ClusterArc hType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>standard</td>
    <td>The cluster type. Valid values:<br>• standard: Intelligent computing high-bandwidth network<br>• managed: Managed intelligent computing<br>• base: Basic intelligent computing<br>• aspeed: Intelligent computing training and inference</td>
  </tr>
  <tr>
    <td>MachineTy peList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq****"} ]</td>
    <td>The list of bare metal server types to be added to the supercomputing cluster.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>VswitchIdL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>StandardV switchId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>vsw-3gagdup8scary04iq****</td>
    <td>The ID of the vSwitch, used to build the management and control service network channel.</td>
  </tr>
  <tr>
    <td>EvpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>evpc-htchvitxlfjyso****</td>
    <td>The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard or aspeed.<br>You can call the ListEvpc operation to query the EVPC ID.</td>
  </tr>
  <tr>
    <td>VolumeId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>MountPath</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>ActivationI d</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>4ECEEE12-56F1-4FBC-9AB1-890F1234****</td>
    <td>The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>Activation Code</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>a-hz0ch3SwhOlE1234+Xo3 2lAZC****</td>
    <td>The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>IsCreateCp fsCluster</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable the high-performance storage client cluster. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.<br>This parameter is optional when ClusterArchType is set to standard or aspeed.</td>
  </tr>
  <tr>
    <td>CpfsCluste rType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>CPFS</td>
    <td>The type of the high-performance storage client cluster. Valid values:<br>• CPFS<br>• APFS<br>This parameter is required when IsCreateCpfsCluster is set to true.</td>
  </tr>
</table>

<table>
  <tr>
    <td>VolumeInf o</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023-04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, {"VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, {"VolumeType": "mount", "VolumeParams": {"Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ]</td>
    <td>The third-party storage mount information.<br>This parameter is optional when ClusterArchType is set to managed.</td>
  </tr>
  <tr>
    <td>IsInstallYu ndunAegis</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable Aegis. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>SwitchMet hod</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>CHSW</td>
    <td>The networking mode of the vSwitch.<br>• When ClusterArchType is set to standard, base, or aspeed, this parameter must be set to CHSW.<br>• When ClusterArchType is set to managed, this parameter can be set to CHSW or HSW.</td>
  </tr>
  <tr>
    <td>EnableIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable IPv6. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>EvpcEnabl eIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable EVPC IPv6.<br>IPv6 can be enabled only when EvpcId is specified.Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp-bpnopt\*\*\*\*" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateBmcpCluster
http://[Endpoint]/?Action=CreateEhpcCluster
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-env***-d01
&ZoneId=cn-wulan-env***-****-a
&VpcId=vpc-bp1b1xjllp3ve5yze****
&ClusterName=cluster-name
&ClusterArchType=standard
&MachineTypeList=[
 {
 "MachineType": "test",
 "Arch": "x86",
 "CpuCount": 2,
 "MemCount": 4,
 "FlopsCount": 4.8,
 "VideoMemCount": 5,
 "NodeCount": 10,
 "VswitchId": "vsw-3gagdup8scary04iq****"
 }
]
&StandardVswitchId=vsw-3gagdup8scary04iq****
&EvpcId=evpc-htchvitxlfjyso****
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&IsCreateCpfsCluster=true
&CpfsClusterType=CPFS
&SwitchMethod=CHSW
&EnableIpv6=true
&EvpcEnableIpv6=true
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-2"></a>

#### 5.1.1.2. ListBmcpMachineType

Query the list of Bare Metal Computing Platform (BMCP) machine types.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| MachineTy pe | Strin g | Quer y | No | QPG78P4M8G3V.03BB | The machine type name. |
| CPUArch | Strin g | Quer y | No | x86_64 | The CPU architecture.Valid values:<br>• x86_64<br>• arm64 |
| DiskType | Strin g | Quer y | No | cloud_ssd | The disk type. Valid values:<br>• HDD<br>• SSD<br>• SATA |
| Manufactu rer | Strin g | Quer y | No | NVIDIA | The manufacturer name. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the zone.<br>• If this parameter is specified, the number of available standard instances in the specified zone is counted.<br>• If this parameter is not specified, the number of available standard instances across all zones for this machine type is counted. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| DeployTyp es | Json | Quer y | No | "\["bmcp"\]" | The list of machine type categories to query. Valid values:<br>• bmcp: intelligent computing with high-bandwidth networking<br>• ehpc: High-Performance Computing (HPC) with high-bandwidth networking<br>• base: intelligent computing basic<br>• aspeed: training and inference optimization<br>• bfi: converged high-bandwidth networking<br>• bfi_base: converged basic |
| Specificati on | Strin g | Quer y | No | gBMC-Ch4ce8hdr | The machine type specification. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "PageNumber": 1, "PageSize": 10, "TotalCount": 10, "MachineTypeList": \[ { "ratedPower": "1", "memory": 500, "defaultFmin": "", "gpuManufacturer": "NVIDIA", "CPUNumber": 128, "networkCardType": "10G", "unitNum": 2, "description": "", "updateTime": "2024-03-14T10:48:43+08:0 0", "CPUArch": "x86_64", "gpu": "T4", "deployType": "bmcp", "manufacturer": "HW", "networkCardNum": 2, "GpuNum": 4, "disk": 500, "cpuManufacturer": "Hygon", "createTime": "2024-03-14T10:48:43+08:0 0", "name": "T4", "ID": 2, "diskType": "SSD", "CPUModel": "Hygon C86 7285 32-core Processor", "StandardInstance Count": 10, "Specification": "xxxx" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListBmcpMachineType
&MachineType=MachineType
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{},
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data  />
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-3"></a>

#### 5.1.1.3. ListBmcpCluster

Query the list of bare metal - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt\*\*\*\* | The ID of the cluster. |
| Status | Strin g | Quer y | No | active | The cluster status. Valid values:<br>• creating: Creating<br>• active: Running<br>• createFailed: Creation failed<br>• deleting: Deleting<br>• deleteFailed: Deletion failed<br>• scalingDown: Scaling in<br>• scalingDownFailed: Scale-in failed<br>• scalingUp: Scaling out<br>• scalingUpFailed: Scale-out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| Zone | Strin g | Quer y | No | cn-\*\*\*\*-env\*\*-d01-a | The ID of the available zone. |
| ClusterArc hType | Strin g | Quer y | No | standard | The cluster type. Valid values:<br>• standard: Intelligent computing high-bandwidth network<br>• managed: Managed intelligent computing<br>• base: Basic intelligent computing<br>• aspeed: Intelligent computing training and inference. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the Enterprise Virtual Private Cloud (EVPC).<br>You can call the ListEvpc operation to query the EVPC ID. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterList": \[ {"Description": "testDescription", "Organization": "5", "IsSetPassword": true, "SwitchMethod": "CHSW", "CpfsClusterType": "APFS", "Gpu": \[ {"GpuNum": 32, "GpuModel": "NVIDIA_Ampere_A 10_80G_NVLink" }\], "EvpcId": "evpc-pi2q\*\*\*z8b", "EnableIpv6": true, "FlopsCount": 9984, "Department": 5, "CpuCount": 512, "ClusterName": "cluster-name", "ResourceGroup": 4, "Status": "active", "ActiveNodeCount": 4, "NodeCount": 4, "ClusterId": "bmcp-v8\*\*\*QVZT", "Zone": "cn-wulan-env\*\*\*-d01-a", "CreateTime": "2026-01-12T10:44:46+08:0 0", "Specification": \[ { "Count": 3, "Name": "gBMC-Ci8af8nbr" } \], "CpfsClusterState": "active", "AscmCreateUser": "admin", "MemCount": 8192, "ClusterArchType": "standard", "VpcId": "vpc-7kkjbu\*\*\*\*od7pxs6 10", "OldClusterBzid": "", "UpdateTime": "2026-01-22T15:58:01+08:0 0", "Region": "cn-wulan-env\*\*\*-d01", "CpfsMountFs": "efs-01\*\*\*08", "RegionId": "cn-wulan-env\*\*\*-d01", "VideoMemory": 2560, "EnableIpv6": true, "EvpcEnableIpv6": true } \], "PageSize": 10, "TotalCount": 1, "PageNumber": 1 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListBmcpCluster
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-env***-d01
&ZoneId=cn-wulan-env***-****-a
&VpcId=vpc-bp1b1xjllp3ve5yze****
&ClusterName=cluster-name
&Common request parameters&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "ClusterList":[
   {
    "Description":"testDescription",
    "Organization":"5",
    "IsSetPassword":true,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"APFS",
    "Gpu":[
     {
      "GpuNum":32,
      "GpuModel":"NVIDIA_Ampere_A10_80G_NVLink"
     }
    ],
    "EvpcId":"evpc-pi2q***z8b",
    "EnableIpv6":true,
    "FlopsCount":9984,
    "Department":5,
    "CpuCount":512,
    "EvpcEnableIpv6":true,
    "ClusterName":"cluster-name",
    "ResourceGroup":4,
    "Status":"active",
    "ActiveNodeCount":4,
    "NodeCount":4,
    "ClusterId":"bmcp-v8***QVZT",
    "Zone":"cn-wulan-env***-d01-a",
    "CreateTime":"2026-01-12T10:44:46+08:00",
    "Specification":[
     {
      "Count":3,
      "Name":"gBMC-Ci8af8nbr"
     }
    ],
    "CpfsClusterState":"active",
    "AscmCreateUser":"admin",
    "MemCount":8192,
    "ClusterArchType":"standard",
    "VpcId":"vpc-7kkjbu****od7pxs610",
    "OldClusterBzid":"",
    "UpdateTime":"2026-01-22T15:58:01+08:00",
    "Region":"cn-wulan-env***-d01",
    "CpfsMountFs":"efs-01***08",
    "RegionId":"cn-wulan-env***-d01",
    "VideoMemory":2560
   }
  ],
  "PageSize":10,
  "PageNumber":1
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>1</TotalCount>
 <ClusterList>
  <Description>testDescription</Description>
  <Organization>5</Organization>
  <IsSetPassword>true</IsSetPassword>
  <SwitchMethod>CHSW</SwitchMethod>
  <CpfsClusterType>APFS</CpfsClusterType>
  <Gpu>
   <GpuNum>32</GpuNum>
   <GpuModel>NVIDIA_Ampere_A10_80G_NVLink</GpuModel>
  </Gpu>
  <EvpcId>evpc-pi2q***z8b</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <FlopsCount>9984</FlopsCount>
  <Department>5</Department>
  <CpuCount>512</CpuCount>
  <EvpcEnableIpv6>true</EvpcEnableIpv6>
  <ClusterName>cluster-name</ClusterName>
  <ResourceGroup>4</ResourceGroup>
  <Status>active</Status>
  <ActiveNodeCount>4</ActiveNodeCount>
  <NodeCount>4</NodeCount>
  <ClusterId>bmcp-v8***QVZT</ClusterId>
  <Zone>cn-wulan-env***-d01-a</Zone>
  <CreateTime>2026-01-12T10:44:46+08:00</CreateTime>
  <Specification>
   <Count>3</Count>
   <Name>gBMC-Ci8af8nbr</Name>
  </Specification>
  <CpfsClusterState>active</CpfsClusterState>
  <AscmCreateUser>admin</AscmCreateUser>
  <MemCount>8192</MemCount>
  <ClusterArchType>standard</ClusterArchType>
  <VpcId>vpc-7kkjbu****od7pxs610</VpcId>
  <OldClusterBzid />
  <UpdateTime>2026-01-22T15:58:01+08:00</UpdateTime>
  <Region>cn-wulan-env***-d01</Region>
  <CpfsMountFs>efs-01***08</CpfsMountFs>
  <RegionId>cn-wulan-env***-d01</RegionId>
  <VideoMemory>2560</VideoMemory>
 </ClusterList>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-4"></a>

#### 5.1.1.4. DescribeBmcpCluster

Query the details of a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt\*\*\*\* | The ID of the bare metal -intelligent computing cluster.<br>You can call the ListBmcpCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterId": "bmcp-bpnopt\*\*\*\*", "ClusterName": "cluster-name", "Description": "testDescription", "Status": "active", "CreateTime": "2023-11-29T17:08:15+08:0 0", "UpdateTime": "2023-12-13T15:15:25+08:0 0", "NodeCount": 3, "ActiveNodeCount": 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "cn-\*\*\*\*-env\*\*-d01", "Organization": "4", "ResourceGroup": "3", "InstanceList": \[ "i-d8offheheob5qaf0\* \*\*\*", "i-d620b2eheobcabte \*\*\*\*", "i-d75ppnuheobcnhq o\*\*\*\*" \], "VpcId": "vpc-bp1b1xjllp3ve5yze \*\*\*\*", "ClusterArchType": "standard", "EvpcId": "evpc-htchvitxlfjyso\*\*\*\*", "Zone": "cn-\*\*\*\*-env\*\*-d01-a", "IsSetPassword": true } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The request ID. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DescribeBmcpCluster
&ClusterId=bmcp-bpnopt****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "Status":"active",
  "Description":"testDescription",
  "ActiveNodeCount":1,
  "Organization":"4",
  "IsSetPassword":true,
  "NodeCount":3,
  "ClusterId":"bmcp-bpnopt****",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "MemCount":36,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "ClusterArchType":"standard",
  "FlopsCount":50,
  "CpuCount":10,
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "ClusterName":"cluster-name",
  "Region":"cn-****-env**-d01",
  "VideoMemory":50,
  "InstanceList":[
   "i-d8offheheob5qaf0****",
   "i-d620b2eheobcabte****",
   "i-d75ppnuheobcnhqo****"
  ],
  "ResourceGroup":"3"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <Status>active</Status>
 <Description>testDescription</Description>
 <ActiveNodeCount>1</ActiveNodeCount>
 <Organization>4</Organization>
 <IsSetPassword>true</IsSetPassword>
 <NodeCount>3</NodeCount>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <MemCount>36</MemCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <ClusterArchType>standard</ClusterArchType>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <ClusterName>cluster-name</ClusterName>
 <Region>cn-****-env**-d01</Region>
 <VideoMemory>50</VideoMemory>
 <InstanceList>i-d8offheheob5qaf0****</InstanceList>
 <InstanceList>i-d620b2eheobcabte****</InstanceList>
 <InstanceList>i-d75ppnuheobcnhqo****</InstanceList>
 <ResourceGroup>3</ResourceGroup>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-5"></a>

#### 5.1.1.5. AddBmcpClusterInstances

Scale out a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt\*\*\*\* | The ID of the bare metal -intelligent computing cluster.<br>You can call ListEhpcCluster to query the cluster ID. |
| InstanceLis t | Json | Quer y | No | null | This parameter is deprecated. |
| Password | Strin g | Quer y | No | null | This parameter is deprecated. |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal server types to be added to the intelligent computing cluster.<br>This parameter is required When ClusterArchType is set to standard, base, or aspeed. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | \[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\*", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\*" } \] | The list of parameters required for requesting bare metal servers.<br>This parameter is required when ClusterArchType is set to managed. |
| VswitchIdL ist | Json | Quer y | No | null | This parameter Is deprecated. |
| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| Activation Code | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| ZoneId | Strin g | Quer y | No | cn-\*\*\*\*-env\*\*-d01-a | The ID of the available zone. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp-bpnopt\*\*\*\*" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-6"></a>

#### 5.1.1.6. ListAvailableBmcpInstance

Query the list of available Bare Metal Computing Platform (BMCP) BMCP instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource setgroup. |
| VpcId | Strin g | Quer y | No | vpc-4uftp58qtzn7t663xajtj | The ID of the Virtual Private Cloud (VPC). |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "InstanceList": \[{ "InstanceId": "1", "InstanceIp": "192.168.1.1", "InstanceAlias": "c25d0\*\*\*\*.cloud.d 04.\*\*\*\*", "HostName": "c25d0\*\*\*\*.cloud.d 04.\*\*\*\*", "SN": "98001716037\*\*\*\* ", "InstacneType": "VM", "CpuCount": 192, "MemCount": 256, "FlopsCount": 2496, "VideoMemCount": 640, "VpcId": "vpc-xxxx" } \] } | The response data. |
| status | Integer | 0 | The status of the responsequest. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListAvailableBmcpInstance
&Department=4
&ResourceGroup=3
&VpcId=vpc-4uftp58qtzn7t663xajtj
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "InstanceList":[
   {
    "FlopsCount":2496,
    "CpuCount":192,
    "VideoMemCount":640,
    "VpcId":"vpc-xxxx",
    "InstanceId":"1",
    "InstanceAlias":"c25d0****.cloud.d04.****",
    "InstanceIp":"192.168.1.1",
    "SN":"98001716037****",
    "InstacneType":"VM",
    "HostName":"c25d0****.cloud.d04.****",
    "MemCount":256
   }
  ]
 },
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <InstanceList>
  <FlopsCount>2496</FlopsCount>
  <CpuCount>192</CpuCount>
  <VideoMemCount>640</VideoMemCount>
  <VpcId>vpc-xxxx</VpcId>
  <InstanceId>1</InstanceId>
  <InstanceAlias>c25d0****.cloud.d04.****</InstanceAlias>
  <InstanceIp>192.168.1.1</InstanceIp>
  <SN>98001716037****</SN>
  <InstacneType>VM</InstacneType>
  <HostName>c25d0****.cloud.d04.****</HostName>
  <MemCount>256</MemCount>
 </InstanceList>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-1-7"></a>

#### 5.1.1.7. DeleteBmcpClusterInstances

Scale in a bare metal cluster instance.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt\*\*\*\* | The ID of the bare metal -supercomputing cluster.<br>You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | \["i-d92sc86heobfdsc1\*\*\*\*"\] | The list of node IDs to be removed from the cluster. |
| InstanceLis t | Json | Quer y | No | \[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } \] | The list of bare metal servers to be removed from the cluster. This parameter is optional. |
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released.<br>• true: Clean<br>• false: Do not clean |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Valid values: 1 to 720.<br>Default value: 168.<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp-bpnopt\*\*\*\*" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteBmcpClusterInstances
&ClusterId=bmcp-bpnopt****
&InstanceIdList=["i-d92sc86heobfdsc1****"]
&ZoneId=cn-wulan-env***-****-a
&InstanceList=    
[
  {
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
  }
]  
&OsUpdate=true
&RetentionPeriod=168
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-1-8"></a>

#### 5.1.1.8. DeleteBmcpCluster

Delete a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt\*\*\*\* | The ID of the bare metal -supercomputing cluster.<br>You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceLis t | Json | Quer y | No | \[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } \] | The list of bare metal servers to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released.<br>• true: Clean<br>• false: Do not clean |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period of instances in the recycle bin. Unit: hours. Value range: 1 to 720.<br>Default value: 168.<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp-bpnopt\*\*\*\*" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Successful: true<br>• Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteBmcpCluster
&ClusterId=bmcp-bpnopt****
&InstanceList=[
 {
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
 }
]
&OsUpdate=true
&RetentionPeriod=168
&Common request parameters
```

Sample success responses

<a id="section-5-1-2"></a>

### 5.1.2. ACK - intelligent computing cluster

<a id="section-5-1-2-1"></a>

#### 5.1.2.1. CreateAckCluster

Create a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster.The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the cluster. Length: 0–1000 characters. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The login password for machines in the cluster.<br>The password must be 8– 30 characters in length, and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters.Supported special characters include \`()~!@#$%^&amp;\*-_+=\|{} \[\]:;'&lt;&gt;.,?/. |

<table>
  <tr>
    <td>ApplyBmsI nstanceLis t</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq****", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234****" } ]</td>
    <td>The list of Bare Metal Computing Platform (BMCP) instances for managed intelligent computing clusters.</td>
  </tr>
  <tr>
    <td>VpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>vpc-bp1b1xjllp3ve5yze****</td>
    <td>The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC.</td>
  </tr>
  <tr>
    <td>VswitchIdL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["vsw-2ze3ds0mdip0hdz8i****", "vsw-3gagdup8scary04iq****"]</td>
    <td>The list of master node vSwitch IDs. Valid values for the number of vSwitches:<code> [1,3] </code>. To ensure high availability of the cluster, we recommend that you select 3 vSwitches across different availability zones.</td>
  </tr>
</table>

<table>
  <tr>
    <td>Kubernete sVersion</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>1.32.7-aliyun.1</td>
    <td>The version of the Kubernetes which is aligned with the Kubernetes community baseline version. We recommend that you select the latest version.If not specified, the latest version is used by default.<br>You can call the DescribeKubernetesVersi onMetadata operation to query details of supported Kubernetes versions. For more information, see the Query Kubernetes <strong>version details</strong> section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>Runtime</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>{docker 19.03.5}</td>
    <td>The container runtime.Supported runtimes: containerd, Docker, and Sandboxed-Container.runv. The parameter runtime includes the following two information:<br>• name: Container runtime name<br>• Version: Container runtime version<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported runtime information. For more information, see the Query Kubernetes <strong>version details</strong> section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>MasterCou nt</td>
    <td>Integ er</td>
    <td>Quer y</td>
    <td>No</td>
    <td>3</td>
    <td>The number of master nodes. Valid values: 3 or 5.</td>
  </tr>
  <tr>
    <td>MasterInst anceTypeL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["ecs.n4.xlarge","ecs.n4.2 xlarge"]</td>
    <td>The list of master node instance types.<br>You can call the ListAckInstanceType operation to query instance types supported by master nodes (NodeType is set to master).</td>
  </tr>
  <tr>
    <td>MasterSyst emDiskCat egory</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>cloud_ssd</td>
    <td>The system disk type of master nodes. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: Solid-State Disk (SSD)<br>• cloud_pperf: High-performance disk<br>• cloud_sperf: Standard performance disk<br>Default value: cloud_efficiency.<br>The parameter MasterSystemDiskCatego ry must match MasterInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query system disk types supported by master node instance types.</td>
  </tr>
  <tr>
    <td>MasterSyst emDiskSiz e</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>40</td>
    <td>The system disk size of master nodes (GiB). Valid values: 40 to 500.</td>
  </tr>
  <tr>
    <td>WorkerCou nt</td>
    <td>Integ er</td>
    <td>Quer y</td>
    <td>No</td>
    <td>5</td>
    <td>The number of Elastic Compute Service (ECS) worker nodes. Valid values: 0 ≤ WorkerCount ≤ 100 − MasterCount.</td>
  </tr>
  <tr>
    <td>WorkerSys temDiskSiz e</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>40</td>
    <td>The system disk size of ECS worker nodes. Unit: GiB. Valid values: 40 to 500.</td>
  </tr>
  <tr>
    <td>WorkerSys temDiskCa tegory</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>cloud_ssd</td>
    <td>The system disk type of ECS worker nodes. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD cloud disk<br>• cloud_pperf: High-performance disk<br>• cloud_sperf: Standard performance disk<br>Default value: cloud_efficiency.<br>The parameter WorkerSystemDiskCatego ry must match WorkerInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the system disk types supported by worker node instance types.</td>
  </tr>
  <tr>
    <td>WorkerVs witchIdList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>["vsw-2ze3ds0mdip0hdz8i****", "vsw-3gagdup8scary04iq****"]</td>
    <td>The list of ECS worker node vSwitches. Valid values:<code> [1,3] </code>. To ensure high availability, we recommend that you select vSwitches in different availability zones.</td>
  </tr>
  <tr>
    <td>WorkerInst anceTypeL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>["ecs.n4.xlarge","ecs.n4.2 xlarge"]</td>
    <td>The list of ECS worker node instance types. Up to 10 instance types can be specified.<br>You can call the ListAckInstanceType operation to query the instance types supported by master nodes (NodeType is set to worker).</td>
  </tr>
  <tr>
    <td>WorkerDat aDiskList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>[{"Category": "cloud_ssd","Size":60,"En crypted":false}]</td>
    <td>The data disk information of ECS worker nodes. Up to 10 data disks are supported.<br>WorkerDataDiskList includes the following three parameters:<br>• Category: The data disk type. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD<br>• cloud_pperf: High-performance disk<br>• cloud_sperf: Standard performance disk<br>The parameter Category must match WorkerInstanceTypeLis<br>t. You can call the ListInstanceTypeDiskC ategory operation to query supported data disk types for worker nodes.<br>• Size: The data disk size. Unit: GiB. Valid values: 40 to 500.<br>• Encrypted: Whether encrypted.</td>
  </tr>
  <tr>
    <td>Os</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>Linux</td>
    <td>The type of the operating system.<br>• Windows<br>• Linux<br>Default value: Linux.</td>
  </tr>
  <tr>
    <td>Platform</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux</td>
    <td>The operating system distribution.<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported image information. For details, see the <strong>Query</strong> Kubernetes version <strong>details</strong> section in the <strong><em>Container Service for</em></strong> <strong><em>Kubernetes Developer</em></strong> <strong><em>Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>ImageType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux3</td>
    <td>The type of the image.<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported image types. For details, see the Query Kubernetes <strong>version details</strong> section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>PodCidr</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>172.20.0.0/16</td>
    <td>The Pod network CIDR block. It must not overlap with the VPC CIDR block.</td>
  </tr>
  <tr>
    <td>ServiceCid r</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>172.21.0.0/20</td>
    <td>The Service network CIDR block. Valid range: 10.0.0.0/16–24, 172.16– 31.0.0/16–24, and 192.168.0.0/16–24. It must not overlap with the VPC CIDR block 10.1.0.0/21 or any CIDR block already used by existing Kubernetes clusters in the VPC. It cannot be modified after creation.</td>
  </tr>
  <tr>
    <td>SnatEntry</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to configure SNAT (Source Network Address Translation) for the VPC.Valid values:<br>• true: Automatically create a Network Address Translation (NAT) gateway and configure SNAT entries.Set this parameter to true if nodes and applications in the cluster require Internet access.<br>• false: Do not create a NAT gateway or SNAT entries. Nodes and applications in the cluster cannot access the Internet.<br>Default value: false.</td>
  </tr>
  <tr>
    <td>EndpointP ublicAcces s</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable public access.Valid values:<br>• true: Enable public access. Expose the API server via an Elastic IP Address (EIP) to enable cluster access over the Internet.<br>• false: Disable public access. If disabled, the cluster API server cannot be accessed over the Internet.<br>Default value: false.</td>
  </tr>
  <tr>
    <td>SshFlag</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable public Secure Shell (SSH) login. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.<br>This parameter is required if EndpointPublicAccess is set to true.</td>
  </tr>
  <tr>
    <td>LogService</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable the log service.Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>LogProject</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>k8s-log-c2345xxxxxxxxxxxx</td>
    <td>The name of the log project.<br>You can configure this parameter when LogService is set to true.If not specified, a log project is automatically created.</td>
  </tr>
  <tr>
    <td>DeleteProt ection</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable cluster deletion protection. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>InstanceD eleteProte ction</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable instance deletion protection. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>ZoneId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>cn-wulan-env***-****-a</td>
    <td>The ID of the available zone.</td>
  </tr>
  <tr>
    <td>ClusterArc hType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>standard</td>
    <td>The type of the cluster.Valid values:<br>• standard: Intelligent computing high-bandwidth network<br>• managed: Managed intelligent computing<br>• base: Basic intelligent computing<br>• aspeed: Intelligent computing training and inference</td>
  </tr>
  <tr>
    <td>MachineTy peList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "NodePoolName": "bmcp-node-pool" , "VswitchId": "vsw-3gagdup8scary04iq****"} ]</td>
    <td>The list of bare metal instance types to be added to the cluster.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>BmsVswitc hIdList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>EvpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>evpc-htchvitxlfjyso****</td>
    <td>The ID of the Enterprise VPC (EVPC).<br>This parameter is required when ClusterArchType is set to standard or aspeed.<br>You can call the ListEvpc operation to query the EVPC ID.</td>
  </tr>
  <tr>
    <td>ActivationI d</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>a-hz0ch3SwhOlE1234+Xo3 2lAZC****</td>
    <td>The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>Activation Code</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>4ECEEE12-56F1-4FBC-9AB1-890F1234****</td>
    <td>The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>VolumeId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>MountPath</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>IsCreateCp fsCluster</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable the high-performance storage client cluster. Valid values:<br>• true: Enable<br>• false: Disable<br>Default Value: false.<br>You can configure this parameter when ClusterArchType is set to standard or aspeed.<br>To enable the high-performance storage cluster, the following conditions must be met: evpcId is selected; the number of Cloud Parallel File System (CPFS)-type bare metal nodes is at least 3; and the number of Apple File System (APFS) cluster bare metal nodes is at least 1.</td>
  </tr>
  <tr>
    <td>CpfsCluste rType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>CPFS</td>
    <td>The type of the high-performance storage client cluster. Valid values:<br>• CPFS<br>• APFS<br>This parameter is required when IsCreateCpfsCluster is set to true.</td>
  </tr>
  <tr>
    <td>ClassicSlb Spec</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>slb.s2.small</td>
    <td>The Server Load Balancer (SLB) specification.</td>
  </tr>
  <tr>
    <td>VolumeInf o</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023-04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, {"VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, {"VolumeType": "mount", "VolumeParams": {"Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ]</td>
    <td>The third-party storage mount information.<br>You can configure this parameter when ClusterArchType is set to managed.</td>
  </tr>
  <tr>
    <td>AppNameL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["ai-task-inspector","fluid"]</td>
    <td>The list of components to install.<br>You can call the ListApps operation to query the available component list.</td>
  </tr>
  <tr>
    <td>EnabledDr agonfly</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AddonSyst emDiskSiz e</td>
    <td>Integ er</td>
    <td>Quer y</td>
    <td>No</td>
    <td>40</td>
    <td>The system disk size of the software instances.Unit: GiB. Valid values: 40 to 500.</td>
  </tr>
  <tr>
    <td>AddonSyst emDiskCat egory</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>cloud_ssd</td>
    <td>The system disk specifications of the software instances. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD cloud disk<br>• cloud_pperf: High-performance disk<br>• cloud_spPerf: Standard performance disk<br>The parameter AddonSystemDiskCategor y must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query system disk types supported by software instance types.</td>
  </tr>
</table>

<table>
  <tr>
    <td>DataDisk</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>The list of software instance data disk.<br>WorkerDataDiskList includes the following two parameters:<br>• Category: The data disk type. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD<br>• cloud_pperf: High-performance disk<br>• cloud_sperf: Standard performance disk<br>• Size: The data disk size. Unit: GiB. Valid values: 40 to 500.<br>The parameter Category must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query data disk types supported by worker node instance types.</td>
  </tr>
  <tr>
    <td>ImageId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>aliyun_4_x86_64_20G_co ntainer_optimized_alibase _20260407.vhd</td>
    <td>The ID of the image used by the software instance.<br>• If not configured, it defaults to the image used by the cluster.<br>• To configure this parameter, call the DescribeKubernetesVer sionMetadata operation to query supported image IDs.For details, see the Query Kubernetes version details section in the <strong><em>Contain</em></strong> <strong><em>er Service for Kuber</em></strong> <strong><em>netes Developer Gui</em></strong> <strong><em>de</em></strong>.</td>
  </tr>
  <tr>
    <td>AdminUid</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIRootPwd</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIUserNam e</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIPwd</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>Accelerato rVendorNa me</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>The name of the Nanhu Insight accelerator provider.<br>This parameter is required when Nanhu Insight is installed for the AppNameList.</td>
  </tr>
  <tr>
    <td>NanhuInsi ghtClusterI d</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>The ID of the Nanhu Insight cluster.<br>This parameter is required when Nanhu Insight is installed for the AppNameList.</td>
  </tr>
  <tr>
    <td>PeerEvpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>evpc-***hvitxlfjyso****</td>
    <td>The ID of the Nanhu Insight peer EVPC.<br>This parameter is required when Nanhu Insight is installed for the AppNameList.</td>
  </tr>
  <tr>
    <td>AddonInst anceTypeL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4x large"]</td>
    <td>The list of software instance types. Up to 10 types are supported.<br>You can call the ListAckInstanceType operation to query software instance types.The minimum software instance type is 16 vCPU and 16 GB.</td>
  </tr>
  <tr>
    <td>IsCreateEd aCluster</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>true</td>
    <td>Specifies whether to enable cache acceleration clusters.Valid values:<br>• true: Enable<br>• false: Disable<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed.</td>
  </tr>
  <tr>
    <td>IsInstallYu ndunAegis</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>true</td>
    <td>Specifies whether to install Server Guard. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>IsAutoDisk</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>true</td>
    <td>Specifies whether to mount Kubernetes images and pods for BMCP nodes to the data disk.</td>
  </tr>
  <tr>
    <td>SwitchMet hod</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>Access Denied</td>
    <td>CHSW</td>
    <td>The networking mode for the vSwitch.<br>• This parameter must be CHSW when ClusterArchType is set to standard, base, or aspeed.<br>• This parameter can be CHSW or HSW when ClusterArchType is set to managed.</td>
  </tr>
  <tr>
    <td>StandardV switchId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>vsw-2ze3ds0mdip0hdz8i****</td>
    <td>Monitoring channel vSwitch, used for building the cluster management and O&amp;M channel.</td>
  </tr>
  <tr>
    <td>EnableIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable the IPv6 feature.<br>• true: Enable<br>• false: Disable<br>Default value: false</td>
  </tr>
  <tr>
    <td>EvpcEnabl eIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable EVPC IPv6. Valid values:<br>IPv6 can be enabled only when EvpcId is configured.<br>• true: Enable<br>• false: Disable<br>Default value: false</td>
  </tr>
  <tr>
    <td>NodeCidrM ask</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>25</td>
    <td>The number of node IPs, determined by the CIDR of the specified network.This parameter takes effect only for clusters that use the Flannel network plug-in.<br>Default value: 25.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "ack-E7qLEr\*\*\*\*", "AckClusterName": "testname" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

Sample success responses `JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ack-E7qLEr****",
  "ClusterName":"testname",
  "AckClusterName":"testname"
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>ack-E7qLEr****</ClusterId>
 <ClusterName>testname</ClusterName>
 <AckClusterName>testname</AckClusterName>
</data>
<errorTitle  />
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-2"></a>

#### 5.1.2.2. ListAckCluster

Query the list of Container Service for Kubernete (ACK) - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| AckCluster Name | Strin g | Quer y | No | cluster-name | The name of the ACK cluster. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |
| AckCluster Id | Strin g | Quer y | No | cef51d60a6778415ab3a8 026c24\*\*\*\*\* | The ID of the ACK cluster. |
| Status | Strin g | Quer y | No | \*\* | The status of the cluster status. Valid values:<br>• creating: Creating<br>• active: Running<br>• createFailed: Creation failed<br>• deleting: Deleting<br>• deleteFailed: Deletion failed<br>• scalingDown: Scaling in<br>• ScalingDownFailed: Scale-in failed<br>• SaclingUp: Scaling out<br>• ScalingUpFailed: Scale-out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number, used for pagination query.Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page, which specifies the number of results returned per page.Default value: 10. |
| Zone | Strin g | Quer y | No | cn-\*\*\*\*-env\*\*-d01-a | The ID of the available zone. |
| AiStatus | Strin g | Quer y | No | active | The status of the software installed in the cluster.<br>• notInstall: Not installed<br>• active: Running<br>• installFailed: Installation failed<br>• installing: Installing<br>• uninstalling: Uninstalling<br>• unInstallFailed: Uninstallation failed |
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster.Valid values:<br>• standard: Intelligent computing high-bandwidth network<br>• managed: Managed intelligent computing<br>• base: Basic intelligent computing<br>• aspeed: Intelligent computing training and inference |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard or aspeed.<br>You can call the ListEvpc operation to query the EvpcId. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). |
| EdaCluster State | Strin g | Quer y | No | RUNNING | The status of the cache acceleration cluster. Valid values:<br>• INITIAL: Creating<br>• RUNNING: Running<br>• SHRINKING: Scaling in<br>• EXPANDING: Scaling out<br>• RELEASING: Releasing |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TotalCount": 1, "PageNumber": 1, "PageSize": 10, "ClusterList": \[ {"ClusterId": "ack-8EEjd6\*\*\*\*", "AckClusterId": "c4ecce05e63814a 9592b92ad18e59\* \*\*\*", "ClusterName": "cluster-name", "CpfsClusterType": "CPFS", "CpfsMountFs": "", "CpfsClusterState": "", "AckClusterName": "cluster-name", "Description": "testDescription", "Status": "active", "Version": "1.20.11-aliyunedge.1", "CreateTime": "2023-12-29T10:00:00+08:0 0", "UpdateTime": "2023-12-29T10:00:00+08:0 0", "NodeCount": 5, "ClusterResourceT ype": "bmcp", "BmsNodeCount": 2, "BmsActiveNodeCo unt": 1, "Region": "cn-wulan-env\*\*\*-d01", "Organization": "69", "ResourceGroup": "69", "SpId": "", "AiStatus": "notInstall", "VpcId": "vpc-bp1b1xjllp3ve5yze \*\*\*\*", "SlbIp": "", "CpuCount": 0, "MemCount": 0, "FlopsCount": 0, "VideoMemory": 0, "Zone": "cn-wulan-env\*\*\*-\*\*\*\*-a", "ClusterArchType": "standard", "EvpcId": "evpc-htchvitxlfjyso\*\*\*\*", "EcsNodeCount": 3, "IsSetPassword": true, "Gpu": \[ {"GpuNum": 3, "GpuModel": "NvidiaTeslaA100"} \], "SwitchMethod": "CHSW", "EdaClusterState": "RUNNING" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListAckCluster
&Department=4
&ResourceGroup=3
&Zone=cn-****-env**-d01-a
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "ClusterList":[
   {
    "EcsNodeCount":3,
    "Description":"testDescription",
    "Organization":"69",
    "IsSetPassword":true,
    "BmsActiveNodeCount":1,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"CPFS",
    "Gpu":[
     {
      "GpuNum":3,
      "GpuModel":"NvidiaTeslaA100"
     }
    ],
    "EvpcId":"evpc-htchvitxlfjyso****",
    "FlopsCount":0,
    "CpuCount":0,
    "SlbIp":"",
    "Version":"1.20.11-aliyunedge.1",
    "ClusterResourceType":"bmcp",
    "AiStatus":"notInstall",
    "ClusterName":"cluster-name",
    "ResourceGroup":"69",
    "SpId":"",
    "Status":"active",
    "AckClusterId":"c4ecce05e63814a9592b92ad18e59****",
    "NodeCount":5,
    "ClusterId":"ack-8EEjd6****",
    "Zone":"cn-wulan-env***-****-a",
    "CreateTime":"2023-12-29T10:00:00+08:00",
    "AckClusterName":"cluster-name",
    "CpfsClusterState":"",
    "MemCount":0,
    "ClusterArchType":"standard",
    "VpcId":"vpc-bp1b1xjllp3ve5yze****",
    "BmsNodeCount":2,
    "UpdateTime":"2023-12-29T10:00:00+08:00",
    "CpfsMountFs":"",
    "Region":"cn-wulan-env***-d01",
    "EdaClusterState":"RUNNING",
    "VideoMemory":0
   }
  ],
  "PageSize":10,
  "PageNumber":1
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data  />
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-2-3"></a>

#### 5.1.2.3. DescribeAckCluster

Query the details of a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

<table>
  <tr>
    <td>data</td>
    <td>Map</td>
    <td>{ "ClusterId": "ack-8EEjd6****", "AckClusterId": "c4ecce05e63814a 9592b92ad18e59* ***", "ClusterName": "cluster-name", "AckClusterName": "zpftest1", "Organization": "69", "ResourceGroup": "69", "Region": "cn-wulan-env***-d01", "Description": "testDescription", "Status": "active", "Version": "1.20.11-aliyunedge.1", "CreateTime": "2023-12-29T10:00:00+08:0 0", "UpdateTime": "2023-12-29T10:00:00+08:0 0", "NodeCount": 3, "BmsNodeCount": 2, "BmsActiveNodeCo unt": 1, "AliUid": "111", "SpId": "", "AiStatus": "notInstall", "VpcId": "vpc-bp1b1xjllp3ve5yze ****", "DeletionProtection ": false, "CpuCount": 0, "MemCount": 0, "FlopsCount": 0, "VideoMemory": 0, "SlbIp": "", "Zone": "cn-wulan-env***-****-a", "ClusterArchType": "standard", "EvpcId": "evpc-htchvitxlfjyso****", "EcsNodeCount": 3, "IsSetPassword": true }</td>
    <td>The response data.</td>
  </tr>
  <tr>
    <td>status</td>
    <td>Integer</td>
    <td>200</td>
    <td>The status of the response.</td>
  </tr>
  <tr>
    <td>requestId</td>
    <td>String</td>
    <td>66dfddc6-b547-11ee-aa84-acde4800****</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>success</td>
    <td>Boolean</td>
    <td>true</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>responseVersi on</td>
    <td>String</td>
    <td>v1</td>
    <td>The version of the response.</td>
  </tr>
</table>

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DescribeAckCluster&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "EcsNodeCount":3,
  "Organization":"69",
  "Description":"testDescription",
  "IsSetPassword":true,
  "BmsActiveNodeCount":1,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "FlopsCount":0,
  "CpuCount":0,
  "SlbIp":"",
  "Version":"1.20.11-aliyunedge.1",
  "AiStatus":"notInstall",
  "ClusterName":"cluster-name",
  "ResourceGroup":"69",
  "SpId":"",
  "Status":"active",
  "AckClusterId":"c4ecce05e63814a9592b92ad18e59****",
  "NodeCount":3,
  "ClusterId":"ack-8EEjd6****",
  "Zone":"cn-wulan-env***-****-a",
  "CreateTime":"2023-12-29T10:00:00+08:00",
  "AckClusterName":"zpftest1",
  "DeletionProtection":false,
  "MemCount":0,
  "ClusterArchType":"standard",
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "BmsNodeCount":2,
  "UpdateTime":"2023-12-29T10:00:00+08:00",
  "Region":"cn-wulan-env***-d01",
  "VideoMemory":0,
  "AliUid":"111"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <EcsNodeCount>3</EcsNodeCount>
 <Organization>69</Organization>
 <Description>testDescription</Description>
 <IsSetPassword>true</IsSetPassword>
 <BmsActiveNodeCount>1</BmsActiveNodeCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <FlopsCount>0</FlopsCount>
 <CpuCount>0</CpuCount>
 <SlbIp  />
 <Version>1.20.11-aliyunedge.1</Version>
 <AiStatus>notInstall</AiStatus>
 <ClusterName>cluster-name</ClusterName>
 <ResourceGroup>69</ResourceGroup>
 <SpId  />
 <Status>active</Status>
 <AckClusterId>c4ecce05e63814a9592b92ad18e59****</AckClusterId>
 <NodeCount>3</NodeCount>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <Zone>cn-wulan-env***-****-a</Zone>
 <CreateTime>2023-12-29T10:00:00+08:00</CreateTime>
 <AckClusterName>zpftest1</AckClusterName>
 <DeletionProtection>false</DeletionProtection>
 <MemCount>0</MemCount>
 <ClusterArchType>standard</ClusterArchType>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <BmsNodeCount>2</BmsNodeCount>
 <UpdateTime>2023-12-29T10:00:00+08:00</UpdateTime>
 <Region>cn-wulan-env***-d01</Region>
 <VideoMemory>0</VideoMemory>
 <AliUid>111</AliUid>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>200</status>
```

<a id="section-5-1-2-4"></a>

#### 5.1.2.4. AddAckClusterInstances

Scale out a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | \[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\*", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\*" } \] | The list of parameters for requesting bare metal servers.<br>This parameter is required when ClusterArchType is set to managed. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The password of the bare metal instance to be modified. This parameter is required if no password has been set for the cluster. |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal instance types to be added to the supercomputing cluster.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |
| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| Activation Code | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the available zone. |
| WorkerCou nt | Integ er | Quer y | No | 5 | The number of Elastic Compute Service (ECS) worker nodes. Valid values: 0 ≤ WorkerCount ≤ 100 - MasterCount. |
| WorkerSys temDiskSiz e | Strin g | Quer y | No | 40 | The system disk size to be scaled out for ECS worker nodes. Unit: GiB.Valid values: 40-500. |
| WorkerSys temDiskCa tegory | Strin g | Quer y | No | cloud_ssd | The system disk type of ECS worker nodes. Valid values:<br>cloud_efficiency: Ultra disk<br>cloud_ssd: SSD cloud disk<br>cloud_pperf: High-performance disk<br>cloud_sperf: Standard performance disk<br>Default value: cloud_efficiency.<br>The parameter WorkerSystemDiskCatego ry must match WorkerInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the system disk types supported by worker node instance types. |
| WorkerVs witchIdList | Json | Quer y | No | \["vsw-2ze3ds0mdip0hdz8i\*\*\*\*", "vsw-3gagdup8scary04iq\*\*\*\*"\] | The list of ECS worker node vSwitchs. Valid values: \[1, 3\]. To ensure high availability, we recommend selecting vSwitches in different availability zones. |
| WorkerInst anceTypeL ist | Json | Quer y | No | \["ecs.n4.xlarge","ecs.n4.2 xlarge"\] | The list of instance types for scaling out ECS worker nodes. Up to 10 instance types can be specified.<br>You can call the ListAckInstanceType operation to query the instance types supported by master nodes (NodeType is set to worker). |

<table>
  <tr>
    <td>WorkerDat aDiskList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[{"Category": "cloud_ssd","Size":60,"En crypted":false}]</td>
    <td>The data disk configurations for scaling out ECS worker nodes. Up to 10 data disks are supported.<br>WorkerDataDiskList includes the following three parameters:<br>• Category: The data disk type. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: Solid-State Disk (SSD)<br>• cloud_pperf: High-performance disk<br>• cloud_sperf: Standard performance disk<br>The parameter Category must match WorkerInstanceTypeLis<br>t. You can call the ListInstanceTypeDiskC ategory operation to query supported data disk types for worker nodes.<br>• Size: The data disk size. Unit: GiB. Valid values: 40 to 500.<br>• Encrypted: Whether encrypted.</td>
  </tr>
  <tr>
    <td>IsAutoDisk</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to mount Kubernetes images and pods on Bare Metal Computing Platform (BMCP) nodes to data disks.</td>
  </tr>
  <tr>
    <td>WorkerIma geId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>aliyun_4_x86_64_20G_co ntainer_optimized_alibase _20260407.vhd</td>
    <td>The ID of the ECS worker node image.<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported images.For details, see the Query Kubernetes <strong>version details</strong> section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>WorkerIma geType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux3</td>
    <td>The type of the ECS worker node image.<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported images.For details, see the Query Kubernetes <strong>version details</strong> section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
  <tr>
    <td>WorkerPlat form</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux</td>
    <td>The operating system distribution of the ECS worker image platform.<br>You can call the DescribeKubernetesVersi onMetadata operation to query supported images.For details, see the Query Kubernetes <strong>version details</strong> Section in the <strong><em>Container</em></strong> <strong><em>Service for Kubernetes</em></strong> <strong><em>Developer Guide</em></strong>.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack-8EEjd6\*\*\*\*", "AckClusterId": "cef51d60a677841 5ab3a8026c24\*\*\*\* \*", "AckClusterName": "cluster-name" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-5"></a>

#### 5.1.2.5. ListAckClusterInstances

Query the list of nodes in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |
| State | Strin g | Quer y | No | running | The status of the node. If this parameter is not specified, nodes in all states are returned.<br>• pending: creating<br>• running: running<br>• starting: starting<br>• stopping: stopping<br>• stopped: stopped |
| NodePoolI d | Strin g | Quer y | No | bmcp | The ID of the node pool.This parameter is left blank by defaut.<br>You can call ListAckClusterNodePool to query the node pool ID. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TotalCount": 1, "PageNumber": 1, "PageSize": 10, "InstanceList": \[ {"InstanceName": "worker-k8s-for-cs-c42bb3189a\*\*\*\*c2 608634943d67", "NodePoolId": "npba2cf\*\*\*acd093 eb12d5e", "NodeName": "cn\*\*\*\*-d01.192.168.99.14 4", "InstanceId": "i-\*\*\*\*", "State": "running", "CreateTime": "2024-06-20T15:15:24+08:0 0", "IP": "192.\*\*\*.\*\*.144", "ImageId": "aliyun_2_1903_x8 6_64_\*\*\*\*\*_202211 18.vhd", "InstanceRole": "Worker", "InstanceType": "ecs.sn1.medium", "HostName": "iZ0sv0\*\*\*\*9c4las1 hZ", "NodeStatus": "Ready", "SN": "xxxx", "VirtualStrategy": "1", "SupportVirtStg":" \[\\"1\\"\]", "BmcpStatus":"", "BmcpState": "", "BmcpMappingStat us":"", "BMcpRunningStat e": "" }, \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "PageNumber":1,
  "InstanceList":[
   {
    "BMcpRunningState":"",
    "NodeName":"cn****-d01.192.168.99.144",
    "InstanceId":"i-****",
    "CreateTime":"2024-06-20T15:15:24+08:00",
    "IP":"192.***.**.144",
    "SupportVirtStg":"[\"1\"]",
    "BmcpState":"",
    "InstanceName":"worker-k8s-for-cs-c42bb3189a****c2608634943d67",
    "BmcpMappingStatus":"",
    "NodePoolId":"npba2cf***acd093eb12d5e",
    "State":"running",
    "ImageId":"aliyun_2_1903_x86_64_*****_20221118.vhd",
    "InstanceRole":"Worker",
    "VirtualStrategy":"1",
    "BmcpStatus":"",
    "SN":"xxxx",
    "InstanceType":"ecs.sn1.medium",
    "HostName":"iZ0sv0****9c4las1hZ",
    "NodeStatus":"Ready"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <InstanceList>
  <BMcpRunningState  />
  <NodeName>cn****-d01.192.168.99.144</NodeName>
  <InstanceId>i-****</InstanceId>
  <CreateTime>2024-06-20T15:15:24+08:00</CreateTime>
  <IP>192.***.**.144</IP>
  <SupportVirtStg>[&quot;1&quot;]</SupportVirtStg>
  <BmcpState  />
  <InstanceName>worker-k8s-for-cs-c42bb3189a****c2608634943d67</InstanceName>
  <BmcpMappingStatus  />
  <NodePoolId>npba2cf***acd093eb12d5e</NodePoolId>
  <State>running</State>
  <ImageId>aliyun_2_1903_x86_64_*****_20221118.vhd</ImageId>
  <InstanceRole>Worker</InstanceRole>
  <VirtualStrategy>1</VirtualStrategy>
  <BmcpStatus  />
  <SN>xxxx</SN>
  <InstanceType>ecs.sn1.medium</InstanceType>
  <HostName>iZ0sv0****9c4las1hZ</HostName>
  <NodeStatus>Ready</NodeStatus>
 </InstanceList>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>200</status>
```

<a id="section-5-1-2-6"></a>

#### 5.1.2.6. ListAckClusterNodePool

Query the list of node pools in a container intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterId | Strin g | Quer y | Yes | ack-8EEjd6\*\*\*\* | The ID of the cluster.<br>You can call ListAckCluster to query the cluster ID. |
| Type | Strin g | Quer y | No | bmcp | The node pool type. Valid values:<br>• bmcp<br>• ecs<br>If this parameter is not specified, node pools of all types are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "NodePools": \[ {"NodePoolId": "npe576\*\*\*\*3c944 b1\*\*\*\*d144c0263\* \*\*\*", "NodePoolName": "test1", "NodePoolType": "bmcp" }, {"NodePoolId": "npcdcf\*\*\*\*2bb946 288\*\*\*\*ab9aa34\*\*\* \*", "NodePoolName": "test1", "NodePoolType": "ess" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListAckClusterNodePool
&Department=4
&ResourceGroup=3
&ClusterId=ack-8EEjd6****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "NodePools":[
   {
    "NodePoolId":"npe576****3c944b1****d144c0263****",
    "NodePoolName":"test1",
    "NodePoolType":"bmcp"
   },
   {
    "NodePoolId":"npcdcf****2bb946288****ab9aa34****",
    "NodePoolName":"test1",
    "NodePoolType":"ess"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <NodePools>
  <NodePoolId>npe576****3c944b1****d144c0263****</NodePoolId>
  <NodePoolName>test1</NodePoolName>
  <NodePoolType>bmcp</NodePoolType>
 </NodePools>
 <NodePools>
  <NodePoolId>npcdcf****2bb946288****ab9aa34****</NodePoolId>
  <NodePoolName>test1</NodePoolName>
  <NodePoolType>ess</NodePoolType>
 </NodePools>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-7"></a>

#### 5.1.2.7. DeleteAckClusterInstances

Remove nodes from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call ListAckCluster to query the cluster ID. |
| InstanceId List | Json | Quer y | No | \["11"\] | The list of bare metal node IDs to remove from the cluster.<br>You can call ListBmcpInstance to query the bare metal node ID. For more information, see ListBmcpInstance in the BMS Developer Guide. |
| InstanceLis t | Json | Quer y | No | \[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } \] | The list of bare metal nodes to remove from the cluster. |
| EcsInstanc eIdList | Json | Quer y | No | \["i-d92sc86heobfdsc1\*\*\*\*"\] | The list of Elastic Compute Service (ECS) worker node IDs to remove from the cluster.<br>You can call ListAckClusterEcsWorkerI nstances to query the ECS worker node ID. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks when releasing the instance. Valid values:<br>• true: Clear data disks.<br>• false: Do not clear data disks. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Valid values: 1 to 720<br>Default value: 168<br>After a Bare Metal Computing Platform (BMCP) node is removed from the cluster, it is placed in the recycle bin.You can restore the node from the recycle bin to the original cluster within the retention period.After the retention period expires, the node is automatically released to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack-8EEjd6\*\*\*\*", "AckClusterId": "cef51d60a677841 5ab3a8026c24\*\*\*\* \*", "AckClusterName": "cluster-name" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteAckClusterInstances
&ClusterId=ack-8EEjd6****
&InstanceIdList=["11"]
&InstanceList=    
[
  {
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
  }
]  
&OsUpdate=true
&RetentionPeriod=168
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-8"></a>

#### 5.1.2.8. ModifyAckClusterDeletionProtection

Modify the deletion protection status of a Container Service for Kubernetes (ACK)-intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK-intelligent computing cluster.<br>You can call ListAckCluster to query the cluster ID. |
| DeletionPr otection | Bool ean | Quer y | No | true | The deletion protection status. Valid values:<br>• true: Enable deletion protection.<br>• false: Disable deletion protection. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | "The modification was successful" | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON`  format

```json
{
    "errorCode": "",
    "errorTitle": "",
    "errorMessage": "",
    "code": "",
    "data": "The modification was successful",
    "status": 0,
    "requestId": "d239ef18-a5f1-11ee-a470-16f363c78ec1",
    "success": true,
    "responseVersion": ""
}
```

`XML`  format

```xml
<errorCode  />
<errorTitle  />
<errorMessage  />
<code  />
<data>The modification was successful</data>
<status>0</status>
<requestId>d239ef18-a5f1-11ee-a470-16f363c78ec1</requestId>
<success>true</success>
<responseVersion  />
```

<a id="section-5-1-2-9"></a>

#### 5.1.2.9. ListAckInstanceType

Query the instance types supported by Container Service for Kubernete (ACK) - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| AckCluster Name | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| ClusterId | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| AckCluster Id | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| Status | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the available zone. Separate multiple zone IDs with commas (,), example: <code> zone1,zone2 </code>. |
| VpcAdvanc edResourc e | Bool ean | Quer y | No | true | Specifies whether to enable Virtual Private Cloud (VPC) advanced features. Valid values:<br>• true: Enable<br>• false: Disable<br>Default Value: false. |
| NodeType | Strin g | Quer y | No | master | The node type of the ACK.Valid values:<br>• master<br>• worker |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "InstanceTypes": \[ { "MemorySize": 4, "MultiIpPodCount": 0, "CpuCoreCount": 2, "EniTrunkSupporte d": false, "InstanceTypeFami ly": "ecs.n4", "Zone": "cn-wulan-env\*\*\*-\*\*\*\*-a", "EniQuantity": 1, "ExclusivePodCoun t": 0, "GPUAmount": 0, "ExclusiveMode": false, "WarningInfos": \["If the resource specifications are low, business operations may be affected, so we recommend that you use them only for small-scale verification tests" \], "MultiIpMode": false, "GPUSpec": "", "InstanceTypeId": "ecs.n4.large", "TrunkPodCount": 0 } \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListAckInstanceType
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-env***-d01
&ZoneId=cn-wulan-env***-****-a
&VpcAdvancedResource=true
&NodeType=master
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "InstanceTypes":[
   {
    "MemorySize":4,
    "MultiIpPodCount":0,
    "CpuCoreCount":2,
    "EniTrunkSupported":false,
    "InstanceTypeFamily":"ecs.n4",
    "Zone":"cn-wulan-env***-****-a",
    "EniQuantity":1,
    "ExclusivePodCount":0,
    "GPUAmount":0,
    "ExclusiveMode":false,
    "WarningInfos":[
     "If the resource specifications are low, business operations may be affected, so we recommend that you use them only for small-scale verification tests"
    ],
    "MultiIpMode":false,
    "GPUSpec":"",
    "InstanceTypeId":"ecs.n4.large",
    "TrunkPodCount":0
   }
  ]
 },
 "errorTitle":"",
 "requestId":"**",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <InstanceTypes>
  <MemorySize>4</MemorySize>
  <MultiIpPodCount>0</MultiIpPodCount>
  <CpuCoreCount>2</CpuCoreCount>
  <EniTrunkSupported>false</EniTrunkSupported>
  <InstanceTypeFamily>ecs.n4</InstanceTypeFamily>
  <Zone>cn-wulan-env***-****-a</Zone>
  <EniQuantity>1</EniQuantity>
  <ExclusivePodCount>0</ExclusivePodCount>
  <GPUAmount>0</GPUAmount>
  <ExclusiveMode>false</ExclusiveMode>
  <WarningInfos>If the resource specifications are low, business operations may be affected, so we recommend that you use them only for small-scale verification tests</WarningInfos>
  <MultiIpMode>false</MultiIpMode>
  <GPUSpec  />
  <InstanceTypeId>ecs.n4.large</InstanceTypeId>
  <TrunkPodCount>0</TrunkPodCount>
 </InstanceTypes>
</data>
<errorTitle  />
<requestId>**</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>200</status>
```

<a id="section-5-1-2-10"></a>

#### 5.1.2.10. ListApps

Query the list of available components.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| AppType | Strin g | Quer y | No | BMCP | The application type.Valid values:<br>• BMCP<br>• ACK |
| Group | Strin g | Quer y | No | AIComputing | The component group.Different component groups apply to different AI computing scenarios.Valid values:<br>• OpsStability<br>• InferenceOptimize<br>• DataAccelerate<br>• AIComputing |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| SearchVal ue | Strin g | Quer y | No | test | The search keyword. |
| Language | Strin g | Quer y | No | zh_CN | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "PageSize": 10, "PageNumber": 1, "Total": 3, "Apps": \[ { "AppVersion": "1.2.0", "ChartVersion": "1.2.0", "Group": "AIComputing", "Description": "A unified management controller for Bare Metal Computing Platform (BMCP) device plugins (such as DevicePlugin and Exporter). Once deployed, it enables unified management and orchestration of Container Service for Kubernetes (ACK)-side GPU plugins, and installs the Node Feature Discovery (NFD) component to automatically tag nodes.", "Arch": \[ "amd64", "arm64" \], "AppType": "BMCP", "AppName": "bmcp-gpu-operator" }, {"AppVersion": "1.0.0", "ChartVersion": "1.0.0", "Group": "AIComputing", "Description": "The BMCP GPU deployment engine supports flexible, adaptable, and upgradeable GPU component deployments. You need to create a GPU component deployment task based on the custom resource (CR) BMCPClusterPolicy.", "Arch": \["amd64", "arm64"\], "AppType": "BMCP", "AppName": "gpu-deploy-engine" }, {"AppVersion": "1.2.0", "ChartVersion": "1.2.0", "Group": "AIComputing", "Description": "A cloud-native component that provides Alibaba Platform GPU (APG) user-space virtualization, supporting the isolation of compute capabilities and GPU memory.Currently, only APG is supported. The BMCP GPU toolkit must be installed before use.", "Arch": \[ "amd64", "arm64" \], "AppType": "BMCP", "AppName": "kgpu" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListApps
&AppType=BMCP
&Group=Group
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "PageSize":10,
  "PageNumber":1,
  "Total":3,
  "Apps":[
   {
    "AppVersion":"1.2.0",
    "ChartVersion":"1.2.0",
    "Group":"AIComputing",
    "Description":"A unified management controller for Bare Metal Computing Platform (B
MCP) device plugins (such as DevicePlugin and Exporter). Once deployed, it enables unified management and orchestration of Container Service for Kubernetes (ACK)-side GPU plugins, and installs the Node Feature Discovery (NFD) component to automatically tag nodes.",
    "Arch":[
     "amd64",
     "arm64"
    ],
    "AppType":"BMCP",
    "AppName":"bmcp-gpu-operator"
   },
   {
    "AppVersion":"1.0.0",
    "ChartVersion":"1.0.0",
    "Group":"AIComputing",
    "Description":"The BMCP GPU deployment engine supports flexible, adaptable, and upgradeable GPU component deployments. You need to create a GPU component deployment task based on the custom resource (CR) BMCPClusterPolicy.",
    "Arch":[
     "amd64",
     "arm64"
    ],
    "AppType":"BMCP",
    "AppName":"gpu-deploy-engine"
   },
   {
    "AppVersion":"1.2.0",
    "ChartVersion":"1.2.0",
    "Group":"AIComputing",
    "Description":"A cloud-native component that provides Alibaba Platform GPU (APG) user-space virtualization, supporting the isolation of compute capabilities and GPU memory. Currently, only APG is supported. The BMCP GPU toolkit must be installed before use.
",
    "Arch":[
     "amd64",
     "arm64"
    ],
    "AppType":"BMCP",
    "AppName":"kgpu"
   }
  ]
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <Total>3</Total>
 <Apps>
  <AppVersion>1.2.0</AppVersion>
  <ChartVersion>1.2.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>A unified management controller for Bare Metal Computing Platform (BMCP)device plugins (such as DevicePlugin and Exporter). Once deployed, it enables unified management and orchestration of Container Service for Kubernetes (ACK)-side GPU plugins,and installs the Node Feature Discovery (NFD) component to automatically tag nodes.</Description>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>bmcp-gpu-operator</AppName>
 </Apps>
 <Apps>
  <AppVersion>1.0.0</AppVersion>
  <ChartVersion>1.0.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>The BMCP GPU deployment engine supports flexible, adaptable, and upgradeable GPU component deployments. You need to create a GPU component deployment task based on the custom resource (CR) BMCPClusterPolicy.</Description>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>gpu-deploy-engine</AppName>
 </Apps>
 <Apps>
  <AppVersion>1.2.0</AppVersion>
  <ChartVersion>1.2.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>A cloud-native component that provides Alibaba Platform GPU (APG) user-space virtualization, supporting the isolation of compute capabilities and GPU memory. Currently, only APG is supported. The BMCP GPU toolkit must be installed before use.</Description>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>kgpu</AppName>
 </Apps>
</data>
<errorTitle  />
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-11"></a>

#### 5.1.2.11. DescribeApp

Query the details and configuration parameters of an application.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| AppName | Strin g | Quer y | Yes | ai-profiling | The name of the application.<br>You can call the ListApps operation to query the application name. |
| Language | Strin g | Quer y | No | zh_CN | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"AppVersion": "0.1.2", "ChartVersion": "0.1.2", "Description": "AI performance analysis and tuning tool that provides training and inference performance analysis", "Details": "# AI Performance Analysis (ai-profiling) ai-profiling is an AI training and inference performance analysis tool that helps developers optimize model performance.## Components<br>- \*\*ai-profiling\*\*: core performance analysis component ## Functions and features<br>- Training job performance analysis and bottleneck identification<br>- GPU resource utilization monitoring<br>- Inference latency and throughput analysis<br>- Performance optimization suggestions and report generation", "Arch": \[ "amd64"\], "AppType": "BMCP", "AppName": "ai-profiling" } } | The response data. |
|  |  |  |  |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the requeste. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DescribeApp
&AppName=ai-profiling
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "AppVersion":"0.1.2",
   "ChartVersion":"0.1.2",
   "Description":"AI performance analysis and tuning tool that provides training and inference performance analysis",
   "Details":"# AI Performance Analysis (ai-profiling)ai-profiling is an AI training and inference performance analysis tool that helps developers optimize model 
performance.## Components- **ai-profiling**: core performance analysis component## Functions and features- Training job performance analysis and bottleneck identification- GP
U resource utilization monitoring- Inference latency and throughput analysis- Performance optimization suggestions and report generation",
"Arch":[
"amd64"
],
"AppType":"BMCP",
"AppName":"ai-profiling"
}
},
"errorTitle":"",
"requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
"success":true,
"errorMessage":"",
"errorCode":"",
"status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <AppVersion>0.1.2</AppVersion>
  <ChartVersion>0.1.2</ChartVersion>
  <Description>AI performance analysis and tuning tool that provides training and inference performance analysis</Description>
  <Details># AI Performance Analysis (ai-profiling)<br>ai-profiling is an AI training and inference performance analysis tool that helps developers optimize model performance.<br>## Components<br>- **ai-profiling**: core performance analysis component<br>## Functions and features<br>- Training job performance analysis and bottleneck identification<br>- GPU resource utilization monitoring<br>- Inference latency and throughput analysis<br>- Performance optimization suggestions and report generation</Details>
   <Arch>amd64</Arch>
   <AppType>BMCP</AppType>
   <AppName>ai-profiling</AppName>
  </data>
 </data>
 <errorTitle></errorTitle>
 <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
 <success>true</success>
 <errorMessage />
 <errorCode  />
 <status>0</status>
```

<a id="section-5-1-2-12"></a>

#### 5.1.2.12. GetOssStsToken

Obtain an Object Storage Service (OSS) temporary security token (STS Token) for temporary authorized access to Alibaba Cloud OSS resources.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"SecurityToken": "CAISrgJ1q6Ft5B6\* \*\*\*", "Bucket": "baremetal-service-bmcp-cn-wulan-\*\*\*\*-d01", "AccessKeyId": "STS.47W\*\*\*\*cKpt\* \*\*\*wRHDaQf\*\*\*\*", "AccessKeySecret": "Ak2Miq\*\*\*\*LaFsS wrd\*\*\*\*ytZX1\*\*\*\*3 TuhFq9hc\*\*\*\*", "Expiration": "2026-07-28T15:10:49Z", "RegionId": "cn-wulan-\*\*\*\*\*-d01", "EndPoint": "oss-cn-wulan-\*\*\*\*\*-d01-a.intra.\*\*\*\*\*.\*\*\*\*\*.c om" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=GetOssStsToken
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "SecurityToken":"CAISrgJ1q6Ft5B6****",
   "Bucket":"baremetal-service-bmcp-cn-wulan-****-d01",
   "AccessKeyId":"STS.47W****cKpt****wRHDaQf****",
   "AccessKeySecret":"Ak2Miq****LaFsSwrd****ytZX1****3TuhFq9hc****",
   "Expiration":"2026-07-28T15:10:49Z",
   "RegionId":"cn-wulan-*****-d01",
   "EndPoint":"oss-cn-wulan-*****-d01-a.intra.*****.*****.com"
  }
 },
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <SecurityToken>CAISrgJ1q6Ft5B6****</SecurityToken>
  <Bucket>baremetal-service-bmcp-cn-wulan-****-d01</Bucket>
  <AccessKeyId>STS.47W****cKpt****wRHDaQf****</AccessKeyId>
  <AccessKeySecret>Ak2Miq****LaFsSwrd****ytZX1****3TuhFq9hc****</AccessKeySecret>
  <Expiration>2026-07-28T15:10:49Z</Expiration>
  <RegionId>cn-wulan-*****-d01</RegionId>
  <EndPoint>oss-cn-wulan-*****-d01-a.intra.*****.*****.com</EndPoint>
 </data>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-13"></a>

#### 5.1.2.13. UploadCustomApp

Upload a custom application.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| FileType | Strin g | Quer y | Yes | YAML | The type of the application package.Valid values:<br>• YAML<br>• TGZ |
| AddonNam e | Strin g | Quer y | No | test | The name of the application.<br>• This parameter is required when FileType is set to YAML.<br>• This parameter must be left blank when FileType is set to TGZ. |
| AppVersio n | Strin g | Quer y | No | 0.0.1 | The version of the component.<br>• This parameter is required when FileType is set to YAML.<br>• This parameter must be left blank when FileType is set to TGZ. |
| ConfigCont ent | Strin g | Quer y | No | {} | The configuration content.<br>• This parameter is required when FileType is set to YAML. The value must be in YAML format.<br>• This parameter must be left blank when FileType is set to TGZ. |
| OssUrl | Strin g | Quer y | No | https://\*\*\*\*.oss-ap-\*\*\*\*.aliyuncs.com/gpu-deploy-engine-1.0.0.tgz | The Object Storage Service (OSS) Uniform Resource Locator (URL) of the component.<br>• This parameter must be left blank when FileType is set to YAML.<br>• This parameter is required when FileType is set to TGZ. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the component.<br>• This parameter is optional when FileType is set to YAML.<br>• This parameter must be left blank when FileType is set to TGZ. |
| Details | Strin g | Quer y | No | "" | The details of the component.<br>• This parameter is optional when FileType is set to YAML.<br>• This parameter must be left blank when FileType is set to TGZ. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "upload sucess" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UploadCustomApp
&FileType=TGZ
&OssUrl=https://****.oss-ap-****.aliyuncs.com/gpu-deploy-engine-1.0.0.tgz
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"upload success"
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>upload sucess</data>
</data>
<errorTitle></errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-14"></a>

#### 5.1.2.14. ListCustomApps

Query the list of custom components.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SourceTyp e | Strin g | Quer y | No | UPLOAD | The source of the component package. Only UPLOAD is supported. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

<table>
  <tr>
    <td>data</td>
    <td>Map</td>
    <td>{ "PageSize": 12, "PageNumber": 1, "Total": 2, "Items": [ { "ChartVersion": "", "AppVersion": "0.0.2", "Description": "", "Details": "", "FileType": "YAML", "ChartName": "test1", "SourceType": "UPLOAD", "OssPath": "", "CreateTime": "2026-07-21 15:46:40", "UpdateTime": "2026-07-21 15:46:40", "AddonName": "test1" } ] }</td>
    <td>The response data.</td>
  </tr>
  <tr>
    <td>status</td>
    <td>Integer</td>
    <td>0</td>
    <td>The status of the response.</td>
  </tr>
  <tr>
    <td>requestId</td>
    <td>String</td>
    <td>66dfddc6-b547-11ee-aa84-acde4800****</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>success</td>
    <td>Boolean</td>
    <td>true</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>responseVersi on</td>
    <td>String</td>
    <td>v1</td>
    <td>The version of the response.</td>
  </tr>
</table>

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListCustomApps
&SourceType=UPLOAD
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "PageSize":12,
  "PageNumber":1,
  "Total":2,
  "Items":[
   {
    "ChartVersion":"",
    "AppVersion":"0.0.2",
    "Description":"",
    "Details":"",
    "FileType":"YAML",
    "ChartName":"test1",
    "SourceType":"UPLOAD",
    "OssPath":"",
    "CreateTime":"2026-07-21 15:46:40",
    "UpdateTime":"2026-07-21 15:46:40",
    "AddonName":"test1"
   },
   {
    "ChartVersion":"",
    "AppVersion":"0.0.1",
    "Description":"",
    "Details":"",
    "FileType":"YAML",
    "ChartName":"nginx-chart-bw",
    "SourceType":"UPLOAD",
    "OssPath":"",
    "CreateTime":"2026-06-02 10:58:08",
    "UpdateTime":"2026-06-02 10:58:08",
    "AddonName":"nginx-chart-bw"
   }
  ]
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <PageSize>12</PageSize>
 <PageNumber>1</PageNumber>
 <Total>2</Total>
 <Items>
  <ChartVersion  />
  <AppVersion>0.0.2</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>test1</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-07-21 15:46:40</CreateTime>
  <UpdateTime>2026-07-21 15:46:40</UpdateTime>
  <AddonName>test1</AddonName>
 </Items>
 <Items>
  <ChartVersion  />
  <AppVersion>0.0.1</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>nginx-chart-bw</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-06-02 10:58:08</CreateTime>
  <UpdateTime>2026-06-02 10:58:08</UpdateTime>
  <AddonName>nginx-chart-bw</AddonName>
 </Items>
</data>
<errorTitle></errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage></errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-15"></a>

#### 5.1.2.15. DescribeCustomApp

Query the details of a custom component.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| AddonNam e | Strin g | Quer y | Yes | test | The name of the custom component.<br>You can call the ListCustomApps operation to query the custom component name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"ChartVersion": "", "AppVersion": "0.0.2", "Description": "", "Details": "", "FileType": "YAML", "ChartName": "test1", "SourceType": "UPLOAD", "OssPath": "", "CreateTime": "2026-07-21 15:46:40", "UpdateTime": "2026-07-21 15:46:40", "AddonName": "test1" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DescribeCustomApp
&AddonName=test
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "ChartVersion":"",
   "AppVersion":"0.0.2",
   "Description":"",
   "Details":"",
   "FileType":"YAML",
   "ChartName":"test1",
   "SourceType":"UPLOAD",
   "OssPath":"",
   "CreateTime":"2026-07-21 15:46:40",
   "UpdateTime":"2026-07-21 15:46:40",
   "AddonName":"test1"
  }
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <ChartVersion  />
  <AppVersion>0.0.2</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>test1</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-07-21 15:46:40</CreateTime>
  <UpdateTime>2026-07-21 15:46:40</UpdateTime>
  <AddonName>test1</AddonName>
 </data>
</data>
<errorTitle></errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-16"></a>

#### 5.1.2.16. DeleteCustomApp

Delete a custom component.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| AddonNam e | Strin g | Quer y | Yes | test | The name of the custom component.<br>You can call the ListCustomApps operation to query the custom component name. |
| AppVersio n | Strin g | Quer y | Yes | 1.2.0 | The version of the custom component.<br>You can call the ListCustomApps operation to query the custom component and its version. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | {"data": "Delete success"} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteCustomApp
&AddonName=test
&AppVersion=1.2.0
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"Delete success"
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>Delete success</data>
</data>
<errorTitle></errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-17"></a>

#### 5.1.2.17. InstallAiInstanceResource

Install AI instance resources for a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| VswitchIdL ist | Json | Quer y | No | \["vsw-2ze3ds0mdip0hdz8i\*\*\*\*", "vsw-3gagdup8scary04iq\*\*\*\*"\] | The list of vSwitch IDs for master nodes. The number of vSwitches ranges from 1 to 3. To ensure high availability of the cluster, we recommend that you select three vSwitches in different zones. |
| AddonSyst emDiskCat egory | Strin g | Quer y | No | cloud_ssd | The system disk category of the instance where the software is to be installed. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: Solid-State Disk (SSD)<br>• cloud_pperf: Premium Enterprise SSD (ESSD)<br>• cloud_sperf: Basic disk<br>AddonSystemDiskCategor y must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the system disk categories supported by the types of the instance where the software is to be installed. |
| AddonSyst emDiskSiz e | Integ er | Quer y | No | 40 | The system disk size of the instance where the software is to be installed. Unit: GiB. Valid values: 40 to 500 |

<table>
  <tr>
    <td>DataDisk</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[{"Category": "cloud_ssd","Size":60}]</td>
    <td>The list of data disks of the instance where the software is to be installed.<br>WorkerDataDiskList contains the following two fields:<br>• Category: The data disk category. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD<br>• cloud_pperf: Premium ESSD<br>• cloud_sperf: Basic disk<br>• Size: The data disk size. Unit: GiB. Valid values: 40 to 500<br>Category must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the data disk categories supported by the worker node types.</td>
  </tr>
  <tr>
    <td>Platform</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux</td>
    <td>The OS distribution.<br>You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
  <tr>
    <td>ImageId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>aliyun_4_x86_64_20G_co ntainer_optimized_alibase _20260407.vhd</td>
    <td>The ID of the image used by the instance where the software is to be installed.<br>• If this parameter is not specified, the default value is the ID of the image used by the cluster.<br>• To specify a value, call the DescribeKubernetesVer sionMetadata operation to query the IDs of the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
  <tr>
    <td>AddonInst anceTypeL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4x large"]</td>
    <td>The type list of the instance where the software is to be installed. A maximum of 10 instance types can be specified.<br>You can call the ListAckInstanceType operation to query the instance types. The minimum instance type is 16 vCPUs and 16 GB.</td>
  </tr>
</table>

<table>
  <tr>
    <td>Runtime</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>{docker 19.03.5}</td>
    <td>The container runtime.Three runtimes are supported: containerd, Docker, and Sandboxed-Container.runv. Runtime contains the following two fields:<br>• name: The container runtime name<br>• version: The container runtime version<br>You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported runtimes. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
  <tr>
    <td>ClassicSlb Spec</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>slb.s2.small</td>
    <td>The Server Load Balancer (SLB) specification.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "The resource is being installed" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=InstallAiInstanceResource
&ClusterId=ack-8EEjd6****
&VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"]
&AddonSystemDiskCategory=cloud_ssd
&AddonSystemDiskSize=40
&DataDisk=[{"Category": "cloud_ssd","Size":60}]
&Platform=AliyunLinux
&ImageId=aliyun_4_x86_64_20G_container_optimized_alibase_20260407.vhd
&AddonInstanceTypeList=["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4xlarge"]
&Runtime={docker 19.03.5}
&ClassicSlbSpec=slb.s2.small
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The resource is being installed"
 },
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The resource is being installed</data>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-18"></a>

#### 5.1.2.18. UnInstallAiInstanceResource

Uninstall cluster O&M services from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| AppNameL ist | Json | Quer y | No | \["ai-task-inspector","fluid"\] | The list of apps to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {"data": "The resource is being deleted",} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UnInstallAiInstanceResource
&ClusterId=ack-8EEjd6****
&AppNameList=["ai-task-inspector","fluid"]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The resource is being deleted"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The resource is being deleted</data>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-19"></a>

#### 5.1.2.19. InstallAiApplication

Install an application in a Container Service for Kubernetes (ACK) - AI computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK - AI computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | \[ "ai-profiling" \] | The name of the application to install.<br>You can call the ListAckClusterApp operation to query the application name. |
| IsInstallInst anceResou rce | Bool ean | Quer y | No | true | Specifies whether to install resources on the type of the instance where the software is to be installed in the ACK cluster. |
| VswitchIdL ist | Json | Quer y | No | \["vsw-2ze3ds0mdip0hdz8i\*\*\*\*", "vsw-3gagdup8scary04iq\*\*\*\*"\] | The list of vSwitch IDs.Specifies the vSwitches to which the bare metal instances will be connected. |
| AddonSyst emDiskCat egory | Strin g | Quer y | No | cloud_ssd | The system disk category of the instance where the software is to be installed. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: Soliad-State Disk (SSD)<br>• cloud_pperf: Premium Enterprise SSD (ESSD)<br>• cloud_sperf: Basic disk<br>AddonSystemDiskCategor y must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the system disk categories supported by the type of the instance where the software is to be installed. |
| AddonSyst emDiskSiz e | Integ er | Quer y | No | 40 | The system disk size of the instance where the software is to be installed. Unit: GiB. Valid values: 40 to 500 |
| DataDisk | Json | Quer y | No | \[{"Category": "cloud_ssd","Size":60}\] | The list of data disks of the instance where the software is to be installed.<br>DataDiskList contains the following two fields:<br>• Category: The data disk category. Valid values:<br>• cloud_efficiency: Ultra disk<br>• cloud_ssd: SSD<br>• cloud_pperf: ESSD<br>• cloud_sperf: Basic disk<br>• Size: The data disk size. Unit: GiB. Valid values: 40 to 500<br>Category must match AddonInstanceTypeList.You can call the ListInstanceTypeDiskCate gory operation to query the data disk categories supported by the worker node types. |

<table>
  <tr>
    <td>Password</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>Pwd*****</td>
    <td>The logon password of the machines in the cluster.<br>The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.Supported special characters include ()`~!@#$%^&amp;*-_+=|{} []:;'&lt;&gt;,.?/.</td>
  </tr>
  <tr>
    <td>Platform</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>AliyunLinux</td>
    <td>The OS distribution.<br>You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
</table>

<table>
  <tr>
    <td>ImageId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>aliyun_4_x86_64_20G_co ntainer_optimized_alibase _20260407.vhd</td>
    <td>The ID of the image used by the instance where the software is to be installed.<br>• If this parameter is not specified, the default value is the ID of the image used by the cluster.<br>• To specify a value, call the DescribeKubernetesVer sionMetadata operation to query the IDs of supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
  <tr>
    <td>AddonInst anceTypeL ist</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4x large"]</td>
    <td>The type list of the instance where the software is to be installed. A maximum of 10 instance types can be specified.<br>You can call the ListAckInstanceType operation to query the instance types. The minimum instance type is 16 vCPUs and 16 GB.</td>
  </tr>
  <tr>
    <td>AdminUid</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIRootPwd</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIUserNam e</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>AIPwd</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>Accelerato rVendorNa me</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>*</td>
    <td>The name of the Nanhu Insight accelerator vendor.<br>This parameter is required when Nanhu Insight is included in the AppNameList.</td>
  </tr>
  <tr>
    <td>NanhuInsi ghtClusterI d</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>cluster001</td>
    <td>The ID of the Nanhu Insight cluster.<br>This parameter is required when Nanhu Insight is included in the AppNameList.</td>
  </tr>
  <tr>
    <td>PeerEvpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>evpc-***hvitxlfjyso****</td>
    <td>The ID of the peer Enterprise Virtual Private Cloud (EVPC) for Nanhu Insight.<br>This parameter is required when Nanhu Insight is included in the AppNameList.</td>
  </tr>
  <tr>
    <td>Runtime</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>{docker 19.03.5}</td>
    <td>The container runtime.Three runtimes are supported: containerd, Docker, and Sandboxed-Container.runv. Runtime contains the following two fields:<br>• name: The name of the container runtime.<br>• version: The version of the container runtime.<br>You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported runtimes. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide.</td>
  </tr>
  <tr>
    <td>NasEndpoi nt</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>SlbIp</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>192.16*.*.*</td>
    <td>The Server Load Balancer (SLB) IP address.</td>
  </tr>
  <tr>
    <td>ReleaseNa me</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>**</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>Namespac e</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>default</td>
    <td>The namespace.</td>
  </tr>
  <tr>
    <td>AppVersio n</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>1.2.0</td>
    <td>The application version.</td>
  </tr>
  <tr>
    <td>ExtraPara ms</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>{}</td>
    <td>The extra rendering parameters. If the application requires additional rendering variables in <code> key-</code><code>value </code> format, pass them in JSON format.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "The app is being installed"} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=InstallAiApplication
&ClusterId=ack-8EEjd6****
&AppName= [ "ai-profiling" ]
&IsInstallInstanceResource=true
&VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"]
&AddonSystemDiskCategory=cloud_ssd
&AddonSystemDiskSize=40
&DataDisk= [{"Category": "cloud_ssd","Size":60}]
&Platform=AliyunLinux
&ImageId=aliyun_4_x86_64_20G_container_optimized_alibase_20260407.vhd
&AddonInstanceTypeList=["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4xlarge"]
&Runtime={docker 19.03.5}
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The app is being installed"
 },
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The app is being installed</data>
</data>
<errorTitle></errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage></errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-20"></a>

#### 5.1.2.20. UpgradeAiApplication

Upgrade an application in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | ai-profiling | The name of the application to upgrade. |
| ReleaseNa me | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| Namespac e | Strin g | Quer y | No | default | The namespace. |
| AppVersio n | Strin g | Quer y | No | 1.2.0 | The application version. |
| ExtraPara ms | Json | Quer y | No | {} | The extra rendering parameters. If the application requires additional rendering variables as <code> key-</code><code>value </code> pairs, pass them in JSON format. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "The app is being upgraded"} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UpgradeAiApplication
&ClusterId=ack-8EEjd6****
&AppName=ai-profiling
&Namespace=default
&AppVersion=1.2.0
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The app is being upgraded"
 },
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The app is being upgraded</data>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-21"></a>

#### 5.1.2.21. UnInstallAiApplication

Uninstall an application from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | ai-profiling | The name of the application to uninstall. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | {"data": "The app is being uninstalled"} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UnInstallAiApplication
&ClusterId=ack-8EEjd6****
&AppName=ai-profiling
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The app is being uninstalled"
 },
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The app is being uninstalled</data>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-22"></a>

#### 5.1.2.22. ListInstanceTypeDiskCategory

Query the supported disk categories for instance types.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | \*\* | The parameter is deprecated. |
| AckCluster Name | Strin g | Quer y | No | \*\* | This parameter is deprecated. |
| ClusterId | Strin g | Quer y | No | \*\* | The parameter is deprecated. |
| AckCluster Id | Strin g | Quer y | No | \*\* | The parameter is deprecated. |
| Status | Strin g | Quer y | No | \*\* | The parameter is deprecated. |
| InstanceTy peList | Json | Quer y | No | \["ecs.n4.xlarge","ecs.n4.2 xlarge"\] | The list of instance types.<br>You can call the ListAckInstanceType operation to query instance types supported by Container Service for Kubernete (ACK) -intelligent computing clusters. |
| DiskType | Strin g | Quer y | No | SystemDisk | The category of the disk to query. Valid values:<br>• SystemDisk<br>• DataDisk |
| SystemDis kCategory | Strin g | Quer y | No | cloud_ssd | This parameter is required when DiskType is set to DataDisk. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | \[ "cloud_sperf", "cloud_efficiency", "cloud_ssd", "cloud_pperf" \] | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListInstanceTypeDiskCategory
&Department=4
&ResourceGroup=3
&InstanceTypeList=["ecs.n4.xlarge","ecs.n4.2xlarge"]
&DiskType=SystemDisk
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
  "errorCode": "",
  "errorTitle": "",
  "errorMessage": "",
  "code": "",
  "data": [
    "cloud_sperf",
    "cloud_efficiency",
    "cloud_ssd",
    "cloud_pperf"
  ],
  "status": 0,
  "requestId": "d239ef18-a5f1-11ee-a470-16f363c78ec1",
  "success": true,
  "responseVersion": ""
}
```

`XML`  format

```xml
<errorCode  />
<errorTitle  />
<errorMessage  />
<code  />
<data>cloud_sperf</data>
<data>cloud_efficiency</data>
<data>cloud_ssd</data>
<data>cloud_pperf</data>
<status>0</status>
<requestId>d239ef18-a5f1-11ee-a470-16f363c78ec1</requestId>
<success>true</success>
<responseVersion  />
```

<a id="section-5-1-2-23"></a>

#### 5.1.2.23. ListAckClusterEcsWorkerInstances

Query the list of Elastic Compute Service (ECS) worker instances in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call ListAckCluster to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

<table>
  <tr>
    <td>data</td>
    <td>Map</td>
    <td>{ "InstanceList": [{ "InstanceName": "worker-k8s-for-cs-c42bb****b88c260 8634943d67", "NodePoolId": "npba2cfc3a07364 ******d093eb12d5 e", "NodeName": "cn-wula*****68.99.14 4", "InstanceId": "i-0sv0******c4las1h", "State": "running", "CreateTime": "2024-06-20T15:15:24+08:0 0", "IP": "192.***.**.144", "ImageId": "aliyun_2_1903_x8 6_64****_2022111 8.vhd", "InstanceRole": "Worker", "InstanceType": "ecs.sn1.medium", "HostName": "iZ0sv0****4las1hZ ", "NodeStatus": "Ready" } ] }</td>
    <td>The response data.</td>
  </tr>
  <tr>
    <td>status</td>
    <td>Integer</td>
    <td>0</td>
    <td>The status of the response.</td>
  </tr>
  <tr>
    <td>requestId</td>
    <td>String</td>
    <td>66dfddc6-b547-11ee-aa84-acde4800****</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>success</td>
    <td>Boolean</td>
    <td>true</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>responseVersi on</td>
    <td>String</td>
    <td>v1</td>
    <td>The version of the response.</td>
  </tr>
</table>

**Examples**

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "InstanceList":[
   {
    "InstanceName":"worker-k8s-for-cs-c42bb****b88c2608634943d67",
    "NodePoolId":"npba2cfc3a07364******d093eb12d5e",
    "NodeName":"cn-wula*****68.99.144",
    "InstanceId":"i-0sv0******c4las1h",
    "State":"running",
    "CreateTime":"2024-06-20T15:15:24+08:00",
    "IP":"192.***.**.144",
    "ImageId":"aliyun_2_1903_x86_64****_20221118.vhd",
    "InstanceRole":"Worker",
    "InstanceType":"ecs.sn1.medium",
    "HostName":"iZ0sv0****4las1hZ",
    "NodeStatus":"Ready"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <InstanceList>
  <InstanceName>worker-k8s-for-cs-c42bb****b88c2608634943d67</InstanceName>
  <NodePoolId>npba2cfc3a07364******d093eb12d5e</NodePoolId>
  <NodeName>cn-wula*****68.99.144</NodeName>
  <InstanceId>i-0sv0******c4las1h</InstanceId>
  <State>running</State>
  <CreateTime>2024-06-20T15:15:24+08:00</CreateTime>
  <IP>192.***.**.144</IP>
  <ImageId>aliyun_2_1903_x86_64****_20221118.vhd</ImageId>
  <InstanceRole>Worker</InstanceRole>
  <InstanceType>ecs.sn1.medium</InstanceType>
  <HostName>iZ0sv0****4las1hZ</HostName>
  <NodeStatus>Ready</NodeStatus>
 </InstanceList>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-24"></a>

#### 5.1.2.24. DescribeAckClusterLogs

Query the log information of a Container Service for Kubernetes (ACK)-intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK-intelligent computing cluster.<br>You can call ListAckCluster to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": \[ { "Id": "4833\*\*\*\*", "ClusterId": "ack-ZRy3J8\*\*\*\*", "AckClusterId": "c2342\*\*\*\*\*\*7163f d19af\*\*\*", "ClusterLog": "start to update cluster status to CREATE_COMPLET E", "CreateTime": "2026-06-10T10:11:51+08:0 0", "UpdateTime": "2026-06-11T10:11:51+08:0 0" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":[
   {
    "AckClusterId":"c2342******7163fd19af***",
    "ClusterId":"ack-ZRy3J8****",
    "CreateTime":"2026-06-10T10:11:51+08:00",
    "UpdateTime":"2026-06-11T10:11:51+08:00",
    "ClusterLog":"start to update cluster status to CREATE_COMPLETE",
    "Id":"4833****"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <AckClusterId>c2342******7163fd19af***</AckClusterId>
  <ClusterId>ack-ZRy3J8****</ClusterId>
  <CreateTime>2026-06-10T10:11:51+08:00</CreateTime>
  <UpdateTime>2026-06-11T10:11:51+08:00</UpdateTime>
  <ClusterLog>start to update cluster status to CREATE_COMPLETE</ClusterLog>
  <Id>4833****</Id>
 </data>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-25"></a>

#### 5.1.2.25. GetClusterNamespaces

Query the namespace list in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | Yes | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "Namespaces": \["default", "kube-system", "kube-public", "kube-node-lease", "ack-system", "arms-prom", "arms-spyhole" \] } | The response data. |
| status | Integer | 0 | The status of the responsequest. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=GetClusterNamespaces
&ClusterId=ack-8EEjd6****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "Namespaces":[
   "default",
   "kube-system",
   "kube-public",
   "kube-node-lease",
   "ack-system",
   "arms-prom",
   "arms-spyhole"
  ]
 },
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <Namespaces>default</Namespaces>
 <Namespaces>kube-system</Namespaces>
 <Namespaces>kube-public</Namespaces>
 <Namespaces>kube-node-lease</Namespaces>
 <Namespaces>ack-system</Namespaces>
 <Namespaces>arms-prom</Namespaces>
 <Namespaces>arms-spyhole</Namespaces>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-26"></a>

#### 5.1.2.26. ListHistoryEvent

Query the list of historical tasks.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| StartTime | Strin g | Quer y | No | "2026-07-01" | The start time in YYYY-MM-DD format. This parameter specifies the start time of the time range for historical tasks.It is not required if LastAddon is set to true. |
| EndTime | Strin g | Quer y | No | "2026-07-05" | The end time in YYYY-MM-DD format. This parameter specifies the end time of the time range for historical tasks.It is not required if LastAddon is set to true. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| LastAddon | Bool ean | Quer y | No | true | Specifies whether to query only the most recent task. Valid values:<br>• true<br>• false<br>Default value: false |
| EventType | Strin g | Quer y | No | all | The task type. Valid values:<br>• all: All tasks<br>• cluster: Cluster tasks<br>• ai: AI suite tasks<br>Default value: all |
| EventNam e | Strin g | Quer y | No | CreateAckCluster | The task name. Valid values:<br>• CreateBmsCluster<br>• AddBmsInstance<br>• DeleteBmsCluster<br>• DeleteBmsClusterInsta nces<br>• CreateAckCluster<br>• AddAckClusterInstance s<br>• DeleteAckClusterInstan ces<br>• DeleteAckCluster<br>• InstallAiAddon<br>• UnInstallAiAddon<br>• UpgradeAiAddon<br>• UnInstallResource<br>• CreateEhpcCluster<br>• DeleteEhpcCluster<br>• DeleteEhpcClusterInsta nce<br>• RevertBmsMachine<br>• RevertAckMachine<br>• RevertEhpcMachine<br>• CreateBFICluster<br>• ExpandBFICluster<br>• DeleteBFICluster<br>• ShrinkBFICluster<br>• RevertBFIMachine<br>• AddEhpcClusterInstanc e<br>• CreateCpfsClientCluste r<br>• DeleteCpfsClientCluste r<br>• MountFileSystem<br>• UnMountFileSystem<br>• CreateEdaCluster<br>• DeleteEdaCluster |
| Status | Strin g | Quer y | No | success | The task status.<br>• success: Succeeded<br>• failed: Failed<br>• submitted: Submitted<br>• processing: In progress |
| TaskId | Strin g | Quer y | No | 1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\* | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "total": 1, "pageNumber": 1, "data": \[ {"Status": "success", "TaskId": "376ea30f-75b4-11f1-81c7-02420a26\*\*\*\*\*", "EndTime": "2026-07-02T09:20:33+08:0 0", "Message": "success", "RequestId": "376ea30f-75b4-11f1-81c7-02420a26\*\*\*\*\*", "ClusterId": "bfi-6nkkQA\*\*\*\*\*", "CreateTime": "2026-07-02T09:20:31+08:0 0", "StartTime": "2026-07-02T09:20:31+08:0 0", "EventName": "ShrinkBFICluster", "modifyFields": \[ {"paramsValue": \[\], "canModify": false, "paramsKey": "BmsVswitchIdList"}, {"paramsValue": "", "canModify": false, "paramsKey": "EvpcId" }, {"paramsValue": \[\], "canModify": false, "paramsKey": "ApplyFailedInstan ceList" } \], "UpdateTime": "2026-07-02T09:20:33+08:0 0", "ID": 747, "DisplaySummary": false, "events": \[ {"Status": "success", "TaskId": "376ea30f-75b4-11f1-81c7-02420a26\*\*\*\*\*", "EndTime": "2026-07-02T09:20:33+08:0 0", "CreateTime": "2026-07-02T09:20:31+08:0 0", "StartTime": "2026-07-02T09:20:31+08:0 0", "Params": "", "EventStepName": "BatchReleaseInsta nceStep", "IsIgnore": false, "ApplyFailedList": "", "UpdateTime": "2026-07-02T09:20:33+08:0 0", "ClusterBzid": "bfi-6nkkQA\*\*\*\*\*", "ID": 2138, "ErrorMessage": ""} \] } \], "pageSize": 10 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
"2026-07-05"http://[Endpoint]/?Action=ListHistoryEvent
&ClusterId=ack-8EEjd6****
&StartTime="2026-07-01"
&EndTime="2026-07-05"
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":1,
  "data":[
   {
    "Status":"success",
    "TaskId":"376ea30f-75b4-11f1-81c7-02420a26*****",
    "EndTime":"2026-07-02T09:20:33+08:00",
    "Message":"success",
    "RequestId":"376ea30f-75b4-11f1-81c7-02420a26*****",
    "ClusterId":"bfi-6nkkQA*****",
    "CreateTime":"2026-07-02T09:20:31+08:00",
    "StartTime":"2026-07-02T09:20:31+08:00",
    "EventName":"ShrinkBFICluster",
    "modifyFields":[
     {
      "paramsValue":[],
      "canModify":false,
      "paramsKey":"BmsVswitchIdList"
     },
     {
      "paramsValue":"",
      "canModify":false,
      "paramsKey":"EvpcId"
     },
     {
      "paramsValue":[],
      "canModify":false,
      "paramsKey":"ApplyFailedInstanceList"
     }
    ],
    "UpdateTime":"2026-07-02T09:20:33+08:00",
    "ID":747,
    "DisplaySummary":false,
    "events":[
     {
      "Status":"success",
      "TaskId":"376ea30f-75b4-11f1-81c7-02420a26*****",
      "EndTime":"2026-07-02T09:20:33+08:00",
      "CreateTime":"2026-07-02T09:20:31+08:00",
      StartTime:20260702T09:20:31+08:00,
      "Params":"",
      "EventStepName":"BatchReleaseInstanceStep",
      "IsIgnore":false,
      "ApplyFailedList":"",
      "UpdateTime":"2026-07-02T09:20:33+08:00",
      "ClusterBzid":"bfi-6nkkQA*****",
      "ID":2138,
      "ErrorMessage":""
     }
    ]
   }
  ],
  "pageSize":10
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <total>1</total>
 <pageNumber>1</pageNumber>
 <data>
  <Status>success</Status>
  <TaskId>376ea30f-75b4-11f1-81c7-02420a26*****</TaskId>
  <EndTime>2026-07-02T09:20:33+08:00</EndTime>
  <Message>success</Message>
  <RequestId>376ea30f-75b4-11f1-81c7-02420a26*****</RequestId>
  <ClusterId>bfi-6nkkQA*****</ClusterId>
  <CreateTime>2026-07-02T09:20:31+08:00</CreateTime>
  <StartTime>2026-07-02T09:20:31+08:00</StartTime>
  <EventName>ShrinkBFICluster</EventName>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>BmsVswitchIdList</paramsKey>
  </modifyFields>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>EvpcId</paramsKey>
  </modifyFields>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>ApplyFailedInstanceList</paramsKey>
  </modifyFields>
  <UpdateTime>2026-07-02T09:20:33+08:00</UpdateTime>
  <ID>747</ID>
  <DisplaySummary>false</DisplaySummary>
  <events>
   <Status>success</Status>
   <TaskId>376ea30f-75b4-11f1-81c7-02420a26*****</TaskId>
   <EndTime>2026-07-02T09:20:33+08:00</EndTime>
   <CreateTime>2026-07-02T09:20:31+08:00</CreateTime>
   <StartTime>2026-07-02T09:20:31+08:00</StartTime>
   <Params  />
   <EventStepName>BatchReleaseInstanceStep</EventStepName>
   <IsIgnore>false</IsIgnore>
   <ApplyFailedList  />
   <UpdateTime>2026-07-02T09:20:33+08:00</UpdateTime>
   <ClusterBzid>bfi-6nkkQA*****</ClusterBzid>
   <ID>2138</ID>
   <ErrorMessage  />
  </events>
 </data>
 <pageSize>10</pageSize>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-2-27"></a>

#### 5.1.2.27. ListReStartEvent

Retry a cluster task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskId | Strin g | Quer y | No | edbea3ce-76f4-11f1-a9ab-02420a26\*\*\*\* | The task ID.<br>You can call ListHistoryEvent to query the task ID. |
| VswitchIdL ist | Json | Quer y | No | \["vsw-2ze3ds0mdip0hdz8i\*\*\*\*"\] | The vSwitch to which the bare metal instance belongs during retry. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the Enterprise Virtual Private Cloud (EVPC) to which the cluster belongs during retry. |
| DeleteAppl yFailedInst anceName List | Json | Quer y | No | \*\* | The name list of instance names of bare metal instances failed to be createdinstances whose application failed and need to be removed. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the requestsponse. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListReStartEvent
&TaskId=edbea3ce-76f4-11f1-a9ab-02420a26****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":"The retry succeeded",
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>The retry succeeded</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>200</status>
```

<a id="section-5-1-2-28"></a>

#### 5.1.2.28. DeleteAckCluster

Delete a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the ACK -intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| InstanceLis t | Json | Quer y | No | \[ { "hostname": "test", "InstanceId": "i-d8offl6heob05q4v\*\*\*\*", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } \] | The list of bare metal servers to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when servers are released.Valid values:<br>• true: Yes<br>• false: No<br>Default Value: false. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Valid values: 1 to 720.<br>Default value: 168.<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the node from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack-8EEjd6\*\*\*\*", "AckClusterId": "cef51d60a677841 5ab3a8026c24\*\*\*\* \*", "AckClusterName": "cluster-name" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteAckCluster
&ClusterId=ack-8EEjd6****
&InstanceList=[
  {
    "hostname": "test",
    "InstanceId": "i-d8offl6heob05q4v****",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "FlopsCount": 30,
    "VideoMemCount": 30
  }
]
&OsUpdate=true
&RetentionPeriod=168
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-3"></a>

### 5.1.3. Bare metal – supercomputing cluster

<a id="section-5-1-3-1"></a>

#### 5.1.3.1. CreateEhpcCluster

Create a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization, which identifies the organization to which the resource belongs. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set, used to classify and manage resources. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region, which indicates the geological location of the cluster. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the available zone. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster.<br>The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the cluster. The description must be 0 to 1000 characters in length. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The login password for machines in the cluster to ensure cluster security. |
| DeployMod e | Strin g | Quer y | No | Tiny | The deployment type.Only Tiny is supported. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC. |

<table>
  <tr>
    <td>MachineTy peList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq****"} ]</td>
    <td>The list of bare metal server types to be added to the supercomputing cluster.<br>This parameter is required when ClusterArchType is set to standard.</td>
  </tr>
  <tr>
    <td>BmsVswitc hIdList</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>StandardV switchId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>vsw-3gagdup8scary04iq****</td>
    <td>The ID of the vSwitch, used to build the management and control service network channel.</td>
  </tr>
  <tr>
    <td>AccountTy pe</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>Scheduler Type</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>pbs</td>
    <td>The scheduling type.Valid values:<br>• slurm<br>• pbs</td>
  </tr>
  <tr>
    <td>ActivationI d</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>a-hz0ch3SwhOlE1234+Xo3 2lAZC****</td>
    <td>The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard.</td>
  </tr>
  <tr>
    <td>Activation Code</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>4ECEEE12-56F1-4FBC-9AB1-890F1234****</td>
    <td>The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard.</td>
  </tr>
  <tr>
    <td>OsTag</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>null</td>
    <td>This parameter is deprecated.</td>
  </tr>
  <tr>
    <td>EvpcId</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>evpc-htchvitxlfjyso****</td>
    <td>The ID of the Enterprise VPC (EVPC).<br>You can call the ListEvpc operation to query the EVPC ID.</td>
  </tr>
  <tr>
    <td>IsCreateCp fsCluster</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>This parameter is required when ClusterArchType is set to standard. Only true is supported.</td>
  </tr>
  <tr>
    <td>CPFSFileSy stem</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>efs-0137****</td>
    <td>The ID of the high-performance storage file system. Cloud Parallel File System (CPFS) and Apple File System (APFS) file systems are supported.<br>This parameter is optional when ClusterArchType is set to standard.</td>
  </tr>
  <tr>
    <td>SwitchMet hod</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>HSW</td>
    <td>The vSwitch networking mode. Valid values:<br>• CHSW<br>• HSW<br>This parameter is required when ClusterArchType is set to managed.</td>
  </tr>
</table>

<table>
  <tr>
    <td>VolumeInf o</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023-04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, {"VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, {"VolumeType": "mount", "VolumeParams": {"Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ]</td>
    <td>The third-party storage mount information.</td>
  </tr>
  <tr>
    <td>ClusterArc hType</td>
    <td>Strin g</td>
    <td>Quer y</td>
    <td>No</td>
    <td>standard</td>
    <td>The type of the cluster.Valid values:<br>• standard: High-performance computing network<br>• managed: High-performance computing management</td>
  </tr>
</table>

<table>
  <tr>
    <td>ApplyBmsI nstanceLis t</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq****", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234****" } ]</td>
    <td>The list of parameters for requesting bare metal servers.<br>This parameter is required when ClusterArchType is set to managed.</td>
  </tr>
  <tr>
    <td>EnableIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable IPv6. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
  <tr>
    <td>EvpcEnabl eIpv6</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>true</td>
    <td>Specifies whether to enable EVPC IPv6. Valid values:<br>IPv6 can be enabled only when EvpcId is specified.<br>• true: Enable<br>• false: Disable<br>Default value: false.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"ClusterName":"clu ster-name", "ClusterId": "ehpc-FYUr32\*\*\*\*" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateEhpcCluster
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-env***-d01
&ZoneId=cn-wulan-env***-****-a
&ClusterName=cluster-name
&DeployMode=Tiny
&VpcId=vpc-bp1b1xjllp3ve5yze****
&MachineTypeList=[
 {
 "MachineType": "test",
 "Arch": "x86",
 "CpuCount": 2,
 "MemCount": 4,
 "FlopsCount": 4.8,
 "VideoMemCount": 5,
 "NodeCount": 10,
 "VswitchId": "vsw-3gagdup8scary04iq****"
 }
]
&StandardVswitchId=vsw-3gagdup8scary04iq****
&SchedulerType=pbs
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&EvpcId=evpc-htchvitxlfjyso****
&IsCreateCpfsCluster=true
&CPFSFileSystem=efs-0137****
&ClusterArchType=standard
&EnableIpv6=true
&EvpcEnableIpv6=true
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-FYUr32****",
  "ClusterName":"cluster-name"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>ehpc-FYUr32****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-3-2"></a>

#### 5.1.3.2. ListEhpcCluster

Query the list of bare metal - supercomputing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 12 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 12 | The ID of the resource group. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| EhpcCluste rName | Strin g | Quer y | No | cluster-name | The name of the Elastic High Performance Computing (EHPC) cluster. |
| ClusterId | Strin g | Quer y | No | ehpc-FYUr32\*\*\*\* | The ID of the cluster. |
| EhpcCluste rId | Strin g | Quer y | No | ehpc-123sda | The ID of the EHPC cluster. |
| Status | Strin g | Quer y | No | active | The status of the cluster.Valid values:<br>• creating: Creating<br>• active: Running<br>• createFailed: Creation failed<br>• deleting: Deleting<br>• deleteFailed: Deletion failed<br>• scalingDown: Scaling in<br>• scalingDownFailed: Scale-in failed<br>• scalingUp: Scaling out<br>• scalingUpFailed: Scale-out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| Zone | Strin g | Quer y | No | cn-\*\*\*\*-env\*\*-d01-a | The ID of the available zone. |
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster.Valid values:<br>• standard: High performance computing high-network cluster<br>• managed: High performance computing managed cluster |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the Enterprise VPC (EVPC).<br>You can call the ListEvpc operation to query the EVPC ID. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "TotalCount": 2, "PageNumber": 1, "PageSize": 10, "ClusterList": \[ {"ClusterId": "ehpc-SH7mwNVS9r", "ClusterName": "ehpc1", "CpfsClusterState": "", "Description": "Test cluster", "Status": "active", "CreateTime": "2023-11-29T17:08:15+08:0 0", "UpdateTime": "2023-12-08T10:25:37+08:0 0", "NodeCount": 3, "ActiveNodeCount": 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "local", "Organization": "zpf", "ResourceGroup": "zpf1", "VpcId": "vpc-xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc-xxx", "Zone": "xxxxx", "IsSetPassword": true, "SchedulerType": "slurm" }, {"ClusterId": "ehpc-sdfsdfsd", "ClusterName": "ehpc2", "Description": "test", "Status": "active", "CreateTime": "2023-12-07T10:00:00+08:0 0", "UpdateTime": "2023-12-07T10:00:00+08:0 0", "NodeCount": 2, "CpuCount": 11, "MemCount": 12, "FlopsCount": 13, "VideoMemory": 50, "Region": "local", "Organization": "zpf", "ResourceGroup": "zpf1", "VpcId": "vpc-xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc-xxx", "Zone": "xxxxx", "IsSetPassword": true, "SchedulerType": "slurm" } \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":2,
  "ClusterList":[
   {
    "Status":"active",
    "Description":"Test cluster",
    "ActiveNodeCount":1,
    "Organization":"zpf",
    "IsSetPassword":true,
    "NodeCount":3,
    "ClusterId":"ehpc-SH7mwNVS9r",
    "Zone":"xxxxx",
    CreateTime:20231129T17:08:15+08:00,
    "SchedulerType":"slurm",
    "CpfsClusterState":"",
    "MemCount":36,
    "EvpcId":"evpc-xxx",
    "ClusterArchType":"standard",
    "FlopsCount":50,
    "CpuCount":10,
    "VpcId":"vpc-xxxxxxx",
    "UpdateTime":"2023-12-08T10:25:37+08:00",
    "ClusterName":"ehpc1",
    "Region":"local",
    "VideoMemory":50,
    "ResourceGroup":"zpf1"
   },
   {
    "Status":"active",
    "Description":"test",
    "Organization":"zpf",
    "IsSetPassword":true,
    "NodeCount":2,
    "ClusterId":"ehpc-sdfsdfsd",
    "Zone":"xxxxx",
    "CreateTime":"2023-12-07T10:00:00+08:00",
    "SchedulerType":"slurm",
    "MemCount":12,
    "EvpcId":"evpc-xxx",
    "ClusterArchType":"standard",
    "FlopsCount":13,
    "CpuCount":11,
    "VpcId":"vpc-xxxxxxx",
    "UpdateTime":"2023-12-07T10:00:00+08:00",
    "ClusterName":"ehpc2",
    "Region":"local",
    "VideoMemory":50,
    "ResourceGroup":"zpf1"
   }
  ],
  "PageSize":10,
  "PageNumber":1
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>2</TotalCount>
 <ClusterList>
  <Status>active</Status>
  <Description>Test cluster</Description>
  <ActiveNodeCount>1</ActiveNodeCount>
  <Organization>zpf</Organization>
  <IsSetPassword>true</IsSetPassword>
  <NodeCount>3</NodeCount>
  <ClusterId>ehpc-SH7mwNVS9r</ClusterId>
  <Zone>xxxxx</Zone>
  <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
  <SchedulerType>slurm</SchedulerType>
  <CpfsClusterState />
  <MemCount>36</MemCount>
  <EvpcId>evpc-xxx</EvpcId>
  <ClusterArchType>standard</ClusterArchType>
  <FlopsCount>50</FlopsCount>
  <CpuCount>10</CpuCount>
  <VpcId>vpc-xxxxxxx</VpcId>
  <UpdateTime>2023-12-08T10:25:37+08:00</UpdateTime>
  <ClusterName>ehpc1</ClusterName>
  <Region>local</Region>
  <VideoMemory>50</VideoMemory>
  <ResourceGroup>zpf1</ResourceGroup>
 </ClusterList>
 <ClusterList>
  <Status>active</Status>
  <Description>test</Description>
  <Organization>zpf</Organization>
  <IsSetPassword>true</IsSetPassword>
  <NodeCount>2</NodeCount>
  <ClusterId>ehpc-sdfsdfsd</ClusterId>
  <Zone>xxxxx</Zone>
  <CreateTime>2023-12-07T10:00:00+08:00</CreateTime>
  <SchedulerType>slurm</SchedulerType>
  <MemCount>12</MemCount>
  <EvpcId>evpc-xxx</EvpcId>
  <ClusterArchType>standard</ClusterArchType>
  <FlopsCount>13</FlopsCount>
  <CpuCount>11</CpuCount>
  <VpcId>vpc-xxxxxxx</VpcId>
  <UpdateTime>2023-12-07T10:00:00+08:00</UpdateTime>
  <ClusterName>ehpc2</ClusterName>
  <Region>local</Region>
  <VideoMemory>50</VideoMemory>
  <ResourceGroup>zpf1</ResourceGroup>
 </ClusterList>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-3-3"></a>

#### 5.1.3.3. DescribeEhpcCluster

Query the details of a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ehpc-TsrIaN\*\*\*\* | The ID of the bare metal -supercomputing cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterId": "ehpc-SH7mwNVS9r", "ClusterName": "ehpc1", "Description": "Test cluster", "Status": "scalingDown", "CreateTime": "2023-11-29T17:08:15+08:0 0", "UpdateTime": "2023-12-13T15:15:25+08:0 0", "NodeCount": 3, "ActiveNodeCount": 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "cn-\*\*\*\*-env\*\*-d01", "Organization": "zpf", "ResourceGroup": "zpf1", "InstanceList": \["11", "22", "33" \], "VpcId": "vpc-xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc-67mby5210ty3ul\*\* \*\*", "Zone": "cn-\*\*\*\*-env\*\*-d01-a", "IsSetPassword": true, "SchedulerType": "slurm", "CpfsClusterType": "CPFS", "CpfsMountFs": "xxxx", "CpfsClusterState": "", "EnableIpv6": false, "EvpcEnableIpv6": false } | The response data. |
|  |  |  |  |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DescribeEhpcCluster
&ClusterId=ehpc-TsrIaN****
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "Description":"Test cluster",
  "Organization":"zpf",
  "IsSetPassword":true,
  "CpfsClusterType":"CPFS",
  "EvpcId":"evpc-67mby5210ty3ul****",
  "EnableIpv6":false,
  "FlopsCount":50,
  "CpuCount":10,
  "EvpcEnableIpv6":false,
  "ClusterName":"ehpc1",
  "ResourceGroup":"zpf1",
  "Status":"scalingDown",
  "ActiveNodeCount":1,
  "NodeCount":3,
  "ClusterId":"ehpc-SH7mwNVS9r",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "SchedulerType":"slurm",
  "CpfsClusterState":"",
  "MemCount":36,
  "ClusterArchType":"standard",
  "VpcId":"vpc-xxxxxxx",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "Region":"cn-****-env**-d01",
  "CpfsMountFs":"xxxx",
  "VideoMemory":50,
  "InstanceList":[
   "11",
   "22",
   "33"
  ]
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <Description>Test cluster</Description>
 <Organization>zpf</Organization>
 <IsSetPassword>true</IsSetPassword>
 <CpfsClusterType>CPFS</CpfsClusterType>
 <EvpcId>evpc-67mby5210ty3ul****</EvpcId>
 <EnableIpv6>false</EnableIpv6>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <EvpcEnableIpv6>false</EvpcEnableIpv6>
 <ClusterName>ehpc1</ClusterName>
 <ResourceGroup>zpf1</ResourceGroup>
 <Status>scalingDown</Status>
 <ActiveNodeCount>1</ActiveNodeCount>
 <NodeCount>3</NodeCount>
 <ClusterId>ehpc-SH7mwNVS9r</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <SchedulerType>slurm</SchedulerType>
 <CpfsClusterState />
 <MemCount>36</MemCount>
 <ClusterArchType>standard</ClusterArchType>
 <VpcId>vpc-xxxxxxx</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <Region>cn-****-env**-d01</Region>
 <CpfsMountFs>xxxx</CpfsMountFs>
 <VideoMemory>50</VideoMemory>
 <InstanceList>11</InstanceList>
 <InstanceList>22</InstanceList>
 <InstanceList>33</InstanceList>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-3-4"></a>

#### 5.1.3.4. AddEhpcClusterInstances

Scale out a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ehpc-FYUr32\*\*\*\* | The ID of the bare metal -supercomputing cluster.<br>You can call the ListEhpcCluster operation to query the cluster ID. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The bare metal server password to be modified.<br>If no password has been set for the cluster, you must specify this parameter. |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal server types to be added to the supercomputing cluster.<br>This parameter is required when ClusterArchType is set to standard. |
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |
| ActivationI d | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The ID of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The code of the Cloud Assistant activation code.<br>This parameter is required when ClusterArchType is set to standard. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the available zone. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | \[ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*", "ActivationId": "a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\*", "ActivationCode": "4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\*" } \] | The list of parameters for requesting bare metal servers.<br>This parameter is required when ClusterArchType is set to managed. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "test", "ClusterId": "ehpc-WbetRt\*\*\*\*"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=AddEhpcClusterInstances
&ClusterId=ehpc-FYUr32****
&Password=Pwd*****
&ZoneId=cn-wulan-env***-****-a
&MachineTypeList= 
[
 {
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30,
 "InstanceName": "myinstance",
 "UseOriginImage": true,
 "ImageType": "",
 "Image": "",
 "HostName": "xxx",
 "InstanceAlias": "xxx",
 "Description": "testDescription",
 "NodePoolName": "bmcp-node-pool",
 "VswitchId": "vsw-3gagdup8scary04iq****"
 }
]
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-3-5"></a>

#### 5.1.3.5. DeleteEhpcClusterInstances

Scale in a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ehpc-TsrIaN\*\*\*\* | The ID of the bare metal -supercomputing cluster.<br>You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | \["i-d92sc86heobfdsc1\*\*\*\*"\] | The list of node IDs to be removed from the cluster. |
| InstanceLis t | Json | Quer y | No | \[ { "hostname": "test", "InstanceId": "i-d8offl6heob05q4v\*\*\*\*", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } \] | The list of bare metal servers to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released.<br>• true: Clean<br>• false: Do not clean |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Value range: 1 to 720.<br>Default value: 168.<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "test", "ClusterId": "ehpc-WbetRt\*\*\*\*"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteEhpcClusterInstances
&ClusterId=ehpc-FYUr32****
&InstanceIdList=["i-d92sc86heobfdsc1****","i-d8t4ltuheob3s2j0****"]
&ZoneId=cn-wulan-env***-****-a
&InstanceList= 
[
 {
 "hostname": "test",
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
 }
] 
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-3-6"></a>

#### 5.1.3.6. DeleteEhpcCluster

Delete a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ehpc-FYUr32\*\*\*\* | The ID of the bare metal -supercomputing cluster.<br>You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceLis t | Json | Quer y | No | \[ { "hostname": "test", "InstanceId": "i-d8offl6heob05q4v\*\*\*\*", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } \] | The list of bare metal servers to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released.Valid values:<br>• true: Yes<br>• false: No<br>Default value: false. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Value range: 1 to 720.<br>Default value: 168.<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"ClusterName":"tes t", "ClusterId": "ehpc-WbetRt\*\*\*\*"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteEhpcCluster
&ClusterId=ehpc-FYUr32****
&InstanceList=[
 {
 "hostname": "test",
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
 }
]
&OsUpdate=true
&RetentionPeriod=168
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-1-4"></a>

### 5.1.4. Converged computing cluster

<a id="section-5-1-4-1"></a>

#### 5.1.4.1. CreateBFICluster

Create a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The cluster name, which must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The cluster description, which must be 0 to 1,000 characters in length. |
| Password | Strin g | Quer y | No | Pwd\*\*\*\*\* | The login password of the machines in the cluster.<br>The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters, including ()\`~!@#$%^&amp;\*-_+=\|{} \[\]:;'&lt;&gt;,.?/ |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the zone. |
| ClusterArc hType | Strin g | Quer y | No | standard | The cluster type. Valid values:<br>• standard: converged high-bandwidth network<br>• base: converged basic |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal server types to be added to the cluster. |
| VswitchIdL ist | Json | Quer y | No | null | This parameter is deprecated. |
| StandardV switchId | Strin g | Quer y | No | vsw-3gagdup8scary04iq\*\*\*\* | The ID of the vSwitch for building the management and control service network channel. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard.<br>You can call the ListEvpc operation to query the EVPC ID. |
| ActivationI d | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The ID of the Cloud Assistant activation code. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The code of the Cloud Assistant activation code. |
| IsCreateCp fsCluster | Bool ean | Quer y | No | true | Specifies whether to enable the high-performance storage client cluster. Valid values:<br>• true: Enable the cluster.<br>• false: Disable the cluster.<br>Default value: false<br>This parameter can be configured when ClusterArchType is set to standard.<br>To enable the high-performance storage cluster, make sure that an EVPC ID is selected, the number of Cloud Parallel File System (CPFS)-type bare metal nodes is at least 3, and the number of Apple File System (APFS)-bare metal nodes is at least 1. |
| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of the high-performance storage client cluster. Valid values:<br>• CPFS<br>• APFS<br>This parameter is required when IsCreateCpfsCluster is set to true. |
| IsInstallYu ndunAegis | Bool ean | Quer y | No | true | Specifies whether to install Server Guard. Valid values:<br>• true: Install Server Guard.<br>• false: Do not install Server Guard.<br>Default value: true |
| SwitchMet hod | Strin g | Quer y | No | HSW | The switch networking method. Currently, only EHSW is supported. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values:<br>• true: Enable IPv6.<br>• false: Disable IPv6.<br>Default value: false |
| EvpcEnabl eIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable EVPC IPv6.<br>EVPC IPv6 can be enabled only when EvpcId is configured.<br>• true: Enable EVPC IPv6.<br>• false: Disable EVPC IPv6.<br>Default value: false |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p\*\*\*\* | The security group ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {"ClusterName":"clu ster-name", "ClusterId": "bfi-ZZMA5n\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateBFICluster
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-env***-d01
&ZoneId=cn-wulan-env***-****-a
&VpcId=vpc-bp1b1xjllp3ve5yze****
&ClusterName=cluster-name
&ClusterArchType=standard
&MachineTypeList=[
  {
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "VswitchId": "vsw-3gagdup8scary04iq****"
  }
]
&StandardVswitchId=vsw-3gagdup8scary04iq****
&EvpcId=evpc-htchvitxlfjyso****
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&IsCreateCpfsCluster=true
&CpfsClusterType=CPFS
&SwitchMethod=EHSW
&EnableIpv6=true
&EvpcEnableIpv6=true
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-4-2"></a>

#### 5.1.4.2. ListBFICluster

Query the list of converged computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n\*\*\*\* | The ID of the converged computing cluster. |
| Status | Strin g | Quer y | No | active | The cluster status. Valid values:<br>• creating: Creating<br>• active: Running<br>• createFailed: Creation failed<br>• deleting: Deleting<br>• deleteFailed: Deletion failed<br>• scalingDown: Scaling in<br>• scalingDownFailed: Scale-in failed<br>• scalingUp: Scaling out<br>• scalingUpFailed: Scale-out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterList": \[ {"Description": "ycc-apfs", "Organization": "5", "IsSetPassword": true, "SwitchMethod": "CHSW", "CpfsClusterType": "APFS", "Gpu": \[ {"GpuNum": 32, "GpuModel": "NVIDIA_Ampere_A 100_80G_NVLink" }\], "EvpcId": "evpc-pi2q\*\*\*z8b", "EnableIpv6": false, "FlopsCount": 9984, "VolumeId": "", "Department": 5, "CpuCount": 512, "ClusterName": "ycc-apfs", "ResourceGroup": 4, "Status": "active", "ActiveNodeCount": 4, "NodeCount": 4, "ClusterId": "bfi-v8\*\*\*QVZT", "Zone": "cn-ne\*\*\*\*test236001-a", "CreateTime": "2026-01-12T10:44:46+08:0 0", "Specification": \[ { "Count": 3, "Name": "gBMC-Ci8af8nbr" } \], "CpfsClusterState": "error", "AscmCreateUser": "admin", "MemCount": 8192, "ClusterArchType": "standard", "VpcId": "vpc-7kkjbu\*\*\*\*od7pxs6 10", "OldClusterBzid": "", "UpdateTime": "2026-01-22T15:58:01+08:0 0", "Region": "cn-ne\*\*\*\*6e-d01", "CpfsMountFs": "efs-01\*\*\*08", "RegionId": "cn-\*\*\*\*-d01", "VideoMemory": 2560, "EnableIpv6": true, "EvpcEnableIpv6": true } \], "PageSize": 10, "TotalCount": 3, "PageNumber": 1 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ListBFICluster
&Department=4
&ResourceGroup=3
&Status=active
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":3,
  "ClusterList":[
   {
    "Description":"ycc-apfs",
    "Organization":"5",
    "IsSetPassword":true,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"APFS",
    "Gpu":[
     {
      "GpuNum":32,
      "GpuModel":"NVIDIA_Ampere_A100_80G_NVLink"
     }
    ],
    "EvpcId":"evpc-pi2q***z8b",
    "EnableIpv6":true,
    "FlopsCount":9984,
    "VolumeId":"",
    "Department":5,
    "CpuCount":512,
    "EvpcEnableIpv6":true,
    "ClusterName":"ycc-apfs",
    "ResourceGroup":4,
    "Status":"active",
    "ActiveNodeCount":4,
    "NodeCount":4,
    "ClusterId":"bfi-v8***QVZT",
    "Zone":"cn-ne****test236001-a",
    "CreateTime":"2026-01-12T10:44:46+08:00",
    "Specification":[
     {
      "Count":3,
      "Name":"gBMC-Ci8af8nbr"
     }
    ],
    "CpfsClusterState":"error",
    "AscmCreateUser":"admin",
    "MemCount":8192,
    "ClusterArchType":"standard",
    "VpcId":"vpc-7kkjbu****od7pxs610",
    "OldClusterBzid":"",
    "UpdateTime":"2026-01-22T15:58:01+08:00",
    "Region":"cn-ne****6e-d01",
    "CpfsMountFs":"efs-01***08",
    "RegionId":"cn-****-d01",
    "VideoMemory":2560
   }
  ],
  "PageSize":10,
  "PageNumber":1
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>3</TotalCount>
 <ClusterList>
  <Description>ycc-apfs</Description>
  <Organization>5</Organization>
  <IsSetPassword>true</IsSetPassword>
  <SwitchMethod>CHSW</SwitchMethod>
  <CpfsClusterType>APFS</CpfsClusterType>
  <Gpu>
   <GpuNum>32</GpuNum>
   <GpuModel>NVIDIA_Ampere_A100_80G_NVLink</GpuModel>
  </Gpu>
  <EvpcId>evpc-pi2q***z8b</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <FlopsCount>9984</FlopsCount>
  <VolumeId  />
  <Department>5</Department>
  <CpuCount>512</CpuCount>
  <EvpcEnableIpv6>true</EvpcEnableIpv6>
  <ClusterName>ycc-apfs</ClusterName>
  <ResourceGroup>4</ResourceGroup>
  <Status>active</Status>
  <ActiveNodeCount>4</ActiveNodeCount>
  <NodeCount>4</NodeCount>
  <ClusterId>bfi-v8***QVZT</ClusterId>
  <Zone>cn-ne****test236001-a</Zone>
  <CreateTime>2026-01-12T10:44:46+08:00</CreateTime>
  <Specification>
   <Count>3</Count>
   <Name>gBMC-Ci8af8nbr</Name>
  </Specification>
  <CpfsClusterState>error</CpfsClusterState>
  <AscmCreateUser>admin</AscmCreateUser>
  <MemCount>8192</MemCount>
  <ClusterArchType>standard</ClusterArchType>
  <VpcId>vpc-7kkjbu****od7pxs610</VpcId>
  <OldClusterBzid  />
  <UpdateTime>2026-01-22T15:58:01+08:00</UpdateTime>
  <Region>cn-ne****6e-d01</Region>
  <CpfsMountFs>efs-01***08</CpfsMountFs>
  <RegionId>cn-****-d01</RegionId>
  <VideoMemory>2560</VideoMemory>
 </ClusterList>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-4-3"></a>

#### 5.1.4.3. DescribeBFICluster

Query the details of a Big Data Federation Infrastructure (BFI) cluster, including cluster status, node list, resource configuration, and runtime metrics.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n\*\*\*\* | The ID of the converged computing cluster.<br>You can call the ListBFICluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "Status": "active", "Description": "testDescription", "ActiveNodeCount": 1, "Organization": "4", "IsSetPassword": true, "NodeCount": 3, "ClusterId": "bfi-ZZMA5n\*\*\*\*", "Zone": "cn-\*\*\*\*-env\*\*-d01-a", "CreateTime": "2023-11-29T17:08:15+08:0 0", "MemCount": 36, "EvpcId": "evpc-htchvitxlfjyso\*\*\*\*", "ClusterArchType": "standard", "FlopsCount": 50, "CpuCount": 10, "VpcId": "vpc-bp1b1xjllp3ve5yze \*\*\*\*", "UpdateTime": "2023-12-13T15:15:25+08:0 0", "ClusterName": "cluster-name", "Region": "cn-\*\*\*\*-env\*\*-d01", "VideoMemory": 50, "InstanceList": \[ "i-d8offheheob5qaf0\* \*\*\*", "i-d620b2eheobcabte \*\*\*\*", "i-d75ppnuheobcnhq o\*\*\*\*" \], "ResourceGroup": "3" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeBFICluster
&ClusterId=bfi-ZZMA5n****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"1.0",
 "data":{
  "Status":"active",
  "Description":"testDescription",
  "ActiveNodeCount":1,
  "Organization":"4",
  "IsSetPassword":true,
  "NodeCount":3,
  "ClusterId":"bfi-ZZMA5n****",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "MemCount":36,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "ClusterArchType":"standard",
  "FlopsCount":50,
  "CpuCount":10,
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "ClusterName":"cluster-name",
  "Region":"cn-****-env**-d01",
  "VideoMemory":50,
  "InstanceList":[
   "i-d8offheheob5qaf0****",
   "i-d620b2eheobcabte****",
   "i-d75ppnuheobcnhqo****"
  ],
  "ResourceGroup":"3"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>1.0</responseVersion>
<data>
 <Status>active</Status>
 <Description>testDescription</Description>
 <ActiveNodeCount>1</ActiveNodeCount>
 <Organization>4</Organization>
 <IsSetPassword>true</IsSetPassword>
 <NodeCount>3</NodeCount>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <MemCount>36</MemCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <ClusterArchType>standard</ClusterArchType>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <ClusterName>cluster-name</ClusterName>
 <Region>cn-****-env**-d01</Region>
 <VideoMemory>50</VideoMemory>
 <InstanceList>i-d8offheheob5qaf0****</InstanceList>
 <InstanceList>i-d620b2eheobcabte****</InstanceList>
 <InstanceList>i-d75ppnuheobcnhqo****</InstanceList>
 <ResourceGroup>3</ResourceGroup>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-4-4"></a>

#### 5.1.4.4. ExpandBFICluster

Scale out a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n\*\*\*\* | The ID of the converged computing cluster.<br>You can call the ListBFICluster operation to query the cluster ID. |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal server types to be added to the cluster.<br>This parameter is required when ClusterArchType is set to standard or base. |
| VswitchIdL ist | Json | Quer y | No | \["vsw-2ze3ds0mdip0hdz8i\*\*\*\*", "vsw-3gagdup8scary04iq\*\*\*\*"\] | The vSwitch list for the node pool, used for network configuration. |
| ActivationI d | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The ID of the Cloud Assistant activation code. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The code of the Cloud Assistant activation code. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the zone where the clutser is deployed. |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p\*\*\*\* | The security group ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "bfi-ZZMA5n\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the API response, which is used to handle APIs of different versions. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ExpandBFICluster
&ClusterId=bfi-ZZMA5n****
&MachineTypeList=[
  {
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "VswitchId": "vsw-3gagdup8scary04iq****"
  }
]
&VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"]
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC****
&ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&ZoneId=cn-wulan-env***-****-a
&SecurityGroupId=sg-bp67acfmxazb4p****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"1.0",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>1.0</responseVersion>
<data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-4-5"></a>

#### 5.1.4.5. ShrinkBFICluster

Scale in a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bfi-FYUr32\*\*\*\* | The ID of the converged computing cluster.<br>You can call the ListBFICluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | \["1","2"\] | The ID list of instances to be removed from the cluster. |
| InstanceLis t | Json | Quer y | No | \[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373\*\*\*\*", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } \] | The list of bare metal instances to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released.Valid values:<br>• true: Clean data disks.<br>• false: Do not clean data disks. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period.Unit: hours. Valid values: 1 to 720<br>Default value: 168<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {"ClusterName":"clu ster-name", "ClusterId": "bfi-ZZMA5n\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http(s)://[Endpoint]/?Action=ShrinkBFICluster
&ClusterId=bfi-FYUr32****
&InstanceIdList=["11","21"]
&ZoneId=cn-wulan-env***-****-a
&InstanceList=    
[
  {
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
  }
]  
&OsUpdate=true
&RetentionPeriod=168
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-4-6"></a>

#### 5.1.4.6. DeleteBFICluster

Delete a specified converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bfi-FYUr32\*\*\*\* | The ID of the converged computing cluster.<br>You can call the ListBFICluster operation to query the cluster ID. |
| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released.<br>• true: Clean data disks.<br>• false: Do not clean data disks. |

<table>
  <tr>
    <td>RetentionP eriod</td>
    <td>Integ er</td>
    <td>Quer y</td>
    <td>No</td>
    <td>5</td>
    <td>The retention period of instances in the recycle bin. Unit: hours. Valid values: 1 to 720<br>Default value: 168<br>After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool.</td>
  </tr>
  <tr>
    <td>InstanceLis t</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ]</td>
    <td>The list of bare metal instances to be removed from the cluster.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | {"ClusterName":"clu ster-name", "ClusterId": "bfi-ZZMA5n\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteBFICluster
&ClusterId=bfi-ZZMA5n****
&OsUpdate=false
&RetentionPeriod=5
&InstanceList=[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": 
"980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, 
"VideoMemCount": 30 } ]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
 },
 "errorTitle":"",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data>
<errorTitle></errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-1-5"></a>

### 5.1.5. ListInstance

Query the list of Bare Metal Computing Platform (BMCP) instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| InstanceN ame | Strin g | Quer y | No | myinstance | The instance name. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"DeployType": "bfi_base", "RunningState": "offline", "CGWPorts": "TwoHundredGigE1/0/65:1,TwoHundre dGigE1/0/65:2,Two HundredGigE1/0/6 6:1,TwoHundredGi gE1/0/66:2", "IDC": "amtest\*\*\*\*", "SANZone": "", "Image": "alinux_3_x86_64_aiext_20260623_bf 3.qcow2", "InnerBandwidth": "", "Gpu": "", "ImageType": "", "InstanceAlias": "i-7c4ba42a32f64\*\*\* \*", "AliYunAssistID": "mi-rg6owzr81e\*\*\*\*", "ID": 108, "Disk": 0, "RawIP": "192.168.\*\*\*.\*\*\*", "HostName": "SN-2106196KUPXDP50 0\*\*\*\*", "Disable": false, "ErrorDescription": "\[a-87c59321-7ac5-11f1-9014-02420a2608cd\]reo nlineNcEni timeout, eniList not ready", "Status": "power_on", "DeviceModel": "BFIBaseStack", "Protected": true, "IP": "192.168.\*\*\*.\*\*\*", "DefaultHostName": "SN-2106196KUPXDP50 0\*\*\*\*", "PrimaryEniId": "eni-9lpy8hgva2pl0g\*\*\* \*", "WarrantyPeriod": "2027-01-01T00:00:00+08:0 0", "InstanceName": "i-d8t4ltuheob3s2j0\*\* \*\*", "SecondaryEniId": "eni-3ga00weu4ouu93b c\*\*\*\*", "SSHUser": "", "State": "error", "BMCIP": "10.38.\*\*\*.\*\*\*\*", "Region": "cn-wulan-\*\*\*\*-d01", "NetworkCardType ": "", "AgentID": 48, "Subnet": "EHSW-1-\*\*\*\*-A-\*\*\*\*", "RackUnit": "21", "Organization": "4", "Description": "", "VPCID": "vpc-3gasnqceysuxdia5 k\*\*\*\*", "ImageSize": 0, "IPv6": "", "Config": { "Memory": 0, "CPUNumber": 0 }, "BMCPassword": "", "DpuInfo": {"ErrorDescription": "", "Status": "power_on", "LoginName": "root", "MachineSN": "2106196KUPXDP5 00\*\*\*\*", "RunningState": "running", "CGWPorts": "THGigabitEthe\*\*\*\* 0/20:1,THGigabitEt hernet0/20:1", "Zone": "", "Hostname": "c25d0\*\*\*\*.cloud.d 03.am\*\*\*\*", "MachineType": "PG58P2M6S2\*\*\*\*.32", "BMCPassword": "\*\*\*\*", "Specification": "", "BMCPort": "", "InstanceName": "dpu-i-0919\*\*\*\*ad914\*\*\*\* ", "BMCIP": "10.38.\*\*\*.\*\*\*\*", "LastHeartbeatTim e": "2026-07-15T17:28:46+08:0 0", "ID": 1, "SN": "MT2430XZ\*\*\*\*", "BMCUser": "\*\*\*\*", "ASWID": "\*\*\*\*", "Subnet": "", "RawIP": "10.38.\*\*\*.\*\*\*", "LoginPwd": "" }, "SSHRsaId": "", "MappingStatus": "OperatedFailed", "Rack": "D03", "ApplicationGroup": "instance", "GpuNum": 0, "NetworkCardNum": 0, "SubnetIP": "10.38.\*\*\*.\*\*\*", "VPCSubnet": "vsw-3ga970i9dqzq7byb m\*\*\*\*", "SN": "\*\*\*\*", "BMCUser": "\*\*\*\*", "Deleted": false, "Room": "C2-5", "ResourceGroup": "3", "SSHPwd": "", "ImageUniqueKey": "", "UserName": "", "OS": "", "UnitNum": 0, "Zone": "cn-wulan-\*\*\*\*-amte\*\*\*\*-a", "CreateTime": "2026-06-24T17:19:05+08:0 0", "MachineType": "PG58P2M6S\*\*\*\*.3 2", "NetworkMode": "vpc", "CPUArch": "", "BMCPort": "", "WWN": "", "Extra": "", "DefaultImage": "alinux_3_x86_64_aiext_20260623_bf 3.qcow2", "UserId": "127756957048\*\*\* \*", "UpdateTime": "2026-07-08T20:26:43+08:0 0", "LastHeartbeatTim e": "2026-07-09T13:54:42+08:0 0", "ASWID": "\*\*\*\*", "Tag": "" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request.<br>• true: Success<br>• false: Failure |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListInstance
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "DeployType":"bfi_base",
   "RunningState":"offline",
   
"CGWPorts":"TwoHundredGigE1/0/65:1,TwoHundredGigE1/0/65:2,TwoHundredGigE1/0/66:1,TwoHundr
GigE1/0/66:2",
   "IDC":"amtest****",
   "SANZone":"",
   "Image":"alinux_3_x86_64_aiext_20260623_bf3.qcow2",
   "InnerBandwidth":"",
   "Gpu":"",
   "ImageType":"",
   "InstanceAlias":"i-7c4ba42a32f64****",
   "AliYunAssistID":"mi-rg6owzr81e****",
   "ID":108,
   "Disk":0,
   "RawIP":"192.168.***.***",
   "HostName":"SN-2106196KUPXDP500****",
   "Disable":false,
   "ErrorDescription":"[a-87c59321-7ac5-11f1-9014-02420a2608cd]reonlineNcEni timeout, eniList not ready",
   "Status":"power_on",
   "DeviceModel":"BFIBaseStack",
   "Protected":true,
   "IP":"192.168.***.***",
   "DefaultHostName":"SN-2106196KUPXDP500****",
   "PrimaryEniId":"eni-9lpy8hgva2pl0g****",
   "WarrantyPeriod":"2027-01-01T00:00:00+08:00",
   "InstanceName":"i-d8t4ltuheob3s2j0****",
   "SecondaryEniId":"eni-3ga00weu4ouu93bc****",
   "SSHUser":"",
   "State":"error",
   "BMCIP":"10.38.***.****",
   "Region":"cn-wulan-****-d01",
   "NetworkCardType":"",
   "AgentID":48,
   "Subnet":"EHSW-1-****-A-****",
   "RackUnit":"21",
   "Organization":"4",
   "Description":"",
   "VPCID":"vpc-3gasnqceysuxdia5k****",
   "ImageSize":0,
   "IPv6":"",
   "Config":{
    "Memory":0,
    "CPUNumber":0
   },
   "BMCPassword":"",
   "DpuInfo":{
    "ErrorDescription":"",
    "Status":"power_on",
    LoginName:root,
    "MachineSN":"2106196KUPXDP500****",
    "RunningState":"running",
    "CGWPorts":"THGigabitEthe****0/20:1,THGigabitEthernet0/20:1",
    "Zone":"",
    "Hostname":"c25d0****.cloud.d03.am****",
    "MachineType":"PG58P2M6S2****.32",
    "BMCPassword":"****",
    "Specification":"",
    "BMCPort":"",
    "InstanceName":"dpu-i-0919****ad914****",
    "BMCIP":"10.38.***.****",
    "LastHeartbeatTime":"2026-07-15T17:28:46+08:00",
    "ID":1,
    "SN":"MT2430XZ****",
    "BMCUser":"****",
    "ASWID":"****",
    "Subnet":"",
    "RawIP":"10.38.***.***",
    "LoginPwd":""
   },
   "SSHRsaId":"",
   "MappingStatus":"OperatedFailed",
   "Rack":"D03",
   "ApplicationGroup":"instance",
   "GpuNum":0,
   "NetworkCardNum":0,
   "SubnetIP":"10.38.***.***",
   "VPCSubnet":"vsw-3ga970i9dqzq7bybm****",
   "SN":"****",
   "BMCUser":"****",
   "Deleted":false,
   "Room":"C2-5",
   "ResourceGroup":"3",
   "SSHPwd":"",
   "ImageUniqueKey":"",
   "UserName":"",
   "OS":"",
   "UnitNum":0,
   "Zone":"cn-wulan-****-amte****-a",
   "CreateTime":"2026-06-24T17:19:05+08:00",
   "MachineType":"PG58P2M6S****.32",
   "NetworkMode":"vpc",
   "CPUArch":"",
   "BMCPort":"",
   "WWN":"",
   "Extra":"",
   "DefaultImage":"alinux_3_x86_64_aiext_20260623_bf3.qcow2",
   "UserId":"127756957048****",
   "UpdateTime":"2026-07-08T20:26:43+08:00",
   "LastHeartbeatTime":"2026-07-09T13:54:42+08:00",
   "ASWID":"****",
   "Tag":""
  }
 },
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <DeployType>bfi_base</DeployType>
  <RunningState>offline</RunningState>
  
<CGWPorts>TwoHundredGigE1/0/65:1,TwoHundredGigE1/0/65:2,TwoHundredGigE1/0/66:1,TwoHundred
gE1/0/66:2</CGWPorts>
  <IDC>amtest****</IDC>
  <SANZone  />
  <Image>alinux_3_x86_64_aiext_20260623_bf3.qcow2</Image>
  <InnerBandwidth  />
  <Gpu  />
  <ImageType  />
  <InstanceAlias>i-7c4ba42a32f64****</InstanceAlias>
  <AliYunAssistID>mi-rg6owzr81e****</AliYunAssistID>
  <ID>108</ID>
  <Disk>0</Disk>
  <RawIP>192.168.***.***</RawIP>
  <HostName>SN-2106196KUPXDP500****</HostName>
  <Disable>false</Disable>
  <ErrorDescription>[a-87c59321-7ac5-11f1-9014-02420a2608cd]reonlineNcEni timeout, eniList not ready</ErrorDescription>
  <Status>power_on</Status>
  <DeviceModel>BFIBaseStack</DeviceModel>
  <Protected>true</Protected>
  <IP>192.168.***.***</IP>
  <DefaultHostName>SN-2106196KUPXDP500****</DefaultHostName>
  <PrimaryEniId>eni-9lpy8hgva2pl0g****</PrimaryEniId>
  <WarrantyPeriod>2027-01-01T00:00:00+08:00</WarrantyPeriod>
  <InstanceName>i-d8t4ltuheob3s2j0****</InstanceName>
  <SecondaryEniId>eni-3ga00weu4ouu93bc****</SecondaryEniId>
  <SSHUser  />
  <State>error</State>
  <BMCIP>10.38.***.****</BMCIP>
  <Region>cn-wulan-****-d01</Region>
  <NetworkCardType  />
  <AgentID>48</AgentID>
  <Subnet>EHSW-1-****-A-****</Subnet>
  <RackUnit>21</RackUnit>
  <Organization>4</Organization>
  <Description  />
  <VPCID>vpc-3gasnqceysuxdia5k****</VPCID>
  <ImageSize>0</ImageSize>
  <IPv6  />
  <Config>
   <Memory>0</Memory>
   <CPUNumber>0</CPUNumber>
  </Config>
  <BMCPassword  />
  <DpuInfo>
   <ErrorDescription  />
   <Status>power_on</Status>
   <LoginName>root</LoginName>
   <MachineSN>2106196KUPXDP500****</MachineSN>
   <RunningState>running</RunningState>
   <CGWPorts>THGigabitEthe****0/20:1,THGigabitEthernet0/20:1</CGWPorts>
   <Zone  />
   <Hostname>c25d0****.cloud.d03.am****</Hostname>
   <MachineType>PG58P2M6S2****.32</MachineType>
   <BMCPassword>****</BMCPassword>
   <Specification  />
   <BMCPort  />
   <InstanceName>dpu-i-0919****ad914****</InstanceName>
   <BMCIP>10.38.***.****</BMCIP>
   <LastHeartbeatTime>2026-07-15T17:28:46+08:00</LastHeartbeatTime>
   <ID>1</ID>
   <SN>MT2430XZ****</SN>
   <BMCUser>****</BMCUser>
   <ASWID>****</ASWID>
   <Subnet  />
   <RawIP>10.38.***.***</RawIP>
   <LoginPwd  />
  </DpuInfo>
  <SSHRsaId  />
  <MappingStatus>OperatedFailed</MappingStatus>
  <Rack>D03</Rack>
  <ApplicationGroup>instance</ApplicationGroup>
  <GpuNum>0</GpuNum>
  <NetworkCardNum>0</NetworkCardNum>
  <SubnetIP>10.38.***.***</SubnetIP>
  <VPCSubnet>vsw-3ga970i9dqzq7bybm****</VPCSubnet>
  <SN>****</SN>
  <BMCUser>****</BMCUser>
  <Deleted>false</Deleted>
  <Room>C2-5</Room>
  <ResourceGroup>3</ResourceGroup>
  <SSHPwd  />
  <ImageUniqueKey  />
  <UserName  />
  <OS  />
  <UnitNum>0</UnitNum>
  <Zone>cn-wulan-****-amte****-a</Zone>
  <CreateTime>2026-06-24T17:19:05+08:00</CreateTime>
  <MachineType>PG58P2M6S****.32</MachineType>
  <NetworkMode>vpc</NetworkMode>
  <CPUArch  />
  <BMCPort  />
  <WWN  />
  <Extra  />
  <DefaultImage>alinux_3_x86_64_aiext_20260623_bf3.qcow2</DefaultImage>
  <UserId>127756957048****</UserId>
  <UpdateTime>2026-07-08T20:26:43+08:00</UpdateTime>
  <LastHeartbeatTime>2026-07-09T13:54:42+08:00</LastHeartbeatTime>
  <ASWID>****</ASWID>
  <Tag  />
 </data>
</data>
<errorTitle>""</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;"</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-6"></a>

### 5.1.6. GetVswitchSwitchMethod

Query the types of physical switches connected to bare metal dedicated switches in a Virtual Private Cloud (VPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the VPC. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env\*\*\*-\*\*\*\*-a | The ID of the zone. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "vsw-1clbm6xp5ml6jlpt9 \*\*\*\*": "CHSW", "vsw-1cl4ewc5dmbdujs0 w\*\*\*\*": "HSW" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "vsw-1clbm6xp5ml6jlpt9****":"CHSW",
  "vsw-1cl4ewc5dmbdujs0w****":"HSW"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <vsw-1clbm6xp5ml6jlpt9****>CHSW</vsw-1clbm6xp5ml6jlpt9****>
 <vsw-1cl4ewc5dmbdujs0w****>HSW</vsw-1cl4ewc5dmbdujs0w****>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-7"></a>

### 5.1.7. ClusterDryRun

Simulate a cluster operation without actually performing it to validate configurations, check for potential errors, or evaluate the impact of changes.

**Description**

Cluster creation precheck

```text
http://[Endpoint]/?Action=ClusterDryRun
&ClusterType=ack
&ClusterArchType=standard
&MachineTypeList=[
  {
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
  }
]
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA****
&Common request parameters
```

Cluster scale-out precheck

```text
http://[Endpoint]/?Action=ClusterDryRun
&ClusterId=ack-8EEjd6****
&ClusterType=ack
&ClusterArchType=standard
&MachineTypeList=[
  {
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
  }
]
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA****
&Common request parameters
```

Node restoration to cluster precheck

```text
http://[Endpoint]/?Action=ClusterDryRun
&ClusterId=ack-8EEjd6****
&ClusterType=ack
&ClusterArchType=standard
&InstanceNameList=["i-d9jfbieheob5ghiu****"]
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA****
&Common request parameters
```

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |
| ClusterTyp e | Strin g | Quer y | No | ack | The cluster type. Valid values:<br>• bmcp: Bare metal computing cluster<br>• ack: Container Service for Kubernetes (ACK) computing cluster<br>• bfi: Converged computing cluster |
| ClusterArc hType | Strin g | Quer y | No | standard | The cluster instance type.Valid values:<br>• standard: Intelligent computing high-bandwidth network<br>• base: Basic intelligent computing<br>• aspeed: Intelligent computing training and inference<br>• bfi: Converged high-bandwidth network<br>• bfi_base: Converged basic |
| MachineTy peList | Json | Quer y | No | \[ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "NodePoolName": "bmcp-node-pool", "VswitchId": "vsw-3gagdup8scary04iq\*\*\*\*"} \] | The list of bare metal instance types. |
| RequestTo ken | Strin g | Quer y | No | 869F3EDC-C0CA-45E4-AA11-C4638CDA\*\*\*\* | The request token. |
| InstanceN ameList | Json | Quer y | No | \["i-d9jfbieheob5ghiu\*\*\*\*"\] | The list of instance names.<br>This parameter can be configured only when ClusterId is specified. It indicates a node restoration to cluster precheck. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

<table>
  <tr>
    <td>data</td>
    <td>Map</td>
    <td>{ "RequestToken": "869F3EDC-C0CA-45E4-AA11-C4638CDA****", "NeedWarning": true, "ClusterDriverVersi on": {"gpu_driver": ["1.5.3-5239a4" ], "gpu_sdk": [ "12.3"], "gpu_tag": ["1ded:6001" ] }, "InstanceDriverVer sion": [ {"components": [ {"lastReportedAt": 1782274630000, "componentKey": "gpu_driver", "actualVersion": "2.2.0" }, {"lastReportedAt": 1782274630000, "componentKey": "gpu_sdk", "actualVersion": "12.2" }, {"lastReportedAt": 1782274630000, "componentKey": "gpu_tag", "actualVersion": "nvidia" } ], "componentCount": 0, "machineSN": "test", "hasReportedData": false } ] }</td>
    <td>The response data.</td>
  </tr>
  <tr>
    <td>status</td>
    <td>Integer</td>
    <td>0</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>requestId</td>
    <td>String</td>
    <td>66dfddc6-b547-11ee-aa84-acde4800****</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>success</td>
    <td>Boolean</td>
    <td>true</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>responseVersi on</td>
    <td>String</td>
    <td>v1</td>
    <td>The version of the response.</td>
  </tr>
</table>

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ClusterDryRun
&ClusterType=ack
&ClusterArchType=standard
&MachineTypeList=[
  {
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
  }
]
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "RequestToken":"869F3EDC-C0CA-45E4-AA11-C4638CDA****",
  "NeedWarning":true,
  "ClusterDriverVersion":{
   "gpu_driver":[
    "1.5.3-5239a4"
   ],
   "gpu_sdk":[
    "12.3"
   ],
   "gpu_tag":[
    "1ded:6001"
   ]
  },
  "InstanceDriverVersion":[
   {
    "components":[
     {
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_driver",
      "actualVersion":"2.2.0"
     },
     {
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_sdk",
      "actualVersion":"12.2"
     },
     {
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_tag",
      "actualVersion":"nvidia"
     }
    ],
    "componentCount":0,
    "machineSN":"test",
    "hasReportedData":false
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <RequestToken>869F3EDC-C0CA-45E4-AA11-C4638CDA****</RequestToken>
 <NeedWarning>true</NeedWarning>
 <ClusterDriverVersion>
  <gpu_driver>1.5.3-5239a4</gpu_driver>
  <gpu_sdk>12.3</gpu_sdk>
  <gpu_tag>1ded:6001</gpu_tag>
 </ClusterDriverVersion>
 <InstanceDriverVersion>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_driver</componentKey>
   <actualVersion>2.2.0</actualVersion>
  </components>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_sdk</componentKey>
   <actualVersion>12.2</actualVersion>
  </components>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_tag</componentKey>
   <actualVersion>nvidia</actualVersion>
  </components>
  <componentCount>0</componentCount>
  <machineSN>test</machineSN>
  <hasReportedData>false</hasReportedData>
 </InstanceDriverVersion>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-8"></a>

### 5.1.8. TagResources

Tag a cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| RegionId | Strin g | Quer y | Yes | cn-wulan-\*\*\*\*-d01 | The ID of the region to which the resource belongs. |
| ResourceT ype | Strin g | Quer y | Yes | CLUSTER | The resource type.Currently, only CLUSTER is supported. |
| Tags | Json | Quer y | No | \[ {"key":"testacktagk-1","value":"testackv-1"}, {"key":"testacktagk-2","value":"testackv-2"} \] | The tag key-value pairs of the resource. Array length range: <code> [1,20] </code><br><em>It cannot start</em> <em>with </em><em><code> aliyun </code></em><em> or</em> <em><code> acs: </code></em><em>.</em><br><em>It cannot contain </em> <em><code> http:// </code></em><em> or </em> <em><code> https:// </code></em><em>.</em> |
| ResourceId s | Json | Quer y | No | \["ack-ezVaql\*\*\*\*","ack-99VDuz\*\*\*\*"\] | The list of resource IDs.Note that the IDs are Container Service for Kubernetes (ACK) cluster IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "RequestId": "2D69A58F-345C-4FDE-88E4-BF51894\*\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=TagResources
&RegionId=cn-wulan-****-d01
&ResourceType=CLUSTER
&Tags=[
  {"key":"testacktagk-1","value":"testackv-1"},
  {"key":"testacktagk-2","value":"testackv-2"}
]
&ResourceIds=["ack-ezVaql****","ack-99VDuz****"]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "RequestId":"2D69A58F-345C-4FDE-88E4-BF51894*****"
 },
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <RequestId>2D69A58F-345C-4FDE-88E4-BF51894*****</RequestId>
</data>
<errorTitle>“”</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-1-9"></a>

### 5.1.9. RetryFailedInstance

Retry instances that failed to be scaled out or scaled in for bare metal and Container Service for Kubernetes (ACK) clusters. After the retry, a new scale-out or scale-in task is initiated.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskId | Strin g | Quer y | No | 1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\* | The ID of the task. |
| InstanceN ameList | Json | Quer y | No | \["i-d9jfbieheob5ghiu\*\*\*\*"\] | The list of IDs of the instances to retry. |
| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC-9AB1-890F1234\*\*\*\* | The ID of the Cloud Assistant activation code.<br>This parameter is required when the instances to retry are being scaled out to the cluster. |
| Activation Code | Strin g | Quer y | No | a-hz0ch3SwhOlE1234+Xo3 2lAZC\*\*\*\* | The code of the Cloud Assistant activation code.<br>This parameter is required when the instances to retry are being scaled out to the cluster. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks. This parameter is required when the instances are being removed from the cluster.Valid values:<br>• true: Clear data disks.<br>• false: Do not clear data disks. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period of instances in the recycle bin. Unit: hours. Valid values: 1 to 720<br>This parameter is required when the instances to retry are being removed from the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TaskId": "0d1fa517-8576-11f1-9d26-02420a260d50" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=RetryFailedInstance
&TaskId=1284c8b8-9571-11ee-a39e-16f363c7****
&InstanceNameList=["i-d9jfbieheob5ghiu****"]
&ActivationId=4ECEEE12-56F1-4FBC-9AB1-890F1234****
&ActivationCode=a-hz0ch3SwhOlE1234+Xo32lAZC****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TaskId":"0d1fa517-8576-11f1-9d26-02420a260d50"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TaskId>0d1fa517-8576-11f1-9d26-02420a260d50</TaskId>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-2"></a>

## 5.2. Storage management

<a id="section-5-2-1"></a>

### 5.2.1. CreateCpfsClientCluster

Enable high-performance storage for clusters of high-performance network instances and computing-optimized training & inference instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster.<br>The system only supports clusters with <strong>high-</strong>performance network <strong>instances</strong> and computing-optimized training &amp; inference <strong>instances</strong>.<br>Different storage types have different limits on the number of Bare Metal Computing Platform (BMCP) nodes:<br>• Cloud Parallel File System (CPFS): The minimum number of nodes is 3.<br>• Apple File System (APFS): The minimum number of nodes is 1. |
| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of high-performance storage client. Valid values:<br>• CPFS<br>• APFS |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"data": "The asynchronous workflow task for enabling high-performance storage has been initiated"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateCpfsClientCluster
&ClusterId=ack-8EEjd6****
&CpfsClusterType=CPFS
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The asynchronous workflow task for enabling high-performance storage has beeninitiated"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The asynchronous workflow task for enabling high-performance storage has been initiated</data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-2-2"></a>

### 5.2.2. DescribeCpfsClientClusterType

Query the available high-performance storage client types in the environment.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterType": \["CPFS", "APFS" \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Success: true<br>• Failure: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "ClusterType":[
   "CPFS",
   "APFS"
  ]
 },
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <ClusterType>CPFS</ClusterType>
 <ClusterType>APFS</ClusterType>
</data>
<errorTitle>InternalError</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-2-3"></a>

### 5.2.3. MountFilesystem

Mount high-performance storage for a cluster.

**Operation description**

- You can only mount high-performance storage to clusters with **high-performance network instances** and **computing-optimized training & inference instances**.

- Before mounting, call the CreateCpfsClientCluster operation to enable high-performance storage for the cluster.

- Different storage types have different requirements for the number of Bare Metal Computing Platform (BMCP) nodes in a cluster:

  - Cloud Parallel File System (CPFS): The minimum number of nodes is 3.

  - Apple File System (APFS): The minimum number of nodes is 1.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | bmcp-noBklp\*\*\*\* | The ID of the cluster. |
| FileSystem Id | Strin g | Quer y | No | efs-0137\*\*\*\* | The ID of the file system.CPFS or APFS file systems are supported.<br>• CPFS: bmcpfs-01ae\*\*\*\*<br>• APFS: efs-0137\*\*\*\* |
| MountPoin t | Json | Quer y | No | /dev/xvda | The mount point. |

<table>
  <tr>
    <td>MountDire ctory</td>
    <td>Json</td>
    <td>Quer y</td>
    <td>No</td>
    <td>/ai_model_training</td>
    <td>The local mount path of the file system.<br>Mount path requirements:<br>• After you set the mount path, the system automatically creates a directory.Manual creation is not needed..<br>• Recommended format:<code> /[business </code> <code>name]_[purpose] </code>.For example,/ai_model_training.<br>• To ensure stability, avoid using the following paths:<br>• System critical directories, such as<code> / </code>, <code> /bin </code>,<code> /etc </code>, and<code> /tmp </code>.<br>• Paths that start with/efs (including/efs/custom-path).<br>• System reserved paths. For example, when the ID of the file system is efs-123456, the default mount path is/efs/123456.<br>• If the directory already contains files, the original files will be temporarily hidden after mounting and will be restored after unmounting.</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data" :"Launch success" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Success: true<br>• Failure: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=MountFilesystem
&ClusterId=bmcp-noBklp****
&FileSystemId=efs-0137****
&MountPoint=/dev/xvda
&MountDirectory=/ai_model_training
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"Launch success"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>Launch success</data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-2-4"></a>

### 5.2.4. UnmountFilesystem

Unmount a file system from a cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data" :"unmount success" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the response.<br>• Success: true<br>• Failure: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UnmountFilesystem
&ClusterId=ack-8EEjd6****
&common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"unmount success"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>unmount success</data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-2-5"></a>

### 5.2.5. DeleteCpfsClientCluster

Unmount high-performance storage from clusters with high-performance network instances and computing-optimized training & inference instances.

**Operation description**

When you unmount a file system, all processes that are using the file system in the current cluster will be terminated, which may cause data loss or service interruption. Proceed with caution.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"data": "The asynchronous workflow task for disabling high-performance storage has been initiated"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":"The asynchronous workflow task for disabling high-performance storage has been initiated"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>The asynchronous workflow task for disabling high-performance storage has been initiated</data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-3"></a>

## 5.3. EVPC

<a id="section-5-3-1"></a>

### 5.3.1. CreateEvpc

Create an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | test | The ID of the organization, which identifies the organization or department to which the EVPC belongs. |
| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set, used to classify the EVPC to a specified resource group. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region, which specifies the geographical location where the EVPC is created. |
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The name of the EVPC, used to identify the created EVPC instance. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the EVPC, used to provide more information about the EVPC. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values:<br>• true: Enable<br>• false: Disable<br>Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "EvpcId": "evpc-htchvitxlfjyso\*\*\*\*"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateEvpc
&Department=test
&ResourceGroup=ResourceSet(test)
&RegionId=cn-wulan-env***-d01
&EvpcName=evpc-htchvitxlfjyso****
&EnableIpv6=true
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "EvpcId":"evpc-htchvitxlfjyso****"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-3-2"></a>

### 5.3.2. ListEvpc

Query the list of Enterprise Virtual Private Clouds (EVPCs).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| PageNumb er | Integ er | Quer y | No | 1 | The page number, used for pagination query.Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The unique identifier of the EVPC. |
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The name of the EVPC. |
| Cidr | Strin g | Quer y | No | 20.41.\*.\*/16 | The IPv4 CIDR block information of the EVPC. |
| Departme nt | Strin g | Quer y | No | test | The ID of the organization to which the EVPC belongs. |
| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set to which the EVPC belongs. |
| Status | Strin g | Quer y | No | Available | The current status of the EVPC. Valid values:<br>• Available: Normal<br>• Not Available: Unavailable<br>• Deleting: Deleting<br>• DeletingFailed: Deletion failed |
| TenantId | Strin g | Quer y | No | 28065796931554\*\*\*\* | The ID of the tenant associated with the EVPC. |
| Descriptio n | Bool ean | Quer y | No | testDescription | The detailed description of the EVPC. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values:<br>• true: Enabled<br>• false: Disabled<br>Default value: false. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster associated with the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "PageNumber": 1, "PageSize": 10, "TotalCount": 1, "EvpcList": \[ {"EvpcId": "evpc-htchvitxlfjyso\*\*\*\*", "ClusterId": "ack-8EEjd6\*\*\*\*", "EvpcName": "evpc-htchvitxlfjyso\*\*\*\*", "Description":"test", "Cidr": "20.41.\*.\*/16", "TenantId": "28065796931554 \*\*\*\*", "Status": "Available", "RegionId": "cn-wulan-env\*\*\*-d01", "Department":"test ", "ResourceGroup": "ResourceSet(test) ", "CreateTime": "2026-06-01T12:05:00Z", "UpdateTime": "2026-07-01T12:05:00Z", "EnableIpv6": true, "Ipv6Cidr": "1007:1100:\*\*\*\*::/64" } \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListEvpc
&Department=test
&ResourceGroup=ResourceSet(test)
&RegionId=cn-wulan-env***-d01
&Status=Available
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "EvpcList":[
   {
    "Status":"Available",
    "Description":"test",
    "ClusterId":"ack-8EEjd6****",
    "CreateTime":"2026-06-01T12:05:00Z",
    "EvpcName":"evpc-htchvitxlfjyso****",
    "EvpcId":"evpc-htchvitxlfjyso****",
    "EnableIpv6":true,
    "TenantId":"28065796931554****",
    "Department":"test",
    "Cidr":"20.41.*.*/16",
    "UpdateTime":"2026-07-01T12:05:00Z",
    "RegionId":"cn-wulan-env***-d01",
    "ResourceGroup":"ResourceSet(test)",
    "Ipv6Cidr":"1007:1100:****::/64"
   }
  ],
  "PageNumber":1
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <EvpcList>
  <Status>xxxxx</Status>
  <Description>xxxx</Description>
  <ClusterId>xxxxxx</ClusterId>
  <CreateTime>xxxx</CreateTime>
  <EvpcName>xxxx</EvpcName>
  <EvpcId>xxxxxxxxxx</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <TenantId>xxxx</TenantId>
  <Department>xxxx</Department>
  <Cidr>xxxx</Cidr>
  <UpdateTime>xxxx</UpdateTime>
  <RegionId>xxxx</RegionId>
  <ResourceGroup>xxxxx</ResourceGroup>
  <Ipv6Cidr>1007:1100:1100::/64</Ipv6Cidr>
 </EvpcList>
 <PageNumber>1</PageNumber>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-3-3"></a>

### 5.3.3. ListEvpcConnections

Query the Enterprise Virtual Private Cloud (EVPC) connections of an EVPC.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The unique identifier of the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "Connections": \[{ //EvpcConnectionId "EvpcConnectionId ": "125489", //LocalEvpcId "LocalEvpcId": "evpc-htchvitxlfjyso\*\*\*\*",// LocalEvpcName "LocalEvpcName": "test1", //PeerEvpcId "PeerEvpcId": "evpc-b9wfut1m1ry6sh\*\* \*\*", //PeerEvpcName "PeerEvpcName": "test2", // status "Status": "Success"} \] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListEvpcConnections
&EvpcId=evpc-htchvitxlfjyso****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "Connections":[
   {
    "PeerEvpcId":"evpc-b9wfut1m1ry6sh****",
    "Status":"Success",
    "LocalEvpcId":"evpc-htchvitxlfjyso****",
    "PeerEvpcName":"test2",
    "LocalEvpcName":"test1",
    "EvpcConnectionId":"125489"
   }
  ]
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <Connections>
  <PeerEvpcId>evpc-b9wfut1m1ry6sh****</PeerEvpcId>
  <Status>Success</Status>
  <LocalEvpcId>evpc-htchvitxlfjyso****</LocalEvpcId>
  <PeerEvpcName>test2</PeerEvpcName>
  <LocalEvpcName>test1</LocalEvpcName>
  <EvpcConnectionId>125489</EvpcConnectionId>
 </Connections>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-3-4"></a>

### 5.3.4. ModifyEvpc

Modify the name or description of an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The new name of the EVPC, used to update the display name of the EVPC. |
| Descriptio n | Strin g | Quer y | No | testDescription | The new description of the EVPC, used to provide more details about the EVPC. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The unique identifier of the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"EvpcId": "evpc-htchvitxlfjyso\*\*\*\*"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ModifyEvpc
&EvpcId=evpc-htchvitxlfjyso****
&EvpcName=evpc-htchvitxlfjyso****
&Description=testDescription
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "EvpcId":"evpc-htchvitxlfjyso****"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-3-5"></a>

### 5.3.5. DeleteEvpc

Delete an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso\*\*\*\* | The ID of the EVPC, which is the unique identifier of the EVPC. |
| Force | Bool ean | Quer y | No | false | Specifies whether to forcibly delete the EVPC.Valid values:<br>• true: Yes<br>• false: No<br>Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"describe":"The deletion task has been submitted"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListEvpcConnections
&EvpcId=evpc-htchvitxlfjyso****
&Force=false
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "describe":"The deletion task has been submitted"
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data />
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4"></a>

## 5.4. Security group

<a id="section-5-4-1"></a>

### 5.4.1. CreateSecurityGroup

Create a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | test | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | ResourceTest(test) | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| Name | Strin g | Quer y | No | test | The name of the security group.<br>The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, underscores (_), hyphens (-), and colons (:). It cannot start with <code> http:// </code> or <code> https:// </code>. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC) instance. |
| Type | Strin g | Quer y | No | null | The type of the security group. This parameter is not available. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The deployment type.Only bmcp is supported. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description.<br>The description must be 2 to 256 characters in length, and must start with a letter. It can contain digits, underscores (_), hyphens (-), full-width periods (。), full-width commas (，), half-width commas (,), full-width colons (：), colons (:), and slashes (/).It cannot start with <code> http:// </code> or <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg-7s186nsxfz01wa5x \*\*\*\*", "ID": "3", "name": "test" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateSecurityGroup
&Department=test
&ResourceGroup=ResourceTest(test)
&RegionId=cn-wulan-env***-d01
&Name=test
&VpcId=vpc-bp1b1xjllp3ve5yze****
&DeployType=bmcp
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "name":"test",
   "sgId":"sg-7s186nsxfz01wa5x****",
   "ID":"3"
  }
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <name>test</name>
  <sgId>sg-7s186nsxfz01wa5x****</sgId>
  <ID>3</ID>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-2"></a>

### 5.4.2. ListSecurityGroup

Query the list of security groups.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | test | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| Name | Strin g | Quer y | No | test | The name of the security group. |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| VpcId | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the Virtual Private Cloud (VPC). |
| Type | Strin g | Quer y | No | null | The type of the security group. This parameter is not available. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The deployment type.Only bmcp is supported. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": \[ { "ID": 6, "sgId": "sg-bp197668l6iupljy\*\* \*\*", "name": "test", "region": "cn-wulan-env\*\*\*-d01", "organization": "4", "resourceGroup": "3", "vpcId": "vpc-bp1b1xjllp3ve5yze \*\*\*\*", "type": "", "deployType": "bmcp", "description": "testDescription", "AliUid": "127756957048\*\*\* \*", "shared": 0, "version": 0, "deleted": false, "createTime": "2026-07-03T14:50:26+08:0 0", "updateTime": "2026-07-03T14:50:26+08:0 0" } \], "total": 1, "pageNumber": 10, "pageSize": 1 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListSecurityGroup
&Department=test
&ResourceGroup=ResourceTest(test)
&RegionId=cn-wulan-env***-d01
&Name=test
&VpcId=vpc-bp1b1xjllp3ve5yze****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":10,
  "data":[
   {
    "resourceGroup":"3",
    "shared":0,
    "description":"testDescription",
    "updateTime":"2026-07-03T14:50:26+08:00",
    "type":"",
    "version":0,
    "deployType":"bmcp",
    "deleted":false,
    "createTime":"2026-07-03T14:50:26+08:00",
    "organization":"4",
    "vpcId":"vpc-bp1b1xjllp3ve5yze****",
    "name":"test",
    "sgId":"sg-bp197668l6iupljy****",
    "ID":6,
    "region":"cn-wulan-env***-d01",
    "AliUid":"127756957048****"
   }
  ],
  "pageSize":1
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <total>1</total>
 <pageNumber>10</pageNumber>
 <data>
  <resourceGroup>3</resourceGroup>
  <shared>0</shared>
  <description>testDescription</description>
  <updateTime>2026-07-03T14:50:26+08:00</updateTime>
  <type />
  <version>0</version>
  <deployType>bmcp</deployType>
  <deleted>false</deleted>
  <createTime>2026-07-03T14:50:26+08:00</createTime>
  <organization>4</organization>
  <vpcId>vpc-bp1b1xjllp3ve5yze****</vpcId>
  <name>test</name>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <ID>6</ID>
  <region>cn-wulan-env***-d01</region>
  <AliUid>127756957048****</AliUid>
 </data>
 <pageSize>1</pageSize>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-3"></a>

### 5.4.3. ModifySecurityGroup

Modify the name or description of a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| Name | Strin g | Quer y | No | test | The name of the security group.<br>The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, underscores (_), hyphens (-), and colons (:). It cannot start with <code> http:// </code> or <code> https:// </code>. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group.<br>The description must be 2 to 256 characters in length, and must start with a letter. It can contain digits, underscores (_), hyphens (-), full-width periods (。), full-width commas (，), half-width commas (,), full-width colons (：), colons (:), and slashes (/).It cannot start with <code> http:// </code> or <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg-7s186nsxfz01wa5x \*\*\*\*", "ID": "3", "name": "test" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ModifySecurityGroup
&SgId=sg-bp197668l6iupljy****
&Name=test
&Description=testDescription
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "name":"test",
   "sgId":"sg-7s186nsxfz01wa5x****",
   "ID":"3"
  }
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <name>test</name>
  <sgId>sg-7s186nsxfz01wa5x****</sgId>
  <ID>3</ID>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-4"></a>

### 5.4.4. DeleteSecurityGroup

Delete a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteSecurityGroup
&SgId=sg-bp197668l6iupljy****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":""
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <sgId />
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-5"></a>

### 5.4.5. AddSecurityGroupRule

Add a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| Direction | Strin g | Quer y | No | ingress | The rule direction. Valid values:<br>• ingress: Inbound<br>• egress: Outbound |
| AccessPoli cy | Strin g | Quer y | No | accept | The access policy. Valid values:<br>• accept: Allow access.<br>• drop: Deny access. No rejection message is returned. The initiator may experience request timeouts or connection failures.<br>Default value: accept. |
| IpProtocol | Strin g | Quer y | No | tcp | The transport layer protocol (case-insensitive). Valid values:<br>• ICMP<br>• GRE<br>• TCP<br>• UDP<br>• ALL: All protocols are supported. |
| PortRange | Strin g | Quer y | No | 80/80 | The port range. Value range:<br>• TCP/UDP: Valid values are 1 to 65535. Use a forward slash (/) to separate the start port and end port. For example, 1/200.<br>• ICMP: -1/-1.<br>• GRE: -1/-1.<br>• When IpProtocol is set to ALL: -1/-1. |
| Priority | Integ er | Quer y | No | 1 | The priority of the security group rule. A smaller number indicates a higher priority. Value range: 1 to 100.<br>Default value: 1. |
| IpVersion | Strin g | Quer y | No | ipv4 | The IP version. Only ipv4 is supported. |
| CidrIp | Strin g | Quer y | No | 192.168.0.1 | The source IPv4 CIDR block. |
| RelatedGr oupId | Strin g | Quer y | No | sg-7s186nsxfz01wa5x\*\*\*\* | The ID of the authorized security group. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group rule for easier management.<br>The description must be 1 to 512 characters in length, and cannot start with <code> http:// </code> and <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg-bp197668l6iupljy\*\* \*\*", "sgrId": "sgr-tllvexl60s9khyld3p mr" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=AddSecurityGroupRule
&SgId=sg-bp197668l6iupljy****
&AccessPolicy=accept
&Direction=ingress
&IpProtocol=tcp
&PortRange=80/80
&CidrIp=192.168.0.1
&IpVersion=ipv4
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":"sg-bp197668l6iupljy****",
   "sgrId":"sgr-tllvexl60s9khyld3pmr"
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <sgrId>sgr-tllvexl60s9khyld3pmr</sgrId>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-6"></a>

### 5.4.6. ListSecurityGroupRule

Query the list of security group rules.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| Direction | Strin g | Quer y | No | ingress | The rule direction. |
| PageNumb er | Integ er | Quer y | No | 10 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "total": 1, "pageNumber": 1, "data": \[ {"portRange": "80/80", "SgId": "sg-5gh79x2ijuk9yzjo\*\* \*\*", "description": "test", "updateTime": "2026-07-03T16:55:26+08:0 0", "ipProtocol": "tcp", "priority": 1, "relatedGroupId": "", "ipVersion": "ipv4", "deleted": false, "createTime": "2026-07-03T16:55:26+08:0 0", "ID": 3, "accessPolicy": "ACCEPT", "sgrId": "sgr-tllvexl60s9khyld\*\*\* \*", "cidrIp": "192.168.0.1", "direction": "ingress" } \], "pageSize": 10 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListSecurityGroupRule
&SgId=sg-bp197668l6iupljy****
&PageNumber=10
&PageSize=1
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":1,
  "data":[
   {
    "portRange":"80/80",
    "SgId":"sg-5gh79x2ijuk9yzjo****",
    "description":"test",
    "updateTime":"2026-07-03T16:55:26+08:00",
    "ipProtocol":"tcp",
    "priority":1,
    "relatedGroupId":"",
    "ipVersion":"ipv4",
    "deleted":false,
    "createTime":"2026-07-03T16:55:26+08:00",
    "ID":3,
    "accessPolicy":"ACCEPT",
    "sgrId":"sgr-tllvexl60s9khyld****",
    "cidrIp":"192.168.0.1",
    "direction":"ingress"
   }
  ],
  "pageSize":10
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <total>1</total>
 <pageNumber>1</pageNumber>
 <data>
  <portRange>80/80</portRange>
  <SgId>sg-5gh79x2ijuk9yzjo****</SgId>
  <description>test</description>
  <updateTime>2026-07-03T16:55:26+08:00</updateTime>
  <ipProtocol>tcp</ipProtocol>
  <priority>1</priority>
  <relatedGroupId />
  <ipVersion>ipv4</ipVersion>
  <deleted>false</deleted>
  <createTime>2026-07-03T16:55:26+08:00</createTime>
  <ID>3</ID>
  <accessPolicy>ACCEPT</accessPolicy>
  <sgrId>sgr-tllvexl60s9khyld****</sgrId>
  <cidrIp>192.168.0.1</cidrIp>
  <direction>ingress</direction>
 </data>
 <pageSize>10</pageSize>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-7"></a>

### 5.4.7. ModifySecurityGroupRule

Modify a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| SgrId | Strin g | Quer y | No | sgr-tllvexl60s9khyld\*\*\*\* | The ID of the rule. |
| Direction | Strin g | Quer y | No | ingress | The rule direction. Valid values:<br>• ingress: Inbound<br>• egress: Outbound |
| AccessPoli cy | Strin g | Quer y | No | accept | The access policy. Valid values:<br>• accept: Allow access.<br>• drop: Deny access. No rejection message is returned. The initiator may experience request timeouts or connection failures.<br>Default value: accept. |
| IpProtocol | Strin g | Quer y | No | tcp | The transport layer protocol (case-insensitive). Valid values:<br>• ICMP<br>• GRE<br>• TCP<br>• UDP<br>• ALL: All protocols are supported. |
| PortRange | Strin g | Quer y | No | 80/80 | The port range. Value range:<br>• TCP/UDP: Valid values are 1 to 65535. Use a forward slash (/) to separate the start port and end port. For example, 1/200.<br>• ICMP protocol:-1/-1.<br>• GRE protocol:-1/-1.<br>• When IpProtocol is set to ALL: -1/-1. |
| Priority | Integ er | Quer y | No | 1 | The priority of the security group rule. A smaller number indicates a higher priority. Value range: 1 to 100.<br>Default value: 1. |
| IpVersion | Strin g | Quer y | No | ipv4 | The IP version. Only ipv4 is supported. |
| CidrIp | Strin g | Quer y | No | 192.168.0.1 | The source IPv4 CIDR block. |
| RelatedGr oupId | Strin g | Quer y | No | sg-7s186nsxfz01wa5x\*\*\*\* | The ID of the authorized security group. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group rule for easier management.<br>The description must be 1 to 512 characters in length, and cannot start with <code> http:// </code> and <code> https:// </code>. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg-bp197668l6iupljy\*\* \*\*", "sgrId": "sgr-tllvexl60s9khyld3p mr" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ModifySecurityGroupRule
&SgId=sg-bp197668l6iupljy****
&AccessPolicy=accept
&Direction=ingress
&IpProtocol=tcp
&PortRange=80/80
&CidrIp=192.168.0.1
&IpVersion=ipv4
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":"sg-bp197668l6iupljy****",
   "sgrId":"sgr-tllvexl60s9khyld3pmr"
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <sgrId>sgr-tllvexl60s9khyld3pmr</sgrId>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-8"></a>

### 5.4.8. DeleteSecurityGroupRule

Delete a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. You can call the ListSecurityGroup operation to query the security group ID. |
| SgrId | Strin g | Quer y | No | sgr-tllvexl60s9khyld\*\*\*\* | The ID of the security group rule. You can call the ListSecurityGroupRule operation to query the rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "", "SgrId": "" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteSecurityGroupRule
&SgId=sg-bp197668l6iupljy****
&SgrId=sgr-tllvexl60s9khyld****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"",
   "SgrId":""
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <SgId />
  <SgrId />
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-9"></a>

### 5.4.9. AddSecurityGroupInstance

Add Bare Metal Computing Platform (BMCP) instances to a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| InstanceN ameList | Json | Quer y | No | \["test1","test2"\] | The list of instance names. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "sg-bp197668l6iupljy\*\* \*\*", "InstanceNameList ":\["test1","test2"\] }} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=AddSecurityGroupInstance
&SgId=sg-bp197668l6iupljy****
&InstanceNameList=["test1","test2"]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"sg-bp197668l6iupljy****",
   "InstanceNameList":[
    "test1",
    "test2"
   ]
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <SgId>sg-bp197668l6iupljy****</SgId>
  <InstanceNameList>test1</InstanceNameList>
  <InstanceNameList>test2</InstanceNameList>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-10"></a>

### 5.4.10. ListSecurityGroupInstance

Query the list of instances bound to a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| SN | Strin g | Quer y | No | 007269004887\*\*\*\*\*\* | The serial number (SN). |
| InstanceN ame | Strin g | Quer y | No | myinstance | The name of the instance. |
| PageNumb er | Integ er | Quer y | No | 10 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

<table>
  <tr>
    <td>data</td>
    <td>Map</td>
    <td>{ "data": [ { "ID": 0, "sn": "007269004887*** ***", "ip": "10.66.****.***", "rawIp": "10.66.****.***", "instanceName": "myinstance", "runningState": "running", "state": "online", "errorDescription": "", "status": "power_on", "machineType": "myinstance", "vpcId": "vpc-3gaat6wvtl0sbwxx n****", "vpcSubnet": "vsw-3gady7f50dgpp41j 8****", "networkMode": ""} ], "total": 1, "pageNumber": 10, "pageSize": 1 }</td>
    <td>The response data.</td>
  </tr>
  <tr>
    <td>status</td>
    <td>Integer</td>
    <td>200</td>
    <td>The status of the response.</td>
  </tr>
  <tr>
    <td>requestId</td>
    <td>String</td>
    <td>66dfddc6-b547-11ee-aa84-acde4800****</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>success</td>
    <td>Boolean</td>
    <td>true</td>
    <td>The status of the request.</td>
  </tr>
  <tr>
    <td>responseVersi on</td>
    <td>String</td>
    <td>v1</td>
    <td>The version of the response.</td>
  </tr>
</table>

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListSecurityGroupInstance
&SgId=sg-bp197668l6iupljy****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":10,
  "data":[
   {
    "networkMode":"",
    "errorDescription":"",
    "instanceName":"myinstance",
    "ip":"10.66.****.***",
    "vpcId":"vpc-3gaat6wvtl0sbwxxn****",
    "runningState":"running",
    "ID":0,
    "sn":"007269004887******",
    "rawIp":"10.66.****.***",
    "state":"online",
    "machineType":"myinstance",
    "vpcSubnet":"vsw-3gady7f50dgpp41j8****",
    "status":"power_on"
   }
  ],
  "pageSize":1
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <total>1</total>
 <pageNumber>10</pageNumber>
 <data>
  <networkMode  />
  <errorDescription  />
  <instanceName>myinstance</instanceName>
  <ip>10.66.****.***</ip>
  <vpcId>vpc-3gaat6wvtl0sbwxxn****</vpcId>
  <runningState>running</runningState>
  <ID>0</ID>
  <sn>007269004887******</sn>
  <rawIp>10.66.****.***</rawIp>
  <state>online</state>
  <machineType>myinstance</machineType>
  <vpcSubnet>vsw-3gady7f50dgpp41j8****</vpcSubnet>
  <status>power_on</status>
 </data>
 <pageSize>1</pageSize>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-4-11"></a>

### 5.4.11. DeleteSecurityGroupInstance

Remove Bare Metal Computing Platform (BMCP) instances from a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy\*\*\*\* | The ID of the security group. |
| InstanceN ameList | Json | Quer y | No | \["test1","test2"\] | The list of instance names. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "sg-bp197668l6iupljy\*\* \*\*", "InstanceNameList ": \["",""\] } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547-11ee-aa84-acde4800\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteSecurityGroupInstance
&SgId=sg-bp197668l6iupljy****
&InstanceNameList=["test1","test2"]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"sg-bp197668l6iupljy****",
   "InstanceNameList":[
    "",
    ""
   ]
  }
 },
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <SgId>sg-bp197668l6iupljy****</SgId>
  <InstanceNameList  />
  <InstanceNameList  />
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-5"></a>

## 5.5. Key pair

<a id="section-5-5-1"></a>

### 5.5.1. CreateKeyPair

Create a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Name | Strin g | Quer y | No | test | The name of the key pair.<br>The name cannot be the same as an existing key pair. Itmust be 2 to 128 characters in length, and cannot start with a special character or a digit. It can contain only periods (.), underscores (_), hyphens (-), and colons (:) for special characters. |
| Departme nt | Strin g | Quer y | No | Iaas_test | The name of the organization, which identifies the organization to which the resource belongs. |
| ResourceG roup | Strin g | Quer y | No | ResourceTest | The ID of the resource set, used to categorize and manage resoures. |
| RegionId | Strin g | Quer y | No | cn-wulan-env\*\*\*-d01 | The ID of the region. |
| PublicKey | Strin g | Quer y | No | ssh-rsa\*\*\*\* | The public key. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ID": 0, "name": "test", "publicKey": "", "privateKey": "", "keyPairFingerPrint ": "4096 SHA256:xsodVF6lB pYzC5043KdGxoXd RoKuoby6rJDK7h\*\* \*\* root@vm01003800 \*\*\*\* (RSA)" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateKeyPair
&Name=test
&Department=Iaas_test
&ResourceGroup=ResourceTest
&RegionId=cn-wulan-env***-d01
&PublicKey=ssh-rsa****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "privateKey":"",
  "name":"test",
  "ID":0,
  "publicKey":"",
  "keyPairFingerPrint":"4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7h**** root@vm01003800**** (RSA)"
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <privateKey />
 <name>test</name>
 <ID>0</ID>
 <publicKey />
 <keyPairFingerPrint>4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7h**** root@vm01003800**** (RSA)</keyPairFingerPrint>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-5-2"></a>

### 5.5.2. ListKeyPair

Query the list of key pairs.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| KeyPairNa me | Strin g | Quer y | No | test | The name of the key pair. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| KeyPairFin gerPrint | Strin g | Quer y | No | 4096 SHA256:xsodVF6lBpYzC5 043KdGxoXdRoKuoby6rJD K7hR\*\*\*\* root@vm01003800\*\*\*\* (RSA) | The fingerprint of the key pair. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":\[ {"name": "test", "region": "cn-test-\*\*\*\*-d01", "organization": "4", "resourceGroup": "3", "keyPairFingerPrint ": "4096 SHA256:xsodVF6lB pYzC5043KdGxoXd RoKuoby6rJDK7hR\* \*\*\* root@vm01003800 \*\*\*\* (RSA)", "createTime": "0001-01-01T00:00:00Z", "updateTime": "0001-01-01T00:00:00Z" } \], "total":1, "pageNum":1, "pageSize":1 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListKeyPair
&KeyPairName=test
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":1,
  "data":[
   {
    "resourceGroup":"3",
    "createTime":"0001-01-01T00:00:00Z",
    "organization":"4",
    "name":"test",
    "updateTime":"0001-01-01T00:00:00Z",
    "region":"cn-test-****-d01",
    "keyPairFingerPrint":"4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7hR**** root@vm01003800**** (RSA)"
   }
  ],
  "pageSize":1,
  "pageNum":1
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <total>1</total>
 <data>
  <resourceGroup>3</resourceGroup>
  <createTime>0001-01-01T00:00:00Z</createTime>
  <organization>4</organization>
  <name>test</name>
  <updateTime>0001-01-01T00:00:00Z</updateTime>
  <region>cn-test-****-d01</region>
  <keyPairFingerPrint>4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7hR**** root@vm01003800**** (RSA)</keyPairFingerPrint>
 </data>
 <pageSize>1</pageSize>
 <pageNum>1</pageNum>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-5-3"></a>

### 5.5.3. ConfigKeyPair

Attach a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| KeyPairNa me | Strin g | Quer y | No | test | The name of the key pair. |
| MachineSN List | Json | Quer y | No | \["980017160373\*\*\*\*","98 0020500749\*\*\*\*"\] | The list of Bare Metal Computing Platform (BMCP) instance serial numbers (SNs).<br>Each instance can be attached with only one key pair. If the instance has been attached with a key pair, the new key pair automatically replaces the original one after attaching. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":\[ {"MachineSN":"980 017160373\*\*\*", "Message":"succes sful", "Success":true } \],} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | \*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ConfigKeyPair
&MachineSNList=["980017160373****","980020500749****"]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":[
   {
    "MachineSN":"980017160373***",
    "Message":"successful",
    "Success":true
   }
  ]
 },
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <MachineSN>980017160373***</MachineSN>
  <Message>successful</Message>
  <Success>true</Success>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>**</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-5-4"></a>

### 5.5.4. UnbindKeyPair

Detach a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| KeyPairNa me | Strin g | Quer y | No | KeyPair_Name | The name of the key pair. |
| MachineSN List | Json | Quer y | No | \["980017160373\*\*\*\*","98 0020500749\*\*\*\*"\] | The list of Bare Metal Computing Platform (BMCP) instance serial numbers (SNs). |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":\[ {"MachineSN":"980 017160373\*\*\*\*", "Message":"succes sful", "Success":true } \],} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UnbindKeyPair
&KeyPairName=KeyPair_Name
&MachineSNList=["980017160373****","980020500749****"]
&Common request parameters
```

Sample success responses `JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":[
   {
    "MachineSN":"980017160373****",
    "Message":"successful",
    "Success":true
   }
  ]
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <MachineSN>980017160373****</MachineSN>
  <Message>successful</Message>
  <Success>true</Success>
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-5-5"></a>

### 5.5.5. DeleteKeyPair

Delete a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| KeyPairNa me | Strin g | Quer y | No | test-KeyPairName | The name of the key pair. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":{"name":"", "success": true }, } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteKeyPair
&KeyPairName=test-KeyPairName
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "success":true,
   "name":""
  }
 },
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <success>true</success>
  <name />
 </data>
</data>
<errorTitle>Successful</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>Successful</errorMessage>
<errorCode>Successful</errorCode>
<status>200</status>
```

<a id="section-5-6"></a>

## 5.6. Elastic cache acceleration

<a id="section-5-6-1"></a>

### 5.6.1. CreateEdaCluster

Enable an elastic cache acceleration cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {"TaskId":"1284c8b 8-9571-11ee-a39e-16f363c7\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateEdaCluster
&ClusterId=ack-8EEjd6****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TaskId":"1284c8b8-9571-11ee-a39e-16f363c7****"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TaskId>1284c8b8-9571-11ee-a39e-16f363c7****</TaskId>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-6-2"></a>

### 5.6.2. DeleteEdaCluster

Disable an elastic cache acceleration cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TaskId": "1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteEdaCluster
&ClusterId=ack-8EEjd6****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TaskId":"1284c8b8-9571-11ee-a39e-16f363c7****"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TaskId>1284c8b8-9571-11ee-a39e-16f363c7****</TaskId>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-7"></a>

## 5.7. Data distribution

<a id="section-5-7-1"></a>

### 5.7.1. ListMP2pTask

Query the list of data distribution tasks.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| AckCluster ID | Strin g | Quer y | No | cef51d60a6778415ab3a8 026c24\*\*\*\*\* | The unique ID of the Container Service for Kubernetes (ACK) cluster in the Bare Metal Computing Platform (BMCP) cluster. |
| TaskName | Strin g | Quer y | No | task-name | The name of the task. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"TotalCount": 1, "PageSize": 10, "PageNumber": 1, "TaskList": \[ {"PreheatTimeout": "30m", "Status": "Failed", "TaskID": "0040705d-0f0b-4650-9399-d9b78d5d\*\*\*\*", "AckClusterId": "c4c2f574d483740 5b90132ea1b898\* \*\*\*", "Message": "Unknown", "TaskName": "test", "PreheatConcurren cy": 8, "OSSUrl": "oss://{bucket}.en dpoint", "PreheatNodeList": \[ "i-d8pmruuheob4fv1 m\*\*\*\*" \] } \] } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response, which is used to handle different versions of the operation |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListMP2pTask
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "TotalCount":1,
   "PageSize":10,
   "PageNumber":1,
   "TaskList":[
    {
     "PreheatTimeout":"30m",
     "Status":"Failed",
     "TaskID":"0040705d-0f0b-4650-9399-d9b78d5d****",
     "AckClusterId":"c4c2f574d4837405b90132ea1b898****",
     "Message":"Unknown",
     "TaskName":"test",
     "PreheatConcurrency":8,
     "OSSUrl":"oss://{bucket}.endpoint",
     "PreheatNodeList":[
      "i-d8pmruuheob4fv1m****"
     ]
    }
   ]
  }
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <PageNumber>1</PageNumber>
  <TaskList>
   <PreheatTimeout>30m</PreheatTimeout>
   <Status>Failed</Status>
   <TaskID>0040705d-0f0b-4650-9399-d9b78d5d****</TaskID>
   <AckClusterId>c4c2f574d4837405b90132ea1b898****</AckClusterId>
   <Message>Unknown</Message>
   <TaskName>test</TaskName>
   <PreheatConcurrency>8</PreheatConcurrency>
   <OSSUrl>oss://{bucket}.endpoint</OSSUrl>
   <PreheatNodeList>i-d8pmruuheob4fv1m****</PreheatNodeList>
  </TaskList>
 </data>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-7-2"></a>

### 5.7.2. CreateMP2pTask

Create a data distribution task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskName | Strin g | Quer y | Yes | Task1 | The name of the task. |
| AckCluster ID | Strin g | Quer y | Yes | cef51d60a6778415ab3a8 026c24\*\*\*\*\* | The ID of the Container Service for Kubernetes (ACK) cluster. |
| PreheatNo deList | Json | Quer y | No | \["node1","node2"\] | The list of preheat nodes. |
| OSSUrl | Strin g | Quer y | Yes | oss://{bucket}.endpoint | The Uniform Resource Identifier (URI) of the data file in Object Storage Service (OSS). |
| PreheatCo ncurrency | Integ er | Quer y | No | 8 | The preheat concurrency.Valid values: integers from 1 to 100 |
| PreheatTi meout | Integ er | Quer y | No | 30 | The preheat timeout period. Unit: minutes<br>Set an appropriate prehaeat timeout period based on the data size.We recommend that you set at least one minute for every 30 GB of data. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": {"TaskName": "Task1", "AckClusterId": "cef51d60a677841 5ab3a8026c24\*\*\*\* \*" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response, which is used to handle different versions of the operation. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=CreateMP2pTask
&TaskName=Task1
&AckClusterID=cef51d60a6778415ab3a8026c24*****
&PreheatNodeList=["node1","node2"]
&OSSUrl=oss://{bucket}.endpoint
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "data":{
   "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
   "TaskName":"Task1"
  }
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <data>
  <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
  <TaskName>Task1</TaskName>
 </data>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-7-3"></a>

### 5.7.3. DeleteMP2pTask

Delete a data distribution task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskID | Strin g | Quer y | No | 1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\* | The ID of the data distribution task. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "TaskID": "0040705d-0f0b-4650-9399-d9b78d5d\*\*\*\*", "AckClusterId": "c4c2f574d483740 5b90132ea1b898\* \*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DeleteMP2pTask
&TaskID=1284c8b8-9571-11ee-a39e-16f363c7****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TaskID":"0040705d-0f0b-4650-9399-d9b78d5d****",
  "AckClusterId":"c4c2f574d4837405b90132ea1b898****"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TaskID>0040705d-0f0b-4650-9399-d9b78d5d****</TaskID>
 <AckClusterId>c4c2f574d4837405b90132ea1b898****</AckClusterId>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-8"></a>

## 5.8. Node management

<a id="section-5-8-1"></a>

### 5.8.1. DiagnoseQuery

Start an intelligent diagnosis task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Query | Strin g | Quer y | Yes | validateMachineInfo error, hsw is not exists | The fault error message. |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-\*\*\*\*-d01 | The ID of the region. |
| Language | Strin g | Quer y | No | zh_CN | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "status": "pending", "result": "Starting diagnosis", "created_at": "2026-07-09T23:58:44+08:0 0" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DiagnoseQuery
&Query=validateMachineInfo error, hsw is not exists
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-****-d01
&Language=zh_CN
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"1.0",
 "data":{
  "result":"Starting diagnosis",
  "created_at":"2026-07-09T23:58:44+08:00",
  "status":"pending"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>1.0</responseVersion>
<data>
 <result>Starting diagnosis</result>
 <created_at>2026-07-09T23:58:44+08:00</created_at>
 <status>pending</status>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-8-2"></a>

### 5.8.2. TaskQuery

Query the execution progress and results of a fault diagnosis task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskId | Strin g | Quer y | Yes | 1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\* | The ID of the fault diagnosis task. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "allTaskStatus": "processing/compl eted", "response": \[ { "isAdvice": true, "solution": "Solution description", "taskStatus": "pending", "progress": 0.5, "errMessage": "Error message", "subTaskid": "sub-task-001", "subQuery": "Subtask query information" }, {"isAdvice": false, "solution": "Another solution", "taskStatus": "success", "progress": 1.0, "errMessage": "", "subTaskid": "sub-task-002", "subQuery": "Additional query details" } \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=TaskQuery
&TaskId=1284c8b8-9571-11ee-a39e-16f363c7****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "allTaskStatus":"processing/completed",
  "response":[
   {
    "solution":"Solution description",
    "isAdvice":true,
    "progress":0.5,
    "subTaskid":"sub-task-001",
    "taskStatus":"pending",
    "errMessage":"Error message",
    "subQuery":"Subtask query information"
   },
   {
    "solution":"Another solution",
    "isAdvice":false,
    "progress":1.0,
    "subTaskid":"sub-task-002",
    "taskStatus":"success",
    "errMessage":"",
    "subQuery":"Additional query details"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <allTaskStatus>processing/completed</allTaskStatus>
 <response>
  <solution>Solution description</solution>
  <isAdvice>true</isAdvice>
  <progress>0.5</progress>
  <subTaskid>sub-task-001</subTaskid>
  <taskStatus>pending</taskStatus>
  <errMessage>Error message</errMessage>
  <subQuery>Subtask query information</subQuery>
 </response>
 <response>
  <solution>Another solution</solution>
  <isAdvice>false</isAdvice>
  <progress>1</progress>
  <subTaskid>sub-task-002</subTaskid>
  <taskStatus>success</taskStatus>
  <errMessage  />
  <subQuery>Additional query details</subQuery>
 </response>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-8-3"></a>

### 5.8.3. DiagnosePoint

Rate the intelligent diagnosis results.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| TaskId | Strin g | Quer y | Yes | 1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\* | The ID of the task. |
| Score | Float | Quer y | Yes | 5 | The rating, in stars. Valid values: 1 to 5 stars, in increments of 0.5 stars. |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-\*\*\*\*-d01 | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "score": 5, "task_id": "1284c8b8-9571-11ee-a39e-16f363c7\*\*\*\*" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=DiagnosePoint
&Department=4
&ResourceGroup=3
&RegionId=cn-wulan-****-d01
&TaskId=1284c8b8-9571-11ee-a39e-16f363c7****
&Score=5
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "score":5,
  "task_id":"1284c8b8-9571-11ee-a39e-16f363c7****"
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <score>5</score>
 <task_id>1284c8b8-9571-11ee-a39e-16f363c7****</task_id>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-9"></a>

## 5.9. Auto-healing event tickets

<a id="section-5-9-1"></a>

### 5.9.1. ListOrder

Query the list of auto-healing event tickets.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| OrderId | Strin g | Quer y | No | yg9Ve6\*\*\*\* | The ID of the event ticket. |
| OrderType | Strin g | Quer y | No | auto_healing | The type of the event ticket. Currently, only auto_healing is supported. |
| Status | Strin g | Quer y | No | fixed | The ticket status. Valid values:<br>• created: Pending approval<br>• fixed: Closed<br>• timeout: Expired<br>• approved: Approved<br>• rejected: Rejected |
| InstanceId | Strin g | Quer y | No | i-d8pms5uheob3l5ij\*\*\*\* | The ID of the node. |
| ClusterId | Strin g | Quer y | No | ack-ZRy3J8b75x | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster.<br>You can call the ListAckCluster operation to query the cluster ID. |
| CreateTim e | Strin g | Quer y | No | 2021-10-15 08:56:23 | The time when the ticket was created. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "TotalCount": 1, "PageSize": 10, "PageNumber": 1, "OrderList": \[ {"handler": "", "creator": "b225\*\*\*\*-e2ab-47fa-afa3-34f7488c\*\*\*\*-0", "cluster_id": "ack-ZRy3J8b75x", "event_id": "b225\*\*\*\*-e2ab-47fa-afa3-34f7488c\*\*\*\*-0-0", "instance_id": "i-d8pms5uheob3l5ij\* \*\*\*", "create_time": "2026-07-13T01:04:11+08:0 0", "order_source": "bmcp_healing", "order_id": "yg9Ve6\*\*\*\*", "order_type": "auto_healing", "status": "timeout"} \] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListOrder
&OrderType=auto_healing
&Status=fixed
&ClusterId=ack-ZRy3J8b75x
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "PageNumber":1,
  "OrderList":[
   {
    "handler":"",
    "creator":"b225****-e2ab-47fa-afa3-34f7488c****-0",
    "cluster_id":"ack-ZRy3J8b75x",
    "event_id":"b225****-e2ab-47fa-afa3-34f7488c****-0-0",
    "instance_id":"i-d8pms5uheob3l5ij****",
    "create_time":"2026-07-13T01:04:11+08:00",
    "order_source":"bmcp_healing",
    "order_id":"yg9Ve6****",
    "order_type":"auto_healing",
    "status":"timeout"
   }
  ]
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <OrderList>
  <handler  />
  <creator>b225****-e2ab-47fa-afa3-34f7488c****-0</creator>
  <cluster_id>ack-ZRy3J8b75x</cluster_id>
  <event_id>b225****-e2ab-47fa-afa3-34f7488c****-0-0</event_id>
  <instance_id>i-d8pms5uheob3l5ij****</instance_id>
  <create_time>2026-07-13T01:04:11+08:00</create_time>
  <order_source>bmcp_healing</order_source>
  <order_id>yg9Ve6****</order_id>
  <order_type>auto_healing</order_type>
  <status>timeout</status>
 </OrderList>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-9-2"></a>

### 5.9.2. GetOrderDetail

Query the details of an auto-healing event ticket.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| OrderId | Strin g | Quer y | No | yg9Ve6\*\*\*\* | The ID of the event ticket.<br>You can call the ListOrder operation to query the event ticket ID. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "order_detail": {"handler": "", "creator": "4d92\*\*\*\*-06ed-4fac-8658-0ddd7734\*\*\*\*-0", "cluster_id": "ack-ZRy3J8\*\*\*\*", "event_id": "4d92\*\*\*\*-06ed-4fac-8658-0ddd7734\*\*\*\*-0-0", "instance_id": "i-d8pms5uheob3l5ij\* \*\*\*", "create_time": "2026-07-09T23:58:11+08:0 0", "complete_time": "2026-07-13T01:02:11+08:0 0", "approved_time": "2026-07-09T23:58:44+08:0 0", "order_source": "bmcp_healing", "order_id": "QG0J0u\*\*\*\*", "order_type": "auto_healing", "status": "fixed" }} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=GetOrderDetail
&OrderId=yg9Ve6****
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"",
 "data":"",
 "errorTitle":"",
 "requestId":"",
 "success":"",
 "errorMessage":"",
 "errorCode":"",
 "status":""
}
```

<a id="section-5-9-3"></a>

### 5.9.3. UpdateOrder

Approve an auto-healing event ticket.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| OrderId | Strin g | Quer y | No | yg9Ve6\*\*\*\* | The ID of the event ticket.<br>You can call the ListOrder operation to query the event ticket ID. |
| Status | Strin g | Quer y | No | fixed | The status of the event ticket. Valid values:<br>• created: Pending approval<br>• fixed: Closed<br>• timeout: Expired<br>• approved: Approved<br>• rejected: Rejected |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "order_detail": {"handler": "", "creator": "4d92\*\*\*\*-06ed-4fac-8658-0ddd7734\*\*\*\*-0", "cluster_id": "ack-ZRy3J8\*\*\*\*", "event_id": "4d92\*\*\*\*-06ed-4fac-8658-0ddd7734\*\*\*\*-0-0", "instance_id": "i-d8pms5uheob3l5ij\* \*\*\*", "create_time": "2026-07-09T23:58:11+08:0 0", "complete_time": "2026-07-13T01:02:11+08:0 0", "approved_time": "2026-07-09T23:58:44+08:0 0", "order_source": "bmcp_healing", "order_id": "QG0J0u\*\*\*\*", "order_type": "auto_healing", "status": "fixed" }} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=UpdateOrder
&OrderId=yg9Ve6****
&Status=fixed
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "order_detail":{
   "handler":"",
   "creator":"4d92****-06ed-4fac-8658-0ddd7734****-0",
   "cluster_id":"ack-ZRy3J8****",
   "event_id":"4d92****-06ed-4fac-8658-0ddd7734****-0-0",
   "instance_id":"i-d8pms5uheob3l5ij****",
   "create_time":"2026-07-09T23:58:11+08:00",
   "complete_time":"2026-07-13T01:02:11+08:00",
   "approved_time":"2026-07-09T23:58:44+08:00",
   "order_source":"bmcp_healing",
   "order_id":"QG0J0u****",
   "order_type":"auto_healing",
   "status":"fixed"
  }
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <order_detail>
  <handler  />
  <creator>4d92****-06ed-4fac-8658-0ddd7734****-0</creator>
  <cluster_id>ack-ZRy3J8****</cluster_id>
  <event_id>4d92****-06ed-4fac-8658-0ddd7734****-0-0</event_id>
  <instance_id>i-d8pms5uheob3l5ij****</instance_id>
  <create_time>2026-07-09T23:58:11+08:00</create_time>
  <complete_time>2026-07-13T01:02:11+08:00</complete_time>
  <approved_time>2026-07-09T23:58:44+08:00</approved_time>
  <order_source>bmcp_healing</order_source>
  <order_id>QG0J0u****</order_id>
  <order_type>auto_healing</order_type>
  <status>fixed</status>
 </order_detail>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage  />
<errorCode  />
<status>0</status>
```

<a id="section-5-10"></a>

## 5.10. Recycle bin

<a id="section-5-10-1"></a>

### 5.10.1. ListRecycleBMCPMachine

Query information about recycled Bare Metal Computing Platform (BMCP) bare metal instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| Application Group | Strin g | Quer y | No | recycle | The type of the resource.Currently, only recycle is supported. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number.Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| InstanceN ameList | Json | Quer y | No | \["test1","test2"\] | The list of node names. |
| KeyPairNa me | Strin g | Quer y | No | test-KeyPairName | The name of the key pair. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The type of the instance deployed. Valid values:<br>• bmcp: Intelligent computing high-bandwidth network<br>• bmcp_managed: Intelligent computing -managed<br>• bmcp_no_clone: Intelligent computing -in-band managed<br>• ehpc: High-performance computing (HPC) high-bandwidth network<br>• ehpc_managed: HPC -managed<br>• aspeed: Training and inference optimization<br>• base: Basic intelligent computing<br>• bfi: Converged high-bandwidth network<br>• bfi_base: Cconverged basic |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p\*\*\*\* | The ID of the security group. |
| ClusterTyp e | Strin g | Quer y | No | bmcp | The cluster type. Valid values:<br>• bmcp: Bare metal -intelligent computing cluster<br>• ack: Container Service for Kubernetes (ACK) -intelligent computing cluster<br>• ehpcp: Bare metal -HPC cluster<br>• bfi: Converged computing cluster |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6\*\*\*\* | The ID of the cluster. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| State | Strin g | Quer y | No | offline | The operation status of the node. If you leave this parameter empty, nodes in all statuses are returned. Valid values:<br>• manageable: Running<br>• available: Completed<br>• enroll, rolling: Creating<br>• operating: Under O&amp;M<br>• cleaning: Releasing<br>• deleting: Deleting<br>• rebooting: Restarting<br>• powering_on: Starting<br>• shutting_down: Stopping<br>• offline: No heartbeat<br>• error: Failed<br>• unknown: Unknown |
| RunningSt ate | Strin g | Quer y | No | running | The heartbeat status.Valid values:<br>• running: Running<br>• offline: No heartbeat |
| InstanceN ame | Strin g | Quer y | No | i-d8pms5uheob4fv1m\*\*\*\* | The name of the node. |
| InstanceAli as | Strin g | Quer y | No | c25j0\*\*\*\*.cloud.j06.\*\*\*\* | The alias of the node, which is an alternative name for easy identification. |
| ID | Strin g | Quer y | No | 2 | The ID of the node. |
| SN | Strin g | Quer y | No | 21061\*\*\*\*JXDP400\*\*\*\* | The serial number (SN) of the node. |
| IP | Strin g | Quer y | No | 192.168.1.1 | The IP address of the node. |
| BMCIP | Strin g | Quer y | No | 192.168.1.1 | The BMC IP address of the node. |
| MachineTy pe | Strin g | Quer y | No | QPG78P4M\*\*\*\*.03BB | The name of the instance type. |
| VPCID | Strin g | Quer y | No | vpc-bp1b1xjllp3ve5yze\*\*\*\* | The ID of the virtual private cloud (VPC). |
| AliYunAssi stID | Strin g | Quer y | No | mi-hz034jn\*\*\*yxhc0 | The globally unique ID of Cloud Assistant. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "PageSize": 10, "data": {"RecycleBMCPMac hineList": \[ {"DeployType": "bfi_base", "RunningState": "running", "Image": "alinux_3_x86_64_uefi_20260423_bf3.qcow2", "Gpu": "NVIDIA_\*\*\*\*_PCIe", "Department": 4, "OverlayEnabled": false, "InstanceAlias": "i-7c4ba42a32f64\*\*\* \*", "AliYunAssistID": "", "ID": 181, "RawIP": "10.66.\*\*\*\*.4", "HostName": "test_name", "Status": "power_on", "OsUpdate": false, "IP": "10.66.\*\*\*\*.4", "InstanceName": "test_neme", "State": "offline", "Region": "cn-wulan-\*\*\*\*-d01", "BMCIP": "10.38.\*\*\*\*.47", "DepartmentName ": "iaas_test", "NetworkCardType ": "0", "AgentID": 24, "VideoMemory": 640, "ResourceGroupNa me": "ResourceSet(iaas_test)", "Organization": "4", "Description": "test", "VPCID": "vpc-3gas7mox8s04hkd 38\*\*\*\*", "TflopsFP32": 6048, "Config": {"Memory": 18, "CPUNumber": 14}, "Operation": "", "RecycleTime": "", "DpuInfo": {"ErrorDescription": "", "Status": "power_on", "LoginName": "root", "MachineSN": "2106\*\*\*\*UPXDP50 0\*\*\*\*", "RunningState": "running", "CGWPorts": "", "Zone": "", "Hostname": "c25d0\*\*\*\*.cloud.d 03.\*\*\*\*", "MachineType": "PG\*\*\*\*M6S2\*\*\*\*.3 2", "BMCPassword": "", "Specification": "", "BMCPort": "", "InstanceName": "test", "BMCIP": "10.38.\*\*\*\*.44", "LastHeartbeatTim e": "2026-07-30T02:33:25+08:0 0", "ID": 1, "SN": "\*\*\*\*30XZ0\*\*\*\*", "BMCUser": "", "ASWID": "EHSW-200G-D-G3-POD1-RMC2-5-\*\*\*\*-35-3-1.\*\*\*\*", "Subnet": "", "RawIP": "10.\*\*\*\*.\*\*\*\*.5", "LoginPwd": "" }, "MappingStatus": "Offline", "ApplicationGroup": "recycle", "GpuNum": 8, "Monitor": "", "NetworkCardNum": 1, "VPCSubnet": "vsw-3ga6o6e1eywm8a yat\*\*\*\*", "ClusterName": "test", "VirtualStrategy": "", "RMRegionId": "cn-wulan-\*\*\*\*-d01", "SN": "test-name", "ResourceGroup": 3, "ImageUniqueKey": "i-d86q88mheobd49s t\*\*\*\*", "OS": "Aliyun", "ClusterId": "bfi-sqFetW\*\*\*\*", "Zone": "cn-wulan-\*\*\*\*-\*\*\*\*-a", "CreateTime": "2026-06-12T14:47:26+08:0 0", "MachineType": "test_name", "SupportVirtStg": "", "Specification": "dpu-host-default-bfi-base", "ClusterType": "bfi", "LvmCapacity": "0", "RetentionPeriod": 0, "ClusterArchType": "", "Extra": "", "DefaultImage": "alinux_3_x86_64_uefi_20260423_bf3.qcow2", "ReleaseTime": "", "UserId": "127756957048\*\*\* \*", "RecycleStatus": "", "RegionId": "cn-wulan-\*\*\*\*-d01" } \]}, "TotalCount": 11, "PageNumber": 2 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ListRecycleBMCPMachine
&Department=4
&ResourceGroup=3
&ApplicationGroup=recycle
&ClusterType=bmcp
&DeployType=bmcp
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"v1",
 "data":{
  "TotalCount":11,
  "PageSize":10,
  "data":{
   "RecycleBMCPMachineList":[
    {
     "DeployType":"bfi_base",
     "RunningState":"running",
     "Image":"alinux_3_x86_64_uefi_20260423_bf3.qcow2",
     "Gpu":"NVIDIA_****_PCIe",
     "Department":4,
     "OverlayEnabled":false,
     "InstanceAlias":"i-7c4ba42a32f64****",
     "AliYunAssistID":"",
     "ID":181,
     "RawIP":"10.66.****.4",
     "HostName":"test_name",
     "Status":"power_on",
     "OsUpdate":false,
     "IP":"10.66.****.4",
     "InstanceName":"test_neme",
     "State":"offline",
     "Region":"cn-wulan-****-d01",
     "BMCIP":"10.38.****.47",
     "DepartmentName":"iaas_test",
     "NetworkCardType":"0",
     "AgentID":24,
     "VideoMemory":640,
     "ResourceGroupName":"ResourceSet(iaas_test)",
     "Organization":"4",
     "Description":"test",
     "VPCID":"vpc-3gas7mox8s04hkd38****",
     "TflopsFP32":6048,
     "Config":{
      "Memory":18,
      "CPUNumber":14
     },
     "Operation":"",
     "RecycleTime":"",
     "DpuInfo":{
      "ErrorDescription":"",
      "Status":"power_on",
      "LoginName":"root",
      "MachineSN":"2106****UPXDP500****",
      "RunningState":"running",
      "CGWPorts":"",
      "Zone":"",
      "Hostname":"c25d0****.cloud.d03.****",
      "MachineType":"PG****M6S2****.32",
      "BMCPassword":"",
      "Specification":"",
      "BMCPort":"",
      "InstanceName":"test",
      "BMCIP":"10.38.****.44",
      "LastHeartbeatTime":"2026-07-30T02:33:25+08:00",
      "ID":1,
      "SN":"****30XZ0****",
      "BMCUser":"",
      "ASWID":"EHSW-200G-D-G3-POD1-RMC2-5-****-35-3-1.****",
      "Subnet":"",
      "RawIP":"10.****.****.5",
      "LoginPwd":""
     },
     "MappingStatus":"Offline",
     "ApplicationGroup":"recycle",
     "GpuNum":8,
     "Monitor":"",
     "NetworkCardNum":1,
     "VPCSubnet":"vsw-3ga6o6e1eywm8ayat****",
     "ClusterName":"test",
     "VirtualStrategy":"",
     "RMRegionId":"cn-wulan-****-d01",
     "SN":"test-name",
     "ResourceGroup":3,
     "ImageUniqueKey":"i-d86q88mheobd49st****",
     "OS":"Aliyun",
     "ClusterId":"bfi-sqFetW****",
     "Zone":"cn-wulan-****-****-a",
     "CreateTime":"2026-06-12T14:47:26+08:00",
     "MachineType":"test_name",
     "SupportVirtStg":"",
     "Specification":"dpu-host-default-bfi-base",
     "ClusterType":"bfi",
     "LvmCapacity":"0",
     "RetentionPeriod":0,
     "ClusterArchType":"",
     "Extra":"",
     "DefaultImage":"alinux_3_x86_64_uefi_20260423_bf3.qcow2",
     "ReleaseTime":"",
     "UserId":"127756957048****",
     "RecycleStatus":"",
     "RegionId":"cn-wulan-****-d01"
    }
   ]
  },
  "PageNumber":2
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>v1</responseVersion>
<data>
 <TotalCount>11</TotalCount>
 <PageSize>10</PageSize>
 <data>
  <RecycleBMCPMachineList>
   <DeployType>bfi_base</DeployType>
   <RunningState>running</RunningState>
   <Image>alinux_3_x86_64_uefi_20260423_bf3.qcow2</Image>
   <Gpu>NVIDIA_****_PCIe</Gpu>
   <Department>4</Department>
   <OverlayEnabled>false</OverlayEnabled>
   <InstanceAlias>i-7c4ba42a32f64****</InstanceAlias>
   <AliYunAssistID  />
   <ID>181</ID>
   <RawIP>10.66.****.4</RawIP>
   <HostName>test_name</HostName>
   <Status>power_on</Status>
   <OsUpdate>false</OsUpdate>
   <IP>10.66.****.4</IP>
   <InstanceName>test_neme</InstanceName>
   <State>offline</State>
   <Region>cn-wulan-****-d01</Region>
   <BMCIP>10.38.****.47</BMCIP>
   <DepartmentName>iaas_test</DepartmentName>
   <NetworkCardType>0</NetworkCardType>
   <AgentID>24</AgentID>
   <VideoMemory>640</VideoMemory>
   <ResourceGroupName>ResourceSet(iaas_test)</ResourceGroupName>
   <Organization>4</Organization>
   <Description>test</Description>
   <VPCID>vpc-3gas7mox8s04hkd38****</VPCID>
   <TflopsFP32>6048</TflopsFP32>
   <Config>
    <Memory>18</Memory>
    <CPUNumber>14</CPUNumber>
   </Config>
   <Operation  />
   <RecycleTime  />
   <DpuInfo>
    <ErrorDescription  />
    <Status>power_on</Status>
    <LoginName>root</LoginName>
    <MachineSN>2106****UPXDP500****</MachineSN>
    <RunningState>running</RunningState>
    <CGWPorts  />
    <Zone  />
    <Hostname>c25d0****.cloud.d03.****</Hostname>
    <MachineType>PG****M6S2****.32</MachineType>
    <BMCPassword  />
    <Specification  />
    <BMCPort  />
    <InstanceName>test</InstanceName>
    <BMCIP>10.38.****.44</BMCIP>
    <LastHeartbeatTime>2026-07-30T02:33:25+08:00</LastHeartbeatTime>
    <ID>1</ID>
    <SN>****30XZ0****</SN>
    <BMCUser  />
    <ASWID>EHSW-200G-D-G3-POD1-RMC2-5-****-35-3-1.****</ASWID>
    <Subnet  />
    <RawIP>10.****.****.5</RawIP>
    <LoginPwd  />
   </DpuInfo>
   <MappingStatus>Offline</MappingStatus>
   <ApplicationGroup>recycle</ApplicationGroup>
   <GpuNum>8</GpuNum>
   <Monitor  />
   <NetworkCardNum>1</NetworkCardNum>
   <VPCSubnet>vsw-3ga6o6e1eywm8ayat****</VPCSubnet>
   <ClusterName>test</ClusterName>
   <VirtualStrategy  />
   <RMRegionId>cn-wulan-****-d01</RMRegionId>
   <SN>test-name</SN>
   <ResourceGroup>3</ResourceGroup>
   <ImageUniqueKey>i-d86q88mheobd49st****</ImageUniqueKey>
   <OS>Aliyun</OS>
   <ClusterId>bfi-sqFetW****</ClusterId>
   <Zone>cn-wulan-****-****-a</Zone>
   <CreateTime>2026-06-12T14:47:26+08:00</CreateTime>
   <MachineType>test_name</MachineType>
   <SupportVirtStg  />
   <Specification>dpu-host-default-bfi-base</Specification>
   <ClusterType>bfi</ClusterType>
   <LvmCapacity>0</LvmCapacity>
   <RetentionPeriod>0</RetentionPeriod>
   <ClusterArchType  />
   <Extra  />
   <DefaultImage>alinux_3_x86_64_uefi_20260423_bf3.qcow2</DefaultImage>
   <ReleaseTime  />
   <UserId>127756957048****</UserId>
   <RecycleStatus  />
   <RegionId>cn-wulan-****-d01</RegionId>
  </RecycleBMCPMachineList>
 </data>
 <PageNumber>2</PageNumber>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-10-2"></a>

### 5.10.2. RevertMachine

Restore instances from the recycle bin.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RevertMac hineList | Json | Quer y | No | \[ { "InstanceName": "i-d8pms5uheob4fv1m\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i-d9jfbieheob5ghiu\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" } \] | The list of bare metal instances to restore. |

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": \[ {"InstanceName": "i-d8pms5uheob4fv1 m\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" }, {"InstanceName": "i-d9jfbieheob5ghiu\*\* \*\*", "ClusterBzid": "", "ClusterType": "bmcp" } \], "total": 10, "pageNum": 1, "pageSize": 10 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=RevertMachine
&Department=4
&ResourceGroup=3
&RevertMachineList=[
  {
    "InstanceName": "i-d8pms5uheob4fv1m****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
  },
  {
    "InstanceName": "i-d9jfbieheob5ghiu****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
  }
]
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"1.0",
 "data":{
  "total":10,
  "data":[
   {
    "InstanceName":"i-d8pms5uheob4fv1m****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
   },
   {
    "InstanceName":"i-d9jfbieheob5ghiu****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
   }
  ],
  "pageSize":10,
  "pageNum":1
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>1.0</responseVersion>
<data>
 <total>10</total>
 <data>
  <InstanceName>i-d8pms5uheob4fv1m****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <data>
  <InstanceName>i-d9jfbieheob5ghiu****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```

<a id="section-5-10-3"></a>

### 5.10.3. ReleaseMachine

Release machines from the recycle bin back to the resource pool.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
| --- | --- | --- | --- | --- | --- |
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ReleaseMa chineList | Json | Quer y | No | \[ { "InstanceName": "i-d8pms5uheob4fv1m\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i-d9jfbieheob5ghiu\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" } \] | The list of bare metal instances to restore. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks. Valid values:<br>• true: Clear data disks.After the data is permanently deleted, you must initialize the node in the resource pool to fully reinstall the node.<br>• false: Do not clear data disks.<br>Default value: false |

<table>
  <tr>
    <td>IsQuickCle an</td>
    <td>Bool ean</td>
    <td>Quer y</td>
    <td>No</td>
    <td>false</td>
    <td>Whether to quickly clear the system disk. Valid values:<br>• true: Clear the system disk. The system disk of the node is restored to its initial image and the node is quickly released. After the release, you can quickly apply for the resource again.<br>• false: Do not clear the system disk.<br>Default value: false</td>
  </tr>
</table>

**Response parameters**

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": \[ {"InstanceName": "i-d8pms5uheob4fv1 m\*\*\*\*", "ClusterBzid": "", "ClusterType": "bmcp" }, {"InstanceName": "i-d9jfbieheob5ghiu\*\* \*\*", "ClusterBzid": "", "ClusterType": "bmcp" } \], "total": 10, "pageNum": 1, "pageSize": 10 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D-5EC1-97C8-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```text
http://[Endpoint]/?Action=ReleaseMachine
&Department=4
&ResourceGroup=3
&RevertMachineList=[
  {
    "InstanceName": "i-d8pms5uheob4fv1m****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
  },
  {
    "InstanceName": "i-d9jfbieheob5ghiu****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
  }
]
&OsUpdate=false
&Common request parameters
```

Sample success responses

`JSON`  format

```json
{
 "responseVersion":"1.0",
 "data":{
  "total":10,
  "data":[
   {
    "InstanceName":"i-d8pms5uheob4fv1m****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
   },
   {
    "InstanceName":"i-d9jfbieheob5ghiu****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
   }
  ],
  "pageSize":10,
  "pageNum":1
 },
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
}
```

`XML`  format

```xml
<responseVersion>1.0</responseVersion>
<data>
 <total>10</total>
 <data>
  <InstanceName>i-d8pms5uheob4fv1m****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <data>
  <InstanceName>i-d9jfbieheob5ghiu****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data>
<errorTitle>“”</errorTitle>
<requestId>F0A8A039-930D-5EC1-97C8-************</requestId>
<success>true</success>
<errorMessage>&quot;“</errorMessage>
<errorCode  />
<status>0</status>
```
