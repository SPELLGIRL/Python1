# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, my_list: list) -> list:
    """
    Функция фильтрации списка по условию
    :param func: Функция - условие, по которому производится фильтрация
    :param my_list: принимаемый список
    :return: новый отфильтрованный список
    """
    filter_list = []
    for i in my_list:
        if func(i):
            filter_list.append(i)
    return filter_list


print(my_filter(lambda x: x % 2 == 0, [1, 5, 6, 3, 4, 8, 9]))
