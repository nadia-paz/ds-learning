/*
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
*/

-- doesn't return null if there is no 2nd highest salary
WITH temp AS (
    SELECT id, salary, ROW_NUMBER() OVER(ORDER BY salary) as ord
    FROM Employee
)
SELECT 
    CASE 
        WHEN (SELECT COUNT(salary) FROM temp) > 1 THEN salary
        ELSE null 
    END AS SecondHighestSalary
FROM temp
WHERE ord = 2

-- works ok
WITH temp AS (
    SELECT MAX(salary) as sal
    FROM Employee
)
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT sal FROM temp)