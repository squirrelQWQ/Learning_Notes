package JDBCUtils;
/*
* Jdbc工具类使用示例
* */
import com.mysql.cj.jdbc.JdbcConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class JdbcUtils_use {

    public static void main(String[] args) {
        JdbcUtils_use jdbcUtils_use = new JdbcUtils_use();
        jdbcUtils_use.testDML();
    }


    public void testDML(){
        Connection connection = JdbcUtils.getConnection();
        String sql = "INSERT INTO `fruits` VALUES (null,?, '10', '110', ?);";

        PreparedStatement preparedStatement = null;

        try {
            preparedStatement =  connection.prepareStatement(sql);
            preparedStatement.setString(1 , "香梨");
            preparedStatement.setString(2 , "香梨");

            int count = preparedStatement.executeUpdate();
            System.out.println(count>0?"插入成功":"插入失败");

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JdbcUtils.close(null , preparedStatement , connection );
        }
    }
}
