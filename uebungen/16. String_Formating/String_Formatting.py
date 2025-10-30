# String Formatting F-Strings
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: F-Strings erlaubt es nur bestimmte Teile eines strings zu formatieren
# Um das zu tun schreibt man ein f vor das string literal

#-------------------------------------------------------------------------------------------------------
# Beispiel

txt = f"The price is 69 dollars"    # Jetzt steht die 69 noch "hardcoded" im string selbst
print(txt)

# Möchte man das aber "modular" halten geht das mit {}
#-------------------------------------------------------------------------------------------------------
# Den sogenannten Placeholder und Modifers      Placeholer {}, Modifiers :
# Um eben jtzt zu formatieren kommen {} rein damit kann man dann variablen, operationen, funktion nutzen

price = 69
txt = f"The price is {price} dollars"
print(txt)

# Placeholder können auch modifier beinhalten um den Wert zu formatieren
# Beispiel

txt = f"The price is {price:.2f} dollars"
print(txt)

# Dadurch haben wir jetzt aus int 69 double 69.00 gemacht

#-------------------------------------------------------------------------------------------------------
# Das ganze geht auch ohne die Variable vorher zu definieren

txt = f"The price is {69:.2f} dollars" # Damit haben wir alles in einer Zeile gemacht und formatiert
print(txt)

#-------------------------------------------------------------------------------------------------------
# Operationen in F-Strings machen
# Darunter sind math-operations, if else usw.

txt = f"The price is {2 * 8} dollars"   # Multiplikationen z.B.
print(txt)

newprice = 69
tax = 0.17
txt = f"The Price is {newprice + (newprice * tax)} dollars"
print(txt)

# Dann auch if else

price = 169
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# Weitere Beispiele spaare ich mir (gibt auf der Seite auch nicht mehr aber das Prinzip is klar)

#-------------------------------------------------------------------------------------------------------
# Auch Funktionen gehen innerhalb von F-Strings

fruit = "banana"
txt = f"I love {fruit.upper()}"
print(txt)

#-------------------------------------------------------------------------------------------------------
# !Wichtig! es müssen nicht nur Python eigene Funktionen sein, es gehen auch selbstgeschriebene

def converter(x):
    return x * 0.3048

txt = f"The plane is flying at a {converter(30000)} meter altitude"
print(txt)

#-------------------------------------------------------------------------------------------------------
# Dazu gibt es noch eine Liste an Modifiers 
# Hier der Link dazu: https://www.w3schools.com/python/python_string_formatting.asp

#-------------------------------------------------------------------------------------------------------
# Falls man eine niedrigere Python Version als 3.6 hat geht das alles ein wenig anders
# Da aber jeder die aktuelle Version hat (hoffe ich) gehe ich da nicht näher darauf ein 
# Sondern verweise auf das Tutorial     ^ den Link oben bitte nehmen :D ^ 

#-------------------------------------------------------------------------------------------------------
# String Formatting (F-Strings) Ende