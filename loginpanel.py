#! Задание 4.2

list_of_logins = [login.strip() for login in "Мавпродош, Лорнектиф, Древерол, Фиригарпиг, Клодобродыч".split(',')]


def CheckLogin(log_for_check=None):
    if log_for_check is not None and log_for_check in list_of_logins:
        return True

if __name__ == '__main__':
    while True:
        input_login = input('Please, write your login :  ')
        if CheckLogin(input_login):
            print('Autorization complete!!!' + '\nBye')
            break
        else:
            print('Wrong login!')
