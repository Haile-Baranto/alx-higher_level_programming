-- Script: List Cities of California (Without JOIN)
-- Description: This script lists all the cities of California without using the JOIN keyword.

SELECT `id`, `name` 
	FROM `cities`
	WHERE `state_id` IN
       (SELECT `id`
		FROM `states`
	 	WHERE `name` = "California")
 ORDER BY `id`;
