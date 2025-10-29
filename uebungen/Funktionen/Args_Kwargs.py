# Arguments und Keywordarguments
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Das selbe wie bei Funktionen schon, es !müssen! die Richtige Anzahl an Argumenten
# gerufen werden damit die es keinen Error gibt
# Aber da man nicht immer weiß wie viele Argumente oder Schlüsselargs man benötigt, gibt es als 
# Abhilfe dafür *args und **kwargs

#-------------------------------------------------------------------------------------------------------
# Arbitraty Arguments (beliebige Argumente)
# Wie schon ^ oben ^ gesagt wenn man die Anzahl nicht weiß, so füge man einen * hinzu

def arbitary(*tanks):               # Durch das * erhält die Funktion ein Tupel an Arugmenten
    print("The most british tank is " + tanks[1])   # Das hält die Funktion modular
                                                

arbitary("Jumbo Sherman", "Sherman-Firefly", "Sherman") # Dann eben noch einsetzten der Arguemnte

# In Python dokus wird das ganze meistens als *args geschrieben

#-------------------------------------------------------------------------------------------------------
# Was ist überhaput *args
# Erlaubt der Funktion, so viele Werte anzunehemen wie sie eben braucht -/ will
# Und wie schon gesagt die Argumente werden zu Tupeln, diese enthalten die übergebenen Arguemnte

def function(*args): # <- Erstelle mal das Tupel
    print("Type:" , type(args))         # Anzeigen das Datentypen (Wie man sieht, es wird zum Tupel)
    print("First argument:", args[0])   # Tupel befüllen / "Aufspannen"
    print("Second argument:", args[1])  # ""
    print("All argument:", args)        # Alles ausgeben

function("Mouse", "Keyboard", "Monitor")    # Elemente Definieren
print("\n")

#-------------------------------------------------------------------------------------------------------
# Auch reguläre Parameter können mit *args verbunden werden
# !Aber! die Parameter müssen vor dem *args kommen

def param(greeting, *names):    # Erst greeting (Parameter), dann *args (names)
    for name in names:          # for Schleife um durch die Namen zu iterieren
        print(greeting, name)   # Ausgabe von unten Hello und dann die Namen

param("Hello", "LinusTechTips", "Grohnk", "PewdDiePie") # Keine Ahnung bei den Namen mir fällt nix ein
print("\n")

#-------------------------------------------------------------------------------------------------------
# Jetzt noch zwei Beispiele dazu:

def numb(*numbers):         # Summe beliebiger Elemente
    total = 0               # Ist die Summe der Elemente
    for num in numbers:     # Schleife iteteriet wieder durch die Elemente
        total += num        # Die Elemente werden addiert und das Ergebnis kommt in die Summe
    return total            # Weitergeben -/ Rückgabe der Summe
    
print(numb(1, 2, 3))        # Eben Modular durch *numbers
print(numb(10, 20, 30, 40)) # Man kann so viel hinzu -/ entfernen wie man möchte
print(numb(5))
print("\n")

#-------------------------------------------------------------------------------------------------------
# Beispiel zwei Maximum:

def max(*numbers):          # So wie immer 
    if len(numbers) == 0:   # Prüfen ob Argumente vorhanden sind
        return None         # Wenn keine Argumente vorhanden sind wird None ausgegeben
    max_num = numbers[0]    # Initialisiert das Maximum mit dem ersten Wert (wird eh überschrieben)
    for num in numbers:     # Iteriere durch die Argumente in numbers
        if num > max_num:   # Wenn die num > max_num (was ja gerade 0 ist) dann max_num = num
            max_num = num   # Das ganze geht so lange bis die Schleife einmal durchgelaufen ist
    return max_num          # Dann sind alle Elemente abgedeckt und verglichen worden und damit return

print(max(3, 7, 2, 9, 1))   #Ausgabe Maximum

#-------------------------------------------------------------------------------------------------------
# Arbitary Keyword Arguments (das selbe gibt es eben auch für Schlüsselargumente) 
# **kwargs
# Gleiches Prinzip: Wenn man nicht weiß wie viele Schlüsselargumente man benötigt dann ** vor Parameter
# -> Statt Tupel ist es hier ein Dictionary

def children(**kid):        # Also zwei ** für Schlüsselargumente
    print("His last name is " + kid["lname"])   # Dann wird ein Dictionary erstellt

children(fname = "Ufuk", lname = "Özer")        # Ausgabe mit Deklaration der Argumente
print("\n")

#-------------------------------------------------------------------------------------------------------
# Was sind **kwargs
# Eben das gleiche wie *args, nur das hierbei ein Dictionary statt Tupel erstellt wird

def kwargs(**var):          # Erstellung des Dictionaries
    print("Type:", type(var))   # Anzeigen welchen Datentypen wir haben (eben class dict)
    print("Name", var["name"])  # Anfügen der Argumente
    print("Age:", var["age"])   # ""
    print("All data:", var)     # Hier wird dann alles angezeigt, auch was in functioncall hinzu kommt

kwargs(name = "Ufuk", age = 25, city = "Buchloe")   # Man kann eben beliebig viel hinzufügen dadurch
print("\n")

#-------------------------------------------------------------------------------------------------------
# Und auch hier kann man **kargs mit regulären Argumenten verbinden
# Selbe Regel erst Parameter dann **kwargs

def login(username, **details):     # Prinzipell das selbe, dieses Beispiel ist aber komplexer 
    print("Username:", username)    # Ausgabe des Benutzernamens
    print("Additional details:")    # "" zusätzliche Details
    for key, value in details.items():  # Iteriere jedes Argument im Dictionary durch: also age, hobby 
        print(" ", key + ":", value)    # usw. value ist dann der Wert dahinter also age = 25 <- value
login("oezeru", age = 25, city = "immernoch Buchloe", hobby = "atmen")  # Dafür ist die details-items()
# Funktion da, das erlaubt wiederum, so viele Elemente hinzuzufügen wie man möchte 
# Dann kommt nurnoch die Ausgabe davon "" <- Key (Argument) : value <- der Wert welcher das Arg annimmt
print("\n")

#-------------------------------------------------------------------------------------------------------
# *args und **kwargs können verbunden werden
# !Wichtig! es gibt eine definierte Reihenfolge!
# 1. reguläre Parameter
# 2. *args
# 3. **kwargs
# Beispiel dazu:

def combine(title, *args, **kwargs):         # Erst Parameter, dann args, zum Schluss kwargs
    print("Title:", title)              
    print("Positional arguments:", args)    # Im Funktionsaufruf sieht man gut welche Args pos sind
    print("Keyword arguments", kwargs)      # und welche die Schlüsselargumente sind

combine("User Info", "Ufuk", "Özer", age = 25, city = "Wie oft soll ich noch Buchloe schreiben")
print("\n")
# Dementsprechend siehe da, man kann modular hinzufügen und kombinieren
#-------------------------------------------------------------------------------------------------------
# Unpacking Argument ("auspacken")
# Der * und ** Operator können auch bei Funktionsaufruf genutzt werden um Listen oder Dictionaries in
# seperate Argumente zu entpacken (vergrößern)
# Höhrt sich komisch an daher ein Beispiel:
# Erstmal mit *

def unpack(a, b, c):    # 3 Normale Variablen übergeben
    return a + b + c    # Rückgabe der Summe

numbers = [1, 2, 3]     # Liste erstellt
result = unpack(*numbers)   # Ist das gleiche wie unpack(1, 2, 3)
print(result)           # Das Ergebnis wird von Liste zu normalen Argument durch *numbers Aufruf

#-------------------------------------------------------------------------------------------------------
# Selbes jetzt mit **

def unpack2(fname, lname):      # Bis hier alles normal nur die Argumente sind in keinem Dictionary
    print("Hello", fname, lname)   # Ausgabe der Parameter

person = {"fname": "Ufuk", "lname": "Özer"} # Dictionary deklariert und initialisiert
unpack2(**person) # Auch hier wieder das selbe wie unpack2(fname = "Ufuk", lname = "Özer")
# ^ hier ^ geht das eigentliche unpacking los: Funktionsaufruf -> unpack Dictionary in Argumente
# Einfach mal Compilen und rumspielen (Namen, Werte, Alter usw. hinzu-/entfernen), type anzeigen lassen 

#-------------------------------------------------------------------------------------------------------
# !Wichtig! nutze * und ** in Funktionsdefinitionen um Argumente zu erhalten
# In Funktionsaufrufen um Argumente zu "entpacken" (von List, Dict zu regulären Argumenten)

#-------------------------------------------------------------------------------------------------------
# Args und Kwargs Ende