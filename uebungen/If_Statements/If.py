# If Statements
#-------------------------------------------------------------------------------------------------------
# Allenvoran if = wenn. Soblad man die Bedingung schreibt immer im Kopf vorsagen ob es Sinn ergibt
# Grundlegendes 
# Syntax: 
# a == b    <- gleich
# a != b    <- ungleich
# a < b     <- kleiner als 
# a > b     <- größer als
# a >= b    <- größer gleich
# a <= b    <- kleiner gleich
# Offensichtlicherweise startet man ein if mit ... if (wow)
# Bei if gibt es keine {} man trennt mit :
#-------------------------------------------------------------------------------------------------------
# Beispiel dazu (auch wenn in den anderen Kapiteln schon welche waren)

a = 33 
b = 220

if b > a:
    print("b is greater than a")

# If Statements bewerten nach Wahrheitswerten also da 220 > 33 ist -> True aber 33 > 220 -> False

#-------------------------------------------------------------------------------------------------------
# !Wichtig! Es muss nach dem : eine neue Zeile und eingerückt werden, sonnst Syntaxerror
#-------------------------------------------------------------------------------------------------------
# Mehrere Statements in einem If Block

age = 24
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal right")
# Ist selbst erklärend

#-------------------------------------------------------------------------------------------------------
# Boolsche Variablen funktionieren als Bedingungen (da if so oder so in bool "denkt")

is_logged_in = True
if is_logged_in:
    print("Welcome Back")
# Also kann man auch mit Wahrheitsabfragen eine Wahrheitsabfrage machen wer hätte es gedacht
# !Wichtig! hierbei: 0 "" None sind leere Sammlungen und damit False alles andere ist True
# Auch negative Zahlen wie -8 oder positive Zahlen wie 3 und nicht leere Strings sind erstmal True 
# Je nach Bedingung ändert sich das erst (Alles außer 0, "", None ist True)

#-------------------------------------------------------------------------------------------------------
# Elif (Else If, else bekommt ein eigenes Kapitel)
# Ist dafür da um mehrere Bedingungen nacheinander zu prüfen
# Sobald eine Bedingung erfüllt ist, wird der Entsprechende Block ausgeführt und der rest wird geskipt

a = 33
b = 33
if b > a:
    print("b is greater than a") # Also wenn dem so ist dann mach das 
elif a == b:
    print("a and b are equal") # Wenn nicht das hier 
# Hier trifft das elif zu, einfach mal das a oder b größer-/ kleiner machen dann sieht man es gut

#-------------------------------------------------------------------------------------------------------
# Mehrere Elif Statements, hier sieht man dann die wirkung von Elif

score = 75

if score >= 90:     # Erstmal das If, wird nie in Kraft treten in diese Konstalation
  print("Grade: A") # Dann wird unterteilt in Noten A B C D je nach dem Score 
elif score >= 80:   # Daher auch die Elif Bedingungen
  print("Grade: B") # Die Note liegt zwischen C und B daher treten nun die >= <= Vergleiche in Kraft
elif score >= 70:   # Da der Score nicht >= 80 ist fällt der Fall weg 
  print("Grade: C") # 75 >= 70 Daher Grade C
elif score >= 60:
  print("Grade: D")

#-------------------------------------------------------------------------------------------------------
# Funktionsweise von Elif: 
# Python / Compiler geht von oben nach unten alle Fälle durch, sobald ein Fall zutrifft fallen alle
# anderen Fälle raus wie ^ oben ^ Grade D ist garnicht mehr im Rennen
# Nur der !erste wahre! Fall wird ausgeführt, !WICHTIG! selbst wenn mehrere wahr sind wird nur der !1.!
# Fall ausgeführt
#-------------------------------------------------------------------------------------------------------
# Wann sollte man Elif benutzten? 
# Sobald man mehrere sich gegenseitig ausschließende Bedingungen überprüfen will
# Ist besser als mehrere einzel if-checks da wie gesagt Python nach der ersten zutreffenden Bedingung 
# auffhört weitere Bedingungen / Fälle zu checken
# Beispiel dazu

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
#-------------------------------------------------------------------------------------------------------
# If Ende
