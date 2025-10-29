# Alles was mit bool zu tun hat
#-------------------------------------------------------------------------------------------------------
# true / false als return des jeweiligen Wahrheitswertes 

print(10 > 9)   # t
print(10 == 9)  # f
print(10 < 9)   # f

# Noch ein Beispiel ist eig selbsterklärend

a = 200 
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#-------------------------------------------------------------------------------------------------------
# Falsche Werte 

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # und mit print(bool(x)) kann man testen ob die Werte wahr / falsch sind 

# Beispiel dazu
# Ein Objekt / Wert gilt als false, wenn __len()__ 0 oder false per return zurück gibt 

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Funktionen geben auch bool zurück

def myFunction():
    return True
# print(myFunction()) hier kommt true raus
if myFunction():
    print("YES!")
else:
    print("NO!") # je nach dem ob myFunction true oder false returned geht das if else rein
                 # bei return false würde NO! kommen

# isinstance() schaut z.B ob ob das Objekt den jeweiligen Datentypen hat

x = 200
print(isinstance(x, int))

#-------------------------------------------------------------------------------------------------------
# Operatoren / Logische Operatoren
# https://www.w3schools.com/python/python_operators.asp