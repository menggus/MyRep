## MySql面试题

![](/home/gram/桌面/面试练习/images/425762-20160803224643778-2071849037.png)

1、自行创建测试数据

2、查询“生物”课程比“物理”课程成绩高的所有学生的学号以及信息；

```sql
# 方式一
SELECT  s.*, s1.number "生物成绩", s2.number "物理成绩"
FROM student s, score s1, score s2
WHERE s.sid=s1.student_id=s2.student_id
AND s1.course_id=1 AND s2.course_id=2 AND s1.number > s2.number;
# 方式二
SELECT s.*, s1.number "生物成绩", s2.number "物理成绩" 
FROM student s
JOIN score s1 ON s1.course_id=1 AND s.sid=s1.student_id
JOIN score s2 ON s2.course_id=2 AND s.sid=s2.student_id
WHERE s1.number > s2.number;
```

3、查询平均成绩大于60分的同学的学号和平均成绩； 

```sql
SELECT student_id, avg(number) "平均成绩" 
FROM score 
group by student_id having avg(number)>60;  
```

4、查询所有同学的学号、姓名、选课数、总成绩；

```sql
SELECT s.sid "学号", s.sname "姓名", count(s1.course_id) "选课数", sum(s1.number) "总成绩"   
FROM student s 
LEFT JOIN score s1 on s.sid=s1.student_id
GROUP BY s.sid;
```

5、查询姓“李”的老师的个数；

```SQL
SELECT COUNT(*) 
FROM teacher
WHERE tname like "李%";
```

6、查询没学过“叶平”老师课的同学的学号、姓名；

![1564407399323](/home/gram/.config/Typora/typora-user-images/1564407399323.png)

```SQL
SELECT DISTINCT s.sid "学号", s.sname "姓名" 
FROM student s, score s1, course c ,teacher t 
WHERE s.sid=s1.student_id
AND s1.course_id=c.coid
AND c.teacher_id = t.tid
AND t.tname <> "叶平";

# 执行计划看起来相对较好
SELECT * FROM student s 
WHERE s.sid NOT IN(
SELECT s1.sid FROM student s1 JOIN score s2 ON s1.sid=s2.student_id WHERE s2.course_id IN (
SELECT c.coid FROM course c JOIN teacher t ON c.coid = t.tid WHERE tname ='李平'));
```

7、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；

```sql
select s.sid, s.sname from student s, score s1,score s2
where s.sid=s1.student_id and s.sid=s2.student_id and s1.course_id=1 and s2.course_id=2;
```

8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；

```sql
???

```



9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；

10、查询有课程成绩小于60分的同学的学号、姓名；

11、查询没有学全所有课的同学的学号、姓名；

12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；

13、查询至少学过学号为“001”同学所选课程中任意一门课的**其他同学**学号和姓名；

14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

15、删除学习“叶平”老师课的SC表记录；

16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 

17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

20、课程平均分从高到低显示（现实任课老师）；

21、查询各科成绩前三名的记录:(不考虑成绩并列情况) 

22、查询每门课程被选修的学生数；

23、查询出只选修了一门课程的全部学生的学号和姓名；

24、查询男生、女生的人数；

25、查询姓“张”的学生名单；

26、查询同名同姓学生名单，并统计同名人数；

27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 

31、求选了课程的学生人数

32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；

33、查询各个课程及相应的选修人数；

34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

35、查询每门课程成绩最好的前两名；

36、检索至少选修两门课程的学生学号；

37、查询全部学生都选修的课程的课程号和课程名；

38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；

39、查询两门以上不及格课程的同学的学号及其平均成绩；

40、检索“004”课程分数小于60，按分数降序排列的同学学号；

41、删除“002”同学的“001”课程的成绩；