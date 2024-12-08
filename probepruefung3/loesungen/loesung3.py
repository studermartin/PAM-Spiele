''' 
Aufgabe 3: Bäume

Du hast im Unterricht die Implementation einer Baumstruktur mit Hilfe der Klasse Knoten kennengelernt.
In der Implementation konnte jeder Knoten mehrere Kind-Knoten haben.

Ein binärer Baum hat nur zwei Kindknoten, einen linken und einen rechten Kindknoten.
Sehr oft genügt es aber, dass nur zwei Kindknoten möglich sind. Es handelt sich dann um einen binärem Baum.
Anstatt das Attribute kinder gibt es neu zwei Kindknoten linkesKind und rechtesKind.

Die assert-Anweisungen geben eine Rückmeldung darüber, ob deine Implementation korrekt ist. 
Tritt ein Fehler auf (AssertionError), dann ist sie nicht korrekt. 
Tritt kein Fehler auf, ist die Implementation auf einem guten Weg.

Beim Erzeugen eines Knotens hat dieser noch kein linkes oder rechtes Kind.
Die Attribute werden mit dem Wert None initialisiert.
Um zu bestimmen, ob ein Knoten ein linkes oder rechtes Kind hat, wird den Attributen zuerst der Wert None zugewiesen.
Die Assert-Anweisungen zeigen die Benutzung des Wertes None.


'''

class Knoten:
    def __init__(self, wert):
        self.wert = wert
        self.linkesKind = None
        self.rechtesKind = None

    # Ausgabe: Knoten mit Wert <Wert> hat <Anzahl Kinder> Kinder(er).""
    def beschreibung(self):
        return "Knoten mit Wert " + str(self.wert) + " hat " + str(self.anzahl_kinder()) + " Kind(er)."
    
    def anzahl_kinder(self):
        anzahl = 0
        if self.linkesKind != None:
            anzahl += 1
        if self.rechtesKind!= None:
            anzahl += 1
        return anzahl

    def print_teilbaum(self, tiefe):
        print(" "*tiefe, self.beschreibung())
        if self.linkesKind != None:
            self.linkesKind.print_teilbaum(tiefe + 1)
        if self.rechtesKind!= None:
            self.rechtesKind.print_teilbaum(tiefe + 1)

    def anzahl(self):
        anzahl = 0
        if self.linkesKind != None:
            anzahl += self.linkesKind.anzahl()
        if self.rechtesKind!= None:
            anzahl += self.rechtesKind.anzahl()
        return anzahl+1

    def summe(self):
        summe = 0
        if self.linkesKind != None:
            summe += self.linkesKind.summe()
        if self.rechtesKind!= None:
            summe += self.rechtesKind.summe()
        return summe + self.wert
        
    def ist_blatt(self):
        return self.linkesKind == None and self.rechtesKind == None


wurzel = Knoten(1)
assert wurzel.linkesKind == None
assert wurzel.rechtesKind == None

kind1 = Knoten(2)
wurzel.linkesKind = kind1
assert wurzel.linkesKind != None
assert wurzel.rechtesKind == None


kind2 = Knoten(4)
wurzel.rechtesKind = kind2
kind2_1 = Knoten(5)
kind2.linkesKind = kind2_1

wurzel.print_teilbaum(0)
assert wurzel.anzahl_kinder() == 2
assert kind1.anzahl_kinder() == 0
assert wurzel.anzahl() == 4
assert wurzel.summe() == 12


