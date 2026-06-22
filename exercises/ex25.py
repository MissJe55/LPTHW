#Ex 25 - Dictionaries and Functions

#Shows how a function can be assigned an alias, in this case rename_print. 
#Step 1: Function Names are Variables

def print_number(x):
    print("Number is", x)

rename_print = print_number
rename_print(100)
print_number(100)


#Step 2: Dictionaries with Variables
#You can put variables into a dict


color = "Red"

corvette = {
    "color": color
}
print("LITTLE", corvette["color"], "CORVETTE")

#Step 3: Dictionaries with Functions

def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run   #Allows the run function to be placed into the corvette dict

}    
print("My", corvette['color'], "can go")
corvette['run']()    #Zed asks us what we think is happening here?
#The run function is being called as a data object of the dictionary? Yes I was correct Woohoo!

#Step 4: Deciphering the Last Line
#Get the run function out of the corvette dict - we could have this code

myrun = corvette['run'] #creates an alias for run(), use run as the key to search the dict
myrun()


#STUDY DRILL - Create a function that creates a car, and it must meet requirements set in drill

#1 Parameters: Yes (model, color, speed, type) 

#2 Dict with Settings & Functions: Yes (held the data and the run function) 

#3 Returns Dict: Yes (return cars) 

#4 Independent Cars: Yes (my_car and work_car) 

#5 Tested independence: Yes (turned the Tesla yellow didnt affect the F-550) 



def create_car(model,color, speed, type):
    print("This car is a", color, model, type, speed)
    

    cars = {
        'model': model,
        'color': color,
        'speed': speed,
        'type': type,    
        'run': run
    }

    return cars


my_car = create_car('Tesla','Yellow', 'Fast', 'Racecar')
my_car['run']()

work_car = create_car('F-550','Blue', 'Moderate', 'Tank')
work_car['run']()