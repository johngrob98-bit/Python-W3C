# JSON
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: JSON ist die Syntax um Daten zu speichern und zu verarbeiten
# JSON ist ein Text welcher in der JavaScript Objekt Notation geschrieben ist

#-------------------------------------------------------------------------------------------------------
# Python hat ein JSON package per import json

import json

#-------------------------------------------------------------------------------------------------------
# JSON in Python konvertieren
# Wenn man einen JSON string hat, kann dieser per json.loads() konvertiert werden
# -> Daraus wird dann ein Python Dictonary

x = '{ "name":"Ufuk", "age":24, "city":"Buchloe"}'  # Hier der JSON string

y = json.loads(x)                                   # Anschließende konvertierung 

print(y["age"])                                     # In ein Dictionary

#-------------------------------------------------------------------------------------------------------
# Anderes herum geht es natürlich auch Python to JSON

o = {                       # Das Python Objekt (hier ein Dictionary)
    "name": "Ufuk",
    "age":24,
    "city": "Buchloe"
}

v = json.dumps(o)           # Konvertierung in ein JSON

print(v)                    # Ausgabe des JSON Strings

#-------------------------------------------------------------------------------------------------------
# Folgende Objekte können in ein JSON string konvertiert werden
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
#-------------------------------------------------------------------------------------------------------
# Hier noch als Beispiel einmal alle Konvertierungen
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#-------------------------------------------------------------------------------------------------------
# !Wichtig! zu wissen: wenn man von Python -> JSON geht ändern sich die Objekte in JS Datentypen
# Bevor ich das alles aufschreibe hier die Liste: https://www.w3schools.com/python/python_json.asp

#-------------------------------------------------------------------------------------------------------
# Formatierung des Ergebnises per indent
# Ohne diese wird das konvertiete Objekt einfach in einer Zeile geprinted, daher per indent schön machen


x = {                           # Hier ein Python dictionary mit allen Datentypen 
  "name": "Ufuk",               # welche für die Konvertierung gültig sind
  "age": 24,
  "married": False,
  "divorced": False,
  "children": ("none thank god lol"),
  "pets": ("two cats"),
  "cars": [
    {"model": "Mazda 3", "engine": "Skyactive X"},
  ]
}

print(json.dumps(x)) # Bei dieser Ausgabe steht alles in einer Zeile
print(json.dumps(x, indent=4))  # Jetzt mit der Formatierung 4 indentations (Einrückungen)

#-------------------------------------------------------------------------------------------------------
# Man kann auch seperators einsetzten, per Komma und Leerzeichen kann die Ausgabe getrennt werden
# Also die Keys und Werte, einfach comilen und selber sehen (hab auch kurz schauen müssen)

print(json.dumps(x, indent = 4, separators=(".", " = "))) 

# Trennt Objekte per Punkt und Leerzeichen (.  ) und Keys von Werten mit =

#-------------------------------------------------------------------------------------------------------
# Und Soriteren geht per sort_keys

print(json.dumps(x, indent = 4, sort_keys = True))


#-------------------------------------------------------------------------------------------------------
# Alle drei mal einzeln compilen, dann nacheinander, dann sieht man die Unterschiede ganz gut

#-------------------------------------------------------------------------------------------------------
# JSON Ende (für jetzt)
