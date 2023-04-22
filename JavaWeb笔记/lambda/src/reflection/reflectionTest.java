package reflection;

public class reflectionTest {
    public static void main(String[] args) throws ClassNotFoundException {
        User user = new User("八戒",12,3);
        Class c1 = Class.forName("reflection.User");
        Class c2 = Class.forName("reflection.User");
        Class c3 = Class.forName("reflection.User");
        Class c4 = Class.forName("reflection.User");

        System.out.println(c1.hashCode());
        System.out.println(c2.hashCode());
        System.out.println(c3.hashCode());
        System.out.println(c4.hashCode());

        System.out.println(user.getName());

    }
}

class User {
    private String name;
    private int id;
    private int age;

    public User(String name, int id, int age) {
        this.name = name;
        this.id = id;
        this.age = age;
    }

    public String getName(){
        return name;
    }

    public int getId(){
        return id;
    }



}
