package lambda;

import java.util.ArrayList;

public class synchronizedTest {

    public static void main(String[] args)  {
         InsertData insertData = new InsertData();

        new Thread() {
            public void run() {
                synchronized (insertData){
                    insertData.insert(Thread.currentThread());
                }

            };
        }.start();


        new Thread() {
            public void run() {
                synchronized (insertData){
                    insertData.insert(Thread.currentThread());
                }

            };
        }.start();
    }
}

class InsertData {
    private ArrayList<Integer> arrayList = new ArrayList<Integer>();

    public void insert(Thread thread){
        for(int i=0;i<5;i++){
            System.out.println(thread.getName()+"在插入数据"+i);
            arrayList.add(i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}


