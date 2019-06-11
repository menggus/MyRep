-- 统计不同月份的已支付订单人数
-- select date_format(paidTime, "%Y-%m") 月份, count(distinct userId) 人数 from orderinfo 
-- where isPaid="已支付" 
-- group by date_format(paidTime, "%Y-%m");

-- 统计用户三月份的复购率和回购率
-- 复购率 sql条件语句：if(条件, true value, false value)
-- select count(userId), count(if(ct>1,1,null)) from (
-- 	select userId, count(userId) ct from orderinfo 
-- 	where isPaid="已支付" and month(paidTime)=3 
-- 	group by userId) t;
-- 回购率  t1.userId 3月份userId, t2.userId 4月份userId
-- 只能算出单月份的回购率 
-- select count(t1.userId), count(t2.userId) from
-- (select distinct userId from orderinfo where month(paidTime)=3) t1 
-- left join (select distinct userId from orderinfo where month(paidTime)=4) t2
-- on t1.userId=t2.userId;
-- 多月份回购率  
-- 时间·减法：t1.m = date_sub(t2.m, interval 1 month)  
-- select t1.m, count(t1.m), count(t2.m) from (select userId, date_format(paidTime,"%Y-%m-01") as m from orderinfo 
-- where isPaid="已支付" group by userId,date_format(paidTIme, "%Y-%m-01")) t1
-- left join (select userId, date_format(paidTime,"%Y-%m-01") as m from orderinfo 
-- where isPaid="已支付" group by userId,date_format(paidTIme, "%Y-%m-01")) t2
-- on t1.userId=t2.userId and t1.m = date_sub(t2.m, interval 1 month)
-- group by t1.m

-- 统计男女用户的消费频次是否有差异
-- select t.sex 性别,avg(t.ct) 消费次数均值	from
-- (select o2.userid,o1.sex sex,count(1) ct from (select * from userinfo where sex!="") o1 
-- inner join (select * from orderinfo where isPaid="已支付") o2
-- on o1.userId=o2.userid 
-- group by o2.userid, o1.sex) t
-- group by sex;

-- select t.sex 性别,avg(t.ct) 消费次数均值	from
-- (select o2.userid,o1.sex sex,count(1) ct from userinfo o1 
-- inner join orderinfo o2
-- on o1.userId=o2.userid 
-- group by o2.userid, o1.sex
-- having o1.sex!="") t
-- group by sex;

-- 统计多次消费的用户，第一次消费和最后一次消费的间隔是多少
-- select userId, datediff(max(paidTime),min(paidTime)) from orderinfo
-- where isPaid="已支付"
-- group by userId
-- having count(1)>1;
-- 统计不同年龄段，用户的消费金额是否有差异
select age, ceil(avg(price)) from
(select price, birth, o1.isPaid, ceil(datediff(now(), birth)/365/10) age from orderinfo o1 
inner join userinfo u1 
on o1.userId=u1.userid having birth>"1901-00-00" and o1.isPaid="已支付") t
group by age;
-- 统计消费的二八法则，消费的top20%用户，贡献了多少额度
select sum(price) from (
select userId,price from orderinfo where isPaid="已支付" group by userId order by price desc limit 17129) t;
