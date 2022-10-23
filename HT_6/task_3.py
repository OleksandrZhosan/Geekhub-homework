"""
3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї
   функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані
   і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK   P.S. Не забудьте використати блок try/except ;)
"""

class LoginException(Exception):
    pass

def login_password_validation(username, password):
    symbols = '!@$%^&*()_-+.;'
    
    def has_numbers(string):
        for i in string:
            if i.isdigit():
                return True
        return False


    def has_symbols(string):
        for i in string:
            if i in symbols:
                return True
        return False


    if len(username) > 50 or len(username) < 3:
        raise LoginException('Невірна довжина логіна')
    if len(password) < 8 or not has_numbers(password):
        raise LoginException('Невірна довжина паролю або в паролі не має цифри')
    if not has_symbols(password):
        raise LoginException('В паролі має бути хоча б 1 символ зі списку: !@$%^&*()_-+')
    else:
        return 'Чудовий пароль!'
    
users = [('user1', 'passw'), ('user2', 'password'), ('user3', 'password1'),
         ('user4', 'password2!'), ('user5', 'password3!')]
for i in users:
    try:
        print('Name:', i[0])
        print('Password:', i[1])
        print('Status:', login_password_validation(i[0], i[1]))
    except LoginException as error:
        print(f'Status: {error}')
    print('*******')