# Given a list with duplicate values,
# write a function to return a new list with duplicates removed.
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]

uniqueList = []
duplicateList = []


for i in numbers_with_duplicates:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

print(uniqueList)
