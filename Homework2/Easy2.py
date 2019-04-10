# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list_init = [1, 2, 3, 5, 7, 9, 22, 74, 83, 1, 83, "Света", "Наташа"]
second_list_init = [1, 7, 9, 22, 53, 6, 8, "Света", "Катя"]

print("\nВариант 1 (на все случаи удаляет только один раз)")

first_list, second_list = first_list_init.copy(), second_list_init.copy()

for i in second_list:
    if i in first_list:
        first_list.remove(i)
print(first_list)

print("\nВариант 2 (запись в одну строку удаляет только 1 раз)")

first_list, second_list = first_list_init.copy(), second_list_init.copy()

[(first_list.remove(i) if i in first_list else False) for i in second_list]
print(first_list)

print("\nВариант 3 оставит только уникальные в рандомном порядке")

first_list, second_list = first_list_init.copy(), second_list_init.copy()

result = list(set(first_list) - set(second_list))
print(result)

print("\nВариант 4 удаляет все элементы второго списка, даже повторяющиеся")

first_list, second_list = first_list_init.copy(), second_list_init.copy()

for i in first_list:
    for j in second_list:
        if i == j:
            first_list.remove(j)
print(first_list)
