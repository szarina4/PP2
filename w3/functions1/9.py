import math
def volume(rad):
    vol=(4/3)*math.pi*(rad**3)
    return vol

r=float(input("Enter radius of sphere: "))
print(volume(r))