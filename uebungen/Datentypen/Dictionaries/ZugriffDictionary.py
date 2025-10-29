# Zugriff auf Dictionary Elemente
#-------------------------------------------------------------------------------------------------------
# Wie in Dictionary.py schon gezeigt per [] auf das jeweilige Element zugreiffbar

#-------------------------------------------------------------------------------------------------------
# Zupgriff per Methode get()

dict = {
    "brand" : "BMW", # Der Aufbau bleibt gleich
    "model" : "120i", 
    "year" : 2018
}
x = dict.get("model") # Zugriff per get = wie []
print(x)

#-------------------------------------------------------------------------------------------------------
# Schlüsselargumente per keys()

y = dict.keys()
print(y) # Die Keys sind hierbei die Attribute welche anschließend zugewiesen werden 

#-------------------------------------------------------------------------------------------------------
# !Wichtig! hierbei ist: Jeder Änderung der Attribute werden auch später wieder ausgegeben
# Beipiel dazu:

car = {
    "brand" : "Nissan",
    "model" : "Skyline GTR R34",
    "year" : 1999
}
z = car.keys()
print(z) # Original Attribute vor Änderung
print(car) # Hier fehlt noch die Farbe
car["color"] = "silver" # Fügt jetzt noch als Attribut Farbe hinzu reflektiert sich in der Ausgabe 
print(z) # Attribute nach der Änderung
print(car) # Hier sieht man dann das hinzukommen der Farbe

#-------------------------------------------------------------------------------------------------------
# Werte erhalten per values()
# Gib eine Liste von Werten aus
# Hier wird die car.values() genommen
z = car.values()
print(z) # Hier stehen dann die Werte welchen den Attributen hinzugefügt wurden
# Auch hier gilt das gleiche Prinzip wie oben jede Änderung wird anschließend angezeigt
car["year"] = 2002 # Nehmen wir das neuere Modell
print(z) # Und somit haben wir aus 1999 -> 2002 gemacht also den "neuesten" R34 genommen Toll!
# Natürlich kann man auch Attribute hinzufügen wie bei der Farbe oben
car["engine"] = "RB24"
print(car) # Jetzt wissen wir auch welchen Motor wir haben
print(z) 

#-------------------------------------------------------------------------------------------------------
# Elemente erhalten per items()

z =  car.items()
print(z) # Alle Elemente und Attribute werden wieder in key.value Paaren ausgegeben
# Ebenso wie oben Änderungen werden auch hier wieder angezeigt (das führe ich jetzt nicht aus)

#-------------------------------------------------------------------------------------------------------
# Schauen ob ein Schlüssel exsistiert per if "..." in

if "model" in car:
    print("Yes, model is one of the keys in car") # Überprüft ob das Attribut model im dict car ist 

#-------------------------------------------------------------------------------------------------------
# Werte ändern per []
# Im Endeffekt das wie oben 

dict["model"] = "320i E46"
dict["year"] = "2005"
print(dict) # Jetzt habe wir aus einem 1er BMW einen 3er BMW gemacht

#-------------------------------------------------------------------------------------------------------
# Andere Methode selbes Ziel update()

dict.update({"year" : 2008}) # Jetzt ist es ein Facelift E46 geworden Toll!
print(dict) # Schreibweise wie bei erstellen hier

#-------------------------------------------------------------------------------------------------------
# Elemente hinzufügen
# Analog ^ zu oben ^
car["turbos"] = 2
print(car) # muss wenig dazu sagen

#-------------------------------------------------------------------------------------------------------
# Elemente entfernen per pop()
# Entfernen wir doch mal die 2 turbos auch wenn das dann kein Skyline mehr ist :(
car.pop("turbos")
print(car) # tja jetzt haben wir keien Turbos mehr

#-------------------------------------------------------------------------------------------------------
# Mit popitem() wird das letzte Element was hinzugefügt wurde entfernt

car.popitem()
print(car) # Jetzt fehlt und auch noch der Motor oder? Wer hat aufgepasst was als letztes geadded wurde

#-------------------------------------------------------------------------------------------------------
# Entfernen per del()

del car["color"] # Angabe welches Element genau gelöscht werden soll 
print(car) # Alles analog ^ zu oben ^ schön zu sehen im Compiler ist wie die Liste erst länger und dann
# kürzer wird da wir erst hinzufügen und dann entfernen
#-------------------------------------------------------------------------------------------------------
# Bei nicht Spezifikation vom Element wird die gesamte Liste gelöscht
# del car
# print(car) gibt natürlich einen error da es car nicht mehr gibt 

#-------------------------------------------------------------------------------------------------------
# clear() leer die Liste ohne sie komplett zu löschen 

car.clear() # Und damit sind wir bei der realität einen R34 werden wir alle nie haben :´(
print(car)