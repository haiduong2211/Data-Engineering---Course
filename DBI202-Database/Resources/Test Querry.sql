ALTER TABLE tblEmployee
ADD Department VARCHAR(10);

SELECT * FROM tblEmployee

INSERT INTO tblEmployee 
VALUES (132,'Dylan','A','Word','HN513777D', '19920914','Customer Relations')

ALTER TABLE tblEmployee
DROP COLUMN Department

ALTER TABLE tblEmployee
ALTER COLUMN Department VARCHAR(15);

ALTER TABLE tblEmployee
ALTER COLUMN Department VARCHAR(20)

SELECT * FROM tblEmployee 
WHERE [EmployeeLastName] >= 'Word'

SELECT * FROM tblEmployee 
WHERE [EmployeeLastName] LIKE 'W%g%'

SELECT * FROM tblEmployee 
WHERE [EmployeeLastName] LIKE '_W' -- '_' is for 1 letter

SELECT * FROM tblEmployee 
WHERE [EmployeeLastName] LIKE '%[r-t]'

SELECT * FROM tblEmployee 
WHERE [EmployeeLastName] LIKE '[^r-t]%'