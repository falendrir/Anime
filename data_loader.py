import pandas as pd

# Les données viennent de github : https://github.com/LeoRigasaki/Anime-dataset/tree/main

df_anime = pd.read_csv("data/anime_seasonal_20251122.csv")
df_airing = pd.read_csv('data/airing_anime.csv')
df_anilist = pd.read_csv('data/anilist_seasonal_20251122.csv')
df_jikan = pd.read_csv('data/jikan_seasonal_20251122.csv' )
df_anime_entries = pd.read_csv('data/anime_entries.csv', dtype={'german_name': str, 'french_name': str, 'spanish_name': str})
df_manga_entries = pd.read_csv( 'data/manga_entries.csv', dtype={'german_name': str, 'french_name': str, 'spanish_name': str})
df_characters = pd.read_csv("data/anime_characters.csv")

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

anime_entries_value = pd.DataFrame([df_anime_entries['item_type'].value_counts()])
anime_entries_value = anime_entries_value.melt(var_name="Type", value_name="Count")

manga_entries_value = pd.DataFrame([df_manga_entries['item_type'].value_counts()])
manga_entries_value = manga_entries_value.melt(var_name="Type", value_name="Count")

#print(df_anime_entries['demographic'].value_counts())

print(df_characters[df_characters['name']=='Miyamoto Musashi'])