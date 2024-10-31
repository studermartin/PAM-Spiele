from ttt.loesungen.ttt_spiel_1 import uberpruefe_spielstand, KREUZ, KREIS, LEER, pruefe_zug

# Spielfeld in Anfangskonfiguration
spielfeld1 = [[LEER] * 3, [LEER] * 3,[LEER] * 3]
assert uberpruefe_spielstand(spielfeld1) == LEER

assert pruefe_zug(spielfeld1, 0, 0)==False
assert pruefe_zug(spielfeld1, 1, 1)==True


# Spielfeld mit 3 Kreuzen in letzter Spalte
spielfeld_3_kreuze_in_letzter_spalte= [
    [LEER, LEER,  KREUZ],
    [LEER, KREIS, KREUZ],
    [KREIS,KREIS, KREUZ]]
assert uberpruefe_spielstand(spielfeld_3_kreuze_in_letzter_spalte) == KREUZ

assert pruefe_zug(spielfeld_3_kreuze_in_letzter_spalte, 1, 1) == True
assert pruefe_zug(spielfeld_3_kreuze_in_letzter_spalte, 3, 1) == False

# Spielfeld mit 3 Kreisen Diagonale von rechts oben nach links unten
spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten = [
    [LEER,  KREUZ, KREIS],
    [KREUZ, KREIS, KREUZ],
    [KREIS, KREIS, KREUZ]]
assert uberpruefe_spielstand(spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten)== KREIS

