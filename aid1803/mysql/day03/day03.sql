-- 创建表时创建index
create database day03;
use day03;
create table t1(
id int,
name varchar(20),
index(id),
index(name)
);

desc t1;

-- 在已有表中添加索引字段
alter table t1 add score tinyint;
desc t1;
create index score on t1(score);
desc t1;

show index from t1;

drop index score on t1;
desc t1;
drop index id on t1;

-- 示例唯一索引
create unique index id on t1(id);
desc t1;
show index from t1;

-- 示例主键索引
create table t2(
id int primary key auto_increment,
name varchar(20));

desc t2;

insert into t2(name) values
("Tom"),
("Lucy"),
("Green");

select * from t2;

insert into t2 values
(8,"Tom"),
(9,"Lucy"),
(10,"Green");

insert into t2 values(null,"Jason");

create table t3(
id int auto_increment,
name varchar(10),
primary key(id)
);

create table t4(
id int auto_increment,
name varchar(10),
primary key(id)
)auto_increment = 10000;

insert into t4(name) values("Lucy");
select * from t4;

desc t4;

alter table t4 modify id int;
alter table t4 drop primary key;

desc t4;

alter table t4 add primary key(id);
desc t4;
alter table t4 modify id int auto_increment;

-- 示例外键索引
-- 表1.缴费信息表（财务）
-- 学号  姓名     班级     缴费金额 
-- 1    唐伯虎   AID01   28000
-- 2    点秋香   AID01   20000
-- 表2.学生信息表（班主任）
create table jftab(
id int primary key,
name char(15),
class char(5),
money int
);
insert into jftab values
(1,"唐伯虎","AID01",28000),
(2,"点秋香","AID01",20000),
(3,"祝枝山","AID01",22000);

select * from jftab;
-- 学号  姓名     缴费金额
-- 1    唐伯虎    28000
-- 2    点秋香    20000
create table bjtab(
stu_id  int,
name char(15),
money int,insert into bjtab values
(1,"唐伯虎",28000);
foreign key(stu_id) references jftab(id)
on delete cascade
on update cascade
);

-- 添加   3    祝枝山    22000，则报错
-- 删除   点秋香，则另一表中也删除

select * from jftab;
select * from bjtab;
insert into bjtab values
(1,"唐伯虎",28000);
insert into bjtab values
(2,"点秋香",20000);

delete from jftab where name = "点秋香";
update jftab set id = 5 where name = "唐伯虎";
insert into jftab values
(2,"点秋香","AID01",20000);
insert into bjtab values
(2,"点秋香",20000);

show create table bjtab;
alter table bjtab drop foreign key bjtab_ibfk_1;

alter table bjtab add 
foreign key(stu_id)
references jftab(id);

select * from jftab;
select * from bjtab;

delete from jftab where name = "唐伯虎";
delete from bjtab where name = "唐伯虎";

select * from bjtab;
select * from jftab;

alter table bjtab add foreign key(stu_id)
references jftab(id)
on delete set null
on update set null;

delete from jftab where name = "点秋香";

desc bjtab;
show create table bjtab;
alter table bjtab drop foreign key bjtab_ibfk_1;

-- 导入文件
create table userinfo(
用户名 char(20),
密码 char(1),
UID int,
GID int,
用户描述 varchar(50),
用户主目录 varchar(50),
登录权限 varchar(50));

desc userinfo;

show variables like 'secure%';

load data infile "/var/lib/mysql-files/passwd"
into table userinfo
fields terminated by ':'
lines terminated by '\n';

select * from userinfo;

-- alter table 表名 add 字段名 数据类型 first | after 字段名;
alter table userinfo add id int primary key auto_increment first;

create table studentinfo(
姓名 char(15),
分数 float(4,1),
电话号码 int,
班级 char(7));

alter table studentinfo add id int primary key first;
alter table studentinfo modify 电话号码 bigint;

load data infile "/var/lib/mysql-files/AID1709.csv"
into table studentinfo
fields terminated by ','
lines terminated by '\n';

select * from studentinfo; 

-- 把userinfo 表中的username\password 和uid导出到文件 user.txt

select 用户名,密码 from userinfo 
into outfile '/var/lib/mysql-files/user.txt'
fields terminated by ','
lines terminated by '\n';

-- 复制一张表
create table userinfo2 select * from userinfo;

select * from userinfo2;

-- 2.赋值userinfo表中的用户名，密码，uid 的 第2-10条记录
create table userinfo3 select 用户名,密码,uid from userinfo
limit 1,9;
select * from userinfo3;

show tables;

drop table jftab2;
create table jftab2 select * from jftab where false;
desc jftab2;

-- 把uid的值小于uid平均值的用户名和uid号显示出来
select avg(uid) from userinfo;

select uid,用户名 from userinfo
where uid < (select avg(uid) from userinfo);

create table sheng(
id int primary key auto_increment,
s_id int,
s_name varchar(15)
)default charset=utf8;

insert into sheng values
(1, 130000, '河北省'),
(2, 140000, '陕西省'),
(3, 150000, '四川省'),
(4, 160000, '广东省'),
(5, 170000, '山东省'),
(6, 180000, '湖北省'),
(7, 190000, '河南省'),
(8, 200000, '海南省'),
(9, 200001, '云南省'),
(10,200002,'山西省');

create table city(
id int primary key auto_increment,
c_id int,
c_name varchar(15),
cfather_id int
)default charset=utf8;

insert into city values
(1, 131100, '石家庄市', 130000),
(2, 131101, '沧州市', 130000),
(3, 131102, '廊坊市', 130000),
(4, 131103, '西安市', 140000),
(5, 131104, '成都市', 150000),
(6, 131105, '重庆市', 150000),
(7, 131106, '广州市', 160000),
(8, 131107, '济南市', 170000),
(9, 131108, '武汉市', 180000),
(10,131109, '郑州市', 190000),
(11,131110, '北京市', 320000),
(12,131111, '天津市', 320000),
(13,131112, '上海市', 320000),
(14,131113, '哈尔滨', 320001),
(15,131114, '雄安新区', 320002);


create table xian(
id int primary key auto_increment,
x_id int,
x_name varchar(15),
xfather_id int
)default charset=utf8;

insert into xian values
(1, 132100, '正定县', 131100),
(2, 132102, '浦东新区', 131112),
(3, 132103, '武昌区', 131108),
(4, 132104, '哈哈', 131115),
(5, 132105, '安新县', 131114),
(6, 132106, '容城县', 131114),
(7, 132107, '雄县', 131114),
(8, 132108, '嘎嘎', 131115);

show tables;

-- 1.显示省市的详细信息
select sheng.s_name,city.c_name from sheng 
inner join city 
on city.cfather_id = sheng.s_id;

select sheng.s_name,city.c_name,xian.x_name from sheng
inner join city inner join xian
on city.cfather_id = sheng.s_id and city.c_id = xian.xfather_id;

select sheng.s_name,city.c_name from sheng 
left join city 
on city.cfather_id = sheng.s_id;

select sheng.s_name,city.c_name,xian.x_name from sheng
left join city on city.cfather_id = sheng.s_id
left join xian on city.c_id = xian.xfather_id;

select sheng.s_name,city.c_name,xian.x_name from sheng
right join city on city.cfather_id = sheng.s_id
right join xian on city.c_id = xian.xfather_id;

create view shengshi as
select sheng.s_name,city.c_name,xian.x_name from sheng
right join city on city.cfather_id = sheng.s_id
left join xian on city.c_id = xian.xfather_id;

create table t8(
name varchar(10)
);

create table t9(
name varchar(10)
);

-- 笛卡尔积
insert into t8 values ("A"),("B");
insert into t9 values ("C"),("D"),("E");
select * from t8,t9;
select * from t8
union
select * from t9;

-- 一下等同于inner join
insert into t8 values("C");
select t8.name,t9.name from t8,t9
where t8.name = t9.name;

create table t10(
ISBN int primary key auto_increment,
Title char(50),
Author char(20),
Rating  float(4,2),
_Count int,
Score float(4,2));

alter table t10 modify ISBN text;
alter table t10 modify Author text;
alter table t10 modify Title text;
alter table t10 modify ISBN char(15);


alter table t10 drop primary key;
load data infile '/var/lib/mysql-files/data.csv'
into table t10
fields terminated by '\t'
lines terminated by '\n';
select * from t10;