from os import system
system('cls')
from colorama import init
init()
from colorama import Fore, Back, Style

def user_choice():
    while True:
        print(Style.RESET_ALL)
        user_input = input('''
        1 - вывод ID, 2 - вывод ФИО 
        3 - вывод ДР, 4 - вывод успеваемости
        5 - вывод пола, 6 - вывод всех данных
        0 - выход\n
Выберите действие: ''')
        try:
            user_input = int(user_input)
        except:
            print(Fore.RED + '''
Введите номер цифрой!''')
            continue
        if user_input >= 0 and user_input <= 6:
            return user_input
        else:
            print(Fore.RED + '''
Выбрать нужно от 0 до 6!''')


if __name__ == '__main__':
    user_choice()