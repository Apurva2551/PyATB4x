# Find the Index of a Value:
#
# Write a function that finds the index of a specific value in a list.
# If the value is not present, the function should return -1.
fruits = ["apple", "banana", "cherry"]
def find_index(lst, value):
    return lst.index(value) if value in lst else -1

print(find_index(["apple", "banana", "cherry"], "banana"))
