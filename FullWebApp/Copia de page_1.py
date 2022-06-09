import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import pickle
from styles import *

class page1:
        

        def render(self):
                return 
                
                        dbc.Row([
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Population", className="population"),
                                                                html.P("10")
                                                                    ])
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Number of Municipalities", className="municipalities"),
                                                                html.P("20")
                                                                    ])
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Global Average Score", className="global_score"),
                                                                html.P("10")
                                                                    ])
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Natural Science Average", className="ns_average"),
                                                                html.P("20")
                                                                    ])
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Math Average", className="math_average"),
                                                                html.P("10")
                                                                    ])
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("English Average", className="english_average"),
                                                                html.P("20")
                                                                    ])
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Critical Reading Average", className="cr_average"),
                                                                html.P("10")
                                                                    ])
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card(
                                                        dbc.CardBody([
                                                                html.H5("Social Citizenship Average", className="sc_average"),
                                                                html.P("20")
                                                                    ])
                                                        )
                                                )
                                        ])
                                ])
                


