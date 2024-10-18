# Start Konfiguration
spieler_am_zug = "A"
anzahl_streichhoelzer = 7

while anzahl_streichhoelzer>0:
    print()
    print("Auf dem Tisch liegen", anzahl_streichhoelzer, "Streichhölzer:", "|"*anzahl_streichhoelzer)
    print("Spieler", spieler_am_zug, "ist am Zug.")

    nimm = int(input("Wieviele Streichhölzer möchtest du nehmen? "))

    # Prüfe, ob der Zug gültig ist, d. h. die zu nehmende Anzahl Streichhölzer zwischen 1 und 3 liegt
    while nimm<1 or nimm>3:
        print("Spieler", spieler_am_zug, ": Die eingegebene Anzahl ist ungültig.")
        nimm = ("Spieler", spieler_am_zug, ": Wieviele Streichhölzer möchtest du nehmen? ")

    anzahl_streichhoelzer -= nimm
    if spieler_am_zug=="A":
        spieler_am_zug = "B"
    else:
        spieler_am_zug = "A"

print()
if spieler_am_zug=="A":
    print("Spieler B hat gewonnen.")
else:
    print("Spieler A hat gewonnen.")