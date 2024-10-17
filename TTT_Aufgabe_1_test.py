from TTT_Aufgabe_1 import spielstand, KREUZ, KREIS, LEER

spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten = [
    [LEER,  KREUZ, KREIS],
    [KREUZ, KREIS, KREUZ],
    [KREIS, KREIS, KREUZ]]
print("Spielfeld mit 3 Kreisen Diagonale von rechts oben nach links unten: ", )

assert spielstand(spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten)== KREIS
