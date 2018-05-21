use ex2;
-- 10、查询Score表中的最高分的学生学号和课程号。
select sno,cno from SCORES
order by degree
limit 1;
-- 11、查询‘3-105’号课程的平均分。
select cno,avg(degree) from SCORES
group by cno
having cno = '3-105'; 
-- 12、查询Score表中至少有5名学生选修的并以3开头的课程的平均分数。
select cno,avg(degree) from SCORES
group by cno
having cno like "3%" and count(sno) >= 5;
-- 13、查询最低分大于70，最高分小于90的Sno列。
select sno from SCORES
group by sno
having max(degree) < 90 and min(degree) >70;
-- 14、查询所有学生的Sname、Cno和Degree列。
select STUDENTS.sname,SCORES.cno,SCORES.degree from STUDENTS
inner join SCORES on STUDENTS.sno = SCORES.sno;
-- 15、查询所有学生的Sno、Cname和Degree列。
select STUDENTS.sno,COURSES.cname,SCORES.degree from STUDENTS
left join SCORES on STUDENTS.sno = SCORES.sno
left join COURSES on COURSES.cno = SCORES.cno;
-- 16、查询所有学生的Sname、Cname和Degree列。
select STUDENTS.sname,COURSES.cname,SCORES.degree from STUDENTS
left join SCORES on STUDENTS.sno = SCORES.sno
left join COURSES on COURSES.cno = SCORES.cno
order by STUDENTS.sname;
-- 17、查询“95033”班所选课程的平均分。
select SCORES.cno,avg(SCORES.degree) from STUDENTS
inner join SCORES on STUDENTS.sno = SCORES.sno
where STUDENTS.class = '95033'
group by SCORES.cno
order by SCORES.cno;
-- 18、假设使用如下命令建立了一个grade表：
create table grade(low   tinyint,upp   tinyint,rank   char(1));
insert into grade values(90,100,'A');
insert into grade values(80,89,'B');
insert into grade values(70,79,'C');
insert into grade values(60,69,'D');
insert into grade values(0,59,'E');
select * from grade;
-- commit;
-- 现查询所有同学的Sno、Cno和rank列。
select sno,cno,grade.rank from SCORES
left join grade on SCORES.degree between grade.low and grade.upp;
-- 19、查询选修“3-105”课程的成绩高于“109”号同学成绩的所有同学的记录。
select * from STUDENTS
left join SCORES on SCORES.sno = STUDENTS.sno
where degree >
(select degree from SCORES where sno = '109' and cno = '3-105') and cno ='3-105';

select * from SCORES as s1 
inner join SCORES as s2 on (s1.cno = s2.cno and s1.degree > s2.degree)
where s2.sno = '109' and s2.cno = '3-105';
-- 20、查询score中选学一门以上课程的同学中分数为非最高分成绩的记录。
select * from SCORES as s1 
inner join
(select cno,max(degree)as max_degree from SCORES
group by cno) as s2 on s1.cno = s2.cno
where degree < max_degree
group by sno
having count(s1.cno) >1;
-- 21、查询成绩高于学号为“109”、课程号为“3-105”的成绩的所有记录。
select * from SCORES
where degree > (select degree from SCORES 
where cno='3-105' and sno = '109');

-- 22、查询和学号为108的同学同年出生的所有学生的Sno、Sname和Sbirthday列。
select s2.sno,s2.sname,s2.sbirthday from STUDENTS as s1
inner join STUDENTS as s2 on (year(s1.sbirthday) = year(s2.sbirthday))
where s1.sno = '107' and s2.sno != s1.sno; 

-- 23、查询“张旭“教师任课的学生成绩。
select TEACHERS.tname,SCORES.cno,SCORES.degree from TEACHERS
inner join COURSES on TEACHERS.tno = COURSES.tno
inner join SCORES on SCORES.cno = COURSES.cno
where TEACHERS.tname = '张旭';

SELECT Sno,Degree
FROM SCORES INNER JOIN COURSES
ON(SCORES.Cno=COURSES.Cno) INNER JOIN TEACHERS
ON(COURSES.Tno=TEACHERS.Tno)
WHERE TEACHERS.Tname='张旭';
-- 24、查询选修某课程的同学人数多于5人的教师姓名。
select TEACHERS.tname, _SCORES._number from TEACHERS
inner join COURSES on TEACHERS.tno = COURSES.tno
inner join(select count(sno) as _number,cno from SCORES
group by cno) as _SCORES on  _SCORES.cno = COURSES.cno
where _SCORES._number > 5;
-- 25、查询95033班和95031班全体学生的记录。
select * from STUDENTS
where class in ("95033","95031");
-- 26、查询存在有85分以上成绩的课程Cno.

-- 27、查询出“计算机系“教师所教课程的成绩表。
-- 28、查询“计算机系”与“电子工程系“不同职称的教师的Tname和Prof。
-- 29、查询选修编号为“3-105“课程且成绩至少高于选修编号为“3-245”的同学的Cno、Sno和Degree,并按Degree从高到低次序排序。
-- 30、查询选修编号为“3-105”且成绩高于选修编号为“3-245”课程的同学的Cno、Sno和Degree.
-- 31、查询所有教师和同学的name、sex和birthday.
-- 32、查询所有“女”教师和“女”同学的name、sex和birthday.
-- 33、查询成绩比该课程平均成绩低的同学的成绩表。
-- 34、查询所有任课教师的Tname和Depart.
-- 35  查询所有未讲课的教师的Tname和Depart. 
-- 36、查询至少有2名男生的班号。
-- 37、查询Student表中不姓“王”的同学记录。
-- 38、查询Student表中每个学生的姓名和年龄。
-- 39、查询Student表中最大和最小的Sbirthday日期值。
-- 40、以班号和年龄从大到小的顺序查询Student表中的全部记录。
-- 41、查询“男”教师及其所上的课程。
-- 42、查询最高分同学的Sno、Cno和Degree列。
-- 43、查询和“李军”同性别的所有同学的Sname.
-- 44、查询和“李军”同性别并同班的同学Sname.
-- 45、查询所有选修“计算机导论”课程的“男”同学的成绩表