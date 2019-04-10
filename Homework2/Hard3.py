# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.#
# Входные данные: В первой строчке задан номер комнаты N,
# 1 ≤ N ≤ 2 000 000 000.Выходные данные:  Два целых числа — номер этажа
# и порядковый номер слева на этаже.
# Пример:
# Вход: 13
# Выход: 6 2
# Вход: 11
# Выход: 5 3

while True:

    try:
        search_room = int(input('Номер искомой комнаты: '))
        if 1 <= search_room <= 2000000000:
            block = 1
            last_room = 1
            stage = 1

            while search_room >= last_room + block ** 2:
                last_room = last_room + block ** 2
                stage += block
                block += 1

            stage += ((search_room - last_room) // block)
            count_room_left = int((search_room - last_room) % block + 1)

            print(stage, count_room_left)

            break
        else:
            print('Номер комнаты должен быть от 1 до 2 000 000 000')

    except ValueError:
        print('Номер комнаты должен быть числом')
