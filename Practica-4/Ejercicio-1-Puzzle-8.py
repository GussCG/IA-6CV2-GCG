
#Autor: Gustavo Cerda García
#Ejericio 1. A* - 8 Puzzle"

#Programa que resuelve el problema del 8-puzzle utilizando el algoritmo de búsqueda A*. La heurística utilizada es la distancia Manhattan. La distancia Manhattan es la suma de las distancias horizontales y verticales de cada número a su posición correcta en el tablero.

#Librerías
import heapq # Para la cola de prioridad
import random # Para generar tableros aleatorios

# Clase para representar un estado del tablero del 8-puzzle
# Atributos:
#   - tablero (Lista): Estado del tablero
#   - movimiento (String): Movimiento que llevó a este estado
#   - costo (int): Costo del estado
#   - padre (Estado): Estado padre
class Estado:
    def __init__(self, tablero, movimiento, costo, padre):
        self.tablero = tablero
        self.movimiento = movimiento
        self.costo = costo
        self.padre = padre

    # Método para comparar dos estados por su costo
    # Se utiliza para la cola de prioridad
    # Entrada:
    #   - other (Estado): Estado a comparar
    # Salida:
    #   - bool: True si el costo de este estado es menor que el costo del otro estado, False en otro caso
    def __lt__(self, other):
        return self.costo < other.costo

# Función para obtener la posición del espacio en blanco en el tablero
# Entrada:
#   - tablero (Lista): Tablero del 8-puzzle
# Salida:
#   - i (int): Fila del espacio en blanco
#   - j (int): Columna del espacio en blanco
def obtener_posicion_espacio(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                return i, j

# Función para generar los movimientos válidos a partir de un estado del tablero
# Entrada:
#   - estado (Estado): Estado actual del tablero
# Salida:
#   - movimientos (Lista): Lista de estados resultantes de los movimientos válidos
def generar_movimientos(estado):
    movimientos = []
    i, j = obtener_posicion_espacio(estado.tablero)

    # Movimientos válidos
    # Arriba, abajo, izquierda, derecha

    # Arriba
    if i > 0:
        nuevo_tablero = [fila[:] for fila in estado.tablero]
        nuevo_tablero[i][j], nuevo_tablero[i - 1][j] = nuevo_tablero[i - 1][j], nuevo_tablero[i][j]
        movimientos.append(Estado(nuevo_tablero, "Arriba", estado.costo + 1, estado))

    # Abajo
    if i < 2:
        nuevo_tablero = [fila[:] for fila in estado.tablero]
        nuevo_tablero[i][j], nuevo_tablero[i + 1][j] = nuevo_tablero[i + 1][j], nuevo_tablero[i][j]
        movimientos.append(Estado(nuevo_tablero, "Abajo", estado.costo + 1, estado))

    # Izquierda
    if j > 0:
        nuevo_tablero = [fila[:] for fila in estado.tablero]
        nuevo_tablero[i][j], nuevo_tablero[i][j - 1] = nuevo_tablero[i][j - 1], nuevo_tablero[i][j]
        movimientos.append(Estado(nuevo_tablero, "Izquierda", estado.costo + 1, estado))

    # Derecha
    if j < 2:
        nuevo_tablero = [fila[:] for fila in estado.tablero]
        nuevo_tablero[i][j], nuevo_tablero[i][j + 1] = nuevo_tablero[i][j + 1], nuevo_tablero[i][j]
        movimientos.append(Estado(nuevo_tablero, "Derecha", estado.costo + 1, estado))

    return movimientos

# Función para calcular la heurística (en este caso, distancia Manhattan)
# Entrada:
#   - tablero_actual (Lista): Tablero actual
#   - tablero_objetivo (Lista): Tablero objetivo
# Salida:
#   - distancia (int): Distancia Manhattan
def heuristica(tablero_actual, tablero_objetivo):
    distancia = 0
    for i in range(3):
        for j in range(3):
            if tablero_actual[i][j] != tablero_objetivo[i][j] and tablero_actual[i][j] != 0:
                valor = tablero_actual[i][j]
                objetivo_i, objetivo_j = divmod(valor - 1, 3)
                distancia += abs(i - objetivo_i) + abs(j - objetivo_j)
    return distancia

# Función para resolver el 8-puzzle utilizando A*
# Entrada:
#   - inicial (Lista): Tablero inicial
#   - objetivo (Lista): Tablero objetivo
# Salida:
#   - solucion (Lista): Lista de tuplas con el movimiento y el tablero resultante
def resolver_8_puzzle(inicial, objetivo):
    # Cola de prioridad para los estados a explorar
    frontera = []
    heapq.heappush(frontera, Estado(inicial, "", 0, None))

    # Conjunto de nodos ya explorados
    explorados = set()

    # Mientras haya nodos en la frontera
    while frontera:
        estado_actual = heapq.heappop(frontera)

        # Verificar si se ha encontrado la solución
        if estado_actual.tablero == objetivo:
            # Se ha encontrado la solución
            solucion = []
            while estado_actual.padre:
                solucion.append((estado_actual.movimiento, estado_actual.tablero))
                estado_actual = estado_actual.padre
            solucion.reverse()
            return solucion

        # Agregar el estado actual a los explorados
        explorados.add(tuple(map(tuple, estado_actual.tablero)))

        # Generar los movimientos válidos a partir del estado actual
        for movimiento in generar_movimientos(estado_actual):
            if tuple(map(tuple, movimiento.tablero)) not in explorados:
                movimiento.costo += heuristica(movimiento.tablero, objetivo)
                heapq.heappush(frontera, movimiento)

    return None

# Función para generar un tablero con números random
# Salida:
#   - tablero (Lista): Tablero generado
def generar_tablero():
    tablero = [[0, 0, 0] for _ in range(3)]
    numeros = list(range(1, 9))
    numeros.append(0)

    for i in range(3):
        for j in range(3):
            numero = random.choice(numeros)
            numeros.remove(numero)
            tablero[i][j] = numero

    return tablero

if __name__ == "__main__":
    # Generar tablero inicial y objetivo
    estado_inicial = generar_tablero()

    estado_objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Imprimir tablero inicial y objetivo
    print("Tablero inicial:")
    for fila in estado_inicial:
        print(fila)
    print("************************")

    # Resolver el 8-puzzle
    solucion = resolver_8_puzzle(estado_inicial, estado_objetivo)

    # Imprimir la solución y los movimientos
    if solucion:
        i = 1
        print("Solución encontrada:")
        for movimiento, tablero in solucion:
            print(f"--- Movimiento {i}: {movimiento} ---")
            for fila in tablero:
                print(fila)
            print()
            i += 1
        print(f"Se encontró la solución en {len(solucion)} movimientos.")
    else:
        print("No se encontró solución.")
