# Range
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Eine unveränderliche Sequenz von Zahlen, gänigerweise genutzt für Schleifendurchlauf
# Die Zahlen haben ihren eigen Datentypen range
# !Auffrischung! Unveränderlich heißt auch wirklich unveränderlich nach Erstellung

#-------------------------------------------------------------------------------------------------------
# Erstellen von ranges
# Die range Funktion kann mit 1, 2 oder 3 Argumenten aufgerufen werden, Syntax: range(start, stop, step)

#-------------------------------------------------------------------------------------------------------
# Aufruf von range mit !EINEM! Argument
# Das eine Argument repräsentiert den stop-Wert
# Der start Wert ist optional, falls nicht gegeben dann Standartmäßig mit 0 
# range(10) gibt eine Reihe von Zahlen 0 - 9 zurück (Das Start-Argument 0 ist einschließlich, das
# Stop-Argment 10 ist ausschließlich), eben wie bei Arrays

x = range(10)
print(x)        # Das gibt den Start-/Endpunkt der Reihe aus
print(list(x))  # Das gibt alle Elemente der Reihe als Liste aus


#-------------------------------------------------------------------------------------------------------
# Aufruf range mit !ZWEI! Argumenten
# Das erste Argument rerpräsentiert den start-Wert und das zweite den stop-Wert

y = range(3,10) # Gibt die Zahlen 3 !bis! 9 an
print(list(y))  # Wie ^ oben ^ die Elemente
print("\n")

#-------------------------------------------------------------------------------------------------------
# Aufruf range mit !DREI! Argumenten
# start-/stop-Werte gleich wie bei zwei Argumenten, hinzu kommt der step-Wert
# Dieser ist die differenz zwischen jeder Zahl in der Reihe, dieser ist optional, falls nicht gegeben
# ist der step-Wert standartmäßig auf 1

z = range(3, 10, 2) # Spring druch die Reihe in 2er Schritten 
print(list(z))      # Dementsprechend ist die Ausgabe 3, 5, 7, 9
print("\n")

#-------------------------------------------------------------------------------------------------------
# Anwendungsfall von range
# Es sollte aufgefallen sein das ranges meistens in for-Schleifen genutzt werden

for i in range(10): # Iteriert druch alle Elemente von 0 - 9
    print(i)
    
print("\n")

#-------------------------------------------------------------------------------------------------------
# Per Listen ranges anzeigen 
# Da ranges unveränderbar sind können diese auch nicht angezeigt werden, daher in Listen konvertieren

print(list(range(5)))           # 0 - 4
print(list(range(1, 6)))        # 1 - 5
print(list(range(5, 20, 3)))    # 5 - 20 mit 3er Sprüngen
print("\n")

#-------------------------------------------------------------------------------------------------------
# Schneiden von ranges, geht wie bei anderen Sequenzen, man erhält eine Subsequenz

r = range(10)                   # Liste erstellt von 0 - 9
print(r[2])                     # Gebe das Element an Index 2 der Reihe aus (es wird von 0 aus gezählt)
print(r[:3])                    # Erstellt neues range Objekt von Index 0 - 3 daher auch range(0, 3)

#-------------------------------------------------------------------------------------------------------
# Membership Testing
# Testen ob bestimmte Elemente innerhalb der Reihe sind z.B. 6 und 7 hier Code dazu:

a = range(0, 10, 2)             # Liste 0 - 9 mit 2er Sprüngen
print(6 in a)                   # Ist 6 in a ? Ja, durch die Sprünge 0 2 4 6 8
print(7 in a)                   # Ist 7 in a ? Nein, ungerade passt nicht in die geraden Sprünge

# Es wird bei zutreffen oder nicht-zutreffen True oder Flase ausgegeben

#-------------------------------------------------------------------------------------------------------
# Länge per len()

b = range(0, 12, 2)             # Mittlerweile selbsterklärend (Reihe von 0 - 12)
print(len(b))                   # Wie lang ist sie? Nicht 12! sondern 6, wir haben 2er Sprünge!

#-------------------------------------------------------------------------------------------------------
# Range Ende