select * from productinsights;
SHOW COLUMNS FROM productinsights;
SELECT `Product sales` FROM productinsights;
SELECT Category, SUM(`Product sales`) AS Total_Sales
FROM productinsights
GROUP BY Category
ORDER BY Total_Sales DESC;
SELECT Category, `Product name`, `Product sales`
FROM (
    SELECT Category, `Product name`, `Product sales`,
           ROW_NUMBER() OVER (PARTITION BY Category ORDER BY `Product sales` DESC) AS ranks
    FROM productinsights
) AS ranked_products
WHERE ranks <= 3;

WITH TopCategories AS (
    SELECT Category, SUM(`Product sales`) AS Total_Sales
    FROM productinsights
    GROUP BY Category
    ORDER BY Total_Sales DESC
    LIMIT 5
)
SELECT tc.Category, pi.`Product name`, pi.`Product sales`
FROM TopCategories tc
JOIN productinsights pi ON tc.Category = pi.Category
WHERE (pi.`Product name`, pi.`Product sales`) IN (
    SELECT `Product name`, `Product sales`
    FROM (
        SELECT `Product name`, `Product sales`,
               ROW_NUMBER() OVER (PARTITION BY Category ORDER BY `Product sales` DESC) AS ranks
        FROM productinsights
        WHERE Category IN (SELECT Category FROM TopCategories)
    ) AS ranked_products
    WHERE ranks <= 3
)
ORDER BY tc.Total_Sales DESC, pi.`Product sales` DESC;




WITH TopCategories AS (
    SELECT Category, SUM(`Product sales`) AS Total_Sales
    FROM productinsights
    GROUP BY Category
    ORDER BY Total_Sales DESC
    LIMIT 3
)
SELECT tc.Category, pi.`Product name`, pi.`Product sales`
FROM TopCategories tc
JOIN productinsights pi ON tc.Category = pi.Category
WHERE (pi.`Product name`, pi.`Product sales`) IN (
    SELECT `Product name`, `Product sales`
    FROM (
        SELECT `Product name`, `Product sales`,
               ROW_NUMBER() OVER (PARTITION BY Category ORDER BY `Product sales` ASC) AS ranks
        FROM productinsights
        WHERE Category IN (SELECT Category FROM TopCategories)
    ) AS ranked_products
    WHERE ranks <= 3
)
ORDER BY tc.Total_Sales DESC, pi.`Product sales` ASC;

SELECT Category, `Product name`, `Product price`
FROM productinsights
WHERE `Product sales` = 0
ORDER BY `Product price` DESC
LIMIT 10;

SELECT Category, `Product name`, `Product price`
FROM productinsights
WHERE `Product sales` = 0
ORDER BY `Product price` ASC
LIMIT 50;


SELECT Category, `Product name`, `Product sales`,`Product price`
FROM productinsights
WHERE `Product sales` = 0
ORDER BY `Product price` ASC
LIMIT 50;


SELECT * FROM productinsights;

SELECT * FROM productinsights ORDER BY "Product price" DESC;































