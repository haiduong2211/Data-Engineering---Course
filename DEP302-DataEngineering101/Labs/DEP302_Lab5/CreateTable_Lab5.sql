USE DEP302_Lab5
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- If the table already exists, it will be dropped
IF OBJECT_ID('dbo.FactResellerSales', 'U') IS NOT NULL
DROP TABLE [dbo].[FactResellerSales];
GO

-- Creation of the new table
CREATE TABLE [dbo].[FactResellerSales](
    [ProductKey] [int] NULL,
    [OrderDateKey] [int] NULL,
    [SalesTerritoryKey] [int] NULL,
    [SalesOrderNumber] [varchar](50) NULL,
    [SalesOrderLineNumber] [int] NULL,
    [RevisionNumber] [int] NULL,
    [OrderQuantity] [int] NULL,
    [UnitPrice] [decimal](10, 4) NULL,
    [ExtendedAmount] [decimal](10, 4) NULL,
	[StartDay] [datetime] NULL,
	[EndDay] [datetime] NULL
) ON [PRIMARY]
GO

ALTER TABLE FactResellerSales
ADD  
StartDate datetime NULL,
EndDate datetime NULL ;

	


SELECT * FROM FactResellerSalesImport
SELECT * FROM FactResellerSales


TRUNCATE TABLE FactResellerSalesImport
ALTER TABLE FactResellerSalesImport
DROP COLUMN StartDate, EndDate