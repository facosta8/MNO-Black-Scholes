
# Usados en este programa
import pandas as pd
import datetime
import numpy as np

# Usados en este programa

from sklearn.metrics import r2_score

# Extraigo Información de Yahoo
import fix_yahoo_finance as yf 


# moment: 'a' = Apertura, 'c'= Cierre, 'h'=máximo, 'l'=mínimo

def fin_poly_reg(years_back, future_code, moment, r2_min):
    
    now = datetime.datetime.now()
    a_t = str(now)[0:10]
    b_t = str(int(str(now)[0:4])-years_back)+str(now)[4:10]
    
    yahoo = yf.download(future_code,b_t,a_t) # Revisar que las fechas
    # coincidan con el rango de los tweets
    
    deg = [1,2,3,4,5,6,7,8,9,10]
    
    if moment == 'a':
    
        # Apertura
        
        for grad in deg:
        
            X = yahoo.iloc[:,0]            
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
    if moment == 'c':
        
        # Cierre 
        
        for grad in deg:
        
            X = yahoo.iloc[:,3]
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
        
        
    if moment == 'h':
    
        # High
        
        for grad in deg:
        
            X = yahoo.iloc[:,1]
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
        
    if moment == 'l':
   
        # Low
        
        
        for grad in deg:
        
            X = yahoo.iloc[:,2]
            
            z = np.polyfit(np.arange(len(X)),X.values,grad)
            
            ypred = np.polyval(z,np.arange(len(X)))
            
            r2 = r2_score(X.values, ypred)
            
            if r2 >= r2_min:
                
                break
    
    if r2 < r2_min:
        
        print('ADVERTENCIA : r2 no alcanzó el mínimo, 6 bethas por default')
        
    return z
    

betas = fin_poly_reg(years_back=3, future_code="GC=F", moment='l', r2_min=0.6)
