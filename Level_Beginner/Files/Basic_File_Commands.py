#This Program showcases the basic ways to read and write a file

#This function writes the content into the file using a list to write multiple lines at one go
def write_a_file():
    f=open('newfile.txt','a')
    l=list()
    space="\n"
    while True:
        x=input("Enter the line(Enter 999 to exit:)")
        if x=='999':
            break
        l.append(x)
        l.append(space)    #So that there is a newline between every line entered by the user
        
    f.writelines(l)
    f.close()

#This function reads the contents of the file
def read_a_file():
    print("The contents of the file are:\n")
    print(open('newfile.txt').read())        #This reads the file in such a way that end-of-line characters are interpreted

#This function deletes the contents of the file but not the file itself
def delete_contents():
    f=open('newfile.txt','w')
    f.truncate()
    print("The contents of the file have been deleted!")

#Main Function
while True:
    print("\n1.Write | 2.Read | 3.Delete contents | 4.Exit\n")
    x=int(input("Enter the option:"))
    if x==1:
        write_a_file()
    
    if x==2:
        read_a_file()

    if x==3:
        delete_contents()
    
    if x==4:
        exit()


    



