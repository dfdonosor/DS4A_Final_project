import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #Ubicamos el interprete en la carpeta actual
from dash import Dash, callback, dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
from components.kpi import KPI
from components.Table import Table

kpi_reg_procces = KPI("", "kpi_model_reg", "Process", "s")
kpi_reg_r_square = KPI("0.441", "kpi_reg_r_square", "R-square", "s")
kpi_classi_procces = KPI("", "kpi_model_classi", "Process", "s")

intro_txt = """This application is the result of a complete analysis of the relationship between **public services** and **ICFES**
(Colombian Institute for the Promotion of Higher Education) score,
the application has an **interactive data visualization** that allows to navigate through the data and understand the relationships,
in addition to this in the **prediction section** there are models that from input data provided by the user predicts the average ICFES
score that the municipality will have with those characteristics. This tool is extremely powerful to find ways to improve the performance
of the results for a municipality. 
"""

background_txt_1 = """
The **ICFES** (Colombian Institute for the Promotion of Higher Education) conducts biannual knowledge tests for students in grade 11. 
These results allow them to establish a selfevaluation of the quality of the education provided and the resources allocated for this purpose. 
"""

background_txt_2 = """
**Our proposal** focuses on the impact of access to different public services (Aqueduct, Sewerage, Energy, Gas, and Internet) on performance in the ICFES tests.
"""

data_txt = """
We took data from the department of **Cundinamarca**,
due to its high number of municipalities **(116)** and the
high diversity among them, these data were delimited
to the years **2019 and 2020**.
"""

regression_model_txt = """
We split the data in 
and testing data (80%,
20% respectively)
"""
kpi_reg_procces.kpi = regression_model_txt
reg_table = Table(["Feature", "Coef"])
reg_table.append_row(["KmDist","-0.10"])
reg_table.append_row(["Internet","137.8"])
reg_table.append_row(["Gas","-53.3"])

classification_model_txt = """
We use XGBoost, to
classify into two
groups the Icfes
scores, high score and
low score (0 or 1), the
separation point is
246.
"""
kpi_classi_procces.kpi = classification_model_txt
classi_table = Table(["Metric", "Score"])
classi_table.append_row(["Accuracy","8"])
classi_table.append_row(["Prec.","8"])
classi_table.append_row(["AUC","8"])
classi_table.append_row(["F1","7"])
classi_table.append_row(["Recall","7"])

background = dbc.Row([
            dbc.Row([
                dbc.Col([
                    html.Img(src="assets\icfes.svg", className="img-fluid h-100 w-100"),
                ], width=1),

                dbc.Col([
                    dcc.Markdown(background_txt_1),
                ], width=6)
               
            ]),

            dbc.Row([
               dbc.Col([
                    dcc.Markdown(background_txt_2),
                ], width=6),

                dbc.Col([
                    html.Img(src="assets\chart.svg", className="img-fluid h-75 w-75")
                ], width=1)
            ]),
        ],
        className="m-0 p-0",
        )

data = dbc.Row([
               dcc.Markdown(data_txt),
               html.Img(src="assets\diagram.svg", className="img-fluid")
        ],
        className="m-0 p-0",
        )

regression_model = dbc.Row([
                dbc.Col([

                    dbc.Row([
                    kpi_reg_procces.display()
                    ], className="m-2 p-2"),

                    dbc.Row([
                    reg_table.display()
                    ], className="m-2 p-2"),

                    dbc.Row([
                    kpi_reg_r_square.display()
                    ], className="m-2 p-2"),

                ], width=3),

                dbc.Col([
                    html.Img(src=r"assets\residual_fitted.png", className="img-fluid h-100 w-100"),
                ], width=8)
            ], className="m-2 p-2")

classification_model = dbc.Row([
                dbc.Col([

                    dbc.Row([
                    kpi_classi_procces.display()
                    ], className="m-2 p-2"),

                    dbc.Row([
                    classi_table.display()
                    ], className="m-2 p-2"),

                ], width=3),

                dbc.Col([
                    html.Img(src=r"assets\roc_clasification.png", className="img-fluid h-100 w-100"),
                ], width=8)
               
            ])


page = html.Div([

        dcc.Markdown(intro_txt),

    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    background,
                ],
                title="BACKGROUND",
            ),
            dbc.AccordionItem(
                [
                    data,
                ],
                title="DATA",
            ),

            dbc.AccordionItem(
                [
                    regression_model,
                ],
                title="REGRESSION MODEL",
            ),

            dbc.AccordionItem(
                [
                    classification_model,
                ],
                title="CLASSIFICATION MODEL",
            ),
        ],
    ),
    ],
    className="p-5 m-0 align-items-center justify-content-center text-start text-wrap lh-sm w-100 fs-4",
)

class homepage:
        def render(self):
                return page

        

