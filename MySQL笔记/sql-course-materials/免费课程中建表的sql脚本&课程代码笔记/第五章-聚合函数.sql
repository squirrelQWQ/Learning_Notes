-- rollup练习
SELECT
	pm.name AS payment_method,
    SUM(amount) AS total
FROM payments p
JOIN payment_methods pm
	ON p.payment_method = pm. payment_method_id
GROUP BY pm.name WITH ROLLUP
;
-- GROUP BY payment_method WITH ROLLUP -- 这么写是错的,使用ROLLUP就不能用别名GROUP BY


-- rollup
SELECT
	state,
    city,
	SUM(invoice_total) AS total_sales
FROM invoices i
JOIN clients c USING(client_id)
GROUP BY state , city WITH ROLLUP
;
-- rollup会对每一个分组以及所有分组都做一次汇总
-- rollup是mysql特有的关键字，oracle和SQL server都没有这语句


-- 练习having
USE sql_store;

SELECT 
	c.customer_id,
    c.first_name,
    c.last_name,
    SUM(oi.quantity * oi.unit_price) AS total_sales
FROM customers c
JOIN orders o USING(customer_id)
JOIN order_items oi USING(order_id)
WHERE state = 'VA'
GROUP BY
	c.customer_id,
    c.first_name,
    c.last_name
HAVING total_sales > 100
;




-- HAVING语句
SELECT 
	client_id,
    SUM(invoice_total) AS total_sales,
    COUNT(*) AS number_of_invoices
FROM invoices
-- WHERE total_sales > 500 -- 很遗憾这么写会报错，where用在分组前的筛选
-- where不可以使用AS后面取的新列名
GROUP BY client_id
HAVING total_sales > 500 AND number_of_invoices > 5
;
-- having语句用在分组后的筛选（即可以由组为单位进行筛选）
-- having可以使用AS后面取的新列名
-- 根本原因在于having是对查询结果表的进一步筛选，where是对原始表的筛选





-- 练习
SELECT 
	date,
    pm.name,
    SUM(amount) AS total_payment
FROM payments p
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
GROUP BY date, nameamount
ORDER BY date
;




SELECT
	state,
    city,
	SUM(invoice_total) AS total_sales
FROM invoices i
JOIN clients USING(client_id)
GROUP BY state , city
ORDER BY total_sales DESC    
;




SELECT
	client_id,
    SUM(invoice_total) AS total_sales
FROM invoices
WHERE invoice_date >= '2019-07-01' 
GROUP BY client_id
ORDER BY total_sales DESC
;




-- 聚合函数示例
SELECT 
	'First half of 2019' AS date_range,
    SUM(invoice_total) AS total_sales,
    SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-01-01' AND '2019-06-30'
 UNION
 SELECT 
	'Secend half of 2019' AS date_range,
    SUM(invoice_total) AS total_sales,
    SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-07-01' AND '2019-12-31'
UNION
SELECT 
	'Total' AS date_range,
    SUM(invoice_total) AS total_sales,
    SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-01-01' AND '2019-12-31'
;


SELECT
	MAX(payment_date),
    MIN(invoice_total) AS min_invoice_total,
    AVG(payment_total) AS average,
    SUM(invoice_total) AS total,
    COUNT(invoice_total) AS number_of_incoices,
    COUNT(payment_date) AS count_of_payments,
    COUNT(*) AS total_records,
    COUNT(DISTINCT client_id) AS number_of_client
FROM invoices
WHERE invoice_date > '2019-07-01'
;