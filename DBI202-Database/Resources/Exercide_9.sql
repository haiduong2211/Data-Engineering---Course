
-- 1. Xoá dữ liệu khách hàng có mã KH02
DROP PROCEDURE IF EXISTS DeleteCustomer;
GO
CREATE PROCEDURE DeleteCustomer
    @MAKH NVARCHAR(50) = 'KH02'
AS
BEGIN
    -- Enable error handling
    BEGIN TRY 
        -- Start a transaction
        BEGIN TRANSACTION;
		DELETE CT
		FROM CHITIETHOADON as CT
		JOIN HOADON as HD
		ON HD.MAHD = CT.MAHD
		WHERE HD.MAKH = @MAKH
        -- Step 1: Delete related records in dbo.HOADON
        DELETE FROM dbo.HOADON
        WHERE MAKH = @MAKH;
        -- Step 2: Delete the customer from dbo.KHACHHANG
        DELETE FROM dbo.KHACHHANG
        WHERE MAKH = @MAKH;
        -- Commit the transaction
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- If error, rollback transaction
        ROLLBACK TRANSACTION;
		DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
		RAISERROR(@ErrorMessag,16,1);
    END CATCH
END
EXEC DeleteCustomer @MAKH = 'KH02'

-- 2. Xoá tất cả khách hàng ở quận TAN BINH
DROP PROCEDURE IF EXISTS DeleteCustomer;
GO
CREATE PROCEDURE DeleteCustomerTanBinh
AS
BEGIN
    -- Enable error handling
    BEGIN TRY 
        -- Start a transaction
        BEGIN TRANSACTION;
		-- Step 1: Delete related records in dbo.CHITIETHOADON
		DELETE CT
		FROM CHITIETHOADON as CT
		JOIN HOADON as HD
		ON HD.MAHD = CT.MAHD
		JOIN KHACHHANG as KH
		ON KH.MAKH = HD.MAKH
		WHERE KH.DIACHI LIKE '%TAN BINH%';
        -- Step 2: Delete related records in dbo.HOADON
        DELETE HD FROM dbo.HOADON as HD
		INNER JOIN dbo.KHACHHANG as KH
		ON KH.MAKH = HD.MAKH
        WHERE KH.DIACHI LIKE '%TAN BINH%';
        -- Step 2: Delete the customer from dbo.KHACHHANG
        DELETE FROM dbo.KHACHHANG
        WHERE KHACHHANG.DIACHI LIKE '%TAN BINH%';
        -- Commit the transaction
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- If error, rollback transaction
        ROLLBACK TRANSACTION;
		DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
		RAISERROR(@ErrorMessag,16,1);
    END CATCH
END
EXEC DeleteCustomerTanBinh


-- 3. Xóa tất cả vật tư có giá mua < 1000
DELETE FROM VATTU 
WHERE GIAMUA < 1000;

GO 
CREATE PROCEDURE DeleteVTLessThan1000 AS
BEGIN
	BEGIN TRY
		BEGIN TRANSACTION
		-- Step 1: Delete records from Chitiethoadon
		DELETE CT FROM CHITIETHOADON as CT
		JOIN VATTU as VT
		ON VT.MAVT  = CT.MAVT
		WHERE VT.GIAMUA <1000;
		-- Step 2: Delte records from VATTU
		DELETE FROM VATTU
		WHERE VATTU.GIAMUA <1000
		COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
        -- If error, rollback transaction
        ROLLBACK TRANSACTION;
		DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
		RAISERROR(@ErrorMessage,16,1);
	END CATCH
END
EXEC DeleteVTLessThan1000 

-- 4. Cập nhật giá bán vật tư có mã VT05 tăng thêm 10%
UPDATE CHITIETHOADON
SET GIABAN = GIABAN * 1.10
WHERE MAVT ='VT05'

SELECT * FROM CHITIETHOADON

--5. Cập nhật giá bán của tất cả các vật tư trong mục chi tiết hoá đơn tăng thêm 10% của hoá đơn HD009
GO
UPDATE CHITIETHOADON
SET GIABAN = GIABAN * 1.1
WHERE MAHD = 'HD009'

SELECT * FROM CHITIETHOADON
WHERE MAHD = 'HD009'

