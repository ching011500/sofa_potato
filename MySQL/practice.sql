-- CREATE DATABASE school;
USE school;

-- CREATE TABLE students (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     age INT,
--     class_id INT,
--     gender VARCHAR(10)
-- );

-- CREATE TABLE classes (
--     id INT PRIMARY KEY,
--     class_name VARCHAR(50),
--     teacher_id INT
-- );

-- CREATE TABLE teachers (
--     id INT PRIMARY KEY,
--     name VARCHAR(100),
--     subject VARCHAR(50)
-- );

-- 教師資料
-- INSERT INTO teachers VALUES
-- (1, '張老師', '數學'),
-- (2, '李老師', '英文'),
-- (3, '王老師', '自然');

-- 班級資料
-- INSERT INTO classes VALUES
-- (101, '數學A班', 1),
-- (102, '英文B班', 2),
-- (103, '自然C班', 3);

-- 學生資料
-- INSERT INTO students VALUES
-- (NULL, '小明', 16, 101, '男'),
-- (NULL, '小美', 15, 102, '女'),
-- (NULL, '小華', 17, 101, '男'),
-- (NULL, '小綠', 16, 103, '女'),
-- (NULL, '小藍', 17, NULL, '男');

-- 1：查詢每位學生的班級名稱與導師姓名
SELECT s.name AS 學生, c.class_name, t.name AS 導師
FROM students s
LEFT JOIN classes c ON s.class_id = c.id
LEFT JOIN teachers t ON c.teacher_id = t.id;

-- 2：列出沒有班級的學生
SELECT name FROM students
WHERE class_id IS NULL;

-- 3：統計每位導師底下的學生人數
SELECT t.name AS 導師, COUNT(s.id) AS 學生人數
FROM teachers t
LEFT JOIN classes c ON t.id = c.teacher_id
LEFT JOIN students s ON c.id = s.class_id
GROUP BY t.name;

-- 4：找出比全體平均年齡高的學生
SELECT name, age
FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);

-- 5：依年齡分類學生（CASE WHEN）
SELECT name, age,
    CASE
        WHEN age < 16 THEN '低年級'
        WHEN age BETWEEN 16 AND 17 THEN '中年級'
        ELSE '高年級'
    END AS 年級分類
FROM students;

-- 6：建立索引觀察效能
CREATE INDEX idx_age ON students(age);
-- 再執行以下 EXPLAIN 查看是否有用到索引
EXPLAIN SELECT * FROM students WHERE age = 17;