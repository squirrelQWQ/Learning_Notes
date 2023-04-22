package lambda;

public class LockTest {
    public static void main(String[] args) {
        Buy buy = new Buy();

        new Thread(buy).start();     //匿名类
        new Thread(buy).start();
        new Thread(buy).start();
    }

}

class Buy extends Thread{

    static Number number = new Number(10);

    @Override
    public void run() {
        while(number.getNumber() >= 0){
            synchronized (number){
                System.out.println( Thread.currentThread().getName() + "  num = "+number.getNumber());
                number.setNum();
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }

        }
    }
}

class Number{
    private int num;

    public Number(int num) {
        this.num = num;
    }

    int getNumber(){
        return num;
    }

    void setNum(){
        this.num -= 1;
    }
}