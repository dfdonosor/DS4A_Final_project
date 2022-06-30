from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
#import dash_labs as dl
from callbacks import register_callbacks

#with open(r'data/consolidado_datos.pickle', 'rb') as f:
#    loaded_obj = pickle.load(f)

app = Dash(__name__, update_title='Cargando...', 
            external_stylesheets=[dbc.themes.BOOTSTRAP], 
            suppress_callback_exceptions=True,
            meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])
server = app.server

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
        )
    ]
    )

app.layout = dbc.Container([
    dcc.Location(id="url"),

    dbc.Row(
        className="app-title",
        children=[dbc.Col(
            html.Img(src="https://colombia5-forum.ds4a.com/uploads/default/original/1X/9486fbcdb19b25244ce16ec41ca0ee998cf31e81.png", 
                    style={'height':'100%', 'width':'100%'}),
            width=2,
            align="center"
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
    app.run_server(port=8080,debug=True)