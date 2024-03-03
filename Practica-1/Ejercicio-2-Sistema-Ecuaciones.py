
#Autor: Gustavo Cerda García
#Ejericio 2. Sistema de ecuaciones lineales

#Programa que resuelve un sistema de ecuaciones lineales de 4x4 
#Lo resuelve de forma "Tonta" ya que los valores de las variables
#Son generados aleatoriamente y no se garantiza que el sistema tenga solución
#Además, el error se calcula con respecto a un valor de solución que se conoce

#Librerias
import random
from math import sqrt

#Variables globales
#vec_sol: Arreglo que representa la solución del sistema
#Nos sirve para calcular que tan cerca estamos de la solución
vec_sol = [56/17,-80/17,-148/17,-1396/17]

#Nombre: resuelveSistema
#Descripción: Resuelve un sistema de ecuaciones lineales de 4x4
#Entradas:
#Salidas: x, y, z, w
def resolverSistema():
    #Primero se generan los valores de las variables
    #Son numeros aleatorios enteros entre -100 y 100
    B = random.randint(-100, 100)
    D = random.randint(-100, 100)
    E = random.randint(-100, 100)
    F = random.randint(-100, 100)

    #Se calcula el error
    #Se utiliza la distancia euclidiana
    error = sqrt((B-vec_sol[0])**2 + (D-vec_sol[1])**2 + (E-vec_sol[2])**2 + (F-vec_sol[3])**2)

    #Se regresa el valor de las variables y el error
    return B, D, E, F, error

#Nombre: main
#Se imprimen los valores de las variables y el error
B, D, E, F, error = resolverSistema()

print("B = ", B)
print("D = ", D)
print("E = ", E)
print("F = ", F)
print("Error = ", error)

