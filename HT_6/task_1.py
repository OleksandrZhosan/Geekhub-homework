"""
1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException (його також треба створити =))"""


class LoginException(Exception):
    pass

def login_validation(username, password, silent='False'):
    users_data = {
        'login1': 'password1',
        'login2': 'password2',
        'login3': 'password3',
        'login4': 'password4',
        'login5': 'password5'
    }
    if users_data.get(username) == password:
        return True
    elif users_data.get(username) != password and silent == 'True':
        return False
    elif users_data.get(username) != password and silent == 'False':
        raise LoginException('Помилка входу')
    
input_data = tuple(input('Введіть логін, пароль, silent через кому та пробіл \n').split(', '))
print(input_data)

try:
    print(login_validation(*input_data))
except LoginException as error:
    print(f'Статус помилки: {error}')