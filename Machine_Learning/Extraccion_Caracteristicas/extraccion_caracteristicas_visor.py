# -*- coding: utf-8 -*-
"""
Código basado en el anterior para extraer características, grandes cambios en visualización

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
plt.title('M1 S1')
plt.plot(tiempo,sensor1, label='Deltoides')
plt.plot(tiempo,sensor2, label='Biceps')
plt.plot(tiempo,sensor3, label='Triceps')
plt.plot(tiempo,sensor4, label='Braquial')
plt.grid()
plt.legend();

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

tiempo_ca = np.linspace(0,60,num_datos)

# Las características son: AAC, DASDV, LOG, MAV, SSI, WL y RMS. Cambie por la que desee graficar

#AAC******************************************************************************************
caracteristica_deltoides = caracteristica_AAC[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_AAC[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_AAC[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_AAC[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica AAC para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#DASDV******************************************************************************************
caracteristica_deltoides = caracteristica_DASDV[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_DASDV[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_DASDV[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_DASDV[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica DASDV para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#LOG******************************************************************************************
caracteristica_deltoides = caracteristica_LOG[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_LOG[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_LOG[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_LOG[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica LOG para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#MAV******************************************************************************************
caracteristica_deltoides = caracteristica_MAV[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_MAV[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_MAV[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_MAV[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica MAV para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#SSI******************************************************************************************
caracteristica_deltoides = caracteristica_SSI[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_SSI[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_SSI[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_SSI[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica SSI para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#WL******************************************************************************************
caracteristica_deltoides = caracteristica_WL[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_WL[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_WL[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_WL[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica WL para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************

#RMS******************************************************************************************
caracteristica_deltoides = caracteristica_RMS[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_RMS[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_RMS[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_RMS[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica RMS para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************
