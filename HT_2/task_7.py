"""
7. Write a script to concatenate all elements in a list into a string and print it.
List must include both strings and integers and must be hardcoded.
"""

lst = [1, 2, 'u', 'a', 4, True]
result = ''

for i in lst:
    result += str(i)

print(result)