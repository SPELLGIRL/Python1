# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

from math import gcd

equations = input('Введите свой пример: ')


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def super_summ(x1, y1, x2, y2):
    if y1 == y2:
        x, y = x1 + x2, y1
    else:
        common_denominator = int(y1 * y2 / gcd(y1, y2))
        result_numerators = int(
            common_denominator / y1 * x1 + common_denominator / y2 * x2)
        general_devider = gcd(result_numerators, common_denominator)
        x, y = int(result_numerators / general_devider), int(
            common_denominator / general_devider)
    return x, y


def func(equation: str) -> str:
    """
    Определяет сумму или разность дробей с выделением целой части.
    :param equation: пример, который необходимо посчитать.
    :return: преобразованный результат сложения или вычитания дробей.
    """
    equation_list = equation.split()
    integer_numbers = []
    equation_other = []
    for i in equation_list:
        if i == '+' or i == '-':
            if not integer_numbers:
                integer_numbers.append('0/1')
            if not equation_other:
                equation_other.append('0/1')
        if is_number(i):
            integer_numbers.append(f'{i}/1')
        else:
            equation_other.append(i)
    if len(integer_numbers) == 1:
        integer_numbers.append('0/1')
    if len(equation_other) == 2:
        equation_other.append('0/1')
    fx1, fy1 = map(int, equation_other[0].split('/'))
    fx2, fy2 = map(int, equation_other[2].split('/'))
    ix1, iy1 = map(int, integer_numbers[0].split('/'))
    ix2, iy2 = map(int, integer_numbers[1].split('/'))
    if equation_other[1] == '-':
        fx2 *= -1
        ix2 *= -1
    result = super_summ(*super_summ(fx1, fy1, fx2, fy2),
                        *super_summ(ix1, iy1, ix2, iy2))
    x, y = result[0], result[1]
    n = abs(x) // y
    if x < 0:
        n *= -1
        x = -x - n * y
    else:
        x = x - n * y
    if n == 0:
        return f'{x}/{y}'
    else:
        return str(n) if y == 1 or x == 0 else f'{n} {x}/{y}'


print(func(equations))
