"""
4. Наприклад маємо рядок -->
"f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка
   обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка,
кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр
та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> {підрахуємо частоту входження кожного символа в строку}
"""

def string_process(s):
    count_alpha = 0
    count_num = 0
    sum_num = 0
    new_s = ''
    d = {}
    if 30 <= len(s) <= 50:
        for i in s:
            if i.isalpha():
                count_alpha += 1
            if i.isdigit():
                count_num += 1
        print(f'Довжина рядка - {len(s)} \nКількість букв - {count_alpha} \nКількість цифр - {count_num}')        
    elif len(s) < 30:
        for i in range(len(s)):
            if s[i].isdigit():
                sum_num += int(s[i])
            if s[i].isalpha():
                new_s += s[i]
        print(f'Сума всіх цифр у рядку - {sum_num} \nРядок тільки з букв - "{new_s}"')        
    else:   #підрахуємо кількість входжень різних символів у рядок (без врахування регістру)
        for i in s.lower():
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for item, value in sorted(d.items()):
            print(f'Кількість символів "{item}" в рядку - {value}')

s = input('Введіть строку \n')
string_process(s)