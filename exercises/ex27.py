#Ex 27 - The Five Simple Rules to the Game of Code

#import the dis function

from dis import dis

#pass code to dis() as a string on multiline denoted by '''

dis('''
x=10
y=20
z=x+y''')

#Byte Code after Passing String to be disassembled

#0           RESUME                   0
#2           LOAD_CONST               0 (10)
#            STORE_NAME               0 (x)
#3           LOAD_CONST               1 (20)
#            STORE_NAME               1 (y)
#4           LOAD_NAME                0 (x)
#            LOAD_NAME                1 (y)
#            BINARY_OP                0 (+)
#            STORE_NAME               2 (z)
#            RETURN_CONST             2 (None)

# While True:
#     x = 10   This will loop forever as True = True
# 
#If we dis() the above
# 

dis("while True: x = 10")         

#Tests and Control Jumps

#X is set to 1, y = 10 will trigger as it is greater than 0

dis('''
x = 1  
if x > 0:
    y = 10
''')

#Drill - What if its changed to -1
# As you can see -1 is not greater than 0 and the y = 10 will not trigger "Return Const is none"

# 0           RESUME                   0
# 2           LOAD_CONST               0 (-1)
#             STORE_NAME               0 (x)
# 3           LOAD_NAME                0 (x)
#             LOAD_CONST               1 (0)
#             COMPARE_OP             148 (bool(>))
#             POP_JUMP_IF_FALSE        3 (to L1)
#4            LOAD_CONST               2 (10)
#             STORE_NAME               1 (y)
#             RETURN_CONST             3 (None)
#3   L1:      RETURN_CONST             3 (None)


dis("input('Yes?')")

# 1           LOAD_NAME                0 (input)
#             PUSH_NULL
#             LOAD_CONST               0 ('Yes?')
#             CALL                     1
#             RETURN_VALUE