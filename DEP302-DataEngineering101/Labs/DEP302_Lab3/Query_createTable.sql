USE [DEP302_Lab3]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON 
GO

CREATE TABLE [dbo].[TuitionData](
	[LastName] [varchar](50) NULL,
	[FirstName] [varchar](15) NULL,
	[EnrollmentStatus][varchar](10) NULL,
	[AcademicStatus][varchar](13) NULL
	) on [PRIMARY]

GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON 
GO

CREATE TABLE [dbo].[StudentData](
	[LastName][varchar](40) NOT NULL,
	[FirstName][varchar](15) NOT NULL,
	[AcademicStatus][varchar](4) NOT NULL
) ON [PRIMARY]

GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON 
GO
CREATE TABLE [dbo].[AttendanceData](
	[LastName][varchar](40) NOT NULL,
	[FirstName][varchar](15) NOT NULL,
	[AcademicStatus][varchar](4) NOT NULL
) ON [PRIMARY]


DROP TABLE [dbo].[TuitionData]
DROP TABLE [dbo].[AttendanceData]
DROP TABLE [dbo].[StudentData]

SELECT * FROM dbo.Tuitiondata
