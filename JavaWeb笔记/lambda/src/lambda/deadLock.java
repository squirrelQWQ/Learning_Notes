package lambda;
//死锁示例
//两个student都想同时用book和pen
public class deadLock {
    public static void main(String[] args) {

        Student student1 = new Student("Tom" , 0);
        Student student2 = new Student("Bob" , 1);

        student1.start();
        student2.start();


    }
}

class Student extends Thread{
    private String name;
    private Integer choice;

    static Pen pen = new Pen();
    static Book book = new Book();


    //static private String book = "《Java从入门到放弃》"; //临界资源
    //static private String pen = "《马良的神笔》";  //临界资源

    @Override
    public void run() {
        try {
            study(name , choice);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void study(String name , Integer choice) throws InterruptedException{
        if(choice == 0){
            synchronized (book){
                System.out.println(name + "获得了book的锁");
                Thread.sleep(1000);
                synchronized (pen){
                    System.out.println(name + "获得了pen的锁");
                }
            }
        }
        else{
            synchronized (pen){
                System.out.println(name + "获得了pen的锁");
                Thread.sleep(1000);
                synchronized (book){
                    System.out.println(name + "获得了book的锁");
                }
            }
        }
    }

    public Student(String name , Integer choice) {
        this.name = name;
        this.choice = choice;
    }
}

class Book{

}
class Pen{

}