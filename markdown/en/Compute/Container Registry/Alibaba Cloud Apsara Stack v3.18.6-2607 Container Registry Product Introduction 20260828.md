Alibaba Cloud  
Apsara Stack  
Container Registry  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Container Registry](#section-1)
    - [1.1. Product details](#section-1-1)
    - [1.2. Benefits](#section-1-2)
    - [1.3. Functions and features](#section-1-3)
    - [1.4. Scenarios](#section-1-4)
    - [1.5. Key concepts](#section-1-5)
    - [1.6. Limitations](#section-1-6)

<a id="section-1"></a>

# 1.Container Registry

Container Registry is a platform that allows you to manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: image permission management, synchronous image distribution, and content signing. The features allow you to manage the entire lifecycle of container images. Container Registry simplifies the setup and O&M of container registry. Container Registry is integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to easily create and deliver a one-stop solution for cloud-native applications.

<a id="section-1-1"></a>

## 1.1. Product details

Container Registry is a platform that lets you manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: artifact management, image replication, artifact security, and deployment integration.

**Artifact management**

- Secure hosting: Host container images securely within namespaces.

- Lifecycle management: Query artifacts and image versions, and delete artifacts and image repositories.

- Fine-grained permission management: Manage permissions for users, Apsara Stack Cloud Management (ASCM) departments, and resource sets.

- Version immutability: Configure version immutability for images and OCI artifacts.

**Image replication**

- Triggers: Configure triggers to automatically initiate events when a container image is updated.

- Image synchronization: Manually synchronize specific image versions for disaster recovery and backup across multiple regions. The service also supports automatic synchronization after an image is pushed .

**Artifact security**

- Encrypted image distribution: Distribute container images securely using the HTTPS protocol.

- Container image signing: Sign container images to ensure end-to-end consistency from distribution to deployment. This prevents man-in-the-middle (MITM) attacks and stops unauthorized images from being updated or run.

- Image security scanning: Scan container images to detect vulnerabilities.

**Deployment integration**

- Secret-free pulls: When deploying on a container service platform, you can configure secret-free pulls to avoid the need to set a Secret for each pull operation.

- Deployment selection: When deploying on a container service platform, you can visually select image repositories and versions from ACR.

<a id="section-1-2"></a>

## 1.2. Benefits

Container Registry provides you with the following benefits: ease of use, security, and integrability.

**Ease of use**

- Allows you to create an image repository without the need to manually build and maintain the images.

- Allows you to pull and push images across multiple regions in a fast and stable manner.

**Security and controllability**

- Provides an all-in-one management system for image permissions. This ensures secure and convenient image sharing.

- Provides the image scanning feature to identify vulnerabilities in images and prompt vulnerability levels.

**Efficient distribution**

- Supports large-scale image distribution in a single region and concurrent image pulls on 500 nodes.

- Supports cross-region image replication and cross-cloud synchronous image distribution. Supports manual and automatic image replication.

**Seamless integration with other Alibaba Cloud services**

Integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to implement continuous deployment after images are updated.

<a id="section-1-3"></a>

## 1.3. Functions and features

This topic describes the core features of Container Registry and how different editions of Container Registry support these features, including instance management, artifact distribution and management, container image signing and management, and integration with the Container Service for Kubernetes (ACK) console for secret-free image pulling and visual deployment. These capabilities help enterprises efficiently manage the full lifecycle of container images.

**Container**

**Container**

**Container**

**Registry**

**Feature**

**Feature**

**Registry**

**Registry**

**Module**

**Multi-**

**category**

**description**

**Standard**

**Advanced**

**Instance**

**Edition**

**Edition**

**Edition**

The system supports the creation of multiple

Multi-instance

Not

Not

instances. By

Supported

creation

supported

supported

default, you can create up to 100 instances.

Instance management

The system

Cross-

supports

instance

image

Not

Not

image

repository

Supported

supported

supported

synchronizati

synchronizati

on

on across instances.

The system supports the

Instance

deletion and

Not

Not

Supported

deletion

release of

supported

supported

image instances.

You can manually trigger the synchronizati on of a

Manual

specific

synchronizati

image

Supported

Supported

Supported

on

version to enable geo-disaster recovery for container images.

The system automatically synchronizes

Automatic

images after

Not

synchronizati

Supported

Supported

a push based

supported

on

on synchronizati

Artifact

on rules.

distribution

After a container image update, the

Trigger

Supported

Supported

Supported

correspondin g event is automatically triggered.

The system

DADI image

supports

Not

Supported

Supported

acceleration

DADI image

supported

acceleration.

You can configure the

Encrypted

HTTPS

container

protocol to

Supported

Supported

Supported

image

distribute

distribution

container images.

The system supports container image signing to ensure end-to-end consistency from distribution to deployment, preventing

Container

Not

Supported

Supported

man-in-the-

image signing

supported

middle attacks and unauthorized image updates or execution.

Artifact security

The system provides a graphical interface for signing operations and supports signing at the instance dimension and namespace dimension.

> <img src="assets/b90af9531619bfc427e611d62e96a9ae.png" width="14" alt="">
>
> **Note**
>
> This feature depends on KMS and Containe r Security Service (CSS)

Signing

Supported

Supported

Supported

> and

management

> requires these services to work together.

The system supports

Not

immutable

Supported

Supported

supported

image versions.

The system supports namespace-based

Not

partitioning

Supported

Supported

supported

for secure container image hosting.

Container

Artifact

You can

image

management

query container image

Not

versions and

Supported

Supported

supported

delete container image repositories.

The system supports the management of the permissions on resource

Supported

Supported

Supported

sets and departments in the Apsara Uni-manager Management Console.

The system supports secret-free image pulling during deployment

Password-free

in the ACK

Not

Supported

Supported

pulling

console,

supported

eliminating the need to reconfigure secrets for each deployment.

Deployment integration

During deployment in the ACK console, you

Deployment

can visually

selection

select image

Supported

Supported

Supported

repositories and versions from Container Registry.

> **Note**
>
> Container Registry fully supports the IPv4/IPv6 dual-stack network mode.

<a id="section-1-4"></a>

## 1.4. Scenarios

Container Registry is suitable for scenarios such as continuous delivery and automatic image synchronization.

**Continuous delivery**

Container Registry is integrated with Jenkins to automate DevOps pipelines from code committing to application deployment and ensure that code is committed for deployment only after the code passes automated testing. This simplifies application deployment and accelerates application iteration.

- DevOps automation

  Container Registry can automate DevOps pipelines, from code update to code building, image building, and application deployment.

- Environment consistency

  Container Registry lets you deliver code together with the runtime environment that is built based on an immutable architecture.

- Continuous feedback

  Container Registry returns results in real time after integration or delivery.

**Automatic image synchronization**

Your containerized applications may require deployment across multiple regions. In such scenarios, you can commit a container application once for deployment to multiple regions. The image synchronization feature of Container Registry improves automated distribution efficiency, reduces manual O&M costs, and enhances disaster recovery capabilities.

- Multi-scenario synchronization

  - Supports synchronization across regions.

  - Supports both manual synchronization and automatic synchronization triggered by image updates.

- Scheduling optimization

  Optimizes the scheduling of image synchronization to increase the success rate.

- Security and compliance

  Supports data encryption to ensure the security of the synchronized images.

<a id="section-1-5"></a>

## 1.5. Key concepts

This topic introduces the key concepts of Alibaba Cloud Container Registry (ACR) to help you build a foundational understanding of the service.

- **Container image**

  A container image is a standardized delivery artifact that contains an application and all its dependencies. You can build an application into a container image with a Dockerfile, push the image to an image repository, and then pull it to start containers in your test or production environments.

- **Container registry instance**

  To manage private images, you first create a container registry instance and image repositories within it. After logging in to a repository, you can push new versions of a modified image or push an image built locally.

- **OCI artifact**

  In addition to container images, ACR supports packaging various types of data, such as Helm charts and CNAB bundles, into OCI-compliant artifacts. These artifacts follow the structure defined by the OCI artifact specification, including manifests and indexes. This provides a unified way to store, manage, and distribute different types of artifacts.

- **RAM access control**

  Resource Access Management (RAM) is an Alibaba Cloud service that lets you manage user identities and resource access permissions. You can create multiple RAM users under a single Alibaba Cloud account to represent employees, systems, or applications within your organization.

- **RAM user**

  A RAM user is an identity in RAM with a unique ID and credentials. A RAM user typically represents a person or an application. You can grant different image access permissions to different RAM users.

- **Helm chart**

  - Helm is a package manager for Kubernetes that helps you manage charts and their running instances, known as releases.

  - A chart is a collection of files that describe a related set of Kubernetes resources. It contains everything needed to run an application, including images, dependencies, and resource definitions. For example, a single chart can deploy a combination of WordPress and MySQL, or an etcd cluster.

- **OSS**

  Object Storage Service (OSS) is an Alibaba Cloud storage service that offers high scalability, security, durability, and cost-effectiveness. OSS provides a platform-independent RESTful API that lets you store and access any type of data from any application.

- **OSS bucket**

  An OSS bucket is a container that stores objects in OSS. All objects must reside in a bucket. A bucket has configurable properties, such as its region, access permissions, and storage class. You can create different types of buckets to meet your specific data storage needs. The Enterprise Edition of Alibaba Cloud Container Registry (ACR) uses a customizable OSS bucket to host container images.

<a id="section-1-6"></a>

## 1.6. Limitations

Before using Container Registry (ACR), understand its limitations.

<table>
  <tr>
    <th rowspan="2">Limit</th>
    <th colspan="3">Value</th>
  </tr>
  <tr>
    <td>Standard edition</td>
    <td>Advanced edition</td>
    <td>Multi-instance edition</td>
  </tr>
  <tr>
    <td>Number of namespaces</td>
    <td>15</td>
    <td>1,000</td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>Number of image repositories per namespace</td>
    <td>1,000</td>
    <td>100,000</td>
    <td>100,000</td>
  </tr>
  <tr>
    <td>Number of instances</td>
    <td>/</td>
    <td>/</td>
    <td>100</td>
  </tr>
</table>
