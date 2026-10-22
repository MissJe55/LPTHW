#Ex 45 - Basic Object Oriented Programming

class Person(object):

        def __init__(self, name, age, eyes): #A class can only have one init
                self.name = name #Three Attributes Stored on the Object
                self.age = age
                self.eyes = eyes

        def talk(self, words):
            print(f"I am {self.name} and {words}")


becky = Person("Becky", 39, "green")
print(becky.__dict__)
becky.talk("I am talking here!")


Jessica = Person("Jessica", 48, "brown")
print(Jessica.__dict__)
Jessica.talk("I am really Wonder Woman")

# Accessing __dict__ for Objects 

#the class that Jessica comes from
print(Jessica.__class__)

#Contents of the class
print(Jessica.__class__.__dict__)

#A list of strings for everyting
print(dir(Jessica))

