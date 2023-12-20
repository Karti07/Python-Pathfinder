from collections import deque


# This function reads in a maze from a file and returns it as a list of lists of integers.
# Each integer corresponds to a different type of cell in the maze.
# 0 = empty cell
# 1 = wall
# 3 = end of the maze
# 5 = start of the maze
def load_maze(filename):
    with open(filename, "r") as file:
        maze = [[int(num) for num in line.strip().split(",")] for line in file]
        if len(maze) == 0:
            print("Maze Not loaded.")
    return maze

# This function takes in a maze and returns the coordinates of the start and end points.
# It searches the maze for the first occurrence of a 5 (start) and a 3 (end) and returns their coordinates as a tuple.
# If either the start or end point is not found, None is returned.
def find_start_and_end(maze):
    rows = len(maze)
    cols = len(maze[0])
    start = None
    end = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 5:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)
            # If both start and end points have been found, return them as a tuple.
            if start != None and end != None:
                return start, end

# This function takes in a maze and finds the shortest path from the start to the end point using BFS.
# It returns a list of coordinates representing the path from start to end.
# If no path is found, it returns None.
def solve_maze(maze):
    # Find the start and end positions in the maze
    start, end = find_start_and_end(maze)
    # Get the number of rows and columns in the maze
    rows = len(maze)
    cols = len(maze[0])
    # Initialize visited and parent 2D arrays to keep track of visited cells and their parents.
    visited = [[False for j in range(cols)] for i in range(rows)]
    parent = [[None for j in range(cols)] for i in range(rows)]
    # Initialize the queue with the start cell and mark it as visited.
    queue = [start]
    # Mark the starting position as visited
    visited[start[0]][start[1]] = True
    # While the queue is not empty, continue BFS.
    while queue:
        current = queue.pop(0)
        # If the current position is the end position, break out of the loop
        if current == end:
            break
        row, col = current
        neighbors = []
        # Check if the neighboring positions are valid and not blocked
        if row > 0 and maze[row - 1][col] != 1:
            neighbors.append((row - 1, col))
        if row < rows - 1 and maze[row + 1][col] != 1:
            neighbors.append((row + 1, col))
        if col > 0 and maze[row][col - 1] != 1:
            neighbors.append((row, col - 1))
        if col < cols - 1 and maze[row][col + 1] != 1:
            neighbors.append((row, col + 1))
        # For each unvisited neighbor, add it to the queue, mark it as visited, and set its parent to the current cell.
        for neighbor in neighbors:
            if not visited[neighbor[0]][neighbor[1]]:
                queue.append(neighbor)
                visited[neighbor[0]][neighbor[1]] = True
                parent[neighbor[0]][neighbor[1]] = current
    # If the end point has no parent, it means no path was found, so return None.
    if parent[end[0]][end[1]] is None:
        return None
    # Construct the path from start to end by backtracking from the end position
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append(start)
    path.reverse()
    return path

def print_maze(maze):
# Prints the maze as a grid of numbers
    for row in maze:
        print(" ".join(str(num) for num in row))

def print_solution(maze, path):
# Prints the maze with the solution path marked as 5's.
# Walls are represented by 1's and the end point is a 3.
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                print("1", end=" ")
            elif maze[i][j] == 3:
                print("3", end=" ")
            elif (i, j) in path:
                print("5", end=" ")
            else:
                print("0", end=" ")
        print()


def create_graph(matrix):
    graph = {}

    rows, cols = len(matrix), len(matrix[0])

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols and matrix[i][j] != 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 1:
                neighbors = []
                # Check neighboring positions
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if is_valid(ni, nj):
                        neighbors.append((ni, nj))
                graph[(i, j)] = neighbors

    return graph

# def create_graph(matrix):
#     graph = {}

#     rows, cols = len(matrix), len(matrix[0])

#     def is_valid(i, j):
#         return 0 <= i < rows and 0 <= j < cols and matrix[i][j] != 1

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] != 1:
#                 current_node = (i,j)  # Node description
#                 neighbors = []

#                 # Check neighboring positions
#                 for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
#                     if is_valid(ni, nj):
#                         neighbor = {}
#                         neighbor_node = (ni,nj)  # Neighbor description
#                         neighbor[neighbor_node] = 1  # Initialize weight to 1
#                         neighbors.append(neighbor)

#                 graph[current_node] = neighbors

#     return graph


def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}

    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex]:
            if distances[neighbor] == float('infinity'):
                distances[neighbor] = distances[current_vertex] + 1
                predecessors[neighbor] = current_vertex
                queue.append(neighbor)

        # Early stopping if the destination is reached
        if current_vertex == end:
            break

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return {'distance': distances[end], 'path': path}

def main():
    filename = "test_maze.txt"
    maze = load_maze(filename)

    # Dijkstra's algorithm
    print("\033[1;4;92mUsing Dijkstra's algorithm:\033[0m")
    # Create the graph
    graph = create_graph(maze)
    start_vertex, end_vertex = find_start_and_end(maze)
    result = dijkstra(graph, start_vertex, end_vertex)
    if(result['distance'] == float('infinity')):
        print("No solution found")
    else:
        print("Solution: ")
        print_solution(maze, result['path'])
    print("")

    # BFS
    print("\033[1;4;92mUsing BFS:\033[0m")
    path = solve_maze(maze)
    if path != None:
        print("Solution: ")
        print_solution(maze, path)
    else:
        print("No solution found")
 

if __name__ == "__main__":
    main()
