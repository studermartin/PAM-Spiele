##################
# Konfiguration
##################

class Nimm_Konfiguration:
    def __init__(self, spieler_am_zug, anzahl_streichhoelzer):
        self.spieler_am_zug = spieler_am_zug
        self.anzahl_streichhoelzer = anzahl_streichhoelzer
        self.gewinnkonfiguration = ""

    def beschreibung(self):
        return "(" + self.spieler_am_zug + ", " + str(self.anzahl_streichhoelzer) + "): " + self.gewinnkonfiguration
    
    def spieler_nicht_am_zug(self):
        if self.spieler_am_zug == "A":
            return "B"
        else:
            return "A"


test_konfiguration = Nimm_Konfiguration("A", 7)
print(test_konfiguration.beschreibung())

#####################################
print("\n\n### Baum\n\n")

class Knoten:
    def __init__(self, konfiguration):
        self.konfiguration = konfiguration
        self.kinder = []

    def print_teilbaum(self, tiefe = 0):
        print(" "*tiefe, self.konfiguration.beschreibung())
        for kind in self.kinder:
            kind.print_teilbaum(tiefe+1)

    def anzahl(self):
        return len(self.kinder)+1


#####################################
print("\n\n### Schritt 1: Startknoten mit Startkonfiguration erzeugen\n\n")

start_konfiguration = Nimm_Konfiguration("A", 7)
wurzel = Knoten(start_konfiguration)


#####################################
print("\n\nSchritt 2: Nachfolgeknoten erzeugen\n\n")


spieler = start_konfiguration.spieler_nicht_am_zug()
zug = 1
while zug <= 3 and zug <= start_konfiguration.anzahl_streichhoelzer:
    konf = Nimm_Konfiguration(spieler, start_konfiguration.anzahl_streichhoelzer-zug)
    neuer_knoten = Knoten(konf)
    wurzel.kinder.append(neuer_knoten)
    zug += 1

wurzel.print_teilbaum()


#####################################
print("\n\nSchritt 2: Nachfolgeknoten erzeugen  als Methode\n\n")

def erzeuge_zuege(self):
    zug = 1
    konfiguration = self.konfiguration
    while zug <= 3 and zug <= konfiguration.anzahl_streichhoelzer:
        konf = Nimm_Konfiguration(konfiguration.spieler_nicht_am_zug(), konfiguration.anzahl_streichhoelzer-zug)
        neuer_knoten = Knoten(konf)
        self.kinder.append(neuer_knoten)
        zug += 1
   
Knoten.erzeuge_zuege = erzeuge_zuege

# alle bereits erzeugten Knoten durchgehen und nochmals Knoten anzähgen


#####################################
print("\n\nBesserer Ansatz: Rekursion\n\n")
 
start_konfiguration = Nimm_Konfiguration("A", 7)
wurzel = Knoten(start_konfiguration)

# 1. Züge erzeugen

def erzeuge_zuege_rekursiv(self):
    erzeuge_zuege(self)
    for kind in self.kinder:
        kind_konfiguration = kind.konfiguration
        if kind_konfiguration.anzahl_streichhoelzer > 0:
            kind.erzeuge_zuege_rekursiv()

Knoten.erzeuge_zuege_rekursiv = erzeuge_zuege_rekursiv


# 2. für jeden zug weiderum das erzeugen aufrufen
wurzel.erzeuge_zuege_rekursiv()
wurzel.print_teilbaum()


#####################################
print("\n\nGewinnkonfigurationen: Rekursion\n\n")

# Eine Konfiguration ist eine Gewinnkonfiguration:
# - für A/B wenn keine Streichhölzer mehr und B/A am Zug ist

def pruefe_gewinnkonfiguration(self):
    konf = self.konfiguration
    if konf.anzahl_streichhoelzer == 0:
        konf.gewinnkonfiguration = konf.spieler_nicht_am_zug()

Knoten.pruefe_gewinnkonfiguration = pruefe_gewinnkonfiguration

def pruefe_gewinnkonfiguration_rekursiv(self):
    for kind in self.kinder:
        kind.pruefe_gewinnkonfiguration_rekursiv()
    self.pruefe_gewinnkonfiguration()


Knoten.pruefe_gewinnkonfiguration_rekursiv = pruefe_gewinnkonfiguration_rekursiv



def pruefe_gewinnkonfiguration(self):
    konf = self.konfiguration
    if konf.anzahl_streichhoelzer == 0:
        konf.gewinnkonfiguration = konf.spieler_nicht_am_zug()
        return
    for kind in self.kinder:
        if konf.spieler_am_zug == kind.konfiguration.gewinnkonfiguration:
            konf.gewinnkonfiguration = konf.spieler_am_zug
            return
    konf.gewinnkonfiguration = konf.spieler_nicht_am_zug()

Knoten.pruefe_gewinnkonfiguration = pruefe_gewinnkonfiguration

wurzel.pruefe_gewinnkonfiguration_rekursiv()
wurzel.print_teilbaum()
print(""+wurzel.konfiguration.beschreibung())
