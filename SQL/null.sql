-- SELECT * 
-- FROM Customers
-- WHERE phone is NULL 
-- WHERE phone is NOT NULL 

-- Exercise
-- Get the orders that are not shipped

SELECT * 
FROM orders
WHERE shipped_date is NULL
