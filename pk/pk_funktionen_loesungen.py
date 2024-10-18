'''
Voraussetzungen
- Du kannst in Python Befehle/Prozeduren mit Parametern implementieren.

Lernziel
- Du kannst in Python eine Funktion mit einem Rückgabewert implementieren.
- Du weisst, was die Anweisung return in einer Funktion bewirkt.
'''


''' Rückblick
Selbst definierte Befehle/Prozeduren können umfangreiche Berechnungen durchführen.
Ihr Resultat können sie mittels der Anweisung print ausgaben.
Die vordefinierten Funktionen schreiben ihr Resultat typischerweise aber nicht mittels print aus,
sondern das Resultat wird zurückgegeben und kann weiterverwendet werden.
'''

# Nutzung der vordefinierten Funktion abs zur Berechnung des Betrags einer Zahl.
abs(-7)             # keine Ausgabe, nur Berechnung

abs_von_7 = abs(-7)    # Berechnung und Speichern der Funktion in der Variablen betrag
print(abs_von_7)       

# Versuchen wir, die Funktion abs selbst zu implementieren
def betrag(wert):
    if wert<0:
        print(-wert)
    else:
        print(wert)

betrag(-7)

# Unsere Befehl gibt nur das Resultat aus, gibt aber keinen Wert zurück
betrag_von_7 = betrag(-7)
print(betrag_von_7)         # Ausgabe ist None


''' Funktionen
Ein Befehl kann einen Rückgabewert haben.
Den Rückgabewert geben wir mit dem Schlüsswort "return" an.
Trifft der Computer auf return, dann wertet er den Ausdruck rechts davon aus, der Rückgabewert, und beendet den Befehl sofort.
'''

def betrag(wert):
    if wert<0:
        return -wert
    else:
        return wert

betrag_von_7 = betrag(-7)   # Der Rückgabewert, der Betrag, wird in der Variablen betrag_von_7 gespeichert.
print(betrag_von_7)


''' Aufgaben '''

''' Aufgabe 1: Additionsfunktion 
Schreibe eine Funktion addiere, die zwei Zahlen addiert und die Summe zurückgibt.
Also Vorlage hier der Additionsbefehl, der zwei Zahlen addiert und die Summe ausgibt.
    def addiere(zahl1, zahl2):
        print(zahl1 + zahl2)
Ändere den Befehl addiere so, dass er das Resultat nicht ausgibt, sondern zurückgibt.

Der Aufruf von 
    summe = addiere(6, 4))
    print(summe)
soll 10 ausgeben.
'''

''' Lösung Aufgabe 1 '''
def addiere(zahl1, zahl2):
    return zahl1 + zahl2

summe = addiere(6, 4)
print(summe)


''' Aufgabe 2: Zahlen in einer Liste suchen 
Schreibe eine Funktion suche, die prüft, ob eine Zahl in einer Liste von Zahlen vorkommt.
Sie soll als Resultat den Index der STelle zurückgeben, an welcher die Zahl das erste mal vorkommt.
Falls die Zahl nicht vorkommt, soll die die Funktion -1 zurückgeben.

Der Aufruf von 
  suche([1, 3, 5], 3)
sucht die Zahl 5 in der Liste. Die Zahl 5 kommt an der STelle mit Index 1 vor. Die Funktion soll also 1 zurückgeben.
'''

''' Lösung Aufgabe 2 '''
def suche(liste, zahl):
    index = 0
    while index<len(liste):
        if zahl == liste[index]:
            return index
        index += 1
    return -1

print(suche([1, 3, 5], 3))
