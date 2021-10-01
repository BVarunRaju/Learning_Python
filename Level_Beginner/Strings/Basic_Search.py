#Program to find the a letter in a string using basic search 

def search(str,letter):
    index=0
    while index<len(str):
        if str[index]==letter:
            return index
        index+=1
    return -1

#Main Function
str=input("Enter the string:")
letter=input("Enter the letter to be found:")
position=search(str,letter)
if position<0:
    print("This letter is not there in the string!")
    exit()
print("The position of",letter,"in",str,"is",position)
        