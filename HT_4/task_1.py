"""
1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, до якої цей мiсяць належить
(зима, весна, лiто або осiнь). У випадку некоректного введеного значення -
виводити відповідне повідомлення.
"""

def seasons(month_num):
    if int(month_num) in (1, 2, 12):
        print(f"Місяць №{month_num} - це зима")
    elif month_num in (3, 4, 5):
        print(f"Місяць №{month_num} - це весна")
    elif month_num in (6, 7, 8):
        print(f"Місяць №{month_num} - це літо")
    elif month_num in (9, 10, 11):
        print(f"Місяць №{month_num} - це осінь")
    else:
        print("Ви ввели некоректне значення!")

n = input("Введіть номер місяця від 1 до 12 \n")
try:
    n = int(n)
except ValueError:
    n = 0

seasons(n)