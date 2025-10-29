# Funktionsargumente
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Informationen können in Funktionen als Argumente eingetragen werden
# Argumente sind spezifiziert nach Funktionsname in den Klammern
# Es gibt kein Limit an der Anzahl der Argumente, diese müssen aber mit einem Komma getrennt werden

#-------------------------------------------------------------------------------------------------------
# Im Beispiel haben wir fname (also first name), wenn die Funktion aufgerufen wird wird der fname weiter
# -gegeben, welcher dann in der Funktion benutzt wird um den vollen Namen zu printen

def my_function(fname):             # Übergabe der first names per fname in den Klammern
    print(fname + "<- First name")  # die Funktion soll fname + den Text dahinter printen

my_function("Emil")                 # Da nur Emil drinne steht weiß der Compiler okay fname = first name
my_function("Tobias")               # Python selber kann nicht wissen was der first name ist !WICHTIG!
my_function("LinusTechTips")        # Die Logik des Codes zeigt dem Compiler eben was der first name ist


#-------------------------------------------------------------------------------------------------------
# Parameters vs Arguments
# Die beiden Wörter können für das selbe genutzt werden: Informationen in eine Funktion weitergeben
# ABER 
# Parameter: is the Variable welche in den Klammern der Funktionsdefinition ist
# Arguemte: is der eigentliche Wert welche übergeben wird bei Funktionsaufruf
# Beispiel dazu:

def functionex(name): # name ist der Parameter
    print("Hello", name)

functionex("Emil") # Emil ist das Argument

#-------------------------------------------------------------------------------------------------------
# Anzahl der Argumente
# !Wichtig! Eine Funktion erwartet eben genau so viele Argumente, sowie diese eben definiert wurde 
# Also 2 Argumente definiert -> 2 Argumente müssen gerufen werden
# Beispiel dazu:

def fullname(fname, lname):
    print(fname + " " + lname)

fullname("Ufuk", "Oezer") # Würde jetzt hier im print nur Ufuk stehen würde es einen Error geben

#-------------------------------------------------------------------------------------------------------
# Standartwerte
# Wenn man mal nicht weiß was für Werte man übergeben möchte aber die Funktion der Funktion testen will
# Dann nutzt man Standartwerte

def default(fname = "friend"): # Also wenn man nicht weiß wie ein Name sein soll steht da friend
    print("Hello " + fname)

default("Hans")
default()       # Und hier steht dann friend weil es eben leer ist
default("Kuni")
default("Hermann")

#-------------------------------------------------------------------------------------------------------
# Schlüsselargumente key = value (also Schlüsselwert = Wert)

def animal(animal, name):                       # Also zwei Argumente werden übergeben
    print("I have a", animal)                   # Ausgabe + Argument
    print("My", animal + " 's name is", name)  # Ebenso Argument 1 + Argument 2 in einem Satz

animal(animal = "cat", name = "Sailor")         # Und hier wird dann der Name definiert in der Funktion 
animal(animal = "cat", name = "Moon")           # Ja fr meine Katzen heißen so

# Die Reihenfolge der Argumente in der Funktion ist egal (also ob erst animal oder name ist egal)
# !Wichtig! noch dazu in Python wird Arguments mit args in Dokus abgekürzt

#-------------------------------------------------------------------------------------------------------
# Ruft man meine Funktion mit Argumenten ohne Schlüsselwörter nennt man das Positional Arguments
# Dies !müssen! in der richtigen Reihenfolge sein

def posanimal(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

posanimal("Cat", "Moon") # Da wir hier nicht genau definieren wird angenommen das Cat = animal ist 
# und Moon = name ist, daher ist die Reihenfolge wichtig 

posanimal("Moon", "Cat") # Das wird die Ausgabe verändern, einfach mal compilen
# Es wird die in der Funktion ^ oben ^ definierte Reihenfolge der Argumente angenommen

#-------------------------------------------------------------------------------------------------------
# Man kann Positional und Schlüsselwortargumente vermischen
# !Wichtig! dabei ist nur das die positional Arguments als ersten kommen !müssen! -> Reihenfolge!

def animalposarg(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

animalposarg("Cat", name = "Sailor", age = 3)  # Hier ist animal positional deswegen als erstes 

#-------------------------------------------------------------------------------------------------------
# Übergeben verschiedner Datentypen
# Egal welcher Datentyp, jeder kann übergeben werden
# Beispiel mit einer Liste

def my_funktion(fruits):    # Deklaration der Funktion mit fruits als Übergabeparameter / Argument
    for fruit in fruits:    # Jedes Element in fruits wird durchiteriert
        print(fruit)        # Und dann Ausgegeben 

my_fruits = ["apple", "banana", "cherry"]   # Hier Deklarieren wir die Elemente für my_fruits
my_funktion(my_fruits)                      # Die Funktion nimmt sich diese Werte und gibt die dann aus

#-------------------------------------------------------------------------------------------------------
# Besipiel mit einem Dictionary

def my_funktion1(person):           # Wieder das gleiche Deklaration mit Übergabe
    print("Name:", person["name"])  # Zugriff auf den Wert zum Schlüssel "name" 
    print("Age:", person["age"])    # Zugriff auf den Wert zum Schlüssel "age"

my_person = {"name": "Ufuk", "age" : 24}    # Dictionary mit zwei Schlüssel-Wert-Paaren
my_funktion1(my_person)                     # Übergabe des Dictionaries in die Funktion

#-------------------------------------------------------------------------------------------------------
# Rückgabe Werte (return values)

def my_function(x, y):
    return x + y

result = my_function(5, 3)  # Übergabe von x und y, diese werden dann hier mit Werten gefüllt
print(result)

#-------------------------------------------------------------------------------------------------------
# Die Übergabe funktioniert auch hier wieder mit verschiedenen Datentypen
# Hier eine Liste

def typelist():
    return ["Apple", "Samsung", "HUAWEI"]

phones = typelist()
print(phones[0])
print(phones[1])
print(phones[2])

# Hier ein Tupel

def typetuple():
    return(10, 20)

x,y = typetuple()
print("x:", x)
print("y:", y)

#-------------------------------------------------------------------------------------------------------
# Positional Only Arguments
# Man kann festlegen das es nur positional Arguments hat
# Das macht man mit ,/ dach den Argumenten in der Funktion

def posargs(name, /):       # <- nach dem name ein , / dann ist es richtig
    print("Hello", name)

    posargs("Ufuk")

# !Wichtig! ohne das , / ist es erlaubt das Schlüsselwortargument zu nutzten auch wenn ein positional
# Argument erwartet wird
# Ich spaare mir das ist die selbe Funktion nur ohne , / und in dem funktionsaufruf steht statt "Ufuk"
# dann name = "Ufuk"

#-------------------------------------------------------------------------------------------------------
# !Wichtig! dazu: Wenn man , / nutzt und dann im Aufruf aber posargs(name = "Ufuk") schreibt -> Error

#-------------------------------------------------------------------------------------------------------
# Keyword-Only Arguments
# Wenn die Funktion nur Schlüsselwörter haben sollen dann mit *, vor den Argumenten

def keyw(*,name):
    print("Hello", name)

keyw(name = "Ufuk")

# Ohne *, darf man positional Arguments benutzten 
# !Wichtig! nicht *, und positional zusammen in einem 

# def wrong(*, name):
#     print("Hello", name)

# wrong("Ufuk") <- wird ohne Fehler angezeigt, also je nach IDE

#-------------------------------------------------------------------------------------------------------
# Als letztes Verbindung von positional und keyword-only 
# Das geht mit /

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#-------------------------------------------------------------------------------------------------------
# Funktionsargumente Ende