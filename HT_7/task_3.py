"""
3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо).
   Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(*args):
    for i in args:
        if not isinstance(i, int):
            raise TypeError(f"'{i}' cannot be interpreted as an integer")    
    if not args:
        raise TypeError('Range expected at least 1 argument, got 0')
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
        if stop == 0:
            return None       
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
        if start >= stop:
            return None
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if step == 0:
            raise ValueError('range() arg 3 must not be zero')    
    elif len(args) > 3:
        raise TypeError(f'range expected at most 3 arguments, got {len(args)}')

    if step > 0:
        point = start
        while point < stop:
            yield point
            point += step
    if step < 0: 
        point = start
        while point > stop:
            yield point
            point += step


print('Введіть через кому значення start, stop, step:')
args = [int(i) for i in input().split(',')]

print(list(my_range(*args)))