package JDBClearn;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCtext01 {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
//        注册驱动,
//        实际上该行不写也可以，在导入的jar驱动包里META-INF/services/java.sql.Driver有对应参数，会自动加载
//        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/shop?useUnicode=true&characterEncoding=utf8&useSSL=true";
        String username = "root";
        String password = "123456";

//        获取连接
        Connection connection =  DriverManager.getConnection(url,username,password);

        String sql = "select * from fruits";

//        获取执行sql的对象
        Statement statement = connection.createStatement();

//        执行sql
        int count = statement.executeUpdate(sql);

        System.out.println("执行成功，受到影响的行数："+count);


//        释放资源
        statement.close();
        connection.close();
    }
}




















