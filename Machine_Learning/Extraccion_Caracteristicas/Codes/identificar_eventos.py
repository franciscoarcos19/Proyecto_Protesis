import numpy as np

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
