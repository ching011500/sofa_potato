-- SELECT * 
-- FROM Customers
-- WHERE last_name LIKE '%field%' == WHERE last_name REGEXP 'field'
-- WHERE last_name REGEXP 'field'
-- WHERE last_name REGEXP 'field|mac|rose'
-- WHERE last_name REGEXP '^field|mac|rose'
-- WHERE last_name REGEXP 'field$|mac|rose'

-- WHERE last_name REGEXP '[gim]e' -- ge/ie/me
-- WHERE last_name REGEXP '[a-h]e' -- ae/.../he

-- ^ beginning
-- $ end 
-- | logical OR
-- [abcd]
-- [a-f]

-- GEt the customers whose
	-- first names are ELKA or AMBUR
    -- last names end with EY or ON
    -- last names start with MY or contains SE
    -- last names contain B followed by R or U
    
SELECT * 
FROM Customers
-- WHERE first_name REGEXP 'ELKA|AMBUR'
-- WHERE last_name REGEXP 'EY$|ON$'
-- WHERE last_name REGEXP '^MY|SE'
WHERE last_name REGEXP 'b[ru]'
