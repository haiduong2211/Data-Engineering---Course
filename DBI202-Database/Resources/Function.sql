
CREATE FUNCTION AmountPlusOne (@Amount smallmoney)
RETURNS smallmoney
AS
BEGIN
    RETURN @amount + 1
END
GO

SELECT DateOfTransaction, EmployeeNum, Amount, dbo.AmountPlusOne(Amount) as AmountAndOne
FROM tblTransaction

DECLARE @myValue smallmoney
EXEC @myValue = dbo.AmountPlusOne @Amount = 123.54
SELECT	@myValue

-- THIS IS A COMPLICATED SCALAR Dunction
if exists (SELECT * FROM sys.objects
WHERE name = 'NumberOfTransactions')
	DROP FUNCTION NumberOfTransactions
	GO

CREATE FUNCTION NumberOfTransactions (@EmployeeNumber int)
RETURNS int 
AS
BEGIN
	DECLARE @NumberOfTransactions INT
	SELECT @NumberOfTransactions= COUNT(*) FROM tblTransaction
	WHERE @EmployeeNumber = EmployeeNum
	RETURN @NumberOfTransactions
END

SELECT *,dbo.NumberOfTransactions(EmployeeNumber) as TransNum
FROM tblEmployee
--Above and Below have the same result but execution plan is different
SELECT E.EmployeeNumber, E.EmployeeLastname, E.EmployeeFirstName, count(T.EmployeeNum) as TransNum
FROM tblEmployee as E
left join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNum
GROUP BY E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastname

-- TABLE QUERY

CREATE FUNCTION [dbo].[FunctionName]
(
    @param1 int,
    @param2 char(5)
)
RETURNS TABLE AS RETURN
(
    SELECT @param1 AS c1,
	       @param2 AS c2
)

