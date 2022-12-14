"""
7. Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список,
в якому знаходяться елементи першого списку, яких немає в другому. Порядок елементів,
що залишилися має відповідати порядку в першому (оригінальному) списку.
Реалізуйте обчислення за допомогою генератора в один рядок.
Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4]
"""


def list_dif(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

lst1 = [1, 2, 2, 2, 3, 4]
lst2 = [2]

print(list_dif(lst1, lst2))