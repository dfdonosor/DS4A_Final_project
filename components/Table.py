import dash_bootstrap_components as dbc
from dash import html

class Table:
    
    def __init__(self, columns_names : list):
        assert len(columns_names) >= 0, f"The number of column_names must be an integer greater than 0, you pass {str(len(columns_names))} column_names"
        self.column_names = columns_names
        self.rows_values = []

    @staticmethod
    def header(columns_names):
        names = []
        for name in columns_names:
            names.append(html.Th(name))

        table_header = [html.Thead(html.Tr(names))]

        return table_header
 
    def append_row(self, rows):
        assert len(rows) == len(self.column_names), f"The number of rows elements must be equal to the column_names, columns_names = {str(len(self.column_names))} you pass {str(len(rows))} column_names"
        rows_val = []
        for element in rows:
            rows_val.append(html.Td(element))
        self.rows_values.append(html.Tr(rows_val))

    def display(self):
        table_body = [html.Tbody(self.rows_values)]

        layaout = dbc.Table(Table.header(self.column_names) + table_body, bordered=True, striped=True, hover=True)

        return layaout

if __name__ == "__main__":
    classi_table = Table(["Metric", "Score"])
    classi_table.append_row(["Accuracy","8"])
    classi_table.append_row(["Prec.","8"])
    classi_table.append_row(["AUC","8"])
    classi_table.append_row(["F1","7"])
    classi_table.append_row(["Recall","7"])
    classi_table.display()