-- 维护索引
/*
	索引可以大大加快查询的速度，但是要注意重复索引和冗余索引的问题
	重复索引：mysql并不会阻止你创建两个一摸一样的索引(只要这两个索引名称不同就可以成功创建)
	冗余索引：冗余索引指，已有索引(A,B)再创建索引(A)那这个新索引(A)就是冗余没必要的索引
			但若是已有索引(A,B),再创建索引(B)或者(B,A)那么这俩新建索引就不算冗余
	永远记住：创建索引前先查看已有索引，查看已有的索引是否可以直接使用
*/


-- 覆盖索引
/*
	其含义就是当你select语句中所有列都包含在摸一个索引中，那么此次查询就很快
    因为它不需要进行读表操作
    注意：每一个索引都暗含了主键这一列，比如前面的idx_state 其实际上是(state , customer_id)这两列的索引
*/


-- 使用索引排序
SHOW INDEX IN customers;
DROP INDEX idx_state_points_2 ON customers;
CREATE INDEX idx_state_points_2 ON customers (state ,points);
EXPLAIN SELECT customer_id FROM customers ORDER BY state;
SHOW STATUS LIKE 'last_query_cost';	-- 和名字一样，这个系统变量可以查看上次查询花费的代价


/*
	当对列建立索引时，mysql会获取该列所有值，对其排序，并存放在索引中
    所以当设计到order by的语句中要尽可能的使用索引
*/

-- 当索引失效时



-- 复合索引中列的顺序
SELECT *
FROM customers
USE INDEX (idx_state_points)	-- 可以这样指定使用哪一个索引
WHERE state LIKE 'A%' AND points > 1000;
/*
	两条准则：
		1.使用更频繁的列放在前面
		2.把基数(Cardinality)更大的列放在前面，基数指列中索引唯一值的个数
			比如性别一栏，只有男、女 故基数为2，索引并不能很好的筛选数据加速搜索
		但是！！！这两条也并不都是最佳策略，具体怎么设计索引应该结合查询语句
*/

-- 复合索引
SHOW INDEX IN customers;
CREATE INDEX idx_state ON customers (state);

explain SELECT * FROM customers WHERE state = 'CA' AND points > 1000;
CREATE INDEX idx_state_points ON customers (state , points);

DROP INDEX idx_state_points ON customers;
/*
	mysql最多支持16个列复合索引，但是实际工作中应该以数据量来设计索引列数
*/

-- 全文索引
USE sql_blog;
CREATE FULLTEXT INDEX idx_title_body ON posts (title , body);

SELECT *
FROM posts
WHERE MATCH(title , body)	-- 从这两列中进行匹配
-- 	AGAINST('react redux')	-- 包含react或者redux的
	AGAINST('react +redux' in boolean mode)	-- 指必须包含redux这个单词
    
;

-- 前缀索引	为长字符串创建索引
CREATE INDEX idx_lastname ON customers (last_name(20));	-- 这里的20应该是依据表中数据而确定的参数

SELECT 
	COUNT(*),
	COUNT(DISTINCT LEFT(last_name , 1)),
	COUNT(DISTINCT LEFT(last_name , 5)),
	COUNT(DISTINCT LEFT(last_name , 10))
FROM customers;
/*
	当列里面是较短的字符串可建可不建前缀索引，因为用普通的索引也可
	若是很长的字符串，比如blob类型那就必须建前缀索引
    前缀索引的长度可以用上面这种查询语句判断索引能否区分大部分的数据，总数据1011条，而5个字符前缀就可以划区分大部分的数据
*/


-- 查看索引
SHOW INDEX IN customers;
ANALYZE TABLE customers;
/*
	Cardinality显示的数据只是一个概数，可能不是数据库实际的数目
	ANALYZE TABLE customers;这一句就是重新统计customers表的情况
*/


-- 创建索引
EXPLAIN SELECT first_name FROM customers WHERE points > 300;
CREATE INDEX idx_points ON customers (points);
EXPLAIN SELECT points FROM customers WHERE points > 500;
-- explain关键字可以输出mysql进行查询方式的各种信息，比如rows就是要扫描的记录的数目


/*
	mysql索引类似于文件系统中的索引
    Mosh提醒：不要在建表的时候就创建索引，因为索引是为了提高查询速度而创建的，
		建表时就创建索引就像解决一个不存在的问题。要为了select而创建索引
*/