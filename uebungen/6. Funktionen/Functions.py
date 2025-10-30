# Funktionen
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Funktionen "funktionieren" nur wenn sie "gerufen" werden
# Funktionen übergeben Daten als ein Ergebnis
# Und am wichtigsten sie verhindern wiederholung im Code

#-------------------------------------------------------------------------------------------------------
# Um eine Funktion überhaput erst benutzten zu können muss diese defniniert werden
# Definition der Funktion per def
# Funktionen werden immer mit einer Klammer am Ende definiert (später werden dann Parameter übergeben)

def greet():
    print("Hallo ich bin eine Funktion\n")

# Einmal definiert und damit kann man diese dann immer überall aufrufen per greet()
# Wird bei Klassen sehr nützlich

#-------------------------------------------------------------------------------------------------------
# Da wir die Funktion nun definiert haben können wir diese jetzt auch aufrufen 

greet() # <- Drei Aufrufe = 3x Hallo ich bin eine Funktion 
greet()
greet()

#-------------------------------------------------------------------------------------------------------
# Namensgebung !Wichtig!
# Funktionsnamen starten mit einem Buchstaben oder einem Unterstrich
# Der Name darf nur Buchstaben Zahlen und Unterstriche enthalten
# Case Sensitive !!!! also greet() und Greet() sind 2 verschiedene Funktionen
# Und bitte benennt Funktionen und Variablen bitte sinnvoll also nicht func1 func2 func3 usw sondern
# Benennung nach funktion der Funktion, ebenso für Variablen danke.

#-------------------------------------------------------------------------------------------------------
# Ein Anwendungsbeispiel für Funktionen Fahrenheit in Celsius umrechnen 
# Damit man das nicht 100x selber machen muss, schreibt man sich eine Funktion die das für einen macht

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# So ist es ohne, relativ lang und mühsam
#-------------------------------------------------------------------------------------------------------
# Jetzt mit Funktionen

def fahrenheit_to_celsius(fahrenheit):# Hier wird direkt fahrenheit übergeben das eben das returned wird
    return(fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))    # Und so hat man dann die 3 Berechnungen in einer ganzen
print(fahrenheit_to_celsius(95))    # Das return ist wie gesagt dafür da damit überhaput ein Ergebnis 
print(fahrenheit_to_celsius(50))    # rauskommt, die 77 95 50 werden dann nur noch Eingetragen und fertig

# Man übergibt also immer den Wert in welcher dann im Ergebnis stehen soll

#-------------------------------------------------------------------------------------------------------
# Jetzt noch ein bisschen genauer zu den return Werten

def get_greeting(): # Hier wird in der Funktion erstmal nichts übergeben das kommt drunter
    return "Hello from a function\n"    # Die Funktion übergibt also Hello from a function 

message = get_greeting() # Jetzt sagen wir die Variable message (hier ein String) ist jetzt die Funktion
print(message)           # Also wird nun die "Funktion" oder eher gesagt die message geprinted

# Also kommt Hello from a function dabei raus

#-------------------------------------------------------------------------------------------------------
# Nun kann man aber auch den zurückgegebenen Wert direkt benutzten (sprich direkt die Funktion nutzen)
# Weil ^ oben ^ ist jetzt gerade wenig Unterschied zur normalen Schreibweise
# Daher so:

def get_greeting():
    return "Hello from a function\n"
print(get_greeting()) # So wird die Funktion direkt übergeben

# Das ist sehr Hilfreich sobald gerechnet wird da man damit Ergebnisse direkt weitergeben kann ohne sie
# erneut deklarieren oder weitergeben zu müssen so geht das in einem Schritt
# !Wichtig! wenn eine Funktion keinen return Wert hat geht diese automatisch auf None (also null) zurück

#-------------------------------------------------------------------------------------------------------
# Funktionsdefinitionen dürfen nicht leer sein daher auch hier wieder pass

def my_function():
    pass # Gibt wie bei allem anderen keinen Compilefehler

#-------------------------------------------------------------------------------------------------------
#