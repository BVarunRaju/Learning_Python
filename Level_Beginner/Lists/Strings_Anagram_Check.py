#Program that checks if two strings are anagrams of each other, using list data structures

#This functions converts the strings to lists
def conversion(s1,s2):
    l1=list(s1)
    l2=list(s2)
    anagram(l1,l2)

#This function sorts the list by ascending alphabetical order and checks if both the lists are identical
def anagram(l1,l2):
    l1temp=sorted(l1)
    l2temp=sorted(l2)
    for i in range(len(l1)):
        if l1temp[i]!=l2temp[i]:
            print("These two words are not anagrams of each other!")
            exit()
    print("The two words are anagrams of each other!")

#Main Function
s1=input("Enter the first string:")
s2=input("Enter the second string:")
conversion(s1,s2)
