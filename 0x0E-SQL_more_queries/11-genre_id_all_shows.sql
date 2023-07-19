-- Script: List Shows with Linked Genres
-- Description: This script lists all the shows contained in the hbtn_0d_tvshows
-- database that have at least one genre linked.

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List shows with linked genres
SELECT tv_shows.'title', tv_show_genres.'genre_id'
FROM 'tv_shows'
INNER JOIN tv_show_genres ON 'tv_shows.id' = tv_show_genres.'tv_show_id'
ORDER BY tv_shows.'title' ASC, tv_show_genres.'genre_id' ASC;

