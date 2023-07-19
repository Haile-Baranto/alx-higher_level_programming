-- Script: List Shows with Linked Genres
-- Description: This script lists all the shows contained in the hbtn_0d_tvshows
-- database that have at least one genre linked.

SELECT show.`title`, genere.`genre_id`
  FROM `tv_shows` AS show
        INNER JOIN `tv_show_genres` AS genere
	ON show.`id` = genere.`show_id`
 ORDER BY show.`title`, genere.`genere_id`;
