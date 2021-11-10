# -*- coding: utf-8 -*-
"""PruebaKiko.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uK61MayhdePhaEiWyPr6EK59bVzlln9R
"""

from google.colab import files
files.upload()

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

X = pd.read_csv("caracteristicas_mav_aac.csv", sep=";", header = None)
X.columns=["f1","f2","f3","f4","f5","f6","f7","f8"]
X.head(2)

Y = pd.read_csv("clase_identificada.csv", header = None)
Y.columns=["output"]
Y["output"] = pd.to_numeric(Y["output"])
Y.head(2)

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

df = pd.concat([X, Y], axis=1)
df.head(2)

training_data, testing_data = train_test_split(df, test_size=0.2, random_state=25)

model = keras.Sequential([
    keras.layers.Dense(8, activation = 'relu'),
    keras.layers.Dense(32, activation = 'relu'),
    keras.layers.Dense(7, activation = 'softmax')
])

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=["accuracy"])

history = model.fit(training_data[["f1","f2","f3","f4","f5","f6","f7","f8"]],training_data[["output"]], epochs = 5000)

print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

predictions = model.predict(testing_data[["f1","f2","f3","f4","f5","f6","f7","f8"]])

mov = [np.argmax(predictions[i]) for i in range(len(testing_data["output"]))]
true_false = mov == testing_data["output"]

sum(true_false)/len(testing_data["output"])

predictions = model.predict(X[:4])
predictions

