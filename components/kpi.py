from dash import html 

import dash_bootstrap_components as dbc

class KPI:
    def __init__(self,kpi,label):
        self.kpi = kpi
        self.label = label

    def display(self):
        layout = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(self.label, className="card-title"),
                html.P(self.kpi, className="card-text"),
            ]
        ),
    ],
    className="align-items-center",
    style={"width": "18rem"},
)
        return layout