#Ex 23 - Introductory Lists
#I'm sure there is a shorter way to print the lists, I will revisit code and update once I learn it

fruit = [['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
        ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadillac',['Black', 'Big', 34500]],
    ['Corvette',[ 'Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
            ['Python', ['Slow', ['Terrible' , 'Mush']]],
            ['Javascript', ['Moderate', ['Alright', 'Bizarre']]],
            ['Perl6', ['Moderate', ['Fun', 'Weird']]],
            ['C', ['Fast', ['Annoying', 'Dangerous']]],
            ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

#Fruit Challenge: Get the elements out of the fruit variable list - Will try shorter method later on
print(f"Here is what you requested: {fruit[0][1]} {fruit[0][2]} {fruit[2][1]} {fruit[1][0]} {fruit[3][0]} {fruit[3][1]} {fruit[0][0]}")

#Cars Challenge: Get all elements out of the cars variable list
print(f"Here is your car information: {cars[0][1][1]} {cars[1][1][0]} {cars[2][1][2]} {cars[3][1][0]} {cars[3][1][2]} {cars[0][1][0]} {cars[0][1][2]} {cars[2][1][0]}")

#Languages Challenge: Get the elements out of the languages variable
print(f"Here is your requested information: {languages[0][1][0]} {languages[1][1][1][0]} {languages[3][1][1][1]} {languages[4][1][0]} {languages[4][1][1][1]} {languages[4][1][1][0]} {languages[3][1][1][0]} {languages[2][1][1][1]} {languages[1][1][0]}")

#Final Challenge
#What does this code spell out 
#My Answer: Little Red Corvette Baby 2 Mush Fast

print(f"{cars[1][1][1]} {cars[1][1][0]} {cars[1][0]} {cars[3][1][1]} {fruit[3][2]} {languages[0][1][1][1]} {fruit[2][1]} {languages[3][1][0]}")
#Correct Answer: Little Red Corvette Baby UR Mush 2 Fast 