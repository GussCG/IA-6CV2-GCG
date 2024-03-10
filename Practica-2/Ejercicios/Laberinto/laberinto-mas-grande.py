
#Autor: Gustavo Cerda García
#Ejercicio 2: Laberinto

#Tipo de Laberinto: Laberinto con solución grande (13x13)

#Programa que resuelve un laberinto utilizanado una DFS (Depth First Search)

#Librerias
import time
from Laberinto import solve_maze

if __name__ == "__main__":
    inicio = time.time()

    # Laberinto más grande con solución
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1'],
        ['1', 'E', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]

    start = (1, 0)
    end = (12, 1)  # Posición final

    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

    fin = time.time()
    print("Tiempo de ejecucion: ", fin - inicio)