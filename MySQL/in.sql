-- USE sql_store;

-- SELECT * 
-- FROM Customers
-- WHERE state = 'VA' OR state = 'GA' OR state = 'FL' == WHERE state IN ('VA', 'GA', 'FL')
-- WHERE state NOT IN ('VA', 'GA', 'FL')

-- Exercise
-- Return the products with uantity_in_stock equal to 49, 38, 72

SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72)