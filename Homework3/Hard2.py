# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def to_list(path: str) -> list:
    """
    Преобразует файл в список
    :param path: Путь к файлу в виде строки
    :return: Возвращает списки строк, разделенные по столбцам
    """
    with open(path, encoding='UTF-8') as file:
        temp_list = [x for x in file]
        temp_list = [[x.strip() for x in y if len(x)] for
                     y in [z.split(' ') for z in temp_list]]
        return temp_list


def dictionary(header: list, values: list) -> list:
    """
    Составляет словри из списков
    :param header: Ключи
    :param values: Значения
    :return: Возвращает список словарей
    """
    temp_list = [list(zip(header, value)) for value in values]
    temp_list = [{x[0]: x[1] for x in y} for y in temp_list]
    return temp_list


def merge(file1: str, file2: str) -> list:
    """
    Возвращает общую таблицу из file1 и file2
    в виде списка из словарей по каждому сотруднику
    :param file1: Путь к певрому файлу
    :param file2: Путь ко второму файлу
    :return: Объединённая таблица
    """
    workers_list = to_list(file1)
    hours_list = to_list(file2)
    w_header = workers_list.pop(0)  # Список заголовков
    h_header = hours_list.pop(0)  # Список заголовков

    workers = dictionary(w_header, workers_list)
    hours = dictionary(h_header, hours_list)

    for x in workers:
        for y in hours:
            if (x['Фамилия'] == y['Фамилия'] and
                    x['Имя'] == y['Имя']):
                x.update(y)

    return workers


def calculate(table: list) -> list:
    """
    Расчёт зарплаты
    :param table: Таблица в виде списка словарей с данными по всем сотрудникам
    :return: Список словарей с добавленным расчётом по каждому сотруднику
    """
    for worker in table:
        salary = int(worker['Зарплата'])
        h_need = int(worker['Норма_часов'])
        h_fact = int(worker['Отработано_часов'])
        h_pay = int(salary / h_need)

        if h_fact == h_need:
            worker['Расчёт'] = f'{salary}'
        elif h_fact > h_need:
            worker['Расчёт'] = f'{salary + (h_fact - h_need) * h_pay * 2}'
        else:
            worker['Расчёт'] = f'{h_pay * h_fact}'
    return table


def show_save(workers: list) -> None:
    """
    Показыввает и записывает выборку данных по всем сотрудникам в файл
    :param workers: Таблица сотрудников в виду списка словарей
    :return: None
    """
    with open('calculate.txt', 'w', encoding='UTF-8') as file:
        header = f"{'Имя':<15}{'Фамилия':<15}{'Расчёт':<15}\n"
        data = ''.join([f"{worker['Имя']:<15}{worker['Фамилия']:<15}"
                        f"{worker['Расчёт']:<15}\n"
                        for worker in workers])
        print(header + data)
        file.write(header + data)


workers_total = calculate(merge('./data/workers', './data/hours_of'))
show_save(workers_total)
