import webbrowser

class Movie():

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,imdb):
        """Generating a website with some of my favorite movies and a brief summary. Click on movie to watch trailer."""
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.imdb_url=imdb

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
