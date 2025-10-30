# Userinput
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Programmieren ohne Benutzereingaben wäre nicht so gut
# Daher geht das mit der Funktion input()

#-------------------------------------------------------------------------------------------------------
# Beispiel

print("Whats your first name?")
fname = input()
print(f"Hello {fname}")     # Kann auskommentiert werden wenn man unten kompilieren will

#-------------------------------------------------------------------------------------------------------
# !Wichtig! Python hört auf das Programm auszuführen solange noch kein Input des Benutzers da ist
# sobald das geschieht geht läuft Programm wieder weiter

#-------------------------------------------------------------------------------------------------------
# Die input() Funktion hat den prompt Parameter, diesen kann man in die selber Zeile tun wie Variable

lname = input("Enter your last name: ") # Die Variable erhält über Input dann den Parameter
print(f"Hello {fname} {lname}")         # Hier ist schon mehrfach input beinhaltet
print("\n")

# Da kann man dann eben alles sauber in einer Zeile machen

#-------------------------------------------------------------------------------------------------------
# Zahlen eingeben
# Die Eingabe wird als string behandelt, deswegen muss dieser konvertiert werden

import math

x = input("Enter a number: ")

y = math.sqrt(float(x)) # Die Eingabe aus x wird dann hier von string in float konvertiert

print(f"The square root of {x} is {y}")
print("\n")

#-------------------------------------------------------------------------------------------------------
# Es ist good-practice dafür zu sorgen das der Benutzer auch nur das eingeben kann was vorgesehen ist
# Also z.B. bei einer positiven berechnung halt auch nur positive Zahlen
# Das deckt man meisten mit if oder while ab, am besten mit try und exception

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again")

print("Thank you")

#-------------------------------------------------------------------------------------------------------
# Userinput Ende