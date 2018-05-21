create database ex1;
use ex1;
create table comment(
id int,
article_id int,
user_id int,
date datetime);

desc comment;

insert into comment(id,article_id,user_id) values
(1,10000,10000),
(2,10001,10001),
(3,10002,10000),
(4,10003,10015),
(5,10004,10006),
(6,10025,10006),
(7,10009,10000);

select * from comment;

select user_id, count(article_id) from comment
group by user_id
order by count(article_id) desc
limit 10;