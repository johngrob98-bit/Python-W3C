# Scope (Übersetzten ist naja, Bereich, Gültigkeitsbereich, wird im Kontext hoffentlich klar)
#-------------------------------------------------------------------------------------------------------
# Vor den Grundlegenden Infos: das alles hier ist jetzt sehr trocken, mein Beileid
# Grundlegendes: Eine Variable ist nur innerhalb des Bereiches verfügbar, wo sie erstellt wurde
# diesen nennt man Scope
# In diesem Kapitel wird nur Scope geschrieben (leider kein Deutsch, hört sich nicht so gut an) 
 
#-------------------------------------------------------------------------------------------------------
# Lokaler Scope
# Eine Variable welche in einer Funktion erstellt wurde, ist nur in dieser Funktion nutzbar 
# -> sie ist eine lokale Variable 

def local():
    x = 300     # Variable wurde in der Funktion deklariert und initialisiert
    print(x)    # Sie darf nur hier verwendet werden (also in der Funktion selbst)

local()

#-------------------------------------------------------------------------------------------------------
# Heißt aber auch, die Variable ist für jede Funktion welche !Wichtig! IN der Ausgangsfunktion sind 
# nutzbar. Dazu ein Beispiel mit einer inneren Funktion

def outerfunc():    # Ausgangsfunktion
    y = 69          # Deklarieren und Initialisiern der Variable
    def innerfunc():    # Innere Funktion, sie darf die obere Variable nutzten (sie ist im selben Scope)
        print(y)        # Tut sie auch durch das print
    innerfunc()         # Aufruf der inneren Funktion

outerfunc()             # Aufruf der Ausgansfunktion

#-------------------------------------------------------------------------------------------------------
# Globaler Scope (global Variablen)
# Wie der Name schon sagt Global -> von jedem nutzbar egal ob local oder global
# -> !Wichtig!: Globale Variablen werden !außerhalb! von Funktionen erstellt 
# Beispiel:

x = 300 # <- Globale Variable (sie ist in keine Funktion)

def func():             # Ab hier beginnt die Funktion
    print(x)            # Siehe da, das x ist nutzbar für die Funktion, weil global

func()                  # Und eben auch außerhalb der Funktion irgendwo im Code ist x nutzbar

print(x)                # Sowie hier 

#-------------------------------------------------------------------------------------------------------
# Kurzer Einschub dazu noch
# Wenn Variablen im gloablen und lokalen Scope den selben Namen haben, unterscheided Python diese in
# zwei Einzelne Variablen, eine im globalen Scope (also überall nutzbar) und eine im lokalen Scope eben
# nur nutzbar in der Funktion daher nicht verwirren lassen wenn man zweimal die selbe Variable mit unter-
# schiedlichen Werten sieht (ist aber weniger konvention und mehr unsauber)

z = 10      # Global

def varlocal():
    z = 12  # Lokal
    print(z)

varlocal()

print(z)    # Die Reihenfolge ist natürlich erst lokal weil da ist das erste print dann global

# Es wird also einmal 10 und 12 seperat geprinted eben global und lokal
# Einschub Ende

#-------------------------------------------------------------------------------------------------------
# Jetzt gibt es den Fall das man eine globale Variable benötigt aber es code-technische nicht geht
# Dann erstellt man ein globales Keyword per global

def globalkey():
    global a    # Die Variable a ist nun auch außerhalb der Funktion verfügbar
    a = 300

globalkey()

print(a)        # Ausgabe der nun globalen Variable innderhalb der Funktion

#-------------------------------------------------------------------------------------------------------
# Möchte man den Wert der Variable nur innerhalb der Funktion ändern dann auch wieder per global

b = 200         # Der Wert ist global auf 200

def changekey():    
    global b    # Innherhalb der Funktion wird dieser nun auf 100 geändert 
    b = 100

changekey()

print(b)        # Dementsprechend ist der change nur lokal, global ist b immernoch 200 für alle Funktionen

#-------------------------------------------------------------------------------------------------------
# Nonlocal Keyword: wird für Variablen innerhalb verketteter Funktion genutzt
# Sorgt dafür das die Variable zur äußeren Funktion gehört
# Beispiel dazu:

def func1():
    c = "Jane"      # C ist jetzt gerade noch Jane in der äußeren Funktion  
    def func2():    # Erstellen der inneren Funktion
        nonlocal c  # Durch das nonlocal wird c an die äußere gebunden 
        c = "Hello" # Heißt alle Änderungen in func2() gehen Automatisch auf func1() rüber
    func2()         
    return c        # Also wird Jane mit Hello überschrieben

print(func1())      # Daher zählt beim print die "neue" Variable aus func2() für func1()
print("\n")

# Hört sich komplizierter an als es ist, compile einmal ohne func2() dann sieht man Jane dann mit = Hello

#-------------------------------------------------------------------------------------------------------
# LEGB Regel (Auf deutsch passt es nicht daher Englisch)
# Python geht nach dieser Reihenfolge bei Variablen Namen
# 1. Local      -> Innerhalb der akutellen Funktion
# 2. Enclosing  -> In der Umschließenden Funktion, bei verschachtelten Funktion (von innen nach außen)
# 3. Global     -> Auf der Modul Ebene definierte Namen (also außerhalb aller Funktionen)
# 4. Build-in   -> Vordefinierte Namen in Python selbst (z.B. len, print, int usw.)

# Wenn Python eine Variable nicht im Local Scope findet, geht es weiter zu Enclosing, dann Global und
# zuletzt in Built-in. Wird der Name nirgends gefunden, gibt es einen NameError!
# Beispiel dazu:

d = "global"                # Erst global Variable

def outer():                # Dann kommt die äußere Funktion und damit enclosing
    d = "enclosing"         # Daher wird d hier zu "enclosing"
    def inner():            # Dann kommt die innere Funktion
        d = "local"         # Diese Variable ist local innherhalb von inner()
        print("Inner:", d)  # Ausgabe der locale Variable
    inner()
    print("Outer:", d)  # Ausgabe der "enclosing" Variable

outer()    
print("Global:", d)         # Und zu guterletzt die Globale Variable

# Es sollte also dranstehen inner -> local, outer -> enclosing, global -> global

#-------------------------------------------------------------------------------------------------------
# Scope Ende