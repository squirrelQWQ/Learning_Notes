菜鸟教程yyds：https://www.runoob.com/python3/python3-tutorial.html

## python3基础

### 基本类型

像python这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。

静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。比如 Java、C语言

**Python大小写敏感**



| 整数 | 浮点数 | 布尔类型 | 字符串 | 列表 | 元组 | 字典 | 集合 |
| ---- | ------ | -------- | ------ | ---- | ---- | ---- | ---- |
|      |        |          |        |      |      |      |      |

#### 类型判断

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



#### 整数

```python
#十六进制表示的整数
print(0x1234);      print(type(0x1234))
#可以在整数中嵌套任意个 _
print(0x12_34)
print(100_000_000 == 100000000)

#执行结果如下
"""
    4660
    <class 'int'>
    4660
    True
"""
```



#### 浮点数

```python
#浮点数的科学表示法
print(1.2e3,end='\t1.2e3表示 1.2 * 10^3')		#print函数默认末尾有个换行，也可以用 end= 来指定末尾的内容

#执行结果
'''
	1200.0	1.2e3表示 1.2 * 10^3
'''
```



#### 字符串

##### 定义和初始化

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

  

#### 数值运算

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



#### 布尔类型

python中：True == 1 、False == 0

- 注意python大小写敏感
- 逻辑运算与或非：and or not   (python没有异或等其他逻辑运算)



#### 列表 List



#### 字典 dict





#### 元组 tuple



#### 集合 set



#### 切片

讲的十分清晰！！！：https://blog.csdn.net/downing114/article/details/70445468

在此博客基础上补充：

- [start_index : end_index : step]	#表示遍历 [start_index , end_index) 即：左开右闭区间

- 正、负向索引可以混用

- step > 0 表示从 start_index 向右遍历
- step < 0 表示从start_index 向左遍历





### 分支

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
a=[1,2,3]
a="Runoob"
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



## Python库

### Pandas

### NumPy

### matplotlib

### Scikit-Learn







