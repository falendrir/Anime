# import packages
import dash
from dash import html
import dash_mantine_components as dmc
import dash_ag_grid as dag
from dash_iconify import DashIconify

# Import data
from data_loader import df_anime, df_airing, df_anilist, df_jikan, anime_value, airing_value, jikan_value, anilist_value

dash.register_page(__name__, name="Anime Trends by Genre", path="/sources")

layout = dmc.Container([
    dmc.Title("Sources", order=1, mb="lg"),
    dmc.Anchor(
        "Voir la source",
        href="https://github.com/LeoRigasaki/Anime-dataset/tree/main/data/raw",
        target="_blank",
        size="md",
        c="blue"
    ),

    dmc.Space(h="lg"),

    # Anime
    dmc.Badge(
            "Anime_seasonal",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
    ),
    dmc.Grid(
        [
            dmc.GridCol(
                dag.AgGrid(
                    rowData=df_anime.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_anime.columns],
                ), span = 9
            ),
            dmc.GridCol(
                dag.AgGrid(
                    rowData=anime_value.to_dict("records"),
                    columnDefs=[{"field": i} for i in anime_value.columns],
                ), span = 3
            ),
        ],
    gutter="xs"
    ),
    dmc.Text(f"Nombre de lignes : {df_anime.shape[0]}", size="md"),

    dmc.Space(h="lg"),

    # Airing
    dmc.Badge(
        "Airing_anime",
        variant="gradient",
        gradient={"from": "indigo", "to": "cyan"},
    ),
    dmc.Grid(
        [
            dmc.GridCol(
                dag.AgGrid(
                    rowData=df_airing.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_airing.columns],
                ), span=9
            ),
            dmc.GridCol(
                dag.AgGrid(
                    rowData=airing_value.to_dict("records"),
                    columnDefs=[{"field": i} for i in airing_value.columns],
                ), span=3
            ),
        ],
        gutter="xs"
    ),
    dmc.Text(f"Nombre de lignes : {df_airing.shape[0]}", size="md"),

    dmc.Space(h="lg"),

    # Anilist
    dmc.Badge(
        "Anilist_seasonal",
        variant="gradient",
        gradient={"from": "indigo", "to": "cyan"},
    ),
    dmc.Grid(
        [
            dmc.GridCol(
                dag.AgGrid(
                    rowData=df_anilist.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_anilist.columns],
                ), span=9
            ),
            dmc.GridCol(
                dag.AgGrid(
                    rowData=anilist_value.to_dict("records"),
                    columnDefs=[{"field": i} for i in anilist_value.columns],
                ), span=3
            ),
        ],
        gutter="xs"
    ),
    dmc.Text(f"Nombre de lignes : {df_anilist.shape[0]}", size="md"),

    dmc.Space(h="lg"),

    # Jikan
    dmc.Badge(
        "Jikan_seasonal",
        variant="gradient",
        gradient={"from": "indigo", "to": "cyan"},
    ),
    dmc.Grid(
        [
            dmc.GridCol(
                dag.AgGrid(
                    rowData=df_jikan.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_jikan.columns],
                ), span=9
            ),
            dmc.GridCol(
                dag.AgGrid(
                    rowData=jikan_value.to_dict("records"),
                    columnDefs=[{"field": i} for i in jikan_value.columns],
                ), span=3
            ),
        ],
        gutter="xs"
    ),
    dmc.Text(f"Nombre de lignes : {df_jikan.shape[0]}", size="md"),


], size="xl", pt="xl")
