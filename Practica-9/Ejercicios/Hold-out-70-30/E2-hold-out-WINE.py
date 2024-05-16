
# Autor: Cerda García Gustavo
# Practica 9: Métodos de Validación (Hold Out 70-30 WINE)

# Programa que divide un dataset en dos subconjuntos de acuerdo a un porcentaje
# Se divide el dataset WINE en 70% entrenamiento y 30% prueba

# Librerias
import numpy as np
import pandas as pd #Libreria para manejo de datos
from sklearn.model_selection import train_test_split #Libreria para dividir un dataset en entrenamiento y prueba

# Leer el archivo
df = pd.read_csv('wine.csv', header=None)

# X y Y
X = df[df.columns[1:]] # Todas las columnas menos la primera
Y = df[df.columns[0]] # La primera columna

print("X\n", X)
print("Y\n", Y)

# Nombre: hold_out_estratificado
# Desc: Divide un dataset en dos subconjuntos de acuerdo a un porcentaje
# Entrada:
#  - X: DataFrame con los datos
#  - y: DataFrame con las etiquetas
# Salida:
#  - X_train: DataFrame con los datos de entrenamiento
#  - X_test: DataFrame con los datos de prueba
#  - y_train: DataFrame con las etiquetas de entrenamiento
#  - y_test: DataFrame con las etiquetas de prueba
def hold_out_estratificado(X, y):
    # Dividir en 70% entrenamiento y 30% prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
    return X_train, X_test, y_train, y_test

# Dividir en 70% entrenamiento y 30% prueba
X_train, X_test, y_train, y_test = hold_out_estratificado(X, Y)
print("HOLD OUT 70-30 WINE")
print("Datos de entrenamiento")
print(X_train)
print(y_train)
print("Numero de datos de entrenamiento: ", len(X_train))
print()
print("Datos de prueba")
print(X_test)
print(y_test)
print("Numero de datos de prueba: ", len(X_test))
print()

