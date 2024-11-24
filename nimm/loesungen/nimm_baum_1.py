##################
# Konfiguration
##################

class Nimm_Konfiguration:
    def __init__(self, spieler_am_zug, anzahl_streichhoelzer):
        self.spieler_am_zug = spieler_am_zug
        self.anzahl_streichhoelzer = anzahl_streichhoelzer

    def beschreibung(self):
        return "(" + self.spieler_am_zug + ", " + str(self.anzahl_streichhoelzer) + ")"
    
    def spieler_nicht_am_zug(self):
        if self.spieler_am_zug == "A":
            return "B"
        else:
            return "A"


test_konfiguration = Nimm_Konfiguration("A", 7)
print(test_konfiguration.beschreibung())

##################
# Baum
##################

class Knoten:
    def __init__(self, konfiguration):
        self.konfiguration = konfiguration
        self.kinder = []

    def print_teilbaum(self):
        print(self.konfiguration.beschreibung())
        for kind in self.kinder:
            kind.print_teilbaum()

    def anzahl(self):
        return len(self.kinder)+1


############
# Schritt 1: Startknoten mit Startkonfiguration erzeugen
############

start_konfiguration = Nimm_Konfiguration("A", 7)
wurzel = Knoten(start_konfiguration)


############
# Schritt 2: Nachfolgeknoten erzeugen
############

alle_knoten = [wurzel]
spieler = start_konfiguration.spieler_nicht_am_zug()
zug = 1
while zug <= 3 and zug <= start_konfiguration.anzahl_streichhoelzer:
    konf = Nimm_Konfiguration(spieler, start_konfiguration.anzahl_streichhoelzer-zug)
    neuer_knoten = Knoten(konf)
    wurzel.kinder.append(neuer_knoten)
    alle_knoten.append(neuer_knoten)
    zug += 1

wurzel.print_teilbaum()


############
# Schritt 2: Nachfolgeknoten erzeugen als Methode
############

def erzeuge_zuege(self):
    

Knoten.erzeuge_zuege = erzeuge_zuege

# alle bereits erzeugten Knoten durchgehen und nochmals Knoten anzähgen


#######
# Besserer Ansatz: Rekurs
#######

# 1. Züge erzeugen
# 2. für jeden zug weiderum das erzeugen aufrufen





