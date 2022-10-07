"""
6. Write a script to check whether a value from user input
is contained in a group of values.
e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
[1, 2, 'u', 'a', 4, True] --> 5 --> False
"""

lst = input().split(', ')    #формуємо список з введених значень (роздільник - ", ")
s = input()
print(s in lst)              #перевіряємо входження s у список lst
