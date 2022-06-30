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

title_1 = SubTitle("Input data for regression or classification modeling")
title_2 = SubTitle("Estimated score result after modeling")
title_3 = SubTitle("Relationships between public services and ICFES Score")
title_4 = SubTitle("Relationships between public services and ICFES Score")

description_range_slider_1 = DescriptionElement("Public service indicator x1")
description_range_slider_2 = DescriptionElement("Public service indicator x2")
description_range_slider_3 = DescriptionElement("Other important indicator")

range_slider_1 = Slider("Indicador internet", "range-slider-internet", 0.01,(float(df["INDICADOR_INTERNET"].min()), float(df["INDICADOR_INTERNET"].max())))
range_slider_2 = Slider("Indicador gas natural", "range-slider-gas", 0.01,(float(df["INDICADOR_GAS_NATURAL"].min()), float(df["INDICADOR_GAS_NATURAL"].max())))
range_slider_3 = Slider("Indicador distancia (km)", "range-slider-dist", 10,(float(df["KmDist"].min()), float(df["KmDist"].max())))

description_button_result = DescriptionElement("Global ICFES score")
button_result = Button("Estimated result", "button_result")

kpi_result = KPI(50, "kpi_result_model_reg", "Result")

kpi_relation_1 = KPI(50, "kpi_relation_model_1", "Indicator 1", "s")
kpi_relation_2 = KPI(50, "kpi_relation_model_2", "Indicator 2", "s")
kpi_relation_3 = KPI(50, "kpi_relation_model_3", "Indicator 3", "s")
kpi_relation_4 = KPI(50, "kpi_relation_model_4", "Indicator 4", "s")

r1_c1 = dbc.Col([
                dbc.Row(
                        title_1.display(),
                        className="m-0 p-0",
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
                className='p-0 m-0',
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
                className='p-0 m-0',
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
                className='p-0 m-0',
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
                        style = {"height" : "50%"}
                        ),

                dbc.Row([
                        dbc.Col([
                                kpi_result.display()
                                ],
                                width=12,
                                className="d-flex justify-content-center align-items-center h-100")
                        ], 
                        className='p-0 m-0 align-items-center', 
                        justify="center",
                        style = {"height" : "40%"})
        ], 
        className="m-0 p-0 mh-100"
        )

r2_c1 = dbc.Col([
        dbc.Row(
                title_3.display(),
                className="m-0 p-0",
                style = {"height" : "10%"}
        ),

        dbc.Row([
                        dbc.Col([
                                kpi_relation_1.display()
                        ],
                        width=3,
                        ),

                        dbc.Col([
                               kpi_relation_2.display()
                        ],
                        width=3,
                        ),

                        dbc.Col([
                                kpi_relation_3.display()
                        ],
                        width=3,
                        ),

                        dbc.Col([
                               kpi_relation_4.display()
                        ],
                        width=3,
                        ),
                ], 
                className='p-0 m-0',
                style = {"height" : "20%"}
                ),
                

                dbc.Row([
                        
                ], 
                className='p-0 m-0',
                style = {"height" : "50%"}
                ),

                dbc.Row([
                        html.H4('"Description of the services that most affect the ICFES results."', id="description_service_most_relevant", className="text-center fst-italic")
                ], 
                className='p-0 m-0',
                style = {"height" : "20%"}
                ),
  
], 
className="m-0 p-0 mh-100"   
)

r2_c2 = dbc.Col([
        dbc.Row(
        title_4.display(),
        className="m-0 p-0",
        style = {"height" : "10%"}
        ),
        
        dbc.Row([

                ]
                ),
], 
className="m-0 p-0 mh-100" 
)

page = dbc.Container([

        dbc.Row([
                r1_c1,
                r1_c2
        ],
        className="m-0 p-0",
        style = {"height" : "40%"}
        ),

        dbc.Row([
                r2_c1,
                r2_c2
        ],
        className="m-0 p-0",
        style = {"height" : "60%"}
        )
], 
fluid=True,
className="m-0 p-0 vh-100"
)

class page2:
        def render(self):
                return page
        


                
