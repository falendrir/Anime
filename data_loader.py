import pandas as pd

# Les données viennent de github : https://github.com/LeoRigasaki/Anime-dataset/tree/main

df_anime = pd.read_csv("data/anime_seasonal_20251122.csv")
df_airing = pd.read_csv('data/airing_anime.csv')
df_anilist = pd.read_csv('data/anilist_seasonal_20251122.csv')
df_jikan = pd.read_csv('data/jikan_seasonal_20251122.csv' )

df_genre = df_anime['genres'].str.split(';', expand=True)

for i in range(df_genre.shape[1]):
    df_genre.rename(columns={i:'genre_'+str(i)}, inplace = True)

df_anime = pd.concat([df_anime, df_genre], axis=1)

metric = df_anime['genre_0'].value_counts()

anime_value = pd.DataFrame([df_anime['type'].value_counts()])
anime_value = anime_value.melt(var_name="Type", value_name="Count")

airing_value = pd.DataFrame([df_airing['type'].value_counts()])
airing_value = airing_value.melt(var_name="Type", value_name="Count")

anilist_value = pd.DataFrame([df_anilist['type'].value_counts()])
anilist_value = anilist_value.melt(var_name="Type", value_name="Count")

jikan_value = pd.DataFrame([df_jikan['type'].value_counts()])
jikan_value = jikan_value.melt(var_name="Type", value_name="Count")
