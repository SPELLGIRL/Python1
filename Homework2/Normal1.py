# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random
import math

any_list = [random.randint(-99, 99) for i in range(25)]
print(any_list)

update_list = []
for i in any_list:
    if i >= 0 and math.sqrt(i).is_integer():
        update_list.append(int(math.sqrt(i)))
print("Новый список:", update_list)
