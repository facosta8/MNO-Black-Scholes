from plotly import tools
import plotly.graph_objs as go
import pandas as pd
from datetime import date

#import pandas as pd
#import datetime
#import numpy as np
#from sklearn.metrics import r2_score
#import sys
#import os


# Paralelización 

# DASK
import dask as dask
from dask.distributed import Client, progress
import dask.dataframe as dd

client = Client()
client.cluster

#import quandl
# Abro llave de quandl
#quank = open('./keys/quandl.txt').readline().split(':')[1].strip()
#quandl.ApiConfig.api_key = quank


# Lista de características del portafolio: [meses a predecir, r2_minima, commodities...]

lista_run = ['1','0.0001',"LBMA/GOLD","CHRIS/CME_O1", "CHRIS/CME_LB1"]

# Lista del total de commodities con que se trabaja 

lista_desc = ["LBMA/GOLD","CHRIS/CME_O1","LBMA/SILVER","CHRIS/CME_DA1","CHRIS/CME_LN1",
              "CHRIS/CME_C1", "CHRIS/CME_RR1", "CHRIS/CME_LB1","CHRIS/CME_RB1", "CHRIS/CME_NG1",
              "CHRIS/CME_PL1","CHRIS/CME_S1"]


from regresion import download_info, analisis_p

download_info(lista_desc)

datos2 = analisis_p(lista_run)
