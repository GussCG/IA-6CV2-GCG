
# Autor: Cerda García Gustavo
# Practica 9: Métodos de Validación (10-Fold Cross Validation IRIS)

# Programa que divide un dataset en 10 subconjuntos de acuerdo a un porcentaje
# Se divide el dataset IRIS en 10 subconjuntos

# Librerias
import numpy as np
import pandas as pd #Libreria para manejo de datos
from sklearn.model_selection import StratifiedKFold #Libreria para dividir un dataset en 10 subconjuntos

# Cargamos el dataset IRIS
df = pd.read_csv('iris.csv', header=None)

# Nombre: 10_fold_cross_validation
# Desc: Divide un dataset en 10 subconjuntos de acuerdo a un porcentaje
# Entrada:
#  - X: DataFrame con los datos
#  - y: DataFrame con las etiquetas
# Salida:
#  - X_train: DataFrame con los datos de entrenamiento
#  - X_test: DataFrame con los datos de prueba
#  - y_train: DataFrame con las etiquetas de entrenamiento
#  - y_test: DataFrame con las etiquetas de prueba
def fold_cross_validation(X,y,modelo):
    # Inicializa el generador de los 10 subconjuntos
    skf = StratifiedKFold(n_splits=10)

    # Inicializa las listas para guardar los resultados
    resultados = []

    # Itera sobre los 10 subconjuntos
    for train_index, test_index in skf.split(X, y):
        # Divide los datos en entrenamiento y prueba
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Entrena el modelo
        modelo.fit(X_train, y_train)

        # Evalua el modelo
        score = modelo.score(X_test, y_test)
        resultados.append(score)

    return resultados

# X y Y
# Todas menos la ultima columna
X = df[df.columns[:-1]]
# La ultima columna
Y = df[df.columns[-1]]

# Modelo
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier()

resultados = fold_cross_validation(X,Y,modelo)

print("Resultados de 10-Fold Cross Validation IRIS")
print(resultados)
