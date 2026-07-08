#Ex 34 - While Loops

i = 0
numbers = []

while i < 6:
    print(f" At the top i is {i}") #'At the top', i holds the current value entering the loop (before any changes happen)
    numbers.append(i)

    i += 1

    # i is incremented here, so 'At the bottom' shows the updated value 
    # that will be tested when the loop restarts
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

#Side Quest: Lets dis() it and see how a while loop works

from dis import dis

dis('''
i = 0
while i < 6:
    i += 1
''' )

  0           RESUME                   0

  2           LOAD_CONST               0 (0)
              STORE_NAME               0 (i)

  3           LOAD_NAME                0 (i)
              LOAD_CONST               1 (6)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE       14 (to L3)

  4   L1:     LOAD_NAME                0 (i)
              LOAD_CONST               2 (1)
              BINARY_OP               13 (+=)
              STORE_NAME               0 (i)

  3           LOAD_NAME                0 (i)
              LOAD_CONST               1 (6)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        2 (to L2)
              JUMP_BACKWARD           13 (to L1)
      L2:     RETURN_CONST             3 (None)
      L3:     RETURN_CONST             3 (None)

