# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9 Sudoku

UNASSIGNED=0    # UNASSIGNED für eine leere Zelle
N=9             # N ist die Seitenlänge des Sudoku-Spielfeldes

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Spielfeld ausgeben
def print_grid(grid):
    row = 0
    while row < N:
        col = 0
        while col < N:
            print(grid[row][col], end=" ")
            col += 1
        row += 1
        print("")


''' Aufgabe 1: Methode used_in_row '''

# Gib True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Zeile row verwendet wird, sonst False.
def used_in_row(grid, row, num):
    pass

assert used_in_row(grid, 0, 6)
assert used_in_row(grid, 0, 1) == False


''' Aufgabe 2: Methode used_in_column '''

# Gibt True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Spalte col verwendet wird, sonst False.
def used_in_col(grid, col, num):
    pass

assert used_in_col(grid, 1, 3)
assert used_in_col(grid, 1, 9) == False


''' Aufgabe 3: used_in_box '''

# Gibt True zurück, falls die gegeben Zahl num bereits in der  
# spefizierten 3x3-Quadrat schon vorkommt, False sonst.
def used_in_box(grid, boxStartRow, boxStartCol, num):
    pass

assert used_in_box(grid, 0, 0, 7)
assert used_in_box(grid, 0, 0, 9) == False


''' Aufgabe 4: is_safe '''

# Git True zurück, falls die gebene Zahl num in an die Zeile/Spalte gesetzt werden kann, sonst False.
# Die Methode prüft, ob die Zahl nicht bereits in der Zeile, Spalte oder im Quadrat vorkommt.
def is_safe(grid, row, col, num):
    pass

assert is_safe(grid, 4, 1, 9) == False
assert is_safe(grid, 4, 1, 1) == True


''' Aufgabe 5: find_unassigned_location '''

# Sucht auf dem Spielfeld nach einem nicht besetzten Feld.
# Falls ein nicht besetztes Feld gefunden wird, werden die Koordinaten als Tuple zurückgegeben.
# Falls alle Felder besetzt sind, wird None zurückgegeben.
def find_unassigned_location(grid):
    pass

assert find_unassigned_location(grid) == (0, 1)


''' Aufgabe 6: solve_sudoku '''


# Versucht in ein partiell-gefülltes Spielfeld Werte in die leeren Felder abzufüllen,
# so dass die Bedingungen für Sudoku erfüllt werden (keine doppelten Werte über Zeilen, Spalten oder 3x3-Quadrate).
# Gibt True zurück, falls das Spielfeld gefüllt werden konnte, sonst False.
def solve_sudoku(grid):
    # Teil 1:
    # Falls es keine leeren Felder mehr hat, dann ist das Spielfeld erfolgreich gelöst.
    pass

    # Teil 2:
    # Der Reihe nach die Ziffern 1 bis 9 durchprobieren.
    # Die Zahl versuchsweise einsetzen, falls sie eingesetzt werden darf.
    # Falls sich so das Spielfeld lösen lässt, gut, sonst die Zahl wieder rausnehmen.
    pass

if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists")
 