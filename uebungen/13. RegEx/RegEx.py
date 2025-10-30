# RegEx 
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Regular Expression
# Ist eine Abfolge von charaktern welche ein Suchmuster bilden
# RegEx kann genutzt werden um zu schauen ob ein string das gesuchte Muster enthält
# Wird mit Beispielen klarer

#-------------------------------------------------------------------------------------------------------
# RegEx Module per import re

import re

#-------------------------------------------------------------------------------------------------------
# So wie nutzt man das jetzt und was macht es überhaupt, dafür ein Beispiel

txt = "Was ist der Sinn von RegEx"      # So hier ein normaler String
x = re.search("^Was.*RegEx$", txt)      # Über die Formatierung reden wir später: !Wichtiger! ist die
# Funktion davon, also ^Was und *RegEx$ bedeutet -> suche im string 1. nach Was und RegEx und 
# 2. Schau ob Was am Anfang und RegEx am Ende des Textes setehen!

if x:
    print("Yes we have a match")
else:
    print("No match :()")

#-------------------------------------------------------------------------------------------------------
# Da die Tabellen mit Erklärungen alle den selben Links haben gibt es den jetzt nur 1x 
# Daher bitte ich um bisschen Eigeninitiative
# Ich schreibe hin welche Tabellen ich gerade meine und du schaust dann da drauf, danke.
# Hier der Link: https://www.w3schools.com/python/python_regex.asp

#-------------------------------------------------------------------------------------------------------
# Dementsprechend haben wir erst einmal die RegEx Funktionen
# Wie ^ oben ^ wurde search schon genutzt, den Rest anschauen / selbst mal probieren

#-------------------------------------------------------------------------------------------------------
# Dann Metacharacters, diese sind normale Chars mit anderen Bedeutung 
# Wie im Beispiel dann hier der * für 0 oder weniger mal vorgekommen z.B.

#-------------------------------------------------------------------------------------------------------
# Flags, kam bei uns jetzt nichts vor, aber gibt es eben trotzdem, einmal anschauen

#-------------------------------------------------------------------------------------------------------
# Special Sequenzenes, ist ein \ mit einem der jeweiligen Angegebenen Chars der Tabelle
# Verwendung und Bedeutung anschauen

#-------------------------------------------------------------------------------------------------------
# Sets [] mit verschiedenen Bedeutungen 

# Tabelle Ende

#-------------------------------------------------------------------------------------------------------
# Die findall() Funktion, gibt alle Matches zurück als Liste

x = re.findall("inn", txt)  # Gibt eben hier alle Wörte aus welche den string "inn" enthalten
print(x)

# Fall es keine gibt wird eine leere Liste zurückgegeben

#-------------------------------------------------------------------------------------------------------
# Die search() Funktion, sucht im string nach einem match und gibt ein match Objekt zurück
# Falls mehr als ein match gibt wird nur das erste match ausgegeben (also da wo es zum ersten mal vorkam)

x = re.search("\s", txt)    # Sucht nach dem ersten white-space (also leer, tab, enter usw.)
print("The first white-space character is located in position:", x.start()) # Das erste leer an 3.Stelle

#-------------------------------------------------------------------------------------------------------
# Die split() Funktion, gibt eine Liste zurück wo der string bei jedem match geteilt wurde

x = re.split("\s", txt)     # Bei jedem white-space wird gesplited
print(x)

# Per maxsplit kann ma die Anzahl der Splits ändern
x = re.split("\s", txt, 1)  # Also nur einen Split
print(x)

#-------------------------------------------------------------------------------------------------------
# Die sub() Funktion, tauscht bei match mit eigenem Text aus

x = re.sub("\s", "MATCH", txt)      # Bei jedem match kommt jetzt ein MATCH also bei jedem white-space
print(x)                  

# Man kann auch die Anzahl der austausche ändern per count Parameter

x = re.sub("\s", "MATCH", txt, 1)       # Jetzt eben nur einmal white-space mit MATCH getauscht
print(x)

#-------------------------------------------------------------------------------------------------------
# Match Objekt
# In diesem befinden sich die Informationen/Inhalte des Suche und das Ergebnis davon
# !Wichtig! wenn es kein match gibt dann wird None zurückgegeben
# Beispiel erstmal wieder mit den selbem Text

x = re.search("as", txt)
print(x)    # Dieser print erstellt das Objekt

# Das match Objekt hat gewisse Eigenschaften und Funktionen um das Ergebnis der Suche zu erhalten
# .span()   -> gibt ein tuple zurück welches die Start-/Endposition des Matches enthält
# .string() -> gibt den angenommenen string in die Funktion zurück
# .group()  -> gibt genau den Teil des strngs zurück wo es den match gab

# Das führe ich hier nicht weiter aus und referenziere wieder auf den tollen Link ^ oben ^
# Dort sind noch die Beispiele für die drei Methoden einfach mal anschauen und ausprobieren 

#-------------------------------------------------------------------------------------------------------
# RegEx Ende