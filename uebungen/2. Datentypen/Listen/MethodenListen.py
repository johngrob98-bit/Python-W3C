#Methoden
#-------------------------------------------------------------------------------------------------------
# Länge der Liste
# -> auch hier wieder len()

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # gibt die Länge der Liste aus (zählt die Anzahl der Elemente hierbei 3)

#-------------------------------------------------------------------------------------------------------
# Datentypen
# Alle Datentypen können in Listen gepackt werden
# -> Diese können auch Unterschiedlich innerhalb der Liste sein

list1 = ["pear", "berry", "strawberry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# -> Verschiedene Datentypen innerhalb der Liste

list4 = ["abc", 34, True, 40, "male"]

#-------------------------------------------------------------------------------------------------------
# type()
# Listen sind als Objekte definiert. Python kann per type() sagen welcher das ist 
# <class 'list'>

mylist = ["pineapple", "strawberry", "coconut"]
print(type(mylist)) # sagt hierbei nur das es eine <class 'list'> ist 
# Wenn man den Datentypen eines einzelen Elementes wissen will dann:
print(type(mylist[0])) # Ausgabe <class 'str'> usw

#-------------------------------------------------------------------------------------------------------
# list() Konstruktor: 
# Damit kann man eine Liste erstellen

thislist2 = list(("Plane", "Car", "Boat")) # Wichtig zu beachten hierbei die Syntax statt [] hat man ()
print(thislist2)

#-------------------------------------------------------------------------------------------------------
# Ändern des Wertes 
# -> an einem Spezifischen Index[n]

thislist3 = ["Key", "House", "Garage"]
thislist3[1] = "Garden"
print(thislist3)

#-------------------------------------------------------------------------------------------------------
# Ändern der Werte in einem spezifischen Bereich

thislist4 = ["Flywheel" , "Clutch", "Steeringwheel", "Gaspedal", "Wheels", "Brakes"]
thislist4[1:3] = ["E-Brake", "Gasket"]
print(thislist4)    

# Wenn mehr Elemente eingefügt werden als man austauscht, werden diese dort angelegt wo man es Angibt
# Die Länge der Liste ändert sich wenn die Anzahl der Elemente != der getauschen Elemente sind 
# Beispiel dazu: 

thislist4 = ["Flaps", "Gear", "Airbrake"]
thislist4[1:2] = ["Rudder", "Compass"] 
print(thislist4) 
# Gear wird mit Rudder getauscht, Compass kommt mit rein und Airbrake bleit gleich
# 0 Flaps, 1 Gear <- Rudder, 2 wäre Airbrake aber da kommt Compass rein, 3 Airbreake an jetzt

# Wenn man weniger Elemente einfügt als man ersetzt, werden sie an der Stelle eingefügt wo man festlegt
# Beispiel dazu

thislist5 = ["cow", "sheep", "deer"]
thislist5 [1:3] = ["fox"]
print(thislist5)
# 0 cow bleibt, 1 <- wird mit fox ersetzt, 2 deer wird gelöscht weil fox nur 1 Wort ist daher weg, 3 leer

#-------------------------------------------------------------------------------------------------------
# Einfügen per insert()
# Fügt an einem festgeleten Index Wert x ein

thislist6 = ["dog", "cat", "bird"]
thislist6.insert(2, "mouse")
print(thislist6) 
# Bei Index 2 Katze wird Maus eingesetzt. Katze geht auf Index 3 und Vogel auf Index 4

#-------------------------------------------------------------------------------------------------------
# Append Methode
# Fügt am Ende der Liste ein Element hinzu

thislist7 = ["paprika" , "broccoli", "tomato"]
thislist7.append("mushrooms")
print(thislist7)

#-------------------------------------------------------------------------------------------------------
# Elemente von einer Liste in die andere hinzufügen
# extend() Methode

thislist8 = ["carrot", "zucchini", "salad"]
otherlist = ["chicken", "turkey", "duck"]
thislist8.extend(otherlist)
print(thislist8) # Die Elemente kommen an das Ende der Liste wie bei append
# Mit der extend() Methode kann man alle der 4 Arten miteinander "verbinden"
# Beispiel dazu

thislist9 = ["pig", "trout", "salmon"]
thistuple = ["bear", "polar-bear"]
thislist9.extend(thistuple)
print(thislist9)

#-------------------------------------------------------------------------------------------------------
# Löschen per remove()
# -> Wichtig hierbei: erst wird bei mehrfachbelegung eines Wertes der erste davon gelöscht
# z.B (1, 2, 3, 1, 3, 4, 1) <- hier wird die erste 1 erste 3 usw gelöscht 

thislist10 = ["1", "2", "1", "1", "3" , "4"]
thislist10.remove("1")  # sieht man hier im coplie ganz gut erste 1 geht weg die anderen bleiben
print(thislist10)

#-------------------------------------------------------------------------------------------------------
# Ein bestimmten Index löschen per pop()

thislist11 = ["John", "Ben", "Max"]
thislist11.pop(1) # <- hier wird jetzt Ben removed
print(thislist11) # wenn man den Index nicht spezifisch angibt wird das letzte Element gelöscht

#-------------------------------------------------------------------------------------------------------
# Index oder gesamte Liste löschen per del()

thislist12 = ["Lecerc", "Stuart", "Sherman"]
del thislist12[2]
print(thislist12) # wenn man [] lässt wird alles gelöscht

#-------------------------------------------------------------------------------------------------------
# Leere Liste per clear()

thislist13 = ["Frogfoot", "Fishbed", "Flanker"]
thislist13.clear()
print(thislist13)