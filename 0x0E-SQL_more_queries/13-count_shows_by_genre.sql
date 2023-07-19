-- Script: Count Shows by Genre
-- Description: This script lists genres in hbtn_0d_tvshows and
-- the number of shows linked to each genre.

SELECT genere.`name`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS genere
       INNER JOIN `tv_show_genres` AS tv
       ON genere.`id` = tv.`genre_id`
 GROUP BY genere.`name`
 ORDER BY `number_of_shows` DESC;
