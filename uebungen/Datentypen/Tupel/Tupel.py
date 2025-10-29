# Tupel
#-------------------------------------------------------------------------------------------------------
# Grundlegendes
# Tupel sind keine Dynamischen Arrays -> sie sind unveränderbar! (Sind halt normale Arrays)
#-------------------------------------------------------------------------------------------------------
# Tupel werden ohne [] geschrieben
# Beispiel dazu

thistuple = ("appel", "banana", "cherry")
print(thistuple)

# Elemente von Tupeln: 
# 1. Sortiert 2. Unveränderbar 3. Erlauben Duplikate
# Sie sind genau wie Array indiziert mit [0], [1], ... [n]
#-------------------------------------------------------------------------------------------------------
# Sortiert bedeutet hierbei: Elemente haben eine Definierte Reihenfolge und diese ändert sich nicht
# Es können keine Elemente Hinzu-/Entfernt werden nach Erstellung
# Duplikate sind indiziert, daher haben Elemente den selben Wert
#-------------------------------------------------------------------------------------------------------
# Beispiel zu Duplikaten

tuple1 = ("olvie", "fig", "watermelon", "olive", "fig", "watermelon")
print(tuple1)

#-------------------------------------------------------------------------------------------------------
# Länge des Tupels per len()

tuple2 = ("Element1", "Element2", "Element3")
print(len(tuple2))

#-------------------------------------------------------------------------------------------------------
# Tupel mit nur einem Element erstellen 
# Wichtig! ein Komma muss nach dem Element rein sonnst wird es nicht erkannt

tuple3 = ("T34",)
print(type(tuple3))

# So nicht!
tuple4 = ("T72")
print(type(tuple4)) # <- wird als class str Erkannt und nicht als Tuple

#-------------------------------------------------------------------------------------------------------
# Datentypen in Tupeln
# Enthalten int, str, bool 

tuple5 = ("string")
tuple6 = (1, 5, 6, 7, 9)
tuple7 = (True, False, True, True, False)

# Sie können ebenso unterschiedliche Datentypen in einem Tupeln enthalten

tupel8 = ("abc", 10, True, 50, "male")

#-------------------------------------------------------------------------------------------------------
# Typen wie oben schon genutzt per type() kann man sehen ob es ein Tupel ist oder nicht

#-------------------------------------------------------------------------------------------------------
# Konstruktor per tuple()
# -> Erstellt ein tuple

tuple9 = tuple(("n1", "n2", "n3"))
print(tuple9)

#-------------------------------------------------------------------------------------------------------
