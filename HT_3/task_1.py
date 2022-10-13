"""
1. Write a script that will run through a list of tuples and
replace the last value for each tuple. The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
"""

lst = [(1, 2), (3,), (5, 6, 7), ()]

result = []
n = input('Введіть нове значення \n')
for i in lst:
    i = list(i)
    if len(i) == 0:
        i.append(n)
    else:
        i[-1] = n
        i = tuple(i)
    result.append(i)
print(result)    