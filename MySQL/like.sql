-- SELECT * 
-- FROM Customers
-- WHERE last_name LIKE 'b%'
-- WHERE last_name LIKE '%b%'
-- WHERE last_name LIKE '_____y'

-- % any number of characters
-- _ single characters

-- Exercise 
-- Get the customers whose addresses contain TRAIL or AVENUE
-- phone numbers end with 9

SELECT * 
FROM Customers
-- WHERE address LIKE '%trail%' OR address LIKE '%avenue%' 
WHERE phone LIKE '%9'


