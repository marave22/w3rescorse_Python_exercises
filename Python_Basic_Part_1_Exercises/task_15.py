# Write a Python program to get the volume of a sphere with radius 6.

import math

radius = int(input("Please enter the radius of sphere: "))
volume = (4 * math.pi * (radius**3))/3

print("The volume of sphere: ", round(volume, 2), "cm")
