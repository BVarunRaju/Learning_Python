#Program to display map, reuce and filter functions in lists
import string

#Reduce function: Combines a sequence of elements into a single value 
def add(lists):
    print("The total sum is:",sum(lists))

#Map function: it maps the function capitalize onto each element in a sequence
def capital(lists):
    temp=[]
    for x in lists:
        temp.append(x.capitalize())
    print("The capitalized list is:",temp)

#Filter function: It selects some of the elements and filters out the rest
def check_capital(lists):
    res=[]
    for x in lists:
        if x.isupper():
            res.append(x)
    return res

#Main Function
lists=[]
print("\nEnter the elements of a list and type 'done' when input is over.")
while True:
    x=input("Enter element:")
    if x=='done':
        break
    lists.append(x)

add(lists)
capital(lists)
result=check_capital(lists)
print("The capital letter words are:",result)
