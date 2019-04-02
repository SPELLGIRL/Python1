# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print('Вычисление корней квадратного уравнения вида ax² + bx + c = 0')

while True:
    flag = False
    try:
        a = float(input('Введите коэффициент a: '))
        b = float(input('Введите коэффициент b: '))
        c = float(input('Введите коэффициент c: '))
    except ValueError:
        print('Необходимо вводить числа!')
    else:
        d = b ** 2 - 4 * a * c
        print(f'Дискриминант D = {d:2f}')
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f'x1 = {x1:.2f} \nx2 = {x2:.2f}')
        elif d == 0:
            x = -b / (2 * a)
            print(f'x = {x:.2f}')
        else:
            print("Корней нет")
        break
