-- FROM子句中的子查询
SELECT *
FROM (
	SELECT
		client_id,
		name,
		(SELECT SUM(invoice_total)
			FROM invoices
			WHERE client_id = c.client_id) AS total_sales,
		(SELECT AVG(invoice_total)
			FROM invoices) AS average,
		(SELECT total_sales - average) AS difference
	FROM clients c
) AS sales_summary
WHERE total_sales IS NOT NULL
;
/*
	在FORM子句中虽然可以嵌套子查询，但是这样会使得主查询变得很复杂
    所以这种操作仅限于简单的查询
*/

-- 练习 SELECT子句中的子查询
SELECT
	client_id,
    name,
    (SELECT SUM(invoice_total)
		FROM invoices
        WHERE client_id = c.client_id) AS total_sales,
	(SELECT AVG(invoice_total)
		FROM invoices) AS average,
	(SELECT total_sales - average) AS difference
FROM clients c
-- HAVING total_sales IS NOT NULL	-- 加上这句话就和FORM中的子查询效果一样
;


-- SELECT子句中的子查询
SELECT
	invoice_id,
    invoice_total,
    (	SELECT AVG(invoice_total)
		FROM invoices) AS invoice_average,
--         invoice_total - invoice_average 		-- 很遗憾，SELECT子句中的子查询不能使用别名
-- 		invoice_total - (	SELECT AVG(invoice_total)
-- 							FROM invoices)		-- 这是一种写法，就是把整个子查询在复制一份
		invoice_total - (SELECT invoice_average)-- 另一种写法，MOSH推荐
FROM invoices
;
/*
	在之前的学习中子查询都是在WHERE子句下的
    现在在SELECT子句中也可以嵌套子查询
	？？？不过为什么MOSH推荐的这种写法可以用别名？？？
*/

-- 练习 EXISTS
-- 查询从来没有被下单过的产品
USE sql_store;

SELECT *
FROM products p
WHERE NOT EXISTS (
	SELECT *
    FROM order_items
    WHERE p.product_id = product_id
)
;

-- EXISTS关键字
-- 查询所有有发票的用户
SELECT *		-- 方法一：使用IN关键字
FROM clients
WHERE client_id IN (
	SELECT DISTINCT client_id
    FROM invoices
)
;

SELECT *		-- 方法二：EXISTS配合相关子查询
FROM clients c
WHERE EXISTS (
	SELECT client_id
    FROM invoices
    WHERE client_id = c.client_id
)
;
/*
	方法一：使用IN关键字，其子查询会返回一张结果表
			如果子查询的结果很大，则会导致结果表很大造成效率降低
	方法二：使用EXISTS关键字其子查询不会返回一个表只进行一个判断结果
			即，子查询是否能查询出结果，其效率可能比方法一更高
*/

-- 练习 相关子查询
USE sql_invoicing;
-- 客户可能有多个发票，查找客户发票中比自己所有发票平均值高的发票
SELECT *
FROM invoices i
WHERE invoice_total > (				-- 找出比平均值高的发票
	SELECT AVG(invoice_total)		-- 计算自己所有发票的平均值
    FROM invoices
    WHERE client_id = i.client_id	-- 自己的所有发票
)
;

-- 相关子查询
USE sql_hr;
SELECT *
FROM employees e
WHERE salary > (
	SELECT AVG(salary)
    FROM employees
    WHERE office_id = e.office_id
)
;
/*
	由于子查询里面使用到了e.office_id，相当于使用到了外层的表
    所以实际执行时会对每一个 e表中的行进行一次子查询（类似一个for循环）
    故实际执行的效率很低
    
    之前使用的子查询都不是相关子查询，其子查询在整个查询过程中只进行一次
*/

-- ANY关键字, “IN” 等价于 “= ANY”
SELECT *
FROM clients
WHERE client_id = ANY (
	SELECT client_id
	FROM invoices
	GROUP BY client_id
	HAVING COUNT(*) >= 2
)
;



-- ALL关键字
SELECT *
FROM invoices
WHERE invoice_total > ALL(		-- 子查询返回的是一系列值，使用ALL，也就是invoice_total要大于所有的这一系列值
	SELECT invoice_total
    FROM invoices
    WHERE client_id = 3
)
;

SELECT *
FROM invoices
WHERE invoice_total > (		-- 子查询返回的是一个单独的值MAX(invoice_total)
	SELECT MAX(invoice_total)
    FROM invoices
    WHERE client_id = 3
)
;


-- 练习，IN
USE sql_invoicing;

SELECT *		-- 写法一：可读性好，但是有时过多的子查询会导致整个SQL语句很乱
FROM clients
WHERE client_id NOT IN(	
	SELECT DISTINCT client_id
    FROM invoices
)
;

SELECT *		-- 写法二，
FROM clients
LEFT JOIN invoices USING(client_id)
WHERE invoice_id IS NULL
;

-- 练习，子查询
USE sql_hr;

SELECT *
FROM employees
-- WHERE salary > AVG(salary) -- 错误写法
WHERE salary > (
	SELECT AVG(salary)
    FROM employees
)
;

-- 子查询

USE sql_store;
SELECT *
FROM products
WHERE unit_price > (
	SELECT unit_price
    FROM products
    WHERE product_id = 3
)
;