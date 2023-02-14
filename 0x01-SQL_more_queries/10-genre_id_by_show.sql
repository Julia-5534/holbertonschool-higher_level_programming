-- LISTS ALL SHOWS IN hbtn_0d_tvshows & HAVE AT LEAST ONE GENRE LINKED
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
    JOIN tv_show_genres 
      ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres 
      ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
