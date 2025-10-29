# Else
#-------------------------------------------------------------------------------------------------------
# Grundlegendes
# else tritt in Kraft sobald die Bedingung im If False ist
#-------------------------------------------------------------------------------------------------------

# Beispiel dazu 

a = 200
b = 33
if b > a:
    print("b is greater than a") # Die If Bedingung tritt nicht in Kraft daher = False
elif a == b:                     # Zweite Bedingung wird aufgestellt
    print("a equals b")          # Stimmt auch nicht = False 
else:                            # Jetzt springt es in das else rein 
    print("a is greater than b") # Die else Bedingung ist True daher print

#-------------------------------------------------------------------------------------------------------
# Else ohne Elif (Eigentlicher Standart Elif ist so Python Ding)
a = 300
b = 40
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#-------------------------------------------------------------------------------------------------------
# Funktionsweise von Else: 
# Else bietet im Endeffekt ein Auffangbecken wenn alle anderen Bedingungen von If und Elif nicht True 
# sind, heißt es gibt bei If-Else Verkettungen (einfach) immer nur eine Two-Choice Lösung True / False

#-------------------------------------------------------------------------------------------------------
# Else wird auch als wie schon ^ oben ^ gesagt Auffangbecken genutzt wenn alle Wege scheitern kommt Else

username = "Ufuk" # Einfach mal den Namen leer lassen dann tritt das Else ein

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty!")
#-------------------------------------------------------------------------------------------------------
# Else Ende