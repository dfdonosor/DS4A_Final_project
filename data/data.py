import os
print("data.py", os.getcwd())
import pandas as pd
from pycaret.classification import *
import statsmodels.api as sm

#Open the consolodida_datos
df = pd.read_pickle("..\data\consolidado_datos.pickle")
#Open the modelo_reg
modelo_reg = sm.load("..\data\modelo_reg.pickle")
#Open the modelo_clasificacion
modelo_classif = load_model("..\data\modelo_clasificacion_xgboost")
