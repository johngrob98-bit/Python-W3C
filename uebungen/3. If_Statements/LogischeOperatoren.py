# Logische Operatoren
#-------------------------------------------------------------------------------------------------------
# Grundlegendes
#-------------------------------------------------------------------------------------------------------
# Python enthät 3 Logische Operatoren
# 1. and -> True wenn beide Bedingungen war sind
# 2. or  -> True bei einer von beiden Bedingungen 
# 3. not -> Wenn true wird es false und false wird zu true
# Jetzt nochmal auf einfacher Sprache:
# and -> Zweihandschalter: nur wenn beide true ist geht die z.B. Maschine an
# or -> Lichtschalter: Egal welcher an ist Hauptsache ein Schalter ist auf an
# not -> Wenn du ja sagst kommt nein dabei raus

#-------------------------------------------------------------------------------------------------------
# and, & Operator

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both condition are Ture") # Ändere a auf 20 dann gibt es keine Ausgabe mehr
# Wie ^ oben ^ schon gesagt beide Bedingungen müssen wahr sein sonnst passiert nix

#-------------------------------------------------------------------------------------------------------
# or, || Operator

a = 200
b = 33
c = 500
if a > b or c > a:
    print("At least one of the conditions is Ture") # Damit der print nicht durchgeht muss b > a & c < a
# Lichtschalter: Hauptsachte einer der beiden Bedingungen ist wahr dann geht es durch 
# Falls beide false sind passiert auch nix

#-------------------------------------------------------------------------------------------------------
# not, ! Operator
 
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b") # Keine Ausgabe wenn a > als b ist 
# a > b = false das not dreht es in ein true um 
# Wenn man es sich vorsagt wirds leichter: a ist nicht größer als b, das ist wahr daher Ausgabe

#-------------------------------------------------------------------------------------------------------
# Verbinden von mehreren Operatoren geht natürlich auch

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
# Hier sind jetzt not, or and in einem
# Bevor man darüber nachdenkt ganz !Wichtig!
# 1. not 
# 2. and
# 3. or
# Das ist die Hierachie der Operatoren
# Alles im Kopf oder auf Papier einklammern weil die Hierachie bindet die jeweilige Variable an den 
# jeweiligen Operator also (Operator Aktion Operand), klar macht man das im Code nicht aber wenn man es 
# per Hand ausrechnen will und verstehen möchte dann lieber so (hat mich grade ne halbe Stunde gekostet)
#-------------------------------------------------------------------------------------------------------
# Also Erst die Klammer da kommt false raus weil beide Bedingung nicht stimmten, bei or ist es dann egal
# Dann den Rest anschauen und im Kopf einklammern 
# Not ist über allem also Klammert man (not is_student) ein da kommt true raus 
# Dann kommt in der Hierachie and, Klammert man is_student und das Ergebnis aus der Age Bedingung ein
# Da steht dann (false and true) = false 
# Dann bleibt nur noch (false or has_discount_code) -> false or true = true 
# Damit ist die Ausgabe true
#-------------------------------------------------------------------------------------------------------

# So jetzt noch eine einfache zum Verständnis 

temperature = 25
is_raning = False
is_weekend = True

if(temperature > 20 and not is_raning) or is_weekend:
    print("Great day for outdoor activities!")

# Auch hier wieder selbes Prinzp: Hierachie beachten
# -> Erstmal einklammern, not is_raning in eine sperate Klammer
# Ergebnis davon dann mit temp > 20 einklammern -> Das ergibt ture and true -> true
# Danach Klammer auflösen und true or is_weekend (true) das ergibt dann true am Ende und daher wird die
# Ausgabe auch kompiliert

#-------------------------------------------------------------------------------------------------------
# Logische Operatoren Ende