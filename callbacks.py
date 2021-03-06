import dash
import pandas as pd
from dash import dcc, html, Input, Output, State,callback
from pages.home_page import homepage
from pages.page_1 import page1
from pages.prediction_page import prediction
import dash_bootstrap_components as dbc
from data.data import DataApp
from pycaret.classification import *

modelo_reg = DataApp.modelo_reg

def register_callbacks(app):
        
    #@app.callback()
    # Callback section: connecting the components
    # ************************************************************************
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return homepage().render()
        elif pathname == "/data_visualization":
            return page1().render()
        elif pathname == "/prediction":
            return prediction().render()
        # If the user tries to reach a different page, return a 404 message
        return dbc.Alert(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
    
    @app.callback(
        Output('output-container-range-slider', 'children'),
        Input('range-slider_1', 'value'))
    def update_output(value):
        print('You have selected "{}"'.format(value))

    @app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")])
    def on_button_click(n):
        if n is None:
            return "Not clicked."
        else:
            return f"Clicked {n} times."

    @app.callback(
        Output("kpi_result_model_reg", "children"),
        Input("button_result","n_clicks"),
        State("range-slider-internet","value"),
        State("range-slider-gas","value"),
        State("range-slider-dist","value"),
        
    )
    def model_reg(btn, val_int, val_gas, val_dist):
        data_input_df = pd.DataFrame({"KmDist" : [float(val_dist)], 
                                    "INDICADOR_GAS_NATURAL" : [float(val_gas)], 
                                    "INDICADOR_INTERNET" : [float(val_int)]})
        prediction = str(round(float(modelo_reg.predict(data_input_df))))
        
        return prediction

    @app.callback(
        Output("kpi_result_model_classi", "children"),
        Output("kpi_result_model_classi", "style"),
        Input("button_result","n_clicks"),
        State("range-slider-internet","value"),
        State("range-slider-gas","value"),
        State("range-slider-dist","value"),
        
    )
    def model_classi(btn, val_int, val_gas, val_dist):
        data_input_df = pd.DataFrame({"KmDist" : [float(val_dist)], 
                                    "INDICADOR_GAS_NATURAL" : float(val_gas), 
                                    "INDICADOR_INTERNET" : float(val_int)})
        prediction = predict_model(DataApp.modelo_classif, data = data_input_df)
        result = float(prediction["Label"].values[0])
        if result == 1:
            return "Above the departmental average", {"background-color": "#198754", "color" : "white"}
        if result == 0:
            return "Below the departmental average", {"background-color": "#df4759", "color" : "white"}
        else:
            return "Undefined"