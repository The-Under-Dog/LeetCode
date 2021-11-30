SELECT a.name as Employee
FROM Employee AS a, Employee AS b
WHERE a.managerID = b.id AND a.salary > b.salary
