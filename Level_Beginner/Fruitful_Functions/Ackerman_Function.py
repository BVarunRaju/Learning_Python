#Program to find Ackerman Function      
#Do not exceed (3,4) the system will not be able to handle the depth of recursions!
#        { n+1              if m=0       
# A(m,n)={ A(m-1,1)         if m>0 and n=0
#        { A(m-1,A(m,n-1))  if m>0 and n>0

def ackerman_function(m,n):                             #This is a recursive function
    if m==0:
        return n+1
    
    elif m>0 and n==0:
        return ackerman_function(m-1,1)

    elif m>0 and n>0:
        return ackerman_function(m-1,ackerman_function(m,n-1))

#Main Function
print("This is a program to find the Ackerman function for two numbers!")
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
result=ackerman_function(m,n)
print("The result is:",result)


