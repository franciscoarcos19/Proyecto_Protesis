# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:12:36 2021

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Los archivos que se van a cargar de las características están asociados a un movimiento
caracteristica_WL = np.load('WL.npy')
caracteristica_AAC = np.load('AAC.npy')
caracteristica_DASDV = np.load('DASDV.npy')
caracteristica_LOG = np.load('LOG.npy')
caracteristica_MAV = np.load('MAV.npy')
caracteristica_RMS = np.load('RMS.npy')
caracteristica_SSI = np.load('SSI.npy')

# Las características son: AAC, DASDV, LOG, MAV, SSI, WL y RMS. Cambie por la que desee graficar
caracteristica_deltoides = caracteristica_DASDV[:,0]#característica de sensor en deltoides
caracteristica_biceps = caracteristica_DASDV[:,1]#característica de sensor en biceps
caracteristica_triceps = caracteristica_DASDV[:,2]#característica de sensor en triceps
caracteristica_braquial = caracteristica_DASDV[:,3]#característica de sensor en tendón triceps braquial

num_datos = 600
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
