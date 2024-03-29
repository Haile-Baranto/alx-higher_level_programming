-- This script displays the top 3 cities' temperatures during July and August,
-- ordered by temperature in descending order.

-- Compute the average temperature during July and August by city
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
