""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import csv
import json
import sys


def export_csv():
    # api.openweathermap.org / data / 2.5 / forecast?id = 524901 & APPID = 1111111111
    pass


def export_json():
    pass


def export_html():
    pass


def info():
    """
        Функция вывода подсказки
        :return: None
        """
    print("help - получение справки")
    print("--csv filename [<город>] - экспорт в формате csv")
    print("--json filename [<город>] - экспорт в формате json")
    print("--html filename [<город>] - экспорт в формате html")


do = {
    '--csv': export_csv,
    '--json': export_json,
    '--html': export_html,
    'help': info,
}

try:
    second_arg = sys.argv[2]
except IndexError:
    second_arg = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    third_arg = sys.argv[3]
except IndexError:
    third_arg = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
