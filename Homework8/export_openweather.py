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
import xml.dom.minidom as xml_dm
import json
import os
import sys
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(f'{SCRIPT_DIR}/app.id', 'r') as f:
    APP_ID = f.readline()

BASE_URL = rf'http://api.openweathermap.org/data/2.5/weather?appid={APP_ID}&units=metric'


def build_response(attr=None):
    url = BASE_URL + f'&id={third_arg}' + (f'&mode={attr}' if attr else '')
    return urllib.request.urlopen(url).read().decode('utf-8')


def export_xml():
    response = build_response('xml')
    with open(f'{SCRIPT_DIR}/{second_arg}.xml', 'w', encoding='utf-8') as file:
        parsed_xml = xml_dm.parseString(response)
        pretty_xml_as_string = parsed_xml.toprettyxml()
        file.write(pretty_xml_as_string)


def export_csv():
    response = build_response()

    def process_value(keys, value, flattened):
        if isinstance(value, dict):
            for key in value.keys():
                process_value(keys + [key], value[key], flattened)
        elif isinstance(value, list):
            for idx, v in enumerate(value):
                process_value(keys + [str(idx)], v, flattened)
        else:
            flattened['__'.join(keys)] = value

    flattened = {}

    for t_key, t_value in json.loads(response).items():
        process_value([t_key], t_value, flattened)

    with open(f'{SCRIPT_DIR}/{second_arg}.csv', 'w+', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        count = 0
        if count == 0:
            header = flattened.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(flattened.values())


def export_json():
    response = build_response()
    json_as_string = json.loads(response)
    with open(f'{SCRIPT_DIR}/{second_arg}.json', 'w', encoding='utf-8') as file:
        json.dump(json_as_string, file, ensure_ascii=False, indent=2,
                  sort_keys=True)


def export_html():
    response = build_response('html')
    with open(f'{SCRIPT_DIR}/{second_arg}.html', 'w', encoding='utf-8') as file:
        file.write(response)


def info():
    """
        Функция вывода подсказки
        :return: None
        """
    print("help - получение справки")
    print("--csv filename [<город>] - экспорт в формате csv")
    print("--json filename [<город>] - экспорт в формате json")
    print("--html filename [<город>] - экспорт в формате html")
    print("--xml filename [<город>] - экспорт в формате xml")


do = {
    '--csv': export_csv,
    '--json': export_json,
    '--html': export_html,
    '--xml': export_xml,
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
