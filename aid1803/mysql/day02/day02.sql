create database db2;
use db2;
create table t1(
id int(3) zerofill);
insert into t1 value(1),(2),(3);
select * from t1;
insert into t1 value(8888);
#使用Where语句
select * from t1 where id = 2;

create database MOSHOU;
use MOSHOU;
create table hero(
id int,
name char(15),
sex enum("男","女"),
country char(10)
)default charset=utf8;
insert into hero values
(1,"曹操","男","魏国"),
(2,"小乔","女","吴国"),
(3,"诸葛亮","男","蜀国"),
(4,"貂蝉","女","东汉"),
(5,"赵子龙","男","蜀国"),
(6,"魏延","男","蜀国");

use MOSHOU;
create table sanguo(
id int,
name char(20),
gongji int,
fangyu tinyint unsigned,
sex enum("男","女"),
country varchar(20)
)default charset=utf8;
insert into sanguo values
(1,'诸葛亮',120,20,'男','蜀国'),
(2,'司马懿',119,25,'男','魏国'),
(3,'关6羽',188,60,'男','蜀国'),
(4,'赵云666',200,66,'男','魏国'),
(5,'8孙权',110,20,'男','吴国'),
(6,'貂蝉',666,10,'女','魏国'),
(7,null,1000,99,'男','蜀国'),
(8,'',1005,88,'女','蜀国');



use MOSHOU;
show tables;
select * from hero;
select * from sanguo;
delete from hero where id =6;
update hero set name = "赵云" where name = "赵子龙";
update hero set name = "大乔",country="魏国"
where 
name = "小乔";
update hero set name = "吕布",sex = "男"
where 
name = "貂蝉";
delete from hero;
-- 1.查找所有蜀国人的信息
-- 2.查找女英雄信息，只显示姓名、性别和国家
-- 3.把曹操的国籍改为蜀国
-- 4.把魏延的性别改为女，国籍改为泰国
-- 5.把id为2 的记录的姓名改为司马懿，性别改为男，国家改为魏国
-- 6.删除所有的泰国人
-- 7.删除所有的记录
select * from hero where country = "蜀国";
select name,sex,country from hero where sex = "女";
update hero set country="蜀国" where name = "曹操";
update hero set sex = "女", country ="泰国" where name ="魏延";
update hero set name ="司马懿",sex = "男",country = "魏国" where id =2;
delete from hero where country = "泰国";
delete from hero;
-- 1.找出攻击力高于150的英雄的名字和攻击力值
select name,gongji from sanguo where gongji > 150;
-- 2.找出防御力不等于100的英雄信息
select * from sanguo where fangyu != 100;

-- 1.找出攻击值大于200的蜀国英雄的名字和攻击值
select name,gongji from sanguo where gongji > 200 and country ="蜀国";
-- 2.查找蜀国和魏国的英雄信息
select * from sanguo where country = "蜀国" or country ="魏国";
-- 3.将吴国英雄中攻击力值为110的英雄攻击值改为100，防御值改为60
update sanguo set gongji =100,fangyu = 60 where gongji = 110 and country ="吴国";
select * from sanguo;
-- 1.查找攻击值在100-200之间的蜀国英雄信息
select * from sanguo where country= "蜀国" and gongji between 100 and 200;
-- 2.找出蜀国和吴国以外国家的女英雄
select * from sanguo where country not in ("蜀国","吴国") and sex = "女";
-- 3.找到编号为1，3或5的蜀国英雄和貂蝉的编号姓名国家信息
select id,name,country from sanguo where (id in(1,3,5) and country="蜀国") or name = "貂蝉";
-- 1.查找姓名为NULL的蜀国男英雄信息
select * from sanguo where name is null and sex = "男" and country = "蜀国";
-- 2.查找姓名为“”的英雄的id,姓名和国家
select id,name,country from sanguo where name = "";

-- 3.示例
--             1.select name from sanguo where name like "_%_";
--             2.select name from sanguo where name like "%";
--             3.select name from sanguo where name like "___"
--             4.select name from sanguo where name like "赵%";
# 显示至少有两个字符的名字
select name from sanguo where name like "_%_";
# 显示除了Null之外的所有名字
select name from sanguo where name like "%";
#显示有3个字符的名字https://www.cnblogs.com/zgqys1980/p/4129239.html
select name from sanguo where name like "___";
#显示姓赵的名字
select name from sanguo where name like "赵%";
select name from sanguo where name regexp "[0-9]";
select name from sanguo where name regexp "^[0-9]";
select name from sanguo where name regexp "[0-9]$";
select name from sanguo where name regexp "^司.*懿$";
select name from sanguo where name regexp "^...$";
-- 1.将英雄按防御值从低到高排序
-- 2.将蜀国英雄按攻击值从高到低排序
-- 3.将魏蜀两国的男英雄中名字为3个字的英雄按防御值升序排列
select * from sanguo order by fangyu asc;
select * from sanguo where country = '蜀国' order by gongji desc;
select * from sanguo 
where country in('魏国','蜀国') and sex = '男' and name like '___'
order by fangyu; 

-- 1.查找防御值倒数第二名到倒数第四名的蜀国英雄记录
-- 2.查找攻击值前三名且名字不为空值的蜀国英雄的姓名，攻击值，国家

select * from sanguo
where country ='蜀国'
order by fangyu 
limit 1,3;

select name,gongji,country from sanguo
where (name is not null) and country = '蜀国'
order by gongji desc
limit 2;

select max(gongji) as best from sanguo;
select count(id),count(name) from sanguo;
select count(id) from sanguo
where country = '蜀国' and gongji > 200;

-- 1.统计三国表中一共有几个国家
-- 2.计算所有国家的平均攻击力
-- 3.查找所有国家中，英雄数量最多的前两名的国家名称及英雄数量
select country from sanguo group by country;
select avg(gongji),country from sanguo group by country;
select country,count(id) as 英雄数量 from sanguo
group by country
order by count(id) desc
limit 2;

-- 1.找出平均攻击力大于105的国家的前两名，显示国家名称和平均攻击力
select country, avg(gongji) as 平均攻击 from sanguo
group by country
having 平均攻击>105
order by 平均攻击 desc
limit 2;

select distinct country from sanguo;
select name,country from sanguo;
select count(id) from sanguo 
where
country in('蜀国','魏国','吴国');
use indexdb;
select * from t1;
use MOSHOU;
select name,gongji * 10,country from sanguo;

#约束分类,默认约束
create table day1(
id int,
name varchar(20),
sex enum('M','F','Secret') default 'Secret'
);
desc day1;

create table day2(
id int not null,
name varchar(15),
sex enum('M','F','Secret') default 'Secret');
desc day2;

use indexdb;
desc t1;

show variables like  "%character%";
show variables like "%pro%";
set profiling = 1;
select name from t1 where name='Lucy99999';
show profiles;

create index name on t1(name);
desc t1;
set profiling = 0;
