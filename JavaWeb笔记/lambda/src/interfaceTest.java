//定义一个接口Shape并用两个类来实现该接口
public class interfaceTest {
    public static void main(String[] args) {
        Circular c = new Circular(1);
        Rectangle r = new Rectangle(2, 3);

        System.out.println("Circular的周长：" + c.getLongth());
        System.out.println("Circular的面积：" + c.getArea());

        System.out.println("Rectangle的周长：" + r.getLongth());
        System.out.println("Rectangle的面积：" + r.getArea());

    }
}

interface Shape {
    public double pi = 3.14;

    public double getLongth();

    public double getArea();
}

//定义Circular类实现Shape接口
class Circular implements Shape {  //此处"实现"的英文单词没记住
    private double pi = 3.14;
    private double R;

    Circular(double R) {
        this.R = R;
    }

    public double getLongth() {  // 周长
        return pi * 2 * R;
    }

    public double getArea() {  //面积
        return pi * R * R;
    }
}

//定义Rectangle类实现Shape接口
class Rectangle implements Shape {
    private double pi = 3.14;
    private double w; //宽
    private double h; //高

    Rectangle(double w, double h) {
        this.w = w;
        this.h = h;
    }

    public double getLongth() {  //周长
        return (w + h) * 2;
    }

    public double getArea() {    //面积
        return w * h;
    }


}

