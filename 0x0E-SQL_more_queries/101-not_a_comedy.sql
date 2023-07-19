-- Script: Shows Without Comedy Genre
-- Description: This script lists all shows without the genre Comedy in the hbtn_0d_tvshows database.
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS show
       ON show.`show_id` = tv.`id`

       LEFT JOIN `tv_genres` AS genere
       ON genere.`id` = show.`genre_id`
       WHERE tv.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv
	             INNER JOIN `tv_show_genres` AS show
		     ON show.`show_id` = tv.`id`

		     INNER JOIN `tv_genres` AS genere
		     ON genere.`id` = show.`genre_id`
		     WHERE genere.`name` = "Comedy")
 ORDER BY `title`;
