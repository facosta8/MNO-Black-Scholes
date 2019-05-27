import pandas as pd
import datetime
import numpy as np
from sklearn.metrics import r2_score
import sys
import os


# Paralelización 

# DASK
import dask as dask
#from dask.distributed import Client, progress
import dask.dataframe as dd

#client = Client()
#client.cluster

from dask import delayed

#os.chdir('git/MNO-Black-Scholes/modelo_simple')


"""

                    ----------------------- ENFOQUE QUANDL -----------------------

"""

import quandl
# Abro llave de quandl
quank = open('quandl.txt').readline().split(':')[1].strip()
quandl.ApiConfig.api_key = quank


# Lista de características del portafolio: [meses a predecir, r2_minima, commodities...]

lista_run = ['1','0.0001',"LBMA/GOLD","CHRIS/CME_O1", "CHRIS/CME_LB1"]

# Lista del total de commodities con que se trabaja 

lista_desc = ["LBMA/GOLD","CHRIS/CME_O1","LBMA/SILVER","CHRIS/CME_DA1","CHRIS/CME_LN1",
              "CHRIS/CME_C1", "CHRIS/CME_RR1", "CHRIS/CME_LB1","CHRIS/CME_RB1", "CHRIS/CME_NG1",
              "CHRIS/CME_PL1","CHRIS/CME_S1"]


# Función de descarga de datos en paralelo  

def download_info(lista_desc):

    @delayed
    def desc_datos(years_back, future_code):
        
        now = datetime.datetime.now()
        a_t = str(now)[0:10]
        b_t = str(int(str(now)[0:4])-years_back)+str(now)[4:10]
        
        sys.stdout = open(os.devnull, "w")
        #yahoo = yf.download(future_code,b_t,a_t)
        yahoo = quandl.get(future_code, collapse="daily",start_date=b_t, end_date=a_t)
    
        sys.stdout = sys.__stdout__
        
        return yahoo.iloc[:,0]
    
    
 
    
    
    to_merge=[]
    for i in range(len(lista_desc)):
         
        
        globals()['data%s'%i] = desc_datos(years_back=3, future_code=lista_desc[i]) #uso 3 años de historia 
        
        to_merge.append(globals()['data%s'%i])
        
    
    @delayed
    def create_variables(to_merge):
        
        variables = pd.concat(to_merge, axis=1)
        return variables
    
    
    intento = create_variables(to_merge)
    datos = intento.compute()
    
    datos.columns = lista_desc
    
    datos.to_csv("datos.csv")
    
    return None 



def analisis_p(lista_run):
    
    # Saco la info de datos.csv de acuerdo al código
    
    info = pd.read_csv("datos.csv")
    
    # Análisis de portafolio 
        
    
    def fin_poly_reg(lista_run,info,investment_length, future_code, r2_min):
        
        # Tiempo que dura la inversión
        
        il = investment_length
        
            
        X = info.loc[:,future_code]
        X = X.dropna()
        # Desviación estándar
        
        sd =np.std(X)
        
        # Valor al ultimo día del stock 
        
        vu = X.tolist()[-1]
        
        # Regresión polinomial 
        
        deg = [1,2,3,4,5,6,7,8,9] # número de bethas posibles 
        
        for j in range(len(deg)):
            
            z = np.polyfit(np.arange(len(X)),X.values,deg[j])
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
        
        
        """
        GUARDO RESULTADOS DE REGRESIÓN EN TXT
            
        El formato dentro del txt es:
        
        sd
        valor al último día del stock
        tiempo que dura la inversión
        betas
        
        """
    
    
        
        nl='\n'
        
            #Betas 
        vec=''   
        for i in range(len(z)):
            vec = vec+str(z[i])+nl
        
            # 
            
        with open('data.txt', 'w') as the_file:
            the_file.write(str(str(sd)+nl+str(vu)+nl+str(il)+nl+vec))
            the_file.close()
        
        """
        CALCULO RENDIMIENTO CON BLACK-SCHOLES Y LEO RESULTADOS
        """
        
        os.system('./programa.o > out.txt')
    
        f = open('out.txt')
        tocayo = f.readlines()
        f.close()
       
        """
        Calculo varianza para ver si las predicciones del tocayo están muy lejos 
        """
        var = np.var(X)
        
        
        sal = [future_code,vu,float(tocayo[0])]
        
        rend = 100*(float(sal[2])-float(sal[1]))/float(sal[1])
        
        return pd.DataFrame({'commodity':[sal[0]],'last_price':[sal[1]],
                             'predicted_price':[sal[2]],'difference(%)':rend,'ts_variance':var,
                             'bethas':[z], 'rango':str(X.min())+'-'+str(X.max())})
    
    
    
    
    
    #uno = fin_poly_reg(info, investment_length=10, future_code='LBMA/GOLD', r2_min=0.5)
    
    # JUNTO TODO 
    
    comodities=[]
    for i in range(len(lista_run)-2):
        i=i+2
        
        globals()['com%s'%i] = fin_poly_reg(lista_run,info,investment_length = float(lista_run[0]),
                                            future_code=lista_run[i], r2_min=float(lista_run[1]))
        
        comodities.append(globals()['com%s'%i])
            
        variables = pd.concat(comodities, axis=0)
    
    return variables 


# Verifica que corra aquí 
prueba = analisis_p(lista_run)

