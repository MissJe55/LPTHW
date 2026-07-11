#Ex 34 - Study Drill 5
#Write the script to use for - loops and range. 
# No need for the incrementer since a range is provided

numbers = []

i = 0
    
for i in range(0, 10):
     print(f"At the top i is {i}") #'At the top', i holds the current value entering the loop (before any changes happen)
     numbers.append(i)

   
     print(f"At the bottom i is {i}")
    

print("Numbers now:", numbers)  