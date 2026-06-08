-- Write your query below
SELECT customer_id, customer_name
FROM customers
WHERE customer_id = ANY (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'A'
) AND customer_id = ANY (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'B'
) AND NOT customer_id = ANY (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'C'
)
ORDER BY customer_name;