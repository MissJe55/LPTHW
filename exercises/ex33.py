#Ex 33 - Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list

for number in the_count:
    print(f"This is count {number}")

for fruits in fruits:
    print(f"A type of fruit is {fruits}")

for i in change:
    print(f"I got {i}")

#We can also build lists first start with an empty one

#elements = range(0, 6) #we can add this here, and forego the for loop. It will print all of the elemnts in the range without using a loop

elements =[] #Created an empty list

#Then use the range function to do 0 to 5 counts

for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)   #append is a function that lists understand

#now we can print them out too

for i in elements:
    print(f" Element was: {i}")

#Lets dis() the for loop

from dis import dis

dis('''
for number in the_count:
    print(number)
''')

# 0           RESUME                 0

# 2          LOAD_NAME               0 (the_count)
#           GET_ITER
#     L1:   FOR_ITER                11 (to L2)
#           STORE_NAME              1 (number)
# 3         LOAD_NAME               2 (print)
#           PUSH_NULL
#           LOAD_NAME               1 (number)
#           CALL                    1
#           POP_TOP
#           JUMP_BACKWARD           13 (to L1)

# 2   L2:   END_FOR
#           POP_TOP
#           RETURN_CONST             0 (None)