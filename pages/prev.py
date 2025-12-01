# import packages
import dash
from dash import callback, Output, Input, State
import dash_mantine_components as dmc

# Import data
from .previsions import lin_reg_scaled, scaler

dash.register_page(__name__, name="Previsions", path="/prev")

layout = dmc.Container([
    dmc.Title("Prevision", order=1, mb="lg"),
    dmc.SimpleGrid([
        dmc.TextInput(
            # props as configured above:
            id='episodes',
            placeholder="Number of episodes",
            label="Episodes",
            description="Enter number of episodes",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.TextInput(
            # props as configured above:
            id='scored',
            placeholder="Number",
            label="Scored by",
            description="Number of people who will be rating",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.TextInput(
            # props as configured above:
            id='members',
            placeholder="Members",
            label="Members",
            description="Number of people",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.TextInput(
            # props as configured above:
            id='favoris',
            placeholder="Favorited",
            label="Favorited",
            description="Number of people who will add it to their favorites",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.TextInput(
            # props as configured above:
            id='popularity',
            placeholder="Popularity",
            label="Popularity",
            description="Estimated anime popularity",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.TextInput(
            # props as configured above:
            id='ranked',
            placeholder="Ranked",
            label="Ranked",
            description="Estimated anime ranked",
            size="sm",
            radius="sm",
            variant="default",
            required=True,
            debounce=True,
        ),
        dmc.Button("Prédire", id="btn-predict", mt="lg"),
        dmc.Card([
            dmc.Text("Prev", fw=500, c="dimmed", size="sm", ta='center'),
            dmc.Title(id="output-resultat", order=2, ta='center')
        ], withBorder=True, p="md"),
    ], cols={"base": 1, "sm": 3}, spacing="lg"),
], size="xl", pt="xl")

@callback(
    Output("output-resultat", "children"),
    Input("btn-predict", "n_clicks"),
    State("episodes", "value"),
    State("scored", "value"),
    State("members", "value"),
    State("favoris", "value"),
    State("popularity", "value"),
    State("ranked", "value"),
    prevent_initial_call=True
)
def traiter_inputs(n_clicks, episodes, scored, members, favoris, popularity, ranked):
    new = [[int(episodes), int(scored), int(members), int(favoris), int(popularity), int(ranked)]]
    new_scaled = scaler.transform(new)
    predict = lin_reg_scaled.predict(new_scaled)
    return predict
