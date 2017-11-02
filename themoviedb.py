import urllib2
import json

API_END_POINT = 'https://api.themoviedb.org/3/'
API_KEY = 'api_key=b95cded270ad96040389d19edba9f132'
POSTER_URL = 'https://image.tmdb.org/t/p/w500'
YOUTUBE_URL = 'https://youtu.be/'


def get_data(url):
    response = urllib2.urlopen(url).read()
    json_response = json.loads(response)
    return json_response['results']


def get_top_rated(limit=False):
    url = API_END_POINT + 'movie/top_rated?' + API_KEY
    full_list = get_data(url)

    # Get only limit number videos from the response list
    if (limit):
        full_list = full_list[0:limit]

    # print('Got the top rated list: ' + str(len(full_list)))
    for movie in full_list:
        print('Getting Data: ' + movie['title'])
        movie['video'] = get_movie_videos(movie['id'])
        movie['poster_url'] = POSTER_URL + movie['poster_path']
    return full_list


def get_movie_videos(movie_id):
    url = API_END_POINT + 'movie/' + str(movie_id) + '/videos?' + API_KEY
    movie_videos = get_data(url)
    if (len(movie_videos) > 0):
        first_video_url = movie_videos[0]['key']
        return YOUTUBE_URL + first_video_url
    else:
        return ''
