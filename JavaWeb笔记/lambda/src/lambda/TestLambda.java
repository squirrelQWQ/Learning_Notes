package lambda;

//方法一：
/*  最原始写法
public class TestLambda {
    public static void main(String[] args) {
        LInter linter = new LInter();
        linter.fun();
    }
}

interface inter{
    void fun();
}

class LInter implements inter{
    @Override
    public void fun() {
        System.out.println("平平无奇java小天才");
    }
}*/


//方法二：
//使用静态内部类
public class TestLambda {

    static class LInter implements inter{
        @Override
        public void fun() {
            System.out.println("平平无奇java小天才");
        }
    }

    public static void main(String[] args) {
        LInter linter = new LInter();
        linter.fun();
    }
}

interface inter{
    void fun();
}

//方法三
/*  局部内部类
public class TestLambda {

    public static void main(String[] args) {

        class LInter implements inter{
            @Override
            public void fun() {
                System.out.println("平平无奇java小天才");
            }
        }

        LInter linter = new LInter();
        linter.fun();
    }
}

interface inter{
    void fun();
}*/


//方法四：
/*  匿名内部类(必须继承一个父类或实现一个接口)
public class TestLambda {

    public static void main(String[] args) {

        inter linter= new inter(){
            @Override
            public void fun() {
                System.out.println("平平无奇java小天才");
            }
        };
        linter.fun();
    }
}

interface inter{
    void fun();
}*/


//方法五： lambda表达式

/*
public class TestLambda {

    public static void main(String[] args) {

        inter linter =(b , c) -> {
            System.out.println(b + "平平无奇java小天才"+c);
        };
        linter.fun(12 , "Hello");
    }
}

interface inter{
    void fun(int a, String s);
}*/
