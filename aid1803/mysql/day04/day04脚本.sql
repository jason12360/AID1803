-- 创建表并插入记录
-- 表1
create database day04;
use day04;
create table CCB(
name varchar(20),
money int)
;
insert into CCB values("Zhuanqian",10000);
-- 表2
create table ICBC(
name varchar(20),
money int
);
insert into ICBC values("Shouqian",4000);
-- 开始转账,以下示例事务相关操作
start transaction;
update CCB set money = 5000 where name = "zhuanqian";
update ICBC set money = 断电了; 
rollback;
select * from CCB;
-- 示例存储引擎
show engines;

use day03;
select * from sheng;
delete from sheng where id = 11;
update CCB set money=5000 where name = "Zhuanqian";