# Program checks wether x<=y<=z using boolean expressions of True and False

def check(x,y,z):
    return x<=y<=z
    
#Main Function
x=int(input("Enter the value of the first number:"))
y=int(input("Enter the value of the second number:"))
z=int(input("Enter the value of the third number:"))
if check(x,y,z):
    print("x<=y<=z")
else:
    print("It doesn't satisfy the condition of x<=y<=z")