# Loop Dictionaries
#-------------------------------------------------------------------------------------------------------
# Iterieren per for-Schleife

car = {
    "brand" : "BMW",
    "model" : "220i G42",
    "year" : 2024
}
for x in car:
    print(x) # Iteriert jedes Attribut einmal durch und gibt es aus
print()

#-------------------------------------------------------------------------------------------------------
# Alle Werte ausgeben mit []

for x in car:
    print(car[x])
print()

#-------------------------------------------------------------------------------------------------------
# Ebenso mit möglich mit values()

for x in car.values():
    print(x)
print()

#-------------------------------------------------------------------------------------------------------
# ^ analog zu oben ^ mit key()

for x in car.keys():
    print(x)
print()

#-------------------------------------------------------------------------------------------------------
# Wenn man beides will dann mit items()

for x, y in car.items():
    print(x, y)
print()

#-------------------------------------------------------------------------------------------------------
# Kopieren der Dictionaries per copy()
# dict2 = dcit1 !geht nicht! es wird nur eine Referenz erstellt -> Änderungen in dict1 auch in dict2 so

carcopy = car.copy()
print(carcopy) # Es wird eine Kopie erstellt welche auf das Original referenziert 

#-------------------------------------------------------------------------------------------------------
# Gleiches geht mit dict() auch

cardict = dict(car)
print(cardict) # Einfache Methode welche im Endeffekt wie list(), set() usw ein neues Objekt erstellt
print()

#-------------------------------------------------------------------------------------------------------
# Verschachtelte Dictionaries
# Wenn man überlegt ein Dictionary besteht ja nicht nur aus einem Auto oder Kind usw. Deswegen je mehr 
# desto besser, Syntaxtechnisch bleigt alles gleich. Eine "Oberklasse" Family bindet alle 3 Kinder 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {    # Oberklasse worauf die "Kinder" aufbauen -> ist wie eine Zugehörigkeit
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#-------------------------------------------------------------------------------------------------------
# Auf Elemente im verschachtelten Dictionary zugreifen per dict[dict2][Element]

#print(myfamily["child2"]["name"]) # Geht ins Dictionary child2 und greif auf das Element Name zu

#-------------------------------------------------------------------------------------------------------
# Iterieren per items()

for x, y in myfamily.items(): # x, y Attribute und Elemente werden iteriert und ausgegeben 
    print(x)

    for z in y: # z ist Schlüssel wie name oder key und es wird im Element iteriert
        print(z + ':', y[z]) # y[z] ist der dazugehörige Wert wie Emil 2006 

#-------------------------------------------------------------------------------------------------------
# Methoden von Dictionaries: https://www.w3schools.com/python/python_dictionaries_methods.asp
#-------------------------------------------------------------------------------------------------------
# Dictionaries Ende