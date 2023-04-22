package JDBClearn;
/*
* connection事务管理代码示例
* */
import java.sql.*;

public class JDBC_connection {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
//        注册驱动,
//        实际上该行不写也可以，在导入的jar驱动包里META-INF/services/java.sql.Driver有对应参数，会自动加载
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/shop?useUnicode=true&characterEncoding=utf8&useSSL=true";
        String username = "root";
        String password = "123456";

//        获取连接
        Connection connection =  DriverManager.getConnection(url,username,password);


//        获取执行sql的对象
        Statement statement = connection.createStatement();


        try {
            //关闭自动提交事务
            connection.setAutoCommit(false);


            String sql1 = "UPDATE `shop`.`account` SET `cash` = '3000' WHERE `id` = '1';";
            //int a = 3/0;
            String sql2 = "UPDATE `shop`.`account` SET `cash` = '4000' WHERE `id` = '2';";

//        执行sql
            int coun1 = statement.executeUpdate(sql1);
            int coun2 = statement.executeUpdate(sql2);

            System.out.println("执行成功，受到影响的行数："+coun1);
            System.out.println("执行成功，受到影响的行数："+coun2);

            //提交事务
            connection.commit();
        } catch (Exception e) {
            connection.rollback();
            e.printStackTrace();
        }


//        释放资源
        statement.close();
        connection.close();
    }
}




















