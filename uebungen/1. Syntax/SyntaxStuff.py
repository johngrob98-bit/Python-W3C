#Hier mal paar Syntaxkonventionen von Phyton
print("Hello! ", end="") #in einer Zeile
print("I will print on the same line.")
print(420) #zahlen gehn einfach auch 
print(69)
print(808)
print(5 + 10) #sogar rechnungen
print("The price is:", 99)

x = 5
y = "John"
print(type(x)) #type casting geht btw auch 
print(type(y)) #variablen werden automatisch zum jeweiligen Datentyp umgewandelt

zeit_fuer_das = 4

print(zeit_fuer_das)

a, b, c = "Orange", "Banana", "Cherry"
print(a,b,c)

d = e = f = "Oh weia"
print(d)

fruits = ["apple", "coconut", "pears"]
g, h, i = fruits
print(g, h, i)

k = "ey jo"
l = 3.0
m = 1
print(type(k))  #eben hier werden Datentypen automatisch getypecasted aber wenn man will kann man diese auch anzeigen lassen
print(type(l))  #btw kann man trzdm sagen ich will das die Variable jz n string ist 
print(type(m))

n = str("miau") #hier wird dann halt gesagt jo du bist jz genau ein string
print(n)


#Global Variablen

o = "awesome"

def myfunc():
    print("Python is " + o)

myfunc()

#Die Globale Variable wird bei der letzten func2 wiederverwendet davor kommt die neue locale variable fantastic (ball ball ball ballin)

p = "nice"

def myfunc2():
    p = "fantastic"
    print("Python is " + p)

myfunc2()

print("Python is " + p)

#Gloable variable innerhalb eine funktion geht auch 
q = "my granny called"

def func():
    global q
    q = "ball ball ballin"

func()

print("Python is " + q)