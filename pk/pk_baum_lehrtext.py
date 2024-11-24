

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


# Aufgabe: hübsche Ausgabe
# Je weiter unten die Knoten im Baum sind, desto mehr einrücken.



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

# Noch ein Knoten
knoten1_1 = Knoten(7)
knoten1.kinder.append(knoten1_1)
wurzel.print()
print("Der Baum startend mit der Wurzel die folgende Anzahl Knoten:", wurzel.anzahl())

# Upps, das stimmt nicht.
# Wie verbessern wir das?

# Aufgabe: Werte im Baum summieren
# Die Knoten haben Werte. Es sollen alle Werte der Knoten im (Teil-)Baum summiert werden.



#####################################
print("\n\n### Auf Blatt prüfen\n\n")

# Wir möchte prüfen, ob ein Knoten ein Blatt ist oder nicht.
#   print(knoten1_1.ist_blatt()) 
# soll TRUE zurückgeben.


#####################################
print("\n\n### Kindknoten mit bestimmtem Wert suchen\n\n")

# Aufgabe: Kindknoten mit bestimmtem Wert suchen



#####################################
print("\n\n### Knoten im Baum mit bestimmtem Wert suchen\n")

# Aufgabe: Kindknoten mit bestimmtem Wert suchen

def erstes_kind_mit_wert(self, wert):
    for kind in self.kinder:
        if kind.wert == wert:
            return kind

Knoten.erstes_kind_mit_wert = erstes_kind_mit_wert
print(wurzel.erstes_kind_mit_wert(10))



#####################################
print("\n\n### Auf Wurzel prüfen\n\n")

# Wir möchte prüfen, ob ein Knoten die Wurzel ist oder nicht.
# Aktuell nicht lösbar!


#####################################
print("\n\n### Verhängen von Knoten (Vater)\n\n")


class Knoten:
    def __init__(self, vater, wert):
        self.vater = vater
        self.wert = wert
        self.kinder = []

    def print(self):
        print("Knoten mit Wert", self.wert, "hat ", len(self.kinder) ,"Kind(er).")
        for kind in self.kinder:
            kind.print()

    def anzahl(self):
        return sum([kind.anzahl() for kind in self.kinder])+1
    
    def ist_wurzel(self):
        return self.vater == None

    def erstes_kind_mit_wert(self, wert):
        for kind in self.kinder:
            if kind.wert == wert:
                return kind



wurzel = Knoten(None, 5)
knoten1 = Knoten(wurzel, 10)
wurzel.kinder.append(knoten1)
print(wurzel.ist_wurzel())
print(wurzel.kinder[0].ist_wurzel())
print(wurzel.kinder[0].vater.ist_wurzel())


#####################################
print("\n\n### Generator-Pattern\n\n")

class Baum:

    def erzeuge_wurzel(self, wert):
        return Knoten(None, wert)
    
    def erzeuge_knoten(self, parent, wert):
        neuer_knoten = Knoten(parent, wert)
        parent.kinder.append(neuer_knoten)
        return neuer_knoten
    
baum = Baum()
wurzel = baum.erzeuge_wurzel(3)
knoten1 = baum.erzeuge_knoten(wurzel, 5)
knoten2 = baum.erzeuge_knoten(wurzel, 10)
knoten3 = baum.erzeuge_knoten(knoten2, -6)

print(wurzel.anzahl())
