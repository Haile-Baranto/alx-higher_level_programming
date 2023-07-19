SELECT tv.`title`, genere.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS show
       ON tv.`id` = show.`show_id`

       LEFT JOIN `tv_genres` AS genere
       ON show.`genre_id` = genere.`id`
 ORDER BY tv.`title`, genere.`name`;
