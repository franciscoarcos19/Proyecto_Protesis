import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from scipy.signal import lfilter, resample, firwin, hilbert
from scipy.fftpack import fft
import math
import pickle
import os
from envolvente import *
from identificar_eventos import *
from analizar_eventos import *

###############################################
###############################################
###############################################
#         CODIGO PRINCIPAL ####
###
root_dir = 'data/'
print("root dir es ", root_dir)
folders_class = glob(root_dir+"*/",recursive=True) 
print("folder class es ", folders_class)

fil_dc = True
alpha  = 0.89

data_per_class = {}
classes = ['M1','M2','M3','M4','M5','M6','M7']
list_sensors = ['C1','C2','C3','C4']
data_per_class = {key: [] for key in classes}


for folder in folders_class:
    print("folder es", folder)
    clase = folder.split('\\')[1][:2]#en linux, \\ debe cambiarse por /. son separadores
    text_files = glob(folder+"**\\*.txt",recursive=True)#en linux, \\ debe cambiarse por /
    names = []
    #generar los nombres de cada sesion    
    for t_file in text_files:
        names.append(t_file.split('\\')[-1][:8])#en linux, \\ debe cambiarse por /
    sessions = np.unique(names)
    data_sep = {key: [] for key in sessions}
    
    print(f'\n[INFO] processing {folder} de la clase : {clase}')
    i=1
    #cargar los 4 archivos por sesion y generar una matriz donde cada fila es un sensor
    for sesion in sessions:
        print(f'Session: {sesion}')
        DATA = []
        ENVS = []
        for C in list_sensors:
            data_file = folder + sesion + C + '.txt'
            #print(f'File: {data_file}')
            data = np.loadtxt(data_file)
            if fil_dc:
                data =  lfilter([1,-1], [1, -alpha], data)
                data[:40] = 0
           
            env = get_env(data)#Llamado de función envolvente
            DATA.append(data)
            ENVS.append(env)
        #promedio de envolvente de energia para cada sensor
        ave_env = np.mean(ENVS,axis=0)
        trh =ave_env.mean()*1.1   
        #detectar eventos
        actv_segment= eventos(ave_env,trh=trh,min_duration=10)#Llamado de función para identificar eventos
        segments = np.zeros(ave_env.size)
        actv = np.hstack(actv_segment) #se agrupan en un solo vector
        segments[actv] = 1; 
        
        data_sep[sesion]=np.array(DATA)
        plt.subplot(2,3,i)
        i=i+1
        #mostrar resultados
        plt.plot(data_sep[sesion].T)
        plt.plot(ave_env)
        plt.plot(segments)        
        
    plt.show()
    
    #para todas las sesiones de la clase, analizar cada segmento: extraer los vectores de caracteristicas
    X = analizar_segmentos(actv_segment,data_sep,fs=1000,min_duration=2)
    #agregar las caracteristicas a la clase correspondiente
    
    data_per_class[clase] = X   
        
 ######## guardar todo en un archivo binario
f = open('data.pickle', 'wb')
pickle.dump(data_per_class, f)
f.close()
    
    
