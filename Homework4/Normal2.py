# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


def find_upper(string: str) -> list:
    """
    Находит символы в верхнем регистре, слева от которых находятся
    два символа в нижнем регистре, а справа - два символа в верхнем регистре
    :param string: Строка, в которой производиться выборка.
    :return: Список символов в верхнем регистре.
    """
    pattern = re.compile(r'([a-z]{2})([A-Z]+)([A-Z]{2})')
    temp_list = pattern.findall(string)
    result = []
    for i in temp_list:
        result.append(i[1])

    return result


def find_upper_advanced(string: str) -> list:
    """
    Находит символы в верхнем регистре, слева от которых находятся два
    символа в нижнем регистре, а справа - два символа в верхнем регистре.
    :param string: Строка, в которой производится выборка
    :return: Список символов, удовлетворяющих условию.
    """
    list_upper_ad = []
    lower_count = ''
    upper_count = ''
    for symbol in string:
        if symbol.islower():
            if len(upper_count) >= 3 and len(lower_count) >= 2:
                list_upper_ad.append(upper_count[:-2])
            if upper_count:
                lower_count, upper_count = '', ''
            lower_count += symbol
        elif symbol.isupper():
            upper_count += symbol
        else:
            lower_count, upper_count = '', ''

    return list_upper_ad


print(find_upper(line))
print(find_upper_advanced(line))
