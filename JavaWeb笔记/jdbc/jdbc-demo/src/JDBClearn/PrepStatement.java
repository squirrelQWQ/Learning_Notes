package JDBClearn;

/*
* PreparedStatement类使用案例
* 读取配置文件login.properties来获取连接数据库的登录名等
* */

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

public class PrepStatement {
    public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
//使用Propertise类获取配置文件中数据
        Properties properties = new Properties();
//        System.out.println(); //获取class的当前路径
        properties.load(new FileInputStream(System.getProperty("user.dir")+"\\jdbc-demo\\src\\pojo\\login.properties"));

        String username1 = properties.getProperty("username");
        String password1 = properties.getProperty("password");
        String url1 = properties.getProperty("url");
        String driver = properties.getProperty("driver");


        Class.forName(driver);
        Connection connection =  DriverManager.getConnection(url1,username1,password1);
        String sql = "INSERT INTO `fruits` VALUES (null,?, '10', '110', ?);";

//预编译
        PreparedStatement preparedStatement = connection.prepareStatement(sql);
        preparedStatement.setString(1 , "香梨");
        preparedStatement.setString(2 , "香梨");

//执行sql，此处不能放入sql不然会执行带"？"的sql语句
        int count = preparedStatement.executeUpdate();

        System.out.println(count>0?"插入成功":"插入失败");
        preparedStatement.close();
        connection.close();
    }
}


















