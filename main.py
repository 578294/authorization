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
    authorization(username_choise)
    registration(username_choise)
    exit(username_choise)
    return username_choise


def authorization(username_choise: str):  # Авторизация
    if username_choise == '1':
        login = input('Введите логин ')
        password = input('Введите пароль ')

        login_password = check_user(login, password)

        if login_password:
            print('Вы авторизовались ')
        else:
            print('Неверный логин или пароль ')


def registration(username_choise: str):  # Регистрация
    if username_choise == '2':
        login = str(input('Введите логин '))
        if len(login) < 3 or len(login) > 20:
            print('Логин не может быть короче 3 и длиннее 20 символов')
            print('Попробуйте снова!')
            greet()

        password = str(input('Введите пароль '))
        if len(password) < 4 or len(password) > 32:
            print('Пароль не может быть короче 4 и длиннее 20 символов')
            print('Попробуйте снова!')
            greet()

        password_repeat = str(input('Повторите пароль '))

        if password != password_repeat:
            print('Пароли не совпадают!')

        print('Попробуйте снова!')
        greet()

        login_password = add_user(login, password)

        if not login_password:
            print('Данный логин уже существует!')
        else:
            print('Регистрация прошла успешно!')


def exit(username_choise: str):  # Выход
    if username_choise == '3':
        print('Завершение работы')
        quit()
        # return True


def main():
    while True:
        greet()


if __name__ == "__main__":
    main()
