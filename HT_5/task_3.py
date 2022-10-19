"""
3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
"""

def is_prime(n):
    flag = True
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if not n % i:
           flag = False
           break
    return(flag)    

n = int(input('Введіть число від 0 до 1000 \n'))
print(f'Число {n} просте' if is_prime(n) else f'Число {n} не просте')

