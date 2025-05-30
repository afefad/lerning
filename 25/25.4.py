sym_sum = 0

people = open('people.txt', 'w')
people.write('Ab\nqwer\ntyro\nqwaq')
people.close()

line_count = 0

try:
    people_file = open('people.txt', 'r')
    for i_line in people_file:
        length = len(i_line)
        line_count += 1
        if i_line.endswith('\n'):
            length -= 1
        if length < 3:
            raise BaseException('Длина {} строки меньше 3х символов.'.format(line_count))
        sym_sum += length
    people_file.close()

except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('Найденная сумма символов:', sym_sum)




# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#
#             raise BaseException('Ты сломал программу!')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#     except BaseException:
#         name_list = []
#         print('Введено стоп-слово!')
#         raise ValueError('Пожалуйста не вводите стоп слово.')
#
# names_file = open('names.txt', 'w', encoding='utf8')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print("Программа закончена, запись завершена")




# Практика

# """
# Задача 1. Имена
# В базе данных одной компании есть баг (или, может быть, фича):
#     если ввести туда имя сотрудника меньше чем из трёх букв, то база сломается и упадёт.
# Как компания принимает на работу людей, например, с китайскими именами, непонятно.
#
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа
# выводит общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n),
# то вызывается ошибка, и программа завершается.
# Содержимое файла people.txt:
#
# Петя
# Ян
# Маша
# Ева
# Дмитрий
# Анастасия
# """
#
# people = open('peoples.txt', 'r', encoding='utf8')
# line_count = 0
# try:
#     for i_line in people:
#         line_count += 1
#         if i_line.endswith('\n'):
#             line_len = len(i_line) - 1
#         else:
#             line_len = len(i_line)
#
#         if line_len < 3:
#             raise BaseException('')
#
#         print(f'Количество символов в строке {line_count}: {line_len}')
#
# except BaseException:
#     print(f'В строке {line_count} меньше 3х символов.')
#     raise
# else:
#     print('\nПодсчёт символов успешно закончен.')




"""
Задача 2. Логирование
Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются, но и записывают эту ошибку в файл.
Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить.
Это называется логированием ошибок.

Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов,
из которых можно получить палиндром (привет предыдущим модулям).
Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log
"""
from tkinter import BooleanVar

def error_log(file: str, text: str) -> None:
    """
    Функция для логирования действий.

    :param file: Название для файла для логирования
    :param text: Текст лога.
    :return:
    """
    log_file = open(file, 'a', encoding='utf8')
    log_file.write(str(text) + '\n')
    log_file.close()

def can_make_palindrome(text: (str)) -> BooleanVar:
    """
    Функция определяет можно ли составить палиндром из переданных данных.

    :param text:
    :return:
    """
    # Подсчитываем частоту каждого символа
    from collections import Counter
    text = str(text)
    char_count = Counter(text)

    # Считаем количество символов с нечётной частотой
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # Если нечётных символов <= 1, то можно сделать палиндром
    return odd_count <= 1

def list_of_lines(file: str) -> list:
    """
    Принимает файл и возвращает список со строками файла.
    :param file: Файл для считывания.
    :return: Список со строк файла.
    """
    list_for_return = []
    file_lines = open(file, 'r', encoding='utf8')
    for i_line in file_lines:
        if i_line.endswith('\n'):
            list_for_return.append(i_line[:-1])
        else:
            list_for_return.append(i_line)
    file_lines.close()
    return list_for_return




file_for_check = 'words.txt'
try:
    for_poly_check = list_of_lines(file_for_check)
    poly_counter = 0
    line_counter = 0
    for i_item in for_poly_check:
        line_counter += 1
        if not i_item.isalpha():
            raise ValueError(f'В файле {file_for_check} есть неправильные значения в строке {line_counter}.')
        if can_make_palindrome(i_item):
            print(f'Из слова {i_item} можно сделать палиндром!')
            poly_counter += 1
except ValueError:
    log_file = 'errors.log'
    error_text = f'В файле {file_for_check} есть неправильные значения в строке {line_counter}.'
    error_log(log_file, error_text)
    raise
else:
    print(f'Общее количество палиндромов в файле {file_for_check} равно {poly_counter}.')



