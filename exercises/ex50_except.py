#Ex50.3 - Automated Testing
#Exceptions (Try/Accept)

#Example 1
try:

 count = int("hello")
except ValueError:  #One Error will stop execution 
    print("Bad number given.")


#Example 2
try:
    assert 1 == 2, "One does not equal two"

#Catch any error, nickname is WHAT, then keep going 
except Exception as what:
   print("assert throws", type(what))

#except ValueError catches only that one kind.
#except Exception catches any kind.

