# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9

from typing import Final, Optional, Tuple

UNASSIGNED:Final[int]=0 # UNASSIGNED is used for empty cells in sudoku grid
N:Final[int]=9          #  N is used for size of Sudoku grid. Size will be NxN

def find_unassigned_location(grid: list[list[int]]) -> Optional[Tuple[int, int]]:
    """
    Searches the grid to find an entry that is still unassigned.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.

    Returns:
    - A tuple (row, col) indicating the position of the first unassigned (empty) cell found in the grid.
    - Returns None if all cells are assigned.

    The function iterates over the grid and returns the coordinates of the first cell that contains
    the value UNASSIGNED. If no such cell is found, it returns None, indicating that the grid is fully assigned.
    """
    return next(((row, col) for row in range(N) for col in range(N) if grid[row][col] == UNASSIGNED), None)

def used_in_row(grid: list[list[int]], row: int, num: int) -> bool:
    """
    Checks if a given number is already used in a specific row of the Sudoku grid.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.
    - row: An integer representing the index of the row to check.
    - num: An integer representing the number to check for in the specified row.

    Returns:
    - A boolean value: True if the number is found in the specified row, False otherwise.

    The function iterates over the specified row and checks if the given number
    is present. If found, it returns True, indicating that the number is already
    used in that row. Otherwise, it returns False.
    """
    return any(grid[row][col] == num for col in range(N))


def used_in_col(grid: list[list[int]], col: int, num: int) -> bool:
    """
    Checks if a given number is already used in a specific column of the Sudoku grid.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.
    - col: An integer representing the index of the column to check.
    - num: An integer representing the number to check for in the specified column.

    Returns:
    - A boolean value: True if the number is found in the specified column, False otherwise.

    The function iterates over the specified column and checks if the given number
    is present. If found, it returns True, indicating that the number is already
    used in that column. Otherwise, it returns False.
    """
    return any(grid[row][col] == num for row in range(N))

def used_in_box(grid: list[list[int]], boxStartRow: int, boxStartCol: int, num: int) -> bool:
    """
    Checks if a given number is already used in a specific 3x3 box of the Sudoku grid.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.
    - boxStartRow: An integer representing the starting row index of the 3x3 box.
    - boxStartCol: An integer representing the starting column index of the 3x3 box.
    - num: An integer representing the number to check for in the specified 3x3 box.

    Returns:
    - A boolean value: True if the number is found in the specified 3x3 box, False otherwise.

    The function iterates over the specified 3x3 box and checks if the given number
    is present. If found, it returns True, indicating that the number is already
    used in that box. Otherwise, it returns False.
    """
    return any(grid[row + boxStartRow][col + boxStartCol] == num for row in range(3) for col in range(3))


def is_safe(grid: list[list[int]], row: int, col: int, num: int) -> bool:
    """
    Determines if it's safe to assign a number to a given position in the Sudoku grid.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.
    - row: An integer representing the row index of the position to check.
    - col: An integer representing the column index of the position to check.
    - num: An integer representing the number to check for safety at the specified position.

    Returns:
    - A boolean value: True if it's safe to assign the number to the specified position,
      meaning the number is not already present in the current row, column, or 3x3 box.
      False otherwise.
    """
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)


grid:list[list[int]] =  [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

assert find_unassigned_location(grid)==(0,1)

assert used_in_row(grid,0,6)
assert used_in_row(grid,0,1) == False

assert used_in_col(grid,1,3)
assert used_in_col(grid,1,9) == False


assert used_in_box(grid, 0, 0, 7)
assert used_in_box(grid, 0, 0, 9) == False

assert is_safe(grid, 4, 1, 9) == False
assert is_safe(grid, 4, 1, 1) == True


# Grid from https://en.wikipedia.org/wiki/Sudoku
grid:list[list[int]] =  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 0]]


def print_grid(grid: list[list[int]]) -> None:
    """
    Prints the Sudoku grid in a formatted manner.

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.

    The function iterates over each row of the grid and prints the numbers
    in a space-separated format.
    """
    for row in grid:
        print(" ".join(str(num) for num in row))


def solve_sudoku(grid: list[list[int]]) -> bool:
    """
    Solves the Sudoku puzzle using backtracking. It takes a partially filled-in grid 
    and attempts to assign values to

    Parameters:
    - grid: A 2D list representing the Sudoku grid, where each element is an integer.

    Returns:
    - A boolean value: True if the Sudoku puzzle is solved successfully, False otherwise.

    The function attempts to assign values to all unassigned locations in the grid
    in such a way that the Sudoku rules are satisfied. It uses backtracking to
    explore possible solutions and returns True if a solution is found.
    """
    # Find an unassigned location
    location = find_unassigned_location(grid)
    if location is None:
        return True  # Puzzle solved

    row, col = location

    # Try digits 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # Tentatively assign num

            if solve_sudoku(grid):
                return True  # Success

            grid[row][col] = UNASSIGNED  # Failure, unmake & try again

    return False  # Triggers backtracking

if solve_sudoku(grid):
    print_grid(grid);
else:
    print("No solution exists")
 