# Авторизация. Регистрация.
import os


def create_file_users():  # Создаем файл для записи пользователя
    if not os.path.exists('users.txt'):  # Проверяем наличие файла
        with open('users.txt', 'w'):
            pass


def add_user(login: str, password: str):  # Добавляем пользователя
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for i in users:
        a = i.split('/')
        if login == a[0]:
            return False

    with open('users.txt', 'a') as f:
        f.write(f'{login}/{password}\n')
    return True


def check_user(login: str, password: str):  # Проверяем пользователей в файле
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for i in users:
        a = i.split('/')
        if login == a[0] and password == a[1]:  # выполняем проверку на наличие пользователя
            return True
    return False


def greet():  # Приветствие
    print('Приветствую, Username! Это проверочная работа по авторизации и регистрации')
    print('Выберите меню:',
          '1.Авторизация',
          '2.Регистрация',
          '3.Выход')
    username_choise = input()
    create_file_users()
    if username_choise == '1':
        authorization()
    elif username_choise == '2':
        registration()
    elif username_choise == '3':
        exit()
    return username_choise


def authorization():  # Авторизация
    login = input('Введите логин ')
    password = input('Введите пароль ')

    login_password = check_user(login, password)

    if login_password:
        print('Вы авторизовались ')
    else:
        print('Неверный логин или пароль ')


def registration():  # Регистрация
    login = input('Введите логин ')
    if len(login) not in range(3, 21):
        print('Логин не может быть короче 3 и длиннее 20 символов')
        print('Попробуйте снова!')
        greet()

    password = input('Введите пароль ')
    if len(password) not in range(4, 33):
        print('Пароль не может быть короче 4 и длиннее 20 символов')
        print('Попробуйте снова!')
        greet()

    password_repeat = input('Повторите пароль ')

    login_password = add_user(login, password)
    if login_password:
        print('Вы зарегистрировались!')

    if password != password_repeat:
        print('Пароли не совпадают!')
        print('Попробуйте снова!')
    greet()

    if not login_password:
        print('Данный логин уже существует!')
    else:
        print('Регистрация прошла успешно!')


def exit():  # Выход
    print('Завершение работы')
    quit()


def main():
    while True:
        greet()


if __name__ == "__main__":
    main()
