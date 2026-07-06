#Ex 32 - Create Your Own Game 

print("**************************")
print("Pick Your Tailored Workout")
print("**************************")
print("                          ")

print("What body part are you working?")
print("1. Legs - The best day ")
print("2. Upper Body")
print("3. Just gimme the Cardio Shorty")


Choice = input("> ")

if Choice == "1":
    print('''
    3 Sets of 10-12 RDLs
    3 Sets of Reverse Lunges 
    3 Sets of Bench Squats''')          

elif Choice == "2":
    print(''' 
        25 Pushups
        25 Bicep Curls
        25 Tricep Press Downs
''')
    
elif Choice == "3":
    print("Which Cardio activity will you knock out today?")
    print("1. Swimming")
    print("2. Dancing") 
    print("3. That boring treadmill")   
    

    Cardio = input("> ")

    if Cardio == "1":
        print("Gimme 3 laps of each stroke. Don't slack on that butterfly!")

    elif Cardio == "2":
        print("Cash Money Records taking over for 99 and 2000's")

    elif Cardio == "3":
        print("Fine, but you gotta use an incline!")

else: 
   print("I guess a rest day is ok as well. See ya tomorrow!")

