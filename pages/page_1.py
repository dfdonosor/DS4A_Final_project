
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from components.range_slider import RangerSlider

class page1:

        def __init__(self):
                self.range_slider_1 = RangerSlider("Indicator", "range-slider_1", (2018, 2020))

                self.df = pd.DataFrame({
                "Year": ["2020", "2020", "2020", "2020", "2020", "2020","2019", "2019", "2019", "2019","2019", "2019", "2018", "2018", "2018", "2018","2018", "2018"],
                "Amount": [3, 1, 6, 2, 4, 2,4, 1, 1, 4, 4, 5, 4, 1, 2, 5, 4, 5],
                "Subject": ["Math", "Natural Science", "English", "Global", "Social Citizenship", "Critical Reading", "Math", "Natural Science", "English", "Global", "Social Citizenship", "Critical Reading", "Math", "Natural Science", "English", "Global", "Social Citizenship", "Critical Reading"]
                })

                self.df2 = pd.DataFrame({
                "Year": ["Internet", "Internet", "Natural Gas", "Internet", "Internet", "Internet","Natural Gas", "Acueducto", "Acueducto", "Acueducto","Acueducto", "Electric Power", "Sewage", "Sewage", "Sewage", "Sewage","Electric Power", "Sewage","Natural Gas", "Sewage","Electric Power", "Sewage","Electric Power","Natural Gas", "Acueducto"],
                "Amount": [3, 1, 6, 2, 4, 2,4, 1, 1, 4, 4, 5, 4, 1, 2, 5, 4, 5, 2, 5, 4, 5,4,3,1],
                "Subject": ["2021", "2020", "2019", "2021", "2021", "2019", "2021", "2019", "2019", "2020", "2020", "2019", "2020", "2020", "2019", "2019", "2021", "2020", "2021", "2020", "2019", "2021","2020","2020", "2021"]
                })

                self.df3 = pd.DataFrame({
                "Year": ["Min", "Average", "Max", "Min", "Average", "Max", "Min", "Average", "Max"],
                "Amount": [100,200,300,120,220,320,150,180,300],
                "Subject": ["Cajica", "Cajica", "Cajica", "Chia", "Chia", "Chia", "Sopo", "Sopo", "Sopo",]
                })

                self.fig = px.line(self.df, x="Year", y="Amount", color="Subject")

                self.fig2 = px.bar(self.df2, x="Subject", y="Amount",color='Year', barmode='group',height=400)

                self.fig3 = px.bar(self.df3, x="Subject", y="Amount",color='Year', barmode='group',height=400)
                
        

        def render(self):
                return  dbc.Row([
                                dbc.Col([
                                                dbc.Row([
                                                        dbc.Col(
                                                                html.Div([
                                                                        html.P("Municipalities"),
                                                                        dcc.RangeSlider(min = 2018, max = 2020, step = 1,
                                                                                        tooltip={"placement": "bottom", "always_visible": True})
                                                                        ], 
                                                                        className='align-middle px-2 py-3 m-1 shadow bg-body rounded"'
                                                                        )
                                                                )
                                                        ]),
                                                dbc.Row([
                                                        dbc.Col(
                                                                html.Div([
                                                                        html.P("hola"),
                                                                        dcc.Checklist(id="checklist",
                                                                                        #options=[{"label": x, "value": x} for x in all_countries],
                                                                                        options=['Tunja', 'Zipaquira', 'Villeta',
                                                                                        'Villapinzon', 'Villagomez', 'Ubaque',
                                                                                        'Ubala', 'Tocancipa', 'Tenjo','Tena', 'Susa', 'Suesca',
                                                                                        'Sibate', 'Cajica', 'Cabrera',
                                                                                        'Arbelaez', 'Apulo', 'Agua de Dios'],
                                                                                        #value=all_countries[:3],
                                                                                        value=['Tunja', 'Zipaquira', 'Villeta'],
                                                                                        labelStyle={'display': 'block'},
                                                                                        style={"height":500, "overflow":"auto"}
                                                                                )
                                                                        ],
                                                                        className='align-middle px-2 py-3 m-1 shadow bg-body rounded"'
                                                                        )
                                                                )
                                                        ])
                                        ], md=2),
                        dbc.Col([
                        dbc.Row([
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Population", className="population"),
                                                                html.P("10")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 mt-1 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Number of Municipalities", className="municipalities"),
                                                                html.P("20")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 mt-1 shadow bg-body rounded"'
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Global Average Score", className="global_score"),
                                                                html.P("10")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Natural Science Average", className="ns_average"),
                                                                html.P("20")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Math Average", className="math_average"),
                                                                html.P("10")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("English Average", className="english_average"),
                                                                html.P("20")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Critical Reading Average", className="cr_average"),
                                                                html.P("10")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Social Citizenship Average", className="sc_average"),
                                                                html.P("20")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                )
                                        ])
                                ]),
                                dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='example-graph',figure=self.fig)
                                                ],
                                                class_name='align-middle p-1 m-1 shadow bg-body rounded"'
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='example-graph',figure=self.fig2)
                                                ],
                                                class_name='align-middle p-1 m-1 shadow bg-body rounded"'
                                                )
                                        ])
                                ]), 
                                
                                dbc.Col([
                                        dbc.Row([
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("MAP", className="cr_average"),
                                                                html.H5("UNDER CONSTRUCTION", className="cr_average"),
                                                                html.P("Cundinamarca"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                html.P("------"),
                                                                
                                                                html.P("------")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 m-1 shadow bg-body rounded"'
                                                        )
                                                )
                                        ]),
                                        
                                        dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='example-graph',figure=self.fig3)
                                                ],
                                                class_name='align-middle p-1 m-1 h-75 mt-1 shadow bg-body rounded"'
                                                )
                                        ])
                                ])


                                ])
                
                       

