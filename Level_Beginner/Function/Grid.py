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
    print('|',' '*4,'|',' '*4,'|')

def grid():
    plus_minus()           
    for i in range(0,4):      #repeats the calling of the function 4 times
        vertical_bars()
    plus_minus()
    for j in range(0,4):
        vertical_bars()
    plus_minus()

#Main Function
grid()           #calls grid function