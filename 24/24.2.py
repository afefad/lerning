import os

# # Скрипт для вывода содержимого папок
# project_list = ['Prod', 'PyCharm', 'Stepik']
#
# def print_dirs(project):
#     if os.path.exists(project):
#         print('\nСодержимое директории', project)
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('\t', path)
#     else:
#         print('Директория', project, 'не существует')
#
# for i_proj in project_list:
#     path_to_project = os.path.abspath(os.path.join('..', i_proj))
#     print_dirs(path_to_project)

# def find_file(current_path, file_name, tab_count = 1):
#     tab = '__'
#     result = None
#     # print(f'{tab * (tab_count - 1)}Переходим в {current_path}')
#
#     for i_elem in os.listdir(current_path):
#         path = os.path.join(current_path, i_elem)
#         # print(f'{tab * tab_count}Смотрим {path}')
#
#         if file_name == i_elem:
#             return path
#
#         if os.path.isdir(path):
#             # print(f'{tab * tab_count}Это директория')
#             tab_count += 1
#             result = find_file(path, file_name, tab_count)
#             if result:
#                 break
#     return result
#
#
# file_path = find_file(os.path.abspath
#                       (os.path.join('..')),
#                       'lada_niva_history.pptx')
#
# if file_path:
#     print(f'\nАбсолютный путь к файлу {file_path}.')
# else:
#     print('Файл не найден!')



"""
Задача 1. Иконки
Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска: 
папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь (на директорию, файл, 
или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает на файл, то также выведите его 
размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути на существование. 

Подсказка: для вывода размера файла поищите соответствующий метод.

Пример 1:

Путь: C:\\Users\\Roman\\PycharmProjects\\Skillbox\\Module17\\lesson2.py
Это файл
Размер файла: 605 байт

Пример 2:

Путь: C:\\Users\\Roman\\PycharmProjects\\Skillbox\\Module17\\lesson2.py
Указанного пути не существует
"""

def size_of_file(file, style = 0):
    size_tup = ('Байт','КБ','МБ','ГБ','ТБ')
    file_size = os.path.getsize(file)

    def size_meter(size, counter = 0):
        if counter > 4:
            return None, None

        if size < 1024:
            return size, counter
        elif size >= 1024:
            counter += 1
            return size_meter(round(size / 1024, 2), counter)

    size, typel = size_meter(file_size)
    return f'Размер файла: {size} {size_tup[typel]}\n'

def type_of_file(link):

    if not os.path.exists(link):
        print('Указанного пути не существует\n')

    if os.path.isdir(link):
        print('Это директория\n')
    elif os.path.isfile(link):
        print('Это файл')
        print(size_of_file(link))
    elif os.path.islink(link):
        print(f'Это символьная ссылка\n')

# while True:
#     path = input('Путь: ')
#     type_of_file(path)




"""
Задача 2. Поиск файла
В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории. Однако,
как мы понимаем, файлов с таким названием может быть несколько.
Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным файлам
и папкам и выводит на экран все абсолютные пути с этим именем.

Пример:
Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
Имя файла: lesson2

Найдены следующие пути:
C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

Задания для практической работы не нужно отправлять на проверку.
"""

# search_dir = input('Ищем в: ')
search_dir = os.path.join('E:', os.path.sep, 'school', 'Coding')
# search_file = input('Имя файла: ')
search_file = 'Bot_0.1.py'

def file_search(dir, file):

    if not os.path.isdir(dir):
        print(f'{os.path.isdir(dir)} - не является директорией.')

    print('\nНайдены следующие пути:')

    def temp_func(dir, file):

        for i_elem in os.listdir(dir):
            if i_elem == file:
                print(os.path.join(dir, i_elem))
            elif os.path.isdir(os.path.join(dir, i_elem)):
                temp_func(os.path.join(dir, i_elem), file)

    temp_func(dir, file)


file_search(search_dir, search_file)
