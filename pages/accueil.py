import dash
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__, path="/", name="Accueil")

layout = dmc.Container([
    dmc.Title("Bienvenue sur l'Accueil", order=1, mb="lg"),
    dmc.Text("Ceci est la page d'accueil de votre application.", size="lg"),
    dmc.Space(h=20),
    dmc.Card([
        dmc.CardSection(
            dmc.Text("Informations", fw=500, size="lg"),
            withBorder=True,
            p="md"
        ),
        dmc.Text("Contenu de votre dashboard ici", p="md")
    ], withBorder=True, shadow="sm", radius="md")
], size="xl", pt="xl")
