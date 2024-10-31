'''
Voraussetzungen:
- 2D-Datenstrukturen (Listen in Listen)
- Funktionen

Lernziel:
- Implementation eines 3-TTT (Spieler gegen Spieler)
'''

'''
Eine Konfiguration von 3-TTT besteht aus dem 3x3-Spielfeld sowie der Angabe, welcher Spieler am Zug ist. Die Felder des Spielfeldes sind entweder leer oder enthalten das Zeichen Kreuz oder Kreis.

In Python kann das Spielfeld durch eine 2D-Datenstruktur modelliert werden.
Zu Beginn ist das Spielfeld leer (hier mit dem Zeichen _ dargestellt).
'''
spielfeld = [ [ "_", "_", "_"], [ "_", "_", "_"], [ "_", "_", "_"]]

'''
Der Spieler A setzt ein Kreuz in der Mitte:
'''

spielfeld[1][1] = "X"

'''
Danach setzt der Spiel B einen Kreis oben links.
'''

spielfeld[0][0] = "O"


#####################################################
''' Teilaufgabe 1: Befehl print_spielfeld

Der Befehl print_spielfeld soll das Spielfeld in hübscher Form ausgeben.
In der aktuellen Situation also beispielsweise wie folgt:
	O _ _
	_ X _
	_ _ _
 '''

def print_spielfeld(spielfeld):
	# Ihre Lösung hier (pass soll gelöscht werden)
    pass
	
	
'''
Möchte man das Spiel am Computer spielen, muss man prüfen, ob der Zug auch gültig ist.
Gültig ist ein Zug, wenn das Feld noch nicht besetzt ist.
'''

#####################################################
''' Teilaufgabe 2: Funktion pruefe_zug

Die Funktion pruefe_zug erhält ein Spielfeld sowie die Angabe der Zeile/Spalte (eine Zahl zwischen 1 und 3), an welcher ein Zeichen gesetzt werden soll. Falls der Zug gültig ist, soll die Funktion True, ansonsten False zurückgeben.
'''

def pruefe_zug(spielfeld, zeile, spalte):
	# Ihre Lösung hier (pass soll gelöscht werden)
    pass

'''
In der aktuellen Situation soll der Funktion für folgende Aufrufe True zurückgeben.
'''
print(pruefe_zug(spielfeld, 1, 2))
print(pruefe_zug(spielfeld, 3, 3))

'''
Für folgende Aufrufe aber False:
'''
print(pruefe_zug(spielfeld, 2, 2))  # Mitte ist besetzt
print(pruefe_zug(spielfeld, 0, 1))  # 0 ist eine ungültige Zeilenangabe


#####################################################
''' Teilaufgabe 3: Funktion uberpruefe_spielstand

Die Funktion ueberpruefe_spielstand soll prüfen, ob eine Endkonfiguration vorliegt.
Eine Endkonfiguration liegt vor, wenn eine Gewinnlinie, also drei gleiche Zeichen in einer Zeile, Spalte oder eine der Diagonalen, vorkommt. Die Funktion soll das Zeichen zurückgeben, aus welchem die Gewinnlinie besteht.
'''

def uberpruefe_spielstand(spielfeld):
	# Ihre Lösung hier (pass soll gelöscht werden)
    pass

'''
Für das folgende Spielfeld soll die Funktion beispielsweise "X" zurückgeben.
'''
spielfeld_3_kreuze_in_letzter_spalte = [
    ["_", "_",  "X"],
    ["_", "O", "X"],
    ["O", "O", "X"]]
print(uberpruefe_spielstand(spielfeld_3_kreuze_in_letzter_spalte))

'''
Für das folgende Spielfeld soll die Funktion "O" zurückgeben.
'''
spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten = [
    ["_", "X", "O"],
    ["X", "O", "X"],
    ["O", "O", "X"]]
print(uberpruefe_spielstand(spielfeld_3_kreise_in_diagonale_linksoben_rechtsunten))



#####################################################
''' Teilaufgabe 4: Spiel implementieren
Jetzt hast du alle Elemente, um das Spiel zu implementieren. Das Spiel besteht aus folgenden Schritten:
1. Spielfels ausgeben
Tipp: Teilaufgabe 1
2. Spieler A um einen Zug bitten (je eine Eingabe für Zeile und Spalte)
Tipp: zeile = input("Bitte Zeile eingeben")
3. Prüfen, ob der Zug gültig ist 
Tipp: Teilaufgabe 2
4. Zug durchführen
5. Prüfen, ob eine Gewinnzeile vorliegt
Tipp: Teilaufgabe 3

Die Schritte müssen für den Spieler B wiederholt und danach für beide wiederholt werden, bis eine Gewinnzeile vorliegt.

'''




