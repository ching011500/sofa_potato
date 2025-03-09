-- USE sql_store;

-- SELECT *
-- FROM customers
-- WHERE customers_id = 1
-- ORDER BY first_name

-- SELECT last_name, first_name, points, (points + 10) * 100 AS 'discount factor'
-- FROM customers

-- SELECT state
-- FROM customers

-- Exercise
-- Return name, unit price, new price (unit price * 1.1)
-- From products

SELECT name, unit_price, unit_price * 1.1  AS 'new price'
FROM products