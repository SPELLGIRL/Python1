# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    """
    Функция выводит последовательность чисел Фибоначчи.
   :param n: номер элемента, с которого начать последовательность
   :param m: последний номер элемента последовательности
   :return: ряд Фибоначчи с элемента n по m
   """
    a, b = 1, 1
    fibonacci_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        fibonacci_list.append(a)

    return fibonacci_list[n - 1:m]


n = int(input("Введите первый элемент"))
m = int(input("Введите последний элемент"))
print(f'Последовательность Фибоначчи от {n} до {m}:', fibonacci(n, m))
