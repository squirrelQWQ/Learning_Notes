package lambda;

import java.text.SimpleDateFormat;
import java.util.Date;

public class sleepTest implements Runnable {
    public static void main(String[] args) {
        Date startTime = new Date(System.currentTimeMillis());//获取系统当前时间

        while(true){
            try {
                Thread.sleep(1000);
                System.out.println(new SimpleDateFormat("HH:mm:ss").format(startTime));//格式化输出时间
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    @Override
    public void run() {

    }

    public static void tenDown() throws InterruptedException{
        int num = 10;
        while(true){
            Thread.sleep(1000);
            System.out.println(num--);
            if(num <= 0) break;
        }
    }
}






























