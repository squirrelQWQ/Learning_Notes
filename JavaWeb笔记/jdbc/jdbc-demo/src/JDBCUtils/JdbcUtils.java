package JDBCUtils;
/*
* 工具类，完成mysql的连接和关闭资源
* */

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

public class JdbcUtils {
    private static String username;
    private static String password;
    private static String url;
    private static String driver;

    static {

        try {
            Properties properties = new Properties();
            properties.load(new FileInputStream(".\\jdbc-demo\\src\\pojo\\login.properties"));

            username = properties.getProperty("username");
            password = properties.getProperty("password");
            url = properties.getProperty("url");
            driver = properties.getProperty("driver");
        } catch (IOException e) {
//            将编译异常变为运行异常
//            调用者可以自行选择是否捕获该异常
            throw new RuntimeException(e);
        }
    }

    public static Connection getConnection(){
        try {
            return DriverManager.getConnection(url , username ,password );
        } catch (Exception e) {
//            将编译异常变为运行异常
//            调用者可以自行选择是否捕获该异常
            throw new RuntimeException(e);
        }
    }

/*
* 关闭相关资源
*  ResultSet
* Statement
* Connection
* */
        public static void close(ResultSet resultSet , Statement statement , Connection connection){
            try {
                if(resultSet != null){
                    resultSet.close();
                }
                if(statement != null){
                    statement.close();
                }
                if(connection != null){
                    connection.close();
                }
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }

}










