# Author: Bralee Gilday
# Course: CS325 - Analysis of Algorithms, Oregon State University
# Date last modified: 8/5/24
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


def solve_puzzle(Board, Source, Destination):
    """
    Solves the puzzle board to find the shortest path from the Source to the Destination using BFS.

    time complexity: O(M*N), where N is the number of rows and M is the number of columns in the puzzle.

    :param Board: A 2D list representing the puzzle board where cells are either empty ('.') or barriers ('#').
    :param Source: A tuple representing the starting cell (row, column).
    :param Destination: A tuple representing the target cell (row, column).
    :return: A tuple containing the shortest path as a list of cells and a string of directions (e.g., "RRDD").
    """
    # Find out the dimensions of the puzzle board
    total_rows = find_rows(Board)        # O(N)
    total_columns = find_columns(Board)  # O(M)

    # Initialize an empty set of visited cells (cells will be added in the form of a tuple (row,column)).
    visited_cells = set()

    # Initialize an empty queue. Add the source vertex to the queue.
    bfs_queue = deque()
    bfs_queue.append(Source)

    # Initialize a dictionary to hold the optimal paths to reach each cell.
    # The key will be the tuple to represent the current cell and the value
    # will be the cell it came from to get there.
    from_cell = {}

    # While the queue is not empty, dequeue the front element.
    # In the worst case, we might visit every cell in the board once; time complexity O(M * N).
    while len(bfs_queue) != 0:
        current_cell = bfs_queue.popleft()              # tuple (row, column)

        # Check if the current vertex (cell) is the goal.
        if current_cell == Destination:
            # trace path in dictionary to get the shortest path
            shortest_path = traverse_path(from_cell, Destination, Source)
            direction_string = direction_of_path(shortest_path, Source)

            result = (shortest_path, direction_string)

            return result

        else:
            # Add current vertex v (as a tuple) to the set of visited vertices.
            visited_cells.add(current_cell)

            # Initialize valid moves on the board
            moves = [(current_cell[0], (current_cell[1] + 1)),  # right
                     (current_cell[0], (current_cell[1] - 1)),  # left
                     ((current_cell[0] - 1), current_cell[1]),  # up
                     ((current_cell[0] + 1), current_cell[1])]  # down

            for adjacent_cell in moves:
                # Ensure the cell is within bounds and not visited yet
                if is_valid_move(Board, total_rows, total_columns, adjacent_cell)\
                        and (adjacent_cell not in visited_cells):
                    # Add the adjacent cell as a key to the dictionary; the value will be the current cell.
                    from_cell[adjacent_cell] = current_cell
                    # Enqueue adjacent cell
                    bfs_queue.append(adjacent_cell)


def find_rows(Board):
    """
    Finds the number of rows in the puzzle board.

    time complexity: O(N) where N is the number of rows in the puzzle.

    :param Board: A 2D list representing the puzzle board.
    :return: The number of rows in the board.
    """
    number_of_rows = 0
    for lists in Board:
        number_of_rows += 1
    return number_of_rows


def find_columns(Board):
    """
    Finds the number of columns in the puzzle board.

    time complexity: O(M) where M is the number of columns in the puzzle.

    :param Board: A 2D list representing the puzzle board.
    :return: The number of columns in the board.
    """
    number_of_columns = 0
    for element in Board[0]:
        number_of_columns += 1
    return number_of_columns


def is_valid_move(Board, rows, columns, cell):
    """
    Checks if a move to a given cell is valid. That is, it makes sure the
    cell is both on the board (within bounds) and not a barrier.

    time complexity: O(1)

    :param Board: A 2D list representing the puzzle board.
    :param rows: The total number of rows in the board.
    :param columns: The total number of columns in the board.
    :param cell: A tuple representing the cell (row, column) to move to.
    :return: True if the move is valid (within bounds and not a barrier), False otherwise.
    """
    # Check that the cell is in bounds
    if cell[0] < 0 or cell[0] >= rows or cell[1] < 0 or cell[1] >= columns:
        return False

    # If tuple is in bounds, then check that there is no barrier in the cell
    if Board[cell[0]][cell[1]] == '#':
        return False

    # Valid move
    return True


def traverse_path(from_cell_dict, dict_key, start):
    """
    Traces back the path from the destination to the source using the from_cell dictionary.

    time complexity: O(P), where P is the length of the shortest path. In the worst case,
        if the shortest path traverses through a significant portion of the board, P can
        be as large as the number of cells in the board, which is O(M * N).

    :param from_cell_dict: A dictionary mapping each cell to the cell it came from.
    :param dict_key: The destination cell.
    :param start: The source cell.
    :return: A list representing the shortest path from the source to the destination.
    """
    # initialize a path that starts with the destination cell (will be reversed)
    path = [dict_key]

    # continue following the path until back to the starting cell
    while dict_key != start:
        dict_value = from_cell_dict[dict_key]
        path.append(dict_value)
        dict_key = dict_value

    # reverse path (to be from start to destination)
    shortest_path = []
    for index in range(len(path)-1, -1, -1):
        cell = path[index]
        shortest_path.append(cell)

    return shortest_path


def direction_of_path(shortest_path, start):
    """
    Converts the shortest path into a string of directions.

    time complexity: O(P), where P is the length of the shortest path. In the worst case,
        if the shortest path traverses through a significant portion of the board, P can
        be as large as the number of cells in the board, which is O(M * N).

    :param shortest_path: A list representing the shortest path from the source to the destination.
    :param start: The source cell.
    :return: A string representing the directions (e.g., "RRDD").
    """
    current_cell = start
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
