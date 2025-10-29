# Nested If (Verschachtelte If's)
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: 
# Es gibt die Möglichkeit mehrere If Statements in einem Ausgansif zu haben (nicht so gerne gesehen)
# Verknüft mehrere Bedingungen aneinander und "checkt" mehrere Fälle direkt ab

#-------------------------------------------------------------------------------------------------------
# Beispiel:

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Hier sieht man gut wie direkt 2 Fälle abgedeckt werden, !Wichtig! hierbei ist: das zweite If
# tritt nur in Kraft wann if x > 10 true ist sonnst spirngt es direkt raus aus der If

#-------------------------------------------------------------------------------------------------------
# Jede Ebene der Verschatelung sorft für ein "tieferes Level der Entscheidungskraft" nenn ich es mal
# Einfach gesagt und !Wichtig! der Code prüft die Bedingungen von außen nach innen
# Beispiel dazu:

age = 25
has_license = True

if age >= 18:                   # Erste Bedingung -> Nur wenn diese Erfüllt ist geht es ins zweite If rein
    if has_license:             # Sobald oben und hier true dann print
        print("You can drive")
    else:                       # Dieses else ist wenn man keinen Führerschein hat 
        print("You need a license")
else:                           # Wenn age < 18 ist
    print("You are too young to drive")

#-------------------------------------------------------------------------------------------------------
# Noch ein Beispiel zur Verkettung

score = 85              # Jetzt sind es drei Variablen
attendance = 90
submitted = True
    
if score >= 60:             # Nur wenn das true geht es weiter sonnst print("fail")
    if attendance >= 80:    # Wenn das true good standing
        if submitted:       # Wenn das true good standing
            print("Pass with good standing")
        else:               # Wenn attendance true aber submitted false
            print("Pass but with missing assignment")
    else:                   # Wenn attendance false aber submitted true
        print("Pass but low attendance")
else:
    print("Fail")           # Nix von oben true

# Hier sieht man gut wie die Verkettung funktioniert
# !Wichtig! dabei ist Verkettungen ist ja ganz nützlich, sorgen aber für viel Verwirrung und sind 
# eher Unübersichtlich daher vermeiden viele ifs aneinander zuketten

#-------------------------------------------------------------------------------------------------------
# Man kann nested if mit logischen Operatoren vereinfachen
# Beispiel:

temp = 25
is_sunny = True

if temp > 25:
    if is_sunny:
        print("Perfect beach weather!")

# So ist es ohne logische Operatoren
# -> jetzt mit 

temperature = 25
is_sunni = True # ich ändere die Namen bissle

if temperature > 20 and is_sunni:
    print("Very perfect beach weather!")

# Aus zwei ifs wurde jetzt nur ein indem man and benutzt -> oben geht so oder so nur durch wenn
# das erste If true ist und wir erinnern uns and -> true and true = true daher kann man sich das 
# zweite If spaaren weil and die gleiche Bedingung hat wie if oder eher gesagt das print 

#-------------------------------------------------------------------------------------------------------
# Jetzt noch zwei Beispiele dazu zum Verstehen sind bisschen länger

username = "Ufuk"
password = "dastehtwas"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")

# Selbes Prinzip wie ^ oben ^

#-------------------------------------------------------------------------------------------------------

score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:       # Hier wurde eine zweite if Bedingung eingefügt
    print("B grade")
else:
    print("C grade or below")    

#-------------------------------------------------------------------------------------------------------
# Einschub Pass Statement (zu wenig Material deswegen hier)
# Grundlegendes: If Statements können nicht leer sein -> das kann man mit pass umgehen

a = 33
b = 200

if b > a:
    pass    # -> ja gut b > a = true 
            # pass ist ein Platzhalter es wird deswege nichts ausgegeben

#-------------------------------------------------------------------------------------------------------
# Warum dann überhaput pass?
# 1. Wenn du die Struktur des Codes schon erstellst aber die Logik dahinter noch fehlt (gibt 0 Errors).
# 2. Wenn ein Statement syntaktisch erforderlich ist aber keine Aktion danach nötig ist.
# 3. Platzhalter für später
# 4. Leer Funktionen oder Klassen welche wie gesagt später implementiert werden
# !Wichtig! noch dazu zu sagen ist: pass vs comment -> pass = no error comment = error weil leeres if

#-------------------------------------------------------------------------------------------------------
# Nested Ifs Ende