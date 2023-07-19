-- Script: Genres by Rating Sum
-- Description: This script lists all genres in hbtn_0d_tvshows_rate by their rating sum.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS genere
       INNER JOIN `tv_show_genres` AS show
       ON show.`genre_id` = genere.`id`

       INNER JOIN `tv_show_ratings` AS rate
       ON rate.`show_id` = show.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
