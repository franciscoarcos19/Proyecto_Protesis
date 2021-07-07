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
from caracteristicas_v2 import *
from scipy.signal import lfilter, resample, firwin, hilbert

#para el filtro
fil_dc = True
alpha  = 0.89

# Segmentación ****************************************************************
muestras = 100
# *****************************************************************************

sensor1 = np.loadtxt('C1.txt')
sensor2 = np.loadtxt('C2.txt')
sensor3 = np.loadtxt('C3.txt')
sensor4 = np.loadtxt('C4.txt')

if fil_dc:
    sensor1 =  lfilter([1,-1], [1, -alpha], sensor1)
    sensor1[:40] = 0
    sensor2 =  lfilter([1,-1], [1, -alpha], sensor2)
    sensor2[:40] = 0
    sensor3 =  lfilter([1,-1], [1, -alpha], sensor3)
    sensor3[:40] = 0
    sensor4 =  lfilter([1,-1], [1, -alpha], sensor4)
    sensor4[:40] = 0

tiempo = np.arange(0,65.000,0.001)

plt.figure()
plt.title('M1 S1')
plt.plot(tiempo,sensor1, label='Deltoides')
plt.plot(tiempo,sensor2, label='Biceps')
plt.plot(tiempo,sensor3, label='Triceps')
plt.plot(tiempo,sensor4, label='Braquial')
plt.grid()
plt.legend();
plt.show()

num_datos = int(60000/muestras)

caracteristica_Mav = np.zeros((num_datos, 4), dtype=float)
caracteristica_Var = np.zeros((num_datos,4), dtype=float)
caracteristica_Rms = np.zeros((num_datos,4), dtype=float)
caracteristica_ZeroCrosing = np.zeros((num_datos,4), dtype=float)
caracteristica_Willison = np.zeros((num_datos,4), dtype=float)
caracteristica_SlopeChange = np.zeros((num_datos,4), dtype=float)
caracteristica_WaveLonge = np.zeros((num_datos,4), dtype=float)
caracteristica_Integral = np.zeros((num_datos,4), dtype=float)

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
        caracteristica_Mav[n,i] = Mav(segmento)
        
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_Var[n,i] = Var(segmento)    

    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_Rms[n,i] = Rms(segmento)
    
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_ZeroCrosing[n,i] = ZeroCrosing(segmento)    
    
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_Willison[n,i] = Willison(segmento)      
        
    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_SlopeChange[n,i] = SlopeChange(segmento)          

    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_WaveLonge[n,i] = WaveLonge(segmento)

    for n in range(num_datos):
        limite_inf = n*muestras - muestras 
        limite_sup = muestras*n - 1
        segmento = sensor[r_[limite_inf:limite_sup]]
        caracteristica_Integral[n,i] = Integral(segmento)  

tiempo_ca = np.linspace(0,60,num_datos)

# Las características son: Mav, Var, Rms, ZeroCrosing, Willison, SlopeChange, WaveLonge, Integra

#Mav******************************************************************************************
caracteristica_deltoides = caracteristica_Mav[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_Mav[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_Mav[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_Mav[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica Mav para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#Var******************************************************************************************
caracteristica_deltoides = caracteristica_Var[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_Var[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_Var[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_Var[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica Var para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#Rms******************************************************************************************
caracteristica_deltoides = caracteristica_Rms[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_Rms[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_Rms[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_Rms[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica Rms para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#ZeroCrosing******************************************************************************************
caracteristica_deltoides = caracteristica_ZeroCrosing[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_ZeroCrosing[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_ZeroCrosing[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_ZeroCrosing[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica ZeroCrosing para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#Willison******************************************************************************************
caracteristica_deltoides = caracteristica_Willison[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_Willison[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_Willison[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_Willison[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica Willison para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#SlopeChange******************************************************************************************
caracteristica_deltoides = caracteristica_SlopeChange[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_SlopeChange[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_SlopeChange[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_SlopeChange[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica SlopeChange para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#WaveLOnge******************************************************************************************
caracteristica_deltoides = caracteristica_WaveLonge[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_WaveLonge[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_WaveLonge[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_WaveLonge[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica WaveLonge para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************

#Integral******************************************************************************************
caracteristica_deltoides = caracteristica_Integral[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_Integral[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_Integral[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_Integral[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica Integral para M1 S1')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
plt.show()
#************************************************************************************************
