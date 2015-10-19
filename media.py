import webbrowser

class Movie():
    """This class provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_storyline,
                    poster_image, trailer_youtube, 
                    movie_imdb, movie_release_date, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb = movie_imdb
        self.release_date = movie_release_date
        self.rating = movie_rating
        
        
    #This method will automatically play a movie's trailer 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
