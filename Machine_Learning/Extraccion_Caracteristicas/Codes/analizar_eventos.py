import numpy as np
from caracteristicas import *

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

