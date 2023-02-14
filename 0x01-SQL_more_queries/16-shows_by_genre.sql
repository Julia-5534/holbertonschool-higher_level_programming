-- LISTS ALL SHOWS & ALL GENRES LINKED TO THAT SHOW FROM hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_genres.name AS name
  FROM tv_shows
  LEFT JOIN tv_show_genres
         ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres
         ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
