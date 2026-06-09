-- Write your query below
SELECT seller_name
FROM seller
WHERE NOT EXISTS (
    SELECT 1
    FROM orders
    WHERE seller.seller_id = orders.seller_id AND
        sale_date >= '2020-01-01' AND sale_date <= '2020-12-31'
)
ORDER BY seller_name;