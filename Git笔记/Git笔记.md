git官方有详细的教程（[Git Book](https://git-scm.com/book/zh/v2)），遇到问题或者不懂的地方还是看人家官方文档比较靠谱

廖雪峰的[Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)也十分的通俗易懂，值得一看

B站黑马Git笔记：https://blog.csdn.net/qq_58168493/article/details/122592304

### GitHub

> 一个在线软件源代码托管服务平台，使用Git作为唯一的版本控制软件

#### 基本概念

**Repository** 仓库：一个仓库等于一个项目

**Star** 收藏 ：

**Fork** 复制克隆项目 ：在原仓库的基础上新建一个分支（相当于对仓库进行备份）

- 快照

  - ```
    存储网络行业协会（SNIA）对快照的定义是：对指定数据集合的一个完全可用拷贝，该拷贝包含源数据在拷贝时间点的静态影像。　　
    快照可以是数据再现的一个副本或者复制。对于文件系统来说，文件系统快照是文件系统的一个即时拷贝，它包含了文件系统在快照生成时刻所有的信息，本身也是一个完整可用的副本。
    ```

**Pull Request** ：你fork了别人的仓库，同时做了修改想要把这个修改发给原仓库，这个请求就是pull request

**Watch** ：相当于关注项目，当对方项目有修改能收到通知

**Issue** ：就是一个讨论，可以用于通知项目维护者你发现的问题或者Bug（相当于一个评论区）



### Git基础

> 一个开源的分布式版本控制系统（svn是集中式版本控制系统）

<font color="red">说明：以下展示的所有代码中 \<xxx\>  表示参数为 xxx</font>

#### 基本概念

Git的基本路子就是每次修改都在本地新建一个文件快照，所以所有的操作都在本地完成

##### Bash、CMD、GUI

**Git Bash**：就是在windows环境下模拟linux环境的命令行窗口，在这里可以使用大部分linux的命令（**首选用此方法操作Git**）

**Git CMD**：就是windows的命令行窗口，在这里可以使用windows指令

- Bash 是一种 Unix shell 和命令语言，是 Linux (Ubuntu 等)和 OS X 上的默认 shell。用外行的术语来说，运行在任何 Linux 设备终端上的 git 称为 git bash。

**Git GUI**：就是一个图形化操作界面，由于Git就是在linux环境中写出来的，所以GUI并不是主流的操作方式，它只是照顾一下不习惯用黑框框的人，不过缺点就是他只实现了Git部分的命令



##### 文件状态转换

关于文件状态转换廖雪峰讲的通俗且易懂：https://www.liaoxuefeng.com/wiki/896043488029600/897271968352576

```
git commit <-m "XXX">
```

这个命令会一次性将暂存区（Staged）中的所有文件都提交到仓库中

其中 <-m "XXX"> 虽然是可选的选项，但是默认情况下都要写上，毕竟使用Git是多人之间合作，你的每次提交还是要写清楚你所做的操作

 

![](Git笔记.assets/git文件状态.png)



git status示例：

![](Git笔记.assets/git文件状态-1682255809454.png)

文件分两种：已追踪和未追踪

**Untracked**：文件未跟踪，就是新建的文件但是没有通知git

- ```
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
  ```
  
- 如上图中的 newFile.txt



**Unmodified**：就是存放在仓库中未修改的文件

- 就是上图git status没显示的文件

**Modified**：跟踪文件已修改但未暂存，文件任在工作区

- ```console
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)
  ```

- 如上图中的 Git笔记/Git笔记.md

**Staged**：跟踪文件已暂存

- ```console
  Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
  ```

- 如上图的  Git笔记/Git笔记.md     MySQL笔记/MySQL散记.md

commit命令提交的是你最后一次运行 `git add` 命令时的那个版本，而不是你运行 `git commit` 时，在工作目录中的当前版本。 所以，运行了 `git add` 之后又作了修订的文件，需要重新运行 `git add` 把最新版本重新暂存起来：



##### Head

HEAD是一个指针，指向当前版本

HEAD^指向当前版本的上一次commit版本

HEAD^100指向当前版本的前100次commit版本



##### 文件类型

Git可以详细的记录下仓库总文件发生的变化

- 对于文本文件，由于是有结构文件，git可以详细的记录下文件的变化
- 对于二进制文件，由于文件本身没有结构，故git仅能记录下文件大小发生的变化



##### 四个区域

图文简述了Git四个区域之间的转换：https://www.cnblogs.com/qdhxhz/p/9757390.html

这副图讲的很明白

![](Git笔记.assets/Git四个区-1681971847306.PNG)

本地三个区域

![](Git笔记.assets/Git本地三个区-1681909130014.png)

- 工作区：就是执行了 git init 的那个文件夹
- 暂存区：是 .git 目录下的 index 文件
- 版本库（本地仓库）：就是 .git 目录



​	所有文件要想提交到本地仓库中，都要先 add 到暂存区，而 git commit 命令是一次性将暂存区所有文件都提交到本地仓库。一次commit就代表本地仓库进行了一次版本替换，可以使用 git reset 命令更改仓库的版本，当然具体改到那个版本需要知道commit ID号。



#### 常用命令

##### 初始配置

Git是分布式的，每个用户之间都是独立的，所以需要自报家门（写明配置信息），只需执行一次即可

```
自报家门：
$ git config --global user.name "squirrel"
$ git config --global user.email "squirrelQWQ@outlook.com"
```

config 配置有system级别 、global（用户级别） 和local（当前仓库）三个 

设置先从system ==> global ==> local  底层配置会覆盖顶层配置 分别使用--system/global/local 可以定位到配置文件

```
查看配置：
$ git config --system --list
$ git config --global --list
$ git config --local --list
```

![](Git笔记.assets/查看config配置.png)



```console
初始化仓库：
$ git init
其实就是在项目所在目录下创建了一个 .git 文件，该文件包含了所有git操作所需的信息
要删除该本地仓库可以直接删除 .git 文件即可
```



##### 添加与查看

```
git add <file/dir>			\\ 注意，可反复多次使用，添加多个文件；
git add .				\\ 一次加入当前文件夹所有文件
git commit -m <message>	\\ 将文件提交至仓库，并使用 -m 选项输入描述信息
git status				\\ 查看仓库目前状态
git diff <file>			\\ 详细查看仓库的变化
```



**git commit**：如果使用commit命令没有添加提示信息会导致此次commit操作失败

- 比如不使用-m选项会直接进入Git默认编辑器，强制要求你写上信息
  - ![](Git笔记.assets/git commit 无-m选项.png)
  - 若执迷不悟还是不写信息就退出vim会导致本次commit失败
  - ![](Git笔记.assets/git commit 无-m选项02.png)



##### 版本选择

使用场景：每次提交后都表示本地仓库生成了一个新的版本，觉得当前版本不好想退回到以前的版本

```
版本查看
git log						\\ 查看仓库的历史版本（主要是各个commit的id和信息）
git log --pretty=oneline	\\ 只显示简略log信息
git log --pretty=oneline --abbrev-commit		\\只显示commit id的前几位
							\\ 次命令很长且经常使用所以可以为该命令取别名
git reflog					\\ 查看历史的所有commit操作

修改版本
git reset --hard <commit id>	
	\\ 其中commit id 可以在git log命令中查看也可以用 git reflog 查看历史命令
	\\ 同时commit id可以只输入前几位，git会自动查找给你补全
```



##### 撤销操作

使用场景：在文件提交前（文件可能在暂存区或工作区）发现操作有误想撤销操作

```
git checkout -- readme.txt
```

意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

- 一种是`readme.txt`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

- 一种是`readme.txt`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。



场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。



##### 删除文件

```
rm test.txt
```

这么直接删除文件会使得git不知道此文件删除了，使用git status 会有提示

```
$ git rm test.txt			\\同时删除工作区和暂存区的 test.txt文件
$ git rm -f test.txt 		\\强行删除工作区和暂存区已经修改过的test.txt文件
$ git rm --cached <file>	\\直接删除暂存区文件 file ，对工作区无影响
```



让git忽略某些文件 .gitignore 文件

详细介绍此文件：https://zhuanlan.zhihu.com/p/52885189



#### Git分支

常用命令

```
git branch <分支名>		\\ 新建分支
git branch				  \\ 查看分支，前面有*的就是当前分支

git 可以有多个分支但操作只能针对某一个分支，所以需要指定当前是哪个分支
git checkout <分支名>		\\ 切换分支
git checkout -b <分支名>	\\ 切换分支，若不存在则创建分支

合并分支
git merge <要合并的分支名>	\\ 合并分支，把参数里面的分支合并到当前分支中
```



**分支合并冲突**



#### 远程仓库

远程仓库就是一些代码托管平台，比如：github、码云、gitlab等



##### SSH认证

1. 首先在github上新建仓库

2. 再配置密钥信息进行身份认证（具体可参见菜鸟教程：https://www.runoob.com/git/git-remote-repo.html）

   1. ```
      ssh-keygen -t rsa -C "squirrelQWQ@outlook.com"		\\先在本地创建一个ssh密钥
      ```

   2. 在github账户设置中添加该SSH密钥![](Git笔记.assets/github添加SSH01.png)

   3. ![](Git笔记.assets/github添加SSH02-1682178731323.png)



##### 远程仓库常用命令

```
ssh-keygen -t rsa -C "squirrelQWQ@outlook.com"	  \\先在本地创建一个ssh密钥

$ git remote rm origin							  \\删除远程仓库origin	
$ git remote									  \\查看本地仓库关联的远程仓库（只显示仓库名称）
$ git remote -v									  \\查看本地仓库关联的远程仓库（显示仓库fetch和push链接）
$ git remote add origin git@github.com:squirrelQWQ/Learning_Notes.git	
												  \\添加远程仓库，并起名为origin

$ git pull <远程主机名> <远程分支名>:<本地分支名>		\\从远程仓库获取代码并合并本地的版本
$ git pull origin master:master
$ git pull origin master						  \\将远程仓库origin获取master分支代码并和当前分支进行合并

$ git push <远程主机名> <本地分支名>:<远程分支名>		\\将本地分支上传到远程分支并合并
$ git push origin master						  \\将本地仓库提交到origin的master上（本地分支名与远程分支名相同，则可以省略冒号：）


```

































