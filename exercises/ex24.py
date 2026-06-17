#Ex 24 - Introductory Dictionaries

fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}

];

cars = [
    {'type': 'Cadillac', 'color': 'Black', 'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red', 'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue', 'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White', 'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow', 'opinion': ['Terrible', 'Mush']},
    {'namne': 'JavaScript', 'speed': 'Moderate', 'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate', 'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast', 'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast', 'opinion': ['Fun', 'Difficult']}
    
]




#fruit Challenge with Lists/ Dictionary
print(f"Please see the fruit challenge below: {fruit[0]['count']} {fruit[0]['rating']}{fruit[2]['count']} {fruit[1]['kind']} {fruit[3]['kind']} {fruit[3]['count']} {fruit[0]['kind']}")

#Cars Challenge

print(f"Please see the cars challenge below: {cars[0]['size']} {cars[1]['color']} {cars[2]['miles']} {cars[3]['color']} {cars[3]['miles']} {cars[0]['color']} {cars[0]['miles']} {cars[2]['color']}")

#Languages Challenge

print(f"Please see the languages challenge below: {languages[0]['speed']} {languages[0]['opinion'][1]}")
#When accessing an object with a list inside add extra bracket for index in that list

#Final Challenge - Write program to print Little Red Corvette Code - (Little Red Corvette Baby 2 Mush Fast)

print(f"And the final challenge is as follows! {cars[1]['size']} {cars[1]['color']} {cars[1]['type']} {cars[3]['size']} {fruit[2]['count']} {languages[0]['opinion'][1]} {languages[3]['speed']}")