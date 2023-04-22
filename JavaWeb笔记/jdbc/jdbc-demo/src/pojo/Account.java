package pojo;

/*
* 创建account的实体类
* 用于在JDBC_resultSet中接收查询结果
* */
import java.math.BigDecimal;

public class Account {
    private int id;
    private String name;
    private BigDecimal cash;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BigDecimal getCash() {
        return cash;
    }

    public void setCash(BigDecimal cash) {
        this.cash = cash;
    }

    @Override
    public String toString() {
        return "account{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", cash=" + cash +
                '}';
    }
}
