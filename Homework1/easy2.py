# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!\

number1 = int(input("Введите первое значение: "))
number2 = int(input("Введите второе значение: "))
# Используя третью переменную
a = number1
b = number2
c = a
a = b
b = c

print("Ваши значения поменяны местами:", number1, number2)

# Используя арифметические действия

a = a + b
b = a - b
a = a - b
print("C помощью арифметики меняем местами:", a, b)
