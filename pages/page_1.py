
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from components.range_slider import RangerSlider
from data.data import DataApp
import plotly.graph_objects as go
import geopandas
import json
import numpy as np

data = DataApp.df


def make_starting_map(geojson_file, geojson_join_col, df, cov):
            """
            Takes a geojson, a dataframe of data, and column, and creates a starting map that can then have buttons added.
           
            This map will not actually display data, and instead requires data to be added via make_buttons_for_map
           
            geojson_file (string): filepath to geojson that you want to map
            geojson_join_col (string): column name of geography that you want to map in the geojson
            df (dataframe): Dataframe that you want to map. The geography needs to be the index of the dataframe
            cov (string): Column name of the data that you want to map
            """
           
            
            
            gdf = geopandas.read_file(geojson_file)
            ### Get center point and zoom level ###
            box = gdf.total_bounds
            center_lon = (box[0]+box[2])/2
            center_lat = (box[1]+box[3])/2
            zoom = 6
            ### CHECKING ###
            # Check to make sure that the row identifier of the geojson matches the index of the df passed in
           
            if len(df.index) > len(df.index.unique()):
                print('Index of data does not appear to be unique!')
           
            assert geojson_join_col in gdf.columns, 'geojson_join_col needs to be in geojson'
            assert gdf[geojson_join_col].dtype == df.index.dtype, 'Datatype of row identifier in geojson does not match datatype of index of dataframe'
         
           
            shape_set = set(gdf[geojson_join_col].unique())
            data_set = set(df.index.unique())
         
            shape_not_found = shape_set - data_set
            data_not_found = data_set - shape_set
         
            print('Fraction of shapes not found in data: ' + str(len(shape_not_found)/len(shape_set)))
            print('Fraction of data not found in shapes: ' + str(len(data_not_found)/len(data_set)))
         
            if len(shape_not_found) > 0:
                print('Shapes not found: ' + str(shape_not_found))
            if len(data_not_found) > 0:
                print('Data rows not found: ' + str(data_not_found))
           
            
            # Load geojson in as a json to be compatible with plotly
            with open(geojson_file) as f:
                terr = json.load(f)
           
            # Get starting map color scale
            mid_point = (1 - df[cov].min()) / (df[cov].max() - df[cov].min())
            if np.isnan(mid_point) or mid_point <= 0:
                mid_point = 0.5
            my_scale = [(0,"orange"), (mid_point, "white"), (1,"purple")]
         
            # Make starting map
            fig = px.choropleth_mapbox(df, geojson=terr, locations= df.index, color = cov,
                                           featureidkey=f"properties.{geojson_join_col}",
                                           color_continuous_scale = 'Viridis',
                                           mapbox_style="open-street-map",
                                           zoom=zoom,
                                           center = {"lat": center_lat, "lon": center_lon},
                                           opacity=0.5,
                                           hover_data = {cov : ':.3f', 'MUNICIPIO' : True}
                                          )
            return fig

class page1:

        def __init__(self):
                self.data = DataApp.df

                
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

                self.fig3 = px.bar(self.data, x="MUNICIPIO", y="PUNT_GLOBAL_MEAN",color='ANO', barmode='group',height=400)

                self.fig3 = go.Figure(data=[
                        go.Bar(name='Min', x=self.data['MUNICIPIO'], y=self.data['PUNT_GLOBAL_MIN']),
                        go.Bar(name='Average', x=self.data['MUNICIPIO'], y= self.data['PUNT_GLOBAL_MEAN']),
                        go.Bar(name='Max', x=self.data['MUNICIPIO'], y=self.data['PUNT_GLOBAL_MAX'])
                ])
                # Change the bar mode
                self.fig3.update_layout(barmode='group')

                print(self.data.columns)

        
        @callback(
                Output("fig_map", "figure"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )

        def grafica_1(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]

                filtered_df = filtered_df[['COD_MUNICIPIO', 'PUNT_GLOBAL_MEAN', 'MUNICIPIO']]
                filtered_df = filtered_df.rename(columns={"COD_MUNICIPIO": "MPIO_CCDGO"})
                filtered_df = filtered_df.groupby(['MPIO_CCDGO','MUNICIPIO']).mean().reset_index()


                #filtered_df.set_index('MPIO_CDPMP', inplace = True)
                print(filtered_df.shape)

                filtered_df['MPIO_CCDGO'] = filtered_df['MPIO_CCDGO'].astype(str)
                filtered_df = filtered_df.set_index('MPIO_CCDGO')
                fig = make_starting_map("cundi.json", 'MPIO_CCDGO',filtered_df,'PUNT_GLOBAL_MEAN')
                return fig 

        @callback(
                Output("fig_scores", "figure"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def grafica_1(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]

                filtered_df = filtered_df.groupby('ANO').mean().reset_index()
                
                fig1 = go.Figure(data=[
                        #go.Line(name='Global', x=filtered_df['ANO'], y=filtered_df['PUNT_GLOBAL_MEAN']),
                        go.Line(name='Math', x=filtered_df['ANO'], y= filtered_df['PUNT_MATEMATICAS_MEAN']),
                        go.Line(name='Science', x=filtered_df['ANO'], y=filtered_df['PUNT_C_NATURALES_MEAN']),
                        go.Line(name='Critical Reading', x=filtered_df['ANO'], y=filtered_df['PUNT_LECTURA_CRITICA_MEAN']),
                        go.Line(name='Social Citizenship', x=filtered_df['ANO'], y=filtered_df['PUNT_SOCIALES_CIUDADANAS_MEAN']),
                        go.Line(name='English', x=filtered_df['ANO'], y=filtered_df['PUNT_INGLES_MEAN'])
                ])

                
                
                # Change the bar mode
                fig1.update_layout(title="Average score by subject by year")

                return fig1

        @callback(
                Output("fig_servicios", "figure"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def grafica_2(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
                
                fig2 = go.Figure(data=[
                        go.Bar(name='Internet', x=filtered_df['ANO'], y=filtered_df['INDICADOR_INTERNET']),
                        go.Bar(name='Natural Gass', x=filtered_df['ANO'], y= filtered_df['INDICADOR_GAS_NATURAL']),
                        go.Bar(name='Water Supply', x=filtered_df['ANO'], y=filtered_df['INDICADOR_ACUEDUCTO']),
                        go.Bar(name='Electric Power', x=filtered_df['ANO'], y=filtered_df['INDICADOR_ENERGIA_ELECTRICA']),
                        go.Bar(name='Sewage', x=filtered_df['ANO'], y=filtered_df['INDICADOR_ALCANTARILLADO'])
                ])

                # Change the bar mode
                fig2.update_layout(barmode='group', title="Access to public services by year")

                return fig2

        @callback(
                Output("min-max", "figure"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def grafica_min_max(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
                
                fig3 = go.Figure(data=[
                        go.Bar(name='Min', x=filtered_df['MUNICIPIO'], y=filtered_df['PUNT_GLOBAL_MIN']),
                        go.Bar(name='Average', x=filtered_df['MUNICIPIO'], y= filtered_df['PUNT_GLOBAL_MEAN']),
                        go.Bar(name='Max', x=filtered_df['MUNICIPIO'], y=filtered_df['PUNT_GLOBAL_MAX'])
                ])
                # Change the bar mode
                fig3.update_layout(barmode='group', title="Global score statistics (min,max,mean)")

                return fig3

        @callback(
                Output("population", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def pupulation_card(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['POBLACION'].mean())

        @callback(
                Output("n_municipalities", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def municipalities_card(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['MUNICIPIO'].nunique())

        @callback(
                Output("average_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def average_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_GLOBAL_MEAN'].mean())

        @callback(
                Output("science_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def science_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_C_NATURALES_MEAN'].mean())

        @callback(
                Output("social_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def science_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_SOCIALES_CIUDADANAS_MEAN'].mean())

        @callback(
                Output("math_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def science_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_MATEMATICAS_MEAN'].mean())

        @callback(
                Output("english_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def science_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_INGLES_MEAN'].mean())

        @callback(
                Output("reading_score", "children"),
                [
                        Input("checklist", "value"), 
                        Input("year-slicer", "value")
                ],

        )
        def science_score(municipios_list, years,*args):
                filtered_df = data[data["MUNICIPIO"].isin(municipios_list)]
                filtered_df = filtered_df[filtered_df["ANO"] >= years[0]]
                filtered_df = filtered_df[filtered_df["ANO"] <= years[1]]
        
                
                return round(filtered_df['PUNT_LECTURA_CRITICA_MEAN'].mean())




        def render(self):
                return  dbc.Row([
                                dbc.Col([
                                                dbc.Row([
                                                        dbc.Col(
                                                                html.Div([
                                                                        html.P("Municipalities"),
                                                                        dcc.RangeSlider(min = 2019, max = 2020, step = 1,
                                                                                        tooltip={"placement": "bottom", "always_visible": True}, id = "year-slicer", value=[2019, 2020])
                                                                        ], 
                                                                        className='align-middle px-2 py-3 m-1 shadow bg-body rounded"'
                                                                        )
                                                                )
                                                        ]),
                                                dbc.Row([
                                                        dbc.Col(
                                                                html.Div([
                                                                        html.P("Filtro por municipios"),
                                                                        dcc.Checklist(id="checklist",
                                                                                        options=[{"label": x, "value": x} for x in self.data['MUNICIPIO'].unique()],
                                                                                        #options=['Tunja', 'Zipaquira', 'Villeta',
                                                                                        #'Villapinzon', 'Villagomez', 'Ubaque',
                                                                                        #'Ubala', 'Tocancipa', 'Tenjo','Tena', 'Susa', 'Suesca',
                                                                                        #'Sibate', 'Cajica', 'Cabrera',
                                                                                        #'Arbelaez', 'Apulo', 'Agua de Dios'],
                                                                                        value=self.data['MUNICIPIO'].unique()[:3],
                                                                                        #value=['Tunja', 'Zipaquira', 'Villeta'],
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
                                                                html.P(children = ["10"], id = "population")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 mt-1 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Number of Municipalities", className="municipalities"),
                                                                html.P(children = ["1"], id = "n_municipalities")
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
                                                                html.P(children = ["10"], id = "average_score")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Natural Science Average", className="ns_average"),
                                                                html.P(children = ["10"], id = "science_score")
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
                                                                html.P(children = ["10"], id = "math_score")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("English Average", className="english_average"),
                                                                html.P(children = ["10"], id = "english_score")
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
                                                                html.P(children = ["10"], id = "reading_score")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card([
                                                        dbc.CardBody([
                                                                html.H5("Social Citizenship Average", className="sc_average"),
                                                                html.P(children = ["10"], id = "social_score")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 mx-1 h-75 shadow bg-body rounded"'
                                                        )
                                                )
                                        ])
                                ]),
                                dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='fig_scores')
                                                ],
                                                class_name='align-middle p-1 m-1 shadow bg-body rounded"'
                                                )
                                        ]),
                                dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='fig_servicios')
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
                                                                html.H5("Municipalities and ICFES Score", className="cr_average"),
                                                                dcc.Graph(id="fig_map")
                                                                    ])
                                                        ],
                                                        class_name='align-middle p-1 m-1 shadow bg-body rounded"'
                                                        )
                                                )
                                        ]),
                                        
                                        dbc.Row([
                                        dbc.Col([
                                                dcc.Graph(id='min-max')
                                                ],
                                                class_name='align-middle p-1 m-1 h-75 mt-1 shadow bg-body rounded"'
                                                )
                                        ])
                                ])


                                ])
                
                       

