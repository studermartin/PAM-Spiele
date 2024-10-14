from random import random
# Start Konfiguration
spieler_am_zug = True
anzahl_streichhoelzer = 7

while anzahl_streichhoelzer>0:
    print()
    print("Auf dem Tisch liegen", anzahl_streichhoelzer, "Streichhölzer:", "|"*anzahl_streichhoelzer)
    print("Du bist am Zug.")

    try:
        nimm = int(input("Wieviele Streichhölzer möchtest du nehmen? "))
    except ValueError:
        nimm = -1

    # Prüfe, ob der Zug gültig ist, d. h. die zu nehmende Anzahl Streichhölzer zwischen 1 und 3 liegt
    while nimm<1 or nimm>3:
        print("Die eingegebene Anzahl ist ungültig.")
        try:
            nimm = int(input("Wieviele Streichhölzer möchtest du nehmen? "))
        except ValueError:
            nimm = -1
    anzahl_streichhoelzer -= nimm

    spieler_am_zug = False
    if (anzahl_streichhoelzer==0):
        break
    
    # Computerzug mit folgender Strategie:
    # 1. Gewinnzug: Falls 3 oder weniger Streichhölzer vorliegen, nimmt diese.
    # 2. Gewinnzug: 
    #    - Wenn möglich, sowieviele Streichhölzer nehmen, dass die Anzahl Streichhölzer ein Vielfaches von 4 ist.
    #      Das gelingt nur, wenn die Anzahl Streichhölzer aktuell kein vielfaches von 4 ist.
    # 3. Kein Gewinnzug möglich: zufällig zwischen 1 und 3 Streichhölzer nehmen.

    print()
    print("Auf dem Tisch liegen", anzahl_streichhoelzer, "Streichhölzer:", "|"*anzahl_streichhoelzer)
    
    if anzahl_streichhoelzer <= 3:
        nimm = anzahl_streichhoelzer
    elif anzahl_streichhoelzer % 4 != 0:
        nimm = anzahl_streichhoelzer % 4
    else:
        nimm = int(random()*3)+1
    print("Ich nehme", nimm, "Streichholz/Streichhölzer.")
    anzahl_streichhoelzer -= nimm

    spieler_am_zug = True

print()
if spieler_am_zug:
    print("Ich gewinne.")
else:
    print("Du gewinnst. Gratuliere!")