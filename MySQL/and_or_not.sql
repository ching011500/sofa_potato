-- USE sql_store;

-- SELECT * 
-- FROM Customers
-- WHERE birth_date > '1990-01-01' AND points > 1000
-- WHERE birth_date > '1990-01-01' OR points > 1000
-- WHERE birth_date > '1990-01-01' OR (points > 1000 AND state = 'VA')
-- WHERE NOT (birth_date > '1990-01-01' OR points > 1000)
-- WHERE NOT (birth_date > '1990-01-01' AND points > 1000) equal to WHERE birth_date <= '1990-01-01' OR points <= 1000

-- Exercise
-- From the order_items table, get the items for order #6 
-- where the total price is greater than 30

SELECT * 
FROM order_items
WHERE order_id = 6 AND quantity * unit_price > 30
