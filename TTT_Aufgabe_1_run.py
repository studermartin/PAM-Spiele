from TTT_Aufgabe_1 import *

spielfeld = [[LEER] * 3, [LEER] * 3, [LEER] * 3]
spieler_am_zug = SPIELER_A

stand = uberpruefe_spielstand(spielfeld)
while stand == LEER:
    print("Spieler", spieler_am_zug, "ist am Zug")
    zeile = int(input("Bitte Zeile eingeben (1 - 3): "))
    spalte = int(input("Bitte Spalte eingeben (1 - 3): "))
    while not pruefe_zug(spielfeld, zeile, spalte):
        print(
            "Eingabe ungültig. Falsche Zeilen-/Spaltennummern oder Feld besetzt. Bitte wiederholen."
        )
        zeile = int(input("Bitte Zeile eingeben (1 - 3): "))
        spalte = int(input("Bitte Spalte eingeben (1 - 3): "))

    spielfeld[zeile - 1][spalte - 1] = spieler_am_zug

    print_spielfeld(spielfeld)

    if spieler_am_zug == KREIS:
        spieler_am_zug = KREUZ
    else:
        spieler_am_zug = KREIS
    stand = uberpruefe_spielstand(spielfeld)

print("Spieler ", uberpruefe_spielstand(spielfeld), "hat gewonnen.")
