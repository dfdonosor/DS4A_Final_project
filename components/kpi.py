import dash_bootstrap_components as dbc

class KPI:
    def __init__(self, kpi : str, id_kpi : str,label : str, size = "l"):
        assert size != "l" or size != "s", f"The options of size is only 'l' or 's', you introduce: {size}" 
        self.kpi = kpi
        self.id_kpi = id_kpi
        self.label = label
        self.size = size

    def display(self):
        if self.size == "l":
            size_card = "h-100 w-50 p-0"
            size_header = "card-title m-0 p-2 w-100 text-center fs-3 text-white fw-bold"
            size_body = "d-flex align-items-center justify-content-center card-text text-center m-0 p-2 w-100 fs-1 fw-bold"
        
        elif self.size == "s":
            size_card = "h-100 w-100 p-0"
            size_header = "card-title m-0 p-2 w-100 text-center fs-4 text-white fw-bold"
            size_body = "d-flex align-items-center justify-content-center text-center card-text m-0 p-2 w-100 fs-3 fw-bold"
        layout = dbc.Card([
            dbc.CardHeader(self.label, className=size_header, style={"background-color": "#2E487E"}),
            dbc.CardBody(children = self.kpi, id = self.id_kpi, className=size_body),
        ],
        className = size_card
        )
        return layout
    
if __name__ == "__main__":
    kpi_relation_1 = KPI(50, "kpi_relation_model_1", "1")