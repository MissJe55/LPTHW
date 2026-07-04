# Ex32 - Making Decisions

print('''You enter a dark room with two doors.
Do you go through door #1 or door #2?''')

door = input('* ')

if door == '1':
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input('*')

    if bear == '1':
        print("The bear eats your face off, good job")

    elif bear == '2':
        print("The bear eats your legs off, good job!")

    else:
        print(f" Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies.")

    insanity = input('*')

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")    


#dis() it

from dis import dis


dis('''if door == '1':
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
''')

              LOAD_CONST               3 ('1. Take the cake.')
              CALL                     1
              POP_TOP

  5           LOAD_NAME                1 (print)
              PUSH_NULL
              LOAD_CONST               4 ('2. Scream at the bear.')
              CALL                     1
              POP_TOP
              RETURN_CONST             5 (None)

  1   L1:     RETURN_CONST             5 (None)