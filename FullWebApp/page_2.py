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
                html.Div(
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "background-color" : "blue"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}
            
        ),

        dbc.Col(
                html.Div(
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "background-color" : "red"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}

        ),
        
        ],
        className="border border-primary",
        style={"padding" : "0px", "height" : "50%", "margin-left" : "auto", "margin-right" : "auto"}
    ),

    dbc.Row(
        [dbc.Col(
                html.Div(
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "background-color" : "red"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}
            
        ),

        dbc.Col(
                html.Div(
                style={"padding" : "0px", "height" : "100%", "width" : "100%", "background-color" : "blue"}
                ),
                style={"padding" : "0px", "height" : "100%", "width" : "100%"}

        ),
        
        ],
        className="border border-primary",
        style={"padding" : "0px", "height" : "50%", "margin-left" : "auto", "margin-right" : "auto"}
    )
    
    
], 
fluid=True,
style={"padding" : "0 0 0 0", "height" : "100%", "width" : "100%"}
)

class page2:

        def render(self):

                return html.Div(page1, style={"padding" : "0 0 0 0", "height" : "100%", "width" : "100%"})


                
