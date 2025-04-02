-- SELECT *
-- FROM customers
-- ORDER BY first_name DESC
-- ORDER BY state DESC, first_name DESC

-- SELECT first_name, last_name, 10 AS points
-- FROM customers
-- ORDER BY first_name, points
-- ORDER BY 1, 2 -- 1 means first_name, 2 means last_name

-- Exercise
SELECT *, quantity * unit_price AS total_price
FROM order_items
WHERE order_id = 2
ORDER BY quantity * unit_price DESC