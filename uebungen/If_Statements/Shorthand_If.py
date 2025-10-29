# Shorthand If (KURZHANDIF)
#-------------------------------------------------------------------------------------------------------
# Grundlegendes:
# Verkürzte Schreibweise von if else Verkettung

a = 10
b = 20
bigger = a if a > b else b # Hier kommen gleich einige neue Sachen
print("Bigger is", bigger) # Ternärer Operator zweier Bedingungen
# Einfacher gesagt <true_wert> if <bedingung> else <false_wert>
#Erklärung
#-------------------------------------------------------------------------------------------------------
# Also Fall a -> Daher auch a if ... Wenn dieser Fall eintrifft dann ist a true 
# Else Fall b -> Da ja a in diesem Fall dann false ist trifft b ein (confusing is weiß b ist eig false)
# a ist der Wert wenn die Bedingung wahr ist a > b <- in dem Beispiel also nein
# b ist der Wert denn die Bedingung falsch ist a > b <- hier also ja da 10 !> 20 ist
# Also wird die Ausgabe Bigger is b sein

# Pythons eigene Syntax dazu: variable = value_if_true if _ condition else value_if_false 
# -> Denke ^ oben ^ ist bissle verständlicher 

#-------------------------------------------------------------------------------------------------------
# Mehrere Bedingungen in einer Zeile
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Hier werden direkt 2 Abfragen in eine Zeile geschrieben, funktioniert aber analog wie Normale If Else
# Nicht verwirren lassen, Python printed von links nach rechts
# Also Fall 1ter a > b false daher printed er = 2ter Fall tritt nicht mehr in Kraft warum?
# Wie im Else Kapitel schon gesagt, sobald 1 else = True wird aufgehört zu printen

#-------------------------------------------------------------------------------------------------------
# Jetzt noch weitere Beispiele 

x = 15
y = 20
max_value = x if x > y else y # Selbes Spiel wie ^ oben ^ 
print("Maximum value:", max_value)
# Wenn x > y wahr dann wird der Wert von x in max_value geschrieben 
# Wenn x > y falsche dann wird y in max_value geschrieben

#-------------------------------------------------------------------------------------------------------
username = ""
display_name = username if username else "Guest" # Wieder gleich
print("Welcome", display_name)
# Wenn username wahr dann wird aus display_name der jeweilige username
# Wenn username falsch wird aus display_name Guest
# Hier wird die Ausgabe Welcome Guest weil username leer ist -> "" = false bei Bedingungen

#-------------------------------------------------------------------------------------------------------
# Wann sollte man Shorthand-If verwenden?
# Bei einfachen Bedingungen
# Wenn es die Lesbarkeit des Codes verbessert (finde ich garnicht lol)
#-------------------------------------------------------------------------------------------------------
#Shorthand-If Ende
