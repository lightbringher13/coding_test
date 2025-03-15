"""
1. group by,in,distinct
SELECT
    CART_ID
FROM
    CART_PRODUCTS
WHERE
    NAME IN ("Milk","Yogurt")
GROUP BY
    CART_ID
HAVING
    COUNT(DISTINCT NAME) = 2
"""
