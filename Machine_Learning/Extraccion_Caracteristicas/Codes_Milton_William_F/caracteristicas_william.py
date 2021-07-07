# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:24:10 2020

@author: usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:32:17 2020

@author: william Rodriguez
"""


import statistics as stats
import math
from scipy.fftpack import fft
import numpy as np
 ###############  Caracteristicas en funcion del tiempo ##################3
 
###       Valor medio absoluto    ###

def Mav(v):
    
    p=[]
    #print('ventana', ventana)
    for i in range(len(v)):
       p.append(abs(v[i]))
    #Absoluto(ventana)   
    promedio=stats.mean(p)
    return promedio

##      Varianza       ##
def Var(v):
    
    vr=[]
    
    for i in range(len(v)):
        vr.append(abs(v[i]))
    #Absoluto(ventana)     
    varianza=stats.pvariance(vr)
    return varianza

##      Valor RMS    ##    
def Rms(v):
     
    suma=0 
    for i in range(len(v)):
        suma += (v[i]**2)
        
    valor_rms=(math.sqrt(suma/(len(v))))
    return valor_rms
    
### zero crossing  ###
    
def ZeroCrosing(v):
    
    count=0
    thresh = 0.01
    for i in range (len(v)-1):
        if ( (v[i]>0 and v[i+1]<0) or (v[i]<0 and v[i+1]>0) ) and abs(v[i]-v[i+1]) >= thresh :
            count += 1
        else:
            count = count
    
    zc=count
    return zc
    
###  Amplitud  willison WAMP  ###
    
def Willison(v):
     
     valor=0
     thresh=0.01
     for i in range(len(v)-1):
         
         if (v[i]-v[i+1])  > thresh:
             valor += 1
         else:
             valor=valor 
     valor_willison=valor
     return valor_willison
     
###  Cambio de pendiente SSC  ###
     
def SlopeChange(v):
    
    thresh=0.00003
    count=0
    i=1
    for i in range(len(v)-1):
        
        if((v[i]-v[i-1])*(v[i]-v[i+1]))>=thresh:
            count += 1
        else:
            count=count
    slope=count
    return slope
    
###   Longitud de onda Wl   ###
    
def WaveLonge(v):
    
    suma=0
    for i in range(len(v)-1):
        suma += abs(v[i+1]-v[i])
    
    wave=suma
    return wave
    
#### Valor integrado EMG (IEMG) ####
    
def Integral(v):
    
    #Absoluto(v)
    inte=[]
    for i in range(len(v)):
       inte.append(abs(v[i]))
    integral=sum(inte)
    return integral

###############  Caracteristicas en funcion de la frecuencia ############
    
#########        transformada de fourier       ################################3

def FastFurier(muestra, fs):
    
    w=[]
    X =fft(muestra)
    absX = abs(X)
    w=absX[0:len(absX)/2]
    F=np.linspace(0,fs/2,w.size)
    return(w,F)
    
## frecuencia mediana ###
def FMD(PSD,fs):
    espectro, frecuencia= FastFurier(PSD,fs)
    mediana=0
    for i in range(len(espectro)):
        mediana += espectro[i]
    return (mediana/2)

## frecuencia media ###
def MNF(PSD,fs):
    numerador=0
    denominador=0
    espectro, frecuencia= FastFurier(PSD,fs)
    for i in range (len(espectro)):
        numerador += (frecuencia[i]*espectro[i])
        denominador += espectro[i]
    return(numerador/denominador)
    
###  Frecuencia pico  ####
def PKF(PSD,fs):
    espectro, frecuencia= FastFurier(PSD,fs)
    #print(max(abs(espectro))
    return(max(abs(espectro)))
     
        

###  potencia media  ####        
def MNP(PSD,fs):
    mean=0
    espectro, frecuencia= FastFurier(PSD,fs)
    for i in range (len (espectro)):
        mean += (espectro[i]/len(espectro))
    return mean

###  potencia total  ####
def TTP(PSD,fs):
    espectro, frecuencia= FastFurier(PSD,fs)
    return(sum(espectro))
