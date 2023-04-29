一个比较系统的python教程（基本上就是缩减+汉化的python官方文档）：http://www.ityouknow.com/python.html

## 说明

学python库无非就是一下几点：

- 这个库主要功能是干嘛的？
- 这个库提供了哪些变量和函数？
- 这个库的变量和函数具体使用方法
- 有没有使用的注意事项？



## python标准库

标准库就是安装python所带的库，就像c语言安装mingw自带stdio.h一样







### os库

> 本模块提供了一种使用与操作系统相关的功能的便捷式途径

#### 系统相关变量和操作

> 等什么时候用到了再写

#### 文件和目录相关操作

##### 常用函数列表

```python
os.walk(top)			#遍历以top为根目录的所有条目
os.listdir(path='.')	#返回path中所有条目组成的列表(.和..两个目录除外)
os.mkdir(path)			#创建目录path
os.makedirs(name)		#递归创建目录
os.remove()				#仅用于删除文件
os.rmdir()				#仅用于删除目录
os.removedirs(name)		#递归删除目录
os.rename(src,dst)		#文件或目录重命名
os.getcwd()				#获取当前路径
os.path.join()			#拼接参数为一个地址（使用该方式能够跨平台，不用考虑路径分隔符）
os.path.split(path)		#将路径 path 拆分为一对，即 (head, tail)
os.path.exists(dir)		#判断dir是否存在
os.path.isabs(dir)		#判断dir是否为绝对路径
os.path.isfile()		#判断是否为文件或者指向文件的符号链接（快捷方式）
os.path.isdir()			#判断是否为目录或者指向目录的符号链接

```



##### os.path.split(path)

- 将路径 path 拆分为一对，即 (head, tail)，其中，tail 是路径的最后一部分，而 head 里是除最后部分外的所有内容。
  - 如果 path 以斜杠结尾，则 tail 将为空。
  - 如果 path 中没有斜杠，head 将为空。
  - 如果 path 为空，则 head 和 tail 均为空。
- tail 部分不会包含斜杠，head 末尾的斜杠会被去掉，除非它是根目录（即它仅包含一个或多个斜杠）。
- 在所有情况下，join(head, tail) 指向的位置都与 path 相同（但字符串可能不同）。



#### 进程相关操作

>等什么时候用到了再补充



### sys库

> 该模块提供了一些变量和函数。这些变量可能被解释器使用，也可能由解释器提供。这些函数会影响解释器。说人话就是这个库提供与解释器的交互



### re库

> 本模块提供了与 Perl 语言类似的正则表达式匹配操作。