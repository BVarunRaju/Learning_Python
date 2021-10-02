#Program that showcases list and string operations

#Function that converts a word to a list
def w_to_l(w):
    t1=[]
    t1=list(w)
    print("The list is:",t1)
    
#Function that converts a string to a list
def s_to_l(s):
    t2=[]
    t2=s.split()
    print("The list is:",t2)

#Function that converts a string to a list using a delimiter
def s_to_l_d(s):
    t3=[]
    delimiter='_'
    t3=s.split(delimiter)
    print("The list is:",t3)

#Function that converts a list to a string
def l_to_s(list1):
    delimiter=' '
    sentence=delimiter.join(list1)
    print("The string is:",sentence)

#Main Function
word='everybody'
print("The word is:",word)
w_to_l(word)
sentence='Hey everybody how are you?'
print("The sentence is:",sentence)
s_to_l(sentence)
sentence2='spam_message_incoming_to_you'
print("The sentence is:",sentence2)
s_to_l_d(sentence2)
t=['varun','Raju','owns','this','laptop']
print("The list is:",t)
l_to_s(t)



    

