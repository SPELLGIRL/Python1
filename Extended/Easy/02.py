"""
Работа со списками
Получить первые элементы
=======================
Пример:
Дано: x = [('A','x'), ('B','y'), ('C','z')]
Результат: ['A','B','C']
Смещение элементов
=============
Поверните список, взяв значение с одного конца и поместив его на другом конце.
Создайте две функции rotate_left () и rotate_right (), которые изменяют список
следующим образом, учитывая список ['A', 'B', 'C']:
rotate_left() меняет на ['B', 'C', 'A']
rotate_right() меняет на ['C', 'A', 'B']
"""

x = [('A', 'x'), ('B', 'y'), ('C', 'z')]


def select_first_items(x_list) -> list:
    """
    Получение первых элементов
    :param x_list: Список входных данных
    :return: Список первых элементов.
    """
    return [i[0] for i in x_list]


def rotate_left(alist: list) -> None:
    """
    Смещение конца списка влево
    :param alist: Список входных данных
    """
    item = alist.pop(0)
    alist.append(item)


def rotate_right(alist: list) -> None:
    """
    Смещение конца списка вправо
    :param alist: Список входных данных
    """
    item = alist.pop()
    alist.insert(0, item)


new_list = select_first_items(x)
new_list_2 = new_list[:]
print(new_list)
rotate_left(new_list)
print(new_list)
rotate_right(new_list_2)
print(new_list_2)
