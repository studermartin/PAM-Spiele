# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9

UNASSIGNED = 0  # UNASSIGNED is used for empty cells in sudoku grid
N = 9          # N is used for size of Sudoku grid. Size will be NxN

# Searches the grid to find an entry that is still unassigned. 
# If found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
def find_unassigned_location(grid):
    row = 0
    while row < N:
        col = 0
        while col < N:
            if grid[row][col] == UNASSIGNED:
                return (row, col)
            col += 1
        row += 1
    return None

# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number. */
def used_in_row(grid, row, num):
    col = 0
    while col < N:
        if grid[row][col] == num:
            return True
        col += 1
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number. */
def used_in_col(grid, col, num):
    row = 0
    while row < N:
        if grid[row][col] == num:
            return True
        row += 1
    return False

# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number. 
def used_in_box(grid, boxStartRow, boxStartCol, num):
    row = 0
    while row < 3:
        col = 0
        while col < 3:
            if grid[row + boxStartRow][col + boxStartCol] == num:
                return True
            col += 1
        row += 1
    return False

# Returns a boolean which indicates whether it will be legal to assign
# num to the given row,col location.
def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

assert find_unassigned_location(grid) == (0, 1)

assert used_in_row(grid, 0, 6)
assert used_in_row(grid, 0, 1) == False

assert used_in_col(grid, 1, 3)
assert used_in_col(grid, 1, 9) == False

assert used_in_box(grid, 0, 0, 7)
assert used_in_box(grid, 0, 0, 9) == False

assert is_safe(grid, 4, 1, 9) == False
assert is_safe(grid, 4, 1, 1) == True

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 0]]

def print_grid(grid):
    row = 0
    while row < N:
        col = 0
        while col < N:
            print(grid[row][col], end=" ")
            col += 1
        row += 1
        print("")

def solve_sudoku(grid):
    location = find_unassigned_location(grid)
    if location == None:
        return True

    num = 1
    while num <= 9:
        (row, col) = location
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = UNASSIGNED
        num += 1
    return False

if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists")
 