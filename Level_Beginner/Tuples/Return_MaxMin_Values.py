#Program that reutuns the max and min values to a tuple from a series of numbers

#Function that returns the maximum and minimum value
def max_min(l):
    return max(l),min(l)

#Main Function
l=list()
t=tuple()
print("Enter the series of numbers(Enter 'done' to exit!):")
while True:
    x=input("Enter number:")                                        
    if x=="done":
        break
    l.append(x) #Tuples are immutable, hence we take in the values as a list and convert it to a tuple

t=max_min(l)
print("The (max,min) values are:",t)


