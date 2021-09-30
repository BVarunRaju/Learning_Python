#Program to find the factorial of a number using recursion

def factorial(n):
    if n==0:            #base case
        return 1
    else:
        return n*factorial(n-1)   #recursion

#Main Function
n=int(input("Enter the number to find the factorial:"))
result=factorial(n)
print("The factorial of",n,"is:",result)