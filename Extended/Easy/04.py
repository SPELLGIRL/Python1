"""
Работа с исключениями
Упражнение 1:
С помощью функции def raise_if_not_length_four (значение): проверить длину
значения аргумента и вызвать исключение (в частности, ValueError), если
длина не 4.
Упражнение 2:
С помощью функции def raise_if_not_four_characters (значение): проверить длину
значения аргумента и вызвать исключение (в частности, ValueError), если
длина не 4 и проверьте значение на тип str и что будет если это не строка?
Упражнение 3:
Вам нужно написать функцию, которая принимает некоторое сетевое соединение (которое
может быть GOOD или BAD). У вас есть сторонний код (его не меняем), который
предоставляет и данные базовое соединение с классом DataBase. Вы можете читать данные
из этого класса, но вы всегда должны вызывать close () до выхода из функции.
Проблема в том, что если сеть плохая, база данных будет запускаться повторно, так как
Вы должны всегда вызывать close () для закрытия соединения.
* Первая часть проблемы заключается в ловушке исключения.
* Вторая часть проблемы состоит в том, чтобы разрешить появление исключения,
но так, чтобы все равно вызывался close ().
"""


# ==== Задание 1:
def raise_if_not_length_four(value: str) -> str:
    try:
        if len(value) != 4:
            raise ValueError
    except ValueError:
        print('Длина не равна 4')
    return value


print(raise_if_not_length_four('444455'))


# ==== Задание 2:
def raise_if_not_four_characters(value):
    try:
        if len(value) != 4:
            raise ValueError
        elif type(value) != str:
            raise TypeError
    except ValueError:
        print('Длина не равна 4!')
    except TypeError:
        print('Тип данных должен быть str!')
    return value


print(raise_if_not_four_characters('jhgffghjkjhgfdfgh'))

# === Задание 3:
# ---- НЕ МЕНЯЕМ
GOOD_NETWORK = 0
BAD_NETWORK = 1


class DataBase(object):
    number_of_connections = 0

    def __init__(self, network):
        self.network = network
        DataBase.number_of_connections += 1

    def read(self):
        if self.network == BAD_NETWORK:
            raise IOError('Ooops')
        return 'Data...'

    def close(self):
        DataBase.number_of_connections -= 1


def reset():
    DataBase.number_of_connections = 0


# ---- НЕ МЕНЯЕМ

def get_data_one(network):
    try:
        db = DataBase(network)
        result = db.read()
        db.close()
    except Exception as e:
        print(e)
    else:
        return result


def get_data_two(network):
    try:
        db = DataBase(network)
        result = db.read()
    except Exception as e:
        print(e)
    else:
        return result
    finally:
        db.close()


print(get_data_one(BAD_NETWORK))

print(get_data_two(GOOD_NETWORK))

