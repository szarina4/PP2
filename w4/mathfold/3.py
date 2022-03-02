from math import *
n=int(input("Input number of sides: "))
l=float(input("Input the length of a side: "))
area=(n*l*l)/(4*(tan(pi/n)))
print("The area of the polygon is:",round(area,3))