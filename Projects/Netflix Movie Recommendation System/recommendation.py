import pandas as pd 

ratings = pd.read_csv("ml-100k/u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])

movies = pd.read_csv("ml-100k/u.item", sep="|", encoding="latin-1", usecols=[0, 1], names=["movie_id", "title"])


movie_ratings = pd.merge(ratings, movies, on="movie_id")

movie_ratings.drop(columns=["timestamp"], inplace=True)

print("Missing Values:\n", movie_ratings.isnull().sum())

print(movie_ratings.head())
