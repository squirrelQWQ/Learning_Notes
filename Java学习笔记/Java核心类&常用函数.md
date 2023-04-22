### String

```java
//创建
String s1 = "hello";
String s2 = new String(new char[] {'H', 'e', 'l', 'l', 'o', '!'});

//比较
s1.equals(s2);				//比较s1与s2值是否相同
s1.equalsIgnoreCase(s2);	//忽略大小写
s1 == s2;					//比较s1与s2是否指向同一个字符串对象

//搜索子串
"Hello".contains("ll"); 	// true
"Hello".indexOf("l");		// 2
"Hello".lastIndexOf("l"); 	// 3
"Hello".startsWith("He"); 	// true
"Hello".endsWith("lo"); 	// true

//提取子串
"Hello".substring(2); 		// "llo"	取下标，闭区间
"Hello".substring(2, 4); 	//"ll"		取下标，左闭右开区间

//去除首尾空白字符
"  \tHello\r\n ".trim(); 		// "Hello"	去除：\t \r \n
"\u3000Hello\u3000".strip();	// "Hello"	中文空格字符\u3000也会移除
" Hello ".stripLeading(); 		// "Hello "	去除开头空格
" Hello ".stripTrailing(); 		// " Hello"	去除结尾空格

//判断为空
"".isEmpty(); 				// true，因为字符串长度为0
"  ".isEmpty(); 			// false，因为字符串长度不为0
"  \n".isBlank(); 			// true，因为只包含空白字符
" Hello ".isBlank(); 		// false，因为包含非空白字符

//替换子串
String s = "hello";
s.replace('l', 'w');		// "hewwo"，所有字符'l'被替换为'w'
s.replace("ll", "~~"); 		// "he~~o"，所有子串"ll"被替换为"~~"

//正则表达式替换与切割
String s = "A,,B;C ,D";
s.replaceAll("[\\,\\;\\s]+", ",");	// "A,B,C,D"
String[] ss = s.split("\\,"); 		// {"A", "B", "C", "D"}

//拼接字符串
String[] arr = {"A", "B", "C"};
String s = String.join("***", arr); // "A***B***C"
//拼接字符串还可以直接用“+”拼接字符串，此方法在System.out.println中常用

//格式化字符串(类似c语言printf)
String s = "Hi %s, your score is %d!";
System.out.println(s.formatted("Alice", 80));
System.out.println(String.format("Hi %s, your score is %.2f!", "Bob", 59.5));
    {	%s：显示字符串；
        %d：显示整数；
        %x：显示十六进制整数；
        %f：显示浮点数。	
    	还有其它操作，比如%.2f等等	}

//类型转换
//要把任意基本类型或引用类型转换为字符串，可以使用静态方法valueOf()
String.valueOf(123); 			// "123"
String.valueOf(45.67); 			// "45.67"
String.valueOf(true); 			// "true"
String.valueOf(new Object()); 	// 类似java.lang.Object@636be97c
//字符串转为其它类型
int n1 = Integer.parseInt("123"); 		// 123
int n2 = Integer.parseInt("ff", 16); 	// 按十六进制转换，255

boolean b1 = Boolean.parseBoolean("true"); 	// true
boolean b2 = Boolean.parseBoolean("FALSE"); // false
//要特别注意，Integer有个getInteger(String)方法，它不是将字符串转换为int，而是把该字符串对应的系统变量转换为Integer：
Integer.getInteger("java.version"); 	// 版本号，11

char[] cs = "Hello".toCharArray(); 		// String -> char[]
String s = new String(cs); 				// char[] -> String

```

Java字符编码及转换，详见[廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1260469698963456)教程



### StringBuilder

> StringBuilder是可变对象，String不可变
> StringBuilder线程不安全,StringBuffer线程安全

```java
StringBuilder strB = new StringBuilder();
//字符串连接
//append(String str)/append(Char c)
System.out.println("StringBuilder:"+strB.append("ab").append('c'));
//return "StringBuilder:abc"

//转为字符串
//toString()：返回一个与构建起或缓冲器内容相同的字符串
System.out.println("String:"+strB.toString());
//return "String:ch111c"

3、appendcodePoint(int cp)：追加一个代码点，并将其转换为一个或两个代码单元并返回this
System.out.println("StringBuilder.appendCodePoint:"+strB.appendCodePoint(2));
//return "StringBuilder.appendCodePoint:ch111c"

4、setCharAt(int i, char c)：将第 i 个代码单元设置为 c（可以理解为替换）
strB.setCharAt(2, 'd');
System.out.println("StringBuilder.setCharAt:" + strB);
//return "StringBuilder.setCharAt:chd11c"

5、insert(int offset, String str)/insert(int offset, Char c)：在指定位置之前插入字符(串)
System.out.println("StringBuilder.insertString:"+ strB.insert(2, "LS"));
//return "StringBuilder.insertString:chLSd11c"
System.out.println("StringBuilder.insertChar:"+ strB.insert(2, 'L'));
//return "StringBuilder.insertChar:chLLSd11c"

6、delete(int startIndex,int endIndex)：删除起始位置（含）到结尾位置（不含）之间的字符串
System.out.println("StringBuilder.delete:"+ strB.delete(2, 4));
//return "StringBuilder.delete:chSd11c"
```













