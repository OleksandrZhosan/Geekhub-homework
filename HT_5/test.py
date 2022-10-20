"""
7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів
у ньому і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""
import pandas as pd

def counter(lst):
    lst = pd.Series(lst)
    result = pd.value_counts(lst)
    
    for index, i in result.iteritems():
        print(f'{index} --> {i}')

        
lst = [1, '1', 'foo', True, [1, 2], 'foo', 1]
counter(lst)



