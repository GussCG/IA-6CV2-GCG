import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Cargamos el dataset FRUIT menos la primera columna
df = pd.read_csv('Top-50-musicality-global.csv', header=None)
# Eliminamos la primera columna
df = df.drop(df.columns[0], axis=1)

# X y Y
# Todas menos la primera columna
X = df[df.columns[1:]]
# La primera columna
Y = df[df.columns[0]]

print("X", X)
print("Y", Y)

# Nombre: hold_out_estratificado
# Desc: Divide un dataset en dos subconjuntos de acuerdo a un porcentaje
# Entrada:
#  - X: DataFrame con los datos
#  - y: DataFrame con las etiquetas en STRING
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
print("HOLD OUT 70-30 FRUITS")
print("Datos de entrenamiento")
print(X_train)
print(y_train)
print("Numero de datos de entrenamiento: ", len(X_train))
print()
print("Datos de prueba")
print(X_test)
print(y_test)
print("Numero de datos de prueba: ", len(X_test))
