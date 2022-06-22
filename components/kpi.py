from dash import html 

import dash_bootstrap_components as dbc

class KPI:
    def __init__(self,kpi,label):
        self.kpi = kpi
        self.label = label

    def display(self):
        layout = dbc.Card([
            dbc.CardHeader(self.label, className="card-title m-0 p-2 w-100 text-center fs-2 fw-bold"),
            dbc.CardBody(self.kpi, className="card-text m-0 p-2 w-100 text-center fs-1 fw-bold"),
        ],
        className="align-items-center h-75 w-50"
        )
        return layout