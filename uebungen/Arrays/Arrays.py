# Arrays
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: !Wichtig! Python selber hat keine Unterstützung für Arrays -> Listen benutzten
# Falls man unbedingt Arrays benutzten will empfiehlt es sich die NumPy Libary zu importieren

#-------------------------------------------------------------------------------------------------------
# Arrays werden dafür genutzt mehrere Werte in eine Variable zu schreiben

cars = ["Ford", "GMC", "Jeep"]      # <- Man kann auf alle 3 Elemente zugreifen über eine einzige

#-------------------------------------------------------------------------------------------------------
# Die jeweiligen Elemente erlangen

x = cars[0]     # <- Erstellt sich eine Variable und nimmt den jeweiligen Index des Elements
print(x)        # Siehe da, jetzt habe ich einen Ford

#-------------------------------------------------------------------------------------------------------
# Ändern eines Arrayeintrags

cars[0] = "Dodge"   # Damit wird aus Ford dann Dodge
print(cars)

#-------------------------------------------------------------------------------------------------------
# Länge eines Arrays per len()
# Genau wie bei Listen

x = len(cars)
print(x)        # Nicht !vergessen! die Länge und die der Index! Länge = Anzahl der Elemente
                # Index = Position im Array !WIR FANGEN VON 0 AN ZU ZÄHLEN!

#-------------------------------------------------------------------------------------------------------
# Bevor ich die ganzen Methoden nocheinmal aufschreibe, (sind die selben) gibt es einen Link:
# https://www.w3schools.com/python/python_arrays.asp

#-------------------------------------------------------------------------------------------------------
# Arrays Ende (für mehr einfach nochmal ins Listen-Kapitel schauen)