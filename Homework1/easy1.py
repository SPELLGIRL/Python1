# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
import random

try:
    number_int = int(input('Введите целое число: '))
    if number_int < 0:
        print('Введено отрицательное значение, знак будет отброшен!')
        number_int *= -1
except ValueError:
    print('Вы ввели не целое число, будет использовано случайное значение!')
    number_int = random.randint(0, 99999)

number = str(number_int)
number_len = len(number)

print('Цикл for')
for i in number:
    print(int(i), end=' ')

print()
print('Цикл while')
i = 0
while i < number_len:
    print(int(number[i]), end=' ')
    i += 1

print()
print('Цикл while (математика) в обратном порядке')
number_int_t = number_int
while number_int_t:
    print(number_int_t % 10, end=' ')
    number_int_t //= 10

print()
print('Цикл while (математика) в правильном порядке')
exp = 10 ** (number_len - 1)
number_int_t = number_int
while exp:
    print(number_int_t // exp, end=' ')
    number_int_t %= exp
    exp //= 10

print()
print('Параметры print')
print(*number, sep=' ')

print('Рекурсия (математика)')


def recursion(n):
    if n < 10:
        return print(int(n), end=' ')
    else:
        return recursion(n // 10), print(n % 10, end=' ')


recursion(number_int)
print()

print('Генератор списка')
print([int(i) for i in number], end=' ')
print()
