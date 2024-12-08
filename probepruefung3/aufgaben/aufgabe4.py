# https://web.archive.org/web/20160828164622/http://www.geeksforgeeks.org/backtracking-set-7-suduku/
# 9x9 Sudoku
'''
Aufgabe 1: Sudoku

Implementiere der Reihe nach die Teilaufgaben.

Die assert-Anweisungen geben eine Rückmeldung darüber, ob deine Implementation korrekt ist. 
Tritt ein Fehler auf (AssertionError), dann ist sie nicht korrekt. 
Tritt kein Fehler auf, ist die Implementation auf einem guten Weg.

Teilaufgabe 5 enthält ein Sprachelement, dass wir so noch nicht behandelt haben: Tuples und den Wert None.
Tuples dienen dazu, dass man mehrere Werte zurückgeben kann. Dasselbe könnte man auch mit einer Liste machen.
Anstatt eine Liste von zwei Zahlen
    [1,5]
nutzt man einfach die Schreibweise als Tuple:
    (1,5)
In einer Funktion kann man also, hat man die Zeile und Spalte gefunden, mittels 
    return (row,col)
die Werte zurückgeben. Vorteil von Tuples, siehe https://builtin.com/software-engineering-perspectives/python-tuples-vs-lists.

Die Methode find_unassigned_location soll die Position eines noch nicht besetzten Feldes zurückgeben.
Normalerweise ist dies also ein Tuple, z. B. (1,5). Falls alle Felder besetzt sind, dann soll None zurückgegeben werden.
Dies bedeutet, dass kein leeres Feld existiert.

'''


UNASSIGNED=0    # UNASSIGNED für eine leere Zelle
N=9             # N ist die Seitenlänge des Sudoku-Spielfeldes

# Ein teilweise ausgefülltes Sudoku-Feld
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


''' Teilaufgabe 1: Methode used_in_row '''

# Gib True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Zeile row verwendet wird, sonst False.
def used_in_row(grid, row, num):
    pass

# Testet, ob die Zahl 6 bereits in der ersten Zeile des Sudoku-Feldes verwendet wird.
assert used_in_row(grid, 0, 6) == True

# Testet, ob die Zahl 1 nicht in der ersten Zeile des Sudoku-Feldes verwendet wird.
assert used_in_row(grid, 0, 1) == False


''' Teilaufgabe 2: Methode used_in_column '''

# Gibt True zurück, falls die gegebene Zahl num bereits
# in der angegebenen Spalte col verwendet wird, sonst False.
def used_in_col(grid, col, num):
    pass

# Testet, ob die Zahl 3 bereits in der zweiten Spalte des Sudoku-Feldes verwendet wird.
assert used_in_col(grid, 1, 3) == True

# Testet, ob die Zahl 9 nicht in der zweiten Spalte des Sudoku-Feldes verwendet wird.
assert used_in_col(grid, 1, 9) == False


''' Teilaufgabe 3: used_in_box '''

# Gibt True zurück, falls die gegeben Zahl num bereits im
# spefizierten 3x3-Quadrat schon vorkommt, False sonst.
# Die Parameter boxStartRow und boxStartCol haben die Werte 0, 3 oder 6.
def used_in_box(grid, boxStartRow, boxStartCol, num):
    pass

# Testet, ob die Zahl 7 im obersten Quadrat im Sudoku-Feld verwendet wird.
assert used_in_box(grid, 0, 0, 7) == True
# Testet, ob die Zahl 9 nicht im obersten Quadrat im Sudoku-Feld verwendet wird.
assert used_in_box(grid, 0, 0, 9) == False


''' Teilaufgabe 4: is_safe '''

# Git True zurück, falls die gebene Zahl num in an die Zeile/Spalte gesetzt werden kann, sonst False.
# Die Methode prüft, ob die Zahl nicht bereits in der Zeile, Spalte oder im Quadrat vorkommt.
def is_safe(grid, row, col, num):
    pass

assert is_safe(grid, 4, 1, 9) == False
assert is_safe(grid, 4, 1, 1) == True


''' Teilaufgabe 5: find_unassigned_location '''

# Sucht auf dem Spielfeld nach einem nicht besetzten Feld.
# Falls ein nicht besetztes Feld gefunden wird, werden die Koordinaten als Tuple zurückgegeben.
# Falls alle Felder besetzt sind, wird None zurückgegeben.
def find_unassigned_location(grid):
    pass

assert find_unassigned_location(grid) == (0, 1)


