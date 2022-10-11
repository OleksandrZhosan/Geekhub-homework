"""
7. Write a script which accepts a <number>(int) from user
and generates dictionary in range <number> where key is <number> and value
is <number>*<number>    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}
"""

n = int(input('Введіть ціле число \n'))
dictn = {}
for i in range(n + 1):
    dictn[i] = pow(i, 2)
print(dictn)    