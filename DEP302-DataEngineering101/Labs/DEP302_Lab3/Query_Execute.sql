USE DEP302_Lab3
SELECT * FROM StudentData

select * from TuitionData
select * from AttendanceData

select len(AcademicStatus) From StudentData

ALTER TABLE AttenDanceData
ADD AcademicStatus varchar(5)

DROP TABLE AttendanceData
DROP TABLE TuitionData
DROP TABLE StudentData