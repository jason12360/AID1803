insert into	students values(4,"momm",9,"add");
select * from students;
use db2;
create table t2(
id  int,
age tinyint unsigned
);
insert into t2(age) values(-1);
insert into t2(age) values(299);
insert into t2(age) values(255);
select * from t2;
drop table t2;
create table t3(
salary float(12,2)
);
insert into t3 values(1234567890.12);

desc stuinfo;
insert into stuinfo values(1,"jason","AID1803",20,1.80),(2,"jason2","AID1803",21,1.90);
select * from stuinfo;
select name,age,height from stuinfo;

show databases;
drop database db2;
show databases;
drop database stu1;
show databases;
drop database python;
drop database student;
create database day01;
use day01;

create table t5(
id int,
name char(20),
age tinyint unsigned,
sex enum("boy","girl","secret"),
likes set("girl","boy","Python","Mysql")
)default charset=utf8;

desc t5;
insert into t5(name,sex,likes) values("金花婆婆","girl","boy,Mysql,Python");

select * from t5;

insert into t5(name,sex,likes) values("金花婆婆","ss","boy,Mysql,Python");

create table t6(
id int,
name varchar(15),
age tinyint unsigned,
birth_year year,
birth_day date,
class time,
meeting datetime)default charset=utf8;

desc t6;
insert into t6 values
(1,"武松",40,1979,19790520,090000,20180504000000);

select * from t6;

create table t7(
class datetime,
meeting timestamp
);

desc t7;

insert into t7(class) values(20180520000000);
select * from t7;
show tables;

desc t5;

use school;

create table students(
id int,
name varchar(15),
age tinyint unsigned,
score tinyint unsigned,
sex enum("male","Female"),
likes set("Study","Gamming","Sports","Work"),
enrollment date);

desc students;

show create table students;
alter table students change id student_id int;
desc students;
alter table students add id int first;
desc students;

insert into students values
(1,001,'a',1,80,"male","Study,Work",20170901),
(2,002,'b',2,81,"Female","Study,Work",20170901),
(3,003,'c',1,80,"male","Study,Work",20170901),
(4,004,'d',2,80,"male","Study,Work",20170901),
(5,005,'e',1,80,"male","Study,Work",20170901);

select * from students;
select name,score from students;

