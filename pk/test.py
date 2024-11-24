# Bäume bestehen aus Knoten. 
# Typischerweise ist der Baum umgekehrt dargestellt: Die Äste gehen nach unten.
# Den obersten Knoten nennt man Wurzel.
# Die untersten Knoten Blätter.
# Die Knoten enthalten Werte.

class Knoten:
    def __init__(self,wert):
        self.wert = wert
        self.kinder = [ ]
    
    def beschreibung(self):
        return "Knoten mit Wert " + str(self.wert) + " und " + str(len(self.kinder)) + " Kindern."

    def drucke(self, tiefe=0):
        print(" "*tiefe + self.beschreibung())
        for kind in self.kinder:
            kind.drucke(tiefe+1)
    
    def anzahl(self):
        return 1+sum([kind.anzahl() for kind in self.kinder])

wurzel = Knoten(3)

knoten2 = Knoten(5)
wurzel.kinder.append(knoten2)

knoten3 = Knoten(10)
wurzel.kinder.append(knoten3 )

print(wurzel.wert)
print(wurzel.beschreibung())

wurzel.drucke()

print(wurzel.anzahl())
