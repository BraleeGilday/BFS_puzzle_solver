# BFS_puzzle_solver

## Description
This program implements a 2-D puzzle solver using Breadth-First Search (BFS) to find the shortest path (in terms of the number of cells traversed) between two points on a puzzle board. The puzzle consists of an MxN grid where each cell is either empty (`-`) or contains a barrier (`#`). The goal is to travel from a given starting cell to a target destination while avoiding barriers and using the fewest possible moves.

### Rules:
- The puzzle grid is made up of empty cells (`-`) and barrier cells (`#`).
- You can move in four directions: Left (L), Right (R), Up (U), Down (D).
- You can only move to an empty cell, not to a barrier.
- The objective is to reach the destination with the least number of moves.

## Example Usage
The following examples show how the BFS-puzzle solver can be used to find paths through a puzzle grid.

```python
puzzle = [
   ['-', '-', '-', '-', '-'],
   ['-', '-', '#', '-', '-'],
   ['-', '-', '-', '-', '-'],
   ['#', '-', '#', '#', '-'],
   ['-', '#', '-', '-', '-']
  ]

# Example 1: Solving from (0, 2) to (2, 2)
print("Path from (0, 2) to (2, 2):", solve_puzzle(puzzle, (0, 2), (2, 2)))
# Expected output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR'

# Example 2: Solving from (0,0) to (4,4)
print("Path from (0, 0) to (4, 4):", solve_puzzle(puzzle, (0, 0), (4, 4)))
# Expected path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'DDRRRRDD'

# Example 3: No valid path from (0,0) to (4,0)
print("Path from (0, 0) to (4, 0):", solve_puzzle(puzzle, (0, 0), (4, 0)))
# Expected: None

# Example 4: Starting and destination are the same
print("Path from (0, 0) to (0, 0):", solve_puzzle(puzzle, (0, 0), (0, 0)))
# Expected path: [(0,0)], ''

```

## Features
- **Efficient Pathfinding**: Uses Breadth-First Search (BFS) to ensure the shortest path is found in the puzzle.
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
This project is currently complete, with potential for future enhancements, such as...

### License
This project is licensed under the MIT License. See the LICENSE file for more information.

### Contact
Bralee Gilday - www.linkedin.com/in/bralee-gilday
