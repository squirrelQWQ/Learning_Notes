一个比较系统的python教程（基本上就是缩减+汉化的python官方文档）：http://www.ityouknow.com/python.html

## 说明

学python库无非就是一下几点：

- 这个库主要功能是干嘛的？
- 这个库提供了哪些变量和函数？
- 这个库的变量和函数具体使用方法
- 有没有使用的注意事项？

Python模块是一个Python文件，以.py结尾，Python包就是包含多个模块的文件夹（包含\_\_init\_\_.py文件）

在pycharm中可以 按ctrl+鼠标点击模块名进入模块.py文件 



## python标准库

标准库就是安装python所带的库，就像c语言安装mingw自带stdio.h一样



### os库

> 本模块提供了一种使用与操作系统相关的功能的便捷式途径

<font color=#b407e4>**说明：以下代码中参数不一定是函数的全部参数，只写出部分必要的参数，想看详细参数自查官方文档：https://docs.python.org/zh-cn/3/library/os.html**</font>

#### 系统相关

> 等什么时候用到了再写

#### 文件和目录相关

<font color=#b407e4>**说明：一般来说下面所用到的路径参数都是字符串，不过有些也支持：文件描述符、类路径对象、bytes类型**</font>

##### 常用函数列表

```python
# 扫描目录
os.walk(top)			#遍历以top为根目录的所有条目
os.listdir(path='.')	#返回path中所有条目组成的列表(.和..两个目录除外)

# 创建和删除
os.mkdir(name)			#创建目录path
os.makedirs(name)		#递归创建目录
os.remove(path)			#仅用于删除文件
os.rmdir(path)			#仅用于删除目录
os.removedirs(name)		#递归删除目录
os.rename(src,dst)		#文件或目录重命名

# 路径类型判断
os.path.exists(path)	#判断dir是否存在
os.path.isabs(path)		#判断dir是否为绝对路径
os.path.isfile(path)	#判断是否为文件或者指向文件的符号链接（快捷方式）
os.path.isdir(path)		#判断是否为目录或者指向目录的符号链接

# 其它工具
os.getcwd()					#获取当前路径
os.path.join(path,*paths)	#拼接参数为一个地址（使用该方式能够跨平台，不用考虑路径分隔符）
os.path.split(path)			#将路径 path 拆分为一对，即 (head, tail)
```

##### os.listdir(path=’.‘)

- 返回一个列表，里面记录path目录下的所有条目名称（包括目录和文件），不扫描子目录中内容
- path如果是文件，则会报错
- 运行示例：
  - ![](python模块笔记.assets/listdir执行.png)
  - ![](python模块笔记.assets/listdir执行结果.png)
  - 可以看到结果中既有文件夹名也有文件名，且都用字符串形式表示



##### os.path.split(path)

- 将路径 path 拆分为一对，即 (head, tail)，其中，tail 是路径的最后一部分，而 head 里是除最后部分外的所有内容。
  - 如果 path 以斜杠结尾，则 tail 将为空。
  - 如果 path 中没有斜杠，head 将为空。
  - 如果 path 为空，则 head 和 tail 均为空。
- tail 部分不会包含斜杠，head 末尾的斜杠会被去掉，除非它是根目录（即它仅包含一个或多个斜杠）。
- 在所有情况下，join(head, tail) 指向的位置都与 path 相同（但字符串可能不同）。



#### 进程相关

>等什么时候用到了再补充



### sys库

> 该模块提供了一些变量和函数。这些变量可能被解释器使用，也可能由解释器提供。这些函数会影响解释器。说人话就是这个库提供与解释器的交互



### re库

> 本模块提供了与 Perl 语言类似的正则表达式匹配操作。（主要针对字符串而非字节串）

使用re库进行正则表达式匹配的一般流程是：

1. 书写正则表达式模板
2. 使用re.compile() 将正则表达式模式编译成一个正则表达式对象
3. 使用正则表达式对象的方法来进行搜索、匹配等操作

这么做的好处是可以重复使用该正则表达式模板，嫌麻烦也可以不生成正则表达式对象



#### 语法

> 就是如何用字符来构造一个正则表达式





#### 常量

> re库定义好了一些常量（标志），用做方法的参数，从而控制如何进行匹配（比如：是否要忽略模式串的大小写？）

| 常量简写 | 常量全称      | 常量作用           |
| -------- | ------------- | ------------------ |
| re.I     | re.IGNORECASE | 忽略大小写进行匹配 |
| re.M     | re.MULTILINE  |                    |
| re.S     | re.DOTALL     |                    |
| re.L     | re.LOCALE     |                    |
| re.A     | re.ASCII      |                    |
| re.X     | re.VERBOSE    |                    |



#### 函数

> 罗列了正则表达式对象的常用方法

```python
re.compile(pattern, flags=0)		
									#依据正则表达式和标志（即：re库中定义的常量）生成正则表达式对象
re.search(pattern, string, flags=0)	
									#在字符串中搜索匹配正则表达式的第一个位置并返回MatchObject对象。
    								#如果没有匹配项，则返回None
re.match(pattern, string, flags=0)	
									#尝试从字符串开头匹配正则表达式，并返回MatchObject对象。
    								#如果没有匹配项，则返回None。
re.split(pattern, string, maxsplit=0, flags=0)
									#根据正则表达式对字符串进行分割，并返回分割后的子字符串列表。
    								#maxsplit参数控制最大分割次数。
re.fullmatch(pattern, string, flags=0)
									#尝试从字符串开头到结尾完全匹配正则表达式，并返回MatchObject对象。
    								#如果没有匹配项，则返回None。
re.findall(pattern, string, flags=0)
									#查找字符串中所有与正则表达式匹配的非重叠子串，并以列表形式返回。
re.sub(pattern, repl, string, count=0, flags=0)
									#使用repl替换字符串中与正则表达式匹配的部分，返回替换后的字符串。
    								#count参数控制替换次数，0表示全部替换。
re.finditer(pattern, string, flags=0)
									#查找字符串中所有与正则表达式匹配的非重叠子串，并以迭代器形式返回MatchObject对象。
re.escape(pattern)
									#转义正则表达式中的特殊字符，返回转义后的字符串。
```



#### 匹配对象

> 正则对象的方法很多都会返回一个匹配对象作为结果







#### 例子



## python非标准库



### pandas



### numpy



### tensorflow





















