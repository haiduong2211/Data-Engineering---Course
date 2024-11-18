SELECT Department 
FROM 
(SELECT Department, count(*) as NumOfDep
FROM tblEmployee
GROUP BY Department) as newTable

--derived table

SELECT DISTINCT Department, CONVERT(varchar(20),N'') as DepartmentHead
INTO tblDepartment
FROM tblEmployee

DROP TABLE tblDepartment

ALTER TABLE tblDepartment
ALTER COLUMN DepartmentHead varchar(30) NULL