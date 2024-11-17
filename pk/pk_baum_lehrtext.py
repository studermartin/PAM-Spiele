

# Bäume bestehen aus Knoten. 
# Typischerweise ist der Baum umgekehrt dargestellt: Die Äste gehen nach unten.
# Den obersten Knoten nennt man Wurzel.
# Die untersten Knoten Blätter.
# Die Knoten enthalten Werte.

class Knoten:
    def __init__(self, wert):
        self.wert = wert

    def print(self):
        print("Knoten mit Wert", self.wert, ".")

wurzel = Knoten(5)
wurzel.print()


#######################
# Verhängen von Knoten (Kinder)
#######################

# Der Vater-Knoten merkt sich die Kind-Knoten.
class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.kinder = []

    def print(self):
        print("Knoten mit Wert", self.wert, "hat ", len(self.kinder) ,"Kind(er).")

wurzel = Knoten(5)
wurzel.print()

knoten1 = Knoten(10)
wurzel.kinder.append(knoten1)
wurzel.print()


#####################################
print("\n\n### Alle Knoten ausgeben\n\n")

# Sich alle erzeugten Knoten merken
baum = [wurzel, knoten1]
print("Alle erzeugten Knoten ausgeben:")
for knoten in baum:
    knoten.print()


# print-Methoode ergänzen
class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.kinder = []

    def print(self):
        print("Knoten mit Wert", self.wert, "hat ", len(self.kinder) ,"Kind(er).")
        for kind in self.kinder:
            kind.print()
        
wurzel = Knoten(5)
knoten1 = Knoten(10)
wurzel.kinder.append(knoten1)

print("Baum ausgeben:")
wurzel.print()


#####################################
print("\n\n### Zähle die Anzahl Knoten im Baum\n\n")


# Wir wollen eine Methode, die die Anzahl Knoten im Baum ausgibt
class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.kinder = []

    def print(self):
        print("Knoten mit Wert", self.wert, "hat ", len(self.kinder) ,"Kind(er).")
        for kind in self.kinder:
            kind.print()

    def anzahl(self):
        print(len(self.kinder)+1)

wurzel = Knoten(5)
knoten1 = Knoten(10)
wurzel.kinder.append(knoten1)

print("Der Baum startend mit der Wurzel die folgende Anzahl Knoten:")
wurzel.anzahl()

# Bessere Variante
# Wir wollen eine Methode, die die Anzahl Knoten im Baum zählt
class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.kinder = []

    def print(self):
        print("Knoten mit Wert", self.wert, "hat ", len(self.kinder) ,"Kind(er).")
        for kind in self.kinder:
            kind.print()

    def anzahl(self):
        return len(self.kinder)+1

wurzel = Knoten(5)
knoten1 = Knoten(10)
wurzel.kinder.append(knoten1)

print("Der Baum startend mit der Wurzel die folgende Anzahl Knoten:", wurzel.anzahl())



#####################################
print("\n\n### Auf Blatt prüfen\n\n")

# Wir möchte prüfen, ob ein Knoten ein Blatt ist oder nicht.



#####################################
print("\n\n### Knoten suchen\n\n")

# Wir möchte prüfen, ob ein Knoten ein Blatt ist oder nicht.



#####################################
print("\n\n### Auf Wurzel prüfen\n\n")

# Wir möchte prüfen, ob ein Knoten die Wurzel ist oder nicht.



#####################################
print("\n\n### Verhängen von Knoten (Vater)\n\n")



# alle durchgehen
# rekursiv kein Problem
# navigieren




# Aufgaben


