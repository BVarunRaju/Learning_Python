#Program to showcase reverse LookUp in a dictionary. Rverse LookUp is finding the key by entering the value

#Function returns the key of the value
def reverse_lookup(d,value):
    for c in d:
        if d[c]==value:
            return c
    raise LookupError()       #Raises and excpetion if the value is not present in the dictionary

#Function returns the value of a given key
def lookup(d,key):
    print(d[key])

#Creates a user entered dictionary
def add_dictionary():
    print("Enter the key and value pairs of the dictionary(enter done in key to exit!):")
    key=''
    value=''
    d=dict()
    while True:
        key=input("Enter the key:")
        if key=='done':
         break
        value=input("Enter the value:")
        d[key]=value
    return d

#Main Function
d=add_dictionary()
print("The dictionary given is:")
for c in d:
    print(c,":",d[c])

key=input("Enter the key to be searched:")
lookup(d,key)

v=input("Enter the value to be searched:")
result=reverse_lookup(d,v)
print("The value",v,"has a key of:",result)



