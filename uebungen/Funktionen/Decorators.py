# Decoratos
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Dekotratoren fügen einer Funktion zusätzliches Verhalten hinzu, ohne den Code zu ändern
# Decorator ist eien Funktion, die eine andere Funktion als Eingabe erhählt
# und dann eine neue Funktion zurückgibt
# Dekoratoren haben mich gebrochen frfr

#-------------------------------------------------------------------------------------------------------
# Dekoratoren erst definieren und dann per @decorator_name über der Funktion anwenden
# Beispiel dazu (der Dekorator fügt uppercase funktion hinzu):

def changecase(func):           # Uppercase Funktion, Dekorator nimmt Funktion entgegen
    def inner():                # Innere Funktion, die das Verhalten verändert
        return func().upper()   # Eingabe wird in UPPER CASE geschrieben
    return inner                # Gibt die neue "dekorierte" Funktion zurück

@changecase                 # nach dem @ <- gibt den jeweiligen Funktionsnamen an, wird angewendet
def function():             # Das hier ist die "Hauptfunktion" an sie wird uppercase gehangen
    return "Hello guys"     # Der String wird dann über die changecase Funktion einmal durchgelassen

print(function())           # Damit wird die Ausgabe HELLO GUYS

# Also ist somit changecase der decorator
# Und function wird mit ihr decorated
# Man sieht damit, die Funktion selber wurde nicht geändert, sonder bleibt seperat
# Durch das "dekorieren" wird der Rückgabewert automatisch in uppercase umgewandelt

#-------------------------------------------------------------------------------------------------------
# Jetzt geht das natürlich auch mit mehreren decorator calls, changecase kann auf alle Funktionen im 
# Code angewendet werden

@changecase
def otherfunction():
    return "I am speed!"

print(otherfunction())
print("\n")

# Das ist eben für alle Funktion replizierbar, ist im Endeffekt nix anderes wie in Java
# Methodenanwendung z.B. Array.getLength(), nur das hier eine Funktion eine andere erweitert

#-------------------------------------------------------------------------------------------------------
# Argumente in einer decorated Function
# Auch Funktionen mit Parametern können dekoriert werden, !Wichtig! ist nur, dass die Argumente an die 
# Wrapper-Funktion (also die umhüllende Funktion) übergeben werden
# Jetzt noch eine gesonderte changecase Funktion mit Argumenten

def changecasearg(funcarg):         # Dekorator nimmt eine Funktion mit einem Argument entegen
    def innerarg(x):                # Innere Funktion die das Argument x übernimmt
        return funcarg(x).upper()   # Führt die ursprüngliche Funktion mit x aus und macht uppercase
    return innerarg                 # Gibt neue "dekorierte" Funktion zurück 

@changecasearg                      # Dekorator wird auf function2() angewendet
def function2(nam):                 # Die Hauptfunktion, die einen Namen entgegenimmt (daher nam)
    return "Hello " + nam           # Ist glaube klar, Hello + Name

print(function2("Ufuk"))            # Ausgabe in upper case 

# Da ich selber durcheinander gekommen bin, noch ein kurzer (langer) Einschub zu dieser Funktion
# -> funcarg ist genau der Teil der Funktion welcher im Endeffekt alles macht es steht nämlich so
# funcarg("Ufuk").upper() das ist der Teil welcher die Argumente also x aufnimmt und weitergibt danach
# So kann der Dekorator das Ergebnis verändern, ohne die Originalfunktion zu ändern


#-------------------------------------------------------------------------------------------------------
# *args und **kwargs in diesem Kontext:  
# Manchmal hat die Dekorator Funktion keine Kontrolle darüber, welche Argumente von der "dekorierten" 
# Funktion übergeben werden. Um das zu beheben fügt man *args und **kwargs an die wrapper Funktion hinzu
# Damit kann die wrapper dann alle Zahlen und alle typen von Argumenten annehmen, und diese an die 
# "dekorierten" Funktion weitergeben
# Beispiel dazu: "Sicherung" per *args und **kwargs

def changecase1(func1):             # Prinzipell das selbe wie ^ oben ^
    def inner1(*args, **kwargs):    # Nur werden hier dann *args und **kwargs gesetzt für modularität
        return func1(*args, **kwargs).upper()   # Funktion bleibt gleich
    return inner1                   # Das return auch

@changecase1
def my_function(name):
    return "Hello " + name

print(my_function("Ufuk"))          # Hier könnten dann dementsprechend mehr Arugmente hinzukommen

#-------------------------------------------------------------------------------------------------------
# Mehrere Decorators
# Natürlich gehen mehrere in einer Funktion, das macht man indem man die decorator calls übereinander
# stellt. Decorators werden in umgekehrter Reihenfolge gerufen, gestartet wird mit dem welcher am 
# nächsten an der Funktion ist also 
# @dec1
# @dec2
# @dec3
# function()      <- also dec3 als erstes

def addgreeting(func):  # Also der Dekorator möchte eine Funktion ändern also (func)
    def myinner():      # wrapper Funktion in welcher der eigentliche Code steckt
        return "Hello " + func() + " have a good day!"  # Rückgabe von Hallo + myfunction1() also steht
    return myinner      # dort dann myfunction1 = addgreeting(myfunction) eben weil Dekorator func
                        # erwartet, daher wird der Code welcher in der wrapper ist darüber ausgeführt
@changecase
@addgreeting            # Hier wird als erstes addgreeting-Decorator ausgeführt
def myfunction1():      # Dann die Hauptfunktion welche nicht geändert wird übergibt ja "Ufuk"
    return "Ufuk"       # das geht dann in den decorator rein und von dort in die wrapper Funktion
                        # da wird dann uppercase und greeting hinzugefügt und über print ausgegeben
print(myfunction1())    # !Wichtig! bei der Reihenfolge: myfunction1 = changecase(addgreeting(myfunc1))
                        # Also erst greeting dann uppercase steht zwar ^ oben ^ aber snytaktisch jetzt

#-------------------------------------------------------------------------------------------------------
# Funktionen in Python haben Metadaten (nicht so wichtig was das ist)
# Auf diese Daten können per __name__ und __doc__ zugegriffen werden

def yourfunc():
    return "Have a great day!"

print(yourfunc.__name__)    # Damit bekommt man den Namen der Funktion also hier yourfunc

# Bei einer decorated Funktion werden die "originalen" Metadaten gelöscht
# Die bekommt man nur mit functool.wraps zurück
# Das muss importiert werden per import functools

import functools

def changecasetool(func):   # Bleibt gleich
    @functools.wraps(func)  # Jetzt kommt functools.wraps hinzu, das behält die "originale From" 
    def yourinner():        # des Codes bevor decorated wird
        return func().upper()   # alles andere bleibt gleich
    return yourinner

@changecasetool
def hisfunction():
    return "Have a great day!"

print(hisfunction.__name__) # Und damit hat man den Namen der Funktion

#-------------------------------------------------------------------------------------------------------
# Decoratoren Ende (endlich)
