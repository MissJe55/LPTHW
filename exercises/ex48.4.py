#Ex48.4 - Inheritance vs Composition
#Implicit/Explicit Inheritance, and altering before/after parent class runs

class Parent():

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        
        print("CHILD, BEFORE PARENT altered())")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered())")

    
father = Parent()
son = Child()

father.implicit()
son.implicit()

father.override()
son.override()

father.altered()
son.altered()


