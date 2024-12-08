# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9

from typing import Final

UNASSIGNED:Final[int]=0 # UNASSIGNED is used for empty cells in sudoku grid
N:Final[int]=9          #  N is used for size of Sudoku grid. Size will be NxN

# Searches the grid to find an entry that is still unassigned. 
# If found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
def find_unassigned_location(grid:list[list[int]])->tuple[int,int]:
    row:int=0
    while row < N:
        col:int = 0
        while col < N:
            if grid[row] [col] == UNASSIGNED:
                return (row,col)
            col += 1
        row += 1
    return None

# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number. */
def used_in_row(grid:list[list[int]], row:int, num:int)->bool:
    col:int = 0
    while col < N:
        if grid[row][col] == num:
            return True;
        col += 1
    return False;


# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number. */
def used_in_col(grid:list[list[int]], col:int, num: int)->bool:
    row:int=0
    while row < N:
        if grid[row][col] == num:
            return True
        row += 1
    return False;

# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number. 
def used_in_box(grid:list[list[int]], boxStartRow:int, boxStartCol:int, num:int)->bool:
    row:int=0
    while row < 3:
        col:int = 0
        while col < 3:
            if grid[row+boxStartRow] [col+boxStartCol] == num:
                return True
            col += 1
        row += 1
    return False

# Returns a boolean which indicates whether it will be legal to assign
# num to the given row,col location.
def is_safe(grid:list[list[int]], row:int, col:int, num:int)->bool:
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row%3 , col - col%3, num)


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


# A utility function to print grid
def print_grid(grid)->None:
    row:int=0
    while row < N:
        col:int = 0
        while col < N:
            print(grid[row][col], end=" ")
            col += 1
        row += 1
        print("");




# Takes a partially filled-in grid and attempts to assign values to
 # all unassigned locations in such a way to meet the requirements
#  for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(grid)->bool:
    # If there is no unassigned location, we are done
    location:tuple[int,int] = find_unassigned_location(grid)
    if location == None:
       return True
 
    # consider digits 1 to 9
    num:int = 1
    while num <= 9:
        # if looks promising
        (row,col)=location
        if is_safe(grid, row, col, num):
            # make tentative assignment
            grid[row][col] = num;
 
            # return, if success, yay!
            if solve_sudoku(grid):
                return True;
 
            # failure, unmake & try again
            grid[row][col] = UNASSIGNED;
        num += 1
    return False; # this triggers backtracking

if solve_sudoku(grid):
    print_grid(grid);
else:
    print("No solution exists")
 