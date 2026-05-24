#More Files
#Shorty Python Script to copy one file to another
#Study Dril 2 - How short can you make the script? Removed areas are commented

from sys import argv
from os.path import exists
 
from_file = "test.txt"    #holding names of the files to be used
to_file = "new_test.txt" 

print(f"Copying from {from_file} to {to_file}")

#We could put these two lines on one, do you know how?

#in_file = open(from_file)
#indata = in_file.read()

#Trying it on one line

in_file = open(from_file); indata = in_file.read()

print(f"Does the output file exist? {exists(to_file)}")  #Both Lines on One Line


#print("Alright, all done.")

out_file = open(to_file, 'w')  #opens new_test.txt  - if it doesnt exist, python creates it, if its there it gets truncated first
out_file.write(indata) #writes contents into new_test.txt


out_file.close() #Study Drill 3- We need this to close the out_file we opened above
in_file.close()

#Study Drill 4 - All can be placed on one line with ;