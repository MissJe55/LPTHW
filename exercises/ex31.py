#Ex 31 - Else and If

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")


if trucks > cars:
    print(" That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

#dis() it

from dis import dis

dis('''
if trucks > cars:
    print(" That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
''')

#0           RESUME                   0

#  2           LOAD_NAME                0 (trucks)
#              LOAD_NAME                1 (cars)
#              COMPARE_OP             148 (bool(>))
#              POP_JUMP_IF_FALSE        9 (to L1)

#  3           LOAD_NAME                2 (print)
#              PUSH_NULL
#              LOAD_CONST               0 (" That's too many trucks.")
#              CALL                     1
#              POP_TOP
#              RETURN_CONST             3 (None)

#  4   L1:     LOAD_NAME                0 (trucks)
#              LOAD_NAME                1 (cars)
#              COMPARE_OP              18 (bool(<))
#              POP_JUMP_IF_FALSE        9 (to L2)

#  5           LOAD_NAME                2 (print)
#              PUSH_NULL
#              LOAD_CONST               1 ('Maybe we could take the trucks.')
#              CALL                     1
#              POP_TOP
#              RETURN_CONST             3 (None)

#  7   L2:     LOAD_NAME                2 (print)
#              PUSH_NULL
#              LOAD_CONST               2 ("We still can't decide.")
#              CALL                     1
#              POP_TOP
#              RETURN_CONST             3 (None)

#Study Drill

#elif lets you chain multiple, specific conditions together in a sequence. Python checks them one by one, but only if the previous conditions were false.

#else acts as a catch-all safety net. It runs if—and only if—every single condition before it failed.