-- Script: List Cities of California (Without JOIN)
-- Description: This script lists all the cities of California without using the JOIN keyword.

SELECT city.`id`, city.`name`, state.`name`
  FROM `cities` AS city
       INNER JOIN `states` AS state
       ON city.`state_id` = state.`id`
 ORDER BY city.`id`;
