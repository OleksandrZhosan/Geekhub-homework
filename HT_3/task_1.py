"""
1. Write a script that will run through a list of tuples and
replace the last value for each tuple. The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
"""

lst = [(1, 2), (3, 4), (5, 6, 7)]

result = []
for i in lst:
    i = list(i)
    i[-1] = 'new_value'
    i = tuple(i)
    result.append(i)
print(result)    