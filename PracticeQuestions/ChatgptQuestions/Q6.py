# List Filtering
# Filter Negative Numbers:
#
# Given a list of integers,
# write a function that returns a new list containing only the positive numbers.

numbers = [10, -5, 7, -2, 0, 8, -1]
Positive_Values = [pos_nums for pos_nums in numbers if pos_nums > 0 ]
print(Positive_Values)
Negative_Values = [pos_nums for pos_nums in numbers if pos_nums < 0 ]
print(Negative_Values)