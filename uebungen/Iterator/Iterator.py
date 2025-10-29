# Iterator
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Der Iterator ist ein Objekt welches Werte von zählbaren Zahlen enthält
# !Wichtig! Es kann auf einen Iterator -> iteriert werden d.h man kann durch die Werte travesieren
# Technisch gesehen in ist der iterator in Python ein Objekt, welches die Methoden __iter__() __next__()

#-------------------------------------------------------------------------------------------------------
# Iterator vs Iterable (Iterator vs Iterierbares Objekt)
# Listen, Tupel, Dictionaries und Sets sind alles Iterierbare Objekte. Sie sind Container, über die man
# iterieren kann und aus denen man einen Iterator erzuegen kann
# Alle diese Objekte können mit der iter() Funktion in einen Iterator konvertiert werden
# Beispiel dazu:

tuple = ("apple", "banana", "cherry")   # Erstellen eines Tupels
it = iter(tuple)                        # Iterator erstellen

print(next(it))     # Hier werden dann die Werte ausgegeben
print(next(it))     # Ditto
print(next(it))     # Ditto

# Rückgabe vom Iterator in einem Tupel und prints der jeweiligen Werte

#-------------------------------------------------------------------------------------------------------
# Selbst Strings sind Iterierbare Objekte, sie enhalten eine Abfolge von Charakteren

str = "banana"          # Das Prinzip ist glaube ich klar
myit = iter(str)        # Man erhält dadurch immer genau das Element in Objekt was vom Start aus als 
                        # nächstes kommt
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("\n")

#-------------------------------------------------------------------------------------------------------
# Per Schleife durch den Iterator 

tuple2 = ("Dog", "Cat", "Bird")

for x in tuple2:
    print(x)

# Gibt jedes Element im Iterator aus, und man kann sich den Iterator wie einen Zeiger vorstellen
# Dieser zeigt immer auf das erste Element im Index, dann iteriert man einfach immer weiter bis zum Ende
# !Wichtig! dazu: die for-Schleife erstellt ein Iterator Objekt und führt für jede Schleife next() aus

#-------------------------------------------------------------------------------------------------------
# Erstellen eines Iterators
# Um ein Objekt/Klasse als einen Iterator zu erstellen benötigt man die Methoden __iter__() __next__()
# Kurzer Einschub, alle Klassen in Python haben eine __init__() Funktion, sie erlaubt initialisierung 
# wenn Objekte erstellt werden

# Die __iter__() Methode funktioniert ähnlich, damit kann man Operationen wie (initialiserungen etc.)
# machen, aber man muss !immer! das Iterator Objekt selber zurückgeben
# Einfach gesagt die iter() Methode gibt es Iteraotr-Objekt zurück

# Die __next__() Methode erlaubt Operationen, das nächste Element der Reihe muss zurückgegeben werden

#-------------------------------------------------------------------------------------------------------
# Iterator welcher Zahlen zurückgibt, Start bei 1 und Reihe erhöhrt sich um 1 (return 1,2,3,4,5 etc.)

class Numbers:              # Ist vorhergegriffen aber, hier wir eine Klasse erstellt
    def __iter__(self):     # Erstellen eines Iterators, mit dem Objekt self (muss returned werden)
        self.a = 1          # Initialisiert die Objektvariable mit 1
        return self         # Rückgabe des Objekts
    
    def __next__(self): 
        if self.a <= 20:     # Dito, aber hier muss das nächste Element returned werden
         x = self.a          # Variable bekommt den Wert vom Iterator Objekt
         self.a += 1         # Erhöht den Zustand um 1
         return x            # Das nächste Element muss returned werden
        else:
           raise StopIteration

myclass = Numbers()         # Variable myclass bekommt die Elemente und Variablen aus Klasse Numbers
myiter = iter(myclass)      # Der Iterator wird erstellt, mit den Werten aus myclass

# print(next(myiter))         # Dann wird 5x durch iteriert
                              # Für 5 Iterartionen muss dann 5x print(next(myiter)) dranstehen 
for x in myiter:              # Wurde aber für das Beispiel unten entfernt
   print(x)                   # Hier wird dann 20x Ausgegeben 



#-------------------------------------------------------------------------------------------------------
# Stopiteration
# Im Beispiel ^ oben ^, der Code würde ewig laufen, bei genug next() Statements oder einer for Schleife
# Um das zu verhindern, benutzt man das StopIteration Statement, in der __next__() Methode, dort wird 
# eine Terminierungsbedingung hinzugefügt. Dieser wirft dann einen Fehler bei bestimmter 
# Anzahl von Iterationen

#-------------------------------------------------------------------------------------------------------
# Ab 20 Iterationen gibt es einen Error
# Dafür kann man im Code oben einfach eine if else hinzufügen und fertig

#-------------------------------------------------------------------------------------------------------
# Iterator Ende
