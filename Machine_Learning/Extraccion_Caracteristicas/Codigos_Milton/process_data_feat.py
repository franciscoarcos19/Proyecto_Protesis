import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from scipy.signal import lfilter, resample, firwin, hilbert
from scipy.fftpack import fft
import math
import pickle
import os

##### funcion para calcular envolvente
def get_env(s):
     s_h = hilbert(s)   
     s_en =  np.log10(np.abs(s_h))         
     windowSize = 60;  #30 ms aprox using fs=1khz
     b = (1/windowSize)*np.ones(windowSize);
     a = 1;
     s_en = lfilter(b, a, s_en);
     s_en[0:windowSize+1] =s_en[windowSize+1]
     s_en=(s_en-s_en.min())/np.abs(s_en).max()
     return s_en

######## funcion para identificar eventos candidatos a ser actividad
def eventos(E,trh=0.5,min_duration=10):
    #en caso de que sea una envolvente aplicar umbral, no es necesario si ya es bool
    E = (E > trh).astype(int)
    #agregar ceros al inicio y final para garantizar segmentos cerrados
    E[E.size-2:]=0
    E[:2]=0
    Ed=np.roll(E,1)
    #calcular la derivada    
    O = E-Ed
    #detectar puntos de inicio y final
    ind_ini=np.where(O>0)[0]
    ind_fin=np.where(O<0)[0]
    #descartar los segmentos muy cortos
    length = ind_fin-ind_ini
    ind_ini = ind_ini[length>min_duration]
    ind_fin = ind_fin[length>min_duration]
    #comparar la distancia de elventos adyacentes para unirlos
    dist_ss = ind_ini-np.roll(ind_fin,1) #distancia entre segmentos adyacentes
    max_dist = 500 #aprox 500 ms, si la separacion es mayor son eventos diferentes
    long_segment=[]
    #depurar segmentos
    ini = ind_ini[0]

    for i in range(1, len(dist_ss)):
        if dist_ss[i]>max_dist:
            fin=ind_fin[i-1]
            long_segment.append(np.arange(ini-500,fin+500))
            ini=ind_ini[i]
      
    long_segment.append(np.arange(ini,ind_fin[-1]))

    #retornar los segmentos depurados
    return long_segment     
#
#############################################################
#############################################################
######### funcion para analizar los eventos de cada sesion
def analizar_segmentos(segmentos,set_signal,fs=1000,min_duration=0.1,len_window=100):   
    fs = fs
    sessions = set_signal.keys()
    print('[INFO] proceso de extraer caracteristicas a cada evento')
    FEATS = []
    for session in sessions:
        data = set_signal[session]
        #recorrer la informacion de cada sensor, una fila es una senal
        for signal in data:
            
           #recorrer cada segmento de la senal para extraer caracteristicas
           for segmento in segmentos:
               
               #chunk es un segmento de senal donde se detecto actividad
               chunk_data = signal[segmento]
               #se puede descartar aquellos segementos que tienen una duracion muy corta
               if chunk_data.size/fs >  min_duration:
                    print("Duracion: ",chunk_data.size/fs)
                                        
                    #### en esta parte se incluye el proceso de extraer caracteristicas
                    X = extr_caracteristicas(chunk_data,len_window)
                    
                    FEATS.append(X)
                    #### 
    FEATS = np.vstack(FEATS)

    return FEATS

#################
#a esta funcion llega un segmento y se extran caracteristicas cada 100 ms, se agrupan en una matriz y se retorna 
def extr_caracteristicas(s,len_window):
    ini = 0
    fin = len_window
    x = []
    while fin < s.size:
        y = s[ini:fin]
        #por ejemplo calcular la FFT
        Y = fft(y)
        # Calcular magnitud, normalizar por el num de muestras
        absY = abs(Y)/(y.size)                                      
        #reorganizar el espectro para graficar
        #numero de muestras hasta la mitad del espectro
        hN=int(math.floor((Y.size+1)/2))
        absY=np.hstack((absY[hN:],absY[:hN]))
        #calcular la magnitud en dB
        # Si hay ceros, reemplazar por un valor muy pequeno, antes de aplicar el log
        absY[absY < np.finfo(float).eps] = np.finfo(float).eps    
        Ydb = 20 * np.log10(absY) 

        #calcular 4 valores, por ejemplo (cosas sin sentido): media, desviacion estandar, max y min
        feat = [np.mean(Ydb), np.std(Ydb), Ydb.max(), Ydb.min()]
        #agregar a la matriz de caracteristicas de ese segmento
        x.append(feat)
        
        #avanzar los indices
        ini=fin
        fin = fin + len_window
    x = np.array(x)


    return x
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
            env = get_env(data)
            DATA.append(data)
            ENVS.append(env)
        #promedio de envolvente de energia para cada sensor
        ave_env = np.mean(ENVS,axis=0)
        trh =ave_env.mean()*1.1   
        #detectectar eventos
        actv_segment= eventos(ave_env,trh=trh,min_duration=10) 
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

#f = open('data.pickle', 'rb')
#unpickled = pickle.load(f)
#f.close()    
