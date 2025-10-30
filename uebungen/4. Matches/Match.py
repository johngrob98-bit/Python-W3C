# Match
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: 
# Statt viele if und else zu schreiben kann man auch ein match nutzten
# Im Endeffekt ist match der switch case aus Java C C++ usw.

#-------------------------------------------------------------------------------------------------------
# Beispiel dazu

# match expression:
#   case x:
#       code block
#   case y:
#       code block
#   case z:
#       code block

# Und so funktioniert es:
# match wird einmal ausgewertet (also einmal für alle cases)
# Der Wert des Ausdruckes wird mit den Werten der cases verglichen
# Wenn es ein match gibt wird der jeweilig gematchte code block ausgeführt
#-------------------------------------------------------------------------------------------------------
# Jetzt ein Code Beispiel dazu (wie gesagt ist wie bei switch cases nur ohne den ganzen fluff)

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wensday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# So da unser day = 4 ist, wird Donnerstag geprinted das match wertet die Variable day aus 
#-------------------------------------------------------------------------------------------------------

# Jetzt gibt es noch default values _ mit Unterstrich gezeichnet (Standart Werte)
# Diese sind für den Fall wenn es keine matches gibt, dann wird der _ ans Ende des Codes gesetzt

month = 3
match month:
    case 2:
        print("Febuary")
    case 4:
        print("April")
    case _:
        print("I love december")

# Hier ist also der match März, den case gibts nicht aber mit dem Unterstrich wird dann trotzdem gematched
# !Wichtig! der Unterstrich muss ans Ende also als letztes dran kommen sonnst kein match!

#-------------------------------------------------------------------------------------------------------
# Wenn man mehrere Werte in einem Case abprüfen will dann mit |

day = 5
match day:
    case 1 | 2 | 3| 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("Its the weekend")

# Hier gruppiert man direkt die Woche und das Wochenende zusammen 
# Man sieht auch schön wie die Gruppierung den code vereinfacht

#-------------------------------------------------------------------------------------------------------
# Torzdessen kann man natürlich auch weiterhin ifs in die Cases einbauen 

month = 4
day = 9
match day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 if month == 4:
        print("Its my Birthday lol")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 if month == 5:
        print("A weekday in May")
    case _:
        print("no match")
# Wie man hier schön sieht cases mit ifs 
# Es wird erstmal abgefragt ob der day im case ist, und anschließend per if gechecked ob der Monat passt
# Das geht dann im zweiten case genau so weiter -> würde oben nämlich month = 5 sein dann ist es Mai
# Und natürlich wieder Unterstrich bei no match
# -> Das alles wäre mit Eingaben vom Benutzer ersichtlicher, da eben nur das compielt wird was stimmt

#-------------------------------------------------------------------------------------------------------
# match Ende