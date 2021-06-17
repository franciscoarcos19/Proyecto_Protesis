import matplotlib.pyplot as plt

valores_sensor_A = open('registro_A.txt','r')
valores_sensor_B = open('registro_B.txt','r')
valores_sensor_C = open('registro_C.txt','r')
valores_sensor_D = open('registro_D.txt','r')

datos_A = []
for line in valores_sensor_A:
    if line.strip():
        n = int(line)
        datos_A.append(n)

print(datos_A)

datos_B = []
for line in valores_sensor_B:
    if line.strip():
        n = int(line)
        datos_B.append(n)

print(datos_B)

datos_C = []
for line in valores_sensor_C:
    if line.strip():
        n = int(line)
        datos_C.append(n)

print(datos_C)

datos_D = []
for line in valores_sensor_D:
    if line.strip():
        n = int(line)
        datos_D.append(n)

print(datos_D)

print("Datos sensor A ", len(datos_A))
print("Datos sensor B ", len(datos_B))
print("Datos sensor C ", len(datos_C))
print("Datos sensor D ", len(datos_D))

plt.title('Values for 4 Sensors')
plt.ylim((-50,1100))
plt.ylabel('Values')
plt.xlabel('Time')
plt.plot(datos_A)
plt.plot(datos_B)
plt.plot(datos_C)
plt.plot(datos_D)
plt.grid()
plt.show()