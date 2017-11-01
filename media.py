import re

class Movie():
    """ Movies Class """
    def __init__(self, title, poster_image_url, trailer_youtube_url, story):
        self.title = title
        self.poster_image_url = poster_image_url
        self.story = story
        self.set_trailer_youtube_id(trailer_youtube_url)

    def set_trailer_youtube_id(self, url):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
        self.trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
