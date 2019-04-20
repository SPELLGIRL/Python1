# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def make_dir(name_dir: str) -> None:
    """
    Функция создает директорию
    :param name_dir: Имя директории, которую надо создать.
    :return: None
    """
    try:
        os.makedirs(name_dir)
    except FileExistsError:
        print(f'{name_dir} - уже существует')


def remove_dir(name_dir: str) -> None:
    """
    Функция удаляет дирректорию
    :param name_dir: Имя директории, которую надо удалить
    :return: None
    """
    try:
        os.removedirs(name_dir)
    except FileNotFoundError:
        print(f'{name_dir} - папки не существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir() -> None:
    """
    Функция показывает папки в текущей директории.
    :return: None
    """
    buf = os.listdir()
    print('Список папок:')
    for index, element in enumerate(buf, start=1):
        if os.path.isdir(element):
            print(f'{element}')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy() -> str:
    """
    Функция создает копию текущего файла.
    :return: Строку, с путем к созданному файлу
    """
    new_file = __file__ + '.copy'
    shutil.copy(__file__, new_file)
    return new_file


if __name__ == '__main__':
    print('-' * 10 + 'Задача №1' + '-' * 10)
    # Создаем дирректориис названием dir_1 - dir_9
    for i in range(9):
        make_dir(f'dir_{i + 1}')
    print(os.listdir())
    # Удаляем дирректории с названиями dir_1 - dir_9
    for j in range(9):
        remove_dir(f'dir_{j + 1}')

    print(os.listdir())

    print('-' * 10 + 'Задача №2' + '-' * 10)

    show_dir()

    print('-' * 10 + 'Задача №3' + '-' * 10)

    print(f'{current_file_copy()} - создан')
