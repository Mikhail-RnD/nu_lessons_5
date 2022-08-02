import os, sys, shutil


def print_menu():

    menu = ('создать папку',
            'удалить (файл/папку)',
            'копировать (файл/папку)',
            'просмотр содержимого рабочей директории',
            'посмотреть только папки',
            'посмотреть только файлы',
            'просмотр информации об операционной системе',
            'создатель программы',
            'играть в викторину',
            'мой банковский счет',
            'смена рабочей директории',
            'выход.'
    )

    for i in range(0, len(menu)):
        print(f'- ({i+1}) {menu[i]}')

def main_loop():

    while True:

        request = int(input('\nВыбирите пункт меню из списка: '))

        if request == 1:
            dir_name = input('Введите имя папки: ')
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            print_menu()
        elif request == 2:
            pass
        elif request == 12:
            break

#if __name__ == '__main__':

print_menu()

main_loop()