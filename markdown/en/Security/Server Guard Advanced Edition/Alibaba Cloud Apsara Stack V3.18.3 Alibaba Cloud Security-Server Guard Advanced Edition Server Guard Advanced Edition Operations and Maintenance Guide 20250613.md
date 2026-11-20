Alibaba Cloud  
Apsara Stack  
Alibaba Cloud Security-Server  
Guard Advanced Edition  
Server Guard Advanced  
Edition Operations and  
Maintenance Guide  
Product Version: V3.18.3  
Document Version: 20250613

**Table of Contents**

- [1.Check the service status](#section-1)
    - [1.1. Log on to the Apsara Infrastructure Management console](#section-1-1)
    - [1.2. Check the agent status](#section-1-2)
    - [1.3. Check the status of Aegiserver](#section-1-3)
    - [1.4. Check the Server Guard Update Service status](#section-1-4)
    - [1.5. Check the Defender module status](#section-1-5)
    - [1.6. Restart Server Guard](#section-1-6)

<a id="section-1"></a>

# 1.Check the service status

<a id="section-1-1"></a>

## 1.1. Log on to the Apsara Infrastructure Management console

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

- The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator.

  The endpoint of the Apsara Uni-manager Operations Console is in the following format: *regi on-id*.ops.console.*intranet-domain-id*.

- A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.

2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the ENTER key.

   ![](assets/dd668306d2357f8f85843dbc54a02439.jpeg)

   > **Note**
   >
   > You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

   > **Note**
   >
   > - Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator.
   >
   > - If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account.

   If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted.

   To enhance security, your password must meet the following requirements:

   - The password contains uppercase and lowercase letters.

   - The password contains digits.

   - The password contains at least one of the following special characters: ! @ # $ %

   - The password is 10 to 20 characters in length.

4. Click **Log In**.

5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products > Platforms > Apsara Infrastructure Management Framework**.

<a id="section-1-2"></a>

## 1.2. Check the agent status

Check the Server Guard agent based on the information provided in this topic and and make sure that the agent is running as normal.

**Check the agent logs**

Agent logs are stored in the data directory of the directory in which the process file of the Server Guard agent is stored. Example: /usr/local/aegis/aegis_client/aegis_xx_xx/data.

The log files are named by date. Example: data.1-data.7

**Check the status of the agent**

Run the following command to check whether the agent is online:

```text
 ps -aux | grep AliYunDun 
```

**Check the network connectivity**

Run the following command to check whether the agent can communicate with Server Guard over TCP:

```text
 netstat -tunpe |grep AliYunDun 
```

**Check the UUID of the agent**

Open the data.x log file of the agent and check the string that follows  `Currentuid Ret` . The string is the UUID of the agent.

**Check the processes of the agent**

The  `AliYunDun`  and  `AliYunDunUpdate`  processes of the agent are running. If you enable automatic virus blocking, the  `AliHips`  process of the agent is also running.

If both the AliYunDun and AliYunDunUpdate processes are running as normal, the agent is working as expected.

> **Note**
>
> If the agent runs in a Windows operating system, the  `AliYunDun`  and
>
> `AliYunDunUpdate`  processes run as services named  `Alibaba Security Aegis Detect Service`  and  `Alibaba Security Aegis Detect Service` .

<a id="section-1-3"></a>

## 1.3. Check the status of Aegiserver

**Background information**

To check the running status of Aegiserver, follow the following steps:

**Procedure**

1. Run the  `ssh server IP address`  command to log on to the server of Aegiserver.

2. Run the following command to find the Aegiserver image ID:

   ```bash
    docker ps -a |grep aegiserver 
   ```

   The following message is displayed:

   ```text
   b9e59994df41 
   reg.docker.alibaba-
   inc.com/aqs/aegiserverlite@sha256:f9d292f54c58646b672a8533a0d78fba534d26d376a194034e884
   70d9aa0b3 "/bin/bash /startApp." 2 hours ago Up 2 hours 80/tcp, 7001/tcp, 8005/tcp, 8009/tcp yundun-aegis.Aegiserverlite__.aegiserverlite. 1484712802
   ```

3. Run the following command to go to the Docker container:

   ```bash
    docker exec -it [imageId] /bin/bash 
   ```

4. Run the following command to check whether the Java process is normal:

   ```text
    ps aux |grep aegiserver 
   ```

   The following message is displayed:

   ```text
   root 153 0.6 25.8 2983812 1084588 ? Sl 12:13 1:01 /opt/taobao/java/bin/java -Djava.util.logging.config.file=/home/admin/aegiserverlite/.default/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -server -Xms2g -Xmx2g-XX:PermSize=96m -XX:MaxPermSize=384m -Xmn1g -XX:+UseConcMarkSweepGC -
   XX:+UseCMSCompactAtFullCollection -XX:CMSMaxAbortablePrecleanTime=5000 -XX:+CMSClassUnloadingEnabled -XX:+UseCMSInitiatingOccupancyOnly -
   XX:CMSInitiatingOccupancyFraction=80 -XX:+HeapDumpOnOutOfMemoryError -
   XX:HeapDumpPath=/home/admin/logs/java.hprof -verbose:gc -
   Xloggc:/home/admin/logs/gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Djava.awt.headless=true -Dsun.net.client.defaultConnectTimeout=10000 -
   Dsun.net.client.defaultReadTimeout=30000 -XX:+DisableExplicitGC -Dfile.encoding=UTF-8-Ddruid.filters=mergeStat -Ddruid.useGloalDataSourceStat=true -
   Dproject.name=aegiserverlite -Dcatalina.vendor=alibaba -
   Djava.security.egd=file:/dev/./urandom -Dlog4j.defaultInitOverride=true -Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_EQUALS_IN_VALUE=true -
   Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_HTTP_SEPARATORS_IN_V0=true -Djava.endorsed.dirs=/opt/taobao/tomcat/endorsed -classpath 
   /opt/taobao/tomcat/bin/bootstrap.jar:/opt/taobao/tomcat/bin/tomcat-juli.jar -Dcatalina.logs=/home/admin/aegiserverlite/.default/logs -
   Dcatalina.base=/home/admin/aegiserverlite/.default -Dcatalina.home=/opt/taobao/tomcat 
   -Djava.io.tmpdir=/home/admin/aegiserverlite/.default/temp 
   org.apache.catalina.startup.Bootstrap -
   Djboss.server.home.dir=/home/admin/aegiserverlite/.default -
   Djboss.server.home.url=file:/home/admin/aegiserverlite/.default start
   ```

5. Run the following command to perform the health check:

   ```bash
    curl 127.0.0.1:7001/checkpreload.htm 
   ```

   If the response is "success", the service is normal.

6. View related logs.

   - **Protocol logs**: View logs about upstream and downstream protocol messages between the server and client in /home/admin/aegiserver/logs/AEGIS_MESSAGE.log.

   - **Operation logs**: View abnormal stack information during operation in /home/admin/aegiserver/logs/aegis-default.log.

   - **Offline logs**: View the logs about client disconnection caused by time-out in /home/admin/aegiserver/logs/AEGIS_OFFLINE_MESSAGE.log.

<a id="section-1-4"></a>

## 1.4. Check the Server Guard Update Service status

**Background information**

To check the status of Server Guard Update Service, follow the following steps:

**Procedure**

1. Run the  `ssh host IP address`  command to log on to the server of Aegiserver.

2. Run the following command to find the Aegiserver image ID:

   ```bash
    docker ps -a |grep aegiserver 
   ```

3. Run the following command to go to the Docker container:

   ```bash
    docker exec -it [imageId] /bin/bash 
   ```

4. Run the following command to check whether the Java process is normal:

   ```text
    ps aux |grep aegisupdate 
   ```

5. Run the following command to perform the health check:

   ```bash
    curl 127.0.0.1:7001/checkpreload.htm 
   ```

   If the response is "success", the service is normal.

<a id="section-1-5"></a>

## 1.5. Check the Defender module status

**Background information**

To check the status of the Defender module of Server Guard, follow these steps:

**Procedure**

1. Run the  `ssh server IP address`  command to log on to the server that hosts the Defender module of Server Guard.

2. Run the following command to find the image ID of the Defender module of Server Guard:

   ```bash
    docker ps -a |grep defender 
   ```

3. Run the following command to go to the Docker container:

   ```bash
    docker exec -it [imageId] /bin/bash 
   ```

4. Run the following command to check whether the Java process is normal:

   ```text
    ps aux |grep defender 
   ```

5. Run the following command to perform health check:

   ```bash
    curl 127.0.0.1:7001/checkpreload.htm 
   ```

   If the response is "success", the service is normal.

<a id="section-1-6"></a>

## 1.6. Restart Server Guard

**Background information**

To restart Server Guard when a fault occurs, follow these steps:

**Procedure**

1. Run the  `ssh server IP address`  command to log on to the server that hosts Server Guard.

2. Run the following command to find the image ID of Server Guard:

   ```bash
    docker ps -a |grep application name 
   ```

3. Run the following command to go to the Docker container:

   ```bash
    docker exec -it [imageId] /bin/bash 
   ```

4. Restart related services.

   - Restart the Server Guard client service.

     - For a server running a Windows OS, go to the service manager, locate Server Guard Detect Service, and restart this service.

     - For a server running a Linux OS, use either of the following methods to restart the Server Guard client service:

       - Run the  `service aegis restart`  command to restart the service.

       - Run the  `killall                                            AliYunDun`  command as the root user to stop the current process, and then restart the /usr/local/aegis/aegis_client/aegis_xx_xx/AliYunDun process.

   - Restart the Aegiserver service.

     <ol type="a">

     <li>

     Run the following command to view the Java process ID:

     ```text
       ps aux |grep
                                         aegiserver 
     ```

     </li>

     <li>

     Run the following command to stop the current process:

     ```text
      kill -9 process 
     ```

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Run the following command to restart the process:

     ```bash
      sudo -u admin
     ```

     </li>

     </ol>

```text
                                        /home/admin/aegiserever/bin/jbossctl
```

```text
                                restart 
```

<ol type="i" start="500">

<li>

Run the following command to check whether the process has been successfully restarted:

```bash
  curl
                                        127.0.0.1:7001/checkpreload.htm 
```

</li>

</ol>

- Restart Server Guard Update Service:

  <ol type="a">

  <li>

  Run the following command to view the Java process ID:

  ```text
    ps aux |grep
                                  aegisupdate 
  ```

  </li>

  <li>

  Run the following command to stop the current process:

  ```text
   kill -9 process 
  ```

  </li>

  </ol>

  <ol type="i" start="100">

  <li>

  Run the following command to restart the process:

  ```bash
   sudo -u admin
  ```

  </li>

  </ol>

```text
                                        /home/admin/aegisupdate/bin/jbossctl
```

```text
                                restart 
```

<ol type="i" start="500">

<li>

Run the following command to check whether the process has been successfully restarted:

```bash
  curl
                                        127.0.0.1:7001/checkpreload.htm 
```

</li>

</ol>

- Restart the Defender service of Server Guard.

  <ol type="a">

  <li>

  Run the following command to view the Java process ID:

  ```text
    ps aux |grep
                                          secure-service 
  ```

  </li>

  <li>

  Run the following command to stop the current process:

  ```text
   kill -9 process 
  ```

  </li>

  </ol>

  <ol type="i" start="100">

  <li>

  Run the following command to restart the process:

  ```bash
   sudo -u admin
  ```

  </li>

  </ol>

```text
                                        /home/admin/secure-service/bin/jbossctl
```

```text
                                restart 
```

<ol type="i" start="500">

<li>

Run the following command to check whether the process has been successfully restarted:

```bash
  curl
                                        127.0.0.1:7001/checkpreload.htm 
```

</li>

</ol>
