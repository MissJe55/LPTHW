# Ex 13 - Parameters, Unpacking, Variables
# Taking a quick look at the Terminal / Powershell

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("Do you want to enter more variables?", end= ' ')
answer = input()

print("Sorry, there is no more space.")

#Code Notes
#Script must be run with variables entered by user at runtime - ARGV
#Info enter via keyboard while program runs is (IE, asking a user their age)- INPUT 
