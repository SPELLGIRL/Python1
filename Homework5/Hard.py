# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def change_dir() -> None:
    """
    Функция меняет текущую директорию на указанную.
    :return: None
    """
    if not second_arg:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.chdir(second_arg)
        print(f'Успешно перешли в папку: {second_arg}')
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print(f'{second_arg} - папки не существует')


def file_copy() -> None:
    """
    Функция создает копию указанного файла
    :return: None
    """
    if not second_arg:
        print("Необходимо указать имя файла вторым параметром")
        return
    cur_dir = os.getcwd()
    old_file = os.path.join(cur_dir, second_arg)
    new_file = os.path.join(cur_dir, (second_arg + '.copy'))
    if os.path.isfile(old_file):
        if os.path.isfile(new_file):
            print('Файл уже скопирован')
        else:
            shutil.copy(old_file, new_file)
            print(new_file + ' - создан')
    else:
        return print('Файла не существует')


def remove_file() -> None:
    """
    Функция удаляет указанный файл и требует подтверждения.
    :return: None
    """
    if not second_arg:
        print("Необходимо указать имя файла вторым параметром")
        return
    cur_dir = os.getcwd()
    old_file = os.path.join(cur_dir, second_arg)
    if os.path.isfile(old_file):
        answer = input('Вы уверены что хотите удалить файл? y/n: ')
        if answer == 'y':
            os.remove(old_file)
            print(old_file + ' - удален')
        else:
            return
    else:
        print('Файла не существует')


def current_dir() -> None:
    """
    Функция показывает путь текущей директории
    :return: None
    """
    print(os.getcwd())


def print_help() -> None:
    """
    Функция вывода подсказки
    :return: None
    """
    print("help - получение справки")
    print("mkdir <second_arg> - создание директории")
    print("ping - тестовый ключ")
    print("cp - копирует указанный файл как 'имя файла'.copy")
    print("cd - меняет текущую директорию на указанную")
    print("rm - удаляет указанный файл (запрашивает подтверждение операции)")
    print("ls - отображает полный путь текущей директории")


def make_dir() -> None:
    """
    Функция создает директорию с указанным именем.
    :return: None
    """
    if not second_arg:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), second_arg)
    try:
        os.mkdir(dir_path)
        print(f'Директория {second_arg} создана')
    except FileExistsError:
        print(f'Директория {second_arg} уже существует')


def ping() -> None:
    """
    Тестовая функция выводящая сообщение.
    :return: None
    """
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": file_copy,
    "cd": change_dir,
    "rm": remove_file,
    "ls": current_dir,
}

try:
    second_arg = sys.argv[2]
except IndexError:
    second_arg = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
