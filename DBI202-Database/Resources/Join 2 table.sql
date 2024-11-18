SELECT tblEmployee.EmployeeNumber, EmployeeFirstName, EmployeeLastName, sum(Amount) as SumOfAmount
FROM tblEmployee
RIGHT JOIN tblTransaction
ON tblEmployee.EmployeeNumber = tblTransaction.EmployeeNum
GROUP BY tblEmployee.EmployeeNumber, EmployeeFirstName,EmployeeLastname
ORDER BY EmployeeNumber

SELECT * FROM tblTransaction
ORDER BY EmployeeNum ASC