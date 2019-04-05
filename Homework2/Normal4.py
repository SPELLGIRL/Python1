# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить^
# lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

any_list = [random.randint(-100, 100) for i in range(20)]
print('Исходный список', any_list)

new_list_a = set(any_list)
print('Задание а:', new_list_a)

new_list_b = []
for i in any_list:
    if any_list.count(i) == 1:
        new_list_b.append(i)
print('Задание б:', new_list_b)
