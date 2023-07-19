-- Script: Shows and Linked Genres
-- Description: This script lists all shows and their linked genres from the hbtn_0d_tvshows database.
SELECT tv.`title`, genere.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS show
       ON tv.`id` = show.`show_id`

       LEFT JOIN `tv_genres` AS genere
       ON show.`genre_id` = genere.`id`
 ORDER BY tv.`title`, genere.`name`;
