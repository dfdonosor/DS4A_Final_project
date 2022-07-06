import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
#import dash_labs as dl
from callbacks import register_callbacks

#with open(r'data/consolidado_datos.pickle', 'rb') as f:
#    loaded_obj = pickle.load(f)

app = Dash(__name__, update_title='Cargando...', 
            external_stylesheets=[dbc.themes.BOOTSTRAP], 
            suppress_callback_exceptions=True)
server = app.server

app.title = "DS4A Icfes predictor app - T182"

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Select the option you want to review", className="lead fs-5"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", className="fs-4"),
                dbc.NavLink("Data Visualization", href="/data_visualization", active="exact", className="fs-4"),
                dbc.NavLink("Prediction", href="/prediction", active="exact", className="fs-4"),
            ],
            vertical=True,
            pills=True,
        )
    ]
    )

app.layout = dbc.Container([
    dcc.Location(id="url"),

    dbc.Row(
        className="app-title",
        children=[dbc.Col(
            html.Img(src=app.get_asset_url('logo.svg'), 
                    style={'height':'100%', 'width':'100%'}),
            width=2,
            align="center",
            className="py-0 my-0 align-self-center col-2"
        ),

        dbc.Col(
            html.H1("Access to public services and their impact on ICFES scores", className="text-center"),
            width=9,
            align="center"
        ),

        dbc.Col(
            html.H5("Team 182"),
            width=1,
            align="end"
        ),        
        ],
    ),

    dbc.Row([dbc.Col(
        sidebar,
        width=2,
        ),

    dbc.Col(
        html.Div(id="page-content"),
        align="center" 
    )
    ]),
], 
fluid=True,
)

# Call to external function to register all callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(port=8080,debug=False)