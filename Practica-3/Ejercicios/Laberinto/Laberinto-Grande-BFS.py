from collections import deque
import sys

def solve_maze(maze, start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return True, path

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '2'

    return False, []

if __name__ == "__main__":
    print("Laberinto más grande con solución (13x13)")
    # 0 = open path, 1 = wall, S = start, E = end
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

    print("Uso de memoria:")
    print("Solved: ", sys.getsizeof(solved))
    print("Path: ", sys.getsizeof(path))