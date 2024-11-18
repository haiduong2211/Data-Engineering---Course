CREATE TABLE TuitionDataSystem (
	last_name VARCHAR(40),
	first_name VARCHAR (25),
	academic_status VARCHAR (3) -- FGS, PGS, FAP, PAP
);

CREATE TABLE AttendaceDataSystem (
	last_name VARCHAR(35),
	fist_name VARCHAR(15),
	enrollment_status VARCHAR(10), --2 values: "Full-time", "Part-time"
	academic_status VARCHAR(13) -- "Good Standing" , "
);


SELECT * FROM TuitionDatabase
