
# Spielfeld
LEER = "_"
KREUZ = "X"
KREIS = "O"

def print_spielfeld(spielfeld):
    """ Gibt den Inhalt des Spielfeldes aus
    
    Parameters:
    spielfeld -- das auszugebende Spielfeld
    """
    for zeile in spielfeld:
        zeilen_text=""
        for feld in zeile:
            zeilen_text += feld + " "
        print(zeilen_text)


# Spieler
SPIELER_A = KREUZ
SPIELER_B = KREIS

# Überprüfe den Spielstand
def uberpruefe_spielstand(spielfeld):
    """ Überprüfe den Spielstand
    Eine Schlusskonfiguration liegt vor, wenn drei Kreuze oder drei Kreise in einer Reihe, Spalte oder Diagonale vorliegen.

    Return:
    Gibt X, O oder _ zurück, je nach dem ob Spieler A gewonnen hat, Spieler B gewonnen hat 
    oder noch keine Schlusskonfiguration vorliegt.
    """

    # Prüfe alle Zeilen auf das Vorliegen von drei Kreuzen oder Kreisen
    zeile = 0
    while zeile < 3:
        erster_zeilenwert = spielfeld[zeile][0]
        dreier_in_zeile = True
        spalte = 1
        while spalte < 3:
            if erster_zeilenwert != spielfeld[zeile][spalte]:
                dreier_in_zeile = False
                break
            spalte += 1
        if dreier_in_zeile and erster_zeilenwert != LEER:
            return erster_zeilenwert
        zeile += 1
  
    # Prüfe alle Spalten auf das Vorliegen von drei Kreuzen oder Kreisen
    spalte = 0
    while spalte < 3:
        erster_spaltenwert = spielfeld[0][spalte]
        dreier_in_spalte = True
        zeile = 1
        while zeile < 3:
            if erster_spaltenwert != spielfeld[zeile][spalte]:
                dreier_in_spalte = False
                break
            zeile += 1
        if dreier_in_spalte and erster_spaltenwert != LEER:
            return erster_spaltenwert
        spalte += 1
    
    # Prüfe, ob die Spalte von links oben nach rechts unten drei Kreuzen oder Kreisen enthalten
    dreier_in_diagonale = True
    erster_diagonalenwert = spielfeld[0][0]
    index = 1
    while index < 3:
        if spielfeld[index][index] != erster_diagonalenwert:
            dreier_in_diagonale = False
            break
        index += 1
    if dreier_in_diagonale and erster_diagonalenwert != LEER:
        return erster_diagonalenwert
    
    # Prüfe, ob die Spalte von rechts oben nach links unten drei Kreuzen oder Kreisen enthalten
    dreier_in_diagonale = True
    erster_diagonalenwert = spielfeld[0][3-1]
    index = 1
    while index < 3:
        if spielfeld[index][3-index-1] != erster_diagonalenwert:
            dreier_in_diagonale = False
            break
        index += 1
    if dreier_in_diagonale and erster_diagonalenwert != LEER:
        return erster_diagonalenwert

    return LEER

def pruefe_zug(spielfeld, zeile: int, spalte: int):
    """ Prüft, ob das Setzen eines Kreuzes oder eines Kreises in der angegebenen Zeile und Spalte ein gültiger Zug ist
    """
    zeilen_und_spalten_gueltig:bool = 1 <= zeile and zeile <= 3 and 1 <= spalte and spalte <= 3
    if not(zeilen_und_spalten_gueltig):
        return False
    feld_leer = spielfeld[zeile - 1][spalte - 1] == LEER
    if not (feld_leer):
        return False
    return True