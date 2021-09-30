#Program to print:
#+----+----+
#|    |    |
#|    |    |
#|    |    |
#|    |    |
#+----+----+
#|    |    |
#|    |    |
#|    |    |
#|    |    |
#+----+----+

def plus_minus():
    print('+','-'*4,'+','-'*4,'+')

def vertical_bars():
    for i in range(0,4):                      #repeats the vertical bar grid 4 times
        print('|',' '*4,'|',' '*4,'|')

def grid():
    plus_minus()           
    vertical_bars()
    plus_minus()
    vertical_bars()
    plus_minus()

#Main Function
grid()           #calls grid function
