# Given a list of strings, write a function
# that returns a new list containing
# only the strings that have more than 3 characters.


words = ["cat", "elephant", "dog", "horse", "rat"]
def more_than_3_characters(words):
    return [texts for texts in words if len(texts) > 3]
result = more_than_3_characters(words)
print(result)
