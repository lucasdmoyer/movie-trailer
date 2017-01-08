import media
import fresh_tomatoes

# toy story movie
toy_story = media.Movie(
    "Toy Story", 
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio")

# avatar movie
avatar = media.Movie(
    "Avator",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# school of rock movie
school_of_rock = media.Movie(
    "School of Rock", 
    "Storyline", 
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # noqa
    "http://www.youtube.com/watch?v=3PsUJFEBC74")

# A list of all the movies
movies = [toy_story, avatar, school_of_rock]

# uses the fresh_tomatoes function open_movies_page on the list of movies
fresh_tomatoes.open_movies_page(movies)
