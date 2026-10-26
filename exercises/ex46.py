#Ex 46 - Inheritance and Advanced OOP
#This is not a program to be run, it simply enforces relationships between classes, objects, etc by having the comments filled in be me


#Animal is-a object
class Animal(object):

    def bark(self):
       print(" Woof Woof")


class dog(Animal):
   
   def __init__(self, name):
      self.name = name

Macho = dog("Macho")
Macho.bark()
#Study Drill 3 - Fill out animal with a function that makes the animal do something - See above




#Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
      #Dog has-a name
      self.name = name


## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
       #Cat has-a name
       self.name = name


# Person is-a object
class Person(object):

   def __init__(self, name):
      
   #Person has-a name
    self.name = name

   #Person has-a pet of some kind
    self.pet = None
   

#Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
       #Employee has a name
       super(Employee ,self).__init__(name)
       #Employee has-s salary
       self.salary = salary

# Fish is-a object
class Fish(object):
   pass

#Salmon is-a fish
class Salmon(fish):
   pass

#Halibut is-a fish
class Halibut(fish):
   pass

#rover is-a dog
rover = Dog("Rover")

#stan is-a cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

#mary has-a pet named Satan
mary.pet = satan

#frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

#frank has-a pet named Rover
frank.pet = rover

