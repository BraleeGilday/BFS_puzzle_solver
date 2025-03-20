# BFS_puzzle_solver

## Description
This program implements a **2-D puzzle solver** using **Breadth-First Search (BFS)** to find the shortest path (in terms of the number of cells traversed) between two points on a puzzle board. It is now structured using **object-oriented design**, with two classes:

- **`Board`**: Represents the puzzle grid, handling board-related logic (e.g., move validation, barriers).
- **`Puzzle`**: Implements BFS to find the shortest path and reconstructs the solution.

The puzzle consists of an MxN grid where each cell is either empty (`-`) or contains a barrier (`#`). The goal is to travel from a given **starting cell** to a **target destination** while avoiding barriers and using the **fewest possible moves**.

### Rules:
- The puzzle grid is made up of **empty cells** (`-`) and **barrier cells** (`#`).
- You can move in four directions: Left (**L**), Right (**R**), Up (**U**), Down (**D**).
- You can only move to an empty cell, not to a barrier.
- The objective is to reach the destination with the least number of moves.

## Example Usage
The following examples show how the BFS-puzzle solver can be used to find paths through a puzzle grid.

```python
puzzle_board = [
   ['-', '-', '-', '-', '-'],
   ['-', '-', '#', '-', '-'],
   ['-', '-', '-', '-', '-'],
   ['#', '-', '#', '#', '-'],
   ['-', '#', '-', '-', '-']
  ]

# Example 1: Solving from (0, 2) to (2, 2)
puzzle1 = Puzzle(puzzle_board, (0, 2), (2, 2))
print("Path from (0, 2) to (2, 2):", puzzle1.solve())
# Expected output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR'

# Example 2: Solving from (0, 0) to (4, 4)
puzzle2 = Puzzle(puzzle_board, (0, 0), (4, 4))
print("Path from (0, 0) to (4, 4):", puzzle2.solve())
# Expected path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)], 'DDRRRRDD'

# Example 3: No valid path from (0,0) to (4,0)
puzzle3 = Puzzle(puzzle_board, (0, 0), (4, 0))
print("Path from (0, 0) to (4, 0):", puzzle3.solve())
# Expected: None

# Example 4: Starting and destination are the same
puzzle4 = Puzzle(puzzle_board, (0, 0), (0, 0))
print("Path from (0, 0) to (0, 0):", puzzle4.solve())
# Expected path: [(0,0)], ''

```

## Features
- **Efficient Pathfinding**: Uses Breadth-First Search (BFS) to ensure the shortest path is found in the puzzle.
- **Object-Oriented Design**: Uses Board to manage grid logic and Puzzle to handle solving.
- **Flexible Grid Sizes**: Supports any MxN grid, allowing for puzzles with varying dimensions.
- **Barrier Handling**: Correctly identifies barriers (`#`) and avoids them during the search for the shortest path.
- **Direction Output**: Returns both a list of coordinates for the shortest path and a string indicating the directions (e.g., `"RRDD"`).
- **Custom Starting and Ending Points**: Easily set your own source and destination cells on the grid.

## Time Complexity
The time complexity of the BFS approach is **O(M * N)**, where:
- **M** is the number of columns.
- **N** is the number of rows.

This complexity reflects the fact that each cell is processed at most once, ensuring an efficient exploration of the grid.

### Project Status
Completed refactor from a function-based approach to an object-oriented design. <br>
The next update on this project will be to add validation for the puzzle board (e.g., ensure input is a valid rectangular grid).

### Contact
Bralee Gilday - www.linkedin.com/in/bralee-gilday
