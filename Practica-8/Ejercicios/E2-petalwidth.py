
# Autor: Cerda García Gustavo
# Practica 8: Clasificador Simple (petalwidth)

# Programa que clasifica una flor en base a la anchura del pétalo
# Se calcula el umbral de separación para las anchuras del pétalo
# Se clasifican las flores de un archivo de pruebas y se calcula el porcentaje de aciertos

# Librerias
import pandas as pd #Libreria para manejo de datos

# Cargar el archivo CSV
datos = pd.read_csv("../Materiales/train.csv")

# Calcular los umbrales de separación para las longitudes del pétalo
umbral_petalwidth = datos["petalwidth"].mean() # Se calcula el promedio de la longitud del pétalo
print("----------------------------------------------------")
print("                     PETALWIDTH                     ")
print("----------------------------------------------------")
print(f"Umbral de separación para la anchura del pétalo: {umbral_petalwidth}")
print("----------------------------------------------------")

# Nombre: clasificador_petalwidth
# Descripción: Clasifica una flor en base a la anchura del pétalo
# Entrada:
#   - petalwidth: anchura del pétalo
# Salida:
#   - Clase a la que pertenece la flor
def clasificador_petalwidth(petalwidth):
    if petalwidth < umbral_petalwidth:
        return "Iris-setosa"
    elif petalwidth < umbral_petalwidth + 0.75:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"
    
# Cargar archivo de pruebas
pruebas = pd.read_csv("../Materiales/test.csv")

# Imprimir tabla con las predicciones (petalwidth - clase real - clase predicha) y contar aciertos
aciertos = 0
print(f"#PRUEBA | PETALWIDTH | CLASE REAL | CLASE PREDICHA")
print("----------------------------------------------------")
for i in range(len(pruebas)):
    petalwidth = pruebas["petalwidth"][i]
    clase_real = pruebas["class"][i]
    clase_predicha = clasificador_petalwidth(petalwidth)
    if clase_real == clase_predicha:
        aciertos += 1
    print(f"  {i}    | {petalwidth} | {clase_real} | {clase_predicha}")

# Calcular el porcentaje de aciertos
porcentaje_aciertos = aciertos / len(pruebas) * 100
print("----------------------------------------------------")
print(f"Aciertos: {aciertos}")
print(f"Porcentaje de aciertos: {porcentaje_aciertos}%")
print("----------------------------------------------------")
