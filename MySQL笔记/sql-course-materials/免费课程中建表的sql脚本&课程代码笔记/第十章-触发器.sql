-- 查看、删除、修改事件
SHOW EVENTS LIKE 'yearly%';
DROP EVENT IF EXISTS yearly_delete_stale_audit_rows;
ALTER EVENT yearly_delete_stale_audit_rows DISABLE;	-- 当然也可以用ENABLE来启用事件


-- 事件events
show variables LIKE 'event%';
SET GLOBAL event_scheduler = ON;	-- 当然也可以设为OFF关闭

-- 创建一个事件event
DELIMITER $$
CREATE EVENT yearly_delete_stale_audit_rows
ON SCHEDULE
	-- AT '2019-05-01'	-- 只执行一次的事件
    EVERY 1 YEAR STARTS '2019-01-01' ENDS '2030-01-01'
DO BEGIN
	DELETE FROM payments_audit
    WHERE action_date < NOW() - INTERVAL 1 YEAR;
END $$
DELIMITER ;

-- 使用触发器进行审计
-- 详细见文件:第十章-Trigger-payment_after_delete.sql
/*
	使用触发器记录下是谁在什么时候做了什么，(类似于创建日志)
*/
INSERT INTO payments	-- 测试一下触发器
VALUES (DEFAULT , 5 , 3 , '2019-01-01' , 10 , 1)
;

DELETE
FROM payments
WHERE payment_id = 10;


-- 删除触发器
DROP TRIGGER IF EXISTS payment_after_delete;
/*
	和创建表和视图一样，建议将创建和删除语句放在同一个sql脚本文件中，便于和其他人使用
*/


-- 查看触发器
SHOW TRIGGERS;
SHOW TRIGGERS LIKE 'payment%';
/*
	显示当前数据库的触发器
    这里告诉我们，触发器的命名要规范
*/

-- 练习 触发器
DELIMITER $$
CREATE TRIGGER payment_after_delete
	AFTER DELETE ON payments
	FOR EACH ROW
BEGIN
	UPDATE invoices
	SET payment_total = payment_total - OLD.amount
    WHERE invoice_id = OLD.invoice_id;
END $$
DELIMITER ;

DELETE 
FROM payments
WHERE payment_id = 9
;

-- 触发器
DELIMITER $$

CREATE TRIGGER payment_after_insert
	AFTER INSERT ON payments
	FOR EACH ROW
BEGIN
	UPDATE invoices
	SET payment_total = payment_total + NEW.amount
    WHERE invoice_id = NEW.invoice_id;
END $$
DELIMITER ;

INSERT INTO payments	-- 测试一下触发器
VALUES (DEFAULT , 5 , 3 , '2019-01-01' , 10 , 1)
;
/*
	仅对表有效(对视图、临时表无效)
    触发器是对表而言的，且每个表最多关联6个触发器(INSERT、UPDATE、DELETE  * 执行前/执行后触发)
    最好在每个数据库触发器名称唯一(MYSQL5支持每一个表内触发器名称唯一)
    
    NEW关键字用于INSERT新记录，OLD用于UPDATE、DELETE的旧记录
*/