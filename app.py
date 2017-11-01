import media
from fresh_tomatoes import open_movies_page
from themoviedb import get_top_rated

TOP_RATED_MOVIES = get_top_rated(20)
movies = []
for top_rated_movie in TOP_RATED_MOVIES:
    movie = media.Movie(top_rated_movie['title'], top_rated_movie['poster_url'], top_rated_movie['video'])
    movies.append(movie)

open_movies_page(movies)