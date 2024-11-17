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
'''


###############################
# Klassen in Python erstellen
###############################

# leere Klasse erstellen
class Bear:
    pass


# Klasse mit Variablen
class Baer:
    alter = 20
    gewicht = 680
    groesse = 250

    def schlafen(self, dauer):
        print("schlafe", str(dauer), "Minuten")

    def fressen(self):
        print("fressen")

# Klassen sind wie Baupläne.
# Wir haben noch keine Bären erzeugt.


###############################
# Mit Python Klassen verschiedene Typen erzeugen
###############################

bruno = Baer()
bruno.fressen()
bruno.schlafen(30)
print("Bruno ist", bruno.alter, "Jahre alt.")

balu = Baer()
balu. schlafen(50)

# Ändern der Attributwert
balu.alter = 18
print("Balu ist", balu.alter, "Jahre alt.")
print("Bruno ist", bruno.alter, "Jahre alt.")

# Language Specification:
# 3.2.11. Class instances: https://docs.python.org/3/reference/datamodel.html#id4
# 6.3.1. Attribute references: https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-attributeref
# Inhalt der Klasse oder eines Objektes ausgeben: print(Baer.__dict__) oder print(bruno.__dict__)


# Achtung: 
# Die Attribute alter, gewicht und groesse sind aktuell am falschen Ort. 
# Sie sind auf der Klasse gespeichert, nicht im Objekt selbst.
# Wir erzeugen einen Bären resp. eine Bärin, und setzen dann die Attributwert.
anja = Baer()
anja.alter = 5
print(anja.__dict__)

###############################
# Bauen mit Parametern: Konstruktor
###############################

# Wir wollen die Werte für das Alter, das Gewicht und die Grösse gleich am Anfang festlegen.
# Bei der Erzeugung wollen wir diese mitgeben:
#   anja = Bear(5, 200, 150)
# Dazu schreiben wir einen Konstruktor. In Python durch eine Methode mit dem speziellen Namen __init__

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
