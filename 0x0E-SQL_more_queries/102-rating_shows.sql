-- Script: Shows by Rating Sum
-- Description: This script lists all shows from hbtn_0d_tvshows_rate by their rating sum.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_ratings` AS rate
       ON tv.`id` = rate.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
