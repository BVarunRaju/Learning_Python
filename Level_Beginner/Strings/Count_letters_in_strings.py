#program to find the number of letters in a string and to print their indexes

import string
def count_letters(str,letter):
    if str.find(letter)==-1:
        print("The letter is not there in the string!")
        exit()
    print("The number of",letter,"in",str,"is",str.count(letter))

#main function
str=input("Enter the string:")
letter=input("Enter the letter to be found:")
count_letters(str,letter)