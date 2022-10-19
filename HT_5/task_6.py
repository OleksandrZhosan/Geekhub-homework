"""
6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатна -
пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""

def shift(lst, n):
    if n > 0:
        for _ in range(n):
            last_item = lst.pop()
            lst.insert(0, last_item)
    elif n < 0:
        for _ in range(n * (-1)):
            first_item = lst.pop(0)
            lst.append(first_item)
    return lst

lst = list(map(int, input('Введіть елементи списку через пробіл \n').split()))
n = int(input('Введіть величину зсуву \n'))

new_list = shift(lst, n)
print(*new_list)