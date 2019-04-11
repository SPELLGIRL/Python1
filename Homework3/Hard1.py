# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание)
# с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части,
# или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

from math import gcd

equations = input('Введите свой пример: ')


def is_number(string: str) -> bool:
    """
    Выполняет проверку является ли строка числом
    :param string: Вводимая строка
    :return: True/False
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def super_summ(a: str, b: str, o='+') -> str:
    """
    Выполняет действие с двумя дроби
    :param a: Первая дробь
    :param b: Вторая дробь
    :param o: Оператор
    :return:
    """
    x1, y1 = map(int, a.split('/'))
    x2, y2 = map(int, b.split('/'))
    if y1 == y2:
        x, y = x1 + (x2 if o == '+' else -x2), y1
    else:
        common_denominator = int(y1 * y2 / gcd(y1, y2))
        result_numerators = int(
            common_denominator / y1 * x1 + common_denominator / y2 * (
                x2 if o == '+' else -x2))
        general_devider = gcd(result_numerators, common_denominator)
        x, y = int(result_numerators / general_devider), int(
            common_denominator / general_devider)
    return f'{x}/{y}'


def split(string: str) -> tuple:
    """
    Разделяет строку на списки целых чисел, дробных чисел и операторов
    :param string: Вводимое выражение
    :return: Возвращает три списка
    """
    equation_list = string.split()
    integer_numbers = []
    other_numbers = []
    operators = []
    for i in equation_list:
        if is_number(i):
            integer_numbers.append(f'{i}/1')
        elif i == '+' or i == '-':
            if len(integer_numbers) == len(operators):
                integer_numbers.append('0/1')
            if len(other_numbers) == len(operators):
                other_numbers.append('0/1')
            operators.append(i)
        else:
            other_numbers.append(i)
    if len(integer_numbers) == len(operators):
        integer_numbers.append('0/1')
    if len(other_numbers) == len(operators):
        other_numbers.append('0/1')
    for n, i in enumerate(integer_numbers):
        if '-' in i:
            other_numbers[n] = f'-{other_numbers[n]}'

    return integer_numbers, other_numbers, operators


def equation(string: str) -> str:
    """
    Вычисляет заданное строкой выражение с выделением целой части
    :param string: Вводимая строка
    :return: Результат подсчета
    """
    integer_numbers, other_numbers, operators = split(string)
    sub_result = list(map(super_summ, integer_numbers, other_numbers))
    result = sub_result[0]
    for n, i in enumerate(operators, start=1):
        result = super_summ(result, sub_result[n], i)
    x, y = map(int, result.split('/'))
    n = abs(x) // y
    if x < 0:
        x = -x - n * y
        n *= -1
    else:
        x = x - n * y
    if n == 0:
        return f'{x}/{y}'
    else:
        return str(n) if y == 1 or x == 0 else f'{n} {x}/{y}'


print('Результат: ', equation(equations))
