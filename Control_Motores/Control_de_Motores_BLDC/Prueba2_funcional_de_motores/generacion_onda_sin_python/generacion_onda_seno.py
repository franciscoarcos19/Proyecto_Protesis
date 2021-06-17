# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:56:32 2021

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
import math

f = 1
w = 2*math.pi*f
t = np.arange(0,1,0.005)

y = np.zeros(len(t))

for i in range(len(t)):
    y[i] = round(127*math.sin(w*t[i]) + 128,0)
    
onda_seno = np.array(y)

desfase = 68

currentStepA = 1
currentStepB = desfase
currentStepA = desfase*2

coilA = np.zeros(len(onda_seno))
coilB = np.zeros(len(onda_seno))
coilC = np.zeros(len(onda_seno))

for k in range(len(onda_seno)):
    currentStepA = currentStepA + 1; 
    currentStepB = currentStepA + desfase;
    currentStepC = currentStepA + desfase*2;
    
    currentStepA = (currentStepA % len(onda_seno))
    currentStepB = (currentStepB % len(onda_seno))
    currentStepC = (currentStepC % len(onda_seno))

    coilA[k] = onda_seno[currentStepA];
    coilB[k] = onda_seno[currentStepB];
    coilC[k] = onda_seno[currentStepC];
    
plt.plot(coilA)
plt.plot(coilB)
plt.plot(coilC)
plt.xlabel('time')
plt.ylabel('Coil PWM')
plt.show()
    
    

    



