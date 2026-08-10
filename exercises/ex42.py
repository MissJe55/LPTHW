#Ex 42 - Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(stuff) #I wanted to see result after the .split

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print(" Let's do some thing with stuff.")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))


#Notes 
# .split(' ') — breaks one string into a list of separate strings, cutting wherever the given separator (here, a space) appears

# .pop() — removes the last item from a list and returns that item; use .pop(n) to remove the item at a specific index instead

# ' '.join(list) — combines all items in a list back into a single string, placing the given separator (here, a space) between each item
