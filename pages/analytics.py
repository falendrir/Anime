import dash
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__, name="Analytics")

layout = dmc.Container([
    dmc.Title("Analytics", order=1, mb="lg"),
    dmc.SimpleGrid([
        dmc.Card([
            dmc.Text("Métrique 1", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title("1,234", order=3, ta='center')
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Métrique 2", fw=500, c="dimmed", size="sm"),
            dmc.Title("5,678", order=2)
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Métrique 3", fw=500, c="dimmed", size="sm"),
            dmc.Title("9,012", order=1)
        ], withBorder=True, p="md"),
    ], cols={"base": 1, "sm": 3}, spacing="lg")
], size="xl", pt="xl")
