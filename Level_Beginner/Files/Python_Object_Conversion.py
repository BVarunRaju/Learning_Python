#This program illustrates the way to enter variety of python object such as strings, integers, lists and dictionaries in a
#File using conversion tools

#This function converts integer numbers to strings
def integer_write(my_file):
    print("Enter any 3 numbers:")
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    z=int(input("Enter number 3:"))
    my_file.write('%s,%s,%s\n'%(x,y,z))

#THis function directly enters the string to the file
def string_write(my_file):
    s=input("Enter a string:")
    my_file.write(s+'\n')

#This function takes in a list and converts it to a string to enter in the file
def list_write(my_file):
    l=list()
    print("Enter the contents of the list(Enter 999 to exit):")
    while True:
        x=input("Enter item:")
        if x=='999':
            break
        l.append(x)
    
    my_file.write(str(l)+'\n')

#This function takes in a dictionary and converts it to a string to enter in the file
def dictionary_write(my_file):
    d=dict()
    print("Enter the values of the dictionary(Enter 999 in key to exit):")
    while True:
        key=input("Enter the key:")
        if key=='999':
            break
        value=input("Enter the value:")
        d[key]=value
    my_file.write(str(d)+'\n')

#This function displays the contents of the file
def display_file():
    print("\nThe contents of the file are:\n")
    print(open('conversion.txt').read())

#This funtion deletes all the contents of the file
def delete_contents():
    f=open('conversion.txt','w')
    f.truncate()
    print("The contents of the file have been deleted!")
    f.close()

#Main Function
my_file=open('conversion.txt','a')
integer_write(my_file)
string_write(my_file)
list_write(my_file)
dictionary_write(my_file)
display_file()
delete_contents()
my_file.close()





