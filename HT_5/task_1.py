"""
1. Написати функцію <square>, яка прийматиме один аргумент -
сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
периметр квадрата, площа квадрата та його діагональ
"""

def square(a):
    p = a * 4
    s = a ** 2
    d = pow(2, 0.5) * a
    return p, s, d

a = float(input('Введіть сторону квадрата \n'))
print(f'Периметр: {square(a)[0]}, площа: {square(a)[1]}, діагональ: {round(square(a)[2], 2)}')