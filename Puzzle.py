# Author: Bralee Gilday
# Course: CS325 - Analysis of Algorithms, Oregon State University
# Date last modified: 3/19/25
# Description: Implementation of a 2-D puzzle solver. This implementation uses Breadth-First Search (BFS)
# to find the shortest path (least number of cells traversed) from the source to the destination on
# the puzzle board.
#
# Rules of the game are as follows:
# You are given a 2-D puzzle of size MxN, with N rows and M columns (M and N can be different).
# Each cell in the puzzle is either empty or has a barrier.
# An empty cell is marked by a '-' (hyphen) and a cell with a barrier is marked by a '#'.
# You are given two coordinates from the puzzle: (a, b) and (x, y).
# You are currently located at (a, b) and want to reach (x, y). You can move only in the following directions:
#
# L: move to the left cell from the current cell
# R: move to the right cell from the current cell
# U: move to the upper cell from the current cell
# D: move to the lower cell from the current cell
#
# You can move only to an empty cell and cannot move to a cell with a barrier.
# Your goal is to reach the destination cell while covering the minimum number of cells as you
# travel from the starting cell.

from collections import deque

class Board:
    """
    Represents a 2D puzzle board for the BFS puzzle solver.

    :param puzzle_board: A 2D list representing the puzzle board, where:
                         - An empty cell is represented by `'-'`.
                         - A barrier is represented by `'#'`.

    Data Members:
        _puzzle_board (list of list of str): The puzzle grid.
        _num_rows (int): The total number of rows in the board.
        _num_columns (int): The total number of columns in the board.
        _moves (list of tuple): A list of valid movement directions, where each 
                                tuple represents the (row change, column change).

    Methods:
        get_puzzle_board(): Returns the puzzle grid.
        get_num_rows(): Returns the total number of rows in the board.
        get_num_columns(): Returns the total number of columns in the board.
        get_moves(): Returns a list of valid movement directions.
        is_barrier(row_index, column_index): Checks if a given cell is a barrier.
        is_valid_move(cell): Determines if a move to a given cell is valid 
                             (within bounds and not a barrier).


    """
    def __init__(self, puzzle_board):
        """
        Initializes the Board with a given puzzle grid.

        :param puzzle_board: A 2D list representing the puzzle board.
        """
        self._puzzle_board = puzzle_board           # puzzle_board = a list of lists

        self._num_rows = len(puzzle_board)          # The number of lists represents the number of rows
        self._num_columns = len(puzzle_board[0])    # This is assuming all rows are the same length (valid puzzle board)

        # represent the (change in row index, change in column index)
        self._moves = [
                    (0, +1),   # right
                    (0, -1),   # left
                    (-1, 0),   # up
                    (+1, 0)    # down
        ]

    def get_puzzle_board(self):
        """
        Returns the puzzle grid.

        :return: A 2D list representing the puzzle board.
        """
        return self._puzzle_board
    
    def get_num_rows(self):
        """
        Returns the total number of rows in the board.

        :return: The number of rows in the board.
        """
        return self._num_rows
    
    def get_num_columns(self):
        """
        Returns the total number of columns in the board.

        :return: The number of columns in the board.
        """
        return self._num_columns
    
    def get_moves(self):
        """
        Returns a list of valid movement directions.

        :return: A list of tuples representing (row change, column change).
        """
        return self._moves
    
    def is_barrier(self, row_index, column_index):
        """
        Checks if a given cell is a barrier.

        :param row_index: The row index of the cell.
        :param column_index: The column index of the cell.
        :return: True if the cell is a barrier ('#'), False otherwise.
        """
        return self._puzzle_board[row_index][column_index] == "#"
    

    def is_valid_move(self, cell):
        """
        Checks if a move to a given cell is valid. That is, it makes sure the
        cell is both on the board (within bounds) and not a barrier.

        time complexity: O(1)

        :param cell: A tuple representing the cell (row, column) to move to.

        :return: True if the move is valid (within bounds and not a barrier), False otherwise.
        """
        # Check that the cell is in bounds
        if cell[0] < 0 or cell[0] >= self._num_rows:
            # if cell is out of row bounds
            return False
        
        if cell[1] < 0 or cell[1] >= self._num_columns:
            # if cell is out of column bounds
            return False
        
        # If tuple is in bounds, then check that there is no barrier in the cell
        if self.is_barrier(cell[0], cell[1]) == True:
            # if cell is a barrier
            return False

        # Valid move
        return True


class Puzzle:
    """
    Represents a puzzle solver that uses Breadth-First Search (BFS) to find the shortest path 
    from a source cell to a destination cell on a 2-D puzzle grid.

    :param board: A puzzle grid, which contains the layout of empty cells (`-`) and barriers (`#`).
    :param source: A tuple (row, column) representing the starting position on the board.
    :param destination: A tuple (row, column) representing the target destination on the board.
    
    Data Members:
        _board: An instance of the `Board` class, representing the puzzle grid.
        _source: A tuple (row, column) representing the starting position on the board.
        _destination: A tuple (row, column) representing the target destination on the board.
        _visited_cells: A set that tracks the cells that have already been visited.
        _bfs_queue: A queue used for BFS traversal, initially containing the source.
        _from_cell: A dictionary which will hold the hold the optimal paths to reach each cell. 
                    The key is a tuple to represent the current cell (row, column) and the 
                    value is the cell it came from to get there.

    Methods:
        solve(): Solves the puzzle using BFS and returns the shortest path and directions.
        get_shortest_path(): Traverses the path from the destination to the source using the from_cell dictionary.
        get_directions(): Converts the shortest path into a string of movement directions (e.g., "RRDD").
    """

    def __init__(self, board, source, destination):
        """
        Initializes the Puzzle solver with a given board, source, and destination.

        :param board: A puzzle grid, which contains the layout of empty cells (`-`) and barriers (`#`).
        :param source: A tuple (row, column) representing the starting position.
        :param destination: A tuple (row, column) representing the target destination.
        """
        self._board = Board(board)
        self._source = source
        self._destination = destination

        self._visited_cells = set()                 # cells will be added in the form of a tuple (row,column)

        self._bfs_queue = deque()                   # Initialize an empty queue. 
        self._bfs_queue.append(self._source)        # Add the source vertex to the queue.

        self._from_cell = {}

    
    def solve(self):
        """
        Solves the puzzle board to find the shortest path from the Source to the Destination using BFS.

        time complexity: O(M*N), where N is the number of rows and M is the number of columns in the puzzle 
                        (i.e., we might visit every cell in the board once).

        :return: A tuple containing the shortest path as a list of cells and a string of directions (e.g., "RRDD").
        """

        # While the queue is not empty, dequeue the front element.
        while len(self._bfs_queue) != 0:
            current_cell = self._bfs_queue.popleft()              # tuple (row, column)

            # Check if the current vertex (cell) is the goal.
            if current_cell == self._destination:
                # trace path in dictionary to get the shortest path
                shortest_path = self.get_shortest_path()
                direction_string = self.get_directions(shortest_path)

                result = (shortest_path, direction_string)

                return result

            else:
                # Add current vertex v (as a tuple) to the set of visited vertices.
                self._visited_cells.add(current_cell)

                for move in self._board.get_moves():
                    adjacent_cell = (current_cell[0] + move[0], current_cell[1] + move[1])
                    
                    # Ensure the cell is within bounds and not visited yet
                    if self._board.is_valid_move(adjacent_cell) and (adjacent_cell not in self._visited_cells):
                        # Add the adjacent cell as a key to the dictionary; the value will be the current cell.
                        self._from_cell[adjacent_cell] = current_cell
                        # Enqueue adjacent cell
                        self._bfs_queue.append(adjacent_cell)

    def get_shortest_path(self):
        """
        Traces back the path from the destination to the source using the from_cell dictionary.

        time complexity: O(P), where P is the length of the shortest path. In the worst case,
            if the shortest path traverses through a significant portion of the board, P can
            be as large as the number of cells in the board, which is O(M * N).

        :return: A list representing the shortest path from the source to the destination.
        """
        # initialize a path that starts with the destination cell (will be reversed)
        cell = self._destination
        path = [cell]

        # continue following the path until back to the starting cell
        while cell != self._source:
            dict_value = self._from_cell[cell]
            path.append(dict_value)
            cell = dict_value

        # reverse path (to be from source to destination)
        return path[::-1]


    def get_directions(self, shortest_path):
        """
        Converts the shortest path into a string of directions.

        time complexity: O(P), where P is the length of the shortest path. In the worst case,
            if the shortest path traverses through a significant portion of the board, P can
            be as large as the number of cells in the board, which is O(M * N).

        :param shortest_path: A list representing the shortest path from the source to the destination.

        :return: A string representing the directions (e.g., "RRDD").
        """
        current_cell = self._source
        direction_string = ""

        for cell in shortest_path:
            # if move is to the right
            if cell == (current_cell[0], (current_cell[1] + 1)):    # right
                direction_string += "R"

            # if move is to the left
            elif cell == (current_cell[0], (current_cell[1] - 1)):  # left
                direction_string += "L"

            # if move is down
            elif cell == ((current_cell[0] - 1), current_cell[1]):  # up
                direction_string += "U"

            # if move is up
            elif cell == ((current_cell[0] + 1), current_cell[1]):  # down
                direction_string += "D"

            current_cell = cell

        return direction_string
