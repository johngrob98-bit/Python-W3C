# Class_Object_Syntax
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: So gut wie alles in Python ist ein Objekt, mit seinen Eigenschaften und Methoden
# Eine Klasse ist wie ein Objektkonstruktor oder eine "Blaupause" um Objekte zu erschaffen

#-------------------------------------------------------------------------------------------------------
# Wie erstellt man eine Klasse? 
# Dazu benötigt man nur das Schlüsselwort class

class myfirstclass:
    x = 5               # Und damit haben wir schon eine Klasse erstellt mit der Variable x = 5

#-------------------------------------------------------------------------------------------------------
# Jetzt benötigten wir noch Objekte in der Klasse
# Dazu erstellen wir das Objekt p1 mit dem Wert von x

p1 = myfirstclass()     # Das Objekt bezieht sich mit dem = auf die Klasse und erhält "Berechtigung"
                        # auf alle Elemente Methoden usw der Klasse zuzugreifen
print(p1.x)             # Damit geben wir wie ^ oben ^ gesagt p1 den Wert von x

#-------------------------------------------------------------------------------------------------------
# Erstellte Objekte können auch wieder gelöscht werden
# Dafür nutz man del()

del(p1)                 # Und damit exsistiert p1 nicht mehr und verliert den Wert von x
print("\n")

#-------------------------------------------------------------------------------------------------------
# Mehrere Objekte erzeugen

p1 = myfirstclass()
p2 = myfirstclass()
p3 = myfirstclass()

print(p1.x)
print(p2.x)
print(p3.x)
print("\n")

#-------------------------------------------------------------------------------------------------------
# !Wichtig! jedes Objekt ist alleinständig und hat seine eigene Kopie der Klasseneigenschaften

#-------------------------------------------------------------------------------------------------------
# Pass Statement
# Klassen können nicht leer sein daher nutzt man pass wenn man gerade noch nicht weiß was man eigibt

class Person:
    pass
