/*
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

-- submitted, accepted beats 53%
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN

IF N <= 0 THEN 
    RETURN QUERY SELECT NULL::INT;
    RETURN;
END IF;

RETURN QUERY (
    -- Write your PostgreSQL query statement below.


SELECT DISTINCT e.salary
FROM Employee e
ORDER BY e.salary DESC
LIMIT 1 OFFSET CASE WHEN N < 2 then 0 ELSE N-1 END

    ) ;
END;
$$ LANGUAGE plpgsql;

-- with window function dense_rank(), submitted, accepted, beats 65%
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN

IF N <= 0 THEN 
    RETURN QUERY SELECT NULL::INT;
    RETURN;
END IF;

RETURN QUERY (
    -- Write your PostgreSQL query statement below.
WITH temp AS (
    SELECT e.salary,
        DENSE_RANK() OVER(ORDER BY e.salary DESC) AS r
    FROM Employee e
)

SELECT t.salary
FROM temp t
WHERE r = N
LIMIT 1

    ) ;
END;
$$ LANGUAGE plpgsql;

-- incorrect, returns smallest if N < 0, needs to return null
-- save because of custom order by with distinct
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT A.salary
    FROM (
        SELECT DISTINCT(e.salary),
            CASE WHEN N >= 0 THEN e.salary END AS sal1,
            CASE WHEN N < 0 THEN e.salary END AS sal2
    
        FROM Employee e
        ORDER BY
            CASE WHEN N >= 0 THEN  e.salary END DESC,
            CASE when N < 0 then e.salary END
        LIMIT 1 OFFSET CASE WHEN N < 2 then 0 ELSE N-1 END ) A
    ) ;
END;
$$ LANGUAGE plpgsql;