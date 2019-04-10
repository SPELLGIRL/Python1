# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию
# и метод sort()


def sort_to_max(origin_list: list) -> list:
    """
    Функция сортировки от минимального значения к максимальному
    :param origin_list: принимаемый список
    :return: новый, отсортированный список
    """
    n = len(origin_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                buff = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = buff
    return origin_list


print([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
