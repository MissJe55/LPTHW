#Ex 48.2 - Inheritance versus Composition
#Overriding Implicit Inheritance

class Parent():

    def override(self):
     print("PARENT override()")

class Child(Parent):

    def override(self): 
     print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

#Note:
#The classes only describe things, and the methods need an object to run on. The last four lines do two jobs:

#dad = Parent() and son = Child(): create an object from each class and save it under a name.
#dad.override() and son.override(): call the method on each of those objects.








