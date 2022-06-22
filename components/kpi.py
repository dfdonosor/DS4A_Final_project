from dash import html 

import dash_bootstrap_components as dbc

class KPI:
    def __init__(self, kpi : str, id_kpi : str,label : str):
        self.kpi = kpi
        self.id_kpi = id_kpi
        self.label = label

    def display(self):
        layout = dbc.Card([
            dbc.CardHeader(self.label, className="card-title m-0 p-2 w-100 text-center fs-3"),
            dbc.CardBody(children = self.kpi, id = self.id_kpi, className="card-text m-0 p-2 w-100 text-center fs-1 fw-bold"),
        ],
        className="align-items-center h-100 w-50"
        )
        return layout