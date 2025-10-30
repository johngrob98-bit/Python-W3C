# Listen
#-------------------------------------------------------------------------------------------------------
# Sind Dynamische Arrays
# -> Speichern mehrere Elemente in eine einzelne Variable
# !!! Ganz wichtig: Listen sind ein Teil von Arrays es gibt 4 Unterschiedliche Arten davon (Unterarten)

# Listen sind eine Sammlung welche geordnert und veränderbar sind. Duplikate sind erlaubt

# Tuple sind eine Sammlung welche geordnet aber unveränderbar sind. Duplikate sind erlaubt

# Set sind eine Sammlung welche ungeordnet und unveränderbar sind. Es sind keine Duplikate erlaubt

# Dictionary ist eine Sammlung welche geordnet und veränderbar sind. Es sind keine Duplikate erlaubt

# Snytax: 

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Die Elemente sind: 
# 1. Sortiert 2. Austauschbar 3. Erlauben Duplikate der Werte 4. Elemente sind indexiert (nummeriert) 
# Startet wie ein Array bei Index[0] - Index[n]

#-------------------------------------------------------------------------------------------------------
# Die Elemente haben eine Definierte Reihenfolge und diese ändert sich nicht!
# -> Neue Elemente kommen ans Ende der Liste (Index[n + 'neues Element'])
# Es gibt Methoden welche die Reihenfolge ändern. Die Reihenfolge der Elemente bleibt aber gleich!

#-------------------------------------------------------------------------------------------------------
# Änderbarkeit der Liste:
# Syntax:

thislist2 = ["apple", "banana", "cherry", "apple", "cherry"] # Listen erlauben wie oben gesagt Duplikate
print(thislist2)                                             # Die haben den selben Wert