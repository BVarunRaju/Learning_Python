#Program to find the fibonacci series of a number using recursion (fibonacci(n)=fibonacci(n-1)+fibonacci(n-2))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#Main Function
n=int(input("Enter the number of steps for  fibonacci series:"))
if n<=0:
    print("The range has to be greater than 1!")
    exit()
for i in range(n):
    print(fibonacci(i))



