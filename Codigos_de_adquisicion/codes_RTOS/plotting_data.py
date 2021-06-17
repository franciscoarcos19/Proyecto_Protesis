import numpy as np
import matplotlib.pyplot as plt

valores_sensor_A = open('registro_A.txt','r')
valores_sensor_B = open('registro_B.txt','r')
valores_sensor_C = open('registro_C.txt','r')
valores_sensor_D = open('registro_D.txt','r')

#valores_sensor_A = open('registro0.txt','r')
#valores_sensor_B = open('registro1.txt','r')
#valores_sensor_C = open('registro2.txt','r')
#valores_sensor_D = open('registro3.txt','r')

datos_A = []
for line in valores_sensor_A:
    if line.strip():
        #n = int(line)
        n = float(line)
        datos_A.append(n)

print(datos_A)

datos_B = []
for line in valores_sensor_B:
    if line.strip():
        #n = int(line)
        n = float(line)
        datos_B.append(n)

print(datos_B)

datos_C = []
for line in valores_sensor_C:
    if line.strip():
        #n = int(line)
        n = float(line)
        datos_C.append(n)

print(datos_C)

datos_D = []
for line in valores_sensor_D:
    if line.strip():
        #n = int(line)
        n = float(line)
        datos_D.append(n)

print(datos_D)

print("Datos sensor A ", len(datos_A))
print("Datos sensor B ", len(datos_B))
print("Datos sensor C ", len(datos_C))
print("Datos sensor D ", len(datos_D))

plt.title('Values for 4 Sensors')
plt.ylim((-1,1200))
plt.ylabel('Values')
plt.xlabel('Muestra')

#vector_tiempo = np.linspace(0,len(datos_A)*0.02,len(datos_A)) #0.02 hace referencia al periodo de muestreo
#vector_tiempo = np.linspace(0,len(datos_A)*0.0033,len(datos_A)) #0.0033 hace referencia al periodo de muestreo
#vector_tiempo = np.arange(0,410,1)
vector_tiempo = np.arange(0,len(datos_A),1)
#print(len(vector_tiempo))
plt.plot(vector_tiempo,datos_A,'-b')
plt.plot(vector_tiempo,datos_B,'-r')
plt.plot(vector_tiempo,datos_C,'-k')
plt.plot(vector_tiempo,datos_D,'-g')

#plt.plot(datos_A)
#plt.plot(datos_B)
#plt.plot(datos_C)
#plt.plot(datos_D)

plt.grid()
plt.show()