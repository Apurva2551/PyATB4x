# List Manipulation:
#
# Create a list of numbers from 1 to 10. Write a Python function that
# returns a new list containing only the even numbers from the original list.
numbers = list(range(1, 11))
print(numbers)
Even_numbers = [num for num in numbers if num % 2 == 0]
print(Even_numbers)
