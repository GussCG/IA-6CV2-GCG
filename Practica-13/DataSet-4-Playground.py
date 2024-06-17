import numpy as np # Para generar el dataset
import tensorflow as tf # Para construir el modelo
from tensorflow.keras.models import Sequential # Para construir el modelo
from tensorflow.keras.layers import Dense # Para construir el modelo
import matplotlib.pyplot as plt # Para visualizar el dataset y los resultados

# Generar un dataset de doble espiral
def generate_double_spiral(n_points, noise=0.5):
    n = np.sqrt(np.random.rand(n_points, 1)) * 780 * (2*np.pi) / 360
    d1x = -np.cos(n) * n + np.random.rand(n_points, 1) * noise
    d1y = np.sin(n) * n + np.random.rand(n_points, 1) * noise

    d2x = np.cos(n) * n + np.random.rand(n_points, 1) * noise
    d2y = -np.sin(n) * n + np.random.rand(n_points, 1) * noise

    X = np.vstack((np.hstack((d1x, d1y)), np.hstack((d2x, d2y))))
    y = np.hstack((np.zeros(n_points), np.ones(n_points)))
    return X, y

# Generar el dataset
X, y = generate_double_spiral(200)

# Visualizar el dataset
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='orange', label='Class 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Class 1')
plt.legend()
plt.show()

# Dividir el dataset en conjuntos de entrenamiento y prueba (70/30)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Construir el modelo
model = Sequential([
    Dense(64, activation='tanh', input_shape=(2,)),
    Dense(32, activation='tanh'),
    Dense(16, activation='tanh'),
    Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test))

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.4f}')

# Graficar la precisión y la pérdida
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()
