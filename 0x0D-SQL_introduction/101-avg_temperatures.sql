-- Description: This script displays the average temperature (Fahrenheit) by city,
-- ordered by temperature in descending order.

-- Compute the average temperature by city
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
