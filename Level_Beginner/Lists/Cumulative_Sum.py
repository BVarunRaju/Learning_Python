#Program to cumalitivly add all the elements of the list

def cum_sum(t):
    temp=[]
    sum=0
    for i in t:
        sum+=i
        temp.append(sum)
    return temp

#Main function
t=[1,3,5,7,9]
print("The list is:",t)
result=cum_sum(t)
print("The cumilative elements in the list are:",result)

