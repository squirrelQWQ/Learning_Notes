-- mosh减少死琐发生的小建议
/*
	1.更新数据的语句最好顺序相同
	2.尽量减少一个事务中sql语句的数量
    3.把耗时长的事务放在用户量小的时间段执行
*/



-- 查看和更改事务隔离级别
SHOW VARIABLES LIKE 'transaction_isolation';
SET SESSION TRANSACTION ISOLATION LEVEL serializable;


-- 创建事务
START TRANSACTION;

INSERT INTO orders (customer_id , order_date , status)
VALUES(1 , CURDATE() , 1);

INSERT INTO order_items
VALUES (LAST_INSERT_ID() , 1 , 1 , 1);

COMMIT;


SHOW VARIABLES LIKE 'autocommit%';
/*
	INSERT、UPDATE、DELETE默认情况下都会根据系统变量autocommit的取值被装进事务执行
    同样的，也可以使用SET将其设为DISABLE，或ENABLE
    特别注意：autocommit变量是针对连接而言的，也就是同一个设置autocommit变量只会影响同一个会话中的其它语句
	ACID事务的四个属性
		原子性	atomicity
        一致性	consistency
        隔离性	isolation
        持久性	durability
*/