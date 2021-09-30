#Program to find GCD of (m,n) using recursion

def GCD(m,n):
    if n==0:                   #Base case
        return m
    else:                      # gcd(m,n)=gcd(n,r) where r is the remainder of m/n
        r=m%n
        return GCD(n,r)

#Main Function
x=int(input("Enter the value of the first number:"))
y=int(input("Enter the value of the second number:"))
result=GCD(x,y)
print("THhe GCD of",x,"and",y,"is:",result)
