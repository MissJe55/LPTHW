#Ex 34 - Study Drill 3
# Add another variable to the function arguments that you can pass in that letting you change the + 1 on line 8 so you can change how much it increments by

numbers = []

def convert(arg1, inc):
    i = 0
    
    while i < arg1:
     print(f"At the top i is {i}") #'At the top', i holds the current value entering the loop (before any changes happen)
     numbers.append(i)

     i += inc

    # i is incremented here, so 'At the bottom' shows the updated value 
    # that will be tested when the loop restarts
    
     print(f"At the bottom i is {i}")
    
convert(26, 3)

print("Numbers now:", numbers)  
