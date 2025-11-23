# import packages
import dash
from dash import html
import dash_mantine_components as dmc

# Import data
from data_loader import metric

dash.register_page(__name__, name="Anime Trends by Genre", path="/trend_genre")

layout = dmc.Container([
    dmc.Title("Analytics", order=1, mb="lg"),
    dmc.SimpleGrid([
        dmc.Card([
            dmc.Text("Comedy", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(metric['Comedy'], order=2, ta='center')
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Action", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(metric['Action'], order=2, ta='center')
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Music", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(metric['Music'], order=2, ta='center')
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Adventure", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(metric['Adventure'], order=2, ta='center')
        ], withBorder=True, p="md"),
        dmc.Card([
            dmc.Text("Kids", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(metric['Kids'], order=2, ta='center')
        ], withBorder=True, p="md"),
    ], cols={"base": 1, "sm": 5}, spacing="md"),
    dmc.Stack(
        children=[
            dmc.Divider(size="lg", mt='lg')
        ],)

], size="xl", pt="xl")
