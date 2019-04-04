# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого
# числа. Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
import random

any_number = random.randint(0, 99999)
print("Произвольное число: ", any_number)

print("C помощью цикла while: ")

i = 0
number = str(any_number)
max_number = 0
while i < len(number):
    if int(number[i]) >= max_number:
        max_number = int(number[i])
    i += 1

print("Самая большая цифра в данном числе равна = ", max_number)

print('Цикл while вариант 2 :')
number = any_number
max_num = 0
while number > 0:
    n = number % 10
    if n >= max_num:
        max_num = n
    number //= 10
print(f'Максимальная цифра: {max_num}')

print('Генератор списка :')
number = any_number

print(f'Максимальная цифра: {max([int(i) for i in str(number)])}')
