SHOW CHARSET;



-- 更改主键和外键约束 （在以有表的基础上可以用以下语句创建或删除主键外键约束）
ALTER TABLE orders
	ADD PRIMARY KEY (order_id),		-- 如果是复合主键，就是括号里面加逗号：(key1 , key2)
    DROP PRIMARY KEY,	-- 删除主键无需写名字，每个表的主键是唯一的
    DROP FOREIGN KEY fk_orders_customers,
    ADD  FOREIGN KEY fk_orders_customers (customer_id)
		REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
;
    


-- 创建关系
DROP TABLE IF EXISTS orders;
CREATE TABLE orders
(
	order_id	INT PRIMARY KEY,
    customer_id	INT NOT NULL,
    FOREIGN KEY fk_orders_customers (customer_id)
		REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
/*
	创建了关系之后数据库中的各表可能就不能随意删除或修改，
    比如此处orders表和customers表建立的外键关系，故customers表就不能正常删除
    故创建整个数据库的脚本文件中应该先删除orders表再删除customers表，具体结果可见：第十三章-store2-脚本文件
*/


-- 更改表
ALTER TABLE customers
	ADD last_name 	VARCHAR(50) NOT NULL AFTER first_name,
    ADD city 		VARCHAR(30) NOT NULL,
    MODIFY COLUMN first_name VARCHAR(50) DEFAULT '',
    DROP points
;
-- 修改表的操作很危险，一定要在测试环境中确定无误后再放在运行环境中


-- 创建表
CREATE DATABASE IF NOT EXISTS sql_store2;
USE sql_store2;
DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers
(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name 	VARCHAR(50) NOT NULL,
    points 		INT NOT NULL DEFAULT 0,
    email		VARCHAR(255) NOT NULL UNIQUE
);
-- 以上展示了创建表所能用到的各种约束


/*
	虽然DBMS可以图形化操作数据库，但是作为开发人员至少要能看懂DBMS生成的脚本语句从而判断其有无不妥之处
*/