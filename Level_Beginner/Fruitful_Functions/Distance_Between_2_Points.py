#Program to display pythagorean theroem of finding the distance between two points (x1,y1) and (x2,y2)
# distance = sqrt((x2-x1)^2 + (y2-y1)^2)

import math

def pythagorean(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    sum=dx**2+dy**2
    distance=math.sqrt(sum)
    return distance

#Main function

print("Enter the first pair of  coordinates!")
x1=int(input("x1:"))
y1=int(input("y1:"))

print("Enter the second pair of coordinates!")
x2=int(input("x2:"))
y2=int(input("y2:"))

result=pythagorean(x1,y1,x2,y2)
print("The distance between (",x1,",",y1,") and (",x2,",",y2,") is:",result," units")
