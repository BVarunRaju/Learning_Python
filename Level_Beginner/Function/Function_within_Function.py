#Program to showcase function calling another function

#Function definiton
def print_lyrics():
    print("Everyday I spend my time")
    print("Drinnking wine,feeling fine")

#Function_call() calls print_lyrics()
def function_call():
    print_lyrics() #calling the function
    print_lyrics() 

#Main function
function_call()

