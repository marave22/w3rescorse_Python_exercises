# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Area = 3.8013271108436504
# r = 1.1
# pi = 3.14159265359
# print("Area =", pi*(r**2))
from math import pi

r = float(input('Enter the radius of circle: '))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))
