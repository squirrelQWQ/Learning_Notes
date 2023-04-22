package lambda;

public class yiledTest implements Runnable{

    public static void main(String[] args) {

        yiledTest myThread = new yiledTest();

        new Thread(myThread, "a").start();
        new Thread(myThread , "b").start();

    }

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "线程开始");
        Thread.yield();
        System.out.println(Thread.currentThread().getName() + "线程结束");
    }
}
