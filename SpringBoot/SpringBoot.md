当服务器程序还在跑时，这时对源文件的修改不会影响已经打开了的页面



### Restful风格

> RESTful风格只是一种规范，没有强制实现，但是按着规矩来代码更简洁易懂

比如：GET仅用来查询，POST用于新增，Put用于修改，Delete用于删除

这样做的好处是显而易见的，可读性增强，代码分工明确





### 注解

##### @RestController

> @RestController = @Controller + @ResponseBody

用于标记一个类或者方法，表示该类或方法用于处理HTTP请求，并将响应的结果直接返回给客户端，而不需要进行视图渲染

**@Controller和@RestController**：

- 二者都是标记一个类来处理http请求

- 　@Controller类中的方法可以直接通过返回String跳转到jsp、ftl、html等模版页面。在方法上加@ResponseBody注解，也可以返回实体对象。

- 　　@RestController类中的所有方法只能返回String、Object、Json等实体对象，不能跳转到模版页面。



##### @GetMapping

标记一个方法，表示映射HTTP的GET请求到对应的处理方法，与之相似的还有下面几种注解

- @GetMapping
- @PostMapping
- @PutMapping
- @DeleteMapping

当然同一类型的HTTP请求可能会有多个，为了区分这些请求都会加上不同的id（组成所谓的url）来区分

例子：

- ```java
  @GetMapping              /*当浏览器输入 localhost:8080 时会调用此方法*/
  @GetMapping("hello2")    /*当浏览器输入 localhost:8080/hello2 时会调用此方法*/
  ```

所谓api 我的理解就是这些HTTP请求所映射的方法（也就是这些注解所标注的方法）

除了上述这几个注解还有：@RequestMapping、@PatchMapping等

@RequestMapping：默认字段是value（和path等价），默认方法是GET，可以使用 RequestMethod.POST来指定POST方法

```java
@RequestMapping(value = "/register01",method = RequestMethod.POST)
@PostMapping("/register02")
//这两种写法都可以，但还是第二种更简洁
```



### 持久层框架

##### mybatis和springdata jpa

二者都是持久层框架（即操作数据库的东西），但是二者倾向不同（思想也不同）

- mybatis：主要是进行SQL语句的映射，如果你SQL写的牛逼，大可选用它
  - 优势：
    - 可以精细话的设计SQL语句（所以当需求很复杂的时候用mybatis就比较好）
    - 对初学者友好（因为既然学Mybatis了肯定之前学过了数据库，对SQL语句编写也不那么陌生，所以选择Mybatis亲切些且上手快）
- springdata jpa：将java类和数据库实体对应，通过操作类自动生成SQL语句
  - 优势：
    - 相对简单，可以对SQL语句不那么熟练
    - 与SpringBoot高度集成（直接无缝衔接）

二者的关系有点像TCP和UDP的关系，TCP更精密、UDP主打的就是简单效率高，二者各有优劣。



清晰的对比：https://cloud.tencent.com/developer/article/1702931























