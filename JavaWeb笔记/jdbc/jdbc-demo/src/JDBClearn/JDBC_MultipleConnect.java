package JDBClearn;
/*
* 连接数据库的5种方法
* */

import org.w3c.dom.ls.LSOutput;

import java.sql.*;
import java.util.Properties;

public class JDBC_MultipleConnect {

    private String sql = "INSERT INTO `fruits` VALUES (null,'葡萄', '10', '110', '葡萄'); ";
    private String url = "jdbc:mysql://localhost:3306/shop?useUnicode=true&characterEncoding=utf8&useSSL=true";
    Properties properties = new Properties();

    public static void main(String[] args) throws SQLException {
        JDBC_MultipleConnect jdbc_multipleConnect = new JDBC_MultipleConnect();
        jdbc_multipleConnect.connect_01();


    }

//    第一种方法 创建driver对象，
    public void connect_01() throws SQLException {
        Driver driver = new com.mysql.cj.jdbc.Driver();     //初始化连接数据
        properties.setProperty("user" , "root");
        properties.setProperty("password" , "123456");

        Connection connection = driver.connect(url , properties);   //获取连接
        Statement statement = connection.createStatement();     //创建执行sql的对象
        int count = statement.executeUpdate(sql);               //执行sql语句
        System.out.println(count>0?"执行成功":"执行失败");         //输出执行结果
        statement.close();                                      //释放连接
        connection.close();
    }


//方法二，用反射获取连接
//    使得代码更具有灵活性
    public void connect_03(){}
    public void connect_04(){}
    public void connect_05(){}

}















