
# Autor: Cerda García Gustavo
# Practica 8: Clasificador Simple (petallength)

# Programa que clasifica una flor en base a la longitud del pétalo
# Se calcula el umbral de separación para las longitudes del pétalo
# Se clasifican las flores de un archivo de pruebas y se calcula el porcentaje de aciertos

# Librerias
import pandas as pd #Libreria para manejo de datos

# Cargar el archivo CSV
datos = pd.read_csv("../Materiales/train.csv")

# Calcular los umbrales de separación para las longitudes del pétalo
umbral_petallength = datos["petallength"].mean() # Se calcula el promedio de la longitud del pétalo
print("----------------------------------------------------")
print("                   PETALLENGTH                      ")
print("----------------------------------------------------")
print(f"Umbral de separación para la longitud del pétalo: {umbral_petallength}")
print("----------------------------------------------------")

# Nombre: clasificador_petallenght
# Descripción: Clasifica una flor en base a la longitud del pétalo
# Entrada:
#   - petallenght: longitud del pétalo
# Salida:
#   - Clase a la que pertenece la flor
def clasificador_petallength(petallength):
    if petallength < umbral_petallength:
        return "Iris-setosa"
    elif petallength < umbral_petallength + 1.5:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"
    
# Cargar archivo de pruebas
pruebas = pd.read_csv("../Materiales/test.csv")

# Imprimir tabla con las predicciones (petallength - clase real - clase predicha) y contar aciertos
aciertos = 0
print(f"#PRUEBA | PETALLENGTH | CLASE REAL | CLASE PREDICHA")
print("----------------------------------------------------")
for i in range(len(pruebas)):
    petallength = pruebas["petallength"][i] # Se obtiene la longitud del pétalo
    clase_real = pruebas["class"][i] # Se obtiene la clase real
    clase_predicha = clasificador_petallength(petallength) # Se obtiene la clase predicha
    if clase_real == clase_predicha:
        aciertos += 1
    print(f"  {i}    | {petallength} | {clase_real} | {clase_predicha}")

# Calcular el porcentaje de aciertos
porcentaje_aciertos = aciertos / len(pruebas) * 100
print("----------------------------------------------------")
print(f"Aciertos: {aciertos}")
print(f"Porcentaje de aciertos: {porcentaje_aciertos}%")
print("----------------------------------------------------")

