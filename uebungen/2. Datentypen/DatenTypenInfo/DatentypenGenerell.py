# Datentypen
# Pyhton hat einige lol
# Wenn in einem Kommentar "" steht heißt es analog zu (also gleich wie...)

#-------------------------------------------------------------------------

#text type:     str
#numeric type:  int, float, complex
#sequence type: list, tuple, range
#mapping type:  dict
#set type:      set, frozenset
#bool:          bool
#binary type:   byte, bytearray, memoryview
#none type:     none

# Mit der type() Funktion bekommt man den jeweiligen Datentyp
#x = 5
#print(type(x))

# Konventonen
#x = "Hello World!"                             -> str
#x = 20                                         -> int
#x = 20.5                                       -> float
#x = 1j                                         -> complex
#x = ["apple, banana, cherry"]                  -> list
#x = ("apple" , "banana", "cherry")             -> tuple
#x = range(6)                                   -> range
#x = {"name" : "John", "age" : 36}              -> dict
#x = {"apple", "banana", "cherry"}              -> set
#x = frzenset({"apple", "banana", "cherry"})    -> frozenset
#x = true                                       -> bool
#x = b"Hello"                                   -> bytes
#x = bytearray(5)                               -> bytearray
#x = memoryview(bytes(5))                       -> memoryview
#x = None                                       -> NoneType

# Man kann jetzt hinter alles noch den spezifischen Datentypen dahinter schreiben also z.B x = int(20) usw

# Type conversion von Datentypen

x = 1   # int
y = 2.8 # float
z = 1j  # complex

# convert int -> float
a = float(x)

# convert float -> int
b = int(y)

# convert int -> complex  (complex kann nicht in ein anderen nummerntyp convertet werden!)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Pyhton hat kein random() Funktion muss imported werden

import random

print(random.randrange(1, 10))

print("i love 'specific' people" )
