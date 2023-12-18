# Python-Pathfinder

This Python program is designed to find a path through mazes of varying complexity. The mazes are represented in a text file called 'test_maze.txt' and are stored internally as a two-dimensional list. The program marks the path with '5's and outputs the completed maze, highlighting the path used.

## Usage

1. Place your maze files in the same directory as the program.
2. Ensure your maze file follows the specified format (see Maze File Format).
3. Run the program by executing the 'python_pathfinder.py' file in your IDE.

## Maze File Format (test_maze.txt)

Each maze file should contain rows of integers separated by commas, with each row represented on a separate line. The integers represent the following:

- **0**: Empty space
- **1**: Wall
- **5**: Current location (path)
- **3**: Finish/exit point

### Example

5, 0, 1, 1, 1, 1
1, 0, 1, 0, 0, 0
0, 0, 1, 0, 1, 0
0, 1, 0, 0, 1, 0
0, 0, 0, 1, 1, 3

**Output**

The program will output the solution as a path of '5's in a grid, leaving the walls and finish point unchanged. Values are separated by a space.

5 5 1 1 1 1
1 5 1 5 5 5
5 5 1 5 1 5
5 1 5 5 1 5
5 5 5 1 1 3
