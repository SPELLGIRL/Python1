# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os

import Easy as e


def change_dir(path: str) -> str:
    """
    Функция перехода в папку.
    :param path: Полный путь до директории.
    :return:Ссообщение, успешно перешли в директорию или нет.
    """
    try:
        os.chdir(path)
        return f'Успешно перешли в папку: {path}'
    except FileNotFoundError:
        return f'{path} - папки не существует'


def start():
    answer = ''
    while answer != '5':
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer == '5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            e.show_dir()
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            e.remove_dir(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            e.make_dir(name)


if __name__ == '__main__':
    start()
