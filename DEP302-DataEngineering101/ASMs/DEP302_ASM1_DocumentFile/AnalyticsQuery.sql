-- TRUY VẤN NGHIỆP VỤ DÙNG ĐỂ PHÂN TÍCH DỮ LIỆU TỪ DATASET
--1. Số lượng thú nuôi chưa được tiêm vaccine và chưa được sổ giun, phân theo từng khu vực (state)
SELECT s.State, count(*) as TotalAnimalNeedCare
FROM Pet_fact p
JOIN Health_Dim h
ON h.HealthID = p.HealthID
JOIN state_dim s
ON p.stateID = s.stateID 
WHERE h.vacinated != 'Yes'
	AND h.Dewormed != 'Yes'
Group by s.state

--2. Số lượng từng loài thuần chủng (Không được lai giữa 2 loại khác nhau)
SELECT t.type, count(*) as totalPet
FROM Pet_Fact p
LEFT JOIN Breed_dim b
on p.Breed2ID = b.BreedID
LEFT JOIN PetType_Dim t
ON t.PetTypeID = p.PetTypeID
WHERE b.Breed = 'None'
GROUP BY t.Type
ORDER BY totalPet


--3. Phí nhận nuôi theo trung bình theo kích thước trưởng thành 
SELECT m.MaturitySize, AVG(p.fee) as AverageFee
FROM Pet_fact p
JOIN MaturitySize_Dim m
on p.MaturitySizeID = m.MaturitySizeID
GROUP BY MaturitySize
ORDER BY AverageFee DESC


--4. Phí nhận nuôi trung bình theo giống 
SELECT b.breed AS breed1, b2.breed AS breed2, AVG(p.fee) AS avgFee
FROM Pet_Fact p
JOIN Breed_Dim b ON p.Breed1ID = b.BreedID 
JOIN Breed_Dim b2 ON p.Breed2ID = b2.BreedID
GROUP BY b.Breed, b2.Breed
ORDER BY avgFee DESC
