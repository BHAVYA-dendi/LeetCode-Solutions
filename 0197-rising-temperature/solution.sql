# Write your MySQL query statement below
with compare as (select id,temperature,recordDate,lag(temperature) over (order by recordDate) as prevtemp, lag(recordDate) over (order by recordDate) as prevdate from weather )
select id from compare where temperature>prevtemp and datediff(recordDate,prevdate)=1
