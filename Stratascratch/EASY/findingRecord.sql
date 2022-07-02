/*

Finding Updated Records

Microsoft

We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

Table: ms_employee_salary

ms_employee_salaryPreview
id:int
first_name: varchar
last_name:varchar
salary:int
department_id:int
*/


-- The GROUP BY statement groups rows that have the same values into summary rows

select distinct id, first_name,last_name, max(salary) as current_salary, department_id 
from ms_employee_salary
GROUP BY id, department_id
-- order according to empid
order by id;