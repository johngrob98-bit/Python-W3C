#Methoden
#-------------------------------------------------------------------------------------------------------
# Zugriff auf Elemente im Tupel 
# Indexnummer und []

tuple1 = ("a", "b", "c")
print(tuple1[1]) # Gibt b aus 
# Es wird immer noch von 0 gezählt

#-------------------------------------------------------------------------------------------------------
# Negativer Index
# Von Start zu Ende des Tupels 
# -1 Ende, -2 Vorletztes usw

tuple2 = ("d", "e", "f")
print(tuple2[-1]) # Es wird f geprintet

#-------------------------------------------------------------------------------------------------------
# Bereich von Indindizies, hierbei Start und Endwert 
# Wichtig! z.B 2:5 heißt nicht das 5 Element ist mit dabei sondern die Differenz von 5 - 2 = 3

tuple3 = ("g", "h", "i", "j", "k", "l", "m")
print(tuple3[2:5]) # Nochmal von i - k (l ist nicht dabei eben nur die Differenz)

#-------------------------------------------------------------------------------------------------------
# Geht in beide Richtungen also [:4] und [2:]
# Start bei dem jeweiligen Index bis zum gewählten Index

tuple4 = ("n", "o", "p", "q", "r", "s", "t")
print(tuple4[:4]) # Geht von n - q 

#-------------------------------------------------------------------------------------------------------
# Anderesherum 

tuple5 = ("u", "v", "w", "x", "y", "z")
print(tuple5[2:]) # Geht von w - z

#-------------------------------------------------------------------------------------------------------
# Bereich der negativen Indexe
# Geht von hinten los je nachdem welcher Index gewählt wurde

tuple6 = ("1", "2", "3", "4", "5", "6", "7")
print(tuple6[-4:-1]) # Geht von 7 bis -4 7 = [-1], 6 = [-2], 5 = [-3], 4 = [-4]

#-------------------------------------------------------------------------------------------------------
# Prüfen ob Element im Tupel ist per if "tuple" in tuple1

tuple7 = ("8", "9", "10")
if "9" in tuple7:
    print("Yes 9 is in tuple7")

#-------------------------------------------------------------------------------------------------------
# Elemente änderbar machen
# Geht doch eigentlich nicht oder? Doch indem man das Tupel zu einer Liste convertet

x = ("apple", "banana", "cherry")
y = list(x) # y wird zu einer Liste mit den Elementen von x (Tuple)
y[1] = "kiwi" # banana wird zu kiwi in der Liste
x = tuple(y) # Die geänderten Elemente aus der Liste werden wieder ins Ausgangstupel gespeichert 
# -> Gleichzeitig wird die Liste wieder zu einem Tuple
print(x)

#-------------------------------------------------------------------------------------------------------
# Elemente hinzufügen
# Geht genauso wieder in eine Liste konvertieren, Element hinzufügen fertig :D

tuple8 = ("pear", "orange", "kiwi")
y = list(tuple8)    # Konvertieren in eine Liste
y.append("apple")   # Hinzufügen vom Element
tuple8 = tuple(y)   # Zurück konvertieren in Tuple
print(tuple8)

#-------------------------------------------------------------------------------------------------------
# Tuple zu Tuple hinzufügen

tuple9 = ("T54", "T55", "T55A")
y = ("T62",) # y wird als neues Tuple Wichtig! Komma nicht vergessen nach dem Element
tuple9 += y # Hinzufügen des neuen Elementes aus den Tuple y into tuple9

print(tuple9)

#-------------------------------------------------------------------------------------------------------
# Entfernen von Elementen
# Das Prinzip ist klar oder? Konvertieren, Entfernen, Konvertieren usw.

tuple10 = ("T62A", "T62B", "T64A")
y = list(tuple10)
y.remove("T62B")
tuple10 = tuple(y)
print(tuple10)

#-------------------------------------------------------------------------------------------------------
# Löschen per del()

tuple11 = ("A", "B", "C")
del tuple11 # Selbsterklärend

#-------------------------------------------------------------------------------------------------------
# Unpacking
# -> Werte die dem Tupel zugewiesen werden 

tuple12 = ("T72A", "T72B", "T80") # <- Normale zuweisung von Elementen
# Aber mit unpacking geht es auch anders
(green, red, yellow) = tuple12 # green, red, yellow werden die Werte der Elemente in tuple12 zugewiesen
# Diese sind dann Referenzen auf die dann zugegriffen werden kann per print
# Die prints hier geben demnach T72A, T72B und T80 aus
print(green)
print(red)
print(yellow)

#-------------------------------------------------------------------------------------------------------
# Asterisk verwenden *
# Wird genutzt wenn: Wenn es weniger Werte als Variablen gibt, dann * an den Variablen Namen (Element)
# Diese bekommt dann den die Restlichen Werte der Liste

# Beispiel dazu:

tuple13 = ("Leopard", "Gepard", "Tiger", "Maus", "Lynx")

(blue, white, *grey) = tuple13 # Erstmal wieder das selbe Prinzip nur das hier bei grey ein * ist

print(blue)  # Tiger Maus Lynx werden in eine Seperate Liste gepackt 
print(white) # Leopard, Gepard werden Normal ausgegeben
print(grey)  # In der Ausgabe sieht man es gut 

# Eben weil es nur 3 Referenzvariablen gibt wird an die dritte, die restlichen Elemente gehangen

