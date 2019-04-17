# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random


def create_points() -> list:
    """
    Функция генерирует случайный несовпадающий набор 8 точек координат
    :return: Список координат 8-ми точек.
    """
    x = []
    while len(x) < 8:
        point = (random.randint(1, 8), random.randint(1, 8))
        if x:
            if point not in x:
                x.append(point)
        else:
            x = [point]
    return x


def attack(list_point: list) -> bool:
    """
    Проверяет бьют ли Ферзи друг друга по координатам
    :param list_point: список 8-ми точек с координатами
    :return: True если Ферзи бьют друг друга и False если нет.
    """
    for p1 in list_point:
        for p2 in list_point:
            if p2 != p1:
                if abs(p2[0] - p1[0]) == abs(p2[1] - p1[1]) or p1[0] == p2[0] or \
                        p1[1] == p2[1]:
                    return True
    else:
        return False


# Для проверки список координат Ферзей, когда они не бьют (существует 92 варианта)
# list_attack = [(1, 5), (2, 1), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]

list_attack = create_points()
print(list_attack)
print('Yes' if attack(list_attack) else 'No')
