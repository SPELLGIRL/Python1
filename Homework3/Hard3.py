# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв,
# имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

alphabet = tuple(map(chr, range(ord('А'), ord('Я') + 1)))


def sort_fruits(file: str) -> list:
    """
    Возвращает сортированный по алфавиту
    список cловарей из фруктов
    :param file: Путь к файлу
    :return: Сортированный список
    """
    with open(file, encoding='UTF-8') as file:
        fruits = []
        fruits_all = [fruit.strip() for fruit in file]
        fruits_all = [fruit for fruit in fruits_all if len(fruit)]
        for letter in alphabet:
            fruits_sorted = [fruit for fruit in fruits_all if
                             letter == fruit[0]]
            if len(fruits_sorted):
                fruits.append({letter: sorted(fruits_sorted)})

    return fruits


def save_fruits(fruits_list: list) -> None:
    """
    В зависимости от первой буквы названия
    фрукта, записывает его в соответсвующий файл
    :param fruits_list: Сортированный список
    :return: None
    """
    for fruit in fruits_list:
        for key, value in fruit.items():
            with open(f'./data/fruits_sorted/fruits_{key}.txt', 'w',
                      encoding='UTF-8') as file:
                file.write('\n\n'.join(value))


save_fruits(sort_fruits('./data/fruits.txt'))
