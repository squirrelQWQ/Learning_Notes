### 基础知识

##### 宿主机

宿主机就是安装了docker的那台机器。

例子：我本地安装vm-Ware，并开了一个centos，centos上又安装了docker。此时运行容器时所谓的宿主机就是centos系统所在的虚拟机。

##### Docker Registry

其实就是仓库，就像maven仓库一样，别人把写好的镜像放在仓库开放给用户使用。最常用的就是[Docker Hub](https://hub.docker.com/search?q=&type=image)

同样的，和Maven一样既然有公开仓库那也能设一个本地的私有仓库



##### Dockerfile



##### 命令行窗口

比如下面这段命令行显示：

```bash
[root@localhost ~]# docker pull ubuntu:18.04
[root@localhost ~]# docker run -it --rm ubuntu:18.04 bash
root@f43b4e46d382:/# cat /ect/os-release
```

1. `root`: 这表示当前用户的用户名。在这里，用户是`root`，这是Linux系统中超级用户（拥有系统管理员权限）的默认用户名。
2. `f43b4e46d382`: 这是一个唯一的容器标识符（Container ID），用于标识正在运行的 Docker 容器。每个容器都有一个唯一的ID，以便可以轻松地识别和操作容器。
3. `:`: 冒号用于分隔用户名和容器ID。

因此，`root@f43b4e46d382:` 表示你正在以超级用户 `root` 的身份登录到一个名为 `f43b4e46d382` 的 Docker 容器中。这是一个标准的Docker容器命令行提示符，用于指示你在哪个用户下，以及你正在哪个容器中执行命令。



##### 镜像和容器

> 镜像和容器的关系类似于程序和进程之间的关系
>
> 镜像-->程序
>
> 容器-->进程

**镜像（Image）：**

- 镜像是一个包含了应用程序及其依赖关系的只读文件系统。
- 镜像是用于创建容器的模板。它包含了应用程序运行所需的所有信息，包括代码、运行时、库、环境变量和配置文件等。
- 镜像是静态的，不会改变。当你启动一个容器时，实际上是在镜像的基础上创建了一个可写的容器层，用于存储运行时状态。

**容器（Container）：**

> 使用一次进入容器的命令：docker exec -it <container_name_or_id> /bin/bash
> 就理解了为什么说docker是一个轻量化的虚拟机技术，每个容器就像是一个单独的虚拟机

- 容器是基于镜像运行的实体，它可以被启动、停止、删除和移动。
- 容器是镜像的一个实例，它包含了镜像以及在运行时所需的可写文件系统层。这个可写的文件系统层使得容器可以在运行时修改和存储数据。
- 容器是一个独立的运行环境，可以在不同的环境中进行部署，而不用担心环境差异。

**关系：**

- 一个镜像可以生成多个容器实例。多个容器可以基于同一个镜像运行，每个容器都是独立的、隔离的运行环境。
- 容器实际上是在镜像的基础上创建的一个可写层，这使得容器可以在运行时进行修改、存储数据等操作。
- 当容器被停止或删除时，容器内的可写层会被丢弃，但镜像本身是不受影响的。

简而言之，镜像是一个静态的模板，而容器是基于这个模板创建的一个运行实例。多个容器可以共享同一个镜像，但它们之间是相互隔离的。



### 常用命令

##### 查看

```shell
查看所有本地镜像(二者等价)
docker images
docker image ls	

查看正在运行的容器
docker ps
查看所有容器（包括停止的）
docker ps -a

查看容器统计信息（View Container Stats）:
docker stats <container_name_or_id>

```

##### 运行

```shell
==1==启用docker服务：
systemctl start docker	

==2==根据镜像启动容器
docker run -d --name <container_name> <image_name>:<tag>
	-d: 后台运行容器
	--name: 指定容器的名称
	
==3==进入容器内部
docker exec -it <container_name_or_id> /bin/bash

==4==启动exited的容器
docker start <container_id_or_name>


```

##### 终止





##### 删除

```shell
==1==删除镜像（<image_name_or_id> 表示要删除的镜像的名称或ID。）
docker rmi <image_name_or_id>

删除镜像强制（如果镜像有关联的容器则不能直接删除，可以强制删除）
docker rmi -f <image_name_or_id>

删除容器（<container_name_or_id> 表示要删除的容器的名称或ID）
docker rm <container_name_or_id>

```







### 容器

#### 生命周期

参考博客：https://www.linkedin.com/pulse/understanding-docker-container-lifecycle-depth-rohit-kumar-shaw/

![](Docker笔记.assets/docker生命周期.gif)docker容器的生命周期像极了程序五态：创建、就绪、运行、阻塞、终止

##### Created

容器已创建但尚未运行

##### Running

*docker run* 命令就是创建+运行两件事一起搞定

##### Exited

比如容器中的任务全都执行完了、遇到了异常状态、发生了错误都可能使容器进入此状态。

和Deleted状态不同，此状态的容器还可以restart

##### Paused

容器被暂停，此时容器对CPU的使用几乎为0，但对存储的占有不为0（只是占用变少了，但还是占着资源）

##### Deleted

不会有容器会标明是此状态，因为此状态的容器都已经被删除了（没了，找不到了根本谈不上标出状态）

删除容器并不会删除对应的镜像

##### Dead

可以理解为running和deleted之间的一种状态，容器已经没用了（不占用任何CPU和memory等资源）但一时也没被删除的状态。

















