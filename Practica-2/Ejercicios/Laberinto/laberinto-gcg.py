
#Autor: Gustavo Cerda García
#Ejercicio 2: Laberinto

#Tipo de Laberinto: Laberinto con solución (5x5)

#Programa que resuelve un laberinto utilizanado una DFS (Depth First Search)

#Librerias
import time
from Laberinto import solve_maze

if __name__ == "__main__":
    inicio = time.time()

    # 0 = camino libre, 1 = pared, S = inicio, E = final
    maze = [
        ['1', '1', '1', '1', '1'],
        ['S', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', 'E'],
        ['1', '1', '1', '1', '1']
    ]

    start = (1, 0) # Posicion de inicio
    end = (3, 4) # Posicion final

    # Resolvemos el laberinto
    solved, path = solve_maze(maze, start, end)

    # Si encontramos solucion, marcamos el camino
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
    print("Tiempo de ejecucion: ", fin - inicio)
