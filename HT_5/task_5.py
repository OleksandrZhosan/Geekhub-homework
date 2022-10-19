"""
5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить
всі числа Фібоначчі, що не перевищують його.
"""

def fibonacci(n):
    lst =[0]
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        if a <= n:
            lst.append(a)
    return lst

n = int(input('Введіть число > 0 \n'))
print(*fibonacci(n))