# Modules
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Modlue sind wie eine Bibliothek, sie enthalten ganz viele Funktionen

#-------------------------------------------------------------------------------------------------------
# Um ein Modul zu erstellen muss man einfach .py ans Ende des Dateinamens setzten
# Aufmerksame Leser haben gemerkt das es schon eine Greeting.py Datei gibt
# Das ist im Endeffekt deine Methode, in einer anderen Datei welche per import aufgerufen wird
# Das sind headerdatein aus C++ 
# Einmal in den Module Ordner schauen. dort liegt jetzt eine Greeting.py Datei, in dieser ist die 
# Hello Funktion, auf dieser wird dann eben per import + dateiname zugegriffen

#-------------------------------------------------------------------------------------------------------
# Wie nutzt man das aber? 
# Mit imports

import Greeting

Greeting.greeting("Ufuk")       # Das heißt auch das die Ausgabe Hallo Ufuk sein wird

# Wenn man eine Funktion aus einem Module nutzt dann bitte mit dieser Syntax: module_name.function_name

#-------------------------------------------------------------------------------------------------------
# Variablen in Modules
# Module können auch Variablen aller Art enthalten (Tupel, Arrays, Listen, Objekte usw.)
# Jetzt wurde in Module das person1 Dictionary hinzugefügt daraus holen wir uns jetzt das Alter

a = Greeting.person1["age"]
print(a)

# Wie man sieht, alle Daten, Variablen, Methoden usw. sind wegen dem import für alle Dateien Verfügbar

#-------------------------------------------------------------------------------------------------------
# Namensgebung der Module: Die Namen sind egal, Hauptsache das .py steht am Ende
# Es sollten halt Sinnvolle Namen sein (am besten wie Methoden behandeln oder Klassen)

#-------------------------------------------------------------------------------------------------------
# Den Namen kann man aber auch ändern
# Das funktioniert per Alias as

import Greeting as person       # Das Modlue heißt nur für diesen Import jetzt person

a = person.person1["country"]
print(a)

#-------------------------------------------------------------------------------------------------------
# Eingebaute Modules: Python selber hat mehr als genug eigene Module
# Für spezifische in der Python Dokumentation nachlesen, kenne selber nur eine Handvoll 

import platform

x = platform.system()       # Zeigt das Betriebssystem an
print(x)

#-------------------------------------------------------------------------------------------------------
# Bei jedem import wird alles aus dem jeweiligen Modul mitgenommen, wenn man das nicht will from nutzen

from Greeting import person1    # Damit wurde nur das Dictionary übernommen, die greeting Methode nicht

print(person1["name"])

# Beim importieren mit from nicht den Modulnamen nutzten wenn man einzelne Elemente möchte
# Da sollte man dann person1["age"] <- richtig ! und nicht greeting.person1["age"] <- falsch!

#-------------------------------------------------------------------------------------------------------
# Module Ende