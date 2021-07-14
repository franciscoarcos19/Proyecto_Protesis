import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier

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
target_names = list(keys)
###### separar train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42,shuffle=True)

plt.plot(X_train)
plt.show()

mu = np.mean(X_train,axis=0)
std = np.std(X_train,axis=0)
#X_train = (X_train - mu)/std
#X_test = (X_test - mu)/std

pca= PCA()
pca.fit(X_train)
plt.plot(pca.explained_variance_ratio_.cumsum())
plt.plot(np.arange(X_train.shape[1]),0.98*np.ones(X_train.shape[1]))
plt.show()

### usar solo las componentes necesarias
pca= PCA(n_components = 30)
pca.fit(X_train)
Xtrain= pca.transform(X_train)
Xtest=pca.transform(X_test)

#crear un clasficador
#clf = LogisticRegression(solver='lbfgs', max_iter=1000,multi_class='ovr')
clf = KNeighborsClassifier(n_neighbors=10)
#clf = RandomForestClassifier(max_depth=2, random_state=0)
#clf = DecisionTreeClassifier(random_state=0)
#entrenar clasificador
clf.fit(Xtrain,y_train)
#evaluar
y_pred=clf.predict(Xtest) 

acc = np.sum(y_pred == y_test)/y_test.size*100
print(f'[INFO] Accuracy = {acc}')


target_names = list(keys)
print(classification_report(y_test, y_pred, target_names=target_names))
