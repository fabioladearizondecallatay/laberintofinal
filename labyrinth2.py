#definir funcion que para buscar el camino
def find_path(maze):
    #define una funcion dentro que es para hacer un "depth first search"
    def dfs(x, y):
        #marcar la posición actual como visitada
        visited[x][y] = True

        #para ver si hemos llegado a la salida
        if x == rows - 1 and y == columns - 1:
            return True

        # Intentar moverse hacia abajo, derecha, arriba y izquierda
        directions = [(1, 0, 'Abajo'), (0, 1, 'Derecha'), (-1, 0, 'Arriba'), (0, -1, 'Izquierda')]
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            #para verificar si la posicion es valida y no esta ya visitada 
            if 0 <= nx < rows and 0 <= ny < columns and maze[nx][ny] == ' ' and not visited[nx][ny]:
                path.append(move)
                if dfs(nx, ny):
                    return True
                path.pop()

        return False

    #inicializa variables
    rows = len(maze)
    columns = len(maze[0])
    #para hacer la matriz visited
    visited = [[False] * columns for _ in range(rows)]
    path = []

    #comienza la dfs desde la esquina superior izquierda
    dfs(0, 0)

    return path

#define la dimension del laberinto
rows = 5
columns = 5
#para hacerel laberinto con espacios
maze = [[' ' for _ in range(columns)] for _ in range(rows)]

wall_coordinates = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
for i, j in wall_coordinates:
    maze[i][j] = 'X'

#encuentra el camino en el laberinto
path = find_path(maze)

#para mostrar el camino
print(path)
