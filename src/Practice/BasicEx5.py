# Write a Python program that accepts the
# user's first and last name and prints them
# in reverse order with a space between them.
from collections.abc import Reversible

FirstName=str(input("Enter First Name "))
LastName=str(input("Enter Last Name "))
print("Hello "+LastName+" "+ FirstName)