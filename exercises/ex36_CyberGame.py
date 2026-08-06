#Ex 36 - Create your own game similar to Ex 35 - Use lists, functions and modules
#Game Plot: Wonder Woman Saves the Cyber Day
#Room 1 - Armory
#Room 2 - Villian Password2Short - hurling dictionary attack passwords
#Room 3 - Villian RansomRob - locks and encrypts victim files 
#WW will enter each room in any order selected by user

#Encounter each villian and defeat them
#An option to come back another time for any villian
#If you try to enter a room where the villian was, display message and return to armory room
#Implemented Lists -  Her armor? Cuffs, Shield, Tiara, Body armor
#Implemented Functions - Rooms 1 - 3 (what happens in each room)
#Implemented Modules - exit

from sys import exit

gear = ['Shield', 'Cuffs', 'Tiara', 'Lasso of Truth', 'Body Armor']

def MainRoom():
    print("This is the main armory room. Current Armor Available:")
    print("***********************************************************************")
    print(''' 
    1. Shield
    2. Cuffs
    3. Tiara
    4. Lasso of Truth
    5. Body Armor
''')
    print("Which armor item will you take on your journey?")

    
    armor = int(input("> "))
    if armor >= 1 and armor <= 5:

        print(f"It is dangerous to go alone, take the {gear[armor - 1]} with you!")
        print("Ready to begin your mission? There are two doors in front of you.")

    else:
        print("Please enter a valid armor selection.")
        MainRoom()

    print("Select the door you wish to enter: Left or Right?")
   
    choice = input("> ")
    if choice == "Left":
        VillianRoom1()
    elif choice == "Right":
        VillianRoom2()
    else:
        print("Please enter a valid door selection.")
        MainRoom()

        
def VillianRoom1():
    print("You have entered the lair of Ransomeware Rob!")
    print("Ransomware Rob is at one of the terminals conducting an attack!")
    print("You can thwart his attack or flee.")

    choice = input("> ")

    if choice == "thwart":
        print("You attack with your weapon and knock Ransomware Rob away from the terminal")
        print("Racing to the terminal, you stop the attack and extract all encryption keys!")
        print("Job Well Done!")
        print("Your mission isn't over, head back to the armory room!")
        MainRoom()

    elif choice == "flee":
        print("Ransomware attack complete, millions of victims suffer needlessly.")
        print("Head back to the armory to refill your courage meter!")
        MainRoom()


def VillianRoom2():
    print("You have entered the lair of Password Pete!")
    print("As soon as you walk in, dictionary attack entries are flying at you!")
    print("You can parry or flee, are you brave enough to remain?")

    choice = input("> ")
    if choice == "parry":
        print("The brute password attacks are knocked out of the air before reaching the terminals!")
        print("Great Job!")
        exit(0)

    elif choice == "flee":
        print("Brute password attacks are successful and compromise system and admin accounts")
        print("Head back to the armory to assess your fortitude.")
    MainRoom()


MainRoom()


