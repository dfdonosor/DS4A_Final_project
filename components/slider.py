from typing import Tuple
from dash import html, dcc 

class Slider:
    def __init__(self, title : str, id_slider : str, range_slider : Tuple):
        self.title = title
        self.id_slider = id_slider
        self.range_slider = range_slider

    def display(self):
        min_value = self.range_slider[0]
        max_value = self.range_slider[1]

        layout =  html.Div([
                        html.P(self.title),
                        dcc.Slider(min = min_value, max = max_value, value=min_value, id = self.id_slider,
                                        tooltip={"placement": "bottom", "always_visible": True})
                        ], 
                        className='align-middle  p-1 m-1 shadow bg-body rounded"',
                        )
        return layout