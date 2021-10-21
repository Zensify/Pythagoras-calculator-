# Importing or getting the math to Square Rooot 
from math import sqrt

print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

#Finding The value of C / The hypotenuse 
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )