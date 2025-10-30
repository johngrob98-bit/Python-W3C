# Rekursion
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Die Rekursion beschreibt wenn eine Funktion sich selber aufruft
# Die Rekursion benötigt immer eine Abbruchbedingung, sonnst läuft sie !endlos!
# Rekursionen haben Basisfälle welche immer zutreffen und damit der Standart sind
# Die Rekursionsfälle sind meistens Mathematische Berechnungen mit Selbstaufruf

#-------------------------------------------------------------------------------------------------------
# Einfaches Beispiel: Runterzählen von 5 bis 0

def countdown(n):
    if n <= 0:
        print("Done!")      # Basisfall wenn dieser erreicht wird endet die Rekursion
    else:
        print(n)            # Schreibe jede Zahl bis wir eben bei 0 sind
        countdown(n - 1)    # Rekursionsfall -> n ist hierbei dann die 5, ziehe solange -1 bis 0

countdown(5)
# Das heißt auch wir erreich den Basisfall am Ende, bis hierhin eigentlich ganz simpel!

#-------------------------------------------------------------------------------------------------------
# Basis und Rekursionsfall nocheinmal genauer:
# Rekursionsfall: Die Funktion ruft sich selber mit einem abgeänderten Argument auf
# Basisfall: Eine Bedingung welche die Rekursion beendet
# Wie gesagt ohne Basisfall = Endlosschleife

#-------------------------------------------------------------------------------------------------------
# Jetzt kommen paar gängige Mathematischen Rekursionsfälle die jeder IT'ler mal gehört haben soll

#-------------------------------------------------------------------------------------------------------
# Wie erkennt man Basis und Rekofall?

def factorial(n):
    if n == 0 or n == 1: # <- Basisfall, sobald n 0 oder 1 beende die Rekursion per return 1
        return 1
    else:
        return n * factorial(n - 1) # <- Rekursionsfall eben weil sich die Funktion selber aufruft
    
print(factorial(5))

# ^ Das hier ist ein Fakultätrechner übrigens, die Berechnung steht schon da 
# Aber hier nochmal: 5! = 1 * 2 * 3 * 4 * 5 = 120

#-------------------------------------------------------------------------------------------------------
# Fibbonacci Folge
# Erst mal die Rekursion bevor die Berechnung erklärt wird:

def fibonacci(n):
    if n <= 1:      # Wie gehabt der Basisfall
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Und der Rekursionsfall
    
print(fibonacci(7))

# Erklärung Fibonacci: Jede Zahl ist die Summe der zwei vorherigen Zahlen und immer so weiter
# Es gibt 2 Arten wie die Reihe startet, entweder von 0 und 1 oder 1 und 1 (Marcel Davis 1 & 1?)
# 0 1 -> 0 + 1 = 1 dann 1 1 -> 2 dann 1 2 -> 3 dann 2 3 -> 5 dann 3 5 -> 8 dann 5 8 -> 13
# Und so weiter und sofort... (das ist wirklich nur wichtig es einmal gesehen zu haben damit man das -
# vor und zurück rechnen versteht, was prinzipell das selbe ist wie bei der Rekursion da immer auf die
# vorhergende Funktion gegriffen wird, hier ist es halt das vorherige Ergebnis + nächste Zahl)

# https://blog.assets.studyflix.de/wp-content/uploads/2022/10/WP_Fibonacci-Folge-1-1024x576.jpg Bild

#-------------------------------------------------------------------------------------------------------
# Rekursion mit Listen
# Summe aller Elemente in einer Liste:

def sum_list(numbers):
    if len(numbers) == 0:   # Basisfall wenn die Länge der Liste 0 ist
        return 0    
    else:
        return numbers[0] + sum_list(numbers[1:]) # Rekursionsfall:
# Nimmt das erste Element in der Liste und addiert es zum Ergebnis der rekursiven Summe, !aber! mit 
# der Restliste also ohne dem !ersten! Element da dieses ja schon ausgenommen ist
    
my_list = [1, 2, 3, 4, 5]   # Die beliebig wählbaren Elemente der Liste
print(sum_list(my_list))

#-------------------------------------------------------------------------------------------------------
# Maximum in der Liste rekursiv

def find_max(numbers):      
    if len(numbers) == 1:       # Basisfall wie oben wenn Länge der Liste 1 ist 
        return numbers[0]       # Gib eben nur das eine Element als Maximum aus
    else:
        max_of_rest = find_max(numbers[1:]) # Rekursionsfall: 
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
    
# Variable für Maximum erstellen, auch hier Start vom !zweiten! Element der Liste. Die Rekursion 
# durchläuft den Rest der Liste bis zum Ende. Dann wird max_of_rest mit numbers[0] verglichen 
# wenn > als numbers dann Maximum sonnst Basisfall 

list = [3, 7, 3, 9, 1]     
print(find_max(list))
print("\n")

#-------------------------------------------------------------------------------------------------------
# Rekursionstiefe, in Python gibt es ein Limit für Rekursionen, es sind bis zu 1000 Rekursivenaufrufen

import sys
print(sys.getrecursionlimit())      # Zeigt das Limit einfach mal an

# Das Limit ist erweiterbar !aber! sorgt für Abstürze

#-------------------------------------------------------------------------------------------------------
# Rekursion Ende