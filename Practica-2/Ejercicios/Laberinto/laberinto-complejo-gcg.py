
# Autor: Gustavo Cerda García
# Practica 2
# Ejercicio 2: Laberinto

# Tipo de Laberinto: Laberinto con solución mas complejo (10x10)

# Programa que resuelve un laberinto utilizanado una DFS (Depth First Search)

# Librerias
import time
from Laberinto import solve_maze

if __name__ == "__main__":
    inicio = time.time()

    # Laberinto más grande y complejo (10x10)
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', 'E', '1', '0', '0', '1']
    ]

    start = (1, 0)  # Posición de inicio
    end = (9, 5)    # Posición final

    # Resolvemos el laberinto
    solved, path = solve_maze(maze, start, end)

    # Si encontramos solución, marcamos el camino
    if solved:
        print("Maze Solved!")
        # Marcamos el camino en el laberinto
        for x, y in path:
            # Si no es el inicio o el final
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        # Imprimimos el laberinto
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

    fin = time.time()
    print("Tiempo de ejecución: ", fin - inicio)
