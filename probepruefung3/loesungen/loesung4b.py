'''
Lösung 1b: Sudoku

Bessere Lösung mehr im Python-Stil mit for-Schleifen.

'''

# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9

UNASSIGNED = 0  # UNASSIGNED is used for empty cells in sudoku grid
N = 9          # N is used for size of Sudoku grid. Size will be NxN


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def print_grid(grid):
    for row in range(N):
        for col in range(N):
            print(grid[row][col], end=" ")
        print("")


''' Teilaufgabe 1: Methode used_in_row '''

# Gib True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Zeile row verwendet wird, sonst False.
def used_in_row(grid, row, num):
    return num in grid[row]


# Testet, ob die Zahl 6 bereits in der ersten Zeile des Sudoku-Feldes verwendet wird.
assert used_in_row(grid, 0, 6) == True

# Testet, ob die Zahl 1 nicht in der ersten Zeile des Sudoku-Feldes verwendet wird.
assert used_in_row(grid, 0, 1) == False


''' Teilaufgabe 2: Methode used_in_column '''

# Gibt True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Spalte col verwendet wird, sonst False.
def used_in_col(grid, col, num):
    for row in range(N):
        if grid[row][col] == num:
            return True
    return False

# Testet, ob die Zahl 3 bereits in der zweiten Spalte des Sudoku-Feldes verwendet wird.
assert used_in_col(grid, 1, 3) == True

# Testet, ob die Zahl 9 nicht in der zweiten Spalte des Sudoku-Feldes verwendet wird.
assert used_in_col(grid, 1, 9) == False


''' Teilaufgabe 3: used_in_box '''

# Gibt True zurück, falls die gegeben Zahl num bereits im   
# spefizierten 3x3-Quadrat schon vorkommt, False sonst.
# Die Parameter boxStartRow und boxStartCol haben die Werte 0, 3 oder 6.
def used_in_box(grid, boxStartRow, boxStartCol, num):
    for row in range(3):
        for col in range(3):
            if grid[row + boxStartRow][col + boxStartCol] == num:
                return True
    return False

# Testet, ob die Zahl 7 im obersten Quadrat im Sudoku-Feld verwendet wird.
assert used_in_box(grid, 0, 0, 7) == True
# Testet, ob die Zahl 9 nicht im obersten Quadrat im Sudoku-Feld verwendet wird.
assert used_in_box(grid, 0, 0, 9) == False


''' Teilaufgabe 4: is_safe '''

# Git True zurück, falls die gebene Zahl num in an die Zeile/Spalte gesetzt werden kann, sonst False.
# Die Methode prüft, ob die Zahl nicht bereits in der Zeile, Spalte oder im Quadrat vorkommt.
def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)

assert is_safe(grid, 4, 1, 9) == False
assert is_safe(grid, 4, 1, 1) == True


''' Teilaufgabe 5: find_unassigned_location '''

# Sucht auf dem Spielfeld nach einem nicht besetzten Feld.
# Falls ein nicht besetztes Feld gefunden wird, werden die Koordinaten als Tuple zurückgegeben.
# Falls alle Felder besetzt sind, wird None zurückgegeben.
def find_unassigned_location(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == UNASSIGNED:
                return (row, col)
    return None

assert find_unassigned_location(grid) == (0, 1)

