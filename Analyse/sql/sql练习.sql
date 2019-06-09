-- select city, count(positionId) from position 
-- group by city;

-- -- -- -- -- -- -- -- -- -- -- -- 
-- 分组
-- 查看不同城市的职位和公司数
-- select city, count(positionId), count(distinct(companyId)) from position
-- group by city;

-- 查看不同城市不同学历职位数
-- select city, education, count(1), count(positionId) from position
-- group by city, education;

-- 查看不同城市电子商务岗位的数量
-- select city, count(1) from position
-- where industryField like "%电子商务%"
-- group by city
-- having count(positionName)>50;

-- 查看包含电子商务职位的数量大于50的城市
-- select city from position
-- group by city
-- having count(if(industryField like "%电子商务%", 1, null))>50;

-- 查看领域包含电子商务的职位在不同城市的占比
-- select city, count(1) as total, 
-- count(if(industryField like "%电子商务%", industryField, null)) as emark,
-- count(if(industryField like "%电子商务%", industryField, null))/count(1) as ratio
-- from position group by city
-- having emark>50
-- order by ratio desc;

-- --- ------- --------- -----------
-- 函数  截取 
-- 从左截取：left(字段, 位置),  right(字段, 位置), 字符长度: length()
-- select left(salary, 1), salary from position;
-- 查找字符位置: locate("字符", 字段, 开始位置)
-- select left(salary, 1),locate("k", salary), salary from position;

-- select left(salary, locate("k",salary)) as bottom_salary, salary from position;

-- select left(salary, locate("k",salary)) as bottom_salary, salary,
-- right(salary, length(salary)-locate("-", salary)) 
-- from position;

-- substr(字段, 截取开始位置, 截取长度)
-- select left(salary, locate("k",salary)) as bottom_salary, salary,
-- substr(salary, locate("-", salary)+1, length(salary)-locate("-",salary)) as top_salary
-- from position;

-- 子查询, 查询的表当做数据来用
-- select (bottom_salary+top_salary)/2, salary from 
-- (select left(salary, locate("k",salary)) as bottom_salary, salary,
-- substr(salary, locate("-", salary)+1, length(salary)-locate("-",salary)) as top_salary
-- from position) as t;

-- case when ....else.... end
-- select 
-- case
-- 	when (bottom_salary+top_salary)/2<10 then "10k以下"
--     when (bottom_salary+top_salary)/2<20 then "10k-20k"
--     when (bottom_salary+top_salary)/2<30 then "20k-30k"
-- 	else "30k以上"
-- end as 范围,salary
-- from (select left(salary, locate("k",salary)) as bottom_salary, salary,
-- substr(salary, locate("-", salary)+1, length(salary)-locate("-",salary)) as top_salary
-- from position) as t;

-- 子查询额外用法
-- select city from position group by city having count(positionId)>200;
select * from position
where city in (select city from position group by city having count(positionId)>200);

select * from position as p 
left join company as c on p.companyId=c.companyId 
where c.companyShortName="唯医网";
