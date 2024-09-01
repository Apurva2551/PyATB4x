# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral
# (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

a = int(input("Enter First Side of Triangle "))
b = int(input("Enter Second Side of Triangle "))
c = int(input("Enter Third Side of Triangle "))

if a == b == c:
    print("It is Equilateral")

elif a == b or b == c or a == c:
    print("It is isosceles")

else:
    print("It is scalene")
