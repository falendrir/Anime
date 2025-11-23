import pandas as pd

# Les données viennent de github : https://github.com/LeoRigasaki/Anime-dataset/tree/main

df_anime = pd.read_csv("data/anime_seasonal_20251122.csv")

df_genre = df_anime['genres'].str.split(';', expand=True)

for i in range(df_genre.shape[1]):
    df_genre.rename(columns={i:'genre_'+str(i)}, inplace = True)

df_anime = pd.concat([df_anime, df_genre], axis=1)

metric = df_anime['genre_0'].value_counts()

#print(metric)
