
with hiredByDepartment as
(
SELECT he.department_id, COUNT(he.id) as total
from dbo.hired_employees he
where YEAR(CONVERT(DATETIME, [datetime], 127)) = 2021
group by he.department_id
),
avghiredByDepartment as
(
select AVG(total) as [avg]
from hiredByDepartment
)
select d.id, d.department, h.total from hiredByDepartment h
left join departments d
on d.id = h.department_id
, avghiredByDepartment a
where h.total > a.[avg]
order by h.total desc	


