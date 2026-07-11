#Ex 34 - While Loops
# Study Drill 1
#Convert this while-loop to a function that you can call, and replace 6 int he test (i < 6) with a variable. 


numbers = []

def convert(arg1):
    i = 0
    
    while i < arg1:
     print(f"At the top i is {i}") #'At the top', i holds the current value entering the loop (before any changes happen)
     numbers.append(i)

     i += 1 

    # i is incremented here, so 'At the bottom' shows the updated value 
    # that will be tested when the loop restarts
    
     print(f"At the bottom i is {i}")
    
convert(6)

print("Numbers now:", numbers)  


#Takeaways
#Consistent errors due to inconsistent indentation - all remedied
#I set i = 0 outside of the created function and it should be have been declared after the function, but before the while loop

