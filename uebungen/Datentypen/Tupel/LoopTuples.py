# Loop Tuples   
#-------------------------------------------------------------------------------------------------------
# Prinzipiell ist es genau so wie bei Listen es kann while, for, range, len, usw genutzt werden
#-------------------------------------------------------------------------------------------------------

# Iteration per for-Schleife
# Funktioniert wieder analog zu Listen (Bei allen 4 Arten Arraytypen ist es gleich)

tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x) # Wie auch bei Listen gibt es alle 3 Elemente aus
print()

#-------------------------------------------------------------------------------------------------------
# Ebenso analog, Index durch iterieren

tuple2 = ("apple", "banana", "cherry")
for i in range(len(tuple2)): # Dabei kann man auch wieder einen bestimmten Index wählen und ausgeben
    print(tuple2[i])
print()

#-------------------------------------------------------------------------------------------------------
# While Schleife ""    

tuple3 = ("F4S", "SU30SM", "MIG 29")
i = 0                   # Wir starten die Schleife bei 0
while i < len(tuple3):  # Counte solange, bis das Ende des Tupels erreicht ist
    print(tuple3[i])    # Alle Elemente werden geprintet (hier kann man wieder ein Bestimmtes wählen)
    i = i + 1           # Nicht vergessen zu inkrementieren sonnst passiert nix

#-------------------------------------------------------------------------------------------------------
# Verbinden von verschiedenen Tuplen per + Operator
# Selbes Prinzip (ich glaub man merk das es sich wiederholt)

tuple4 = ("a", "b", "c")
tuple5 = (1, 2, 3)

tuple6 = tuple4 + tuple5 
print(tuple6)

#-------------------------------------------------------------------------------------------------------
# Multiplizieren per * Operator
# Anzahl der Elemente wird hier multipliziert 

tuple7 = ("4", "5", "6")
multituple = tuple7 * 2
print(multituple) # Einfach mal compilen

#-------------------------------------------------------------------------------------------------------
# 2 Weitere Methoden zum nachlesen: https://www.w3schools.com/python/python_tuples_methods.asp
# Tupel Ende