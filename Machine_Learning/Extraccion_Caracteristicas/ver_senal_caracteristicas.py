# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:36:31 2021

@author: Francisco Arcos
Este código permite visualizar la señal y las características ya generadas
"""

import numpy as np
from numpy import array, r_
import matplotlib.pyplot as plt
from caracteristicas import *

sensor1 = np.loadtxt('C1.txt')
sensor2 = np.loadtxt('C2.txt')
sensor3 = np.loadtxt('C3.txt')
sensor4 = np.loadtxt('C4.txt')
tiempo = np.arange(0,65.000,0.001)

plt.figure()
plt.title('M1 S2')
plt.plot(tiempo,sensor1, label='Deltoides')
plt.plot(tiempo,sensor2, label='Biceps')
plt.plot(tiempo,sensor3, label='Triceps')
plt.plot(tiempo,sensor4, label='Braquial')
plt.grid()
plt.legend();

caracteristica_AAC = np.load('AAC.npy')
caracteristica_DASDV = np.load('DASDV.npy')
caracteristica_LOG = np.load('LOG.npy')
caracteristica_MAV = np.load('MAV.npy')
caracteristica_SSI = np.load('SSI.npy')
caracteristica_WL = np.load('WL.npy')
caracteristica_RMS = np.load('RMS.npy')

num_datos = 600
tiempo_ca = np.linspace(0,60,num_datos)

# Las características son: AAC, DASDV, LOG, MAV, SSI, WL y RMS. Cambie por la que desee graficar

#AAC******************************************************************************************
caracteristica_deltoides = caracteristica_AAC[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_AAC[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_AAC[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_AAC[:,3]#característica de sensor en tendón triceps braquial    

plt.figure()
plt.title('Característica AAC para M1 S2')
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
plt.title('Característica DASDV para M1 S2')
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
plt.title('Característica LOG para M1 S2')
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
plt.title('Característica MAV para M1 S2')
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
plt.title('Característica SSI para M1 S2')
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
plt.title('Característica WL para M1 S2')
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
plt.title('Característica RMS para M1 S2')
plt.plot(tiempo_ca,caracteristica_deltoides, label='Deltoides')
plt.plot(tiempo_ca,caracteristica_biceps, label='Biceps')
plt.plot(tiempo_ca,caracteristica_triceps, label='Triceps')
plt.plot(tiempo_ca,caracteristica_braquial, label='Braquial')
plt.grid()
plt.legend();
#************************************************************************************************


