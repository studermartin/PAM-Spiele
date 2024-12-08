''' 
Aufgabe 2: Bäume

Du hast im Unterricht die Implementation einer Baumstruktur mit Hilfe der Klasse Knoten kennengelernt.

Implementiere der Reihe nach die Teilaufgaben.

Die assert-Anweisungen geben eine Rückmeldung darüber, ob deine Implementation korrekt ist. 
Tritt ein Fehler auf (AssertionError), dann ist sie nicht korrekt. 
Tritt kein Fehler auf, ist die Implementation auf einem guten Weg.


'''

class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.kinder = []

    def beschreibung(self):
        return "Knoten mit Wert " + str(self.wert) + " hat " + str(len(self.kinder)) + " Kind(er)."
    
    def print_teilbaum(self, tiefe):
        print(" "*tiefe, self.beschreibung())
        for kind in self.kinder:
            kind.print_teilbaum(tiefe + 1)

    def anzahl(self):
        anzahl = 0
        for kind in self.kinder:
            anzahl += kind.anzahl()
        return anzahl+1

    def summe(self):
        summe = 0
        for kind in self.kinder:
            summe += kind.summe()
        return summe + self.wert
        
    def ist_blatt(self):
        return len(self.kinder) == 0

    def anzahl_kinder(self):
        return len(self.kinder)
        pass    # Teilaufgabe 1

    def hoehe(self):
        if self.ist_blatt():
            return 0
        else:
            max_hoehe_der_kinder = 0
            for kind in self.kinder:
                hoehe_kind = kind.hoehe()
                if hoehe_kind>max_hoehe_der_kinder:
                    max_hoehe_der_kinder = hoehe_kind
            return max_hoehe_der_kinder+1
        pass    # Teilaufgabe 2

wurzel = Knoten(1)
kind1 = Knoten(2)
wurzel.kinder.append(kind1)
kind2 = Knoten(4)
wurzel.kinder.append(kind2)
kind2_1 = Knoten(5)
kind2.kinder.append(kind2_1)

wurzel.print_teilbaum(0)
assert wurzel.anzahl() == 4
assert wurzel.summe() == 12



''' Teilaufgabe 1: Anzahl Kinder (nicht rekursiv) '''

# Implementiere eine Methode, die die Anzahl Kinder eines Knotens (nicht des ganzen Teilbaumes) zurückgibt.

assert wurzel.anzahl_kinder() == 2
assert kind1.anzahl_kinder() == 0


''' Teilaufgabe 2: Höhe des Baumes (rekursiv) '''

# Implementiere eine Methode, die die Höhe des Baumes zurückgibt.
# Ein Baum nur mit einem Wurzelknoten hat die Höhe 0.
# Der vorliegende Baum hat die Höhe 2.
# Hinweis: 
# - Nutzen die Methode anzahl oder summe als Vorlage benutzen.

assert kind2_1.hoehe() == 0
assert kind2.hoehe() == 1
assert wurzel.hoehe() == 2





