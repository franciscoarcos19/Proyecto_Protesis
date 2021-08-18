import numpy as np
import pickle

clasificador = pickle.load(open('DTCPickle_file3', 'rb'))
#datos_caracteristicas = np.array([[0.87342854, 0.12012847, 0.39627003, 0.25624559]])
datos_caracteristicas = np.array([[0.00186, 0.011, 0.0045, 0.0019, 1, 1, 1, 1]])
resultado = clasificador.predict(datos_caracteristicas)
print(resultado[0]) 

