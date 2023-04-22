package JDBClearn;

import pojo.Account;
/*
* 使用resultSet接受查询语句的结果，并用ArrayList进行封装
* */

import java.math.BigDecimal;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class JDBC_resultSet {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
//        注册驱动,
//        实际上该行不写也可以，在导入的jar驱动包里META-INF/services/java.sql.Driver有对应参数，会自动加载
//        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/shop?useUnicode=true&characterEncoding=utf8&useSSL=true";
        String username = "root";
        String password = "123456";

//        获取连接
        Connection connection =  DriverManager.getConnection(url,username,password);

        String sql = "SELECT * FROM `account`";

//        获取执行sql的对象
        Statement statement = connection.createStatement();

        List<Account> list = new ArrayList<>();
//        执行sql
        try {
            ResultSet resultSet = statement.executeQuery(sql);


            while(resultSet.next()){
                Account account = new Account();
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                BigDecimal cash =  resultSet.getBigDecimal("cash");

                account.setId(id);
                account.setName(name);
                account.setCash(cash);

                list.add(account);

//                System.out.println("id = "+id);
//                System.out.println("name = "+name);
//                System.out.println("cash = "+cash);
//                System.out.println("++++++++++++++++++++++++++++++++++");
            }

        } catch (Exception e) {
            System.out.println("查询失败");
            e.printStackTrace();
        }

        System.out.println(list);

//        释放资源
        statement.close();
        connection.close();
    }
}




















