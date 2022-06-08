import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import pickle
from styles import *

page1 = dbc.Container([

    dbc.Row(
        [dbc.Col(
                html.Div([

                        dbc.Row([
                                html.H4("Input data for regression or classification modeling")
                        ],
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green"}
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        style={"height":"90%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"}
                        ),
                ],
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "border" : "1px solid blue"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}
            
        ),

        dbc.Col(
                html.Div([

                        dbc.Row([
                                html.H4("Estimated score result after modeling")
                        ],
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green"}
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        style={"height":"90%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"}
                        ),
                ],
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}

        ),
        
        ],
        className="border border-primary",
        style={"padding" : "0px", "height" : "45%", "margin-left" : "auto", "margin-right" : "auto"}
    ),

    dbc.Row(
        [dbc.Col(
                html.Div([
                        dbc.Row([
                                html.H4("Relationships between public services and ICFES Score")
                        ],
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green"}
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        style={"height":"90%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"}
                        ),
                ],
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "border" : "1px solid red"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}
            
        ),

        dbc.Col(
                html.Div([
                        dbc.Row([
                                html.H4("Relationships between public services and ICFES Score")
                        ],
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green"}
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        style={"height":"90%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"}
                        ),
                ],
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "border" : "1px solid blue"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}

        ),
        
        ],
        className="border border-primary",
        style={"padding" : "0px", "height" : "55%", "margin-left" : "auto", "margin-right" : "auto"}
    )
    
    
], 
fluid=True,
style={"padding" : "0 0 0 0", "height" : "100%", "width" : "100%"}
)

class page2:

        def render(self):

                return html.Div(page1, style={"padding" : "0 0 0 0", "height" : "100%", "width" : "100%"})


                
