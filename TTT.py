from treelib import Node, Tree

tree = Tree()
tree.create_node(tag="B2", identifier="B2")
tree.create_node("A1", parent="B2", data="Spielfeld")
print(tree.show(stdout=False))


### benötigte Elemente

LEER = "_"
KREUZ = "X"
KREIS = "O"
#
spielfeld = [[LEER] * 3, [LEER] * 3,[LEER] * 3]
spielfeld[1][1]=KREUZ
print(spielfeld)

def print_spielfeld(spielfeld):
    for zeile in spielfeld:
        zeilen_text=""
        for feld in zeile:
            zeilen_text += feld + " "
        print(zeilen_text)

print_spielfeld(spielfeld)

# Algorithmus für NIMM implementieren.



class NIMM_Konfiguration:
    def __init__(self, anzahl: int, a_am_zug: bool, gewinnstellung_fuer: str=""):
        self.anzahl = anzahl
        self.a_am_zug = a_am_zug
        self.gewinnstellung_fuer = gewinnstellung_fuer

    def beschreibung(self):
        ausgabe_streichhoelzer = "Streichhölzer: " + str(self.anzahl) + ". "
        ausgabe_am_zug = "Spieler "
        if self.a_am_zug:
            ausgabe_am_zug += "A"
        else:
            ausgabe_am_zug += "B"
        ausgabe_am_zug += " am Zug. "
        ausgabe_gewinnstellung_fuer = "Gewinnstellung für " + self.gewinnstellung_fuer + "."
     
        return ausgabe_streichhoelzer + ausgabe_am_zug + ausgabe_gewinnstellung_fuer

    def ausgabe(self):
        print(self.beschreibung())

    

# am besten würde man das wohl rekursiv machen
# iterativ, einfach Stufe für Stufe geht auch
# leaves könnte man verwenden

NIMM = Tree()
data=NIMM_Konfiguration(12, True)
root:Node = NIMM.create_node(tag=data.beschreibung(), data=data)
tiefe=0
while tiefe<data.anzahl:
    for leaf in NIMM.leaves():
        nimm:NIMM_Konfiguration=leaf.data
        i=1
        while i<=3 and i<=nimm.anzahl:
            spieler_am_zug = "A"
            if nimm.a_am_zug:
                spieler_am_zug = "B"
            n = NIMM_Konfiguration(nimm.anzahl-i, not nimm.a_am_zug)
            NIMM.create_node(n.beschreibung(), parent=leaf, data=n)
            i += 1
    tiefe += 1

# Gewinnstellung bei den Blättern
leaf:Node=None
for leaf in NIMM.leaves():
    nimm:NIMM_Konfiguration=leaf.data
    if nimm.anzahl==0:
        if nimm.a_am_zug:
            nimm.gewinnstellung_fuer = "B"
        else:
            nimm.gewinnstellung_fuer = "A"
        leaf.tag=nimm.beschreibung()

tiefe = 0
while tiefe <=tiefe<data.anzahl:
    for leaf in NIMM.all_nodes():
        nimm:NIMM_Konfiguration=leaf.data
        if nimm.gewinnstellung_fuer == "":
            ein_A=False
            ein_B=False
            alle_A=True
            alle_B=True
            for l in NIMM.children(leaf.identifier):
                n:NIMM_Konfiguration=l.data
                if n.gewinnstellung_fuer=="A":
                    ein_A=True
                    alle_B=False
                elif n.gewinnstellung_fuer=="B":
                    ein_B=True
                    alle_A=False
                else:
                    alle_A=False
                    alle_B=False
            # wenn alle ich am Zug bin und mindestens einer der Kinder eine Gewinnstellung für nich, dann ist es eine Gewinnstellung
            if nimm.a_am_zug:
                if ein_A:
                    nimm.gewinnstellung_fuer="A"
                    leaf.tag=nimm.beschreibung()
                if alle_B:
                    nimm.gewinnstellung_fuer="B"
                    leaf.tag=nimm.beschreibung()
            elif not nimm.a_am_zug:                    
                if ein_B:
                    nimm.gewinnstellung_fuer="B"
                    leaf.tag=nimm.beschreibung()
                if alle_A:
                    nimm.gewinnstellung_fuer="A"
                    leaf.tag=nimm.beschreibung()
            else:
                None

    tiefe += 1

print(NIMM.show(stdout=False))

rootNIMM: NIMM_Konfiguration = root.data
print("Für das Spiel NIMM", rootNIMM.anzahl, "gilt für Spieler A")
if rootNIMM.gewinnstellung_fuer=="A":
    print("Spieler hat eine Gewinnstrategie.")
    # finde ersten Zug mit einer Gewinnstellung für A
    konf: NIMM_Konfiguration
    for leaf in NIMM.children(root.identifier):
        konf = leaf.data
        if konf.gewinnstellung_fuer=="A":
            break;
    zug = rootNIMM.anzahl-konf.anzahl
    print("A nimmt im ersten Zug", zug, "Streichhölzer.")
elif rootNIMM.gewinnstellung_fuer=="B":
    print("Spieler A verliert, weil Spieler B eine Gewinnstrategie hat.")
else:
    None



# class Spielfeld:
#     def __init__(self, id: Optional[int], name: str = "Unnamed"):
#         self.id = id
#         self.name = name


