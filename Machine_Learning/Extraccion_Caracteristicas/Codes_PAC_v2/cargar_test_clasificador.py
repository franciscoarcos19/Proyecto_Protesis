import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.metrics import classification_report

#cargar datos y organizar la matriz X y el vector de etiquetas y
f = open('data.pickle', 'rb')
dic_data = pickle.load(f)
f.close()    

keys = dic_data.keys()
X = []
y = []
i = 0
for key in keys:
    X.append(dic_data[key])
    n_vec = dic_data[key].shape[0]
    y.append(np.ones(n_vec)*i)
    i=i+1
X= np.vstack(X)
y=np.hstack(y).astype(int)
print(f'[INFO] Data loaded: X  {X.shape}, y  {y.shape}')

###### separar train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42,shuffle=True)

scaler = Normalizer()
scaler.fit(X_train)
X_train1 = scaler.transform(X_train)
X_test1 = scaler.transform(X_test)

loaded_model = pickle.load(open('DTCPickle_file', 'rb'))
y_pred = loaded_model.predict(X_test1)

#para probar solamente
#esta ejemplo aplica solamente para una característica "MAV"
#datos_caracteristicas = np.array([[0.8, 0.5, 0.7, 0.4]]) 
#prueba_datos = loaded_model.predict(datos_caracteristicas)

acc = np.sum(y_pred == y_test)/y_test.size*100
print(f'[INFO] Accuracy = {acc}')


target_names = list(keys)
print(classification_report(y_test, y_pred, target_names=target_names))
