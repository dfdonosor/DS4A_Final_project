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

range_slider_1 = RangerSlider("Indicator", "range-slider_1", (0, 20))
range_slider_2 = RangerSlider("Indicator", "range-slider_2", (0, 20))
range_slider_3 = RangerSlider("Indicator", "range-slider_3", (0, 20))

description_button_result = DescriptionElement("Global ICFES score")
button_result = Button("Estimated result", "button_result")

kpi_result = KPI(50, "kpi_result_model", "Result")

r1_c1 = dbc.Col([
                dbc.Row(
                        title_1.display(),
                        className="m-0 p-0 border border-primary",
                        style = {"height" : "10%"}
                ),

                
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
                ], 
                className='p-0 m-0 border border-primary',
                style = {"height" : "30%"}
                ),
                

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
                ], 
                className='p-0 m-0 border border-primary',
                style = {"height" : "30%"}
                ),

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
                ], 
                className='p-0 m-0 border border-primary',
                style = {"height" : "30%"}
                ),

        ],
        className='p-0 m-0 border border-primary h-100'
        )           

r1_c2 = dbc.Col([
                dbc.Row(
                        title_2.display(),
                        className="m-0 p-0 align-items-center border border-primary",
                        style = {"height" : "10%"}
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
                        className='p-2 m-0 border border-primary'
                        ),

                        ], 
                        className='p-0 m-0 align-items-center border border-primary',
                        style = {"height" : "50%"}
                        ),

                dbc.Row([
                        dbc.Col([
                                kpi_result.display()
                                ],
                                width=12,
                                className="d-flex justify-content-center align-items-center border border-primary h-100")
                        ], 
                        className='p-0 m-0 align-items-center border border-primary', 
                        justify="center",
                        style = {"height" : "40%"})
        ], 
        className="m-0 p-0 mh-100 border border-primary"
        )

r2_c1 = dbc.Col([
        dbc.Row(
                title_3.display(),
                className="m-0 p-0"
        ),

        dbc.Row([

        ]
        ),    
]   
)

r2_c2 = dbc.Col([
        dbc.Row(
        title_4.display(),
        className="m-0 p-0"
        ),
        
        dbc.Row([

                ]
                ),
]
)

page = dbc.Container([

        dbc.Row([
                r1_c1,
                r1_c2
        ],
        className="m-0 p-0 border border-primary",
        style = {"height" : "40%"}
        ),

        dbc.Row([
                r2_c1,
                r2_c2
        ],
        className="m-0 p-0 border border-success h",
        style = {"height" : "60%"}
        )
], 
fluid=True,
className="m-0 p-0 border border-danger vh-100"
)

class page2:
        def render(self):
                return page
        


                
