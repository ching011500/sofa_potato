-- SELECT 
-- 	c.customer_id,
--     c.first_name,
--     o.order_id
-- FROM customers c 
-- JOIN orders o
-- 	ON o.customer_id = c.customer_id
-- ORDER BY c.customer_id

-- SELECT 
-- 	c.customer_id,
--     c.first_name,
--     o.order_id
-- FROM customers c 
-- LEFT JOIN orders o
-- 	ON o.customer_id = c.customer_id
-- ORDER BY c.customer_id

-- SELECT 
-- 	c.customer_id,
--     c.first_name,
--     o.order_id
-- FROM customers c 
-- RIGHT JOIN orders o
-- 	ON o.customer_id = c.customer_id
-- ORDER BY c.customer_id

-- Exercise
SELECT 
	p.product_id,
    p.name,
    oi.quantity
FROM products p
JOIN order_items oi
	ON p.product_id = oi.product_id

