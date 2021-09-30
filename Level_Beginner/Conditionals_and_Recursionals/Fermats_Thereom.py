#program to prove fermats thereom i.e, there are no positive integers a,b and c such that a^n + b^n = c^n for n>2

def fermats(a,b,c,n):
    if n<=2:                                                     
        print("The value of n has to be greater than 2!")
        exit()
    x=a**n+b**n
    y=c**n
    if x==y:
        print("Fermat's was wrong!")
    else:
        print("Fermat's was right!")

#Main Function
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
n=int(input("Enter the value of n:"))
fermats(a,b,c,n)

