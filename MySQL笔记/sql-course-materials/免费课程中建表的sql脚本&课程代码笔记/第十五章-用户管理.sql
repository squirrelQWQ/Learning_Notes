-- 查看权限
SHOW GRANTS FOR moon_app@localhost;
SHOW GRANTS FOR moon_app;		-- 创建用户时指定了连接方式，在其它所有地方用到该用户名都要加上连接方式才行


-- 用户权限
-- 1. web/desktop application
CREATE USER moon_app@localhost IDENTIFIED BY '1234';

GRANT SELECT,INSERT,UPDATE,DELETE,EXECUTE
ON sql_store.*
TO moon_app@localhost;
-- 2. admin
GRANT ALL
ON *.*	-- 对所有数据库和所有表适用
TO john;
/*
	以上只是几个常用权限，更多权限google：mysql privilege
*/


-- 删除用户
CREATE USER Bob@bilibili.com IDENTIFIED BY '1234';
DROP USER Bob@bilibili.com;



-- 查看用户
SELECT * FROM mysql.user;


-- 创建用户
CREATE USER john@172.0.0.1;
CREATE USER john@localhost;
CREATE USER john@bilibili.com;
-- 用户名为john，@后面的表示限制用户连接方式
CREATE USER john@'%.bilibili.com';	-- 使用通配符，表示可以在该域名的所有子域连接数据库
CREATE USER john IDENTIFIED BY 'password';	-- 用户连接不受任何限制,且密码为：password