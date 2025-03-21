"""
1. NOT EXIST,EXIST
WITH RECURSIVE GEN AS (
SELECT
    ID,
    PARENT_ID,
    1 AS GEN
FROM
    ECOLI_DATA
WHERE
    PARENT_ID IS NULL
    
UNION ALL
    
SELECT
    E.ID,
    E.PARENT_ID,
    GEN + 1 AS GEN
FROM
    ECOLI_DATA E
INNER JOIN
    GEN G
    ON
    G.ID = E.PARENT_ID
)

SELECT
    COUNT(*) AS COUNT,
    GEN AS GENERATION
    
FROM
    GEN G
WHERE NOT EXISTS(
SELECT 1
FROM
    ECOLI_DATA E
WHERE
    E.PARENT_ID = G.ID
)
GROUP BY
    GEN
ORDER BY 
    GEN
"""
