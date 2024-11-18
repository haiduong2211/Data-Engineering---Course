select T.*
from tblTransaction as T
inner join tblEmployee as E
on E.EmployeeNumber = T.EmployeeNum
Where E.EmployeeLastname like 'y%'
order by E.EmployeeNumber

SELECT *
FROM tblTransaction as T
Where EmployeeNum in 
(select EmployeeNumber FROM tblEmployee Where EmployeeLastname not like 'Y%')
order by EmployeeNum -- must be in tblTransaction and tblEmployee, and not 126-129
					-- LEFT JOIN

SELECT *
FROM tblTransaction as T
Where EmployeeNum not in 
(select EmployeeNumber FROM tblEmployee Where EmployeeLastname like 'Y%')
order by EmployeeNum -- must be in tblTransaction, and not 126-129
					-- LEFT JOIN

					---------------
SELECT *
FROM tblTransaction as T
Where EmployeeNum = ANY-- Equal ANY of the following
(select EmployeeNumber FROM tblEmployee Where EmployeeLastname like 'Y%')
order by EmployeeNum 

SELECT *
FROM tblTransaction as T
Where EmployeeNum = SOME 
(select EmployeeNumber FROM tblEmployee Where EmployeeLastname like 'Y%')
order by EmployeeNum 

--------------FROM
SELECT *
FROM tblTransaction as T
left join (SELECT * FROM tblEmployee
WHERE EmployeeLastname like 'y%') as E
on E.EmployeeNumber = T.EmployeeNum
ORDER BY T.EmployeeNum


SELECT *
FROM tblTransaction as T
left join tblEmployee as E
ON E.EmployeeNumber	= T.EmployeeNum
WHERE E.EmployeeLastname like 'y%' -- if change Where to and -> there will be no filter 
order by T.EmployeeNum 


------------SELECT 
SELECT *
FROM tblEmployee as E
WHERE E.EmployeeLastname like 'y%'

SELECT E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastname, count(T.EmployeeNum) as NumTransactions
FROM tblTransaction as T
inner join tblEmployee as E
ON E.EmployeeNumber = T.EmployeeNum
WHERE E.EmployeeLastname like 'y%'
GROUP BY E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastname
ORDER BY E.EmployeeNumber

SELECT E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastname, (SELECT count(T.EmployeeNum)
			FROM tblTransaction as T
			WHERE E.EmployeeNumber = T.EmployeeNum) as NumTransactions
FROM tblEmployee as E
WHERE E.EmployeeLastname like 'y%' --Correlated Subquery

--------- WHERE exists
SELECT *
FROM tblTransaction as T
WHERE exists 
	(SELECT EmployeeNumber from tblEmployee as E WHERE EmployeeLastname like 'y%' and T.EmployeeNum = E.EmployeeNumber)
ORDER BY EmployeeNum

----------WITH
SELECT * FROM
(SELECT D.Department, EmployeeNumber, EmployeeFirstName, EmployeeLastName, rank() over (partition by D.Department ORDER BY E.EmployeeNumber) as THERANK
from tblDepartment as D
join tblEmployee as E 
ON D.Department = E.Department) as myTable
WHERE THERANK < 5
ORDER BY Department, EmployeeNumber

-->Version WITH
WITH TblWithRanking as
(SELECT D.Department, EmployeeNumber, EmployeeFirstName, EmployeeLastName, rank() over (partition by D.Department ORDER BY E.EmployeeNumber) as THERANK
from tblDepartment as D
join tblEmployee as E 
ON D.Department = E.Department),

Transaction2014 as
(SELECT * FROM tblTransaction WHERE DateOfTransaction < '2015-01-01')

SELECT * FROM TblWithRanking
left join Transaction2014 
on TblWithRanking.EmployeeNumber = Transaction2014.EmployeeNum
WHERE THERANK <= 5
ORDER BY Department, TblWithRanking.EmployeeNumber


---------XEP HANG BAN GHI

SELECT * FROM 
(SELECT D.Department, EmployeeNumber, EmployeeFirstName, EmployeeLastName,
	rank() over(partition by D.Department order by E.EmployeeNumber) as TheRank
FROM tblDepartment as D
	join tblEmployee as E on D.Department = E.Department) as MyTable
WHERE TheRank <= 5
ORDER BY Department, EmployeeNumber

-------GENERATING A LIST OF NUMBER
SELECT * FROM tblEmployee as E
Left join tblTransaction as T
on T.EmployeeNum = E.EmployeeNumber
WHERE T.EmployeeNum is NULL
ORDER BY E.EmployeeNumber

SELECT * FROM tblTransaction
ORDER BY EmployeeNum ASC

WITH Numbers as (
SELECT top(SELECT MAX(EmployeeNum) from tblTransaction) row_number() over(ORDER BY (SELECT NULL)) as RowNumber
FROM tblTransaction as U)

SELECT RowNumber FROM Numbers as U
left join tblTransaction as T
on U.RowNumber = T.EmployeeNum
WHERE T.EmployeeNum is NULL
ORDER BY U.RowNumber

SELECT row_number() over (order by(Select null)) FROM sys.objects O Cross join  sys.objects P


---------GROUPING NUMBERS
WITH Numbers as 
	(SELECT top(SELECT MAX(EmployeeNum) from tblTransaction) row_number() over(ORDER BY (SELECT NULL)) as RowNumber
	FROM tblTransaction as U),
Transaction2014 as
	(SELECT * FROM tblTransaction where DateOfTransaction >= '2014-01-01' and DateOfTransaction <'2015-01-01'),
TblGap as 
	(SELECT RowNumber, RowNumber - LAG(RowNumber) over(order by RowNumber) as PreviousRowNumber,
						LEAD(RowNumber) over(order by RowNumber) - RowNumber as NextRowNumber,
						case when RowNumber - LAG(RowNumber) over(order by RowNumber) = 1 then 0 else 1 end as GroupGap
	FROM Numbers as U
	left join Transaction2014 as T
	on U.RowNumber = T.EmployeeNum
	WHERE T.EmployeeNum is NULL),
tblGroup as
	(SELECT *, SUM(GroupGap) over(ORDER BY RowNumber) as TheGroup
	FROM TblGap)

SELECT Min(RowNumber) as StartingEmployeeNumber, Max(RowNumber) as EndingEmployeeNumber
FROM tblGroup
GROUP BY TheGroup
ORDER BY TheGroup