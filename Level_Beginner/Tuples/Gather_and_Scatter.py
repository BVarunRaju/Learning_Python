#This program showcases the uses Gather and Scatter which is used for variable-length arguement tuples

#This function uses gather which can print all the values of the arguements passed in the function
def gather(*args):
    print("The arguements are:",args)

#This function returns the sum of all the numbers in the tuple
def sum_all(t):
    return sum(t)

#This function uses scatter to use only one arguement in the divmod() built-in-function
def div_mod(t2):
    return divmod(*t2)

#Main function
gather(1,2,'hello',4.9)
t1=(1,2,3,4,5,6,7)
result=sum_all(t1)
print("The sum of",t1,"is:",result)
t2=(7,3)
print("The (Quotient/Remainder)of",t2,"is:",div_mod(t2))

