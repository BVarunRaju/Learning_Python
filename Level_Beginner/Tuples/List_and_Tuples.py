#This program showcases how to combine and use lists and tuples together

def combine_list_string(s,l):
    t=zip(l,s)
    print("The tuple of combines list and strings is:")
    for pair in t:
        print(pair)
    

def list_of_tuples(s,l):
    l1=list(zip(l,s))
    print("The lit of tuple is:",l1)
    print("The traverse of the list of tuples is:")
    for number,letter in l1:
        print(number,letter)

#Main Function
s='Hello'
l=[1,2,3,4,5]
print("The string is:",s)
print("The list is:",l)
combine_list_string(s,l)
list_of_tuples(s,l)

