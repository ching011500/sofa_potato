-- SELECT * 
-- FROM Customers
-- WHERE points >= 1000 AND points <= 3000 == WHERE points BETWEEN 1000 AND 3000
-- WHERE points BETWEEN 1000 AND 3000

-- Exercise
-- return customers born between 1/1/1990 - 1/1/2000

SELECT * 
FROM Customers
WHERE birth_date BETWEEN '1990/1/1' AND '2000/1/1'