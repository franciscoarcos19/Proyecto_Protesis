import itertools
import time
from bbb_pru_adc import capture

R0 = open("registro0.txt","w+")
R1 = open("registro1.txt","w+")
R2 = open("registro2.txt","w+")
R3 = open("registro3.txt","w+")

with capture.capture([0,1,2,3], clk_div=1, target_delay=200000, auto_install=True) as c:
    num_values = 0
    start = time.time()
    for num_dropped, _, values in itertools.islice(c, 0, 1000):
        print(num_dropped, _[0])
        num_values += num_dropped + len(values)
        count = 0
        for k in range(len(values)):
            dato = str(values[k])
            if count == 0:
                R0.write(dato + '\r\n')
            if count == 1:
                R1.write(dato + '\r\n')
            if count == 2:
                R2.write(dato + '\r\n')
            if count == 3:
                R3.write(dato + '\r\n')
            count = count + 1
            if count == 4:
                count = 0

    end = time.time()

freq = (num_values / (end - start))/4
print('Frecuencia: ', freq)
print('Cantidad de datos', num_values)
