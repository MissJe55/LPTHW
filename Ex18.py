#Ex 18 - Names, Variables, Code, Functions
#Functions name pieces of code, take arguments, let you make your own mini-scripts/tiny commands

#This one is like your scripts with argv

def print_two(*args): #*args denotes that multiple arguments will be used, there is no limit
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")  #Format string to print out the values assigned to arg1, arg2 when calling function
 
print_two("Jessica", "Wonder Woman")  #Calling funciton with values assigned, format string print will print these


#*******************************************************************************************

def print_two_again(arg1, arg2):   #Instead of *args, its only two to provide
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two_again("Jessica", "Wonder Woman")


#*******************************************************************************************

def print_one(arg1):
    print(f"Arg1: {arg1}")

print_one("WonderWoman")

#*******************************************************************************************

def print_none():
    print("I got nothing!")

print_none()

