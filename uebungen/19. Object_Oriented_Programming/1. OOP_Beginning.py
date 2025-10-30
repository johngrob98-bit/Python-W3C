# OOP (Objekt Orientieres Programmieren)
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Python ist eine OOP Sprache, daher auch in diesem Kaptiel der Fokus auf die stärken 
# dieser Art zu programmieren

#-------------------------------------------------------------------------------------------------------
# Vorteile von OOP
# - gibt Programmen eine klare Struktur
# - vereinfach es den Code zu überarbeiten, wieder zu verwenden, und das debuggen
# - DRY (Dont Repeat Yourself) -> relativ synonym im Coding 
# - Erstellen von wiederverwendbarem Code -> dieser ist dann "schlanker" mit weniger unnötigen Sachen

#-------------------------------------------------------------------------------------------------------
# Was sind Klassen und Objekte? 
# Eine Klasse definiert wie ein Objekt auszusehen hat, und ein Objekt wird erstellt basierend auf den
# Informationen innerhalb der Klasse. Hier ein Beispiel dazu:

#   Class           Objects
#   Fruit           Apple, Banana, Cherry
#   Car             Volo, Audi, Toyota

# Wenn man ein Objekt aus einer Klasse erstellt, dann !vererben! die Objekte alle Variablen welche
# innerhalb der Klasse definiert wurden

# Das ist jetzt nicht vom Tutorial sondern so wie ich es gelernt habe.

# Beispiel Dackel

# Ein Dackel gehört zur Famile Hund -> d.h Klasse Hund Objekt Dackel
# Jedes Objekt hat bestimmte Attribute (Variablen) welche ihn/sie einzigartig machen

# Ein Dackel hat lange Ohren, einen kurzen Körper und eine lange Schnauze
# Diese Attribute sind Dackel spezifisch 

# Das heißt diese sind Protected im Dackel Objekt

# Der Hund selber als "Oberklasse" hat natürlich auch eine Schnauze, vier Beine, Ohren usw.

# Diese Attribute sind frei verfügbar für den Dackel

# Der Sinn von Klassen ist es im besten Fall Code wiederholungen zu vermeiden

#-------------------------------------------------------------------------------------------------------
# Man erstellt eine Klasse mit beliebig vielen Methoden -> auf diese können alle Objekte zugreifen 
# welche aus der Oberklasse erben 

# Also nehmen wir an die Hund Klasse hat die Methode bellen()

# Dann kann das Dackel Objekt auf diese Methode zugreifen ohne sie selber vorher nocheinmal zu definieren

#-------------------------------------------------------------------------------------------------------
# Deswegen erleichtern Klassen und Objekte einem das Leben

#-------------------------------------------------------------------------------------------------------
# OOP Beginning Ende