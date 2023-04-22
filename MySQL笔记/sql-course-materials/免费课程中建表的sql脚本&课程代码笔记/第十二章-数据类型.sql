-- 获取JSON类型中的键值对数据
SELECT 
	product_id,
    JSON_EXTRACT(properties,'$.weight') AS weight
FROM products
WHERE product_id = 1
;
/*
	$.weight是一个路径,其中$表示当前位置(即函数中第一个参数的对象properties)
*/

-- 使用函数更新JSON类型数据
UPDATE products
SET properties = JSON_OBJECT(
	'weight',10,
    'dimensions',JSON_ARRAY(1,2,3),
    'manufacturer',JSON_OBJECT('name','sony')
)
WHERE product_id = 1
;



-- 手动更新JSON类型数据
UPDATE products
SET properties = '
{
	"dimensions":[1,2,3],
    "weight":10,
    "manufacturer":{"name":"sony"}
}
'
WHERE product_id = 2
;


/*
关于枚举类型ENUM
	mysql支持该类型，但是不建议使用，一旦建立的表中包含这个类型，未来某一天要添加新类型，唯一的办法就是重建整张表，这是一项耗费巨大的操作。
	推荐的做法是建一张新表，比如sql_store中的shippers表，未来要是增加一个新的运输方式操作起来很简单，查询时也只需一个联表查询即可

关于BLOB类型
	一般来说不要把文件放入数据库中，因为数据库对文件的操作不如文件系统快速
	同时会有以下问题：
		数据库内容变多
		备份功能弱化
		数据库性能下降
		同时图片等文件放在数据库中取用还要编写特定的代码
*/