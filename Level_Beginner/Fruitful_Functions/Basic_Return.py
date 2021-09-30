#program returns the greater number between two numbers using functions

def greater(x,y):
    if x>y:
        return x
    if x<y:
        return y
    if x==y:
        return 0

#Main Function
x=int(input("Enter the value of the first number:"))
y=int(input("Enter the value of the second number:"))
result=greater(x,y)
if result==0:
    print("The two numbers are equal!")
else:
    print("The greater number is:",result)