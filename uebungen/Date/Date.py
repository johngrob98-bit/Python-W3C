# Date (Datum)
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Ein Datum in Python ist ein eigener Datentyp (naja es ist eig ein int aber egal)
# Das kann man in Python per import datetime beheben, das Datum ist dann ein Datumsobjekt
#(Das aus dem Englischen zu übersetzten ist ein Albtraum)

import datetime

x = datetime.datetime.now()
print(x)                        # Siehe da das Datum und die Uhrzeit von Heute (also deinem Heute)
                                # Bei mir ist es der 29.10.2025

#-------------------------------------------------------------------------------------------------------
# Ausgabe vom Datum: So wie es jetzt ist steht 2025-10-29 14:29:17.03371
# Heißt wie ^ oben ^ Jahr, Monat, Tag, Stunden, Minuten, Sekunden
# Man kann auch den Wochentag ausgeben lassen, und im Endeffekt alle Daten, diese halt auch seperat usw.

print(x.year)
print(x.strftime("%A"))     # Damit haben wir das Jahr und den Wochentag

#-------------------------------------------------------------------------------------------------------
# Erstellen von Datums Objekten per datetime() Klasse (Konstruktor) des datetime Modules
# Die datetime() Klasse benötigt drei Parameter um ein Datum zu erstellen: year, month, day

y = datetime.datetime(2001, 4, 1)   # Und damit haben wir meinen Geburtstag als Easter Egg
print(y)

# Die datetime() Klasse nimmt auch Parameter für Uhrzeit, Zeitzone an (Stunde, Minute, Sekunde, mirkosek
# -kunde, tzone (Zeitzone))

#-------------------------------------------------------------------------------------------------------
# Die strftime() Methode diese wurde ^ oben ^ schon benutzt
# Formatiert Datumsobjekte in lesbare strings
# Methode nimmt einen Parameter, format, und festzulegen welches Format es sein soll und gibt string aus

z = datetime.datetime(2025, 9, 1)   
print(z.strftime("%B"))

# Bevor ich erkläre was jedes %... macht hier eine Tabelle 
# https://www.w3schools.com/python/python_datetime.asp
#-------------------------------------------------------------------------------------------------------
# Datum Ende

