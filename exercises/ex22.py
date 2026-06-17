#Ex 22 - Strings, Bytes, and Character Encodings

import sys
script, input_encoding, error = sys.argv   #utilizing sys.argv instead of argv as it imports the entire sys module

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    #broken_bytes = b"Caf\xe9"   #Lets Break the code - caused UnicodeDecodeError
    #broken_bytes.decode("utf-8", errors="strict")  #Add some text encoded in another encoding scheme

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.decode(encoding, errors=errors)
    cooked_string = raw_bytes.encode(encoding, errors=errors)   
    print(raw_bytes, "<=====>", cooked_string)
languages = open("Languages.txt",'rb')  #Reversed version of original script String to Raw Bytes


main(languages, input_encoding, error)                 
            

















#Py Doc Info to Remember

#str.encode returns a string encoded to bytes
#encoding defaults to utf-8
#"errors" controls how the encoding errors are handled (strict, ignore, replace)
#.encode('utf-8) turns text into raw bytes
#.decode('utf-8') turns raw bytes back to readable text/string
#Use Pnemonic "DBES" Decode Bytes, Encode Strings
