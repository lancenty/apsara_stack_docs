Alibaba Cloud  
Apsara Stack  
Bastionhost  
Bastionhost Product  
Introduction  
Product Version: v3.18.6-2607  
Document Version: 20260902

**Table of Contents**

- [1.What is Bastionhost?](#section-1)
- [2.Features](#section-2)
- [3.Benefits](#section-3)
- [4.Scenarios](#section-4)

<a id="section-1"></a>

# 1.What is Bastionhost?

Developed by Alibaba Cloud based on years of theoretical and practical experience in O&M security management, Bastionhost provides a platform for centralized security management and audit that controls risks in O&M operations. Bastionhost complies with the requirements of the Multi-Level Protection Scheme (MLPS) and other laws and regulations on O&M audit. Bastionhost adopts the B/S architecture and integrates features including authentication, account management, authorization, and log audit. It supports security monitoring and historical data queries based on multiple character terminal protocols, file transfer protocols, graphic terminal protocols, and remote application protocols.

**User permission management**

Bastionhost supports multiple user roles: super administrator, department administrator, O&M administrator, audit administrator, O&M engineer, auditor, and system administrator. Each user role has different permissions, which can meet compliance requirements for permission management.

**Centralized authorization**

Centralized authorization helps sort out authorization relationship between users and hosts. You can grant permissions on a host to a user, grant permissions on multiple hosts to a user, grant permissions on a host to multiple users, and grant permissions on multiple hosts to multiple users.

**Single sign-on (SSO)**

You can host the usernames and passwords of hosts on Bastionhost. An O&M engineer can click Log On to log in to the required host without the need to enter the username and password.

**Centralized audit**

Bastionhost records all operations and allows you to query the records. Audit logs can be played online, and operation logs can be automatically backed up.

**Automatic password change**

Network management personnel are required to manually update passwords for network devices on a regular basis. The automatic password change feature of Bastionhost can automatically rotate the passwords of assets on a regular basis.

**Command control**

Bastionhost provides command control policies in a centralized manner and allows you to configure command control policies based on different hosts and users. Command control policies support the following actions: command blocking, command blacklist, and command whitelist.

**Ticket**

When an O&M engineer requests permissions from an administrator to access a device, the O&M engineer can submit an O&M ticket and specify the IP address of the device, device account, O&M validity period, and remarks. Then, the administrator is notified of the O&M ticket by email.

After the administrator reviews the O&M ticket, the administrator notifies the O&M engineer by email. If the administrator approves the request, the O&M engineer can access the device. Otherwise, the O&M engineer cannot access the device.

**System self-review**

Bastionhost audits the operations that are performed by users and itself, and generates system analysis reports.

<a id="section-2"></a>

# 2.Features

**Feature**

**Feature**

**Description**

**category**

Management

Allows you to manage user data based on the department

by department

structure.

User

Allows you to create users or import users from templates.

management

Supports login to Bastionhost through the following authentication methods: Active Directory (AD), Lightweight Directory Access Protocol (LDAP), and Remote Authentication Dial-In User Service (RADIUS). Multiple AD domains are

User

supported. Automatic AD and LDAP user synchronization is

synchronization

supported.

Allows you to customize password policies, such as the

Password

password length, complexity, relevance, unique usernames,

settings

unique usernames in reverse order, and expiration alert rules.

Allows you to configure Bastionhost login methods, such as

Login methods

DingTalk and WeCom login by scanning QR codes.

User management

Automatically deactivates users who remain logged off for a

User login

long period of time. You can configure a threshold for

settings

deactivating such users.

Supports user security policies that define the user validity

User security

period, user login time, user login IP address range, and user

settings

login MAC address range.

Supports multiple user roles, such as super administrators,

User roles

system administrators, security administrators, security auditors, and regular users. You can also create custom roles.

Two-factor

Authenticates logins to your bastion host based on dynamic

authentication

verification codes sent through apps and text messages.

Authentication

- Supports different two-factor authentication modes based on

method

global or different users.

settings

- Supports multiple authentication methods for a single user at the same time.

Tree view

Supports host management in tree view mode and custom asset directory hierarchies to facilitate asset data management.

Supports common O&M protocols, such as SSH, Telnet, RDP,

O&M protocols

VNC, FTP, SFTP, Rlogin, and X11.

Allows you to extend O&M protocols by releasing applications,

O&M

such as Oracle, MSSQL, MySQL, VMware vSphere Client,

applications

browsers, and other client tools.

You can use single sign-on (SSO) to call a variety of local client tools:

- Characters: Xshell, SecureCRT, PuTTY, and MobaXterm.

- Graphics: RealVNC, TightVNC, and TigerVNC.

- File transfer: SecureFX, FlashFXP, FileZilla, WinSCP, Xftp, and MobaXterm.

Compatible client types

- Databases: SQL Server Management Studio (SSMS), sqlwb, DBeaver, MySQL Client, DbVisualizer, MySQL Workbench, MySQL Front, PL/SQL, SQL\*PLUS, db2cmd, Quest Central, pgAdmin III, PgSQL, KSQL, lsql, dlsql, DM manager, GBaseDataStudio, Toad, Toad for DB2, and Navicat. With the help of these tools, you do not need to use application release servers.

Asset management

Adaptive to multiple cloud environments, including Huawei

Multi-cloud

Cloud, Baidu Cloud, Amazon Web Services, Tencent Cloud,

asset discovery

Microsoft Azure, Ucloud, BlueKing, and Qingteng Sentry, and supports synchronization of cloud hosts to bastion hosts.

LAN asset

Scans local area networks (LANs) for IP addresses of hosts that

discovery

are not managed on Bastionhost.

Asset

Runs diagnostics on hosts managed on Bastionhost for issues

diagnostics

such as connectivity, zombie assets, and disabled assets.

Asset export

Encrypted exported assets in ZIP.

encryption

Supports protocols of DB2, Oracle, MySQL, SQL Server, PostgreSQL, KingbaseES, DM, GBase 8a, GBase 8s, HighGo, Redis, and GaussDB. After automatic login, Bastionhost can directly call the database client tool of the on-premises Windows system to perform database O&M, without the need to use jump servers. Supported database client tools include SSMS, sqlwb, DBeaver, MySQL Client, MySQL Workbench, MySQL Front,

Database

DbVisualizer, PL/SQL, SQL\*PLUS, Toad, Toad for DB2, db2cmd,

compatibility

Quest Central, pgAdmin III, PgSQL, KSQL, lsql, dlsql, DM manager, GBaseDataStudio, and Navicat.

Database management

Database

Supports database command control, which can block sessions

command

and commands, review actions, and allow actions.

control

Auto-fill for Internet Explorer, Google Chrome, Firefox, and other

Auto-fill for

browsers during application release: Automatically fill in the

web

account username and password for HTTP and HTTPS web

applications

devices.

Application release requirements

Supports URL blacklists and whitelists for HTTP and HTTPS

URL access

assets. Unauthorized users are not allowed to redirect to other

control

websites by manually entering URLs.

Supports review rules for O&M tickets, password tickets,

Ticket

Ticket

emergency O&M tickets, command review, O&M review, and

management

management

O&M tasks.

Supports automatic password change for Windows servers,

Automatic

Automatic

network devices, Linux servers, Unix servers, mainstream

password

password

databases, databases developed by Chinese vendors, and web

change

change

applications.

Supports authorization rules at different dimensions, such as

Authorization

user, user group, asset, asset account, and asset directory. You

rules

can also specify an effective time period and applicable IP addresses for the authorization rule.

- Supports host control policies based on dynamic policy matching. You can also specify an effective time period and applicable IP addresses for the policy.

Host command

- Supports four host command control actions, including allow,

control

close session, block request, and review.

- Supports parsing and regular expressions for matching host

Policy-based

commands against command sets.

control

- Supports database command control based on dynamic policy matching. You can also specify an effective time period and applicable IP addresses for the policy.

Database command

- Supports four database command control actions, including

control

allow, close session, block request, and review.

- Supports SQL parsing and regular expressions for matching database commands against command sets.

Supports the B/S architecture for Bastionhost O&M. You can use browsers such as Internet Explorer, Google Chrome, Firefox, and

O&M

Microsoft Edge to open Bastionhost web pages and directly call local O&M client tools, such as mstsc, VNC, Xshell, SecureCRT, PuTTY, WinSCP, FlashFXP, FileZilla, and SecureFX.

Support Bastionhost-dedicated O&M clients based on the C/S

Dedicated O&M

architecture for Windows and macOS operating systems. You

clients

can log in to Bastionhost by using a dedicated client to perform simple O&M operations and asset management.

Supports multiple H5 O&M protocols and methods: SSH, Telnet,

H5 O&M

Rlogin, RDP, VNC, FTP, SFTP, and X11. You do not need to use

protocols

on-premises O&M client tools.

In H5 O&M mode, you can use RDP or SSH to transfer files online

H5 file transfer

over a web page, without the need to use third-party client tools.

The H5 O&M mode supports online session collaboration. O&M

H5 session

engineers can invite Bastionhost users to operate and maintain

collaboration

the same session together. The number of invitees is unlimited, but a single invitation link can invite only one user.

- The session collaboration feature allows you to view collaboration engineers in real time on the O&M page. The

Session

initiator can assign control rights online and remove

collaboration

collaboration engineers in real time.

operations

- Session collaborators can proactively apply for control over the current session, and can manage the session after the session initiator grants the permission.

Session

During session audit, related O&M information is recorded for

collaboration

collaborative sessions, such as the invitee account, invitation

audit

reason, and operations.

To log in to Bastionhost from a client, use an on-premises client

Login from

tool such as Mstsc, Xshell, SecureCRT, PutTTY, WinSCP, and Xftp

client tools

to log in to Bastionhost and access graphics, characters, SFTP devices, and FTP devices.

You can log in to the SSH server in SSH-agent-forwarding mode

SSH-agent-

in scenarios where the same private key is used to log in to both

forwarding

Bastionhost and the SSH host.

O&M methods

You can log in to an SSH asset by using a password or a public

SSH login

key, and send environment variables such as O&M user information and O&M source IP addresses to the asset.

Supports login to multiple character devices at the same time:

Automatic login

Bastionhost can automatically generate SecurCRT or Xshell

to multiple

batch login files, which enable automatic login to multiple

character hosts

devices from a tool at the same time.

Supports login to multiple host assets that use different protocols at the same time. You can also select a login method

Batch login

for different assets. For example, you can perform H5 O&M on all assets, or perform H5 O&M on Asset A but local O&M on Asset B.

Provides an interactive dialog box during batch logins. Then,

Batch login

you can select the default login mode or a custom login mode

mode

(uses the same account and O&M protocol).

Recent O&M

Records the most recent hosts for quick O&M.

Automatic login

In an AD or LDAP environment, AD or LDAP users of Bastion can

to hosts for

use their passwords to directly log in to hosts.

domain users

Limits on the

Allows you to limit the number of user sessions. You can specify

number of

the maximum number of sessions that a user can maintain at a

sessions

time.

Session information

Displays the information about connected sessions of a host.

display

- Displays available O&M hosts in a tree view. You can also classify hosts into different groups and adjust the order of groups.

Tree view

- Provides the tree view configured by the administrator so that you do not need to configure a view.

Allows you to add frequently used O&M hosts to Favorites so

O&M favorites

that you can quickly find them.

Supports the automatic orchestration feature, which allows you to orchestrate actions to perform scheduled or periodic

Task

automated O&M on assets. Supported actions include file

orchestration

upload, command execution, and file download. The actions are executed in the specified sequence. You can use this feature to perform common O&M tasks, such as upgrades and inspections.

Automated tasks

During automated orchestration, you can enable or disable a

Task

single action, enable or disable manual confirmation after the

orchestration

execution of a single action, and specify whether to push the

management

result by email.

- Supports online monitoring and real-time blocking on O&M sessions.

- Supports video playback at a certain speed from 0.5 to 64.

- Record the following information about O&M sessions: start

O&M audit log

time, end time, source users, source IP addresses, accessed servers, protocol or application types, commands, and operations such as file uploading, downloading, deletion, and modification.

- Supports real-time monitoring on O&M sessions.

Real-time monitoring

- Supports real-time monitoring on file transfer sessions.

Supports recording, searching, and positioning of RDP screen

RDP transcript

texts, title windows, keyboard inputs.

Supports auditing on SQL statements used for O&M on

SQL records

mainstream databases, such as DB2, Oracle, MySQL, SQL Server, Postgres, GBase 8a, KingbaseES, and Dameng.

Allows O&M users to query their O&M audit sessions. This

Self-review on

reduces the workload of audit administrators and helps O&M

O&M sessions

users improve O&M efficiency.

Audit management

SSH and SFTP file transfer

Stores the sz and rz commands of SSH (ZMODEM transmission)

audit

and original files transferred over SFTP or FTP.

RDP file

Stores the original files transferred by using the RDP pasteboard

transfer audit

or disk mapping.

Retains uploaded and downloaded files, limits the size of transferred and stored files, and generates SHA1 values for transferred files.

File retention

Automatically archives audit data over SFTP or FTP. You can also query whether the data is archived on the page. During the archiving process, you can specify the time for automatic

Log archiving

archiving, the speed limit for transmitting archived files, and automatic data deletion after archiving. The archived data can be viewed offline by using a dedicated player.

Provides built-in analysis reports from different dimensions, such as the number of O&M operations, duration, O&M duration, active O&M duration, session size, number of character commands, number of transferred files, number of source IP

Built-in reports

addresses, and O&M time distribution. You can also view the global values, average values, maximum values, minimum values, data of a single O&M operation, and data of a single session.

Provides various built-in report templates. You can click on a

Report

O&M reports

desired line chart for data drilling and analysis, and export data

templates

to PDF, DOC, and HTML files.

Automatically analyzes statistics and generates custom reports

Custom reports

based on the conditions that you specify.

Allows you to subscribe to reports. You can customize the report

Report

content and recipients of the subscription and the time interval

subscription

at which you want the system to send reports.

Limits on the

Allows you to limit the idle time period for all O&M sessions.

O&M idle time

Protocols and

Supports custom ports for the proxy protocols of Bastionhost.

ports

Limits on

Allows you to allow or block logins from specific IP addresses to

source IP

Bastionhost. You can configure an IP blacklist or whitelist.

addresses

System

Automatically backs up system configuration files to FTP or SFTP

configuration

servers. You can specify the time interval for backup.

backup

Supports self-auditing, including but not limited to the following

System self-

check items: system status, login logs, user logs, asset logs,

review

policy operation logs, audit logs, configuration logs,

System

maintenance logs, and O&M logs.

configuration requirements

System log

Supports system log reports, including but not limited to the

reports

following statistical items: login logs, configuration logs, O&M access logs, and ticket reports. You can also export the reports.

Supports the following system languages: simplified Chinese,

Custom

English, and traditional Chinese. You can specify whether to

settings

allow users to switch languages and customize the logo of the Web management console.

- Sends Bastionhost alerts and the Bastionhost status.

Alerting

- Sends alert logs through emails, Syslog, and DingTalk. You can also specify log priorities.

Provides troubleshooting tools such as ping, TCP port probing,

Troubleshootin

UDP port probing, route tracing, and packet capturing by using

g

the tcpdump command.

- Supports NFS and CIFS storage.

Storage management

- Supports video storage in Object Storage Service (OSS).

Deployment

Deployment on

Supports HA deployment and active-active deployment. Audit

requirements

dual servers

data can be automatically synchronized between servers.

<a id="section-3"></a>

# 3.Benefits

**Enhances transparency in the operational process**

Multiple individuals perform O&M tasks on hosts each day. An administrator has limited visibility into the operations performed by O&M engineers on the assets, which may include potential violations or errors. Monitoring the operations of external personnel in real-time is also challenging. This lack of oversight makes it difficult to identify the responsible party when an O&M security incident occurs.

Bastionhost provides comprehensive O&M audit and supports real-time monitoring during O&M. After an O&M session ends, you can replay videos to audit all O&M operations.

**Reduces costs of asset account management**

A larger number of hosts indicates a larger number of host accounts. A single host may have multiple accounts. A host account may be shared among multiple individuals. An individual may have permissions on multiple host accounts. Different individuals may simultaneously have permissions on multiple host accounts. As a result, administrators cannot track the relationship between accounts and individuals, and concerns regarding potential data leaks arise due to the presence of temporary accounts.

Bastionhost allows you to manage assets and asset accounts. You can configure authorization rules to manage asset O&M permissions and reduce management costs. You can also configure multiple access control policies to prevent unauthorized access.

**Improves O&M efficiency**

As the number of host accounts continues to increase, the management and regular change of passwords have become challenging tasks for administrators. Ensuring password complexity and periodic changes are essential. However, manual changes can significantly increase workload. Various host types require different login methods. For Linux and UNIX operating systems, character client tools are required, while the Windows operating system requires remote desktop connection tools. Web systems can be accessed by using browsers, and databases require database client tools in most cases.

Bastionhost provides multiple O&M methods. You can directly access assets by using web pages or by using Bastionhost Assistant for access from on-premises clients. Bastionhost helps O&M engineers perform operations on multiple assets. This greatly improves O&M efficiency.

**Controls high-risk O&M operations**

O&M engineers may perform unintentional operations that cause data loss or service failures. Attackers can also remotely access hosts and engage in data theft or tampering. To ensure precise control, administrators must implement refined policies across multiple hosts to control intentional and unintentional high-risk operations.

Bastionhost allows you to configure command control policies to block sensitive operations, such as high-risk command execution, that may occur in real time during O&M. You can adjust the policies based on your business requirements to control high-risk operations in an efficient manner.

**Meets compliance requirements**

Currently, numerous standards, laws, and regulations, in and outside China, mandate organizations to establish audit systems for security management. The systems must ensure that audit information is secure, comprehensive, accessible, and unique.

- Multi-Level Protection Scheme (MLPS) requires user identification, permission isolation, data audit, log records, and audit reports.

- The ISO 27001 standard mandates organizations to record user access, incidents, and information security events to investigate and collect evidence for security incidents.

- The Sarbanes-Oxley (SOX) Act mandates organizations to establish and enforce suitable policies to ensure the reliability and trustworthiness of financial statement data.

- Enterprise internal control standards mandate enterprises to adhere to the requirements. This helps enhance and standardize internal control practices and improve risk prevention capabilities.

<a id="section-4"></a>

# 4.Scenarios

**Centralized management of assets to resolve scattered asset issues**

Bastionhost can manage multiple types of assets, such as hosts, databases, and applications. Bastionhost can automatically discover assets, host asset accounts, and manage different asset access permissions to prevent unauthorized access.

**Various O&M methods for complex scenarios such as automated O&M**

Bastionhost adapts to the O&M habits of different O&M engineers. Bastionhost is compatible with various client tools, including Xshell, SecureCRT, MobaXTerm, Microsoft Terminal Services Client (MSTSC), VNC Viewer, Putty, winscp, flashFXP, SecureFX, and OpenSSH. Bastionhost also supports the following O&M methods:

- Web page-based O&M: suitable for O&M engineers who prefer to use web pages to log in to hosts.

- Client-based O&M: suitable for O&M engineers who prefer to use local client tools to access Bastionhost and then connect to the required hosts.

Bastionhost supports batch O&M tasks and can simultaneously execute scripts and commands on multiple hosts. This improves O&M efficiency.

**Comprehensive O&M management and audit to meet internal audit and compliance requirements**

Bastionhost supports features, such as user identity authentication, access permission management, and O&M operation audit, to help enterprises build internal audit processes and comply with classified protection requirements.
