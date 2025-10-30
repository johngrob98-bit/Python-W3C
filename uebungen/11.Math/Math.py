# Mathe
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Python hat eine Handvoll eigener Mathematischer Funktionen

#-------------------------------------------------------------------------------------------------------
# Hier mal ein paar der gängigsten (für mehr einfach in die Python Dokumentation schauen)
# min() max()

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#-------------------------------------------------------------------------------------------------------
# abs() Absoluter positiver Wert einer Zahl

z = abs(-7.25)

print(z)

#-------------------------------------------------------------------------------------------------------
# pow(x,y) x^y

a = pow(4, 3)

print(a)    # 4 * 4 * 4

#-------------------------------------------------------------------------------------------------------
# Math Module per import math
# Auch hier wieder in die Dokumentation schauen für bestimmte Funktionen

import math

# Hier wird nach oben und unten gerundet
b = math.ceil(1.4)
c = math.floor(1.4)

print(b)
print(c)

# Hier ist die Wurzel 
d = math.sqrt(64)

print(d)

#-------------------------------------------------------------------------------------------------------
# Wie gesagt, Python selber hat die meisten Mathematischen Funktionen in der eigenen Library 
# Ich empfehle trotzdem mal diese ganzen Funktionen per Hand zu schreiben (am besten auch mal Rekursiv)

#-------------------------------------------------------------------------------------------------------
# Math Ende