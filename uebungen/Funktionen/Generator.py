# Generatoren
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Generatoren sind Funktionen welche ihre Ausführungen pausieren und weiterführen können
# Generatorfunktionen geben beim Aufruf einen Iterator zurück
# Der Code in der Funktion wird noch !nicht! ausgeführt, sondern nur !kompiliert! Die Funktion wird 
# nur ausgeführt sobald man über den Generator iteriert hat.
# Es wird ein lazy iterator zurückgegeben
# https://en.wikipedia.org/wiki/Lazy_evaluation        <- Generell
# https://en.wikipedia.org/wiki/Lazy_evaluation#Python <- Pyhton spezifisch

#-------------------------------------------------------------------------------------------------------
# Beispiel dazu:

def generator():
    yield 1
    yield 2
    yield 3

for value in generator():
    print(value)

print("\n")

# Generatoren erlauben es, große Datenmengen Stück für Stück zu verarbeiten, ohne alles auf 
# einmal zu speichern. Anstadt return, benutzten Generatoren das yield Schlüsselwort
# 
# -> Im Endeffekt ist es wie eine Serie im Stream statt komplett herunterzuladen
# man streamt Folge für Folge statt Staffel für Staffel 
# (weniger Daten zum runterladen = wenig Wartezeit zwischen Folgen)

#-------------------------------------------------------------------------------------------------------
# yield Schlüsselwort
# Ohne das gibt es keinen Generator
# yield-Schlüsselwort ist notwendig, um eine Generatorfunktion zu erstellen. Sobald Python auf yield 
# triff, wird der aktuelle Zustand der Funktion gepseichert und der Wert zurückgegeben. Beim nächsten
# Aufruf des Generators wird die Funktion genau an dieser Stelle fortgesetzt
# Wird mit kommenden Beispielen klarer

#-------------------------------------------------------------------------------------------------------
# Beispiel, ein Generator welcher bis n hochzählt

def count_up_to(n):     # Erstellen der Funktion "Zähle bis n"
    count = 1           # Der Zähler wird auf 1 gestzt, also Start bei 1
    while count <= n:   # Zähle solange bis der Zähler <= n ist im Beispiel also bis 5
        yield count     # Generator wird erzeugt, gibt die Werte einzeln zurück, statt die alle gleich-
                        # zeitig im Speicher zu halten (spaar eben deswegen Speicher)
        count += 1      # Inkrementiere den Zähler

for num in count_up_to(5):  # for Schleife für den print unten, iteriere durch alle Elemente 
    print(num)              # printe alle iterierten Elemente
print("\n")
# !Wichtig! dazu noch, Unterschied zwischen return und yield: return beendet die Funktion also nach
# return ist Schluss und yield pausiert sie und kann mehrmals aufgerufen werden

#-------------------------------------------------------------------------------------------------------
# Generatoren spaaren Speicher
# Eben weil sie Werte im Handumdrehen erstellen statt alles im Hauptspeicher zu speichern
# Für große Datensätze ist das gut, das spaar Speicher und damit kompilierzeit

#-------------------------------------------------------------------------------------------------------
# Beispiel für große Sequenzen dazu:

def large_sequence(n):
   for i in range(n):
        yield i

gen = large_sequence(1000000)       # <- Normalerweise würde jetzt eine Millionen Nummern gepseichert
print(next(gen))                    # aber durch den Generator wird eben immer nur !eine! Zahl ""
print(next(gen))                    # per next(gen) wird dann eben die !zweite! Zahl gespeichert usw.
print(next(gen))
print("\n")

#-------------------------------------------------------------------------------------------------------
# Manuell durch Generatoren iterieren per next()

def simple_gen():
    yield "Jin"
    yield "Kazuya"
    yield "Heihachi"

gen = simple_gen()
print(next(gen))        # Wie schon oben erwähnt, es wird eben immer nur das Element gespeichert,
print(next(gen))        # auf das man eben gerade iteriert hat alle anderen sind irrelevant
print(next(gen))
print("\n")
# Einschub dazu, iteriert man über die Anzahl der yields gibt's einen Error

#-------------------------------------------------------------------------------------------------------
# Ähnlich wie bei Listen, kann man einen Generator Ausdruck mit () statt [] erstellen

list_comp = [x * x for x in range(5)]       # Eben hier die Liste
print(list_comp)

gen_exp = (x * x for x in range(5))         # Hier der Generator
print(gen_exp)                              # Unterschied: im großen und ganzen Laufzeitspeicherung
print(list(gen_exp))
print("\n")

#-------------------------------------------------------------------------------------------------------
# Generator für eine Summe ohne eine Liste zu erstellen

total = sum(x * x for x in range(4))        # 0 - 3 ist die Range
print(total)                                # Dann 0 + 0 = 0, 1 * 1 = 1, 2 * 2 = 4, 3 * 3 = 9
                                            # Danach werden alle Ergebnisse addiert 
                                            # Also 0 + 1  + 4 + 9 = 14
print("\n")
                    
#-------------------------------------------------------------------------------------------------------
# Geht auch für Fibonacci

def fibonacci():                   # Die ersten 100 Fibonacci Zahlen
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(100):
    print(next(gen))

#-------------------------------------------------------------------------------------------------------
# Da ich ehrlich keine Lust mehr auf die zwei Methoden da habe hier der Link, ist nur open, close
# https://www.w3schools.com/python/python_generators.asp