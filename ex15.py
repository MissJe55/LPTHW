#Ex 15 - Reading Files - Close and Open Functions

from sys import argv            #importing argument vector via sys module

script, filename = argv         # Sets argv to accept script which runs auto, and file name which we supply at runtime

txt = open(filename)             #declares txt to open the created text file

print(f"Here's your file {filename}:")   #print the intro to file for user
print(txt.read())            #calls read function on txt to display file contents
txt.close()    
print("Closing file...")              #close file after reading

print("Type the filename again:")      #prompt for user input

file_again =  input("* ")              #prompt cursor

txt_again = open(file_again)           #declaring txt again to open file

print(txt_again.read())                #calls read function on txt_again to display file contents once more
txt_again.close()                      #close file after reading
print("Closing file...")
