import urllib2
import json

API_END_POINT = 'https://api.themoviedb.org/3/'
API_KEY = 'api_key=b95cded270ad96040389d19edba9f132'
POSTER_URL = 'https://image.tmdb.org/t/p/w500'
YOUTUBE_URL = 'https://youtu.be/'

def get_data(url):
    RESPONSE = urllib2.urlopen(url).read()
    JSON_RESPONSE = json.loads(RESPONSE)
    return JSON_RESPONSE['results']

def get_top_rated(limit = False):
    URL = API_END_POINT + 'movie/top_rated?' + API_KEY
    FULL_LIST = get_data(URL)
    
    # Get only limit number videos from the response list
    if (limit):
        FULL_LIST = FULL_LIST[0:limit]
        
    print('Got the top rated list: ' + str(len(FULL_LIST)))
    for movie in FULL_LIST:
        print('Getting Data: ' + movie['title'])
        movie['video'] = get_movie_videos(movie['id'])
        movie['poster_url'] = POSTER_URL + movie['poster_path']
    return FULL_LIST

def get_movie_videos(movie_id):
    URL = API_END_POINT + 'movie/' + str(movie_id) + '/videos?' + API_KEY
    MOVIE_VIDEOS = get_data(URL)
    FIRST_VIDEO_URL = MOVIE_VIDEOS[0]['key']
    return YOUTUBE_URL + FIRST_VIDEO_URL