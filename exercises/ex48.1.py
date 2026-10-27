#Ex 48 - Inheritance versus Composition

# Parent class with one method, implicit(), prints a message
class Parent():

    def implicit(self):
        print("PARENT implicit()")

#Child Class is built on Parent, so it inherits implicit() 
class Child(Parent):
    pass

#Create Parent and Child objects
dad = Parent()
son = Child()

#Dad uses Parent method directly, son inherits it
dad.implicit()
son.implicit()

