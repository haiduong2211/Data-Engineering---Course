G
USE dbfx16133
-- ****** INPUT DEMO DATA ****** -- 
GO
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
    ('C005', 'Entertainment');
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
    ('U009', 'user9', 'password9', 'user9@gmail.com');
INSERT INTO Editor (userid, promote_date) 
VALUES 
	('U001', '2022-01-01'),
	('U002', '2022-01-02');
INSERT INTO Reporter (userid, promote_date)
VALUES
	('U001', '2022-01-01'),
	('U003', '2022-01-03');
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
    ('C009', 'Comment9', 'pending', '2023-04-18', 'A001', 'U009');

