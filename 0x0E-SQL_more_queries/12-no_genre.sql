-- Script: List Shows Without Genre
-- Description: This script lists shows in hbtn_0d_tvshows without a genre linked.
SELECT show.`title`, genere.`genre_id`
  FROM `tv_shows` AS show
       LEFT JOIN `tv_show_genres` AS genere
       ON show.`id` = genere.`show_id`
       WHERE genere.`genre_id` IS NULL
 ORDER BY show.`title`, genere.`genre_id`;
