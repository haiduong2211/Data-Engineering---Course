CREATE TABLE KHACHHANG(
MAKH nvarchar(5) NOT NULL,
TENKH nvarchar(30) NOT NULL,
DIACHI nvarchar(300) NULL,
DT varchar(10) NOT NULL,
EMAIL varchar(30) NOT NULL,
CONSTRAINT MAKH_PK PRIMARY KEY(MAKH)
)
CREATE TABLE VATTU(
MAVT nvarchar(5) NOT NULL,
TENVT nvarchar(30) NOT NULL,
DVT nvarchar(20) NOT NULL,
GIAMUA money,
SLTON int,
CONSTRAINT MAVT_PK PRIMARY KEY(MAVT)
)

CREATE TABLE HOADON(
MAHD nvarchar(10) NOT NULL,
NGAY datetime NOT NULL,
MAKH nvarchar(5) NOT NULL,
TONGTG money,
CONSTRAINT MAHD_PK PRIMARY KEY(MAHD)
)

CREATE TABLE CHITIETHOADON(
MAHD nvarchar(10) NOT NULL,
MAVT nvarchar(5) NOT NULL,
SL int NOT NULL,
GIABAN money NOT NULL,
CONSTRAINT CHITIETHD_PK PRIMARY KEY(MAHD,MAVT)
)