import codecademylib
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns={
  'id': 'id',
  'name': 'movie_title',
  'genre': 'genre',
  'year': 'year',
  'imdb_rating': 'imdb_rating'},
  inplace=True)


print(df)