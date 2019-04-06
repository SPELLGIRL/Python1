# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

list_equation = equation.split(' ')

print('y = ', float(list_equation[2][:-1])*x + float(list_equation[4]))

