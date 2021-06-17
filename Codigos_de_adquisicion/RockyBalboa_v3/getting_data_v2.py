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

    muestras = 100 #datos vistos en tiempo real
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
    lecturas=1000 #datos guardados en registros
    registro1=[]
    registro2=[]
    registro3=[]
    registro4=[]
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

            #drawnow(plotValues)

            registro1.append(a)
            registro2.append(b)
            registro3.append(c)
            registro4.append(d)

            #i = i + 1
            print('Iteración ', i)
        except:
            print('Lectura no valida')

    tiempo_final = time.time()
    print("el tiempo transcurrido fue: ", tiempo_final - tiempo_inicio, " segundos")

    registro1 = registro1[4:len(registro1)]
    registro2 = registro2[4:len(registro2)]
    registro3 = registro3[4:len(registro3)]
    registro4 = registro4[4:len(registro4)]

    f_A = open("registro_A.txt", "w+")
    for k in range(len(registro1)):
        dato = str(registro1[k])
        f_A.write(dato + '\n')

    f_B = open("registro_B.txt", "w+")
    for k in range(len(registro2)):
        dato = str(registro2[k])
        f_B.write(dato + '\n')

    f_C = open("registro_C.txt", "w+")
    for k in range(len(registro3)):
        dato = str(registro3[k])
        f_C.write(dato + '\n')

    f_D = open("registro_D.txt", "w+")
    for k in range(len(registro4)):
        dato = str(registro4[k])
        f_D.write(dato + '\n')

#serialArduino = serial.Serial('/dev/ttyACM0', 9600)
plt.ion()
serialArduino = serial.Serial('COM7', 9600)
hilo = threading.Thread(target = capturar())