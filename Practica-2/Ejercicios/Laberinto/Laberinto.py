
# Autor: Gustavo Cerda García
# Practica 2
# Ejercicio 2: Laberinto

#Aquí guardamos las funciones necesarias para resolver el laberinto

#Librerías
import random

#Función que resuelve el laberinto
#Entradas:
#   maze: Laberinto (matriz de caracteres)
#   start: Posición de inicio (tupla)
#   end: Posición final (tupla)
#Salidas:
#   solved: Booleano que indica si se encontró solución
#   path: Lista con el camino a seguir
def solve_maze(maze, start, end):
    stack = [start]

    # Mientras haya nodos por visitar
    while stack:
        x, y = stack[-1] # Posicion actual

        # Si llegamos al final
        if (x, y) == end:
            return True, stack

        # Si no, marcamos la posicion actual como visitada
        maze[x][y] = '2'

        # Generamos los movimientos posibles
        # Si encontramos un camino, lo agregamos a la pila
        # Los movimientos son: arriba, derecha, abajo, izquierda
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy # Nueva posicion

            # Si la nueva posicion es valida
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                # Si la nueva posicion es un camino o el final
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    stack.append((nx, ny)) # Agregamos la nueva posicion a la pila
                    break
        else:
            stack.pop() # Si no encontramos un camino, retrocedemos

    return False, [] # Si no encontramos solucion, retornamos falso

    # Escoge dos puntos aleatorios en el laberinto
    x1, y1 = random.randint(1, len(maze) - 2), random.randint(1, len(maze[0]) - 2)
    x2, y2 = random.randint(1, len(maze) - 2), random.randint(1, len(maze[0]) - 2)

    # Asegura que los puntos no sean paredes
    while maze[x1][y1] == '1':
        x1, y1 = random.randint(1, len(maze) - 2), random.randint(1, len(maze[0]) - 2)
    while maze[x2][y2] == '1' or (x2 == x1 and y2 == y1):
        x2, y2 = random.randint(1, len(maze) - 2), random.randint(1, len(maze[0]) - 2)

    # Conecta los dos puntos con un puente
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if maze[x1][y] == '0':
                maze[x1][y] = 'B'
            else:
                maze[x1][y] = '0'
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if maze[x][y1] == '0':
                maze[x][y1] = 'B'
            else:
                maze[x][y1] = '0'