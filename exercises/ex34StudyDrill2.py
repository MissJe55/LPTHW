#Ex 34 - Study Drill 2 
# Use this function to rewrite the script to try different numbers

numbers = []

def convert(arg1):
    i = 0
    
    while i < arg1:
     print(f"At the top i is {i}") #'At the top', i holds the current value entering the loop (before any changes happen)
     numbers.append(i)

     i += 2 

    # i is incremented here, so 'At the bottom' shows the updated value 
    # that will be tested when the loop restarts
    
     print(f"At the bottom i is {i}")
    
convert(26)

print("Numbers now:", numbers)  
