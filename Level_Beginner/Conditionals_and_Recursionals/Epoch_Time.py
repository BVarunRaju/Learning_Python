#Program to display the time and the number of days since epoch

import time

def epoch():
    print("The number of days since epoch is:",time.time())    #Time since epoch

def display_time():
    print("The current time and date is:", time.asctime())              #Time in string format

#Main function
epoch()
display_time()
