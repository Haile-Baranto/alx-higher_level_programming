-- Script: Genres Not Linked to Dexter
-- Description: This script lists all genres not linked to the show
-- Dexter in the hbtn_0d_tvshows database.
SELECT DISTINCT `name`
  FROM `tv_genres` AS genere
       INNER JOIN `tv_show_genres` AS show
       ON genere.`id` = show.`genre_id`

       INNER JOIN `tv_shows` AS tv
       ON show.`show_id` = tv.`id`
       WHERE genere.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS genere
	             INNER JOIN `tv_show_genres` AS show
		     ON genere.`id` = show.`genre_id`

		     INNER JOIN `tv_shows` AS tv
		     ON show.`show_id` = tv.`id`
		     WHERE tv.`title` = "Dexter")
 ORDER BY genere.`name`;
