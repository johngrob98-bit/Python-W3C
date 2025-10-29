# Sortierverfahren Listen
#-------------------------------------------------------------------------------------------------------

# Listen Alphanummerisch sortieren (a1 a2 b1 b2 usw ist Alphanummerisch)

# Alphabetisches sortieren
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # Die Methode übernimmt das sortieren
print(thislist)

# Nummerisches sortieren
thislist1 = [100, 50, 65, 82, 23]
thislist1.sort() # hier wieder das gleiche
print(thislist1)

# Von "oben nach unten" (einfach kompilen)
thislist2 = [200, 78, 20, 192, 23, 1]
thislist2.sort(reverse = True) # Geht vom höchsten Element (bei Zahlen) und sortiert in descending order
print(thislist2)

# Anpassen der Sortierfunktion
# geht mit den Argument key = function
# Beispiel dazu: Sortiert die Liste, anhand welcher Zahl am nähesten an 50 ist

def myfunc(n):  # Erstellen einer Funktion
    return abs(n - 50) # n sind die Elemente kann auch x,y,z usw sein wird oben in myfunc definiert
# Rechnet Element - 50 und schaut welches der Elemente die kleinste Differenz hat und sortiert dann
thislist3 = [100, 50, 38, 10]
thislist3.sort(key = myfunc)
print(thislist3)

#-------------------------------------------------------------------------------------------------------
# Weitere Methoden für Sortierverfahren

# Case Sensitive Sort <- Python sortiert standartmäßig Case Sensitive (d.h Erst groß dann klein usw)
# Ist zwar bissle Komplex aber: Warum ist die Ausgabe anders als erwartet? Simple ASCII-Reihenfolge
# Die ASCII Werte werden verglichen und zwischen Groß-/Kleinschreibung value1 > value2 = Position[0]
# Beispiel dazu: 

thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.sort()
print(thislist4) # Jetzt denk man ob groß oder klein banana cherry kiwi orange 
# Ist hierbei nicht so: Es kommt Kiwi Orange banana cherry
# Erst werden Großbuchstaben sortiert, per ASCII Wert dann Kleinbuchstaben (beides erfolgt Alphabetisch)
# Wenn man es Case Insensitive macht dann per key = str.lower

thislist5 = ["Melon", "apple", "Strawberry", "grapes", "Elderberry"]
thislist5.sort(key = str.lower) # Ignoriert hierbei alles was mit ASCII zutun hat 
print(thislist5)                # Sortiert nur Alphabetisch (Groß-/Kleinschreibung vermischt)

#-------------------------------------------------------------------------------------------------------
# Reverse Order 
# Methode geht vom Ende des Arrays an den Anfang durch (per iteration -1 der Gesamtlänge)

thislist6 = ["Element 1", "Element 2", "Element 3", "Element 4"]
thislist6.reverse()
print(thislist6)

#-------------------------------------------------------------------------------------------------------
# Listen Kopieren per copy()
# Wichtig! list2 = list1 geht nicht -> wird nur zu einer Referenz (alle Änderungen in list1 -> list2)

thislist7 = ["apple", "mandarin", "berry"]
mylist = thislist7.copy() # Alle Elemente werden kopiert und in mylist eingefügt 
print(mylist) # Zur veranschaulichung kann man auch thislist7 printen dann sieht man 2x das gleiche
print(thislist7)

#-------------------------------------------------------------------------------------------------------
# Kopieren per list() 
# Geht genauso wie copy() daher nur als Text 

#-------------------------------------------------------------------------------------------------------
# Kopieren per slice() (hört sich komisch an kopieren per schnitt)
# Syntax ist wichtig dabei
# bei dem Schritt mylist = thislist7[:]

#-------------------------------------------------------------------------------------------------------
# Verbinden zweier Listen per + Operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # Fügt die Listen zusammen

#-------------------------------------------------------------------------------------------------------
# Per for-Schleife Verbinden (Jedes Element einzeln verbinden mit append)

list4 = ["d", "e", "f"]
list5 = [4, 5, 6]

for x in list5: # Jedes Element von Liste 5 
    list4.append(x) # Einzeln einfügen in Liste 1 Wichtig! am Ende der Liste wird eingefügt
print(list4)

#-------------------------------------------------------------------------------------------------------
# Geht auch per extend()

list6 = ["g", "h", "i"] # Selbes Prinzip
list7 = [7, 8, 9]

list6.extend(list7)
print(list6)

# Nocheinmal alle Methoden auf einem Blick: https://www.w3schools.com/python/python_lists_methods.asp

# Listen Ende