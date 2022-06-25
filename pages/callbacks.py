import dash
from dash import dcc, html, Input, Output, State, callback
from pages.home_page import homepage
from pages.page_1 import page1
from pages.page_2 import page2
import dash_bootstrap_components as dbc

def register_callbacks(app):
        
    #@app.callback()
    # Callback section: connecting the components
    # ************************************************************************
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return homepage().render()
        elif pathname == "/page-1":
            return page1().render()
        elif pathname == "/page-2":
            return page2().render()
        # If the user tries to reach a different page, return a 404 message
        return dbc.Alert(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ], color="warning"
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
    Output("aqueduct", "active"), 
    Input("aqueduct", "n_clicks")
    )
    def toggle_state(n_aqueduct):
        if n_aqueduct:
            print(n_aqueduct)
            return True
            

