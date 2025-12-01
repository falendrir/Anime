import dash
from dash import Dash, html, Input, Output, State, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)


def create_nav_link(icon, label, href):
    return dmc.NavLink(
        label=label,
        href=href,
        leftSection=DashIconify(icon=icon, width=20),
        active="exact",
        variant="subtle",
        style={"marginBottom": "5px"}
    )


app.layout = dmc.MantineProvider(
    children=[
        html.Div([
            dmc.AppShell(
                [
                    dmc.AppShellHeader(
                        dmc.Group([
                            dmc.ActionIcon(
                                DashIconify(icon="tabler:menu-2", width=20),
                                id="burger-button",
                                variant="subtle",
                                size="lg",
                            ),
                            dmc.Text("Mon Application", size="xl", fw=700),
                        ], px="md", py="sm")
                    ),
                    dmc.AppShellNavbar(
                        [
                            dmc.Stack([
                                dmc.Text(
                                    "Navigation",
                                    fw=500,
                                    size="sm",
                                    c="dimmed",
                                    id="nav-title"
                                ),
                                create_nav_link("tabler:home", "Accueil", "/"),
                                #create_nav_link("tabler:chart-line", "Analytics", "/analytics"),
                                #create_nav_link("tabler:settings", "Paramètres", "/parametres"),
                                create_nav_link("mdi:animation", "Anime Trends by Genre", "/trend_genre"),
                                create_nav_link("mdi:animation", "Prevision", "/prev"),
                                create_nav_link("grommet-icons:resources", "Sources", "/sources"),
                            ], p="md", gap="xs")
                        ],
                        id="navbar"
                    ),
                    dmc.AppShellMain(
                        dash.page_container,
                        id="main-content"
                    ),
                ],
                header={"height": 60},
                navbar={
                    "width": 250,
                    "breakpoint": "sm",
                    "collapsed": {"mobile": True, "desktop": False},
                },
                padding="xl",
                id="app-shell"
            ),
            dmc.Modal(
                id="navbar-state",
                opened=False,
                withCloseButton=False,
                styles={"modal": {"display": "none"}},
                children=html.Div(id="navbar-open", **{"data-open": "true"})
            )
        ])
    ]
)


@callback(
    Output("app-shell", "navbar"),
    Input("burger-button", "n_clicks"),
    State("navbar-open", "data-open"),
    prevent_initial_call=True
)
def toggle_navbar(n_clicks, is_open):
    is_currently_open = is_open == "true"
    new_width = 80 if is_currently_open else 250

    return {
        "width": new_width,
        "breakpoint": "sm",
        "collapsed": {"mobile": False, "desktop": False},
    }


@callback(
    Output("navbar-open", "data-open"),
    Input("burger-button", "n_clicks"),
    State("navbar-open", "data-open"),
    prevent_initial_call=True
)
def update_state(n_clicks, is_open):
    return "false" if is_open == "true" else "true"


@callback(
    Output("nav-title", "style"),
    Input("navbar-open", "data-open"),
)
def toggle_text(is_open):
    if is_open == "false":
        return {"display": "none"}
    return {"display": "block"}


if __name__ == "__main__":
    app.run(debug=True)
