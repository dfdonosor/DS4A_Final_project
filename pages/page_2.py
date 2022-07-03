import os
# importing sys
import sys
# adding Folder_2 to the system path
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from components.sub_title import SubTitle
from components.slider import Slider
from components.description_element import DescriptionElement
from components.button import Button 
from components.kpi import KPI
from data.data import DataApp

df = DataApp.df

title_1 = SubTitle("Input data for regression and classification modeling")
title_2 = SubTitle("Estimated score result after modeling")
title_3 = SubTitle("Relationships between public services and ICFES Score")
title_4 = SubTitle("Relationships between public services and ICFES Score")

description_range_slider_1 = DescriptionElement("INTERNET")
description_range_slider_2 = DescriptionElement("NATURAL GAS")
description_range_slider_3 = DescriptionElement("DISTANCE")

range_slider_1 = Slider("Indicator internet", "range-slider-internet", 0.01,(0, 1))
range_slider_2 = Slider("Indicator natural gas", "range-slider-gas", 0.01,(0, 1))
range_slider_3 = Slider("Indicator distance(km)", "range-slider-dist", 10,(float(df["KmDist"].min()), float(df["KmDist"].max())))

description_result_reg = DescriptionElement("Regression model")
description_result_classi = DescriptionElement("Classification model")
button_result = Button("Estimated result", "button_result")

kpi_result_reg = KPI("", "kpi_result_model_reg", "Result", "s")
kpi_result_classi = KPI("", "kpi_result_model_classi", "Result", "s")

r1_c1 = dbc.Col([
                dbc.Row(
                        title_1.display(),
                        className="m-0 p-0 align-items-center",
                        style = {"height" : "10%"}
                ),
                
                dbc.Row([
                        dbc.Col([
                                description_range_slider_1.display()
                        ],
                        width=4,
                        ),

                        dbc.Col([
                                range_slider_1.display()
                        ],
                        width=8,
                        ),
                ], 
                className='p-0 m-0 d-flex align-items-center justify-content-center',
                style = {"height" : "30%"}
                ),
                
                dbc.Row([
                        dbc.Col([
                                description_range_slider_2.display()
                                ],
                                width=4,
                                ),

                                dbc.Col([
                                        range_slider_2.display()
                                ],
                                width=8,
                                ),
                ], 
                className='p-0 m-0 container d-flex align-items-center justify-content-center',
                style = {"height" : "30%"}
                ),

                dbc.Row([
                        dbc.Col([
                                description_range_slider_3.display()
                        ],
                        width=4,
                        ),
                                        
                        dbc.Col([
                                range_slider_3.display()
                        ],
                        width=8,
                        ),
                ], 
                className='p-0 m-0 container d-flex align-items-center justify-content-center',
                style = {"height" : "30%"}
                ),

        ],
        className='p-0 m-0 h-100'
        )           

r1_c2 = dbc.Col([
                dbc.Row(
                        title_2.display(),
                        className="m-0 p-0 align-items-center",
                        style = {"height" : "10%"}
                ),

                dbc.Row([
                        dbc.Col([
                                button_result.display()
                        ],
                        width=12,
                        className='p-2 m-0'
                        ),

                        ], 
                        className='p-0 m-0 align-items-center',
                        style = {"height" : "20%"}
                        ),

                dbc.Row([
                        dbc.Col([
                                description_result_reg.display()
                        ],
                        width=6,
                        ),

                        dbc.Col([
                                kpi_result_reg.display()
                        ],
                        width=6,
                        className="d-flex justify-content-center align-items-center h-75")
                        ], 
                        className='p-0 m-0 align-items-center', 
                        justify="center",
                        style = {"height" : "30%"}),

                dbc.Row([
                        dbc.Col([
                                description_result_classi.display()
                        ],
                        width=6,
                        ),

                        dbc.Col([
                                kpi_result_classi.display()
                                ],
                                width=6,
                                className="d-flex justify-content-center align-items-center h-75")
                        ], 
                        className='p-0 m-0 align-items-center', 
                        justify="center",
                        style = {"height" : "40%"})
        ], 
        className="m-0 p-0 mh-100"
        )


page = dbc.Container([

        dbc.Row([
                r1_c1,
                r1_c2
        ],
        className="m-0 p-0",
        style = {"height" : "70%"}
        ),

        dbc.Row([
                
        ],
        className="m-0 p-0",
        style = {"height" : "30%"}
        )
], 
fluid=True,
className="m-0 p-0 vh-100"
)

class page2:
        def render(self):
                return page
        


                
