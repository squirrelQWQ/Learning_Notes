### IOC和DI

> spring IOC 三种配置方式：XML、注解、JavcConfig类（JavaConfig类可以说是注解的一种应用）
>
> spring DI 三种方式：构造方法注入（Construct注入），setter注入，基于注解的注入（接口注入）

IOC 三种配置方式就是：用什么方式传送 spring 容器构造 Bean 时需要的参数

DI 三种方式：spring 容器创建 Bean 时怎么把参数写入 Bean 中



Bean与spring容器的关系：

![](C:\Users\squir\Desktop\Bean与spring容器关系.png)



#### XML方式

##### bean标签

> 更详细的介绍：http://c.biancheng.net/spring/bean-definition.html

- id属性：在容器中Bean的唯一标识
  - 理论上id可以任取，但是约定使用首字母不大写的类名

- class属性：要实例化的Bean的全限定名

- scope属性：Bean的作用范围，常用的有以下两个选项
  - Singleton（默认），容器中仅含一个实例对象（<font color='red'>单例模式</font>）
  - prototype，每次容器调用方法 getBean( ) 都会返回一个新的实例对象（<font color='red'>多例模式</font>）

- \<property>标签：（属性注入）
  - name属性：此属性值是对应set方法的名称
    - 比如 User 对象有 setMySalary() 方法
    - property标签的那么属性就应该取名：mySalary  （和id属性的命名约定差不多，首字母不大些其余照抄）
  - value属性：注入的普通属性值
  - ref属性：注入的对象引用值
  - \<list>标签
  - \<map>标签
  - \<properties>标签
- \<constructor-arg>标签：默认使用无参构造，该标签就是指定使用有参构造，且传递相应的参数值



##### import标签

import标签可以对xml配置文件进行拆解，类似于web文件中把JavaScript和html，CSS文件分割开，分割后只需调用主配置文件即可

```XML
<import resource="applicationContext-xxx.xml"/>
```



#### 注解方式

##### 原始注解

> spring的原始注解主要就是替代<Bean>标签的作用

- @Component		使用在类上用于实例化Bean（下面那三个功能和@Compoment功能一样，就是增强了可读性）
  - @Controller			使用在web层类上用于实例化Bean
  - @Service				使用在service层类上用于实例化Bean
  - @Repository		使用在dao层类上用于实例化Bean

- @Autowired		使用在字段上用于根据类型依赖注入（也就是所谓的依赖注入，写上该注解让Spring自动装配）
  - 也可单独使用，前提是容器中仅含有一个该数据类型实例

- @Qualifier			结合@Autowired一起使用用于根据名称进行依赖注入


@Resource			相当于@Autowired+@Qualifier，按照名称进行注入

@Value				注入普通属性

@Scope				标注Bean的作用范围

@PostConstruct	使用在方法上标注该方法是Bean的初始化方法

@PreDestroy		使用在方法上标注该方法是Bean的销毁方法



##### 新注解

> 简单来说就是XML配置中很多操作都不能用原始注解来解决

比如：

- 非自定义的Bean的配置：\<bean>
- 加载properties文件的配置：\<context:property-placeholder>
- 组件扫描的配置：\<context:component-scan>
- 引入其他文件：\<import>

https://blog.51cto.com/u_15754099/5585277

```java
@Configuration
@ComponentScan
@Bean
@PropertySource
@Import
```



##### 组件扫描

就是在applicationContext.XML 中指明，注解中要生成的Bean要在哪些包里面进行查找，从而将参数和方法传递给容器





### 配置数据源

> 就是spring配置数据库连接池比如：Druid、C3P0

Java 开发中，需要将一些易变的配置参数放置再 XML 配置文件或者 properties 配置文件中。然而 XML 配置文件需要通过 DOM 或 SAX 方式解析，而读取 properties 配置文件就比较容易。

##### 命名空间：

简单来说就和package一样都是用来解决命名冲突的，只不过XML里面叫命名空间，而 java 中叫package

和java类会被加上package翻译为全类名一样，XML配置也会加上命名空间，不过package同时也是文件夹名称罢了

https://jluncc.github.io/2019/02/17/spring-xml-namespace/

字段解释：https://www.cnblogs.com/sonng/p/6582439.html





### 集成Junit



### 集成Web

ApplicationContext应用上下文获取方式：

```java
 ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
```

web工程将会含有很多servlet 但每次获取对象时都需要用上述方法，读取配置文件，创建ApplicationContext对象，这样显然不合适

可以使用 ServletContextListener监听Web应用的启动，同时创建ApplicationContext对象，并放置在最大的域servletContext中这样就可以创建一次，多次使用

spring提供了ContextLoaderListener监听器实现了上述功能

> 导入spring-web坐标

原理介绍博客：https://zhuanlan.zhihu.com/p/65258266



### 名词解释

##### Bean

简单来说就是和数据库中表对应的 java 类，方便和数据库的操作

通常包含以下几部分：

- 所有属性为private
- 提供默认构造方法
- 提供getter和setter
- 实现serializable接口



##### POJO

> plain old JavaScript object

和Bean类似，也是 java 中一种特殊的类

大致符合以下几点：

- 不继承任何类

- 不继承实现任何接口

- 没有包含注解



##### Dao

> Data Access Object

简单来说就是把对数据库的访问都封装起来，这是一种模式（可以理解为代码组织的风格）

通常包含以下几部分：

- DAO接口： 把对数据库的所有操作定义成抽象方法，可以提供多种实现
- DAO 实现类：针对不同数据库给出DAO接口定义方法的具体实现
- 实体类：用于存放与传输对象数据，比如表示查询到的所有字段存放的的对象
- 数据库连接和关闭工具类：避免了数据库连接和关闭代码的重复使用，方便修改



##### impl

java impl 是一个资源包，用来存放java文件的（属于java后台开发代码工程文件的组织方式）。
在Java开发中，通常将后台分成几层，常见的是三层（MVC）model、view、controller

impl的全称为implement，表示实现的意思，故该文件夹（包）里面存放接口实现类。



##### AOP

> Aspect Oriented Program 面向切面编程

在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。

异常清晰的回答：https://www.zhihu.com/question/24863332



##### XML

言简意赅的回答：https://www.zhihu.com/question/31353595

虽然XML本身是没有预定义标签的（比如HTML种的h1标签，p标签等）。

但是对大部分情况而言，都是使用别人规定好的一套规则来使用XML。

比如spring中

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="userDaoId" class="com.spring.dao.impl.UserDaoImpl"></bean>
</beans>
```

这里的 bean 以及其属性 id，class 都是 spring 的开发者设计好的。

只需要考虑：

- spring 作者定义了哪些标签和属性，以及各有什么用即可
- 了解这些标签实际上干了些什么
  - bean 标签就是用来告诉spring框架要创建 bean
  - id 就是告诉 spring 创建哪一种 bean
  - class 就是告诉 spring 怎么创建 bean （这里的是使用无参构造方式，还可以选用静态工厂，动态工厂）



##### 依赖注入

> Dependency Injection 简称 DI



通过代码阐述控制反转 IOC 和依赖注入DI：https://juejin.cn/post/6857406008877121550#heading-12

“自然经济”、“商品经济”类比描述 IOC 和 DI 到底在干嘛（理解理念）：https://www.bilibili.com/video/BV1Pq4y1Q7p9/?spm_id_from=333.337.search-card.all.click&vd_source=553038a6aa71e8272f6ae73b38f60f80



