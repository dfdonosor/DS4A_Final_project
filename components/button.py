from dash import html
import dash_bootstrap_components as dbc

class Button:
    def __init__(self, text : str, id_button : str):
        self.text = text
        self.id_button = id_button

    def display(self):

        layout =  html.Div(
            [
                dbc.Button(
                    self.text, color="info", id=self.id_button, size="lg", className="mx-auto fs-3 text-white fw-bold", n_clicks=0, style={"background-color": "#2E487E"}
                )
            ],
            className="d-grid gap-2 col-6 mx-auto"
            )
        return layout