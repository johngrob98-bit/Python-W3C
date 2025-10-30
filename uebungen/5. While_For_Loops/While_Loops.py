# While Schleifen
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: in Python gibt es zwei primitive commands: for & while
# !Wichtig! die while Schleife wird so lange ausgeführt wie die Bedinung es vorgibt !Endlospotenzial!
# Die Variablen in der while müssen vorher deklaiert werden sonnst läuft diese nicht an
#-------------------------------------------------------------------------------------------------------
# Beispiel dazu:

i = 1
while i < 6:
    print(i)
    i += 1
# Ich persöhnlich "spreche" die conditions immer vor damit es Sinn ergibt
# Während i kleiner 6 printe...
# !Wichtig! das i (oder egal welche andere Variable) muss inkrementiert oder dekrementiert werden 
# Falls das nicht geschieht läuft die Schleife wie gesasgt Endlos
#-------------------------------------------------------------------------------------------------------

# Dazu gibt es noch das break Statement
# Damit wird die Schleife beendet auch wenn die Bedingung true ist 

x = 1
while x < 6:
    print(x)
    if x == 3:  # Ja man kann auch ifs in whiles setzten (muss man meistens sogar)
        break
    x += 1
# Hier wird die Schleife beendet sobald x den Wert 3 erreicht hat.

#-------------------------------------------------------------------------------------------------------
# Zum break gibt es noch das continue
# Mit continue wird das aktuelle Statement gestoppt und es wird mit dem nächsten weitergemacht

y = 0
while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)
# Ab dem Punkt wo y = 3 wird das print dafür übersprungen -> also ist die Ausgabe 1 2 4 5 6
# Einfach mal compilen dann wird es ersichtlicher 

#-------------------------------------------------------------------------------------------------------
# Auch else kann im while genutzt werden
# Damit wird der Code Block ausgeführt auch wenn die Bedingung nicht mehr true ist !Wichtig! aber nur 1x

z = 1
while z < 6:
    print(z)
    z += 1
else:
    print("z is no longer less than 6")

# Der print geht nur durch da das else ein mal nach Erfüllung der Bedingung durchlaufen wird 
#-------------------------------------------------------------------------------------------------------
# While Schleifen Ende