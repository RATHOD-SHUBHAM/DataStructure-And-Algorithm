/*

Employees With Bonuses




Dropbox
Easy

Find employees whose bonus is less than $150.
Output the first name along with the corresponding bonus.

Table: employee

employee Preview
id: int
first_name:varchar
last_name:varchar
age:int
sex:varchar
employee_title:varchar
department:varchar
salary:int
target:int
bonus:int
email:varchar
city:varchar
address:varchar
manager_id:int

*/

select first_name, bonus 
from employee
where bonus < 150;