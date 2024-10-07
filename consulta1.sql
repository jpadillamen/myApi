
with detailEmployejobQuarter as
(
SELECT d.department, j.job, DATEPART(Quarter,CONVERT(DATETIME, [datetime], 127)) q
from dbo.hired_employees he
inner join dbo.departments d
on he.department_id = d.id
inner join dbo.jobs j
on j.id = he.job_id
where YEAR(CONVERT(DATETIME, [datetime], 127)) = 2021
),
detailEmployejobQuarter2 as
(
select department, job,
case when q = 1 then 1 else 0 end as q1,
case when q = 2 then 1 else 0 end as q2,
case when q = 3 then 1 else 0 end as q3,
case when q = 4 then 1 else 0 end as q4
from detailEmployejobQuarter
)
select department, job, SUM(q1) as q1, SUM(q2) as q2, SUM(q3) as q3, SUM(q4) as q4
from detailEmployejobQuarter2
group by  department, job
order by department, job

