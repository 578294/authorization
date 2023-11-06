# Авторизация. Регистрация.
import os
def create_file_users(): #Создаем файл для записи пользователя
    if not os.path.exists('users.txt'): #Проверяем наличие файла
        with open('users.txt', 'w'):
            pass
def add_user(login: str, password: str): #Добавляем пользователя
    #login = str
    #password = str

    with open('users.txt', 'r') as f:
        u = f.read().splitlines()

    for i in u:
        a = i.split('/')
        if login == a[0]:
            return 0

    with open('users.txt', 'a') as f:
        f.write(f'{login}/{password}\n')
    return 1

def check_user(login: str, password: str): #Проверяем пользователей в файле
    #login = str
    #password = str
    with open('users.txt', 'r') as f:
        u = f.read().splitlines()

    for i in u:
        a = i.split('/')
        if login == a[0] and password == a[1]: #выполняем проверку на наличие пользователя
            return 1
    return 0

def authorization_and_registration(login):

    print('Приветствую, Username! Это проверочная работа по авторизации и регистрации')

create_file_users()

while True:
    print('Приветствую, Username! Это проверочная работа по авторизации и регистрации')
    print('Выберите меню:',
          '1.Авторизация',
          '2.Регистрация',
          '3.Выход')

    usename_choise = input()
    if usename_choise == '1':
        login = str(input('Введите логин '))
        password = str(input('Введите пароль '))

        login_pswd = check_user(login, password)

        if login_pswd:
            print('Вы авторизовались ')
        else:
            print('Неверный логин или пароль ')

    elif usename_choise == '2':
        login = str(input('Введите логин '))
        if len(login) < 3 or len(login) > 20:
            print('Логин не может быть короче 3 и длиннее 20 символов')
            print('Попробуйте снова!')
            continue
        password = str(input('Введите пароль '))
        if len(password) < 4 or len(password) > 32:
            print('Пароль не может быть короче 4 и длиннее 20 символов')
            print('Попробуйте снова!')
            continue
        password_repeat = str(input('Повторите пароль '))

        if password != password_repeat:
            print('Пароли не совпадают!')
            continue
        print('Попробуйте снова!')

        login_pswd = add_user(login, password)

        if not login_pswd:
            print('Данный логин уже существует!')
        else:
            print('Регистрация прошла успешно!')

    elif usename_choise == '3':
        print('Завершение работы')
        break






