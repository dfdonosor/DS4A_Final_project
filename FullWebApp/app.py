import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import pickle
from styles import *
from page_1 import page1
from page_2 import page2
from home_page import homepage


#with open(r'data/consolidado_datos.pickle', 'rb') as f:
#    loaded_obj = pickle.load(f)

#print(loaded_obj)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
def home_page():
        page = homepage()
        return page.render()

def page_1():
        page = page1()
        return page.render()

def page_2():
        page = page2()
        return page.render()

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Select the option you want to review", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
    )

app.layout = dbc.Container([

    dcc.Location(id="url"),

    dbc.Row(
        [dbc.Col(
            html.Img(src="https://colombia5-forum.ds4a.com/uploads/default/original/1X/9486fbcdb19b25244ce16ec41ca0ee998cf31e81.png", 
            style={"height":"100%", "width":"100%", "padding" : "1rem 1rem 1rem 1rem"} ),
            width=3,
            align="center"
        ),

        dbc.Col(
            html.H1("Access to public services and their impact on ICFES scores"),
            style={"padding" : "1rem 1rem 1rem 1rem"},
            width=8,
            align="center"
        ),

        dbc.Col(
            html.H2("Team 182"),
            className="h-5",
            width=1,
            align="end",
            style={"padding" : "0 0 0 0", "font-size": "1rem"}
        ),
        
        ],
        className="border border-primary",
        style=HEADER_STYLE
        #align="center"
    ),

    dbc.Row([dbc.Col(
            sidebar,
            width=2
        ),

        dbc.Col(
            html.Div(id="page-content", style=CONTENT_STYLE),
            width=10,
            align="center" 
        ),
    ], style={"height": "100%"}),

    
], 
fluid=True,
style=CONTAINER_STYLE
)



# Callback section: connecting the components
# ************************************************************************
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])


def render_page_content(pathname):
    if pathname == "/":
        return home_page()
    elif pathname == "/page-1":
        return page_1()
    elif pathname == "/page-2":
        return page_2()
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

    



if __name__ == "__main__":
    app.run_server(port=8888,debug=True)