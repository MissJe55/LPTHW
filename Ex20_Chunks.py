#Ex 20 - Functions and Files

from sys import argv

#script, input_file = argv  #if we want to enter file at runtime use this

input_file = "ex20_test.txt" #set the input file to be used, we create this

def print_all(f):      #define the function that will print file
    print(f.read())    #read from file

current_file = open(input_file) #open input file and store it in current file object

print("First let's print the entire file:\n")

print_all(current_file)  #Call the function to print contents of file object



#******************************************************************

def rewind(f):  #define function used to rewind and use seek
    f.seek(0)   # invokes seek the 0 means go to the beginning of the file
    
rewind(current_file)  #set the current input file to the beginning

print("Now let's rewind like a tape.") #this function just moved a cursor to the top

#******************************************************************

def print_a_line(line_count, f):   #Define function to print a line of file
    print(line_count, f.readline())  #print the line number and read each line

print("Let's print three lines!")

current_line = 1  #first line variable assignment
print_a_line(current_line, current_file)  #function call to print a line from the file

current_line += 1 #increment operator for line 2
print_a_line(current_line, current_file)

current_line += 1 #increment operator for line 3
print_a_line(current_line, current_file)
