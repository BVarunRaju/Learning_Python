#Function right_justify takes a string named s as a parameter amd prints the string with enough leading spaces so the last letter of
#the string is in column 70 of the display

import string                    # to find the length of the word

def right_justify(word,length):
    spaces=70-length             # to make sure that the last letter of the word is column 70, we add the right amount of spaces
    print(" "*spaces,word)       

#Main function
word=input("Enter the word:")
length=len(word)
right_justify(word,length)


