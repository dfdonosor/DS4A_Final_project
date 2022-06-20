import os
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from components.sub_title import SubTitle
from components.range_slider import RangerSlider
from components.description_element import DescriptionElement
from components.button import Button
from components.kpi import KPI

title_1 = SubTitle("Input data for regression or classification modeling")
title_2 = SubTitle("Estimated score result after modeling")
title_3 = SubTitle("Relationships between public services and ICFES Score")
title_4 = SubTitle("Relationships between public services and ICFES Score")

description_range_slider_1 = DescriptionElement("Public service indicator x1")
description_range_slider_2 = DescriptionElement("Public service indicator x2")
description_range_slider_3 = DescriptionElement("Other important indicator")

range_slider_1 = RangerSlider("Indicator", (0, 20))
range_slider_2 = RangerSlider("Indicator", (0, 20))
range_slider_3 = RangerSlider("Indicator", (0, 20))

description_button_result = DescriptionElement("Global ICFES score")
button_result = Button("Estimated result")

kpi_result = KPI(50, "Result")

page1 = dbc.Container([

    dbc.Row(
        [dbc.Col(
                html.Div([

                        dbc.Row(
                                title_1.display(),
                                className="m-0 p-0 border border-primary",
                                style={"height": "10%"}
                        ),

                        dbc.Row([
                                dbc.Row([
                                        dbc.Col([
                                                description_range_slider_1.display()
                                        ],
                                        width=6,
                                        ),
                                        dbc.Col([
                                                range_slider_1.display()
                                        ],
                                        width=6,
                                        ),
                        ], className='p-0 m-0'),

                                dbc.Row([
                                        dbc.Col([
                                                description_range_slider_2.display()
                                        ],
                                        width=6,
                                        ),
                                        dbc.Col([
                                                range_slider_2.display()
                                        ],
                                        width=6,
                                        ),
                        ], className='p-0 m-0'),

                                dbc.Row([
                                        dbc.Col([
                                                description_range_slider_3.display()
                                        ],
                                        width=6,
                                        ),
                                        dbc.Col([
                                                range_slider_3.display()
                                        ],
                                        width=6,
                                        ),
                        ], className='p-0 m-0'),
                                
                        ],
                        className="m-0 p-0 border border-success",
                        style={"height": "90%"}
                        ),
                ]
                ),
                className="m-0 p-0"      
        ),

        dbc.Col(
                html.Div([

                        dbc.Row(
                                title_2.display(),
                                className="m-0 p-0 align-items-center",
                                style={"height": "10%"}
                        ),

                        dbc.Row([
                                dbc.Col([
                                        description_button_result.display()
                                ],
                                width=6,
                                ),
                                dbc.Col([
                                        button_result.display()
                                ],
                                width=6,
                                className='p-2 m-0'
                                ),
                        ], 
                        className='p-0 m-0 align-items-center',
                        style={"height": "30%"}),

                        dbc.Row([
                                dbc.Col([
                                        kpi_result.display()
                                ],
                                width=12)
                        ], 
                        className='p-0 m-0 align-items-center', 
                        justify="center",
                        style={"height": "60%"}),
                ],
                className="m-0 p-0",
                style={"height": "100%"}
                ),

        ),
        
        ],
        className="border border-primary",
    ),

    dbc.Row(
        [dbc.Col(
                html.Div([
                        dbc.Row(
                                title_3.display(),
                                className="m-0 p-0"),
                        dbc.Row([
                                
                        ]
                        ,
                        ),
                ],
                ),
            
        ),

        dbc.Col(
                html.Div([
                        dbc.Row(
                                title_4.display(),
                                className="m-0 p-0"
                        ),

                        dbc.Row([
                                
                        ]
                        ,
                        ),
                ],
                ),

        ),
        
        ],
        className="border border-primary",
    )
    
    
], 
fluid=True,
className="m-0 p-0"
)

class page2:

        def render(self):

                return page1
        


                
