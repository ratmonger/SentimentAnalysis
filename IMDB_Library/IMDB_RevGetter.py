from imdb import IMDb
import pandas as pd

# BEFORE YOU RUN THIS CODE
# install the required library by running command in terminal
# pip install git+https://github.com/cinemagoer/cinemagoer

# For other documentation use link below:
# https://cinemagoer.readthedocs.io/en/latest/index.html


# Create an instance of the IMDb class
ia = IMDb()

# Search for a movie by title
movie_title = "The Shawshank Redemption"  # Replace with the actual title
movies = ia.search_movie(movie_title)

imdb_id = 0

# Get the IMDb ID of the first result
if movies:
    imdb_id = movies[0].getID()
    print(f"IMDb ID for '{movie_title}': {imdb_id}")
else:
    print(f"No results found for '{movie_title}'")

movie = ia.get_movie(imdb_id)

# Display the keys in the data dictionary
print(movie.data.keys())

# Check if 'reviews' is present in the data dictionary
if 'reviews' in movie.data:
    reviews = movie.data['reviews']
    df = pd.DataFrame(reviews)
    print(df)
else:
    print(f"No reviews found for '{movie_title}'")

# Get synopsis for the movie
sys = movie.data['synopsis']

# Convert reviews to a DataFrame
df = pd.DataFrame(sys)

# Display the DataFrame
# print(df.to_string())
