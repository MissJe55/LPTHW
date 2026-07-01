#Ex 30 - What if ... introducing the if statement

people = 15
cats = 50
dogs = 100

if people < cats:
    print("Too many cats! The world is doomed. ")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

#Dogs = Dogs + 5 long method for below
dogs += 5    

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs.")

if cats == 30 and False:
    print("Get out the catnip.")

# dis() it

from dis import dis

dis('''
if people < cats:
    print("Too many cats! The world is doomed!")
''')

# 2            LOAD_NAME                0 (people)
#              LOAD_NAME                1 (cats)
#              COMPARE_OP              18 (bool(<))
#              POP_JUMP_IF_FALSE        9 (to L1)

#  3           LOAD_NAME                2 (print)
#              PUSH_NULL
#              LOAD_CONST               0 ('Too many cats! The world is doomed!')
#              CALL                     1
#              POP_TOP
#              RETURN_CONST             1 (None)
#
#  2   L1:     RETURN_CONST             1 (None)

#Study Drill

#1. What do you think the if code does under it?  The if code causes what is under it to run the code if the condition of the if is true

#2. Why does the code under the if need to be indented 4 spaces? If not indented, its not recognized as being in the same code block

#3. What happens if it isn't indented? If not indented, it will not be controlled by the if statement, most likely will return an error

#4. Can you put other Boolean statments in the if statement, try it. (See line 31)

#5 What happens if you change the initial values for people, dogs, and cats? the output changes as well if applicable