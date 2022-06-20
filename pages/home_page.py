import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt

class homepage:
        
        def render(self):
                return html.P("This is the content of the home page!")

        

