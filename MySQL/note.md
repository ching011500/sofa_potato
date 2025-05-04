# MySQL workbench
## 🧱 單元 1：資料庫與資料表操作

本單元介紹如何在 MySQL 中：
- 建立與刪除資料庫
- 建立與刪除資料表
- 選擇要操作的資料庫

---

### 📂 1. 建立資料庫

```sql
CREATE DATABASE 資料庫名稱;
```

---

### 🗂 2. 查看目前有哪些資料庫

```sql
SHOW DATABASES;
```

---

### ✅ 3. 選擇要使用的資料庫

```sql
USE 資料庫名稱;
```

---

### ❌ 4. 刪除資料庫

```sql
DROP DATABASE 資料庫名稱;
```

⚠️ **注意：刪除後資料無法復原，請小心使用。**

---

### 📋 5. 建立資料表

```sql
CREATE TABLE 資料表名稱 (
    欄位名稱1 資料型別 [約束條件],
    欄位名稱2 資料型別 [約束條件],
    ...
);
```

🔸 範例：
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    department VARCHAR(50)
);
```

---

### 🔎 6. 查看目前有哪些資料表

```sql
SHOW TABLES;
```

---

### 🧾 7. 查看資料表結構

```sql
DESCRIBE 資料表名稱;
```

---

### ❌ 8. 刪除資料表

```sql
DROP TABLE 資料表名稱;
```

---

### 🛠 常用資料型別補充

| 型別       | 說明                     |
|------------|--------------------------|
| `INT`      | 整數                     |
| `VARCHAR(n)` | 可變長度文字（最多 n 字元） |
| `DATE`     | 日期（yyyy-mm-dd）       |
| `DATETIME` | 日期與時間               |
| `FLOAT`    | 浮點數                   |
| `BOOLEAN`  | 布林值（0 或 1）         |

---

### 📌 小提醒

- 每次使用 `USE 資料庫名稱;` 要確認目前操作哪個資料庫。
- 若欄位要自動遞增，使用 `AUTO_INCREMENT`。
- 主鍵用 `PRIMARY KEY` 設定，確保資料唯一性。

---

## 🧱 單元 2：資料表完整性與約束（PRIMARY KEY, FOREIGN KEY, UNIQUE）

本延伸單元補充單元 1，說明如何在建立資料表時：
- 設定主鍵（PRIMARY KEY）保證資料唯一
- 使用唯一約束（UNIQUE）避免重複資料
- 建立外鍵（FOREIGN KEY）建立表格間的關聯
- 加強資料的一致性與正確性

---

### 🔐 1. 主鍵 PRIMARY KEY

主鍵為資料表中可唯一識別每筆資料的欄位，**不允許 NULL、不可重複**。

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
);
```

📌 也可以分開寫在最後一行：

```sql
CREATE TABLE employees (
    id INT,
    name VARCHAR(100),
    salary INT,
    PRIMARY KEY (id)
);
```

---

### 🔁 2. 自動遞增主鍵（AUTO_INCREMENT）

常與主鍵搭配，讓每筆新資料自動生成流水號：

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    salary INT
);
```

📌 插入資料時可略過 `id` 欄位，系統自動補上數字。

---

### 🆔 3. 唯一約束 UNIQUE

防止某欄位出現重複值（例如 email），允許 NULL。

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    username VARCHAR(50)
);
```

---

### 🧩 4. 外鍵 FOREIGN KEY

連接兩張表，讓子表中的欄位必須對應到主表中的值。

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

📌 `employees.dept_id` 需對應 `departments.dept_id`。

---

### 🔄 5. 設定外鍵連動行為（ON DELETE / ON UPDATE）

```sql
FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
ON DELETE CASCADE
ON UPDATE CASCADE
```

| 動作 | 說明 |
|------|------|
| `CASCADE` | 主表刪除時，子表也刪除 |
| `SET NULL` | 主表刪除時，子表設為 NULL |
| `RESTRICT`（預設） | 不允許刪除或更新主表資料 |

---

### 📌 小提醒

- 每張表只能有一個 `PRIMARY KEY`，但可以有多個 `UNIQUE`。
- 設定外鍵時，資料型別需一致，且主表必須先存在。
- 記得為外鍵表設定索引以提升查詢效率。

---

## 📥 單元 3：插入資料（INSERT）

本單元介紹如何在 MySQL 中：
- 插入單筆或多筆資料
- 插入時指定欄位或全部欄位
- 注意資料格式與錯誤處理

---

### ✏️ 1. 插入資料

#### 插入單筆資料

```sql
INSERT INTO 資料表名稱 (欄位1, 欄位2, ...) 
VALUES (值1, 值2, ...);
```

#### 插入多筆資料

```sql
INSERT INTO 資料表名稱 (欄位1, 欄位2, ...) 
VALUES 
(值1_1, 值1_2, ...),
(值2_1, 值2_2, ...),
...;
```

🔸 範例：
```sql
INSERT INTO employees (name, age, department)
VALUES
('Bob', 28, 'Marketing'),
('Charlie', 35, 'HR'),
('Diana', 40, 'IT');
```

---

### ✏️ 2. 不指定欄位（所有欄位都要提供值）

```sql
INSERT INTO 資料表名稱 
VALUES (值1, 值2, 值3, ...);
```

⚠️ **注意：** 欄位順序要與資料表完全一致，否則會出錯。

🔸 範例（假設欄位為 id, name, age, department）：
```sql
INSERT INTO employees 
VALUES (NULL, 'Evan', 26, 'Finance');
```

---

### 📌 小提醒

- 若使用 `AUTO_INCREMENT`，可將主鍵欄位設為 `NULL` 或省略不填。
- 插入文字類型（`VARCHAR`）時，請使用 `'單引號'`。
- 插入日期格式請用 `YYYY-MM-DD`，例如 `'2025-04-15'`。

---

## ✍️ 單元 4：修改與刪除資料（UPDATE / DELETE）

本單元介紹如何在 MySQL 中：
- 修改現有資料（UPDATE）
- 刪除資料列（DELETE）
- 搭配 WHERE 條件使用，避免誤更新或誤刪除

---

### ✍️ 1. 修改資料（UPDATE）

```sql
UPDATE 資料表名稱
SET 欄位1 = 新值1, 欄位2 = 新值2, ...
WHERE 條件;
```

🔸 範例：將員工編號為 3 的名字改為 Kevin，部門改為 IT：

```sql
UPDATE employees
SET name = 'Kevin', department = 'IT'
WHERE id = 3;
```

---

### ✍️ 2. 小心沒有 WHERE 的 UPDATE

```sql
UPDATE employees
SET department = 'HR';
```

⚠️ **沒有 WHERE 條件會導致整張表格所有資料都被更新！**

---

### ✍️ 3. 刪除資料（DELETE）

```sql
DELETE FROM 資料表名稱
WHERE 條件;
```

🔸 範例：刪除名字為 "Tom" 的員工：

```sql
DELETE FROM employees
WHERE name = 'Tom';
```

---

### ✍️ 4. 小心沒有 WHERE 的 DELETE

```sql
DELETE FROM employees;
```

⚠️ **會刪除整張表格的所有資料！建議先備份再操作。**

---

### ✍️ 5. 結合條件操作

🔸 範例：將所有年齡小於 25 歲的員工部門改為 "實習部門"：

```sql
UPDATE employees
SET department = '實習部門'
WHERE age < 25;
```

🔸 範例：刪除所有薪資為 NULL 的資料：

```sql
DELETE FROM employees
WHERE salary IS NULL;
```

---

### 📌 小提醒

- **UPDATE / DELETE 一定要搭配 WHERE**，避免全表操作錯誤。
- 執行前建議先 `SELECT` 條件看看會有哪些資料被影響。
- 若資料庫支援，可先 `BEGIN TRANSACTION` 試操作，確認無誤再 COMMIT。

---

## 🔍 單元 5：查詢資料（SELECT, REGEXP）

本單元介紹如何在 MySQL 中：
- 查詢資料表內容
- 選擇特定欄位
- 欄位加上別名
- 基本運算與簡單函數應用
- 使用正則表達式（REGEXP）進行進階比對

---

### 📑 1. 查詢整張資料表

```sql
SELECT * FROM 資料表名稱;
```

🔸 範例：
```sql
SELECT * FROM employees;
```

---

### 📑 2. 查詢特定欄位

```sql
SELECT 欄位1, 欄位2, ... FROM 資料表名稱;
```

🔸 範例：
```sql
SELECT name, department FROM employees;
```

---

### 📑 3. 欄位加上別名（AS）

```sql
SELECT 欄位名稱 AS 別名 FROM 資料表名稱;
```

🔸 範例：
```sql
SELECT name AS 姓名, age AS 年齡 FROM employees;
```

---

### 📑 4. 欄位基本運算

```sql
SELECT 欄位1 + 欄位2 AS 新欄位名稱 FROM 資料表名稱;
```

🔸 範例：
```sql
SELECT base_salary + bonus AS total_salary
FROM employees;
```

---

### 📑 5. 使用簡單內建函數

| 函數 | 說明 |
|------|------|
| `COUNT(欄位)` | 計算資料筆數 |
| `SUM(欄位)` | 計算總和 |
| `AVG(欄位)` | 計算平均值 |
| `MAX(欄位)` | 找最大值 |
| `MIN(欄位)` | 找最小值 |

🔸 範例（計算平均年齡）：
```sql
SELECT AVG(age) AS 平均年齡 FROM employees;
```

---

### 📑 6. 使用 REGEXP 進行正則比對（進階文字篩選）

```sql
SELECT 欄位 
FROM 資料表名稱
WHERE 欄位 REGEXP '正則表達式';
```

- `REGEXP` 比 `LIKE` 更強，可以用模式範圍、選擇等。

🔸 範例（查詢名字中有字母 a 或 e）：
```sql
SELECT * 
FROM employees
WHERE name REGEXP 'a|e';
```

🔸 範例（名字以大寫字母開頭）：
```sql
SELECT * 
FROM employees
WHERE name REGEXP '^[A-Z]';
```

---

### 📌 小提醒

- `*` 代表選取所有欄位，但正式開發建議指名欄位以提升效率。
- 使用 `AS` 設定別名時可以讓結果更易讀。
- `REGEXP` 適合做複雜文字比對，注意語法格式。

---

## 🎯 單元 6：條件查詢（WHERE, NULL, IN, LIKE）

本單元介紹如何在 MySQL 中：
- 使用 WHERE 子句設定條件篩選資料
- 多條件組合（AND、OR、NOT）
- 進階條件查詢（BETWEEN、IN、LIKE）
- 判斷空值（NULL）

---

### 🎯 1. 基本條件查詢（WHERE）

```sql
SELECT 欄位 
FROM 資料表名稱
WHERE 條件式;
```

🔸 範例：
```sql
SELECT * 
FROM employees
WHERE department = 'Sales';
```

🔸 範例：
```sql
SELECT * FROM employees
WHERE age > 30;
```

---

### 🎯 2. 多條件組合（AND、OR、NOT）

- `AND`：兩個條件都成立
- `OR`：其中一個條件成立
- `NOT`：條件不成立時成立

🔸 範例（AND）：
```sql
SELECT * 
FROM employees
WHERE department = 'Sales' AND age > 30;
```

🔸 範例（OR）：
```sql
SELECT * 
FROM employees
WHERE department = 'Sales' OR department = 'HR';
```

🔸 範例（NOT）：
```sql
SELECT * 
FROM employees
WHERE NOT department = 'IT';
```

---

### 🎯 3. 使用 BETWEEN 範圍查詢

```sql
SELECT * 
FROM employees
WHERE age BETWEEN 25 AND 35;
```

---

### 🎯 4. 使用 IN 指定多個值

```sql
SELECT * 
FROM employees
WHERE department IN ('Sales', 'HR', 'Marketing');
```

---

### 🎯 5. 使用 LIKE 模糊查詢

- `%`：任意多個字元
- `_`：單一個字元

🔸 範例：
```sql
SELECT * 
FROM employees
WHERE name LIKE 'A%';
```

---

### 🎯 6. 判斷 NULL 值（IS NULL / IS NOT NULL）

```sql
SELECT 欄位 
FROM 資料表名稱
WHERE 欄位 IS NULL;
```

🔸 查詢欄位為空值：
```sql
SELECT * 
FROM employees
WHERE department IS NULL;
```

```sql
SELECT * 
FROM employees
WHERE department IS NOT NULL;
```

---

### 📌 小提醒

- `BETWEEN` 是包含邊界的（≥ 最小值且 ≤ 最大值）。
- `IN` 可以取代多個 OR 條件。
- `LIKE` 適合文字篩選，但對大小寫敏感與否取決於資料庫設定。
- `NULL` 不能直接用 `= NULL`，要用 `IS NULL` 或 `IS NOT NULL`。

---

## 🧮 單元 7：排序與限制（ORDER BY, LIMIT）

本單元介紹如何在 MySQL 中：
- 排序查詢結果
- 限制回傳筆數
- 搭配篩選與排序一起使用

---

### 🧮 1. 排序查詢結果（ORDER BY）

```sql
SELECT 欄位 
FROM 資料表名稱
ORDER BY 欄位 [ASC|DESC];
```

- `ASC`：升冪（由小到大，預設）
- `DESC`：降冪（由大到小）

🔸 範例（按年齡由小到大）：
```sql
SELECT * 
FROM employees
ORDER BY age ASC;
```

🔸 範例（按年齡由大到小）：
```sql
SELECT * 
FROM employees
ORDER BY age DESC;
```

---

### 🧮 2. 同時依多個欄位排序

```sql
SELECT 欄位 
FROM 資料表名稱
ORDER BY 欄位1 [ASC|DESC], 欄位2 [ASC|DESC];
```

🔸 範例（先依部門排序，同部門內再依年齡降冪）：
```sql
SELECT * 
FROM employees
ORDER BY department ASC, age DESC;
```

---

### 🧮 3. 限制回傳筆數（LIMIT）

```sql
SELECT 欄位 
FROM 資料表名稱
LIMIT 數量;
```

🔸 範例（只取前3筆）：
```sql
SELECT * 
FROM employees
LIMIT 3;
```

---

### 🧮 4. 分頁查詢（LIMIT + OFFSET）

```sql
SELECT 欄位 
FROM 資料表名稱
LIMIT 偏移量, 筆數;
```
或寫成
```sql
SELECT 欄位 
FROM 資料表名稱
LIMIT 筆數 OFFSET 偏移量;
```

- **偏移量（OFFSET）**：跳過幾筆資料
- **筆數（LIMIT）**：取出幾筆資料

🔸 範例（跳過前5筆，取出3筆）：
```sql
SELECT * FROM employees
LIMIT 5, 3;
```
或
```sql
SELECT * FROM employees
LIMIT 3 OFFSET 5;
```

---

### 📌 小提醒

- `ORDER BY` 必須在 `LIMIT` 之前。
- `LIMIT` 主要用於控制資料筆數或分頁顯示。
- 分頁查詢常搭配 `ORDER BY`，保證資料順序穩定。

---

## 🧩 單元 8：群組與統計（GROUP BY, HAVING）

本單元介紹如何在 MySQL 中：
- 使用 GROUP BY 將資料分組
- 搭配聚合函數進行每組的統計
- 使用 HAVING 設定分組後的篩選條件

---

### 🧩 1. 基本分組（GROUP BY）

```sql
SELECT 欄位, 聚合函數(欄位)
FROM 資料表名稱
GROUP BY 欄位;
```

🔸 範例（各部門員工人數）：
```sql
SELECT department, COUNT(*) AS 員工數
FROM employees
GROUP BY department;
```

🔸 範例（各部門平均年齡）：
```sql
SELECT department, AVG(age) AS 平均年齡
FROM employees
GROUP BY department;
```

---

### 🧩 2. 分組後條件篩選（HAVING）

- `WHERE` 是在分組**之前**篩選
- `HAVING` 是在分組**之後**篩選

```sql
SELECT 欄位, 聚合函數(欄位)
FROM 資料表名稱
GROUP BY 欄位
HAVING 條件式;
```

🔸 範例（只顯示員工人數超過 5 人的部門）：
```sql
SELECT department, COUNT(*) AS 員工數
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

---

### 🧩 3. 結合 WHERE 與 HAVING

- `WHERE`：先篩選原始資料
- `GROUP BY`：分組
- `HAVING`：篩選分組結果

🔸 範例（只考慮年齡超過 25 歲的員工，再統計每個部門平均年齡大於30的部門）：

```sql
SELECT department, AVG(age) AS 平均年齡
FROM employees
WHERE age > 25
GROUP BY department
HAVING AVG(age) > 30;
```

---

### 📌 小提醒

- `GROUP BY` 後，SELECT 的欄位要不是聚合函數，就是出現在 GROUP BY 裡。
- `HAVING` 主要搭配聚合結果（如 COUNT、AVG）使用。
- `WHERE` 不能直接搭配聚合函數，要用 HAVING！

---

## 🧠 單元 9：CASE WHEN 條件判斷

本單元介紹如何在 MySQL 中：
- 使用 `CASE WHEN` 根據條件分類
- 在查詢中建立條件欄位（如高薪 / 低薪）
- 與 GROUP BY、ORDER BY 等結合使用

---

### 🧠 1. 基本語法

```sql
SELECT
    CASE
        WHEN 條件1 THEN 結果1
        WHEN 條件2 THEN 結果2
        ...
        ELSE 預設結果
    END AS 欄位別名
FROM 資料表名稱;
```

🔸 範例：薪資分類

假設有 `salary` 欄位，分類為「高薪」、「中薪」、「低薪」：

```sql
SELECT name, salary,
    CASE
        WHEN salary >= 60000 THEN '高薪'
        WHEN salary >= 30000 THEN '中薪'
        ELSE '低薪'
    END AS 薪資等級
FROM employees;
```

🔸 範例：年齡分群

```sql
SELECT name, age,
    CASE
        WHEN age < 30 THEN '年輕族群'
        WHEN age BETWEEN 30 AND 50 THEN '中壯年'
        ELSE '高齡族群'
    END AS 年齡分類
FROM employees;
```

---

### 🧠 2. 搭配聚合函數使用（GROUP BY 前分類）

```sql
SELECT 
    CASE
        WHEN age < 30 THEN '年輕族群'
        WHEN age BETWEEN 30 AND 50 THEN '中壯年'
        ELSE '高齡族群'
    END AS 年齡群,
    COUNT(*) AS 人數
FROM employees
GROUP BY 年齡群;
```

---

### 🧠 3. 搭配 ORDER BY 使用（分類後排序）

```sql
SELECT name, salary,
    CASE
        WHEN salary >= 60000 THEN '高薪'
        ELSE '一般'
    END AS 薪資等級
FROM employees
ORDER BY 薪資等級 DESC;
```

---

### 📌 小提醒

- `CASE WHEN` 通常用在 SELECT 中創造「分類欄位」。
- 可以搭配 `GROUP BY` 做統計、搭配 `ORDER BY` 做排序。
- `ELSE` 是預設情況（沒有符合時使用），可省略，但建議保留！

---

## 🪜 單元 10：子查詢（Subquery）

本單元介紹如何在 MySQL 中：
- 在 SELECT、WHERE、FROM 中嵌套子查詢
- 找出與某些條件相比的值（如最大薪資）
- 使用子查詢進行巢狀查詢與交叉比對

---

### 🪜 1. 子查詢是什麼？

子查詢（Subquery）是一個「內部查詢」，嵌套在其他查詢中。  
常見用在：

- `WHERE` 子句內：找出「大於平均值」之類的條件
- `SELECT` 中：查出與其它欄位比較的值
- `FROM` 中：將子查詢視為一個臨時表格

---

### 🪜 2. 子查詢 in WHERE（條件比對）

```sql
SELECT * FROM employees
WHERE salary > (
    SELECT AVG(salary) FROM employees
);
```

📌 找出薪資高於所有員工平均薪資的人

---

### 🪜 3. 子查詢 in SELECT（顯示比較值）

```sql
SELECT name, salary,
    (SELECT AVG(salary) FROM employees) AS 全體平均薪資
FROM employees;
```

📌 顯示每個員工薪資，並附上全體平均薪資欄位

---

### 🪜 4. 子查詢 in FROM（當作臨時表）

```sql
SELECT 部門, 平均薪資
FROM (
    SELECT department AS 部門, AVG(salary) AS 平均薪資
    FROM employees
    GROUP BY department
) AS 部門薪資統計
WHERE 平均薪資 > 50000;
```

📌 找出平均薪資超過 50000 的部門  
（這種查詢方式也可搭配 JOIN 或報表統計）

---

### 🪜 5. 使用 IN 搭配子查詢

```sql
SELECT name FROM employees
WHERE department IN (
    SELECT department FROM employees
    WHERE salary > 60000
);
```

📌 查詢出現過「高薪員工」的部門中的所有員工

---

### 📌 小提醒

- 子查詢可搭配 `IN`, `=`, `<`, `>`, `BETWEEN`, `EXISTS` 等使用。
- 子查詢要放在小括號 `()` 中。
- 使用 `FROM (...) AS 暫名` 時記得加上別名（AS xxx）。

---

## 🔗 單元 11：多表 JOIN 查詢

本單元介紹 MySQL 中的多表查詢技術，透過 JOIN 將不同資料表之間的資料**整合起來使用**。  
JOIN 是資料分析與報表製作中最核心的工具之一。

本單元拆分為以下 9 個子單元：

---

### 🔗 11.1 INNER JOIN（內部連接）

只保留兩張表中「關聯欄位符合」的資料（交集）。

```sql
SELECT A.欄位, B.欄位
FROM 表A
INNER JOIN 表B
ON 表A.關聯欄位 = 表B.關聯欄位;
```

🔸 範例：

```sql
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;
```

---

### 🔗 11.2 LEFT JOIN（左外部連接）

保留左表所有資料，若右表找不到對應則以 NULL 補上。

```sql
SELECT A.欄位, B.欄位
FROM 表A
LEFT JOIN 表B
ON 表A.關聯欄位 = 表B.關聯欄位;
```

🔸 範例：

```sql
SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id;
```

---

### 🔗 11.3 RIGHT JOIN（右外部連接）

保留右表所有資料，若左表無配對資料則以 NULL 補上。

```sql
SELECT A.欄位, B.欄位
FROM 表A
RIGHT JOIN 表B
ON 表A.關聯欄位 = 表B.關聯欄位;
```

🔸 範例：

```sql
SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments
ON employees.dept_id = departments.dept_id;
```

---

### 🔗 11.4 FULL OUTER JOIN（完整外部連接）

MySQL 不支援 FULL OUTER JOIN，可用 UNION 組合 LEFT + RIGHT JOIN 模擬：

```sql
SELECT A.*, B.*
FROM A
LEFT JOIN B ON A.key = B.key

UNION

SELECT A.*, B.*
FROM A
RIGHT JOIN B ON A.key = B.key;
```

---

### 🔗 11.5 SELF JOIN（自己 JOIN 自己）

用來比對同張表中不同列的資料，必須使用別名。

🔸 範例：找出員工與他們的主管名稱（假設主管也是員工）

```sql
SELECT e1.name AS 員工, e2.name AS 主管
FROM employees AS e1
JOIN employees AS e2
ON e1.manager_id = e2.id;
```

---

### 🔗 11.6 多層 JOIN（3 表以上）

可依照需求串接多張資料表（通常從最主要的那張表開始 JOIN）。

```sql
SELECT e.name, d.dept_name, l.location
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN locations l ON d.loc_id = l.loc_id;
```

---

### 🔗 11.7 JOIN + GROUP BY（實務統計應用）

JOIN 串接後再進行分組統計分析。

🔸 範例：統計每個部門的員工人數

```sql
SELECT d.dept_name, COUNT(*) AS 員工數
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

---

### 📌 小提醒

- JOIN 條件不明確會造成「笛卡兒積」錯誤結果！
- JOIN 的欄位資料型別必須相容（建議型別一致）
- 常搭配別名（AS）簡化程式碼
- 多 JOIN 時務必注意順序與資料邏輯關係

---

## 📅 單元 12：處理日期與時間（NOW, CURDATE, DATE_FORMAT）

本單元介紹如何在 MySQL 中：
- 取得現在時間與日期
- 篩選特定時間範圍資料（例如：今天、本月、近7天）
- 自訂時間格式輸出
- 使用日期函數進行計算與轉換

---

### 📅 1. 取得目前時間與日期

| 函數 | 說明 |
|------|------|
| `NOW()` | 取得現在的日期與時間（yyyy-mm-dd hh:mm:ss） |
| `CURDATE()` | 取得現在的「日期」部分（yyyy-mm-dd） |
| `CURTIME()` | 取得現在的「時間」部分（hh:mm:ss） |

🔸 範例：

```sql
SELECT NOW();        -- 2025-04-28 14:35:22
SELECT CURDATE();    -- 2025-04-28
SELECT CURTIME();    -- 14:35:22
```

---

### 📅 2. 篩選今天、近7天、本月資料

#### 📌 今天的資料：

```sql
SELECT * FROM orders
WHERE DATE(order_time) = CURDATE();
```

#### 📌 過去 7 天內的資料：

```sql
SELECT * FROM orders
WHERE order_time >= CURDATE() - INTERVAL 7 DAY;
```

#### 📌 本月資料：

```sql
SELECT * FROM orders
WHERE MONTH(order_time) = MONTH(CURDATE())
  AND YEAR(order_time) = YEAR(CURDATE());
```

---

### 📅 3. 自訂時間格式輸出（DATE_FORMAT）

```sql
SELECT DATE_FORMAT(order_time, '%Y年%m月%d日 %H:%i') AS 訂單時間
FROM orders;
```

| 格式符號 | 說明 |
|----------|------|
| `%Y` | 西元年（4 位數） |
| `%m` | 月份（兩位數） |
| `%d` | 日期（兩位數） |
| `%H` | 小時（24 小時制） |
| `%i` | 分鐘 |
| `%s` | 秒數 |

---

### 📅 4. 計算日期間距（DATEDIFF）

計算兩個日期間的「天數差」：

```sql
SELECT DATEDIFF('2025-05-01', '2025-04-28') AS 相差天數;
-- 結果：3
```

📌 可搭配 `NOW()` / `CURDATE()` 做出「距今天幾天」的查詢！

---

### 📅 5. 加減時間（DATE_ADD / DATE_SUB）

#### ➕ 增加 3 天：

```sql
SELECT DATE_ADD(CURDATE(), INTERVAL 3 DAY);
```

#### ➖ 減去 1 週：

```sql
SELECT DATE_SUB(CURDATE(), INTERVAL 1 WEEK);
```

---

### 📌 小提醒

- `DATE()` 可從 `DATETIME` 取出日期部分（若只比日期用這個）。
- `NOW()` 是精確到秒的時間戳，`CURDATE()` 是純日期。
- 注意使用 `BETWEEN` 時，需包含時間範圍完整：

```sql
SELECT * FROM orders
WHERE order_time BETWEEN '2025-04-01' AND '2025-04-30 23:59:59';
```

---

## 🏛️ 單元 13：查詢效能與索引（INDEX）

本單元介紹如何在 MySQL 中使用索引（INDEX）來：
- 加快查詢速度
- 提升 WHERE、JOIN、ORDER BY 的效率
- 避免全表掃描
- 建立、查看與刪除索引

---

### 🏛️ 1. 為什麼需要索引？

當資料量很大時，若沒有索引，MySQL 在執行查詢時會**逐筆掃描整張表（Full Table Scan）**，  
導致查詢效能大幅下降。

📌 索引就像是資料庫的目錄，可以幫助快速定位資料所在的位置。

---

### 🏛️ 2. 建立索引的語法

```sql
CREATE INDEX 索引名稱
ON 資料表名稱 (欄位名稱);
```

🔸 範例：

```sql
CREATE INDEX idx_name ON employees(name);
```

📌 建議欄位名稱加上 `idx_欄位名` 作為索引名稱，有助辨識。

---

### 🏛️ 3. 常見的索引類型

| 索引類型 | 說明 |
|----------|------|
| `PRIMARY KEY` | 主鍵，自動建立唯一索引 |
| `UNIQUE` | 唯一值索引，防止重複資料 |
| `INDEX` | 一般索引，加速查詢 |
| `FULLTEXT` | 全文索引，用於全文搜索 |
| `MULTI-COLUMN INDEX` | 複合索引，針對多欄位組合 |

---

### 🏛️ 4. 查看目前有哪些索引

```sql
SHOW INDEXES FROM 資料表名稱;
```

🔸 範例：

```sql
SHOW INDEXES FROM employees;
```

---

### 🏛️ 5. 刪除索引

```sql
DROP INDEX 索引名稱 ON 資料表名稱;
```

🔸 範例：

```sql
DROP INDEX idx_name ON employees;
```

---

### 🏛️ 6. 索引最佳實務建議

✅ **應該加索引的情況**：

- WHERE 條件中經常查詢的欄位
- JOIN 條件欄位（主鍵對外鍵）
- ORDER BY / GROUP BY 所用的欄位
- DISTINCT 或 COUNT 時常用欄位

🚫 **不建議加索引的情況**：

- 資料極少的表格（全表掃描更快）
- 常更新的欄位（會增加寫入成本）
- 大量重複值的欄位（如性別）

---

### 📈 7. 查詢效能分析工具（EXPLAIN）

```sql
EXPLAIN SELECT * FROM employees WHERE name = 'Kevin';
```

📌 可用來分析此查詢是否有用到索引，以及是否全表掃描！

---

### 📌 小提醒

- 索引會佔用儲存空間，不能亂加太多。
- 善用 `EXPLAIN` 工具觀察查詢計劃。
- 複合索引的順序非常重要（從前往後有效）。

---

## 🔥 綜合實戰練習題組：從建表到查詢分析一次搞懂！

本章節設計一組完整的練習任務，包含：

- 建立資料表與資料約束
- 插入樣本資料
- 多表 JOIN、條件查詢、分組統計
- 使用子查詢與 CASE WHEN 條件分類
- 索引與效能觀察

---

### 🔧 步驟 1：建立三張資料表

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    class_id INT,
    gender VARCHAR(10)
);

CREATE TABLE classes (
    id INT PRIMARY KEY,
    class_name VARCHAR(50),
    teacher_id INT
);

CREATE TABLE teachers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(50)
);
```

---

### 📥 步驟 2：插入範例資料

```sql
-- 教師資料
INSERT INTO teachers VALUES
(1, '張老師', '數學'),
(2, '李老師', '英文'),
(3, '王老師', '自然');

-- 班級資料
INSERT INTO classes VALUES
(101, '數學A班', 1),
(102, '英文B班', 2),
(103, '自然C班', 3);

-- 學生資料
INSERT INTO students VALUES
(NULL, '小明', 16, 101, '男'),
(NULL, '小美', 15, 102, '女'),
(NULL, '小華', 17, 101, '男'),
(NULL, '小綠', 16, 103, '女'),
(NULL, '小藍', 17, NULL, '男');
```

---

### 📊 步驟 3：實戰查詢任務

#### ✅ 任務 1：查詢每位學生的班級名稱與導師姓名

```sql
SELECT s.name AS 學生, c.class_name, t.name AS 導師
FROM students s
LEFT JOIN classes c ON s.class_id = c.id
LEFT JOIN teachers t ON c.teacher_id = t.id;
```

---

#### ✅ 任務 2：列出沒有班級的學生

```sql
SELECT name FROM students
WHERE class_id IS NULL;
```

---

#### ✅ 任務 3：統計每位導師底下的學生人數

```sql
SELECT t.name AS 導師, COUNT(s.id) AS 學生人數
FROM teachers t
LEFT JOIN classes c ON t.id = c.teacher_id
LEFT JOIN students s ON c.id = s.class_id
GROUP BY t.name;
```

---

#### ✅ 任務 4：找出比全體平均年齡高的學生

```sql
SELECT name, age
FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);
```

---

#### ✅ 任務 5：依年齡分類學生（CASE WHEN）

```sql
SELECT name, age,
    CASE
        WHEN age < 16 THEN '低年級'
        WHEN age BETWEEN 16 AND 17 THEN '中年級'
        ELSE '高年級'
    END AS 年級分類
FROM students;
```

---

#### ✅ 任務 6：建立索引觀察效能

```sql
CREATE INDEX idx_age ON students(age);

-- 再執行以下 EXPLAIN 查看是否有用到索引
EXPLAIN SELECT * FROM students WHERE age = 17;
```
