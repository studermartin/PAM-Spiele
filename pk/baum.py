

# Bäume bestehen aus Knoten. 
# Typischerweise ist der Baum umgekehrt dargestellt: Die Äste gehen nach unten.
# Den obersten Knoten nennt man Wurzel.
# Die untersten Knoten Blätter.
# Die Knoten enthalten Werte.


wurzel = { "wert": 3}

knoten1 = { "wert": 10 }

wurzel["kinder"] = [ knoten1 ]
knoten1["kinder"] = []

def print_knoten(knoten):
    print("Knoten mit Wert", knoten["wert"], "und", len(knoten["kinder"]), "Kindern.")

print_knoten(wurzel)

# Verhängen

# alle durchgehen
# rekursiv kein Problem



# Aufgaben


