# Methoden Sets (wird ein längeres Kapitel)
#-------------------------------------------------------------------------------------------------------
# Zugriff auf Elemente im Set
# Wichtig! Geht nicht mit [] und Index -> for-Schleife wird benötigt!

set = {"apple", "berry", "cherry"}
for x in set:
    print(x) # Gibt dabei alle Elemente aus 
#-------------------------------------------------------------------------------------------------------
# Wenn man nach einem Bestimmten Element sucht dann per if

set1 = {"banana", "pear", "fig"}
print("banana" in set1) 
# Es wird jetzt kein Traditionelles if verwendet sondern wenn banana im Set dann printe True
#-------------------------------------------------------------------------------------------------------
# Wenn man schaut ob ein Element nicht im Set ist dann analog zu oben mit not

set2 = {"string", "strong", "stronk"}
print("stronk" not in set2) # Gibt false aus weil stronk eben im Set ist wenn nicht -> True

#-------------------------------------------------------------------------------------------------------
# Elemente hinzufügen per add()

set3 = {"Hello", "my name", "is"}
set3.add("Ufuk") # Man denk Ufuk kommt am Ende also Hello my name is Ufuk aber nein!
print(set3) # Wichtig! Sets sind random von der Reihenfolge her aufpassen!

#-------------------------------------------------------------------------------------------------------
# Elemente von einem Set ins andere hinzufügen per update()

set4 = {"mango", "papaya", "pineapple"}
set5 = {"banana", "honeymelon", "watermelon"} # 2 Unterschiedliche Sets 

set4.update(set5) # <- Per update() zusammenführen
print(set4) 

#-------------------------------------------------------------------------------------------------------
# Info zu Update: Egal ob List Tupel Dictionary, sie alle kännen update in ein Set konvertiert werden

set6 = {"BMW", "Audi", "Volkswagen"}
list = {"Nissan", "Toyota"}

set6.update(list)
print(set6) # Die Liste wird zu einem Set -> wird im Endeffekt per add() danach in set6 reingesteckt

#-------------------------------------------------------------------------------------------------------
# Entfernen von Elementen per remove() oder discard()
# remove()

set7 = {"Ford", "Mercedes", "Porsche"}
set7.remove("Ford") # Wir mögen kein Ford!
print(set7) # Wichtig! Wenn es das Element nicht im Set gibt = error

# discard() Wichtig! Wenn es hier das Element nicht gibt -> kein error!

set8 = {"Mazda", "Honda", "Lexsus"}
set8.discard("Audi") # Hier als Beispiel es wird keinen Error geben 
print(set8)

#-------------------------------------------------------------------------------------------------------
# Das selbe per pop() -> Wichtig! Entfernt ein random Element

set9 = {"SEGA", "Capcom", "Konami"}
x = set9.pop() # Irgendeins der 3 Elemente wird entfernt
print(x) # Das Element was entfernt wird Ausgabe
print(set9)

#-------------------------------------------------------------------------------------------------------
# "" per clear() & del()
# clear() leer das Set & del() entfernt das Set komplett

set10 = {1, 2, 3, 4}
set10.clear() # <- Leeres Set 
print(set10)

set11 = {5, 6, 7, 8}
del set11
# print(set11) -> Error weil set11 gelöscht wurde 

#-------------------------------------------------------------------------------------------------------
# Loop Sets -> Hier kein Eigenes Kapitel weil nur for-Schleife

set12 = {"Element1", "Element2", "Element3"}
for x in set12:
    print(x) # Gibt halt alle 3 Elemente an

#-------------------------------------------------------------------------------------------------------
# Sets verbinden 
# Es gibt mehrere Methoden, alle haben Besonderheiten
# union() und update() -> alle Elemente von beiden Sets werden verbunden
# insertsection() -> behält !nur! die Duplikate
# difference() -> behält Elemente vom Ersten Sets welche nicht in anderen Sets sind (Beispiel kommt)
# symmetric_difference() -> behält alle Elemente !außer! die Duplikate
#-------------------------------------------------------------------------------------------------------
# Verbinden per union()

setone = {"a", "b", "c"}
settwo = {9, 10, 11}
setthree = setone.union(settwo) # Verbindung !unsortier! beider Sets
print(setthree)

# Man kann auch | benutzen statt union() (Im Endeffekt ist das ganze wie logisches oder ||)
# Verbindung mit | Funktioniert analog zu union(). Einfach union() mit | erstzen
# Natürlich kann man auch mehr als 2 Sets miteinander verbinden

set13 = {"d", "e", "f"}
set14 = {12, 13, 14}
set15 = {"John", "Grob"}
set16 = {"Fruits", "Vegetables"}

unionset = set13.union(set14, set15, set16)
print(unionset) # Auch hier wieder mit | ersetzbar aber ich spaare mir das zu schreiben

#-------------------------------------------------------------------------------------------------------
# Verbinden von Sets und Tuple per union()

x = {"g", "h", "i"}
y = (15, 16, 17)
# Nicht vergessen Set {} Tuple () Listen [] 

z = x.union(y)
print(z) # Geht alles wie sonsnt auch, wie oben erklärt wird Tuple wieder konvertiert zum Set 
# Jetzt denk mal wahrscheinlich das | auch das gleiche macht wie oben !Wichtig! nein das geht nur mit 
# den selben Datentypen also nur Set | Set die union() Methode kann das bei allen | aber nur Set mit Set

#-------------------------------------------------------------------------------------------------------
# Einfügen per update()
# Wie oben erwähnt update() fügt alle Elemente von Set1 in Set2 rein !aber! es verändert hierbei das 
# Ausgangsset und gibt kein neues Set dabei raus also returned es wieder Set1

set17 = {"j", "k", "l"}
set18 = {18, 19, 20}

set17.update(set18)
print(set18) # !Wichtig! update() und union() ignorieren Duplikate 

#-------------------------------------------------------------------------------------------------------
# Nur Duplikate behalten per intersection()

set19 = {"Microsoft", "Apple", "Google"}
set20 = {"OpenAi", "Microsoft", "Google", "Siemens"} # Es gibt 2 Dupliakte in beiden Sets
set21 = set19.intersection(set20) # Immer ein neues Set erstellen und da dann die Duplikate speichern
print(set21) # Ausgabe Microsoft, Google

# !Wichtig! wie bei union() geht es hier mit & statt | gleiches gilt auch hier & kann nur Set mit Set
# Methode intersection() kann Set mit Tuple usw 
#-------------------------------------------------------------------------------------------------------
# intersection_update() Methode behält nur Duplikate aber verändert das Ausgangsset statt return set

set22 = {"Roccat", "Razor", "Logitech"}
set23 = {"Razor", "Astro", "Roccat"}
# Jetzt nicht set24 sondern wieder in set22 rein
set22.intersection_update(set23)
print(set22)

#-------------------------------------------------------------------------------------------------------
# Gleiches geht auch wenn True(1) oder False(0) im set sind, diese Zählen natürlich auch als Duplikate
#-------------------------------------------------------------------------------------------------------
# Unterschiedliche Elemente per difference()
# Es werden nur nicht Duplikate übernommen 

set24 = {"apricot", "butter", "bacon","Oil"}
set25 = {"chicken", "butter", "apricot"} # Es wird also nur bacon oil übernommen
set26 = set24.difference(set25) # Eben weil nur Elemente vom ersten Set (set24) welche nicht in set26
# enthalten sind übernommen werden
print(set26) # Hierbei wird wieder ein neues Set erstellt
# Simpler erklärt zeig mir nur die Zutaten welche in Schüssel1 (set24) sind welche nicht in Schüssel2
# (set26) sind
#-------------------------------------------------------------------------------------------------------
# Auch hier geht es wieder mit einem anderen Operator: hier ist es -
# Gleiche Regel - nur Set mit Set difference() Set mit Tuple usw
#-------------------------------------------------------------------------------------------------------
# difference_update() gleiches Prinzip nur dass das Ausgangset verändert wird also kein neues Set 

set27 = {21, 22, 23, 24} # Es wird nur 23 und 24 übernommen
set28 = {25, 26, 21, 22} # Weil eben nur 23,24 in set27 sind aber nicht in set28
set27.difference_update(set28)
print(set27)

#-------------------------------------------------------------------------------------------------------
# Symmetrische Unterschiede per symmertic_difference
# Behält nur die Elemente welche !NICHT! in beiden Sets vorhanden sind
# Also es wird nur das entfernt was in beiden Sets enthalten ist 
# Beispiel dazu:

set29 = {"Hello", "I", "am", "here"} 
set30 = {"I", "will", "get", "kicked"} # Nur das I ist in beiden enthalten daher wird I gestrichen
set31= set29.symmetric_difference(set30)
print(set31) # Bei der Ausgabe wie oben erwähnt bleibt nur das I zurück

#-------------------------------------------------------------------------------------------------------
# Gleiches Spiel mit anderem Operator hier ist es: ^
# Und auch hier nur Set ^ Set, Set ^ Tuple !ungültig!
#-------------------------------------------------------------------------------------------------------
# Frozensets ist eine unveränderbare Art von Sets
# Enthält 1. Einzigartige 2. Unsortierte 3. Unveränderbare Elemente
# Unterschied zu Sets !Elemente können weder hinzugefügt noch entfernt werden
#-------------------------------------------------------------------------------------------------------
# Erstellen eines frozensets per frozenset() Konstruktor

a = frozenset({"Im", "here", "now"})
print(a)
print(type(a)) # Zeigt ob es ein frozenset ist oder nicht
# Übrigens liegen die Eigenschaften von frozensets schon in Namen forzen = gefroren daher verständlicher
#-------------------------------------------------------------------------------------------------------
# Methoden von frozensets: https://www.w3schools.com/python/python_frozenset.asp
# Alle Methoden von Sets nocheinmal im Überblick: https://www.w3schools.com/python/python_sets_methods.asp
#-------------------------------------------------------------------------------------------------------
# Sets Ende