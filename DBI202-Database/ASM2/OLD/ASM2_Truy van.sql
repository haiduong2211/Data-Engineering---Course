-- Truy vấn dữ liệu trên một bảng
SELECT title, pub_date, status,created_date FROM Article

-- Truy vấn có sử dụng Order by
SELECT * FROM Comment
ORDER BY comment_date, userid

-- Truy vấn sử dụng toán tử Like và các so sánh xâu ký tự.
SELECT * FROM Article
WHERE title LIKE '%1%' 

-- Truy vấn liên quan tới điều kiện về thời gian
SELECT * FROM Article
WHERE pub_date BETWEEN '2022-01-8' AND '2022-01-31';

SELECT * FROM Article
WHERE pub_date BETWEEN '2022-01-07' AND '2022-01-31'
AND approved_date is not NULL

-- Truy vấn dữ liệu từ nhiều bảng sử dụng Inner join
SELECT Article.article_id, Article.title, Category.cat_name
FROM Article
INNER JOIN ArticleCategory ON Article.article_id = ArticleCategory.article_id
INNER JOIN Category ON Category.category_id = ArticleCategory.category_id;

-- Truy vấn sử dụng Self join, Outer join.
SELECT u1.username, u2.username AS referral_username
FROM Account u1
INNER JOIN Account u2 ON u1.userid = u2.userid;

--Truy vấn sử dụng truy vấn con.
-- Tìm những người có trên 2 bài viết
SELECT DISTINCT Author_id
FROM Article
WHERE status = 'published' AND Author_id IN (
  SELECT Author_id
  FROM Article
  WHERE status = 'published'
  GROUP BY Author_id
  HAVING COUNT(*) >= 2
);

-- Truy vấn sử dụng With.
-- Tổng số bài viết được xuất bản theo từng tháng
WITH PublishedArticles AS (
  SELECT YEAR(pub_date) AS PubYear, MONTH(pub_date) AS PubMonth, COUNT(*) AS TotalPublished
  FROM Article
  WHERE status = 'published'
  GROUP BY YEAR(pub_date), MONTH(pub_date)
)
SELECT PubYear, PubMonth, TotalPublished
FROM PublishedArticles
ORDER BY PubYear, PubMonth;

-- Truy vấn thống kê sử dụng Group by và Having
-- Thống kê những người có trên 2 bài viết kèm theo số bài viết 
SELECT author_id, COUNT(*) AS num_articles
FROM Article
WHERE status = 'published'
GROUP BY author_id
HAVING COUNT(*) >= 2;

--Truy vấn sử dụng function (hàm) đã viết trong bước trước.
SELECT cat_name, dbo.CountPublishedArticlesByCategory(category_id) AS published_articles_count
FROM Category
