#This program reverse the key-value pair of a dictionary assuming the values are non unique

#This function converts the string to a dictionary where the key if the letter and the value is the number of times it appears 
def dictionary(s):
    d=dict()
    for letter in s:
        if letter not in d:
            d[letter]=1
        else:
            d[letter]+=1
    return d

#This function reverse the dicitonary for non-unique values
def inverse_Dictionary(d):
    inverse=dict()
    for k, v in d.items():                     #d.items() fetches all key-value pairs
        inverse[v] = inverse.get(v, []) + [k]  #dictionary_name.get() is an in-built function that takes a key and a defualt value and returns the corresponding value
    return inverse


#Main function
s=input("Enter the string:")
d=dictionary(s)
print("The letters and the number of times it is repeated are:")
print(d)

print("The inverse of this dictionary is:")
newd=inverse_Dictionary(d)
print(newd)
