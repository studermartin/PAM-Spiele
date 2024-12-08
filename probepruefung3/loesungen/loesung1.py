'''
Aufgabe 1: Klasse für Schülerinnen und Schüler

Schülerinnen und Schüler am GKD sollen erfasst werden.
Für Schülerinnen und Schüler sollen folgende Werte gespeichert werden:
- Vorname, Nachname
- Alter
- Klasse (1, 2 usw. für 1G, 2G usw.)
- Eine Liste mit Noten

Implementiere die 3 Teilaufgaben als Methode in der Klasse SuS.
Die Benutzung ist im Programm ersichtlich.

'''

class SuS:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def print(self):
        print(self.vorname, self.nachname, "Alter:", self.alter, "Klasse:", self.klasse, "Noten:", self.noten)

    def notendurchschnitt(self):
        return sum(self.noten)/len(self.noten)


# Teilaufgabe 1: Konstruktor
anna = SuS("Anna", "Arpagaus")
anna.alter = 16
anna.klasse = 4
anna.noten = [4, 5, 6]

fritz = SuS("Fritz", "Fischer")
fritz.alter = 15
fritz.klasse = 3
fritz.noten = [3, 3.5, 2.5]

# Teilaufgabe 2: print-Methode
# Erwartete Ausgabe: Anna Arpagaus Alter: 16 Klasse: 4 Noten: [4, 5, 5.5]
anna.print()
# Erwartete Ausgabe: Fritz Fischer Alter: 15 Klasse: 3 Noten: [3, 3.5, 3]
fritz.print()

# Teilaufgabe 3: Methode notendurchschnitt
assert anna.notendurchschnitt() == 5
assert fritz.notendurchschnitt() == 3



