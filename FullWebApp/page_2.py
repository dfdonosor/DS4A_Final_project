import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import pickle
from styles import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

page1 = dbc.Container([

    dbc.Row(
        [dbc.Col(
                html.Div([

                        dbc.Row([
                                html.H4("Input data for regression or classification modeling")#style={"width": "100%", "display": "flex", "align-items":"center", "justify-content":"center"})
                        ],
                        style={"height":"15%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green", "margin-left" : "0px", "margin-right" : "0px"}
                        ),

                        dbc.Row([
                                dbc.Row([

                                        dbc.Col([
                                               html.H5("Public service indicator x1", className='text-center align-middle', style={"height":"100%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"})  
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid black", "margin-left" : "0px", "margin-right" : "0px", "vertical-align" : "middle"},
                                        ),

                                        dbc.Col([
                                                html.Div([
                                                        html.P("Indicator"),
                                                        dcc.RangeSlider(min = 0, max = 20, value=[5, 15], id='my-range-slider', tooltip={"placement": "bottom", "always_visible": True}),
                                                        html.Div(id='output-container-range-slider'), 
                                                        ], 
                                                        className='align-middle',
                                                        style={"height":"100%", "width":"100%", "padding" : "0px", "box-shadow" : "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px"}
                                                )
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid gray", "margin-left" : "0px", "margin-right" : "0px"}
                                        ),
                                
                                        ],
                                style={"height":"33%", "width":"100%", "padding" : "0px", "border" : "1px solid green", "margin-left" : "0px", "margin-right" : "0px"},      
                                ),
                        
                                dbc.Row([
                                        dbc.Col([
                                               html.H5("Public service indicator x2", className='text-center align-middle', style={"height":"100%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"})  
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid black", "margin-left" : "0px", "margin-right" : "0px", "vertical-align" : "middle"},
                                        ),

                                        dbc.Col([
                                                html.Div([
                                                        html.P("Indicator"),
                                                        dcc.RangeSlider(min = 0, max = 20, value=[5, 15], id='my-range-slider', tooltip={"placement": "bottom", "always_visible": True}),
                                                        html.Div(id='output-container-range-slider'), 
                                                        ], 
                                                        className='align-middle',
                                                        style={"height":"100%", "width":"100%", "padding" : "0px", "box-shadow" : "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px"}
                                                )
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid gray", "margin-left" : "0px", "margin-right" : "0px"}
                                        ),
                                
                                        ],
                                style={"height":"33%", "width":"100%", "padding" : "0px", "border" : "1px solid red", "margin-left" : "0px", "margin-right" : "0px"}        
                                ),
                        
                                dbc.Row([
                                        dbc.Col([
                                               html.H5("Other important indicator", className='text-center align-middle', style={"height":"100%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"})  
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid black", "margin-left" : "0px", "margin-right" : "0px", "vertical-align" : "middle"},
                                        ),

                                        dbc.Col([
                                                html.Div([
                                                        html.P("Indicator"),
                                                        dcc.RangeSlider(min = 0, max = 20, value=[5, 15], id='my-range-slider', tooltip={"placement": "bottom", "always_visible": True}),
                                                        html.Div(id='output-container-range-slider'), 
                                                        ], 
                                                        className='align-middle',
                                                        style={"height":"100%", "width":"100%", "padding" : "0px", "box-shadow" : "rgba(99, 99, 99, 0.2) 0px 2px 8px 0px"}
                                                )
                                        ],
                                        style={"height":"100%", "width":"50%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid gray", "margin-left" : "0px", "margin-right" : "0px"}
                                        ),
                                
                                        ],
                                style={"height":"33%", "width":"100%", "padding" : "0px", "border" : "1px solid blue", "margin-left" : "0px", "margin-right" : "0px"}        
                                ),

                                
                        ]
                        ,
                        style={"height":"85%", "width":"100%", "padding" : "0px", "margin-left" : "0px", "margin-right" : "0px"}
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
                        style={"height":"15%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green", "margin-left" : "0px", "margin-right" : "0px"}
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        style={"height":"85%", "width":"100%", "padding" : "0px", "margin-left" : "0px", "margin-right" : "0px"}
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
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green", "margin-left" : "auto", "margin-right" : "auto"}
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
                        style={"height":"10%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem", "border" : "1px solid green", "margin-left" : "auto", "margin-right" : "auto"}
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

@app.callback(
        Output('output-container-range-slider', 'children'),
        [Input('my-range-slider', 'value')])
def update_output(value):
        return 'You have selected "{}"'.format(value)

class page2:

        def render(self):

                return html.Div(page1, style={"padding" : "0 0 0 0", "height" : "100%", "width" : "100%"})
        


                
