# Lambda Funktionen
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Lambda Funktion können eine beliebige Anzahl an Argumenten annehmen aber nur 
# !einen! Ausdruck haben, !Wichtig! Lambda Funktionen sind annonym (kommt später)
# Lambda Funktionen spaaren Platz da keine Definition für sie nötig sind

#-------------------------------------------------------------------------------------------------------
# Snytax: lambda arguments : expression
# Der Ausdruck wird augeführt und das Ergebnis wird zurückgegeben
# Beispiel dazu:

x = lambda a : a + 10   # Es wird + 10 zum Argument a gerechnet
print(x(5))             # Damit wird 5 + 10 gerechnet

#-------------------------------------------------------------------------------------------------------
# Bei mehreren Argumenten und Multiplikation:

y = lambda a, b : a * b         # Multiplikation mit zwei Argumenten funktioniert wie gehabt
print(y(5, 6))                  # Ausgabe von 5 * 6 = 30

z = lambda a, b, c : a + b + c  # Nun sind es drei Argumente statt einem
print(z(5, 6, 2))               # Diese werden dann wie gehabt zusammen verrechnet

#-------------------------------------------------------------------------------------------------------
# Warum sollte man überhaput Lambda Funktionen verwenden?
# Gut zu sehen ist es wenn man Lambda nicht innerhalb einer Funktion sondern als annonyme Funktion
# verwendet. 
# Eine Funktionsdefinition hat ein Argument, dieses soll mit einer Unbekannten Zahl multipliziert werden
# Beispiel dazu:

def func(n):                    # Das n ist vordefiniert, aber das a ist die Unbekannte 
    return lambda a : a * n     # das gute ist das diese irgendwo im Code deklariert werden kann

# Damit kann man dann eine Funktion schreiben welche z.B. immer die Zahl verdoppelt

doubler = func(2)               # Also wird die 2 zu n und 11 zu a dementsprechend modular im Code

print(doubler(11))
#-------------------------------------------------------------------------------------------------------

trippler = func(3)              # Natürlich kann auch verdreifachen vierfachen usw.       

print(trippler(11))

# Das zeigt ganz gut warum Lambda so gut ist, man benötigt wie ^ oben ^ schon gesagt kein def mehr 

#-------------------------------------------------------------------------------------------------------
# Lambda mit eingebauten Funktionen
# Meisten werden Lambdafunktionen mit eingbeauten Funktionen wie map(), filter(), sorted() verwendet
# Beispiel mit map()
# map()  wendet vorher gewählte eine Funktion auf jedes Element in einer Iteration an

number = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, number))   # Wendet die doubled Funktion auf 1, 2, 3, 4, 5 an
print(doubled)

#-------------------------------------------------------------------------------------------------------
# List von Elementen erstellen per filter(), gibt True zurück

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))  # Wie der Name schon sagt "filtert" nach odd
print(odd_numbers)

#-------------------------------------------------------------------------------------------------------
# Sortieren nach festgelegtem Element per sorted()

students = [("Emil", 25), ("Tobias", 22), ("Hans", 28)]     # Sortiert hier nach dem Alter 
sorted_students = sorted(students, key = lambda x : x[1])   # x[0 = Name, 1 = alter]
print(sorted_students)


word = ["apple", "pie", "banana", "cherry"]                 # Sortiert nach Wortlänge
sorted_words = sorted(word, key = lambda x : len(x))        # len(x) = Länge der Elemente
print(sorted_words)                                         # Also pie = 3 chars, apple = 4 usw.

#-------------------------------------------------------------------------------------------------------
# Lambda Ende (Black Mesa)


