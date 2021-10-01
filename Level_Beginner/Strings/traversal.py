#program that traverses a string using for and while loop

import string

def for_loop(str):
    print("This does a traversal of the string using a for loop:")
    for letter in str:
        print(letter)

def while_loop(str):
    index=0
    print("This does a traversal of the string using a while loop:")
    while index<len(str):
        print(str[index])
        index+=1

#Main Function
print("Program illustrates the traversal of a string using for and while loop")
str=input("Enter the string:")
for_loop(str)
while_loop(str)

