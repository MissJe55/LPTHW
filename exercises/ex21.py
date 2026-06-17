#Functions Can Return Something

def add(a, b):     
    print(f"Adding {a} + {b}")
    return a + b


print("Lets do some math with just functions!")

age = add(40, 7)

#****************************************************

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b 

height = subtract(20, 5)

#**************************************************

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

weight = multiply(1.8, 100)

#***************************************************

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b 
iq = divide(40, 5)

print(f"age {age}, height {height}, weight {weight}, iq {iq}")


#And one puzzle for extra credit

print(" Here is a puzzle!")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
 
#***Study Drill 2
#Work out the normal formula that would re-create the set of operations in line 42

what2 = height - weight * iq/2 + age
print("Change it to a simple formula", what2, "matches the first total?")

 

#Study Drill 2 Breakdown - Why this works step-by-step
#Inner functions must be calculated first



#Study Drill 3
#When I changed parts of the function I received errors or different totals that were incorrect


#Study Drill 4 
#Do the inverse, write a simple formula and use the functions in the same way to calculate it

what3 = weight + height * age - iq / 2 
print("If you play around and invert it, your total will be", what3,)

#Now lets make a nested formula from the above

what3 = add(weight, multiply(height, age))

