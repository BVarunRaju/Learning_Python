#Program that adds up all integers in a nested list

def nested_sum(t):
    total=0
    for nested in t:
        total+=sum(nested)
    print("The sum of numbers in the list are:",total,"\n")

#Main function
t=[[1,2],[3],[4,5,6]]
print("\nThe list is:",t)
nested_sum(t)
