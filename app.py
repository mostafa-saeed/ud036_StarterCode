import media
from fresh_tomatoes import open_movies_page
from themoviedb import get_top_rated

top_rated_movies = get_top_rated(20)
movies = []
for top_rated_movie in top_rated_movies:
    movie = media.Movie(
        top_rated_movie['title'],
        top_rated_movie['poster_url'],
        top_rated_movie['video'],
        top_rated_movie['overview']
    )
    movies.append(movie)

open_movies_page(movies)
