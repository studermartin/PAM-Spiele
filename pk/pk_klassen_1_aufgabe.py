'''
Voraussetzungen
- Du kannst in Python eine Liste (mit Zahlen) erstellen.
- Du kannst in Python Elemente an einer bestimmten Stelle den Wert lesen sowie den Wert in die Liste schreiben.
- Du kannst in Python mit Hilfe von Schleifen alle Elemente einer Liste durchlaufen.

Lernziel
- Du verstehst, wie man mit Hilfe von Klassen Baupläne für Objekte definiert.
- Du verstehst, wie Instanzen von Klassen erzeugt, Methoden aufruft und Attribute nutzt.
'''


''' Einführung '''
''' 
Im Internet gibt es verschiedene Einführungen zu Klassen.
Im folgenden wollen wir https://www.sivakids.de/python-klassen/ nutzen.
Bitte lies die Einführung bis vor das Kapitel "Klassen in Python: Vererbung".
Nachfolgend findest du den Code am Schluss des Textes.
'''

class Baer:
    def __init__(self, alter, gewicht, groesse):
        self.alter = alter
        self.gewicht = gewicht
        self.grosse = groesse
    
    def schlafen(self, dauer):
        print("Schlafe " + str(dauer) + "Minuten")

    def fressen(self):
        print("fressen")

bruno = Baer(20, 300, 200)
balu = Baer(30, 320, 190)

print(bruno.alter)
print(balu.alter)

''' Zusammenfassung:
Klassen ermöglichen und Daten zu Objekten (hier Alter, Gewicht und Grösse) sowie die dazugehörigen Methoden (hier schlafen und fressen) passend zu gruppieren.
'''


''' Aufgabe '''
# tbd.
