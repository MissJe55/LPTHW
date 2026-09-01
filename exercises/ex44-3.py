#Ex 44 - 3 - Closures 
#Closure - Any function that's created inside another function, but accesses data in its parent. 

#this function makes functions

def constructor(color, size):
    print(">>> constructor color:", color, "size:", size)

    def repeater():
        #this function is using color, size
        print("### repeater color:", color, "size:", size)

    print("<<< exit constructor");
    return repeater

#Repeater functions are returned
blue_x1 = constructor("blue", "x1")
green_sm = constructor("green", "sm")

#The repeaters know the parameters
for i in range(0,4):
    blue_x1()
    green_sm()

