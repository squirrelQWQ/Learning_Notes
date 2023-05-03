菜鸟教程yyds：https://www.runoob.com/python3/python3-tutorial.html

## python3基础

python的一大特点就是简单，很多东西不再那么细分，比如整数就只用int，不像c语言细分为short、int、long、longlong

### 基本类型

#### 预备知识

##### 变量

python变量是没有类型的，也就是说在定义变量时不用像c、java那样指明类型，编译器会自动辨认出变量的类型。

比如可以像下面这样操作

```python
str = "hello"
print(f"str内容为：{str}")
print(f"str类型为：{type(str)}")
str = 123
print(f"str内容为：{str}")
print(f"str类型为：{type(str)}")

执行结果如下：
'''
str内容为：hello
str类型为：<class 'str'>
str内容为：123
str类型为：<class 'int'>
'''
str这个变量既可以表示字符串也可以表示数字
```

由此可见python中的变量就像一个万能的指针可以指向任意类型的数据，它自己本身没有类型或者说是一种特殊的类型。

<font color=browen>**注意：Python大小写敏感**</font>



##### 局部变量和全局变量

- 局部变量就是定义在函数中的变量，其作用域仅在函数体中有效

  - 在函数体中定义全局变量用关键词 global，此关键字详细使用效果：

  - ```python
    def fun01():
        num01 = 111
        print(f"id(num01) = {id(num01)}")
    
    num01 = 111111
    print(f"id(num01) = {id(num01)}")
    fun01()
    '''
    id(num01) = 2141168989584   #这是全局变量num01的id
    id(num01) = 2141167947440   #这是局部变量num01的id，可以看出二者id不同说明是两个独立的变量
    '''
    
    #****************************************************************************************************
    def fun02():
        # global num02 = 222    #这么写是错误的，在函数里定义全局变量不能初始化
        global num02            #这么写就是在函数里创建全局变量，哪怕函数结束了num02依旧存在
        num02 = 222
    
    
    fun02()
    print(f"num02={num02}")     #结果：num02=222 ， 也就是说在函数内定义的全局变量在函数结束后依旧存在，还能正常使用
    
    
    #****************************************************************************************************
    def fun03():
        global num03        #这就相当于说明：我接下来在fun03中使用的num03是一个全局变量
        print(f"id(num03) = {id(num03)}")
        num03 = 333
        print(f"id(num03) = {id(num03)}")
    
    
    num03 = 333333
    print(f"id(num03) = {id(num03)}")
    fun03()
    print(f"id(num03) = {id(num03)}")
    print(f"num03={num03}")     #结果：num03=333 ， 由于在fun03之前已经定义了全局变量num03所以fun03()里面的num03和此处的num03是同一个
    
    '''
    id(num03) = 1805577352816   #函数体外定义的num03的id值
    id(num03) = 1805577352816   #函数题内使用global关键字表明函数体内num03就是函数体外的那一个（二者是同一个变量）
    id(num03) = 1805577352592   #在函数体内对num03做修改
    id(num03) = 1805577352592   #结果显示函数体内的修改能影响到函数体外的全局变量num03
    '''
    #****************************************************************************************************
    '''
    def fun04():
        num04 = 444         #这样写会报错：name 'num04' is assigned to before global declaration
        global num04        #意思就是说：你先定义局部变量num04有搞一个全局变量num04那这两个名字不久冲突了，你后续使用num04是要用哪个？
                            # python，貌似没有用来区分二者的关键字（也就是说python作者并不允许你这么搞）
    '''
    
    ```

- 全局变量就是定义在函数之外的变量、



##### 类型

python的类型有如下这些：

| 整数   | 浮点数 | 布尔类型 | 字符串 | 列表 | 元组   | 字典 | 集合 |
| ------ | ------ | -------- | ------ | ---- | ------ | ---- | ---- |
| 不可变 | 不可变 | 不可变   | 不可变 | 可变 | 不可变 | 可变 | 可变 |
|        |        |          | 序列   | 序列 | 序列   | 序列 | 序列 |



学习数据类型无非就是一下几点;

- 类型定义与初始化
- 类型常用函数（增删改查）
- 类型特点（使用场景）
- 类型的特殊操作

其实后四个可以叫容器类型

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
  - 不可变数据进行“修改”后变量的id就会改变
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。
  - 不可变数据进行“修改”后变量的id不会改变

##### 类型判断

可以使用函数 type() 来判断类型

```python
num_type = 1000             # 整数
float_type = 999.0          # 浮点数
bool_type = True            # 布尔类型
str_type = "hello word"     # 字符串

print("num_type的类型是：\t"   + str(type(num_type)))		#类型转换再用+拼接两个字符串输出
print("float_type的类型是：\t" + str(type(float_type)))
print("bool_type的类型是：\t"  , type(bool_type))			#直接用,隔开两个东西一起输出
print("str_type的类型是：\t"   , type(str_type))

#执行结果如下：
'''
    num_type的类型是：	<class 'int'>
    float_type的类型是：	<class 'float'>
    bool_type的类型是：	 <class 'bool'>
    str_type的类型是：	 <class 'str'>
'''
```

#### 数值

数值包括：整数、浮点数、布尔类型、复数

##### 整数

python3整数只有int这一种，没有long或者其他类型

```python
print(0x1234)     		#十六进制表示的整数
print(type(0x1234))
print(0x12_34)			#可以在整数中嵌套任意个 _
print(100_000_000 == 100000000)
print(10_000)

#执行结果如下
"""
4660
<class 'int'>
4660
True
10000
"""
```

##### 浮点数

```python
#浮点数的科学表示法
print(1.2e3,end='\t1.2e3表示 1.2 * 10^3')		#print函数默认末尾有个换行，也可以用 end= 来指定末尾的内容

#执行结果
'''
1200.0	1.2e3表示 1.2 * 10^3
'''
```



##### 布尔类型

python中：True == 1 、False == 0

- 注意python大小写敏感
- 逻辑运算与或非：and or not   (python没有异或等其他逻辑运算)

<font color=browen>**注意：python中if判断中的None等价于False，所以常常可以 if 搭配函数一起使用**</font>



##### 数值运算

```python
#除法和地板除
print(10/3)
print(10//3)	#地板除的结果永远是整数（听名字就知道是向下取整）
print(10%3)
print(2**3)		#python的指数运算和c不一样，使用**

#运行结果
'''
3.3333333333333335
3
1
8
'''
```





#### 字符串

python中没有所谓的char、string的区别，统一都用字符串定义和初始化

- ```python
  str01 = 'str01'
  str02 = "str02"
  str03 = '''str03        # 这么干的好处是字符串初始化可以有多行，相当于str03 = ”str03\n“
          '''
  str04 = r"""str03        # 这么干的好处是字符串初始化可以有多行，相当于str03 = ”str03\n“
          """
  
  print(str01)
  print(str02)
  print(str03)			#str03和str04这种写法和多行注释一样，只不过将注释赋值给了某个变量
  print(str04)
  
  运行结果：
  '''
  str01
  str02
  str03        # 这么干的好处是字符串初始化可以有多行，相当于str03 = ”str03
  “
  
  str03        # 这么干的好处是字符串初始化可以有多行，相当于str03 = ”str03\n“
  '''
  ```

##### 字符串格式化

- 使用 占位符和% 、使用 标记f和{} 、也可以直接对表达式进行格式化

- ```python
  # 字符串之间可以直接用 + 进行拼接
  #也可以使用格式化方式与其他类型数据拼接，和c中的printf()类似,其中占位符和c语言也类似
  name = "流水忆落花"
  age = 12
  salary = 100.1
  massage01 = "名字：%s\n年龄：%d\n薪水：%f"%(name , age , salary)
  print(massage01)
  
  输出结果：
  '''
  名字：流水忆落花
  年龄：12
  薪水：100.100000
  '''
  
  #也可以使用快速格式化	使用标记 f和{}
  massage02 = f"名字：{name}\n年龄：{age}\n薪水：{salary}"		#massage02和massage01的内容一摸一样
  print(massage02)
  
  #直接对表达式进行格式化
  print("1*1 = %d" % (1*1))
  print(f"1*1 = {1*1}")
  print("python中的字符串类型叫：%s" % type('字符串'))
  
  输出结果：
  '''
  1*1 = 1
  1*1 = 1
  python中的字符串类型叫：<class 'str'>
  '''
  ```

##### 字符串输出

- ```python
  print('hello' + "world")    # ''和""都可以表示字符串,和java一样可以用+来进行字符串拼接
  print("hello\tworld\n")     # 和C语言一样可以使用各种转义字符:\t \n
  print(r"hello\tworld\n")    # 在""前面加上r表示字符串中所有转义字符都失效
  print("hello\\tworld\\n")   # 与加上r的字符串是一样的效果
  print("I'm 流水忆落花")       # 在”“里面可以正常输出'.同样的也可以在''中正常输出"
  
  #执行结果
  '''
  helloworld
  hello	world
  
  hello\tworld\n
  hello\tworld\n
  I'm 流水忆落花
  '''
  ```

  



#### 数据容器

各类容器可用的方法w3cschool讲的很好，无需重复记录

##### 列表 List [ ]

```python
list.append(obj)		#末尾添加新的对象
list.count(obj)			#统计某个元素在列表中出现的次数
list.extend(seq)		#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)			#从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)	#在列表的index的地方插入一个对象
list.pop([index=-1])	#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)		#移除列表中某个值的第一个匹配项
list.reverse()			#反向排列列表中元素
list.sort( key=None, reverse=False)	#对原列表进行排序
list.clear()			#清空列表
list.copy()				#复制列表
```



##### 字典 dict {k:v}

```python
radiansdict.clear()			#删除字典内所有元素
radiansdict.copy()			#返回一个字典的浅复制
radiansdict.fromkeys()		#创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None)	#返回指定键的值，如果值不在字典中返回default值
key in dict					#如果键在字典dict里返回true，否则返回false
radiansdict.items()			#以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()			#以列表返回一个字典所有的键
radiansdict.setdefault(key, default=None)	#和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2)	#把字典dict2的键/值对更新到dict里
radiansdict.values()		#以列表返回字典中的所有值
```



##### 元组 tuple （ ）

元组中的内容不可修改，但是可以删除根据原元组的内容新建元组从而达到删除的目的

```python
tuple(seq)					#将列表转换为元组。	
operator(tuple1,tuple2)		#较两个元组元素
```



##### 集合 set { }

python集合符合数学概念：无序、不重复

###### 集合的运算

<font color=browen>**注意：集合使用操作符运算要求被操作对象都是集合，而使用函数的话函数中参数可以是任何可迭代对象**</font>

| 操作符             | 等价函数                             | 含义解释                                             |
| ------------------ | ------------------------------------ | ---------------------------------------------------- |
| a-b                | set.difference(*others)              | a集合中b没有的元素                                   |
| a\|b               | set.union(*others)                   | 并集                                                 |
| a&b                | set.intersection(*others)            | 交集                                                 |
| a^b                | set.symmetric_difference(*other*)    | a独有或b独有元素                                     |
| set\|=other\|...   | set.update(**others*)                | 更新集合，添加来自 others 中的所有元素。             |
| set &= other & ... | intersection_update(**others*)       | 更新集合，只保留其中在所有 others 中也存在的元素。   |
| set-=other\|...    | difference_update(**others*)         | 更新集合，移除其中也存在于 others 中的元素。         |
| set ^= other       | symmetric_difference_update(*other*) | 更新集合，只保留存在于集合的一方而非共同存在的元素。 |

说明：参数中*other表示参数可以接受任意多个



###### **集合的判断**

| **set <= other** | **issubset**(*other*)   | 检测是否集合set中的每个元素都在 *other* 之中。               |
| ---------------- | ----------------------- | ------------------------------------------------------------ |
| **set < other**  | **issubset**(*other*)   | 检测集合set是否为 *other* 的真子集，即 `set <= other and set != other`。 |
| **set >= other** | **issuperset**(*other*) | 检测是否 *other* 中的每个元素都在集合set之中。               |
| **set > other**  | **issuperset**(*other*) | 检测集合是否为 *other* 的真超集，即 `set >= other and set != other`。 |



###### 集合其它函数

```python
add(elem)		#将元素 elem 添加到集合中。
remove(elem)	#从集合中移除元素 elem。 如果 elem 不存在于集合中则会引发 KeyError。
discard(elem)	#如果元素 elem 存在于集合中则将其移除。
pop()			#从集合中移除并返回任意一个元素。 如果集合为空则会引发 KeyError。
clear()			#从集合中移除所有元素。
isdisjoint(other)	#如果集合中没有与 other 共有的元素则返回 True。 当且仅当两个集合的交集为空集合时，两者为不相交集合。
```







#### 序列操作

w3cschool总结的很不错：https://www.w3cschool.cn/python3/python3-sequence.html



<font color=browen>**注意：字典和集合不支持索引、切片、相加、相乘操作**</font>

##### 切片

> 切片(slice)是对序列型对象(如`list`, `string`, `tuple`)的一种高级索引方法。

讲的十分清晰！！！：https://blog.csdn.net/downing114/article/details/70445468

在此博客基础上补充：

- [start_index : end_index : step]	#表示遍历 [start_index , end_index) 即：左开右闭区间

- 正、负向索引可以混用

- step > 0 表示从 start_index 向右遍历
- step < 0 表示从start_index 向左遍历

##### 索引

##### 相加

类型相同的序列才能进行相加

##### 乘法

##### 成员资格

简单来说就是能够用 in 关键字判断元素是否存在



##### 通用函数

![](python基础笔记.assets/序列的内置函数.png)







### 分支

就是if else 不过python中 else if 写为 elif （和c、java的写法都不同）

```python
age = 20
if age >= 6:			#别忘了 :
    print("第一个判断")
    print('teenager')
elif age >= 18:
    print("第二个判断")
    print('adult')
else:
    print("第三个判断")
    print('kid')
    
输出结果
'''
第一个判断
teenager
'''
```



### 循环

比较好的介绍python循环：https://www.runoob.com/python3/python3-loop.html

python循环就两种：while和for (没有do while、goto这种)

- 两种循环都可以配合else语句
- for循环
  - for循环通常搭配 in 或者 range() 实现遍历操作





### 函数

##### 函数定义

```python
def 函数名(传参):
	函数体
	return 返回值

再次说明：python中变量是没有类型的（也就是说变量可以指向任意类型的数据），下面这么写是完全可以的
a = [1,2,3]
a = "Runoob"
```

##### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。



##### 函数参数类型

- 必需参数
- 关键字参数
- 默认参数
- 不定长参数
  - *表示元组
  - **表示字典
  - 



##### 返回值

python 函数默认返回 None ， 在 if 语句中 None 等价于 False



### 迭代器



### 文件操作



### 其他

查看python版本：python --version

安装目录中的python.exe就是python的解释器

#### 和C、Java区别

- python使用缩进来表示代码块而非 { }

- python语句一般都是一行，所以每一个语句末尾不需要写 ; 来表示语句结束

  - 多行语句，也可以使用\来表示语句有多行

  - ```python
    salary = 3 + \
        4 + \
        5
    print(salary)	#运行结果为12
    ```

  - 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 ，例如：

    ```python
    total = ['item_one', 'item_two', 'item_three',
            'item_four', 'item_five']
    ```

- python中变量不用显示申明类型，直接赋值即可

  - ```python
    int num = 3;	\\这是c语言或者java的写法
    num = 3			#这是python的写法
    ```

在python中：变量是没有类型的！



#### 注释

```python
# 这是单行注释

"""
	这是多行注释
"""

'''
	这也是多行注释(可以但不建议,还是统一用双引号)
'''
```

#### 输入输出

就是两个函数：print() 和 input()

input

- ​	菜鸟教程讲的比较详细：https://www.runoob.com/python3/python3-func-input.html

- 以换行为结束符
- 返回值仅为str类型，想输入其他类型数据可以进行类型转换





