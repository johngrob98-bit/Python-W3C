# None
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: None ist eine spezielle konstante, sie repräsentiert die "abwesenheit" eines Wertes
# Der Datentyp davon ist NoneType und None ist die einzige Instantz vom NoneType Objekt

#-------------------------------------------------------------------------------------------------------
# Variablen können None sein um zu zeigen das sie z.B. keinen Wert haben

x = None
print(x)

#-------------------------------------------------------------------------------------------------------
# Über type() erhält man den Datentypen

print(type(x))

#-------------------------------------------------------------------------------------------------------
# Um einen Wert mit None zu vergleichen benutzt man is oder is not 

result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

# Ähnlich mit is not statt is

if result is not None:
    print("No result yet")
else:
    print("Result is ready")

#-------------------------------------------------------------------------------------------------------
# None ist Standartmäßig False

print(bool(None))

#-------------------------------------------------------------------------------------------------------
# Funktionen geben Standartmäßig Nono zurück also False 

def func():
    x = 5

x = func()
print(x)

#-------------------------------------------------------------------------------------------------------
# None Ende