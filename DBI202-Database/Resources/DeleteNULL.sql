SELECT * FROM tblDepartment
SELECT count(*) FROM tblTransaction
SELECT * FROM tblEmployee


-- Derived table
SELECT *
FROM (
SELECT E.EmployeeNumber as ENumber, E.EmployeeFirstName, E.EmployeeLastname, T.EmployeeNum as TNumber,
		sum(T.Amount) as TotalAmount
FROM tblEmployee as E
right join tblTransaction as T
ON T.EmployeeNum = E.EmployeeNumber
GROUP BY E.EmployeeNumber, T.EmployeeNum, E.EmployeeFirstName, E.EmployeeLastname, T.Amount) as NewTable
WHERE ENumber is NULL
ORDER BY ENumber, TNumber, EmployeeFirstName, EmployeeLastname

-- DELETE 
begin transaction

SELECT count(*) FROM tblTransaction

DELETE tblTransaction
FROM tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNum
WHERE E.EmployeeNumber is NULL

SELECT count(*) FROM tblTransaction

rollback transaction

-- ANOTHER 
begin transaction
SELECT count(*) FROM tblTransaction

DELETE tblTransaction
FROM tblTransaction	
WHERE EmployeeNum IN 
(SELECT TNumber
FROM (
SELECT E.EmployeeNumber as ENumber, E.EmployeeFirstName, E.EmployeeLastname, T.EmployeeNum as TNumber,
		sum(T.Amount) as TotalAmount
FROM tblEmployee as E
right join tblTransaction as T
ON T.EmployeeNum = E.EmployeeNumber
GROUP BY E.EmployeeNumber, T.EmployeeNum, E.EmployeeFirstName, E.EmployeeLastname) as NewTable
WHERE ENumber is NULL)

SELECT count(*) FROM tblTransaction
rollback transaction


--UPDATING DATA
SELECT * FROM tblEmployee where EmployeeNumber = 194
SELECT * FROM tblTransaction where EmployeeNum = 3
SELECT * FROM tblTransaction where EmployeeNum = 194

begin tran
--SELECT * FROM tblTransaction where EmployeeNum = 194
UPDATE tblTransaction
SET EmployeeNum = 194
OUTPUT inserted.*,deleted.*
FROM tblTransaction
WHERE EmployeeNum in (3,5,7,9) and DateOfTransaction >= '2015-05-27'
--SELECT * FROM tblTransaction where EmployeeNum = 194
rollback tran