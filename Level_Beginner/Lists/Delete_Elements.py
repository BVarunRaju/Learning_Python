#Program that showcases the multiple ways to delete elements in a list

#This method retuns the element deleted given the index number
def pop_method1(l,n):
    
    element=l.pop(n)
    print("(pop(n))The element",element,"at index",n,"has been deleted!")

#This method returns the last element in the list that is deleted
def pop_method2(l):
    
    element=l.pop()
    print("(pop())The last element",element,"has been deleted")

#This method deletes the element at the given index but does not return any value
def delete_method(l,n):
    del l[n]
    print("(Del)The element at index",n,"has been deleted")

#This method deletes the element by entering the element to be deleted
def remove_method(l,ele):
    index=l.remove(ele)
    print("(remove(element))The element",ele,"at index",index,"has been deleted!")

#Main function
print("Enter the elements of the list, type 'done' if all the elements have been entered!")
l=[]
while True:
    x=input("Enter element:")
    if x=='done':
        break
    l.append(x)

n=int(input("Enter the index to delete:"))
ele=input("Enter the element to delete:")
pop_method1(l,n)
pop_method2(l)
delete_method(l,n)
remove_method(l,ele)



