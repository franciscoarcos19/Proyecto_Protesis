import numpy as np

datos = np.linspace(0,1,50)
print(datos)    

i = 0
while len(datos>9):
    bufer = datos[0:10]
    mediana = np.mean(bufer)
    desviacion = np.std(bufer)
    maximo = bufer.max()
    minimo = bufer.min()
    print("bufer ",i,bufer)
    print("mediana", mediana)
    print("desviacion", desviacion) 
    print("maximo", maximo)
    print("minimo", minimo)
    datos = np.delete(datos, np.s_[0:10])
    i = i + 1
