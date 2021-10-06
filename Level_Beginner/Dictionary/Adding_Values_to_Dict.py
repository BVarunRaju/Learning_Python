#This program adds the key and value pairs to a dictionary as entered by a user

#Main Function
print("Enter the key and value pairs of the dictionary(enter 999 in key to exit!):")
key=''
value=''
d=dict()
while True:
    key=input("Enter the key:")
    if key=='done':
        break
    value=input("Enter the value:")
    d[key]=value

print("The dictionary in dictionary form is:")
print(d)

print("The dictionary in a more readable form is:")
for c in d:
    print(c,":",d[c])


