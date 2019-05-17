
# Usados en este programa
import pandas as pd
import datetime
import numpy as np
from sklearn.metrics import r2_score

# Extraigo Información de Yahoo
import fix_yahoo_finance as yf 

# Paralelización 

# DASK
import dask as dask
from dask.distributed import Client, progress
import dask.dataframe as dd

client = Client()
client.cluster

from dask import delayed


# moment: 'a' = Apertura, 'c'= Cierre, 'h'=máximo, 'l'=mínimo
@delayed
def fin_poly_reg(it,investment_length, years_back, future_code, moment, r2_min):
    
    # Tiempo que dura la inversión
    
    il = investment_length
    
    now = datetime.datetime.now()
    a_t = str(now)[0:10]
    b_t = str(int(str(now)[0:4])-years_back)+str(now)[4:10]
    
    sys.stdout = open(os.devnull, "w")
    yahoo = yf.download(future_code,b_t,a_t)
    sys.stdout = sys.__stdout__
    
    
    deg = [1,2,3,4,5,6,7,8,9]
    
    if moment == 'a':
    
        # Apertura
        
        X = yahoo.iloc[:,0]
        
        # Desviación estándar
        
        sd =np.std(X)
        
        # Valor al ultimo día del stock 
        
        vu = X[-1]
        
        # Regresión polinomial 
        
        for grad in deg:
                                          
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
    if moment == 'c':
        
        # Cierre 
        
        X = yahoo.iloc[:,3]
        
        # Desviación estándar
        
        sd =np.std(X)
        
        # Valor al ultimo día del stock 
        
        vu = X[-1]
        
        # Regresión polinomial 
        
        for grad in deg:
        
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
        
        
    if moment == 'h':
    
        # High
        
        X = yahoo.iloc[:,1]
        
        # Desviación estándar
        
        sd =np.std(X)
        
        # Valor al ultimo día del stock 
        
        vu = X[-1]
        
        # Regresión polinomial 
        
        for grad in deg:  
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
        
    if moment == 'l':
   
        # Low
        
        X = yahoo.iloc[:,2]

        # Desviación estándar
        
        sd =np.std(X)
        
        # Valor al ultimo día del stock 
        
        vu = X[-1]
        
        # Regresión polinomial         
        
        for grad in deg:
        
            
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
    if r2 < r2_min:
        
        # Probablemente sea más util eliminar esta advertencia
        print('ADVERTENCIA : r2 no alcanzó el mínimo, 10 bethas por default')
      
    nl= '\n'
    
    
    # Send to txt 
    
        #Betas 
    vec=''   
    for i in range(len(z)):
        vec = vec+str(z[i])+nl
    
        # 
        
    with open('triplef_'+str(it)+'.txt', 'w') as the_file:
        the_file.write(str(str(sd)+nl+str(vu)+nl+str(il)+nl+vec))
        the_file.close()
    
    
    return None
    

uno = fin_poly_reg(it=1,investment_length=10, years_back=3, future_code="NG=F", moment='a', r2_min=0.5)

### FORMATO DE DATOS GUARDADOS EN TXT

# sd
#valor al último día del stock
#tiempo que dura la inversión
#betas



"""
Descargo toda la información de yahoo al mismo tiempo 
"""

def 





"""
GRAFICA DE COMPROBACIÓN DE REGRESIÓN


plot('xlabel', 'ylabel', data=X)
    
import matplotlib.pyplot as plt

def f(t,z):
    return z[0]+z[1]*t+z[2]*t**2+z[3]*t**3

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1,z), 'bo', t2, f(t2,z), 'k')
"""   