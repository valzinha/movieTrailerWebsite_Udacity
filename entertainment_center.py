import media #the movie object
import fresh_tomatoes #this webpage that will display movie instances

"""File: entertainment_center.py 
   Defines Movie instances and displays them on a Movie Trailer Website
   Run this file to see Movie Trailer Website"""

#Toy Story Movie instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/2/259-pixar-movie-posters/toy-story-poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://www.imdb.com/title/tt0114709/", "22 November 1995 (USA)", "G")

#Princess Bride Movie instance
princessBride = media.Movie("Princess Bride",
                            "As you wish...A story of true love.",
                            "http://2.bp.blogspot.com/-xRGW5a7OnAM/UESufRN-ObI/AAAAAAAAM4Q/6fxTyiwJpHw/s1600/The+Princess+Bride+(1987)+3.jpg",
                            "https://www.youtube.com/watch?v=njZBYfNpWoE",
                            "http://www.imdb.com/title/tt0093779/", "9 October 1987 (USA)", "PG")

#Finding Nemo Movie instance
findingNemo = media.Movie("Finding Nemo", 
                            "A lost fish and the journey to find him.",
                            "http://www.redesignrevolution.com/wp-content/uploads/2012/09/Finding-Nemo-Alternative-Movie-Posters-7.jpg",
                            "https://www.youtube.com/watch?v=wZdpNglLbt8",
                            "http://www.imdb.com/title/tt0266543/",
                            "30 May 2003 (USA)",
                            "G")

#Hungar Games Movie instance
hungarGames = media.Movie("Hungar Games",
                            "Battle for life...and more",
                            "http://ricmeyers.com/wp-content/ric-meyers-uploads/2012/03/the-hunger-games-movie-poster-24.jpg",
                            "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                            "http://www.imdb.com/title/tt1392170/",
                            "23 March 2012 (USA)",
                            "PG-13")

#Harry Potter Movie instance
harryPotter = media.Movie("Harry Potter",
                            "Yur a wizard Harry!",
                            "http://1.bp.blogspot.com/_YdwA1wl6avk/TRhUuWZ_W4I/AAAAAAAACg4/PHdJvThCj48/s1600/harry_potter_and_the_deathly_hallows_part_i.jpg",
                            "https://www.youtube.com/watch?v=_EC2tmFVNNE",
                            "http://www.imdb.com/title/tt0926084/",
                            "19 November 2010 (USA)",
                            "PG-13")

#Define what movie instances to be displayed on the Movie Trailer Website
movies = [toy_story, princessBride, findingNemo, hungarGames, harryPotter]

#Display Movie Trailer Website
fresh_tomatoes.open_movies_page(movies)
