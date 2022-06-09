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

        def __init__(self):

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
                                ]),
                                dbc.Row([
                                        dbc.Col(
                                                dcc.Graph(id='example-graph',figure=self.fig)
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col(
                                                dcc.Graph(id='example-graph',figure=self.fig2)
                                                )
                                        ])
                                ]), 
                                
                                dbc.Col([
                                        dbc.Row([
                                        dbc.Col(
                                                dbc.Card(
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
                                                                html.P("------"),
                                                                html.P("------"),
                                                                
                                                                html.P("------")
                                                                    ])
                                                        )
                                                )
                                        ]),
                                        
                                        dbc.Row([
                                        dbc.Col(
                                                dcc.Graph(id='example-graph',figure=self.fig3)
                                                )
                                        ])
                                ])
                                ])
                
                       

