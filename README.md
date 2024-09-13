# BFS_puzzle_solver
Python-based implementation of a 2D puzzle solver. Uses Breadth-First Search (BFS) to find the shortest path (least number of cells traversed) from the source to the destination on the puzzle board.

### Example Usage
Here's a simple example of how the BFS-puzzle solver finds the shortest path in various puzzle configurations.

```python
puzzle = [
   ['-', '-', '-', '-', '-'],
   ['-', '-', '#', '-', '-'],
   ['-', '-', '-', '-', '-'],
   ['#', '-', '#', '#', '-'],
   ['-', '#', '-', '-', '-']
  ]

print("Example 1:")
# Path from (0,2) to (2,2) through open cells.
# Expected output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR'
print("Path:", solve_puzzle(puzzle, (0, 2), (2, 2)))

print("\nExample 2:")
# Path from (0,0) to (4,4) avoiding obstacles.
# Expected path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'DDRRRRDD'
print("Path:", solve_puzzle(puzzle, (0, 0), (4, 4)))

print("\nExample 3:")
# No valid path from (0,0) to (4,0) due to obstacles.
# Expected: None
print("Path:", solve_puzzle(puzzle, (0, 0), (4, 0)))

print("\nExample 4:")
# Start and end at the same point (0,0).
# Expected path: [(0,0)], ''
print("Path:", solve_puzzle(puzzle, (0, 0), (0, 0)))
```

### Project Status
This project is currently complete, with potential for future enhancements, such as...

### License
This project is licensed under the MIT License. See the LICENSE file for more information.

### Contact
Bralee Gilday - www.linkedin.com/in/bralee-gilday
