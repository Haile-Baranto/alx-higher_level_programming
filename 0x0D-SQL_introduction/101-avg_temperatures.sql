-- Description: This script displays the average temperature (Fahrenheit) by city,
-- ordered by temperature in descending order.

-- Compute the average temperature by city
SELECT city, AVG(temperature) AS avg_temp
FROM weather_data
GROUP BY city
ORDER BY avg_temp DESC;
