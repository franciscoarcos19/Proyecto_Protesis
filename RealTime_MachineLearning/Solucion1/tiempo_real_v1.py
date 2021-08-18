import itertools
import time
from bbb_pru_adc import capture
import random
import numpy as np
import pickle

clasificador = pickle.load(open('DTCPickle_file3', 'rb'))

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
                dato = random.random()
                if count==0:
                    y0.append(dato)
                    y0 = y0[1:101]
                if count==1:
                    y1.append(dato)
                    y1 = y1[1:101]
                if count==2:
                    y2.append(dato)
                    y2 = y2[1:101]
                if count==3:
                    y3.append(dato)
                    y3 = y3[1:101]
                count=count+1
                if count==4:
                    count=0

        mean_y0 = sum(y0)/len(y0)
        mean_y1 = sum(y1)/len(y1)
        mean_y2 = sum(y2)/len(y2)
        mean_y3 = sum(y3)/len(y3)
        print('mean y0: ', mean_y0)
        print('mean y1: ', mean_y1)
        print('mean_y2: ', mean_y2)
        print('mean_y3: ', mean_y3)
        print('lectura: ', ii)
        print('elemento agregado ', dato)
        caracteristicas = np.array([[mean_y0, mean_y1, mean_y2, mean_y3, 0, 0, 0, 0]])
        print('clase predecida', clasificador.predict(caracteristicas))
        print('###################')
    end = time.time()

freq = (num_values/(end - start))/4
print('Frecuencia: ', freq)
print('Cantidad de datos', num_values)
print('Cantidad de datos por canal', num_values/4)
print('cantidad de datos en y0', len(y0))
#if (len(y0)==60000):
 #   print('van 60000 datos')

#print(len(y0))
