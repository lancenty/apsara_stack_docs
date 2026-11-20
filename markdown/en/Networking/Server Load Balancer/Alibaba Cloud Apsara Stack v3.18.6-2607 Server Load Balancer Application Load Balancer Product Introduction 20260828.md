Alibaba Cloud  
Apsara Stack  
Server Load Balancer  
Application Load Balancer  
Product Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260828

**Table of Contents**

- [1.Product details](#section-1)
- [2.Product value](#section-2)
- [3.Scenarios](#section-3)
- [4.Features](#section-4)

<a id="section-1"></a>

# 1.Product details

**Overview**

Application Load Balancer (ALB) is a load balancing service from Alibaba Cloud that provides powerful application-layer processing and advanced routing features. It is designed for application-layer load balancing scenarios that use protocols such as HTTP, HTTPS, and QUIC.

| Concept | Description |
| --- | --- |
| Instance | An instance operates at Layer 7 and provides powerful Layer 7 load balancing. It distributes traffic across multiple backend servers to increase your application's service throughput. |
| Listener | A listener is the smallest service unit of an ALB instance. Configure a protocol and port for the listener to specify the traffic to process, such as HTTP traffic on port 80. Each ALB instance requires at least one listener to process and distribute traffic. By default, you can add up to 50 listeners to each ALB instance to handle different types of service traffic. |
| Forwarding rule | A forwarding rule determines how an ALB instance routes requests to backend servers in one or more backend server groups. ALB has advanced routing capabilities. In addition to traditional routing rules, it can forward requests based on rules such as HTTP headers, cookies, and HTTP request methods. This allows for flexible, service-based scheduling. |
| Server group | A server group is a logical group of backend servers that process requests distributed by ALB. In ALB, server groups exist independently of ALB instances.You can attach the same server group to different ALB instances. By default, you can add up to 100 backend servers to each server group. ALB server groups support various types of backend servers, such as ECS instances, ENIs, and IP addresses. |
| Health check | ALB uses health checks to determine the service availability of backend servers.ALB detects unhealthy servers in a server group and stops distributing traffic to them. ALB supports flexible health check configurations, such as protocol, port, and various health check thresholds. ALB also provides health check templates that you can quickly apply to different server groups. |

<table>
  <tr>
    <td>Access control</td>
    <td>Set an access whitelist or blacklist for a listener:<br>• <strong>Whitelist</strong>: <strong>Allows specific IP addresses to access the load balancer.</strong>Only requests from the IP addresses or address ranges set in the selected access control policy group are forwarded. A whitelist is suitable for scenarios where only specific IP addresses are allowed access.<br>Setting a whitelist poses certain service risks. After you set a whitelist, only IP addresses in the whitelist can access the SLB listener. If you enable a whitelist but do not add any IP addresses to the policy group, the listener forwards all requests.<br>• <strong>Blacklist</strong>: <strong>Denies specific IP addresses access to the load balancer.</strong>Requests from the IP addresses or address ranges set in the selected access control policy group are not forwarded. A blacklist is suitable for scenarios where you want to restrict access from specific IP addresses.<br>If you enable a blacklist but do not add any IP addresses to the policy group, the listener forwards all requests.</td>
  </tr>
  <tr>
    <td>Certificate management</td>
    <td>Manage server certificates and CA certificates:<br>• <strong>Server certificate: Proves the identity of the server.</strong> A browser uses the server certificate to check whether the certificate sent by the server is issued by a trusted authority.<br>• CA certificate: The server uses a CA certificate to authenticate the <strong>signature of a client certificate.</strong> If the authentication fails, the connection is rejected.</td>
  </tr>
</table>

<a id="section-2"></a>

# 2.Product value

Application Load Balancer (ALB) provides powerful processing capabilities and advanced routing features for application-layer protocols such as HTTP, HTTPS, and QUIC. This topic describes the benefits of ALB.

**High elasticity at the application layer**

ALB operates at the application layer. It distributes traffic to scale your applications, eliminates single points of failure, and improves system availability.

**Advanced protocol support**

ALB supports the HTTP, HTTPS, and QUIC protocols. For online applications such as ApsaraVideo Real-time Communication, interactive streaming, and games, ALB provides faster access and more secure, reliable transmission. ALB also supports the gRPC framework to enable efficient API communication among microservices.

**Advanced content-based routing**

ALB can identify specific service traffic based on conditions such as the path, HTTP header, query string, HTTP request method, cookie, and source IP address, and then forward the traffic to different backend servers. ALB also supports advanced operations such as redirection, rewrites, and custom HTTPS headers.

<a id="section-3"></a>

# 3.Scenarios

Application Load Balancer (ALB) provides powerful application-layer processing and advanced routing features. It focuses on the HTTP, HTTPS, and QUIC application-layer protocols.

Common scenarios for ALB include the following:

- **High elasticity at the application layer**: ALB operates at the application layer and provides a virtual IP address (VIP) service to handle a massive volume of requests. ALB scales your applications by distributing traffic. This process eliminates single points of failure and improves application availability.

- **Advanced protocol support**: ALB supports the HTTP, HTTPS, and QUIC protocols and can process traffic at a massive scale. For mobile Internet applications, such as ApsaraVideo Real-time Communication and interactive streams, ALB provides faster access and more secure, reliable transmission. ALB also supports the gRPC framework. This enables efficient API communication between microservices.

- **Advanced content-based routing**: ALB can detect specific service traffic based on conditions such as the path, HTTP header, query string, HTTP request method, cookie, and source IP address. ALB then forwards the traffic to different backend servers. ALB also supports advanced operations such as redirection, rewrites, and custom HTTPS headers.

<a id="section-4"></a>

# 4.Features

This topic describes the features of Application Load Balancer (ALB).

**Instances**

<table>
  <tr>
    <th colspan="2">Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td rowspan="3">Instance network type</td>
    <td>Private network</td>
    <td>Supports private ALB instances, which have only private IP addresses.</td>
  </tr>
  <tr>
    <td>Public network</td>
    <td>Supports public ALB instances, which have both public and private IP addresses.</td>
  </tr>
  <tr>
    <td>Switch between public and private network types</td>
    <td>Supports switching between IPv4/IPv6 public and private network types.</td>
  </tr>
  <tr>
    <td>IP mode</td>
    <td>Static IP</td>
    <td>Supports the static IP mode.</td>
  </tr>
  <tr>
    <td rowspan="2">Protocol version</td>
    <td>IPv4</td>
    <td>Supports IPv4 instances.</td>
  </tr>
  <tr>
    <td>Dual-stack</td>
    <td>Supports IPv4/IPv6 dual-stack instances.</td>
  </tr>
  <tr>
    <td rowspan="2">Instance name</td>
    <td>Specify an instance name</td>
    <td>Supports specifying an instance name.</td>
  </tr>
  <tr>
    <td>Modify an instance name</td>
    <td>Supports modifying an instance name.</td>
  </tr>
  <tr>
    <td rowspan="2">Tags</td>
    <td>Edit instance tags</td>
    <td>Supports adding, modifying, and deleting instance tags.</td>
  </tr>
  <tr>
    <td>Filter instances by tag</td>
    <td>Supports filtering instances by tag.</td>
  </tr>
  <tr>
    <td>Deletion protection</td>
    <td>Enable/Disable deletion protection</td>
    <td>Supports enabling and disabling deletion protection.</td>
  </tr>
  <tr>
    <td>Configuration read-only mode</td>
    <td>Enable/Disable configuration read-only mode</td>
    <td>Supports enabling and disabling the configuration read-only mode.</td>
  </tr>
</table>

**Listeners**

| Feature | Description |
| --- | --- |

ALB supports the HTTP protocol.

Supported protocols

Listener

ALB supports the HTTPS protocol.

protocol

Advanced application layer

ALB supports the QUIC protocol.

protocols

Configure a frontend port

You can configure a frontend port.

Set a listener name

You can set a listener name.

Modify a listener name

You can modify a listener name.

Select a server group

You can select a server group.

Replace a server group

You can replace a server group.

Common features

Set an idle timeout period

You can set an idle timeout period for connections.

Set a request timeout

You can set a request timeout period for connections.

period

You can enable data compression for specific file

Enable data compression

types.

Obtain the client source IP

Retrieves the client IP address from the X-Forwarded-

address

For header field.

Adds the SLB-ID header field to retrieve the ID of the SLB instance.

Additional HTTP header fields

Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance.

Adds the X-Forwarded-Port header field to retrieve

HTTP listener

the listener port of the instance.

Additional HTTP header

Adds the X-Forwarded-Client-srcport header field to

fields for advanced

retrieve the port of the client that accesses the SLB

forwarding

instance.

Enable HTTP/2

You can enable HTTP/2.

Adds the SLB-ID header field to retrieve the ID of the SLB instance.

Additional HTTP header fields

Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance.

Adds the X-Forwarded-Clientcert-subjectdn header field to retrieve the owner information of the client certificate.

Adds the X-Forwarded-Clientcert-issuerdn header field to retrieve the issuer information of the client certificate.

Adds the X-Forwarded-Clientcert-fingerprint header field to retrieve the fingerprint of the client certificate.

Additional HTTP header fields for advanced forwarding

Adds the X-Forwarded-Clientcert-clientverify header

HTTPS listener

field to retrieve the verification result of the client certificate.

Adds the X-Forwarded-Port header field to retrieve the listener port of the SLB instance.

Adds the X-Forwarded-Client-srcport header field to retrieve the port of the client that accesses the SLB instance.

You can enable QUIC upgrade. If you enable this

Enable QUIC upgrade

feature, you must select a created QUIC listener from

(Advanced)

the associated QUIC listener drop-down list.

You can configure server certificates.

Configure SSL certificates

You can configure CA certificates to enable mutual authentication.

Select a TLS security policy

You can select a TLS security policy.

Adds the SLB-ID header field to retrieve the ID of the SLB instance.

Additional HTTP header fields

Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance.

QUIC listener

Additional HTTP header

Adds the X-Forwarded-Port header field to retrieve

fields for advanced

the listener port of the instance.

forwarding

Configure SSL certificates

You can configure server certificates.

Listener status

Start and stop a listener

You can start and stop a listener.

Set a forwarding rule name

You can set a name for a forwarding rule.

You can configure forwarding conditions based on the domain name or path. Matching methods: Domain name: exact match, wildcard character, and case-insensitive regular expression. Path: exact match, wildcard character, case-

Configure request

insensitive regular expression, and case-sensitive

forwarding rules

regular expression.

You can configure the forwarding action to forward requests to one or more server groups. Session persistence between server groups is supported.

You can configure advanced forwarding conditions based on the HTTP header, query string, HTTP request method, cookie, or source IP address. Matching methods: **HTTP header, query string, and cookie**: exact match and wildcard character. **Source IP address**: CIDR block.

Forwarding

Configure advanced

rules

request forwarding rules

Supported forwarding actions include Redirect, Return Fixed Response, Rewrite, Insert Header, Remove Header, Rate Limit, Traffic Mirror, and Cross-Origin Resource Sharing (CORS). Details: Return Fixed Response: You can set the response status code, response body type, and response body. Redirect: You can set the protocol, domain name, port, path, query, and status code (301 to 308). Insert Header: You can set the header key and value. The value can be user-defined, a reference to a field in the request header, or system-defined. Rewrite: You can rewrite the domain name, path, and query. Rate Limit: You can set the total rate limit and the rate limit based on the client source IP address. Cross-Origin Resource Sharing (CORS): You can set the allowed origins, allowed methods, allowed request headers, allowed response headers, whether to allow credentials, and the browser cache time.

Forwarding conditions: request direction (optional), status code, and header.

Configure advanced response forwarding rules

Forwarding actions: Return Fixed Response, Insert Header, and Remove Header.

Edit a forwarding rule

You can edit forwarding rules.

Reorder forwarding rules

You can reorder forwarding rules.

Delete a forwarding rule

You can delete forwarding rules.

WebSocket

HTTP listeners support WebSocket by default.

WebSocket

HTTPS listeners support WebSocket Secure by

WebSocket Secure

default.

**Server groups**

**Feature**

**Description**

Server type

Supports adding ECS instances as backend servers.

Server group

IP type

Supports adding IP addresses as backend servers.

type

<table>
  <tr>
    <td>Server group name</td>
    <td>Set a server group name</td>
    <td>Supports setting a server group name.</td>
  </tr>
  <tr>
    <td rowspan="3">Backend protocol</td>
    <td>HTTP</td>
    <td>Supports HTTP as the backend protocol.</td>
  </tr>
  <tr>
    <td>HTTPS - Advanced security</td>
    <td>Supports HTTPS as the backend protocol.</td>
  </tr>
  <tr>
    <td>gRPC - Advanced application layer</td>
    <td>Supports gRPC as the backend protocol.</td>
  </tr>
  <tr>
    <td rowspan="4">Scheduling algorithm</td>
    <td>Weighted round-robin</td>
    <td>Distributes requests to servers based on their weights in a round-robin manner.</td>
  </tr>
  <tr>
    <td>Weighted least connections</td>
    <td>If weights are the same, backend servers with fewer connections have a higher probability of being selected.</td>
  </tr>
  <tr>
    <td rowspan="2">Consistent hashing</td>
    <td>Supports source IP hashing.</td>
  </tr>
  <tr>
    <td>Supports URL parameter hashing.</td>
  </tr>
  <tr>
    <td rowspan="2">IPv6 attachment</td>
    <td rowspan="2">Enable IPv6 attachment - Advanced IPv6</td>
    <td>Enable IPv6 attachment: The server group supports attaching IPv4 and IPv6 backend servers. The server group type can only be Server type.</td>
  </tr>
  <tr>
    <td>Do not enable IPv6 attachment: The server group supports attaching only IPv4 backend servers. The server group type can be Server type, IP type, or Function Compute type.</td>
  </tr>
  <tr>
    <td rowspan="3">Session persistence</td>
    <td rowspan="2">Enable session persistence</td>
    <td>Supports inserting a cookie to implement session persistence.</td>
  </tr>
  <tr>
    <td>Supports rewriting a cookie to implement session persistence.</td>
  </tr>
  <tr>
    <td>Configure a session persistence timeout period</td>
    <td>Supports configuring a session persistence timeout period.</td>
  </tr>
  <tr>
    <td>Persistent backend connection</td>
    <td>Enable persistent backend connection -Advanced application layer</td>
    <td>After you enable persistent backend connections, ALB maintains a number of persistent TCP connections to backend servers. When a new request arrives, ALB preferentially uses an idle persistent TCP connection to forward the request.</td>
  </tr>
  <tr>
    <td>Slow start</td>
    <td>Enable slow start -Advanced application layer</td>
    <td>After you enable slow start, ALB gradually increases the number of requests sent to a newly added backend server in the server group.</td>
  </tr>
  <tr>
    <td>Connection draining</td>
    <td>Enable connection draining - Advanced application layer</td>
    <td>Supports enabling connection draining.</td>
  </tr>
  <tr>
    <td rowspan="2">Tags</td>
    <td>Edit server group tags</td>
    <td>Supports editing server group tags.</td>
  </tr>
  <tr>
    <td>Filter server groups by tag</td>
    <td>Supports filtering server groups by tag.</td>
  </tr>
  <tr>
    <td rowspan="2">Health check</td>
    <td>Enable and disable health checks</td>
    <td>Supports enabling and disabling health checks.</td>
  </tr>
  <tr>
    <td>Select and load a health check configuration</td>
    <td>Supports creating health check configurations separately and attaching them to server groups.</td>
  </tr>
  <tr>
    <td rowspan="2">Backend server</td>
    <td>Add a backend server</td>
    <td>Based on the server group type, supports adding backend servers of the Server type or IP type.</td>
  </tr>
  <tr>
    <td>Remove a backend server</td>
    <td>Supports removing backend servers.</td>
  </tr>
  <tr>
    <td>Save configuration</td>
    <td>Save a server group configuration</td>
    <td>Supports saving a server group configuration for reuse.</td>
  </tr>
</table>

**Security management**

**Feature**

**Description**

Set a policy group name

Supports setting a policy group name.

Tag

Supports tags.

Supports whitelists.

Access control

Set an access control

Supports blacklists.

method

Supports adding, modifying, and deleting IP entries (CIDR

Edit IP entries

blocks).

**Feature**

**Description**

HTTP: Supports the HEAD and GET methods.

HTTPS: Supports the HEAD and GET methods.

Select a health check protocol

TCP: Checks whether the server port is active by sending SYN handshake messages.

Advanced application layer

gRPC: Sends POST or GET requests.

health check protocols

For HTTP and HTTPS health checks, the HEAD method is used by default.

Select a health check method

HTTP and HTTPS support GET requests.

gRPC supports the POST method by default.

Advanced application layer health check methods

For gRPC health checks, the GET method is also supported.

Advanced application layer

HTTP/1.1 is supported.

health check protocol versions

You can set a health check port. By default, the

Set a health check port

backend service port is used.

Health check

Set a health check path

You can set a health check path.

You can use the private IP address of the backend server. This is the default setting.

You can specify a domain name.

Set a health check domain name

For HTTP/HTTPS health checks, you can select http_2xx, http_3xx, http_4xx, and http_5xx. By default, http_2xx

Set health status return codes

and http_3xx are selected. For gRPC health checks, you can select values from 0 to

99. You can specify up to 20 ranges.

The amount of time to wait for a response to a health

Set a response timeout period

check probe.

Set a health check interval

You can set the interval between health checks.

You can set the Healthy

The number of consecutive successful health checks

Threshold.

required for a backend server to be declared healthy.

The number of consecutive failed health checks

Set an unhealthy threshold

required for a backend server to be declared unhealthy.

<table>
  <tr>
    <th colspan="2">Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td rowspan="4">Certificate management</td>
    <td rowspan="2">Server certificate</td>
    <td>Supports adding additional server certificates.</td>
  </tr>
  <tr>
    <td>Supports deleting additional server certificates.</td>
  </tr>
  <tr>
    <td rowspan="2">CA certificate</td>
    <td>Supports enabling or disabling mutual authentication.</td>
  </tr>
  <tr>
    <td>Supports replacing a CA certificate.</td>
  </tr>
</table>

**Feature**

**Description**

Supports the tls_cipher_policy_1_0 policy.

Supports the tls_cipher_policy_1_1 policy.

Supports the tls_cipher_policy_1_2 policy.

Select a default policy

Supports the tls_cipher_policy_1_2_strict policy.

Supports the tls_cipher_policy_1_2_strict_with_1_3 policy.

TLS security policy

You can select the minimum TLS version.

- TLS 1.0 and later

- TLS 1.1 and later

- TLS 1.2 and later

Custom policies (Advanced)

You can enable TLS 1.3.

You can select specific cipher suites.

**Monitoring**

**Feature**

**Description**

Number of active connections.

Number of idle connections.

Maximum number of concurrent connections.

Number of failed backend TLS handshakes per second.

Number of new connections per second.

Number of dropped connections per second.

Number of failed backend connections per second.

Number of failed frontend TLS handshakes per second.

Number of custom responses per second.

Number of redirections per second.

Number of requests per second (QPS).

Number of requests per second that do not have session persistence.

Backend response time.

Request latency.

Outbound bandwidth.

Monitoring

Instance monitoring

metrics

metrics

Inbound bandwidth.

Number of 2xx status codes per second.

Number of 3xx status codes per second.

Number of 4xx status codes per second.

An SLB instance can handle up to 500 new connections per second.

The SLB instance processes 502 requests per second.

Number of 503 status codes per second.

An SLB instance can process 504 connections per second.

Number of 5xx status codes per second.

Number of backend 2xx status codes per second.

Number of backend 3xx status codes per second.

Number of backend 4xx status codes per second.

Number of backend 5xx status codes per second.

Number of healthy backend servers.

Number of unhealthy backend servers.

View monitoring data

You can view monitoring data in the console.

in the console

View monitoring

View monitoring data

You can view monitoring data using API operations.

information

using API operations

View monitoring data

You can view monitoring data using an SDK.

using an SDK

All resources.

Set the resource scope

Application groups.

for an alert rule

Instances.

Select a monitoring

You can select a monitoring metric for an alert.

metric for an alert

Alert rules

You can select a listener protocol.

Select a dimension

You can select a listener port.

Critical: phone call, text message, email, and WebHook.

Set a threshold and an

Warning: text message, email, and WebHook.

alert level

Info: email and WebHook.
