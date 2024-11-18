select * from VATTU
SELECT * FROM HOADON
JOIN CHITIETHOADON ct on ct.MAHD = HOADON.MAHD
WHERE HOADON.NGAY >= '20000601' and  HOADON.NGAY < '20000701'

SELECT * FROM CHITIETHOADON	
SELECT * FROM VATTU

--1. Lấy ra các thông tin gồm Mã hoá đơn, ngày lập hoá đơn, tên khách hàng, địa chỉ khách hàng và số điện thoại.
SELECT HOADON.MAHD, HOADON.NGAY, KHACHHANG.TENKH, KHACHHANG.DIACHI, KHACHHANG.DT  
FROM HOADON
LEFT JOIN KHACHHANG ON KHACHHANG.MAKH = KHACHHANG.MAKH
--2. Lấy ra các thông tin gồm Mã hoá đơn, tên khách hàng, địa chỉ khách hàng và số điện thoại của ngày 25/5/2000.
SELECT HOADON.MAHD, HOADON.NGAY, KHACHHANG.TENKH, KHACHHANG.DIACHI, KHACHHANG.DT  
FROM HOADON
LEFT JOIN KHACHHANG ON KHACHHANG.MAKH = KHACHHANG.MAKH
WHERE HOADON.NGAY = '20000525'

--3. Lấy ra các thông tin gồm Mã hoá đơn, ngày lập hoá đơn, tên khách hàng, địa chỉ khách hàng và số điện thoại của những hoá đơn trong tháng 6/2000.
SELECT HOADON.MAHD, HOADON.NGAY, KHACHHANG.TENKH, KHACHHANG.DIACHI, KHACHHANG.DT  
FROM HOADON
LEFT JOIN KHACHHANG ON KHACHHANG.MAKH = HOADON.MAKH
WHERE HOADON.NGAY >= '20000601' and  HOADON.NGAY < '20000701'


--4. Lấy ra danh sách những khách hàng (tên khách hàng, địa chỉ, số điện thoại) đã mua hàng trong tháng 6/2000.
SELECT DISTINCT v.TENKH, v.DIACHI, v.DT  
FROM HOADON
JOIN (SELECT DISTINCT MAKH,TENKH, DIACHI, DT FROM KHACHHANG) v ON v.MAKH = HOADON.MAKH
WHERE HOADON.NGAY >= '20000601' and  HOADON.NGAY < '20000701'

SELECT DISTINCT v.TENKH, v.DIACHI, v.DT  
FROM HOADON
JOIN KHACHHANG v ON v.MAKH = HOADON.MAKH
WHERE HOADON.NGAY >= '20000601' and  HOADON.NGAY < '20000701'

--5. Lấy ra danh sách các mặt hàng được bán từ ngày 1/1/2000 đến ngày 1/7/2000. Thông tin gồm: mã vật tư, tên vật tư.
SELECT DISTINCT VATTU.MAVT, VATTU.TENVT
FROM VATTU
JOIN CHITIETHOADON ct on VATTU.MAVT = Ct.MAVT
JOIN HOADON h on ct.MAHD = h.MAHD
WHERE h.NGAY >= '20000601' and  h.NGAY < '20000701'

--6. Lấy ra danh sách các vật tư được bán từ ngày 1/1/2000 đến ngày 1/7/2000. Thông tin gồm: mã vật tư, tên vật tư, tên khách  hàng đã mua, ngày mua, số lượng mua.
SELECT  VATTU.MAVT, VATTU.TENVT, kh.TENKH, h.NGAY,ct.SL
FROM VATTU
JOIN CHITIETHOADON ct on VATTU.MAVT = Ct.MAVT
JOIN HOADON h on ct.MAHD = h.MAHD
JOIN KHACHHANG kh on h.MAKH = kh.MAKH
WHERE h.NGAY >= '20000101' and  h.NGAY < '20000701'

--7. Lấy ra danh sách các vật tư được mua bởi những khách hàng ở Tân Bình, trong năm 2000. Thông tin lấy ra gồm: mã vật tư, tên vật tư, tên khách hàng, ngày mua, số lượng mua.
SELECT  VATTU.MAVT, VATTU.TENVT, kh.TENKH, h.NGAY,ct.SL,kh.DIACHI
FROM VATTU
JOIN CHITIETHOADON ct on VATTU.MAVT = Ct.MAVT
JOIN HOADON h on ct.MAHD = h.MAHD
JOIN KHACHHANG kh on h.MAKH = kh.MAKH
WHERE h.NGAY >= '20000101' and  h.NGAY < '20010101' and kh.DIACHI = 'TAN BINH'
--8. Lấy ra danh sách các vật tư được mua bởi những khách hàng ở Tân Bình, trong năm 2000. Thông tin lấy ra gồm: mã vật tư, tên vật tư.
SELECT DISTINCT  VATTU.MAVT, VATTU.TENVT
FROM VATTU
JOIN CHITIETHOADON ct on VATTU.MAVT = Ct.MAVT
JOIN HOADON h on ct.MAHD = h.MAHD
JOIN KHACHHANG kh on h.MAKH = kh.MAKH
WHERE h.NGAY >= '20000101' and  h.NGAY < '20010101' and kh.DIACHI = 'TAN BINH'

--9. Lấy ra danh sách những khách hàng không mua hàng trong tháng 6/2000 gồm các thông tin tên khách hàng, địa chỉ, số điện thoại.

SELECT DISTINCT KHACHHANG.TENKH, KHACHHANG.DIACHI,KHACHHANG.DT FROM KHACHHANG
EXCEPT
SELECT DISTINCT kh.TENKH, kh.DIACHI, kh.DT
FROM HOADON h
JOIN KHACHHANG kh on h.MAKH = kh.MAKH
WHERE h.NGAY >= '20000601' and  h.NGAY < '20000701'
