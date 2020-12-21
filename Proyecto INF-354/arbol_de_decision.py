# -*- coding: utf-8 -*-
"""Arbol de decision.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sUE4le8QbrJm_teXFI0Y0G0vAReJ_Hen

#Arbol de decision

###Importacion de librerias y dataset
"""

#Importando librerias
import pandas as pd

#Importamos el dataset
dataset = pd.read_csv('bolivia_covid19_cases_daily.csv')
#Preprocesamiento - Eliminamos las filas con valores nulos
dataset.dropna(axis=0, inplace=True) # para columnas se utiliza axis = 1, inplace =  efectuar cambios
print(dataset.tail(5))

"""###Seleccion de datos para entrenamiento
x = "recuperados"     ;      y = "poblacion"
"""

#Seleccion de columnas
x = dataset.iloc[:,[3,4]].values
y = dataset.iloc[:,5].values
#print(x)
#print(y)

#Divicion del conjunto de datos para entrenamiento y pruebas
from sklearn.model_selection import train_test_split
#con el 50% de datos que se usaran para la prueba y el restante para entrenamiento
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
#print(y_train)

"""#Preprocesamiento
Escalamiento estandar - Regresion logistica

"""

#Escalamiento estandard
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()
x_train = escalar.fit_transform(x_train)
print(x_train)
x_test = escalar.fit_transform(x_test)
print(x_test)

"""#Pruebas
Regresion logistica y su matriz de confusion

Permite estimar la probabilidad de una variable cualitativa binaria en función de una variable cuantitativa
"""

#Regresion logistica - para clasificacion
from sklearn.linear_model import LogisticRegression
clasificador = LogisticRegression(random_state = 0) #random fija una semilla para generar nros aleatorios
#Entrenamos el modelo
clasificador.fit(x_train, y_train)

#Se predice y se guarda los dagtos
y_pred = clasificador.predict(x_test)
#Obtener score del entrenamiento
score = clasificador.score(x_test, y_test)
print("Regresion Logistica :",score)

#Matriz de confusion fila=prediccion columna= actual
from sklearn.metrics import confusion_matrix
#le damos los datos de prueba y los que predijo con anterioridad
matriz = confusion_matrix(y_test, y_pred)
print(matriz)

"""Arbol de decision y su Matriz de confusion"""

from sklearn.tree import DecisionTreeClassifier
#Utilizamos el criterio = 0 ya que no deseamos impurezas, pues pertenecen a la misma clase
clasificador2 = DecisionTreeClassifier(criterion = 'entropy', random_state= 0)

#Se entrena el modelo
clasificador2.fit(x_train, y_train)

#Se predice y se guarda los datos
y_pred_tree = clasificador2.predict(x_test) 
print(y_pred_tree[:20])
print(y_test[:20])
#Generamos otra matriz de confusion para verificar el nro de aciertos
matriz2 = confusion_matrix(y_test, y_pred_tree)
print(matriz2)

#El escore obtenido
score2 = clasificador2.score(x_test, y_test)
print("Arbol de decision :",score2)