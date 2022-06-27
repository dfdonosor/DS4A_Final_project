import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt

p1 = """
This (change x2) application has the purpose of showing the most important results that have been found between the result of the ICFES exam and access to the following services:
"""

p2 = """
On page 1 the most important results are shown, represented by interactive graphs that will allow the user to search and explore the information.
On page 2, a predictive model is structured that, according to some input variables given by the user, will estimate the ICFES score that will be obtained.
"""

internet_detail = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut bibendum turpis. Fusce nibh enim, fringilla vel tincidunt et, commodo vitae tortor. 
Suspendisse nec nunc interdum, posuere enim et, sagittis mauris. Proin congue lectus leo, sit amet lacinia dolor eleifend eu. 

Phasellus ac feugiat odio.
"""

aqueduct_detail = """
Vivamus blandit augue sed risus vulputate viverra. Etiam at eros ullamcorper, iaculis massa a, malesuada nulla. 
"""

sewerage_detail = """
Vestibulum facilisis pulvinar sagittis. Fusce interdum imperdiet metus, ac finibus diam commodo sed. Ut ut condimentum diam, ut tincidunt velit. 
Aliquam purus turpis, congue consectetur velit eget, pellentesque dignissim nibh. Cras tellus libero, bibendum id finibus a, sodales gravida arcu.
"""
energy_gas_detail = """
Vivamus vehicula est lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
Aliquam tincidunt erat in lorem cursus facilisis. Aliquam quis lacus tellus. Praesent nec porttitor tellus. Donec malesuada maximus nisi eu pharetra. 
Sed ligula arcu, sodales eget mauris nec, fringilla interdum dolor. Nunc id faucibus enim. Nunc nec faucibus dui. Pellentesque rutrum pharetra justo eget sollicitudin. 
"""


services = dbc.ListGroup([
                dbc.ListGroupItem("Internet",className="list-group-item list-group-item-action w-100", id="internet", n_clicks=0),
                dbc.ListGroupItem("Aqueduct",className="list-group-item list-group-item-action w-100", id="aqueduct", n_clicks=0),
                dbc.ListGroupItem("Sewerage",className="list-group-item list-group-item-action w-100", id="sewerage", n_clicks=0),
                dbc.ListGroupItem("Electric Energy and Natural Gas",className="list-group-item list-group-item-action w-100", id="energy-gas", n_clicks=0),

        ],className="list-group")

explained_services = html.Div([
                dbc.Collapse(
                        dbc.Card(children=internet_detail, body=True, className="w-100 h-100"),
                        className="w-100 h-100",
                        id="collapse-internet",
                        is_open=True,
                    ),

                dbc.Collapse(
                        dbc.Card(children=internet_detail, body=True, className="w-100 h-100"),
                        className="w-100 h-100",
                        id="collapse-aqueduct",
                        is_open=False,
                    ),

                dbc.Collapse(
                        dbc.Card(children=internet_detail, body=True, className="w-100 h-100"),
                        className="w-100 h-100",
                        id="collapse-sewerage",
                        is_open=False,
                    ),

                dbc.Collapse(
                        dbc.Card(children=internet_detail, body=True, className="w-100 h-100"),
                        className="w-100 h-100",
                        id="collapse-energy-gas",
                        is_open=False,
                    ),

                
                ],className="w-100 h-100")
      

page = dbc.Container([

        dbc.Row(
                html.P(p1, className="px-0"),
                className="m-2 p-2 w-75"
        ),

        dbc.Row([
                dbc.Col([
                        services
                ],
                width=4
                ),

                dbc.Col([
                        explained_services
                ],
                width=6
                ),

        ], className="m-2 p-2 w-75"),

        dbc.Row(
                html.P(p2, className="px-0"),
                className="m-2 p-2 w-75"
        ),
        ], 

fluid=True,
className="m-0 p-5 vh-100 justify-content-md-center")

class homepage:
        def render(self):
                return page

        

