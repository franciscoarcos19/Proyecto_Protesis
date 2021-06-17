# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:25:09 2021

@author: Francisco Arcos
Código que permite extraer las características de cada movimiento para todos los canales.
Los archivos de texto C1, C2, C3, C4 hacen referencia a las señales mioeléctricas capturadas a través 
de los sensores puestos sobre la persona bajo estudio

Datos que se pueden cambiar:

muestras: corresponde al número de datos con los que se quiere hacer la segmentación, teniendo en cuenta
que la frecuencia de muestreo para capturar los datos fué 1KHz entonces 100 datos corresponde a 0.1seg de señal,
200 datos corresponden a 0.2seg de señal, y así sucesivamente

En las lineas 103-106 puede cambiar la característica que desea graficar
   
"""

import numpy as np
from numpy import array, r_
import matplotlib.pyplot as plt
from caracteristicas import *

# Segmentación ****************************************************************
muestras = 100
# *****************************************************************************

sensor1 = np.loadtxt('C1.txt')
sensor2 = np.loadtxt('C2.txt')
sensor3 = np.loadtxt('C3.txt')
sensor4 = np.loadtxt('C4.txt')
tiempo = np.arange(0,65.000,0.001)

plt.figure()
plt.plot(tiempo,sensor1)
plt.plot(tiempo,sensor2)
plt.plot(tiempo,sensor3)
plt.plot(tiempo,sensor4)
plt.grid()

num_datos = int(60000/muestras)

caracteristica_AAC = np.zeros((num_datos, 4), dtype=float)
caracteristica_DASDV = np.zeros((num_datos,4), dtype=float)
caracteristica_LOG = np.zeros((num_datos,4), dtype=float)
caracteristica_MAV = np.zeros((num_datos,4), dtype=float)
caracteristica_SSI = np.zeros((num_datos,4), dtype=float)
caracteristica_WL = np.zeros((num_datos,4), dtype=float)
caracteristica_RMS = np.zeros((num_datos,4), dtype=float)

for i in range(4):
    if i == 0:
        sensor = sensor1
    elif i == 1:
        sensor = sensor2
    elif i == 2:
        sensor = sensor3
    elif i == 3:
        sensor = sensor4 
    
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_AAC[n,i] = f_aac(segmento)
        
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_DASDV[n,i] = f_dasdv(segmento)    

    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_LOG[n,i] = f_log(segmento)
    
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_MAV[n,i] = f_mav(segmento)    
    
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_SSI[n,i] = f_ssi(segmento)      
        
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_WL[n,i] = f_wl(segmento)          

    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_RMS[n,i] = f_rms(segmento)          
            
# Las características son: AAC, DASDV, LOG, MAV, SSI, WL y RMS. Cambie por la que desee graficar
caracteristica_deltoides = caracteristica_AAC[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_AAC[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_AAC[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_AAC[:,3]#característica de sensor en tendón triceps braquial

tiempo_ca = np.linspace(0,60,num_datos)    
fig, axs = plt.subplots(2,2)
axs[0, 0].stem(tiempo_ca, caracteristica_deltoides)
axs[0, 0].set_title('Característica Deltoides')
axs[0, 1].stem(tiempo_ca, caracteristica_biceps)
axs[0, 1].set_title('Caracteristica Biceps')
axs[1, 0].stem(tiempo_ca, caracteristica_triceps)
axs[1, 0].set_title('Caracterpistica Triceps')
axs[1, 1].stem(tiempo_ca, caracteristica_braquial)
axs[1, 1].set_title('Característica Braquial')

    

    
    