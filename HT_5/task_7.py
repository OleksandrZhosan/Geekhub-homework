"""
7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів
у ньому і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""
import pandas as pd

def counter(lst):
    no_true = [i for i in lst if (i is not True)]
    no_true = pd.Series(no_true)
    result = pd.value_counts(no_true)
    num_of_true = (len(lst) - len(no_true))
    
    for index, i in result.iteritems():
        print(f'{index} --> {i}')
    print(f'True --> {num_of_true}')

        
lst = [1, '1', 'foo', True, [1, 2], 'foo', True, 1]
counter(lst)