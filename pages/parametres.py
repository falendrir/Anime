import dash
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__, name="Paramètres")

layout = dmc.Container([
    dmc.Title("Paramètres", order=1, mb="lg"),
    dmc.Stack([
        dmc.Switch(label="Activer les notifications", checked=True),
        dmc.Switch(label="Mode sombre", checked=False),
        dmc.Divider(),
        dmc.Button("Sauvegarder", color="blue")
    ], gap="md")
], size="xl", pt="xl")
