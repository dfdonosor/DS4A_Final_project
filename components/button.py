from dash import html
import dash_bootstrap_components as dbc

class Button:
    def __init__(self, text : str):
        self.text = text

    def display(self):

        layout =  html.Div(
    [
        dbc.Button(
            self.text, color="info", id="example-button", size="lg", className="me-2", n_clicks=0, style={"verticalAlign": "middle", "background-color": "#2E487E", "color" : "white"}
        ),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
    ]
)
        return layout