#code has been optimised to run faster using less caching and more direct functions
from collections import deque

def load_maze(filename):
    with open(filename, "r") as file:
        maze = [[int(num) for num in line.strip().split(",")] for line in file]
        if len(maze) == 0:
            print("Maze Not loaded.")
    return maze

def find_start_and_end(maze):
    start = None
    end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 5:
                start = (i, j)
            elif cell == 3:
                end = (i, j)
            if start and end:
                return start, end

def solve_maze(maze):
    start, end = find_start_and_end(maze)
    rows = len(maze)
    cols = len(maze[0])
    visited = set()
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    queue = deque([start])
    visited.add(start)
    while queue:
        current = queue.popleft()
        if current == end:
            break
        row, col = current
        neighbors = []
        if row > 0 and maze[row - 1][col] != 1:
            neighbors.append((row - 1, col))
        if row < rows - 1 and maze[row + 1][col] != 1:
            neighbors.append((row + 1, col))
        if col > 0 and maze[row][col - 1] != 1:
            neighbors.append((row, col - 1))
        if col < cols - 1 and maze[row][col + 1] != 1:
            neighbors.append((row, col + 1))
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor[0]][neighbor[1]] = current
    if parent[end[0]][end[1]] is None:
        return None
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append(start)
    path.reverse()
    return path

def print_maze(maze):
    for row in maze:
        print(" ".join(str(num) for num in row))

def print_solution(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                print("1", end=" ")
            elif maze[i][j] == 3:
                print("3", end=" ")
            elif (i, j) in path:
                print("5", end=" ")
            else:
                print("0", end
