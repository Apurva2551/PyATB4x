# Write a Python program that calculates the area of a circle based on the radius
# entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
import math
from pickle import FLOAT

Radius=float(input("Enter the Radius"))
Pi=math.pi
Area= Pi*math.pow(Radius,2)
Area2=Pi*Radius**2
print("Area of Circle is",Area)
print("Area2 of Circle is",Area2)