# Self Parameter
#-------------------------------------------------------------------------------------------------------
# Grundlegendes: Self ist eine Referenz auf die aktuelle Instantz (das Objekt), das gerade erstellt wird
# Es wird benutzt, um auf die Attribute und Methoden des Objekts zugreifen zu können

#-------------------------------------------------------------------------------------------------------
# Ich will also das name und das alter der Klasse haben -> self.name, self.age damit hab ich Zugriff

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Ufuk", 24)
p1.greet()

# !Wichtig! der self Paramter muss immer der erste erste Parameter eine Methode in der Klasse sein

#-------------------------------------------------------------------------------------------------------
# Warum sollte man self benutzten?
# Ohne self würde Python nicht wissen auf welche Objekteigenschaften der Klasse man zugreifen möchte

#-------------------------------------------------------------------------------------------------------
# !Wichtig! self muss nicht self heißen! -> Hauptsache es ist der erste Parameter der init() Methode

#-------------------------------------------------------------------------------------------------------
# Eigenschaften per self erhalten

class Car:
  def __init__(self, brand, model, year):   # Die Attribute und self
    self.brand = brand                      # Nun hohlt man sich über self alle Attribute, Eigenschaften
    self.model = model
    self.year = year

  def display_info(self):                   # Das ist nur eine Funktion welche die Formatierung einhält
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Supra MK VI", 1998)       # Die Attribute werden ausgefüllt mit Werten
car1.display_info()

#-------------------------------------------------------------------------------------------------------
# Andere Methoden per self rufen

class Person1:
  def __init__(self, name1):        # Gleich wie oben
    self.name1 = name1

  def greet(self):                  # Hier wird eine greet Methode erstellt und diese bekommt das 
    return "Hello, " + self.name1   # Attribut name und greit damit auf alle Informationen davon zu
  
  def welcome(self):                # Neue Methode welche auf die greet Methode der greet Instanz und
    message = self.greet()          # deren Parametern zugreift 
    print(message + "! Welcome to our website.")

p2 = Person1("Ufuk")
p2.welcome()    # Das Objekt p2 nutzt dann die welcome() Methode welche die Daten der Elemente beinhaltet

#-------------------------------------------------------------------------------------------------------
# Self Parameter Ende