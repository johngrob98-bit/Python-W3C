# Loop Lists per While und for (die print() überall sind nur für die Formatierung)
#-------------------------------------------------------------------------------------------------------

# Iteration der Elemente eine Liste per for-Schleife

thislist = ["apple", "banana", "cherry\n"]
for x in thislist:
    print(x)
# Alle Elemente der Liste werden einzeln geprinted

#-------------------------------------------------------------------------------------------------------
# Iteration durch die Index Nummer iterieren per range() und len() 

thislist1 = ["kiwi", "orange", "pear\n"]
for i in range(len(thislist1)):
    print(thislist1[i]) # gibt mir den Index des jeweiligen Elmentes 

#-------------------------------------------------------------------------------------------------------
# Whileschleife in Listen 
# per len() Länge und per inkrement durch die Liste gehen

thislist2 = ["peas", "chhickpeas", "humus\n"]
i = 0
while i < len(thislist2):
    print(thislist2[i])
    i = i + 1 

#-------------------------------------------------------------------------------------------------------
# Per for-Schleife iterieren, bietet den kürzesten Weg

thislist3 = ["zeus", "hades", "hercules\n"]
[print(x) for x in thislist3] # Alle Elemente werden geprintet 

#-------------------------------------------------------------------------------------------------------
# Beispiel: neue Liste Basierend auf bestehender Liste mit einer Bedingung
# Hierbei Elemente welche nur den Buchstaben "a" enthalten 
# 2 Möglichkeiten 1. mit for-Schleife 2. mit [for...]

# Erste Möglichkeit
cars = ["BMW", "Audi", "Volkswagen", "Toyota", "Nissan"] # <- 3 Elemente mit "a"
newlist = [] # Neue leere Liste

for x in cars:   # x -> Alle Elemente werden iteriert 
    if "a" in x: # wenn "a" in der Liste vorhanden
        newlist.append(x) # append() also füge die Elemente in die leere Liste hinzu
print(newlist)   # Hier sind dann nur Audi, VW, Toyota in der Liste 
print()

# Zweite Möglichkeit
cars2 = ["Alfa Romeo", "Mazda", "Mercedes", "Jeep"] # wieder 2 Elemente mit "a"
newlist2 = [x for x in cars2 if "a" in x]           # Die Schleife direkt in der Listenerstellung
print(newlist2)                                     # selbes Prinzip wie vorher nur kompakter
print()                                     

# Der Rückgabewert ist die neue Liste, die alte also cars, cars2 bleiben unverändert
# Die Bedingung ist ein Filter welcher nur True akzeptiert (fügt eben nur bei True ein)
# Beispiel wenn man ein Element ausschließen will: 
# newlist = [x for x in cars if x != "Audi"] schließt hierbei eben Audi aus auch wenn es ein "a" hat 

#-------------------------------------------------------------------------------------------------------
# Itererbares Objekt
# Kann jedes Objekt sein was iterierbar ist (also einfach alles int, list, tuple etc.)
# Per range() kann man ein Objekt erzeugen

newlist3 = [x for x in range(10)] # dazu können auch noch Bedingung 
print(newlist3)
print()

# Bedingung Beispiel 
newlist4 = [x for x in range(10) if x < 5]
print(newlist4)
print()

# Expression ist das aktuelle Element der iteration, gleichzeitig ist es auch das Ergebnis
newlist5 = [x.upper() for x in cars] # Setzt den Wert der Elemente in cars in uppercase
print(newlist5)
print()
# Änderung aller Elemente in ein anderes

newlist6 = ["heyjo" for x in cars] # <- macht aus allen Markne heyjo
print(newlist6)
print()

# Die Expression kann auch Bedingungen enthalten
newlist7 = [x if x != "BMW" else "Ford" for x in cars]  # ersetzt BMW mit Ford 
print(newlist7)
print()