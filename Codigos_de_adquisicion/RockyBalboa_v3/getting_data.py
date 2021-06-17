import serial
import threading
import time
from drawnow import *
import matplotlib.pyplot as plt

def capturar():
    datos_sensor1 = []
    datos_sensor2 = []
    datos_sensor3 = []
    datos_sensor4 = []

    muestras = 100
    for i in range(0,muestras):
        datos_sensor1.append(0)
        datos_sensor2.append(0)
        datos_sensor3.append(0)
        datos_sensor4.append(0)

    def plotValues():
        plt.title('Valores Leidos por los Sensores')
        plt.grid(True)
        plt.ylim((-50, 1100))
        plt.ylabel('Valores')
        plt.plot(datos_sensor1, 'b-', label='valores sensor 1')
        plt.plot(datos_sensor2, 'r-', label='valores sensor 2')
        plt.plot(datos_sensor3, 'g-', label='valores sensor 3')
        plt.plot(datos_sensor4, 'y-', label='valores sensor 4')
        plt.legend(loc='upper right')

    i = 0
    lecturas=1000
    tiempo_inicio = time.time()
    for i in range(0, lecturas):
        while(serialArduino.inWaiting()==0):
            pass
        #lectura = serialArduino.readline()
        lectura = serialArduino.readline().strip()
        values = lectura.decode('ascii').split(',')
        try:
            a, b, c, d = [int(s) for s in values]
            print(lectura)
            datos_sensor1.append(a)
            datos_sensor2.append(b)
            datos_sensor3.append(c)
            datos_sensor4.append(d)
            datos_sensor1.pop(0)
            datos_sensor2.pop(0)
            datos_sensor3.pop(0)
            datos_sensor4.pop(0)
            drawnow(plotValues)
            #i = i + 1
            print('Iteración ', i)
        except:
            print('Lectura no valida')

    tiempo_final = time.time()
    print("el tiempo transcurrido fue: ", tiempo_final - tiempo_inicio, " segundos")

    datos_sensor1 = datos_sensor1[4:len(datos_sensor1)]
    datos_sensor2 = datos_sensor2[4:len(datos_sensor2)]
    datos_sensor3 = datos_sensor3[4:len(datos_sensor3)]
    datos_sensor4 = datos_sensor4[4:len(datos_sensor4)]

    f_A = open("registro_A.txt", "w+")
    for k in range(len(datos_sensor1)):
        dato = str(datos_sensor1[k])
        f_A.write(dato + '\n')

    f_B = open("registro_B.txt", "w+")
    for k in range(len(datos_sensor2)):
        dato = str(datos_sensor2[k])
        f_B.write(dato + '\n')

    f_C = open("registro_C.txt", "w+")
    for k in range(len(datos_sensor3)):
        dato = str(datos_sensor3[k])
        f_C.write(dato + '\n')

    f_D = open("registro_D.txt", "w+")
    for k in range(len(datos_sensor4)):
        dato = str(datos_sensor4[k])
        f_D.write(dato + '\n')

#serialArduino = serial.Serial('/dev/ttyACM0', 9600)
plt.ion()
serialArduino = serial.Serial('COM7', 9600)
hilo = threading.Thread(target = capturar())