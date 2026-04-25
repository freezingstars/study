# MySQL 基础

## 基础操作
- **选中数据库**  
`USE database_name;`

- **设置编码格式**  
`SET character_set_name utf8;`
MySQL 对大小写不敏感，SQL 语句末尾通常以分号 ; 结束。

## 数据库操作

### 数据操作
- **SELECT** — 从数据库中提取数据  
```
SELECT column_name1, column_name2, ...
FROM table_name
WHERE condition
ORDER BY column_name [ASC|DESC];
```
- **UPDATE** — 更新数据  
```
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```
- **DELETE** — 删除数据  
```
DELETE FROM table_name
WHERE condition;
```
- **INSERT INTO** — 插入数据  
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```
### 数据库管理
- **CREATE DATABASE** — 创建新数据库  
- **ALTER DATABASE** — 修改数据库  

### 表操作
- **CREATE TABLE** — 创建表  
```
CREATE TABLE table_name (
    column1 data_type constraint,  -- 例：PRIMARY KEY、NOT NULL
    column2 data_type constraint
);
```
- **ALTER TABLE** — 修改表结构  
```
ALTER TABLE table_name ADD column_name data_type;
```
- **DROP TABLE** — 删除表  

### 索引操作
- **CREATE INDEX** — 创建索引  
```
CREATE INDEX index_name
ON table_name (column_name);
```
- **DROP INDEX** — 删除索引  

### 结果操作
- **ORDER BY** — 排序  
- **GROUP BY** — 分组  
- **HAVING** — 分组筛选  
- **JOIN** — 联表查询  
- **DISTINCT** — 去重  

## 查询
### 去重查询
DISTINCT 用于返回唯一值：
```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```
示例：
```
USE test;

DROP TABLE IF EXISTS websites;

CREATE TABLE websites (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    url VARCHAR(255),
    alexa INT,
    country VARCHAR(10)
);

INSERT INTO websites (id, name, url, alexa, country) VALUES
(1, 'Google', 'https://www.google.com/', 1, 'USA'),
(2, 'YouTube', 'https://www.youtube.com/', 2, 'USA'),
(3, 'Facebook', 'https://www.facebook.com/', 3, 'USA'),
(4, '百度', 'https://www.baidu.com/', 6, 'CN'),
(5, '新浪微博', 'https://weibo.com/', 20, 'CN'),
(6, '淘宝', 'https://www.taobao.com/', 13, 'CN'),
(7, 'Amazon', 'https://www.amazon.com/', 10, 'USA'),
(8, 'Wikipedia', 'https://www.wikipedia.org/', 7, 'USA'),
(9, 'Instagram', 'https://www.instagram.com/', 5, 'USA'),
(10, 'Twitter', 'https://twitter.com/', 12, 'USA'),
(11, 'TikTok', 'https://www.tiktok.com/', 15, 'CN'),
(12, 'Bilibili', 'https://www.bilibili.com/', 64, 'CN'),
(13, '菜鸟教程', 'https://www.runoob.com/', 4689, 'CN'),
(14, '腾讯网', 'https://www.qq.com/', 9, 'CN'),
(15, '网易', 'https://www.163.com/', 55, 'CN'),
(16, 'StackOverflow', 'https://stackoverflow.com/', 45, 'USA'),
(17, 'Reddit', 'https://www.reddit.com/', 18, 'USA'),
(18, 'GitHub', 'https://github.com/', 21, 'USA'),
(19, 'LinkedIn', 'https://www.linkedin.com/', 23, 'USA'),
(20, 'Microsoft', 'https://www.microsoft.com/', 27, 'USA');

SELECT DISTINCT country FROM websites;
```
### 条件查询
```
SELECT url FROM websites WHERE name = "Bilibili";
```

| 运算符     | 描述                        |
| ------- | ------------------------- |
| =       | 等于                        |
| <>      | 不等于。注：在 SQL 的一些版本中，可写成 != |
| >       | 大于                        |
| <       | 小于                        |
| >=      | 大于等于                      |
| <=      | 小于等于                      |
| BETWEEN | 在某个范围内                    |
| LIKE    | 搜索某种模式                    |
| IN      | 指定某列的多个可能值                |

WHERE 子句不一定带比较运算符，当不带运算符时会执行隐式转换：0 转为 false，1 转为 true。

示例：
`SELECT name FROM websites WHERE url <> "%com";`

### 聚合查询
常见聚合函数：

| 函数  | 功能   |
| ----- | ---- |
| count | 统计数量 |
| max   | 最大值  |
| min   | 最小值  |
| avg   | 平均值  |
| sum   | 求和   |

语法：
`SELECT aggregate_function(column_name) FROM table_name;`
例:
```
SELECT COUNT(name) FROM websites;
SELECT name,min(alexa) FROM websites;
```
### 分组查询
语法:
`SELECT column_name FROM table_name [WHERE condition] GROUP BY group_name [HAVING condition];`
having是分组之后对结果进行过滤，where不能对聚合函数进行判断，但是having可以;简：where过程前过滤，having结果过滤
例：
```
SELECT country,avg(alexa) FROM websites GROUP BY country;
SELECT country,avg(alexa) FROM websites WHERE alexa < 100 GROUP BY country;
SELECT country,avg(alexa) FROM websites WHERE alexa < 100 GROUP BY country HAVING avg(alexa) > 20;
```
`GROUP BY` 会把查询结果按照指定列进行 **分组**。这里用的是 `country` 列，所以数据库会把所有相同 `country` 的行 **归为一组**

### 排序查询
语法`SELECT column_name FROM table_name [WHERE condition] [GROUP BY group_name] [HAVING condition] ORDER BY column_name1,column_name2 ASC|DESC;`
ASC|DESC，升|降序。如果是多字段排序，当第一个字段值相同时才会根据第二个字段进行排序
例：
```
SELECT * FROM websites;
SELECT name,alexa,country FROM websites ORDER BY country DESC,alexa ASC;
```

### 分页查询
`SELECT column_name FROM table_name LIMIT init_index,RecordCount;`
起始索引从0开始，等于(查询页码-1)\*每页显示的记录数
分页查询是数据库的方言，不同的数据库有不用的实现方式，MySQL中是LIMIT，如果查询的是第一页数据，可以省略起始索引简写为LIMIT 10
```
SELECT * FROM websites LIMIT 10;
SELECT * FROM websites LIMIT 10,10;
```
可以认为是在步长为1的情况下(起始索引值,显示几个值)
## 通配符

| 通配符     | 作用        |
| ------- | --------- |
| *       | 所有        |
| %       | 选中0或多个字符  |
| _       | 替代一个字符    |
| [char]  | 列表中任意一个字符 |
| [^char] | 列表字符反选    |
| [!char] | 同上        |

## 用户管理
`host`：指定用户可以从哪些主机连接。例如，`localhost` 仅允许本地连接，`%` 允许从任何主机连接。
查询用户：
```
USE mysql;
SELECT * FROM user; 
```
创建用户：
```
CREATE USER 'username'@'host' IDENTIFIED BY `password`;
```
修改用户密码：
```
ALTER USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY `password`;
```
删除用户：
```
DROP USER 'username'@'host';
```

### 权限控制
所有权限：`ALL, ALL PRIVILEGES`,其他的例如`SELECT,INSERT`等
查询权限：
```
SHOW GRANTS FOR 'username'@'host';
```
授予权限：
```
GRANT privileges_list ON database_name.table_name TO 'username'@'host';
```
撤销权限：
```
REVOKE privileges_list ON database_name.table_name FROM 'username'@'host';
```

## SQL语言分类
数据定义语言(DDL):
Data Definition Language，即数据定义语言，定义语言就是定义关系模式、删除关系、修改关系模式以及创建数据库中的各种对象，比如表、聚簇、索引、视图、函数、存储过程和触发器等等。
数据定义语言是由SQL语言集中负责数据结构定义与数据库对象定义的语言，并且由CREATE、ALTER、DROP和TRUNCATE四个语法组成。比如：

数据操纵语言(DML):
Data Manipulation Language，主要是进行插入元组、删除元组、修改元组的操作。主要有insert、update、delete语法组成。

数据查询语言(DQL):
Data Query Language，所以是用来进行数据库中数据的查询的，即最常用的select语句

数据控制语言(DCL):
Data Control Language。用来授权或回收访问数据库的某种特权，并控制数据库操纵事务发生的时间及效果，能够对数据库进行监视。比如常见的授权、取消授权、回滚、提交等等操作。

# 进阶1
## 函数
### 字符串
Mysql内置了一些字符串函数，常用的有：

| 函数                       | 功能                     |
| ------------------------ | ---------------------- |
| CONCAT(S1,S2,...)        | 字符串拼接                  |
| LOWER(str)               | 转小写                    |
| UPPER(str)               | 转大写                    |
| LPAD(str,n,pad)          | 以字符串pad对str进行左填充，达到n长度 |
| RPAD(str,n,pad)          | 以字符串pad对str进行右填充，达到n长度 |
| TRIM(str)                | 去首尾空格                  |
| SUBSTRING(str,start,len) | 返回str从start位置起len长度个字符 |
insert(str,x,y)
## 数值

| 函数         | 功能                |
| ---------- | ----------------- |
| CEIL(x)    | 向上取整              |
| FLOOR(x)   | 向下取整              |
| MOD(x,y)   | 返回x/y的模           |
| RAND()     | 返回0~1的随机数         |
| ROUND(x,y) | 求参数x四舍五入的值，保留y位小数 |
例如生成一个六位随机数：
`SELECT LPAD(ROUND(rand()*1000000, 0), 6, '0');`

## 日期

| 函数                                | 功能                        |
| --------------------------------- | ------------------------- |
| CURDATE()                         | 返回当前日期                    |
| CURTIME()                         | 返回当前时间                    |
| NOW()                             | 返回当前时间和日期                 |
| YEAR(date)                        | 获取指定date的年份               |
| MONTH(date)                       | 获取月份                      |
| DAY(date)                         | 获取日期                      |
| DATE_ADD(date,INTERVAL expr type) | 返回日期/时间值加速一个时间间隔expr后的时间值 |
| DATEDIFF(date1, date2)            | 返回两个时间之间的天数               |
例：
后推70月
`SELECT DATE_ADD(now(), INTERVAL 70 MONTH);`
计算日期差
`SELECT DATEDIFF(NOW(), '2003-02-26');`
`SELECT name as '网站',alexa as '访问量' FROM websites ORDER BY alexa ASC;`
日期的字符串是可以作为查询条件的，例如查询`'2003-02-26'`之后的日期，就可以写为`where date > '2003-02-26'`

## 流程函数

| 函数                                                         | 功能                                   |
| ---------------------------------------------------------- | ------------------------------------ |
| IF(value,t,f)                                              | value为true返回t，反f                     |
| IFNULL(value1,value2)                                      | value1不为空返回value1，反2                 |
| CASE WHEN [val1] THEN [res1] ... ELSE [default] END        | 如果val1为true,返回res1，否则返回默认值           |
| case [expr] when [val1] THEN [res1] ... ELSE [default] END | 如果expr的值等于val1，返回res1，否则返回default默认值 |
'' <> null,即使是`''`也是有意义的空字符串

## 约束

| 关键字            | 功能                        |
| -------------- | ------------------------- |
| NOT NULL       | 非空                        |
| UNIQUE         | 唯一                        |
| PRIMARY KEY    | 主键（非空且唯一）                 |
| DEFAULT        | 默认                        |
| CHECK          | 检查（满足某个条件）                |
| FOREIGN KEY    | 外键（方便两张表建立连接，保证数据一致性或完整性） |
| AUTO_INCREMENT | 自增                        |
`check`的用法：`age int comment '年龄' check (agr > 0 && age < 120)`

### 外键
外键用于建立父表/主表 与 子表/从表之间的关系，外键在的一方为子表/从表。
在建立关系前，两张表仅有逻辑关系，无实际关系。建立外键后，两张表就拥有实际关系，会被影响。
创建表时添加外键：
```
CREATE TABLE table_name(
	字段名 数据类型,
	...
	[CONSTRAINT] [外键名] FOREIGN KEY (外键字段名) REFERENCES 主表(主表列名),
)
```
对于已存在的表格：
`ALTER TABLE table_name ADD CONSTRAINT 外键名 FOREIGN KEY(外键字段名) REFERENCES 主表(主表列名)`
在子表外键被清除之前，不能直接删除父表的键。
删除外键关联`ALTER TABLE teble_name DROP FOREIGN KEY column_name`，只是没了关联，并不是直接删了这个字段

### 外键的约束

| 行为          | 说明                               |
| ----------- | -------------------------------- |
| NO ACTION   | 在父表中删除/更新时，首先检查该记录是否有对应外键，有则拒绝操作 |
| RESTRICT    | 同上                               |
| CASCADE     | 将对应的外键在子表中记录一并删除                 |
| SET NULL    | 有对应外键则设置为NULL（需表允许取NULL）         |
| SET DEFAULT | 父表有变动时，子表外键列设置成默认值               |
`ALTER TABLE table_name ADD CONSTRAINT 外键名 FOREIGN KEY(外键字段名) REFERENCES 主表(主表列名) ON UPDATE [action] ON DELETE [action]`,语法上差不多，但是多出了在更新时做什么，在删除时做什么

## 多表查询
多表关系主要围绕在：一对一，多对多，一对多
多对多的实现一般至少包含三个表，中间表用于中继关联。多表查询要注意防止笛卡尔积的产生。
### 连接查询
#### 内连接
相当于查询两表交集的部分数据，分为隐式与显式，隐式为常见的查询方式:
`SELECT colume_name FROM table_name1,table_name2 WHERE condition;`
显式内连接则为:
`SELECT column FROM table_name1 [INNER] JOIN table_name2 ON condition;`
对于选中具体的字段，使用`表名.字段名`的形式，例如`websites.url = websites_extra.url`,如果表名较长，可以用别名形式`表名 别名`，例如`websites w`,这样表websites的别名就成为了w，接下来可以直接`w.url`

`SELECT w.url, w.name, w.id FROM websites w INNER JOIN websites_extra we ON w.url = we.url;`


#### 外连接
- 左外连接：查询左表中所有数据以及俩表交集数据
`SELECT w.url,w.name,w.id FROM websites w left JOIN websites_extra we ON w.url = we.url;`
会有20条结果，会先返回符合条件的结果，然后再返回剩下的所有值
- 右外连接：右表所有+交集
`SELECT w.url,w.name,w.id FROM websites w right JOIN websites_extra we ON w.url = we.url;`
会有20条结果，13条为null，因为会返回右表中所有记录，而如果未与左表匹配上，则为null


#### 自连接
当前表与自身的连接查询，自连接必须使用表别名
`SELECT column_name FROM table name1,table name2 WHERE condition;`
给同一张表取两个不同的别名，但是上述这种实际上是自连接与内连接结合的结果，如果条件为满足则不被选取。

如果想要先展示满足条件者，再展示不满足者，则需要使用自连接+左连接的方式。一般用于查询上级对应关系，如果其中含有一个最高级，则最高级在第一种方式中会遗漏，因为上头没人了；所以使用自连接+左连接的方式把这个最高级一同展示出来。

#### 联合查询
union,union all
对于union查询，就是将多次查询的结果合并起来，形成一个新的查询结果集
```
查询语句1
UNION [ALL]
查询语句2;
```
对于联合查询，多张表的列数和字段类型需要保持一致
union会粗暴地**全部合并**，union则会对合并的数据进行**去重**

#### 子查询
SQL中嵌套SELECT语句，称为嵌套语句，又称子查询
`SELECT * FROM table1 WHERE COLUMN1 = (SELECT column1 FROM table2);`
子查询外部的语句可以是INSERT/UPDATE/DELETE/SELECT中的任何一个
根据子查询结果不同，分为：
	- 标量子查询
	- 列子查询
	- 行子查询
	- 表子查询
子查询的位置可以在SELECT/FROM/WHERE之后
通常将仅返回**单个值**的形式成为**标量子查询**，常用操作符为= <> < <= > >=
子查询返回一列(可以是多行)，这种子查询成为列子查询，常用操作符为IN、NOT IN、ANY、SOME(等同于ANY)、ALL（返回列表的所有值都必须满足）
ALL,ANY后跟随的主要是一个数组，例如`all (含int类型的表达式)`

