"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом."""


class LoginException(Exception):
    pass


def has_numbers(string):
    for i in string:
        if i.isdigit():
            return True
    return False


symbols = '!@$%^&*()_-+.;'
def has_symbols(string):
    for i in string:
        if i in symbols:
            return True
    return False


def login_password_validation(username, password):
    if len(username) > 50 or len(username) < 3:
        raise LoginException('Невірна довжина логіна')
    if len(password) < 8 or not has_numbers(password):
        raise LoginException('Невірна довжина паролю або в паролі не має цифри')
    if not has_symbols(password):
        raise LoginException('В паролі має бути хоча б 1 символ зі списку: !@$%^&*()_-+')
    else:
        return 'Чудовий пароль!'
    
    
input_data = tuple(input('Введіть логін, пароль через кому та пробіл \n').split(', '))
print(input_data)

print(login_password_validation(*input_data))