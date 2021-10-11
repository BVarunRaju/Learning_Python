#This program illustrates the module of pickling which automatically type coverts DS like lists and dictionaries to be 
#Entered into a file

import pickle

def pickle_dump_list(my_file):
    l=list()
    print("Enter values for the list(enter 999 to exit):")
    while True:
        x=input("Enter element:")
        if x=='999':
            break
        l.append(x)
    pickle.dump(l,my_file)

def pickle_dump_dictionary(my_file):
    d=dict()
    print("Enter the values for the dictionary(Enter 999 in key to exit:")
    while True:
        key=input("Enter the Key:")
        if key=='999':
            break
        value=input("Enter the value:")
        d[key]=value
    pickle.dump(d,my_file)

def pickle_load():
    file=open('pickle.txt','rb')
    print("The contents of the file are:\n",pickle.load(file))
    file.close()

#Main Function
my_file=open('pickle.txt','wb')
pickle_dump_list(my_file)
pickle_dump_dictionary(my_file)
my_file.close()
pickle_load()

