-- DROP DATABASE dbfx16133

GO--A.TẠO DATABASE
CREATE DATABASE [dbfx16133];


GO
USE dbfx16133
--B.TẠO CÁC BẢNG + CÁC QUAN HỆ, RẰNG BUỘC
--Bảng Category
CREATE TABLE Category (
  category_id VARCHAR(10) PRIMARY KEY,
  cat_name VARCHAR(255) UNIQUE NOT NULL
);

--Bảng User (Sửa lại thành Account)
CREATE TABLE Account (
  userid VARCHAR(10) PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(64) CHECK (LEN(password) >= 6) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL
);

--Bảng Article
CREATE TABLE Article (
  article_id VARCHAR(10) PRIMARY KEY,
  title VARCHAR(255),
  excerpt TEXT,
  content TEXT NOT NULL,
  pub_date DATE,
  status VARCHAR(20) NOT NULL,
  created_date DATE NOT NULL,
  approved_date DATE,
  author_id VARCHAR(10) NOT NULL,
  FOREIGN KEY (author_id) REFERENCES Account(userid)
);

--Bảng Comment
CREATE TABLE Comment (
  comment_id VARCHAR(10) NOT NULL PRIMARY KEY,
  comment_content TEXT NOT NULL,
  status VARCHAR(20) NOT NULL,
  comment_date DATE NOT NULL,
  article_id VARCHAR(10) NOT NULL,
  FOREIGN KEY (article_id) REFERENCES Article(article_id),
  userid VARCHAR(10) NOT NULL,
  FOREIGN KEY (userid) REFERENCES Account(userid)
);

--Bảng Reporter
CREATE TABLE Reporter (
  userid VARCHAR(10) NOT NULL,
  promote_date DATE NOT NULL,
  PRIMARY KEY (userid, promote_date),
  FOREIGN KEY (userid) REFERENCES Account(userid)
);

--Bảng Editor
CREATE TABLE Editor (
  userid VARCHAR(10) NOT NULL,
  promote_date DATE NOT NULL,
  PRIMARY KEY (userid, promote_date), --Không sử dụng UNIQUE vì muốn người dùng có thể được nâng cấp chức danh nhiều lần 1 ngày 
  FOREIGN KEY (userid) REFERENCES Account(userid)
);

--Bảng ArticleCategory
CREATE TABLE ArticleCategory (
  article_id VARCHAR(10) NOT NULL,
  category_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (article_id, category_id),
  FOREIGN KEY (article_id) REFERENCES Article(article_id),
  FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

GO
-- ****** INPUT DEMO DATA ****** -- 
GO

INSERT INTO Account(userid, username, password, email)
VALUES
    ('U001', 'user1', 'password1', 'user1@gmail.com'),
    ('U002', 'user2', 'password2', 'user2@gmail.com'),
    ('U003', 'user3', 'password3', 'user3@gmail.com'),
    ('U004', 'user4', 'password4', 'user4@gmail.com'),
    ('U005', 'user5', 'password5', 'user5@gmail.com'),
    ('U006', 'user6', 'password6', 'user6@gmail.com'),
    ('U007', 'user7', 'password7', 'user7@gmail.com'),
    ('U008', 'user8', 'password8', 'user8@gmail.com'),
    ('U009', 'user9', 'password9', 'user9@gmail.com'),
    ('U010', 'user10', 'password10', 'user10@gmail.com');

INSERT INTO Article(article_id, title, excerpt, content, pub_date, status, created_date, approved_date,author_id)
VALUES 
    ('A001', 'Title 1', 'Excerpt 1', 'Content 1', '2022-01-01', 'published', '2022-01-01', '2022-01-02','U001'),
    ('A002', 'Title 2', 'Excerpt 2', 'Content 2', '2022-01-02', 'published', '2022-01-02', '2022-01-03','U001'),
    ('A003', 'Title 3', 'Excerpt 3', 'Content 3', '2022-01-03', 'draft', '2022-01-03', NULL,'U001'),
    ('A004', 'Title 4', 'Excerpt 4', 'Content 4', '2022-01-04', 'published', '2022-01-04', '2022-01-05','U001'),
    ('A005', 'Title 5', 'Excerpt 5', 'Content 5', '2022-01-05', 'published', '2022-01-05', '2022-01-06','U001'),
    ('A006', 'Title 6', 'Excerpt 6', 'Content 6', '2022-01-06', 'draft', '2022-01-06', NULL,'U001'),
    ('A007', 'Title 7', 'Excerpt 7', 'Content 7', '2022-01-07', 'published', '2022-01-07', '2022-01-08','U001'),
    ('A008', 'Title 8', 'Excerpt 8', 'Content 8', '2022-01-08', 'published', '2022-01-08', '2022-01-09','U001'),
    ('A009', 'Title 9', 'Excerpt 9', 'Content 9', '2022-01-09', 'published', '2022-01-09', '2022-01-10','U001'),
    ('A010', 'Title 10', 'Excerpt 10', 'Content 10', '2022-01-10', 'draft', '2022-01-10', NULL,'U001');

INSERT INTO Category(category_id, cat_name)
VALUES
    ('C001', 'Technology'),
    ('C002', 'Science'),
    ('C003', 'Politics'),
    ('C004', 'Sports'),
    ('C005', 'Entertainment'),
    ('C006', 'Health'),
    ('C007', 'Economics'),
    ('C008', 'Culture'),
    ('C009', 'Environment'),
    ('C010', 'Education')    ;

INSERT INTO ArticleCategory (article_id, category_id)
VALUES
  ('A001', 'C001'),
  ('A001', 'C002'),
  ('A002', 'C003'),
  ('A003', 'C002'),
  ('A003', 'C003'),
  ('A004', 'C001'),
  ('A005', 'C003'),
  ('A006', 'C001'),
  ('A007', 'C002'),
  ('A008', 'C003');

INSERT INTO Editor (userid, promote_date) 
VALUES 
	('U001', '2022-02-01'),
	('U002', '2022-02-01')	,
    ('U003', '2022-02-01'),
    ('U004', '2022-03-01'),
    ('U005', '2022-04-01'),
    ('U006', '2022-05-01'),
    ('U007', '2022-06-01'),
    ('U008', '2022-07-01'),
    ('U009', '2022-08-01'),
    ('U010', '2022-09-01');

INSERT INTO Reporter (userid, promote_date)
VALUES
	('U001', '2022-02-02'),
	('U002', '2022-02-02'),
    ('U004', '2022-02-02'),
    ('U005', '2022-03-03'),
    ('U006', '2022-04-04'),
    ('U007', '2022-05-05'),
    ('U008', '2022-06-06'),
    ('U009', '2022-07-07'),
    ('U010', '2022-08-08'),
    ('U011', '2022-09-09');

INSERT INTO Comment (comment_id, comment_content, status, comment_date, article_id, userid)
VALUES
    ('C001', 'Comment1', 'approved', '2023-04-20', 'A001', 'U001'),
    ('C002', 'comment2', 'pending', '2023-04-21', 'A002', 'U002'),
    ('C003', 'Comment3', 'approved', '2023-04-22', 'A003', 'U003'),
    ('C004', 'Comment4', 'pending', '2023-04-23', 'A004', 'U004'),
    ('C005', 'Comment5', 'approved', '2023-04-23', 'A001', 'U005'),
    ('C006', 'Comment6', 'approved', '2023-04-22', 'A002', 'U006'),
    ('C007', 'Comment7', 'pending', '2023-04-20', 'A003', 'U007'),
    ('C008', 'Comment8', 'approved', '2023-04-19', 'A004', 'U008'),
    ('C009', 'Comment9', 'pending', '2023-04-18', 'A001', 'U009'),
    ('C010', 'Comment10', 'approved', '2023-04-24', 'A002', 'U010');


GO
-- STORED PROCEDURE --
-- Tạo stored procedure: Tìm thông tin article_id, title và pub_date theo author 
CREATE PROCEDURE get_author_articles
@author_id VARCHAR(10)
AS
BEGIN
SELECT article_id, title, pub_date
FROM Article
WHERE Author_id = @author_id
ORDER BY pub_date DESC;
END

GO
EXEC get_author_articles @author_id = 'U001';


--Tạo Index -- 
GO
CREATE INDEX index_articleid ON Article (article_id);


-- TRIGGER --
-- Tạo trigger: Khi thay đổi status từ "draft" -> "published" sẽ update approved_date thành thời điểm  thay đổi status
GO
CREATE TRIGGER update_approved_date
ON Article
AFTER UPDATE
AS
BEGIN
  IF UPDATE(status) AND EXISTS (SELECT * FROM inserted WHERE status = 'published')
    BEGIN
        UPDATE Article SET approved_date = GETDATE() FROM Article a 
		JOIN inserted i ON a.article_id = i.article_id WHERE i.status = 'published'
    END;
END;
/*Câu lệnh test cho Trigger
UPDATE Article
SET status = 'Published'
WHERE article_id = 'A003';

UPDATE Article 
SET status = 'draft', approved_date = NULL 
WHERE article_id = 'A003';
*/

-- FUNCTION -- 
GO
-- Function đến số lượng bài viết đã xuất bản trong category
CREATE FUNCTION dbo.CountPublishedArticlesByCategory (@category_id VARCHAR(10))
RETURNS INT
AS
BEGIN
  DECLARE @count INT;
  SELECT @count = COUNT(*)
  FROM ArticleCategory ac 
  INNER JOIN Article a ON ac.article_id = a.article_id 
  WHERE ac.category_id = @category_id AND a.status = 'published';
  RETURN @count
END

GO
-- Execute Function
SELECT dbo.CountPublishedArticlesByCategory('C001') as PublishedArticlesCount


-- Hàm transaction (1) - Publish Article
GO
BEGIN TRANSACTION;
-- Update the status of an article from 'draft' to 'published'
UPDATE Article
SET status = 'published', approved_date = GETDATE()
WHERE article_id = 'A003' AND status = 'draft';
-- Check if the update was successful
IF @@ROWCOUNT = 0
BEGIN
    --The article was not a draft or not exist: ROLLBACK
    ROLLBACK TRANSACTION;
    PRINT 'Update failed: The article was not a draft or not exist';
END
ELSE
BEGIN
    -- Successfully Update
    COMMIT TRANSACTION;
    PRINT 'Article published successfully.';
END

GO
-- Hàm Transaction (2): Adding new comment to the article
BEGIN TRANSACTION;
DECLARE @NewCommentID VARCHAR(10) = 'C010';
DECLARE @CommentContent VARCHAR(200) = 'This is a new comment';
DECLARE @ArticleID VARCHAR(10) = 'A001';
DECLARE @UserID VARCHAR(10) = 'U002'; -- User adding the comment
DECLARE @Status VARCHAR(20) = 'pending'; -- Initial status of the comment
DECLARE @CommentDate DATE = GETDATE(); -- Use current date for comment date

IF EXISTS (SELECT 1 FROM Article WHERE article_id = @ArticleID AND status = 'published') --Check if the article is published
BEGIN
    INSERT INTO Comment (comment_id, comment_content, status, comment_date, article_id, userid)
    VALUES (@NewCommentID, @CommentContent, @Status, @CommentDate, @ArticleID, @UserID);
    IF @@ROWCOUNT = 0 --Check if the comment is published
    BEGIN
        ROLLBACK TRANSACTION;
        PRINT 'Insert failed: Unable to add comment.';
    END
    ELSE
    BEGIN
        COMMIT TRANSACTION;
        PRINT 'Comment added successfully.';
    END
END
ELSE
BEGIN
    ROLLBACK TRANSACTION;
    PRINT 'Insert failed: Article is not published or no exist.';
END
--SELECT * FROM Comment WHERE comment_id = 'C010'



