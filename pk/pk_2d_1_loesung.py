'''
Voraussetzungen
- Du kannst in Python eine Liste (mit Zahlen) erstellen.
- Du kannst in Python Elemente an einer bestimmten Stelle den Wert lesen sowie den Wert in die Liste schreiben.
- Du kannst in Python mit Hilfe von Schleifen alle Elemente einer Liste durchlaufen.

Lernziel
- Du weisst, wie man mit Hilfe von verschachtelten Listen eine 2-dimensionale Datenstruktur mit Zeilen und Spalten, beispielsweise ein Schachbrett, darstellt.
- Du weisst, wie man mit Hilfe eines Zeilen- und Spaltenindex einen Wert auf der Datenstruktur liest resp. einen Wert in Datenstruktur schreibt.
- Du weisst, wie man mit Schleifen alle Elemente einer Zeile, Spalte oder Diagonalen durchläuft.
'''


''' Repetition: Listen'''

# Liste mit Zahlen erzeugen
liste = [ 4, 9, 5]

# Liste ausgeben
print(liste)

# Wert an Index 1 (=2. Stelle) lesen und danach ausgeben
wert_an_stelle_1 = liste[1]
print(wert_an_stelle_1)

# Wert 13 an Index 2 (=3. Stelle) schreiben und die Liste zur Kontrolle ausgeben
liste[1] = 13
print(liste)

# Alle Elemente der Liste mit einer while-Schleife durchlaufen und ausgeben
index = 0
while index < len(liste):
    print(liste[index])
    index += 1

# Alle Elemente der Liste mit einer for-Schleife durchlaufen und ausgeben
for wert in liste:
    print(wert)



''' Verschachtelung von Listen '''
''' 
Liste können nicht nur Werte, Zahlen, Texte usw. enthalten, sondern auch wieder Listen.
'''

# Liste von Listen mit Zahlen:
# Die Liste mit dem Namen liste_von_listen enthält drei Elemente, welche wiederum Listen sind.
# Das Listenelement liste_von_listen[0] ist die Liste [1, 2, 3], das Listenelement an der Stelle liste_von_listen[1] ist die Liste [4, 5, 6] usw.
liste_von_listen = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Ausgabe von Listen von Listen:
# Die Ausgabe ist analog zur Erzeugung der Liste wie folgt: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(liste_von_listen)

# Lesen von Werten:
# Die Zahl 6 erhalte ich wie folgt:
# 1. Über liste_von_listen[1] erhalte ich die Liste [4, 5, 6].
# 2. In der resultierenden Liste [4, 5, 6] greife ich mit [2] auf das letzte Element zu.
zweite_innere_liste = liste_von_listen[1]
wert6 = zweite_innere_liste[2]
print(wert6)

# Kurzschreibweise für den Zugriff:
# Derselbe Zugriff lässt sich wie folgt kurz schreiben:
wert6 = liste_von_listen[1][2]
print(wert6)

# Schreiben von Werten:
# Überdieselbe Kurzschreibweise lässt sich ein Wert ändern.
liste_von_listen[1][2] = 13
print(liste_von_listen)

# Achtung:
# Die Struktur, nämlich eine Liste mit Listen lässt sich einfach "zerstören".
liste_von_listen[1] = 21
print(liste_von_listen)


''' 2-dimensionale Datenstrukturen '''
''' 
Verschachtelte Listen lassen sich als 2-dimensionale Datenstrukturen mit einer Anzahl von Zeilen und Spalten auffassen.
Bei den Zugriffen auf die Elemente in der verschachtelten Liste fasst man den ersten Index als Zeilenindex, den zweiten Index als Spaltenindex auf.
In der Anweisung
    print(liste_von_listen[1][2])
wäre als die 1 in [1] die Angabe der Zeile, die 2 in [2] die Angabe der Spalte.
Anstatt
    liste_von_listen = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
kann man die Erzeung auch anschaulicher wie folgt schreiben:
    liste_von_listen = 
        [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
'''
drei_mal_drei_feld = [  [1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]]

# Lesen des Werts im Feld in der 1. Zeile (Zeilenindex = 0) und 3. Spalten (Spaltenindex = 2)
wert3 = drei_mal_drei_feld[0][2]
print(wert3)

# Schreiben des Werts 13 in die 3. Spalte und 2. Zeile
drei_mal_drei_feld[2][1] = 13
print(drei_mal_drei_feld)

# Ausgabe der 2. Zeile:
spalte = 0
while spalte < 3:
    print(drei_mal_drei_feld[1][spalte])
    spalte += 1

# Ausgabe der letzten Spalte:
zeile = 0
while zeile < 3:
    print(drei_mal_drei_feld[zeile][2])
    zeile += 1

# Ausgabe der 2. Zeile auf einer Zeile
spalte = 0
zeilentext = ""
while spalte < 3:
    zeilentext += " " + str(drei_mal_drei_feld[1][spalte])  # str wandelt die Zahl in einen Text um
    spalte += 1
print(zeilentext)

# Ausage des ganzen Feldes
zeile = 0
while zeile < 3:
    spalte = 0
    zeilentext = ""
    while spalte < 3:
        zeilentext += " " + str(drei_mal_drei_feld[zeile][spalte])  # str wandelt die Zahl in einen Text um
        spalte += 1
    print(zeilentext)
    zeile += 1


''' Aufgaben '''
print("\n\nAufgaben")

# Gegeben ist ein quadratisches Feld mit Seitenlänge 2
# Das quadratische Feld hat irgendwelche Werte (im Beispiel die Zahlen 1-4).
# Ihre Lösungen sollen unahbängig von den konkreten Werten funktionieren.
feld2x2 = [ [1, 2], [3, 4]]


# Aufgabe 1: Ausgabe
# Schreibe einen Befehle ausgaben2x2, der das quadratische Feld in quadratischer Form ausgibt
# Aufruf:
#  ausgaben2x2(feld2x2)
# Erwartetes Resultat:
#  1 2
#  3 4
print("\nAufgabe 1")

# Lösung Aufgabe 1:
def ausgaben2x2(feld2x2):
    zeile = 0
    while zeile < len(feld2x2):
        spalte = 0
        zeilentext = ""
        while spalte < len(feld2x2):
            zeilentext += " " + str(feld2x2[zeile][spalte])  # str wandelt die Zahl in einen Text um
            spalte += 1
        print(zeilentext)
        zeile += 1

ausgaben2x2(feld2x2)


# Aufgabe 2: Summe aller Elemente
# Schreibe einen Befehl summe2x2, der alle Werte im Feld summiert und ausgibt
# Aufruf:
#  summe2x2(feld2x2)
# Erwartetes Resultat:
#  10
print("\nAufgabe 2")

# Lösung Aufgabe 2:
def summe2x2(feld2x2):
    summe = 0
    zeile = 0
    while zeile < len(feld2x2):
        spalte = 0
        while spalte < len(feld2x2):
            summe += feld2x2[zeile][spalte]
            spalte += 1
        zeile += 1
    print(summe)

summe2x2(feld2x2)


# Aufgabe 3: Wert ändern
# Schreibe einen Befehl wert2x2, der den Wert an der gegebenen Stelle ändert
# Aufruf:
#  wert2x2(feld2x2, 1, 2, 11)   # Schreibe den Wert 11 in Zeile 1 und Spalte 2 ins Feld
# Erwartetes Resultat von print(feld2x2):
#   [[1, 11], [3, 4]]
print("\nAufgabe 3")

# Lösung Aufgabe 3:
def wert2x2(feld2x2, zeile, spalte, wert):
    feld2x2[zeile-1][spalte-1] = wert

wert2x2(feld2x2, 1, 2, 11)
print(feld2x2)


# Aufgabe 4: Wert suchen
# Schreibe einen Befehl suche2x2, der prüft, ob ein Wert im Feld vorkommt.
# Das Resultat wird ausgegeben-
# Aufruf:
#  suche2x2(feld2x2, 3)   # Suche den Wert 3 im Feld 
#  suche2x2(feld2x2, -1)
# Erwartetes Resultat:
#   Die Zahl 3 kommt in Zeile 2 / Spalte 1 vor.
#   Die Zahl -1 kommt nicht vor.
print("\nAufgabe 4")

# Lösung Aufgabe 4:
def suche2x2(feld2x2, wert):
    gefunden = False
    zeile = 0
    while zeile < len(feld2x2):
        spalte = 0
        while spalte < len(feld2x2):
            if wert == feld2x2[zeile][spalte]:
                gefunden = True
                break
            spalte += 1
        if gefunden:
            break
        zeile += 1
    if gefunden:
        print("Die Zahl", wert, "kommt in Zeile", zeile+1, "/ Spalte", spalte+1, "vor.")
    else:
        print("Die Zahl", wert, "kommt nicht vor.")
    
suche2x2(feld2x2, 3)
suche2x2(feld2x2, -1)


