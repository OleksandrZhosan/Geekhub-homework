"""
4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.
"""

def prime_list(start, stop):
    def is_prime(n):
        flag = True
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if not n % i:
               flag = False
               break
        return(flag)
    lst = []
    for i in range(start, stop + 1):
        if is_prime(i):
            lst.append(i)
    return lst

a, b = map(int, input('Введіть 2 додатніх числа через пробіл (друге > першого) \n').split())

if a >= 0 and b >= 0 and b > a:
    print('Список простих чисел у заданому діапазоні:' )
    [print(item, end=' ') for item in prime_list(a, b)]
else:
    print('Ви невірно ввели числа')