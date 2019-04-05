# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен,
# то умножить на два.

import random

any_list = [random.randint(0, 99) for i in range(10)]
print(any_list)

update_list = []
for i in any_list:
    update_list.append(i * 2) if i % 2 else update_list.append(i / 4)
print("Новый список:", update_list)
