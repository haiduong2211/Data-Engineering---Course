SELECT * FROM CHITIETHOADON
SELECT * FROM HOADON
SELECT * FROM KHACHHANG
SELECT * FROM VATTU

---Hiển thị danh sách các khách hàng có điện thoại là 08457895 gồm mã khách hàng, tên khách hàng, địa chỉ, điện thoại, và địa chỉ E-mail.
SELECT * FROM KHACHHANG
WHERE DT like '8457895%'

---Hiển thị danh sách các vật tư là “DA” (bao gồm các loại đá) có giá mua dưới 30000 gồm mã vật tư, tên vật tư, đơn vị tính và giá mua .
SELECT MAVT, TENVT, DVT, GIAMUA 
FROM VATTU
WHERE GIAMUA < 30000 and TENVT like 'DA%'
---Tạo query để lấy ra các thông tin gồm Mã hoá đơn, ngày lập hoá đơn, tên khách hàng, địa chỉ khách hàng và số điện thoại, sắp xếp theo thứ tự ngày tạo hóa đơn giảm dần
SELECT H.MAHD, H.NGAY, K.TENKH, K.DIACHI, K.DT
FROM HOADON as H
inner join KHACHHANG as K 
ON H.MAKH = K.MAKH
ORDER BY H.NGAY DESC
---Lấy ra danh sách những khách hàng mua hàng trong tháng 6/2000 gồm các thông tin tên khách hàng, địa chỉ, số điện thoại.
SELECT distinct K.TENKH, K.DIACHI, K.DT
FROM KHACHHANG as K
left join HOADON as H
ON H.MAKH = K.MAKH
WHERE H.NGAY >= '2000-06-01' and H.NGAY < '2000-07-01'
--Cach2
SELECT TENKH, DIACHI, DT FROM KHACHHANG as K
right join (SELECT MAKH FROM HOADON WHERE NGAY >= '2000-06-01' and NGAY < '2000-07-01') as H
ON K.MAKH = H.MAKH 

---Tạo query để lấy ra các chi tiết hoá đơn gồm các thông tin mã hóa đơn,mã vật tư, tên vật tư, giá bán, giá mua, số lượng , trị giá mua (giá mua * số lượng), trị giá bán (giá bán * số lượng), tiền lời (trị giá bán – trị giá mua) mà có giá bán lớn hơn hoặc bằng giá mua.
GO
With MyTable as 
(SELECT H.MAHD, CT.MAVT, V.TENVT, CT.GIABAN, V.GIAMUA, CT.SL,  TriGiaBan = CT.GIABAN * CT.SL , TriGiaMua = V.GIAMUA*CT.SL
FROM HOADON as H
inner join CHITIETHOADON as CT
on H.MAHD = CT.MAHD
inner join VATTU as V
on CT.MAVT = V.MAVT
WHERE GIABAN >= GIAMUA)

SELECT * , TienLoi = TriGiaBan - TriGiaMua
FROM MyTable

---Lấy ra hoá đơn có tổng trị giá nhỏ nhất trong số các hóa đơn năm 2000, gồm các thông tin: Số hoá đơn, ngày, tên khách hàng, địa chỉ khách hàng, tổng trị giá của hoá đơn.
SELECT H.MAHD, H.NGAY, K.TENKH, K.DIACHI, H.TONGTG
FROM (SELECT * FROM HOADON WHERE TONGTG = (SELECT min(TONGTG) FROM HOADON)) as H
inner join KHACHHANG as K
ON K.MAKH = H.MAKH

---Lấy ra các thông tin về các khách hàng mua ít loại vật tư nhất.
GO
With tblCountVT as
(SELECT K.MAKH,count( DISTINCT C.MAVT) as CountVT
FROM CHITIETHOADON as C
inner join HOADON as H
ON C.MAHD = H.MAHD
inner join KHACHHANG as K
ON H.MAKH = K.MAKH
GROUP BY K.MAKH)

SELECT T.MAKH, K.TENKH, K.DT
FROM tblCountVT as T
inner join KHACHHANG as K
on T.MAKH = K.MAKH
WHERE T.CountVT = (SELECT MIN(CountVt) FROM tblCountVT) 

---Lấy ra vật tư có giá mua thấp nhất
GO
SELECT * 
FROM VATTU 
WHERE GIAMUA = (SELECT MIN(GIAMUA) FROM VATTU)


---Lấy ra vật tư có giá bán cao nhất trong số các vật tư được bán trong năm 2000.
--Chú ý: Có thể có những vật tư chưa bán được đơn vị nào, khi đó cần hiển thị là đã bán 0 đơn vị.

SELECT * FROM VATTU
WHERE MAVT = (
SELECT MAX(MAVT) FROM CHITIETHOADON)
