SELECT * FROM tblEmployee
WHERE DateOfBirth >= '19850101' and DateOfBirth <'19900101'

SELECT * FROM tblEmployee
WHERE DateOfBirth between '19850101' and '19903112'

SELECT * FROM tblEmployee
WHERE year(DateOfBirth) between 1976 and 1988 -- DO NOT USE

SELECT year(DateOfBirth) as YearOfDateOfBirth, count(*) as NumberBorn
FROM tblEmployee
GROUP BY year(DateOfBirth)
ORDER BY year(DateOfBirth) DESC

SELECT  * FROM tblEmployee
WHERE year(DateOfBirth) = 1990

