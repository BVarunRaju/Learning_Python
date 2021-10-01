#To find if a string is a palindrome using string slices

def palindrome(word):
    reverse=word[::-1]
    length=len(word)
    for i in range(length-1):
        if word[i]!=reverse[i]:
            return False
    return True


#Main Function        
str=input("Enter the string:")
result=palindrome(str)
print("Is",str,"a palindrome?:",result)