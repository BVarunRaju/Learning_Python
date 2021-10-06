#program to count letters and repeat letters in a string using a dictionary

#This function converts the string to a dictionary and returns the key as the letter and value as the number of times it 
#appears in the string
def dictionary(s):
    d=dict()
    for letter in s:
        if letter not in d:
            d[letter]=1
        else:
            d[letter]+=1
    return d

#Main function
s=input("Enter the string:")
result=dictionary(s)
print("The letters and the number of times it is repeated are:")
for c in result:
    print(c,":",result[c])