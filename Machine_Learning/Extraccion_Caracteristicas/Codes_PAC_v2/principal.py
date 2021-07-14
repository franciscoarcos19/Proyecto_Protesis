import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from scipy.signal import lfilter, resample, firwin, hilbert
from scipy.fftpack import fft, dct
import math
import pickle
import statistics as stats
import librosa

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
            long_segment.append(np.arange(ini-5,fin+5))
            ini=ind_ini[i]
      
    long_segment.append(np.arange(ini,ind_fin[-1]))

    #retornar los segmentos depurados
    return long_segment     
#
#############################################################
#############################################################
######### funcion para analizar los eventos de cada sesion
def analizar_segmentos(set_signal,fs=1000,min_duration=0.1,len_window=300):   
    fs = fs
    sessions = set_signal.keys()
    print('[INFO] proceso de extraer caracteristicas a cada evento sesion: ')
    FEATS = []
    for session in sessions:
        print(f'{session}')
        #data contiene la info de los 4 sensores en una matriz 4xT
        #sementos son los segmentos activos en la session
        data      = set_signal[session][0]
        segmentos = set_signal[session][1]

        #aislar la informacion de un segmento con sus 4 sensores
        for segmento in segmentos:
            chunk_data = data[:,segmento]
            if segmento.size/fs >  min_duration:
               #print("Duracion: ",segmento.size/fs)
               #tomar la senal de cada sensor para extraer caracteristicas
               feats_seg = []
               for sensor in chunk_data:
                   #### en esta parte se incluye el proceso de extraer caracteristicas
                   x = extr_caracteristicas(sensor,len_window)
                   feats_seg.append(x)
                   
                   ######
               #es necesario agregar las caracteristicas de forma horizontal     
               feats_seg=np.hstack(feats_seg)
               
               FEATS.append(feats_seg)
               
    #unir todas las caracteristicas de todos los segmentos en una sola matriz    
    FEATS = np.vstack(FEATS)

    return FEATS

#################
#a esta funcion llega un segmento y se extran caracteristicas cada 100 ms, se agrupan en una matriz y se retorna 
def extr_caracteristicas(s,len_window,sr=1000,n_fft=512):
    #banco de filtros 
    fil_bank=librosa.filters.mel(sr=sr, n_fft = n_fft-1, n_mels = 20);    #nuevo de Milton
    ini = 0
    fin = len_window
    x = []
    while fin < s.size:
        y = s[ini:fin]
        n = len(y)-1
        
        #######################################FRECUENCIA###################
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
        
        #Solamente para graficar como prueba
        #plt.plot(Ydb)
        #plt.show()
        
        #NUEVA CARACTERISTICA EN FRECUENCIA DE MILTON
        #por ejemplo calcular la FFT
        Y = fft(y,n=n_fft)
        # Calcular magnitud, normalizar por el num de muestras
        absY = abs(Y)/(y.size)                                      
        #reorganizar el espectro para graficar
        #numero de mxuestras hasta la mitad del espectro
        hN=int(math.floor((Y.size+1)/2))
        absY=2*absY[0:hN]
        # calcular la magnitud en dB
        # Si hay ceros, reemplazar por un valor muy pequeno, antes de aplicar el log
        absY[absY < np.finfo(float).eps] = np.finfo(float).eps    
        Ydb = 20 * np.log10(absY)
        #agrupar espectro por bandas
        fbank_e = np.dot(fil_bank, absY)
        #aplicar log
        log_fbank =  np.log10(fbank_e)
        #aplicar DCT
        ceps = dct(fbank_e,norm='ortho')
        
        
        ###WILLIAM###
        p = []
        vr = []
        suma_Rms = 0
        count_ZC = 0
        thresh_ZC = 0.01
        valor_Willison = 0
        thresh_Willison = 0.01 
        thresh_SC = 0.00003
        count_SC = 0
        suma_WL = 0
        inte = []
        
        ###MIAS###
        sum_aac = 0
        sum_dasdv = 0
        sum_ssi = 0
        sum_wl = 0
        sum_rms = 0
        
        for i in range(n):
            #Mav
            p.append(abs(y[i]))
            #Var
            vr.append(abs(y[i]))
            #Rms
            suma_Rms = suma_Rms + y[i]**2
            #ZeroCrosing
            if ((y[i]>0 and y[i+1]<0) or (y[i]<0 and y[i+1]>0)) and abs(y[i]-y[i+1]) >= thresh_ZC:
                count_ZC += 1
            else:
                count_ZC = count_ZC
            #Willison    
            if (y[i]-y[i+1])>thresh_Willison:
                valor_Willison += 1
            else:
                valor_Willison = valor_Willison  
            #SlopeChange
            if((y[i]-y[i-1])*(y[i]-y[i+1]))>=thresh_SC:
                count_SC += 1
            else:
                count_SC = count_SC
            #WaveLonge
            suma_WL += abs(y[i+1]-y[i])
            #Integral
            inte.append(abs(y[i]))
            
            #aac            
            a_aac = abs(y[i+1] - y[i])
            sum_aac = sum_aac + a_aac
            #dasdv
            a_dasdv = (y[i+1] - y[i])**2
            sum_dasdv = sum_dasdv + a_dasdv
            #ssi
            a_ssi = (y[i])**2
            sum_ssi = sum_ssi + a_ssi
            #wl
            sum_wl = sum_wl + abs(y[i+1] - y[i])    
            #rms     
            sum_rms = sum_rms + (y[i])**2  
              
        
        promedio = stats.mean(p)
        varianza = stats.pvariance(vr)   
        valor_Rms = math.sqrt(suma_Rms/len(y)) 
        integral = sum(inte)
        
        aac = sum_aac/n
        dasdv = np.sqrt(sum_dasdv/(n-1))
        ssi = sum_ssi
        wl = sum_wl
        rms = np.sqrt(sum_rms/n)
        log = np.exp((np.sum(np.log10(abs(y))))/n)
        mav = np.mean(abs(y))
         
        #feat = [promedio, varianza, valor_Rms, count_ZC, valor_Willison, count_SC, suma_WL, integral, np.mean(Ydb), np.std(Ydb), Ydb.max(), Ydb.min(),aac, dasdv, log, mav, ssi, wl, rms]
        
        #feat = [promedio, varianza, valor_Rms, count_ZC, valor_Willison, count_SC, suma_WL, integral, aac, dasdv, log, mav, ssi, wl, rms]
        
        #feat = [np.mean(Ydb), np.std(Ydb), Ydb.max(), Ydb.min()]   
        #feat = [aac, dasdv, log, mav, ssi, wl, rms]
        #feat = [promedio, varianza, valor_Rms, count_ZC, valor_Willison, count_SC, suma_WL, integral]
        #feat = [mav, wl, aac]
        feat = np.hstack([mav])
        
        #feat = ceps
        #feat = np.hstack([ceps])
           
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

folders_class = glob(root_dir+"*/",recursive=True) 

fil_dc = True
alpha  = 0.89

data_per_class = {}
classes = ['M1','M2','M3','M4','M5','M6','M7']
list_sensors = ['C1','C2','C3','C4']
data_per_class = {key: [] for key in classes}

for folder in folders_class:
    clase = folder.split('\\')[1][:2]
    text_files = glob(folder+"**\\*.txt",recursive=True)
    names = []
    #generar los nombres de cada sesion    
    for t_file in text_files:
        names.append(t_file.split('\\')[-1][:8])
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
            data0 = np.loadtxt(data_file)
            if fil_dc:
                data =  lfilter([1,-1], [1, -alpha], data0)
                data[:40] = 0
            else:
                data = data0
                
            env = get_env(data)
            DATA.append(data)
            ENVS.append(env)
        #promedio de envolvente de energia para cada sensor
        ave_env = np.mean(ENVS,axis=0)
        trh =ave_env.mean()*1.1   
        #detectectar sementos de eventos activos       
        if clase == 'M7':
           actv_segment = [np.arange(10,ave_env.size-10)]
        else:
           actv_segment= eventos(ave_env,trh=trh,min_duration=10) 
        #guardar informacion en diccionario
        data_sep[sesion]=[np.array(DATA),actv_segment]
        
        plt.subplot(2,3,i)
        i=i+1
        #mostrar resultados
        seg = np.zeros(ave_env.size)
        actv = np.hstack(actv_segment) #se agrupan en un solo vector
        seg[actv] = 1; 
        
        #plt.plot(data_sep[sesion][0].T)
        #plt.plot(ave_env)
        #plt.plot(seg)
                    
    #plt.show()
    
    #para todas las sesiones de la clase, analizar cada segmento: extraer los vectores de caracteristicas
    X = analizar_segmentos(data_sep,fs=1000,min_duration=2)
    
    #agregar las caracteristicas a la clase correspondiente
    
    data_per_class[clase] = X   
        
 ######## guardar todo en un archivo binario
f = open('data.pickle', 'wb')
pickle.dump(data_per_class, f)
f.close()

#f = open('data.pickle', 'rb')
#unpickled = pickle.load(f)
#f.close()    

