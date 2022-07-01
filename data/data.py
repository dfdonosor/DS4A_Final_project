import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from mimetypes import init
import pandas as pd
from pycaret.classification import *
import statsmodels.api as sm

class DataApp:
    #Open the consolodida_datos
    df = pd.read_pickle("consolidado_datos.pickle")
    #Open the modelo_reg
    modelo_reg = sm.load("modelo_reg.pickle")
    #Open the modelo_clasificacion
    modelo_classif = load_model("modelo_clasificacion_xgboost")
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    DataApp
    data_input_df = pd.DataFrame({"KmDist" : [float(0.14)], 
                                    "INDICADOR_GAS_NATURAL" : [float(0.02)], 
                                    "INDICADOR_INTERNET" : [float(34)]})
    prediction = predict_model(DataApp.modelo_classif, data = data_input_df)

    print(type(prediction))
    print(float(prediction["Label"].values[0]))

