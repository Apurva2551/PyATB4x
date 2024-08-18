# Write a Python program that accepts a filename from the user
# and prints the extension of the file.
# Sample filename : abc.java
# Output : java
import os.path

Filename=input("Enter File Name  ")
Text=Filename.split(".")
print(Text[-1])