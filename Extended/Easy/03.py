"""
У нас есть существующий словарь, который отображает штаты США в их столицах.
1. Вывести столицу штата Айдахо
2. Вывести все штаты.
3. Вывести все столицы.
4. Создайте одну строку «Алабама -> Монтгомери, Аляска -> Джуно, ...»
5. Убедитесь, что строка, созданная вами в пункте 4, отсортирована по алфавиту
6. Теперь мы хотим добавить обратный порядок, учитывая название столицы, в каком
штате он находится?
Реализуйте функцию def get_state (capital): ниже, чтобы она возвращала штат.
** Что произойдет, если два штата имеют одинаковое заглавное имя, как вы
справляетесь с этим?
"""

STATES_CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
    'Wiscon': 'Cheyenne',  # Добавлено для проверки последней функции.
}


def capital_of_idaho(dictionary: dict) -> str:
    """
    Находит столицу Айдахо.
    :param dictionary: Словарь данных.
    :return: Результат функции
    """
    return [value for key, value in dictionary.items() if key == 'Idaho'].pop()


print(f'Задание 1:\n{capital_of_idaho(STATES_CAPITALS)}', end='\n\n')


def all_states(dictionary: dict) -> str:
    """
    Возвращает названия всех штатов из словаря
    :param dictionary: Словарь данных.
    :return: Результат функции
    """
    return '\n'.join([key for key in dictionary])


print(f'Задание 2:\n{all_states(STATES_CAPITALS)}', end='\n\n')


def all_capitals(dictionary: dict) -> str:
    """
    Вовращает все столицы штатов из словаря.
    :param dictionary: Словарь данных.
    :return: Результат функции
    """
    return '\n'.join([value for value in dictionary.values()])


print(f'Задание 3:\n{all_capitals(STATES_CAPITALS)}', end='\n\n')


def states_capitals_string(dictionary: dict) -> str:
    """
    Возвращает строку из названий штатов и столиц с разделителем ->
    :param dictionary: Словарь данных.
    :return: Результат функции
    """
    return ', '.join(
        [f'{key} -> {value}' for key, value in sorted(dictionary.items())])


print(f'Задание 4, 5:\n{states_capitals_string(STATES_CAPITALS)}', end='\n\n')


def get_state(capital: str, dictionary: dict) -> str:
    """
    Возвращает название штата, столицу которого передали.
    :param capital: Название столицы, чей штат ищем.
    :param dictionary: Словарь данных.
    :return: Результат функции
    """
    return ', '.join([key for key, value in dictionary.items() if value == capital])


print(f'Задание 6:\n{get_state("Cheyenne", STATES_CAPITALS)}')
