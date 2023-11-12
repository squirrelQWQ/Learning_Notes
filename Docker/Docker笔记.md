### 基础知识

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



### 常用命令

##### 查看

```shell
查看所有本地镜像
docker images

查看正在运行的容器
docker ps

```

##### 运行

```shell
启用docker服务：
systemctl start docker	

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

















