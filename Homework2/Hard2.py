# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне
# от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
# Пример корректной даты
# date = '01.11.1985'
# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

correct = 'Дата введена корректно'
incorrect = 'Дата введена некорректно. Попробуйте снова'
while True:
    date = input('Введите дату в формате dd.mm.yyyy: ')
    check_date = date.split('.')
    try:
        if len(check_date) == 3 and (
                len(check_date[0]), len(check_date[1])) == (
                2, 2) and len(check_date[2]) == 4:
            day = int(check_date[0])
            month = int(check_date[1])
            year = int(check_date[2])
            if 1 <= year <= 9999 and 1 <= month <= 12:
                if month == 2:
                    if 1 <= day <= 28:
                        print(correct)
                        break
                    else:
                        print(incorrect,
                              'в феврале количество дней от 1 до 28')
                elif month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        print(correct)
                        break
                    else:
                        print(incorrect,
                              'Количество дней в данном месяце от 1 до 31')
                else:
                    if 1 <= day <= 30:
                        print(correct)
                        break
                    else:
                        print(incorrect,
                              'Количество дней в данном месяце от 1 до 30')
            else:
                print(incorrect)
        else:
            print(incorrect)
    except ValueError:
        print(incorrect, 'В дате могут быть только целые положительные числа')
