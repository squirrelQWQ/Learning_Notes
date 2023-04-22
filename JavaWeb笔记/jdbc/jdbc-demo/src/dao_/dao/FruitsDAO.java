package dao_.dao;

import JDBClearn.JDBC_MultipleConnect;
import org.apache.commons.dbutils.QueryRunner;

import java.sql.Connection;
import java.util.Queue;

/**
 * Created with IntelliJ IDEA.
 *
 * @Author: 陈文杰
 * @Date: 2022/03/24/16:49
 * @Description:
 */
public class FruitsDAO<T> {
    private QueryRunner qr = new QueryRunner();

    public int update(String sql , Object... parameters){
        Connection connection = null;
        return 1;
    }
}






















