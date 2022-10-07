"""
1. Write a script which accepts a sequence of comma-separated numbers from
user and generates a list and a tuple with those numbers.
"""

lst = list(map(int, input().split(',')))   # генеруємо список з цілими числами
tpl = tuple(lst)                           # генеруємо кортеж зі списку

