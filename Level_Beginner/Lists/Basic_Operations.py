#Program that creates a user filled list, concatenation, reptition, sorting

#Function to display list
def display(lists):
    print("The list is:",lists)

#Function to multiply list
def multiply(lists):
    print("Displays the list 4 times:",lists*4)


#Function to show slices of list
def slice(lists):
    print("First element:",lists[0])
    print("Last element of list:",lists[-1])
    print("middle part of lists:",lists[1:-1])

#Function to sort the list
def sorting(lists):
    lists.sort()
    print("The sorted list is:",lists)

#Main Function
print("\nEnter the elements of the list and type 'done' if all elements are entered in the list\n")
i=0
lists=[]
while True:
    x=input("Enter element:")
    if x=='done':
        break
    lists.append(x)

display(lists)
multiply(lists)
slice(lists)
sorting(lists)

