
# Autor: Gustavo Cerda García
# Practica 4
# Ejericio 2. Simulated Annealing - Funciones

# Programa que implementa el algoritmo de Simulated Annealing para encontrar el mínimo de una función.

# Librerías
import math # Para la función exponencial
import random # Para generar números aleatorios

# Funciones a minimizar
# Función 1: f(x) = x^4 + 3x^3 + 2x^2 - 1
def f1(x):
    return x**4 + 3*x**3 + 2*x**2 - 1

# Función 2: f(x) = x^2 - 3x - 8
def f2(x):
    return x**2 - 3*x - 8

# Función para encontrar el mínimo de una función utilizando Simulated Annealing
# Entrada:
#   - funcion (Función): Función a minimizar
#   - temperatura_inicial (float): Temperatura inicial
#   - temperatura_final (float): Temperatura final
#   - alpha (float): Factor de reducción de la temperatura
#   - iteraciones_por_temp (int): Número de iteraciones por temperatura
# Salida:
#   - x (float): Valor de x que minimiza la función
def simulated_annealing(funcion, temperatura_inicial, temperatura_final, alpha, iteraciones_por_temp):
    # Punto de partida aleatorio
    x_actual = random.uniform(-10, 10)
    mejor_x = x_actual # Mejor valor encontrado
    mejor_valor = funcion(x_actual) # Valor de la función en el mejor valor encontrado

    # Temperatura inicial
    temperatura = temperatura_inicial

    # Bucle principal
    # Mientras la temperatura sea mayor que la final
    while temperatura > temperatura_final:
        # Iteraciones por temperatura
        for _ in range(iteraciones_por_temp):
            # Generar un nuevo punto cercano al actual
            nuevo_x = x_actual + random.uniform(-0.5, 0.5)

            # Calcular diferencias de valores
            delta_valor = funcion(nuevo_x) - funcion(x_actual)

            # Decidir si se acepta el nuevo punto
            # Si el nuevo punto tiene un valor menor o se acepta con una probabilidad dada por la temperatura
            if delta_valor < 0 or random.random() < math.exp(-delta_valor / temperatura):
                x_actual = nuevo_x

                # Actualizar el mejor valor encontrado
                if funcion(x_actual) < mejor_valor:
                    mejor_x = x_actual
                    mejor_valor = funcion(x_actual)

        # Reducir la temperatura
        temperatura *= alpha

    return mejor_x, mejor_valor

if __name__ == "__main__":
    temperatura_inicial = 1000 
    temperatura_final = 1
    alpha = 0.95 # Factor de reducción de la temperatura
    iteraciones_por_temp = 100 # Número de iteraciones por temperatura

    print("Encontrar mínimo de f(x) = x^4 + 3x^3 + 2x^2 - 1:")
    min_x1, min_valor1 = simulated_annealing(f1, temperatura_inicial, temperatura_final, alpha, iteraciones_por_temp)
    print("x =", min_x1)
    print("Valor mínimo =", min_valor1)

    print("\nEncontrar mínimo de f(x) = x^2 - 3x - 8:")
    min_x2, min_valor2 = simulated_annealing(f2, temperatura_inicial, temperatura_final, alpha, iteraciones_por_temp)
    print("x =", min_x2)
    print("Valor mínimo =", min_valor2)
