import itertools
import time
from bbb_pru_adc import capture
import random
import numpy as np
import pickle
from scipy.signal import lfilter
import numpy as np
import math

clasificador = pickle.load(open('DTCPickle_file3', 'rb'))
 
y0_prev = [0]*100
y1_prev = [0]*100
y2_prev = [0]*100
y3_prev = [0]*100
y0 = [0]*100
y1 = [0]*100
y2 = [0]*100
y3 = [0]*100

ii=0
with capture.capture([0,1,2,3], clk_div=1, step_avg=0, max_num = 25, target_delay=190000, auto_install=True) as c:
    num_values=0
    start=time.time()
    minutos=1

    #while True:
     #   ii=ii+1
      #  if (ii%100==0):
       #     print('segundos: ', ii/10, 'lectura: ',ii)
    for ii in range(minutos*10*60):
        for num_dropped, _, values in itertools.islice(c,0,4):
            num_values+=num_dropped + len(values)
            count = 0
            for k in range(len(values)):
                #dato = random.random()
                dato = random.randrange(10)
                #dato = values[k]
                if count==0:
                    y0.insert(0,dato)
                    y0 = y0[0:100]
                if count==1:
                    y1.insert(0,dato)
                    y1 = y1[0:100]
                if count==2:
                    y2.insert(0,dato)
                    y2 = y2[0:100]
                if count==3:
                    y3.insert(0,dato)
                    y3 = y3[0:100]
                count=count+1
                if count==4:
                    count=0

        #capturo 100 datos, y agrego los 100 anteriores, hay un solapamiento del 50%
        #el clasificador trabaja con 200 datos, pero arroja una clasificación cada 100 datos 
        datos_0 = y0_prev + y0
        datos_1 = y1_prev + y1
        datos_2 = y2_prev + y2
        datos_3 = y3_prev + y3

        y0_prev = y0
        y1_prev = y1
        y2_prev = y2
        y3_prev = y3

        #Aplicación del filtro
        vector_y0 = np.array(datos_0)
        vector_y0 = lfilter([1,-1],[1,-0.89], vector_y0)
        vector_y1 = np.array(datos_1)
        vector_y1 = lfilter([1,-1],[1,-0.89], vector_y1)
        vector_y2 = np.array(datos_2)
        vector_y2 = lfilter([1,-1],[1,-0.89], vector_y2)
        vector_y3 = np.array(datos_3)
        vector_y3 = lfilter([1,-1],[1,-0.89], vector_y3)

        #Obtención de característica MAV
        mav_y0 = np.mean(abs(vector_y0))
        mav_y1 = np.mean(abs(vector_y1))
        mav_y2 = np.mean(abs(vector_y2))
        mav_y3 = np.mean(abs(vector_y3))

        #Obtención de característica AAC
        sum_aac_y0 = 0
        sum_aac_y1 = 0
        sum_aac_y2 = 0
        sum_aac_y3 = 0
        for aux in range(99):
            a_aac_y0 = abs(vector_y0[aux+1]-vector_y0[aux])
            sum_aac_y0 = sum_aac_y0 + a_aac_y0
            a_aac_y1 = abs(vector_y1[aux+1]-vector_y1[aux])
            sum_aac_y1 = sum_aac_y1 + a_aac_y1
            a_aac_y2 = abs(vector_y2[aux+1]-vector_y2[aux])
            sum_aac_y2 = sum_aac_y2 + a_aac_y2
            a_aac_y3 = abs(vector_y3[aux+1]-vector_y3[aux])
            sum_aac_y3 = sum_aac_y3 + a_aac_y3

        aac_y0 = sum_aac_y0/100
        aac_y1 = sum_aac_y1/100
        aac_y2 = sum_aac_y2/100
        aac_y3 = sum_aac_y3/100

	#Imprimiendo información
        print('lectura: ', ii)
        #print('elemento agregado ', dato)
        #print(len(vector_y0))
        #Definición del vector de características
        caracteristicas = np.array([[mav_y0, mav_y1, mav_y2, mav_y3, aac_y0, aac_y1, aac_y2, aac_y3]])
        print(caracteristicas)
        #Aplicación del KNN
        print('clase predecida', clasificador.predict(caracteristicas))
        print('###################')
    end = time.time()

#Imprimiendo información
freq = (num_values/(end - start))/4
print('Frecuencia: ', freq)
print('Cantidad de datos', num_values)
print('Cantidad de datos por canal', num_values/4)
print('cantidad de datos en vector', len(vector_y0))
#if (len(y0)==60000):
 #   print('van 60000 datos')

#print(len(y0))