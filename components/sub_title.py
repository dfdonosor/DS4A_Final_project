from dash import html 

class SubTitle:
    def __init__(self, label : str):
        self.label = label

    def display(self):
        layout = html.H3(self.label, className="p-2 m-0")
        return layout