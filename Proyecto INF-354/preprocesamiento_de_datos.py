# -*- coding: utf-8 -*-
"""Preprocesamiento de datos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zk3MaKt4yx_241OrfoBjEgp51UvBkj7l

# Preprocesamiento de datos "Casos diarios de Covid 19 en Bolivia"
"""

"""### Importacion de librerias"""

import pandas as pd
import numpy as np

"""### Lectura del dataset"""

#Utilizando pandas se realiza la lectura
datos = pd.read_csv('bolivia_covid19_cases_daily.csv')
print(datos.tail(5)) #ultimas 10 filas

"""### Eliminacion filas que contengan valores perdidos"""

#conviene eliminar las filas con valores perdidos para no tener que imputar
#Esto es aceptable, pues se tiene un conjunto de datos lo suficientemente grande
datos.dropna(axis=0, inplace=True) # para columnas se utiliza axis = 1, inplace =  efectuar cambios
print(datos.tail(5))

"""### Eliminar filas duplicadas"""

#En conjuntos de valores grandes es recomendable hacerlo
#Verifica si hay filas duplicadas
datos.duplicated()
#Elimina filas duplicadas
datos.drop_duplicates()
datos.dropna(thresh=11)

"""### Describir los datos"""

#Describe los datos media, mediana, etx
datos.describe()

"""### Convertir region a datos numericos"""

#Importamos el modulo LabelEncoder para facilitar el etiquetado
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
#Cse crea una columna con el id region al cual le asigna un numero como identificador unico
#Se preprocesa los valores de la columna region con fit_transform
datos['id region'] = encoder.fit_transform(datos.region.values)
print(datos)

"""### Escalamiento estandar

#### Estandariza los datos eliminando la media tal que su varianza sea 1
Ponemos todas nuestras características en la misma escala para que ninguna esté dominada por otra
(Tiende a llevar la media a 0 y la desviacion estandart a 1)
"""

#Obtenemos los casos recuperados en un array
aux = datos['recuperados']
recuperados_array = np.array(aux).reshape((-1, 1)) #Reformamos en columna
#Importamos la libreria de preprocesamiento
from sklearn import preprocessing
standard_escaler = preprocessing.StandardScaler()
datos['scal_est_recuperados'] = standard_escaler.fit_transform(recuperados_array)
#datos.drop(['standard_scaler'], axis=1, inplace = True) #Elimina una columna
print(datos)
datos.describe()

"""### Normalizacion"""

normalizacion = preprocessing.Normalizer(norm="l2")
datos['normalizer_recuperados'] = normalizacion.fit_transform(recuperados_array)
datos.describe()

