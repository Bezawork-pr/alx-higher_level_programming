-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings on tv_show_ratings.show_id = tv_shows.id
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC
