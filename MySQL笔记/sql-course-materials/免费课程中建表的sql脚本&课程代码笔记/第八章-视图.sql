-- WITH CHECK OPTION 子句
CREATE OR REPLACE VIEW invoices_with_balance_test AS
SELECT 
	invoice_id,
    number,
    client_id,
    invoice_total,
    payment_total,
    invoice_total - payment_total AS balance,
    invoice_date,
    due_date,
    payment_date
FROM invoices
WHERE (invoice_total - payment_total) > 0
WITH CHECK OPTION 
;



-- 可更新视图
CREATE OR REPLACE VIEW invoices_with_balance AS
SELECT 
	invoice_id,
    number,
    client_id,
    invoice_total,
    payment_total,
    invoice_total - payment_total AS balance,
    invoice_date,
    due_date,
    payment_date
FROM invoices
WHERE (invoice_total - payment_total) > 0
-- HAVING balance > 0	-- 这么写就不能通过VIEW进行更新和删除操作，它不是可更新视图
;

DELETE FROM invoices_with_balance
WHERE invoice_id = 1;	
-- 通过这个可更新视图，执行该删除操作会导致
-- VIEW invoices_with_balance中invoice_id = 1的行被删除
-- 同时invoices中invoice_id = 1的行也会被删除
/*
	简单来说可更新视图可以对视图表进行UPDATE、INSERT、DELETE的视图
	可更新视图创建语句的SELECT中不能包含以下这些关键字
    DISTINCT
    聚合函数：MIN()，MAX()等
    GROUP BY / HIVING
    UNION
*/


-- 更改或删除视图
DROP VIEW clients_balance;	-- 方法一：删除视图再创建一次

CREATE OR REPLACE VIEW clients_balance AS -- 方法二：在创建视图的代码中加上“OR REPLACE”，再次执行该代码
SELECT 
	client_id,
    name,
    SUM(i.invoice_total - i.payment_total) AS balance
FROM clients c
JOIN invoices i USING (client_id)
GROUP BY client_id , name
;
/*
	当发现视图出错要进行修改可以采用第二种方法
    最好把创建VIEW的代码另存为同名的SQL文件，并放入git便于版本控制
*/

-- 练习 创建视图
CREATE VIEW clients_balance AS
SELECT 
	client_id,
    name,
    SUM(i.invoice_total - i.payment_total) AS balance
FROM clients c
JOIN invoices i USING (client_id)
GROUP BY client_id , name
;


-- 创建视图
USE sql_invoicing;

CREATE VIEW sales_by_client AS
SELECT 
	c.client_id,
    c.name,
    SUM(payment_total) AS total_sales
FROM clients c
JOIN invoices i USING (client_id)
GROUP BY client_id , name
;
/*
	视图中的内容是根据SELECT中语句进行改变的，SELECT中的表叫基表
    视图的使用和普通表一样，WHERE，JOIN，GROUP BY这些操作都可以
    使用视图确保数据安全，提高查询效率
*/