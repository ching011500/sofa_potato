-- SELECT *
-- FROM order_items oi
-- JOIN sql_inventory.products p
	-- ON oi.product_id = p.product_id
    
-- USE sql_inventory
SELECT *
FROM products p
JOIN sql_store.order_items oi
	ON p.product_id = oi.product_id