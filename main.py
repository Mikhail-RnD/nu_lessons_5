import os, shutil, platform
from victory import get_fameus_person
from bank_account import my_banking

def print_menu():

    menu = ('создать папку',
            'удалить папку',
            'копировать папку',
            'просмотр содержимого рабочей директории',
            'посмотреть только папки',
            'посмотреть только файлы',
            'просмотр информации об операционной системе',
            'создатель программы',
            'играть в викторину',
            'мой банковский счет',
            'выход.'
    )

    for i in range(0, len(menu)):
        print(f'- ({i+1}) {menu[i]}')

def main_loop():

    while True:

        request = int(input('\nВыбирите пункт меню из списка: '))

        if request == 1:
            name = input('Введите имя папки: ')
            if not os.path.exists(name):
                os.mkdir(name)
            else:
                print(f'Папка {name} уже существует!')
            print_menu()
        elif request == 2:
            name = input('Введите имя папки: ')
            if os.path.exists(name):
                os.rmdir(name)
            else:
                print('Папка не существует')
            print_menu()
        elif request == 3:
            name = input('Введите имя папки для копирования: ')
            dist = input('Введите путь папки для копирования: ')
            shutil(name, dist)
            print_menu()
        elif request == 4:
            for val in os.listdir(os.path.join(os.getcwd())):
                print(val)
            print_menu()
        elif request == 5:
            for val in os.listdir(os.path.join(os.getcwd())):
                if os.path.isfile(val):
                    print(val)
            print_menu()
        elif request == 6:
            for val in os.listdir(os.path.join(os.getcwd())):
                if os.path.isdir(val):
                    print(val)
            print_menu()
        elif request == 7:
            print(f'Информация о системе: {platform.system()} {platform.release()} релиз {platform.version()}')
            print_menu()
        elif request == 8:
            print('(c) Я')
            print(menu)
        elif request == 9:
            print('Игра "викторина"')
            request = 'yes'
            while request == 'yes':
                get_fameus_person()
                request = input('сыграть ещё? yes/no ? ')
            print_menu()
        elif request == 10:
            print('Мой банковский счет')
            my_banking()
        elif request == 11:
            break
        else:
            print('Неверный пункт меню')

#if __name__ == '__main__':

print_menu()

main_loop()

