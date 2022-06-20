from dash import html 

class DescriptionElement:    
    def __init__(self, description : str):
        self.description = description

    def display(self):
        layout = html.H5(self.description, className='text-center align-middle')  
        return layout