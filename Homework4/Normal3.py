# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))

random_str = ''.join([str(random.randint(0, 9)) for i in range(2500)])


# Вариант без регулярных выражений

def longest_sequences(string: str) -> list:
    """
    Находит и возвращает максимальные последовательности из одинаковых символов.
    :param string: Произвольная строка из 2500 символов(2500-значное число)
    :return: список последовательностей с максимальной длиной.
    """
    sequence = ''
    max_len = 0
    max_sequences = []
    for i in string:
        if sequence:
            if i == sequence[0]:
                sequence += i
                if len(sequence) > max_len:
                    max_len = len(sequence)
                    max_sequences.clear()
                    max_sequences.append(sequence)
                elif len(sequence) == max_len:
                    max_sequences.append(sequence)
            else:
                sequence = i
        else:
            sequence = i
    return max_sequences


# Вариант с регулярными выражениями

def longest_sequences_v2(string: str) -> list:
    """
    Находит и возвращает максимальные последовательности из одинаковых символов.
    :param string: Произвольная строка из 2500 символов(2500-значное число)
    :return: список последовательностей с максимальной длиной.
    """
    sequences = [x[0] for x in re.findall(r'((.)\2{2,})', string)]
    max_len = len(max(sequences, key=len))
    return list(filter(lambda x: len(x) == max_len, sequences))


with open(f'{script_dir}/data/random_list.txt', 'w+') as file:
    file.write(random_str)
    file.seek(0)
    print(longest_sequences(file.readline()))
    file.seek(0)
    print(longest_sequences_v2(file.readline()))
