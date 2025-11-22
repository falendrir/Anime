import pandas as pd
from PIL.ImageOps import expand

df_anime = pd.read_csv("data/anime_seasonal_20251122.csv")

df_genre = df_anime['genres'].str.split(';', expand=True)

for i in range(df_genre.shape[1]):
    df_genre.rename(columns={i:'genre_'+str(i)}, inplace = True)

df_anime = pd.concat([df_anime, df_genre], axis=1)