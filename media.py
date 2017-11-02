import re


class Movie():
    """ Movies Class """
    def __init__(self, title, poster_image_url, trailer_youtube_url, story):
        '''
        Movies class INIT function

        Args:
            title (str): The movie name
            poster_image_url (str): The url of the poster image for the movie
            trailer_youtube_url (str): The url of the trailer on YouTube
            story (str): The movie overview
        Returns
            (str): The new created object
        '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.story = story
        self.set_trailer_youtube_id(trailer_youtube_url)

    def set_trailer_youtube_id(self, url):
        '''
        Extracts the video id from the YouTube url

        Args:
            url (str): The url of the trailer on YouTube
        Returns:
            (str): The of the YouTube video
        '''
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
        youtube_id_match = (
            youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
        )
        self.trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None
        )
