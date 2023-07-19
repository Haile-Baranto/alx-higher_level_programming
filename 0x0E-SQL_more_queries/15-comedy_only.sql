-- Script: Comedy Shows
-- Description: This script lists all Comedy shows from the hbtn_0d_tvshows database.
SELECT tv.`title`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_genres` AS show
       ON tv.`id` = show.`show_id`

       INNER JOIN `tv_genres` AS genere
       ON genere.`id` = show.`genre_id`
       WHERE genere.`name` = "Comedy"
 ORDER BY tv.`title`;
