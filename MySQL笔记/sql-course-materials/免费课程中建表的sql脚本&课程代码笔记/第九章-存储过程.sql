-- 函数


/*
	函数和存储过程的一大区别就是：函数之只能返回单一的值，而存储过程可以返回结果集(也就是一个表)
*/



-- 变量
SET @invoices_count = 0;
/*
	这句话就相当于java的：int invoices_count = 0;
    这种申明变量称为：“用户变量”、“会话变量”
    其生命周期为一个会话
    
    mysql中还一种变量叫本地变量
*/
DELIMITER $$
CREATE PROCEDURE get_risk_factor()
BEGIN
	DECLARE risk_factor DECIMAL(9,2) DEFAULT 0;
    DECLARE invoices_total DECIMAL(9,2);
    DECLARE invoices_count INT;
    
    SELECT COUNT(*), SUM(invoice_total)
    INTO invoices_count , invoices_total
    FROM invoices;
    
    SET risk_factor = invoices_total / invoices_count * 5 ;
    
    SELECT risk_factor;
 END $$
 DELIMITER ;
/*
	本地变量的定义和使用示例
*/

-- 输出参数
DROP PROCEDURE IF EXISTS get_unpaid_invoices_for_client;

DELIMITER $$
CREATE PROCEDURE get_unpaid_invoices_for_client
(
	client_id INT,
    OUT invoices_count INT,
    OUT invoices_total DECIMAL(9,2)
) 
BEGIN
	SELECT 
		COUNT(*),
        SUM(invoice_total)
	INTO 
		invoices_count,
        invoices_total
	FROM invoices i
    WHERE i.client_id = client_id
		AND payment_total = 0;
END$$
DELIMITER ;
/*
这段存储过程执行会被翻译成下面语句
	set @invoices_count = 0;	-- mysql中变量必须以"@"开头
	set @invoices_total = 0;
	call sql_invoicing.get_unpaid_invoices_for_client(2, @invoices_count, @invoices_total);
	select @invoices_count, @invoices_total;
    默认参数类型都是IN，设定为输出参数则需显示的加上OUT关键字
	查询的结果通过INTO赋值给指定的变量，也因如此查询的结果不能是一个集合，只能是某确定的值才能赋给变量
    
	按照Mosh的说法，这玩意儿不到万不得已不推荐使用
*/


-- 存储过程参数验证
DELIMITER $$
CREATE PROCEDURE make_payment
(
	invoice_id INT,
    payment_amount DECIMAL(9,2),	-- 表示这个参数是一个两位小数
    payment_date DATE
)
BEGIN
	IF payment_amount <= 0 THEN
		SIGNAL SQLSTATE '22003'		-- 这个'22003'报错编码不是乱取的，可以Google关键词：“sqlstate errors”进行查找
			SET MESSAGE_TEXT = 'Invalid payment amount';
	END IF
    ;
    
    UPDATE invoices i
    SET
		i.payment_total = payment_amount,
        i.payment_date = payment_date
	WHERE i.invoice_id = invoice_id
    ;
    
END $$
DELIMITER ;
/*
	之前所学的存储过程仅包含SELECT语句，这不会对原始表产生任何影响
    但是存储过程同样可以包含“增删改”的操作，这就可能导致原始表中出现不合理的数据
    故需要对参数进行判断，判断的手法就是在“增删改”的语句前加一个进行判断的语句
	判断语句可以产生对应的报错编码和具体介绍(有点类似抛出异常)	
    
    注意：虽然可以使用sql语句检查参数，但是这样代价很大，参数的检查和处理应该放在应用层处理，比如表单的筛选，再不济在业务层代码中处理也好过使用sql处理
*/

-- 练习 存储过程默认参数
DELIMITER $$
CREATE PROCEDURE get_payments(
	client_id INT,
    payment_method_id TINYINT
)
BEGIN
	SELECT *
    FROM payments p
    WHERE 
		p.client_id = IFNULL(client_id , p.client_id) AND
        p.payment_method = IFNULL(payment_method_id , p.payment_method)
	;
END
DELIMITER ;

CALL get_payments(1,NULL);
/*
	要实现默认参数还有很多种方法，此处使用的时IFNULL()函数
    还可以用“IF THEN ELSE”关键字等方法
*/


-- 存储过程添加参数
DROP PROCEDURE IF EXISTS get_client_by_state;

DELIMITER $$
CREATE PROCEDURE get_client_by_state
(
	state CHAR(2)
)
BEGIN
	SELECT *
    FROM clients c
    WHERE c.state = state;	-- 这里为了区分参数和表中列名给表取了别名，当然也可以使用其它方法，比如参数名改为p_state（加一个前缀）
END $$
DELIMITER ;

CALL get_client_by_state('CA');	
/*
	使用该存储过程按照上面的创建方法，调用时参数是必填的，否则会报错
    且参数如果格式不对也会报错
*/

-- 删除存储过程
DROP PROCEDURE get_clients_2;
DROP PROCEDURE IF EXISTS get_clients_2;	-- 为了防止报错，这是更好的写法


-- 练习 创建存储过程
USE sql_store;
DELIMITER $$
CREATE PROCEDURE get_invoices_with_balance()
BEGIN
	SELECT *
    FROM invoices
    WHERE invoice_date - payment_total > 0;
END $$
DELIMITER ;
/*
	之前学过，视图和基础表的用法基本一样，故创建存储过程中的SQL语句也可以在视图中进行查找
*/

-- 创建存储过程
DELIMITER $$
CREATE PROCEDURE get_clients_2()
BEGIN
	SELECT * FROM clients;
    SELECT * FROM invoices;
END$$
DELIMITER ;
/*
	BEGIN END 中间包含的是函数体body，函数体中可以包含多个SQL语句，但每一句都要以;结尾
    DELIMITER 是修改分隔符，用以表示这一坨代码是一个整体
    存储过程的一个作用就是讲SQL与其它语言（如JAVA）分离开来，相当于给JAVA定义了一个接口
	当然，创建存储过程也可以直接在workbench左侧SCHEMAS栏中右键单击Stored Procedures进行创建
*/

CALL get_clients;	-- SQL语句调用存储过程