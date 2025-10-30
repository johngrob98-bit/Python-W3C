# Try Except
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Eine Exception ist dafür da um den Programmabbruch zu vermeiden
# Daher wird oft try except genutzt um vorzubeugen, deswegen try = Versuche diesen Codeblock auszuführen
# -> wenn ein Fehler dabei auftritt dann -> except = fange diesen ab und reagiere mit code darauf

#-------------------------------------------------------------------------------------------------------
# Die Grundlegenden Elemente
# try       -> Erlaubt es Code zu testen welcher Fehler enthält
# except    -> "kümmert" sich um den Fehler
# else      -> Erlaubt es Code auszuführen wenn es keinen Fehler gibt
# fianlly   -> Elaubt es den Code auszuführen, und ignoriert dabei das try except Ergebnis
# ^ steht daher auch am höchsten und "scheert" sich eigentlich um garnichts

#-------------------------------------------------------------------------------------------------------
# Exception Handling 
# Wenn ein Fehler auftritt, dann stoppt Python das Programm und "wirft" eine Fehlermeldung
# Diese exceptions können per try gehandhabt werden
# Beispiel dazu: der try Block wird eine exception generieren da x nicht definiert ist
        
try:
    print(x)        # Der Fehler passiert hier
except:
    print("An error occurred!") # Daher wird der except Block trozdem ausgeführt

# Ohne den try block würde das Programm crashen und einen Error werfen

#-------------------------------------------------------------------------------------------------------
# Man so viele exceptions denifineren wie man will

try:
    print(y)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")  # Unter diese exception können noch n-beliebig viele drunter

#-------------------------------------------------------------------------------------------------------
# Else, definiert einen Abschnitt des Codes, welcher ausführbar ist wenn es keine Errors gibt

try:
    print("Here are no errors")     # Dieser try gibt keinen Fehler da er richtig ist
except:
    print("Something went wrong")   # Daher greift das except nicht
else:
    print("Nothing went wrong")     # Aber das else eben schon
print("\n")

#-------------------------------------------------------------------------------------------------------
# Finally, wenn angegeben, wird ausgeführt egal ob der Code einen Fehler hat oder nicht

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Das ist Hilfreich um resourcen zu spaaren (Einfach ein Unnötiger Speicherfresser)
# Salop gesagt, ist wie schon im Namen try zum testen da, wenn man ein großes Programm hat nutzt man try

#-------------------------------------------------------------------------------------------------------
# Hier noch ein Beispiel, Schreibgeschütze Datei, soll beschrieben werden -> geht nicht 

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")          # Überschreiben der Datei
  except:
    print("Something went wrong when writing to the file")  # Die Datei kann nicht geöffnet werden
  finally:
    f.close()   # Da sie nicht aufgeht wird abgebrochen und 
except: 
  print("Something went wrong when opening the file")   # ^ die Nachricht ausgegeben

#-------------------------------------------------------------------------------------------------------
# Raise an exception
# Als Pyhton Entwickler hat man selbst du möglichkeit zu sagen wann eine exception "geworfen" werden soll
# Dafür nutzt man das raise Schlüsselwort

x = -1

if x < 0:
   raise Exception("Sorry, no numbers below zero")

# raise wird hierbei genutzt um eine exception (also Ausnahme) auszulösen
# Dazu kann man noch selbst wählen welche Art von error und mit welchem Text für den Benutzer

x = "Hello"

if not type(x) is int:
   raise TypeError("Only integers are allowed") # TypeError wurde also von mir als Namen dafür gewählt
# Und die Nachricht kommt eben vom Ersteller selsbt

#-------------------------------------------------------------------------------------------------------
# Try Except Ende