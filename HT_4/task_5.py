"""
5. Ну і традиційно - калькулятор
Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя,
яку зробити! Аргументи брати від юзера (можна по одному - окремо 2, окремо +,
окремо 2; можна всі разом - типу 2 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!
"""

def operation_sum(a, b):
    return a + b

def operation_subtract(a, b):
    return a - b

def operation_mult(a, b):
    return a * b

def operation_div(a, b):
    return a / b

def operation_div_reminder(a, b):
    return a % b

def operation_div_int(a, b):
    return a // b

def operation_power(a, b):
    return a ** b

def func_calc(a, op, b):
    if a == "error_value" or b == "error_value":
        return "Ви ввели не число!"
    if op == '+':
        return f'{a} + {b} = {operation_sum(a, b)}'
    if op == '-':
        return f'{a} - {b} = {operation_subtract(a, b)}'
    if op == '*':
        return f'{a} * {b} = {operation_mult(a, b)}'
    if op == '/':
        try:
            return f'{a} / {b} = {operation_div(a, b)}'
        except ZeroDivisionError:
            return "Ділити на 0 не можна!"  
    if op == '%':
        try:
            return f'{a} % {b} = {operation_div_reminder(a, b)}'
        except ZeroDivisionError:
            return "Ділити на 0 не можна!"
    if op == '//':
        try:
            return f'{a} // {b} = {operation_div_int(a, b)}'
        except ZeroDivisionError:
            return "Ділити на 0 не можна!" 
    if op == '**':
        return f'{a} ** {b} = {operation_power(a, b)}'  
    else:
        return 'Помилка при вводі операції'

a = input('Введіть перше число \n')
try:
    a = float(a)
except ValueError:
    a = "error_value"
operation = input('Введіть одну з операцій: +, -, *, **, /, //, %\n')
b = input('Введіть друге число \n')
try:
    b = float(b)
except ValueError:
    b = "error_value"
    
print(func_calc(a, operation, b))