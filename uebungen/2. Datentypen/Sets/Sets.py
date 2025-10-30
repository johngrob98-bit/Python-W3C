#Sets
#------------------------------------------------------------------------------------------------------- 
# Grundlegendes
# Sets sind keine Dynamischen Arrays -> keine feste Reihenfolge, keine Duplikate, kein Indexzugriffe
# Elemente sind Unveränderbar -> !man kann dennoch Elemente entfernen und hinzufügen!
#-------------------------------------------------------------------------------------------------------
# Sets werden mit {} geschrieben
# Beispiel dazu:

set = {"apple", "banana", "cherry"}
print(set)
# Wichtig! Da Sets unsortiert sind kann man nicht wissen welche Reihenfolge die Elemente haben
#-------------------------------------------------------------------------------------------------------
# Elemente von Sets: 
# 1. Unsortiert 2. Unveränderbar 3. Keine Duplikate
#-------------------------------------------------------------------------------------------------------
# Unsortiert: keine definierte Ordnung (sieht man auch bei der Ausgabe von set)
# -> sind nicht referenzierbar über ihren Index (dieser ändert sich durchgehend)
# Unveränderbar: nach Erstellung keine Änderung möglich
# Duplikate: wie gesagt nicht erlaubt
#-------------------------------------------------------------------------------------------------------
# Kurzes Beispeil zu Duplikaten

set1 = {"pear", "melon", "honeymelon", "pear"} # Duplikat wird ignoriert
print(set1)
 
# Ausnahme True und 1 und False und 0 werden als das selbe gesehen
# Gibt man in ein Set also True und 1 ein kommt nur True / False raus
#-------------------------------------------------------------------------------------------------------

# Länge des Sets per len() analog wie bei allen anderen Array-Listen

set2 = {"1", "2", "3", "4"}
print(len(set2))

#-------------------------------------------------------------------------------------------------------
# Datentypen in Sets (analog zu "")

set3 = {"string"}
set4 = {5, 6, 7}
set5 = {True, False, True} # Funktioniert wie bei allen anderen halt

print(set3)
print(set4)
print(set5) # Also können Sets diese 3 Datentypen annehmen

set6 = {"string", 8, True, 40, "male"} # Geht natürlich auch wieder zusammen

#-------------------------------------------------------------------------------------------------------
# Per type() sieht man ob es sich um ein Set handelt oder nicht

#-------------------------------------------------------------------------------------------------------
# Konstruktor per set()
# -> Erstellt ein Set

set7 = set(("fig", "dates", "hummus")) # Wichtig! (()) 2 Klammern dafür
#-------------------------------------------------------------------------------------------------------
 