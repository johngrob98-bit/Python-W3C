# Strings gibt in Python paar besonderheiten

# 1. " " und ' ' sind gleich zu behandeln
# 2. "Hallo 'ich ' bin " geht auch
# 3. Strings können zu Variablen zugewiesen werden
# ->    a = "hello", print(a) = Hello
# 4. Mehrzeiliger Strings: 
# ->  mit """ oder ''' kann man direkt Zeilenumbrüche im String schreiben
# man braucht kein \n oder new line dafür

a = """Mir geht es gut und dir ?
Ja mir geht es auch super danke der Nachfrage"""
print(a)

#-------------------------------------------------------------------------------------------------------
# Strings sind Arrays (es gibt kein Char in Pyhton, leerer String =  String mit der Länge 1)
# Eckige Klammern für einzelnes Element im String (wie charAt() nur einfacher)

b = "Hello, World!"
print(b[1], "\n")  # Es wird wie in einem Array von 0 gezählt also ist das H = [0] e = [1] usw

#-------------------------------------------------------------------------------------------------------
# Per For Schleife kann man durch den String durch loopen

for c in "banana\n":
    print(c)

#-------------------------------------------------------------------------------------------------------
# Länge per len()

print(len(b))

#-------------------------------------------------------------------------------------------------------
# Check String (richtig gut), check if a certian phrase or character is present in a string
# -> per in

txt = "Jetzt schauen wir mal ob das auch wirklich klappt! "
print("klappt" in txt) # wenn klappt im Text is kommt true dabei raus

# Nur print if das Wort im Text ist

txt2 = "Wir schauen uns das Wasser an."
if "schauen" in txt2:
    print("Yes, 'schauen' is present.")

# Check if NOT, wie der Name schon sagt

txt3 = "Ich mag es Python zu coden :D."
print("hasse" not in txt3)

# Gleiches geht auch mit if wieder

txt4 = "Ja genau so ist es oder?"
if "okay" not in txt4:
    print("No, 'okay' is NOT present")

#-------------------------------------------------------------------------------------------------------
# Trennen von Strings (Slicing)
# Hier bekommt man die Buchstaben vom Bereich 2 - 5 !! Wichtig Ende - Start damit hat man die Anzahl !!
f = "Hello, World!"
print(f[2:5])

o = "Hello, World!"
print(o[-5:-2])

#-------------------------------------------------------------------------------------------------------
# Modify Strings
# Es gibt die üblichen upper() lower() case Methoden einfach print(a.lower()/upper())

# Remove Whitespace -> Entfernt leer tab usw 

str = " Hallo, Welt! "
print(str.strip())

# Replace ()
#Damit gehen Einzelne Buchstaben (aber nur einzeln also man kann nicht mehrere gleichzeitig tauschen)

g = "Flavor Text"
print(g.replace("F", "J"))

# Spilt -> teilt in Substring auf

h = "Hello, World!"
print(h.split(",")) # gibt [Hello',' World!] aus

# Mit + zwei Strings verbinden

e = "Hello"
r = "World!"
print(e + r) # ohne Leerzeichen
print(e + " " + r) # mit Leerzeichen

#-------------------------------------------------------------------------------------------------------
# String Formatieren
#-> String und Nummern (int, float, complex) nicht kombinierbar außer mit format()

age = 24
txt5 = f"Meine Name is Ufuk und ich bin {age} alt"
print(txt5)

# Platzhalter / Modifiers
# Enthält Variablen, Operationen, Funktionen und Modifiers 

price = 59
txt6 = f"The price is {price} €"
print(txt6)

# Mit : und dann .2f z.B kann man floats angeben

price2 = 69
txt7 = f"The price is {price2:.2f} €"
print(txt7) # Konvertierung direkt möglich wie in C++

# Berechnen kann man auch darin 

txt8 = f"The price is {69 * 2} €"
print(txt8)

#-------------------------------------------------------------------------------------------------------
# \Charakere -> Genau gleich wie in C, C++, Java 
# https://www.w3schools.com/python/python_strings_escape.asp
# Alle Methoden auf einen Blick:
# https://www.w3schools.com/python/python_strings_methods.asp


