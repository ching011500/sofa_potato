-- SELECT *
-- FROM customers
-- LIMIT 3
-- LIMIT 3, 3
-- LIMIT 6, 3

-- page1 : 1-3
-- pagw2 : 4-6
-- page3 : 7-9

-- Exercise
-- Get the top three loyal customers

SELECT *
FROM customers
ORDER BY points DESC
LIMIT 3