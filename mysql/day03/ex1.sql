-- Day03作业：
-- 综述：两张表，一张顾客信息表customers，一张订单表orders
-- 1、创建一张顾客信息表customers，字段要求如下：
-- 	c_id 类型为整型，设置为主键，并设置为自增长属性
-- 	c_name 字符类型，变长，宽度为20
-- 	c_age 微小整型，取值范围为0~255(无符号)
-- 	c_sex 枚举类型，要求只能在('M','F')中选择一个值
-- 	c_city 字符类型，变长，宽度为20
-- 	c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
-- 	在表中任意插入3条记录,c_name为"Zhangsan","Lisi","Wangwu", c_city尽量	写"Beijing","Shanghai" ......

use day03;
create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint,
c_sex enum('M','F'),
c_city varchar(20),
c_salary float(12,2));

insert into customers(c_name,c_age,c_sex,c_city,c_salary) values
-- ('Zhangsan','18','M','Beijing','10000'),
-- ('Lisi','19','F','Beijing','10000.89'),
-- ('Wangwu','17','M','Beijing','12000.5'),
('Lissss','31','F','Shanghai','10000.89');

-- 
-- 2、创建一张订单表orders，字段要求如下：
-- 	o_id 整型
-- 	o_name 字符类型，变长，宽度为30
-- 	o_price 浮点类型，整数最大为10位，小数部分为2位
-- 	设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
-- 	在表中任意插入5条记录(注意外键限制)
-- 	o_name分别为"iphone","ipad","iwatch","mate9","r11",其他信息自己定
--
select * from customers; 
create table orders(
o_id int,
o_name varchar(30),
o_price float(12,2),
foreign key(o_id) 
references customers(c_id)
on delete cascade
on update cascade);

insert into orders values
(1,'iphone','5999.5'),
(1,'ipad','7999.5'),
(1,'iwatch','2999.5'),
(1,'mate9','1999.5'),
(1,'r11','2000');
-- 3、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
select * from customers 
where c_salary >4000 or c_age < 29
limit 2;
-- 4、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
select c_name,c_age,c_salary*1.15 from customers
where c_age >=25 and c_city in ('Beijing','Shanghai');			
-- 5、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
select * from customers 
where c_city = 'Beijing' 
order by c_salary desc
limit 1;		
-- 6、选择工资salary最少的顾客的信息
select * from customers
order by c_salary
limit 1;			
-- 7、找到工资大于5000的顾客都买过哪些产品的记录明细
select customers.c_name,orders.o_name,orders.o_price from customers
inner join orders on customers.c_id = orders.o_id;				
-- 8、删除外键限制
show create table orders;
alter table orders drop foreign key	orders_ibfk_1;
			
-- 9、删除customers主键限制
alter table customers modify c_id int;
alter table customers drop primary key;
show create table customers;