package lambda;

public class StopTest implements Runnable{

    private boolean flag  = true;

    public static void main(String[] args) {
        StopTest stoptest = new StopTest();

        new Thread(stoptest).start();   //创建子线程并运行

        for(int i=0 ; i<100 ; i++){
            System.out.println("This is main function："+ i);
            if(i > 50){
                stoptest.stop();
            }
        }

    }

    @Override
    public void run() {
        int i = 0;
        while(flag){
            System.out.println("Child tread ："+i);
            i++;
        }
    }

    public void stop(){
        this.flag = false;
    }

}
