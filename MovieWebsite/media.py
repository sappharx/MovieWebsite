"""
This module defines the movie class
"""

import webbrowser

class Movie():
    """Represents a movie"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Initializes an instance of Movie with the input parameters:
            movie title
            movie storyline
            poster image url
            youtube trailer url
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens and plays the movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
