"""
== OpenWeatherMap ==
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.
Необходимо решить следующие задачи:
== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)
        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up
        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in
        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a
    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}
== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQdb со следующей структурой данных
   (если файла базы данных не существует):
    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных
2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))
3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.
При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.
При работе с XML-файлами:
Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>
Чтобы работать с пространствами имен удобно пользоваться такими функциями:
    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''
    tree = ET.parse(f)
    root = tree.getroot()
    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}
    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...
"""

import urllib.request
import os
import subprocess
import gzip
import sqlite3 as db
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DB = f'{SCRIPT_DIR}/data/SQdb.db'
with open(f'{SCRIPT_DIR}/app.id', 'r') as f:
    APP_ID = f.readline().strip()
BASE_URL = rf'http://api.openweathermap.org/data/2.5/weather?appid={APP_ID}&units=metric'


# 1. Создавать файл базы данных SQdb со следующей структурой данных
def create_table():
    url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
    try:
        os.stat(f'{SCRIPT_DIR}/data')
    except FileNotFoundError:
        os.mkdir(f'{SCRIPT_DIR}/data')

    archive_path = f'{SCRIPT_DIR}/data/city.list.json.gz'

    try:
        os.stat(archive_path)
    except FileNotFoundError:
        urllib.request.urlretrieve(url, archive_path)

    with gzip.open(archive_path, 'rb') as f_in:
        list_cities = f_in.read().decode('utf-8')

    try:
        os.stat(PATH_DB)
    except FileNotFoundError:
        with db.connect(PATH_DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS `Погода`
                               (`id_города` INTEGER PRIMARY KEY, `Город` VARCHAR(255), `Дата` DATE,
                                `Температура` INTEGER, `id_погоды` INTEGER)""")
    return json.loads(list_cities)


def add_db(weather_data):
    city_weather = [(weather_data["id"], weather_data["name"], weather_data["dt"],
                     weather_data["main"]["temp"], weather_data["weather"][0]["id"])]
    with db.connect(PATH_DB) as connection:
        cur = connection.cursor()
        cur.executemany("INSERT OR REPLACE INTO `Погода` VALUES (?,?,?,?,?)",
                        city_weather)


# 2. Выводить список стран из файла и предлагать пользователю выбрать страну

def weather_request(name, city_names):
    """Запрос погоды по Id города
    Получение данных в формате JSON и обработка
    """
    for num in range(len(city_names)):
        if name == city_names[num]['name']:
            city_id = '&id=' + str(city_names[num]['id'])
    final_url = f'{BASE_URL}{city_id}'
    web_data = urllib.request.urlopen(final_url).read().decode('utf-8')
    weather_data = json.loads(web_data)
    print(f'Температура в городе {weather_data["name"]} сейчас '
          f'{weather_data["main"]["temp"]} градус(ов) по Цельсию.')
    return weather_data


def city_request(list_cities):
    while True:
        weather_data = None
        city_name = input('Введите название города на английском языке: ').title()
        catches = []
        for line in list_cities:
            if city_name == line['name']:
                weather_data = weather_request(city_name, list_cities)
                add_db(weather_data)
                break
            elif line['name'].startswith(city_name[:int(len(city_name) / 1.5)]):
                catches.append(line['name'])
        if weather_data is not None:
            break
        print("Уточните название")
        if len(catches):
            print("Возможные варианты:")
            print('\n'.join(catches))
        else:
            print('не обнаружено совпадений')


# 3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
# Реализовано в файле export_openweather.py по id города.
# 4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
#    данных. Если данные для данного города и данного дня есть в базе - обновить
#    температуру в существующей записи.

def country_request(list_cities):
    while True:
        country_name = input(
            'Введите аббревиатуру страны на английском языке (например RU): ').upper()
        cities = {}
        for line in list_cities:
            if country_name == line['country']:
                cities[str(line['id'])] = str(line['name'])
        if cities:
            try:
                os.stat(f'{SCRIPT_DIR}/data/weather')
            except FileNotFoundError:
                os.mkdir(f'{SCRIPT_DIR}/data/weather')
            try:
                os.stat(f'{SCRIPT_DIR}/data/weather/{country_name}')
            except FileNotFoundError:
                os.mkdir(f'{SCRIPT_DIR}/data/weather/{country_name}')
            for city_id, name in cities.items():
                subprocess.call(
                    ['python', f'{SCRIPT_DIR}/export_openweather.py', '--json',
                     f'data/weather/{country_name}/{name}', city_id])
                with open(
                        f'{SCRIPT_DIR}/data/weather/{country_name}/{name}.json') as file:
                    data = json.loads(file.read())
                    add_db(data)
            break
        else:
            print('Аббревиатура страны не найдена.')


def menu():
    answer = ''
    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Показать и добавить данные по городу\n'
                       '2. Скачать файлы погоды в формате json и добавить '
                       'информацию в БД по всем городам страны\n'
                       '3. Выход\n')
        if answer == '3':
            break
        city_names = create_table()
        if answer == '1':
            city_request(city_names)
        elif answer == '2':
            country_request(city_names)


if __name__ == '__main__':
    menu()
