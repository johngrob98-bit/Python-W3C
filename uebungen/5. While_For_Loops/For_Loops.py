# For Schleifen
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: for Schleifen werden genutzt um über "Objekte" zu iterieren (also i++, i-- usw.)
# -> Die Obekte können Listen, Tupel, Dictionarys, Sets oder Strings sein
# Das for in Python ist weniger wie in anderen Sprachen, hier ist es mehr ein iterator als der Objekt-
# orientierten Programmierung
# Mit for Schleifen kann man z.B. jede Frucht in einem Tupel, Set, List etc. printen
#-------------------------------------------------------------------------------------------------------

# Beispiel dazu:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("\n")
# Jetzt wird jede Frucht einmal ausgegeben, es wird keine Indexvariable benötigt btw.

#-------------------------------------------------------------------------------------------------------
# Man kann eben auch durch einen String iterieren

for x in "banana":
    print(x)
print("\n")
# Hier wird dann jeder Buchstabe einmal geprinted

#-------------------------------------------------------------------------------------------------------
# Natürlich gehen bei for die "meisten" Konventionen wie bei while dementsprechend geht auch break

cars = ["BMW", "Audi", "VW"]
for x in cars:
    print(x)
    if x == "BMW":
        break

# Der print beendet sobald die Schleife BMW erreicht, kann natürlich auch mit Audi, VW getauscht werden
# Break geht auch vor dem if resultiert in mehr prints bis eben x erreicht wird

planes = ["MIG-19", "MIG-23", "MIG-15"]
for x in planes:
    if x == "MIG-23":
        break
    print(x)
print("\n")
# Dann wird nur MIG-19 ausgegeben weil danach auf MIG-23 iteriert wird 

#-------------------------------------------------------------------------------------------------------
# Wenn es break gibt dann gibt es auch ein continue
# Wie bei while Schleifen wird die iteration beendet und es wird mit der "nächsten" Schleife begonnen

planes2 = ["SU-27", "SU-27SM", "SU30SM"]
for x in planes2:
    if x == "SU-27SM":
        continue
    print(x)
print("\n")
# Dann sieht man es wird wie bei while das SU-27SM ausgelassen weil die Schleife "darüber" läuft

#-------------------------------------------------------------------------------------------------------
# Bestimmte Anzahl an iterationen per range()
# Die Funktion benötigt eine Anzahl an Nummern (Einfach eine Zahl in der Klammer), 0 ist der Standart
# Es wird immer +1 inkrementiert
# Beispiel dazu:

for x in range(6):
    print(x)
print("\n")
# Wie gesagt es wird von 0 Angefangen daher 0 1 2 3 4 5 
# Natürlich kann man wie der Name range schon sagt einen Bereich angeben wie (2, 6) also 2 - 6
# Bitte auch hier nicht vergessen 2 BIS 6 also 2 3 4 5 nicht die 6 

for x in range(2, 6):
    print(x)
print("\n")                 # Die ganzen \n sind nur für die Formatierung 

#-------------------------------------------------------------------------------------------------------
# Wie ^oben^ erwähnt ist das inkrement bei range +1 das kann mit einem dritten Paramenter erhöht werden

for x in range(2, 30, 3):
    print(x)
print("\n")
# Jetzt wird in 3er Schritten inkrementiert also 2 5 8 12 usw

#-------------------------------------------------------------------------------------------------------
# Wenn if dann auch else in for Schleifen
# Beispiel dazu:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Das else fungiert hier jetzt nicht als alternative zur Bedingung sondern als Ausgabe bei Beendigung
# Also ist die Ausgabe 0 1 2 3 4 5 Finally finished!
# !Wichtig! der else Block wird nicht ausgeführt wenn die Schleife per break beendet wird!
# Beispie dazu:

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Da der Fall x = 3 eintritt wird die Schleife beendet und das else wird übersprungen die Ausgabe endet
# bei 0 1 2 

#-------------------------------------------------------------------------------------------------------
# Auch bei for Schleifen gibt es Verkettungen -> genau wie bei if
# Die Innere Schleife wird einmal ausgeführt für jede iteration der äußeren Schleife

adj = ["red", "big", "tasty"]
fruits2 = ["pear", "fig", "coconut"]

for x in adj:
    for y in fruits2:
        print(x,y)

# Zwei Schleifen, äußere zuerst also red dann innere pear, dann äußere red dann innere fig ...
# Also einmal red mit allen Elementen iteriert red pear, red fig, red coconut dann big dann tasty usw.
# Einfach mal compilen

#-------------------------------------------------------------------------------------------------------
# Auch hier gibt es das pass Statement, da forschleifen nicht Leer sein können

for x in [0, 1, 2]:
    pass
# Naja es kommt halt nix raus

#-------------------------------------------------------------------------------------------------------
# for Schleifen Ende