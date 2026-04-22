#Ex 14 - Prompting and Passing
#Using argv and input together to ask the user something specific

from sys import argv  #argument vector - accepts input at the moment program is run

script, user_name, user_age, favorite_food = argv #declares items to be used with argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script, congrats on reaching age {user_age} ")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What is your favorite food?")
fave = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. Your fave food is {favorite_food} ,
And you have a {computer} computer. Nice.''')

