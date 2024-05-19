
# Autor: Cerda García Gustavo
# Practica 10: Clasificación Euclidiana (Hold-out y Cross Validation)

# Programa que implementa un clasificador euclidiano y lo evalúa mediante hold-out y cross-validation
# Se utiliza el dataset WINE

# Librerias
import pandas as pd # Libreria para manejo de datos
import numpy as np # Libreria para manejo de arreglos
from sklearn.model_selection import train_test_split, StratifiedGroupKFold # Libreria para dividir un dataset en entrenamiento y prueba
from sklearn.preprocessing import LabelEncoder # Libreria para codificar etiquetas
from scipy.spatial import distance # Libreria para calcular distancias

# Cargamos el dataset
df = pd.read_csv("wine.csv")

# Separamos las características y las etiquetas
# X es el conjunto de características
X = df.iloc[:, 1:].values
# Y es el conjunto de etiquetas (primera columna)
y = df.iloc[:, 0].values

# Codificamos las etiquetas
le = LabelEncoder() 
y = le.fit_transform(y)

# Nombre: euclidean_classifier
# Entradas: 
# - X_train: características de entrenamiento
# - y_train: etiquetas de entrenamiento
# - X_test: características de prueba
# Salidas:
# - y_pred: etiquetas predichas
def euclidean_classifier(X_train, y_train, X_test):
    predictions = [] # Lista para almacenar las predicciones
    # Por cada punto de prueba
    for test_point in X_test:
        distances = distance.cdist([test_point], X_train, 'euclidean') # Calculamos las distancias
        nearest_neighbor = np.argmin(distances) # Obtenemos el índice del vecino más cercano
        predictions.append(y_train[nearest_neighbor]) # Añadimos la etiqueta del vecino más cercano a las predicciones
    return np.array(predictions)

# Nombre: hold_out_validation
# Entradas:
# - X: características
# - y: etiquetas
# Salidas:
# - accuracy: precisión
def hold_out_validation(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify=y) # Dividimos el dataset
    y_pred = euclidean_classifier(X_train, y_train, X_test) # Realizamos las predicciones
    accuracy = np.mean(y_pred == y_test) # Calculamos la precisión
    return accuracy

# Nombre: cross_validation
# Entradas:
# - X: características
# - y: etiquetas
# Salidas:
# - accuracy: precisión
# - std: desviación estándar
def cross_validation(X,y):
    skf = StratifiedGroupKFold(n_splits=10) # Creamos el objeto StratifiedGroupKFold
    accuracies = [] # Lista para almacenar las precisiones
    # Por cada partición
    for train_index, test_index in skf.split(X, y, groups=df.index): 
        X_train, X_test = X[train_index], X[test_index] # Dividimos las características
        y_train, y_test = y[train_index], y[test_index] # Dividimos las etiquetas
        y_pred = euclidean_classifier(X_train, y_train, X_test) # Realizamos las predicciones
        accuracy = np.mean(y_pred == y_test) # Calculamos la precisión
        accuracies.append(accuracy) # Añadimos la precisión a la lista
    return np.mean(accuracies), np.std(accuracies) # Devolvemos la precisión promedio

# Realizamos la validación hold-out
hold_out_accuracy = hold_out_validation(X,y)
print(f"Hold-out validation accuracy: {hold_out_accuracy}")

# Realizamos la validación cruzada
cross_val_accuracy, std = cross_validation(X, y)
print(f"Cross-validation accuracy: {cross_val_accuracy} +/- {std}")

