# Init Method
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Alle Klassen haben eine eingebaute __init__() Methode, diese wird immer automatisch
# ausgeführt wenn eine Klasse initialisiert wird
# Die __init__() Mehode wird genutzt um Werte an Objekteigenschaften zuzuweisen oder Operationen
# auszuführen welche nötig sind um ein Objekt zu erstellen

#-------------------------------------------------------------------------------------------------------
# Beispiel dazu: Eine Klasse erstellen und per __init__() Werte für Name und Alter zuweisen

class Person:
    def __init__(self, name, age):      # Also hier name und age werden dann zugewiesen
        self.name = name                # self ist notwendig um die Werte an das Objekt zu binden sodass
        self.age = age                  # p1.name und p1.age zugänglich sind
                                        # self repräsentiert das Objekt selbst (in Java z.B. ist es this)
p1 = Person("Ufuk", 24)                 # Also der Variable werden über die Parameter die Werte für 
                                        # Name und Alter zugewiesen
print (p1.name)
print(p1.age)
print("\n")

#-------------------------------------------------------------------------------------------------------
# Warum sollte man __init__() nutzen?
# Ohne die init Methode müsste man die Parameter für jedes Objekt maunell setzten also:

class Person2:
    pass

p2 = Person2()      # Hier macht man alles einzeln, also die vergabe der Variablen, Name, Alter 
p2.name = "Ufuk"
p2.age = 24

print(p2.name)
print(p2.age)
print("\n")

#-------------------------------------------------------------------------------------------------------
# Standart Werte in __init__()
# Man kann eben auch Standartwerte für die Parameter in der init() Methode setzten

class Person3:
    def __init__(self, name, age = 18):   # Im Konstruktor wurde gesagt das age generell auf 18 gestzt ist
        self.name = name
        self.age = age

p3 = Person3("John")                # Heißt John ist jetzt wenn wir nichts ändern 18
p4 = Person3("Yakuza", 25)          # Hier wurde das defaut age geändert auf 25

print(p3.name, p3.age)
print(p4.name, p4.age)

#-------------------------------------------------------------------------------------------------------
# Die Anzahl der Parameter im Konstruktor ist nicht beschränkt (außer auf unendlich ha ha ha)
# Dementsprechend kann man soviele Attribute hinzufügen wie man will

#-------------------------------------------------------------------------------------------------------
# Initmethod Ende