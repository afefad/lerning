# '''Пользователь вводит строку, необходимо написать программу,
# которая определит можно ли из данного набора символов собрать палиндром.'''
#
# # Блок с функцией для определения палиндрома
# def is_palindrome (word: str):
#     # Считаем каждый символ в строке и записываем результаты в список.
#     sym_counts = {sym: word.count(sym) for sym in set(word)}
#     odd_count = 0
#     for i_count in sym_counts.values():
#         if i_count % 2 == 1:
#             odd_count += 1
#     return odd_count <= 1
#
# # Пользователь вводит текст
# text = input()
# # Вывод результата
# print('Можно составить палиндром' if is_palindrome(text) else 'Нельзя составить палиндром')
# from asyncio import start_unix_server
import copy
from itertools import count
from re import search
from time import sleep


# def zip_generator(first, second):
#     min_len = min(len(first), len(second))
#     result = [(first[i], second[i]) for i in range(min_len)]
#     return result
#
# string = 'abcd'
# some_tuple = (10, 20, 30, 40)
#
# print(zip_generator(string, some_tuple))


# # 5! = 1 * 2 * 3 * 4 * 5
# # 5! = 5 * 4 * 3 * 2 * 1
# # 5! = 5 * (4 * 3 * 2 * 1) = 5 * 4!
# # n! = n * (n - 1)!
#
# def factorial(num):
#     if num == 1:
#         return 1
#     fact_n-1 = factorial(num - 1)
#     return num * fact_n-1
#
# print(factorial(5))


# site = {
#     'html': {
#         'head': {
#             'title': 'my site'
#         },
#         'body': {
#             'h2': 'Заголовок',
#             'div': 'Тут блок какой то',
#             'p': 'А вот тут новый абзац'
#         }
#     }
# }
#
# def find_key(structure, key):
#     if key in structure:
#         return structure[key]
#
#     for sub_struct in structure.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# user_key = input('Какой ключ ищем? \n')
# value = find_key(site, user_key)
#
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре нет.')


# def power(a, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / power(a, -n)
#     n -= 1
#     return a * power(a, n)
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))


# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def key_search(structure, key):
#
#     if key in structure:
#         return structure[key]
#
#     for sub_struct in structure.values():
#         if isinstance(sub_struct, dict):
#             result = key_search(sub_struct, key)
#             if result:
#                 break
#     else:
#         return None
#
#     return result
#
# word = input('Введите ключ: ')
# print(key_search(site, word))


# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list[:], 2: copy.deepcopy(some_dict), 3: uniq_nums.copy(), 4: (10, 20, 30)}
#
#
# change_dict(common_dict)
# print(
#     'nums_list', nums_list,
#     'some_dict', some_dict,
#     'uniq_nums', uniq_nums,
#     'common_dict', common_dict,
#     sep='\n'
# )




# def type_of_input (data):
#     """
#     Анализирует переданный объект:
#     - Определяет тип данных.
#     - Проверяет изменяемость.
#     - Выводит ID объекта.
#     """
#     print(f'Тип данных: {type(data).__name__}')
#     print(
#         'Изменяемый (mutable)'
#         if type(data).__name__ in ('list', 'dict', 'set', 'bytearray')
#         else
#         'Неизменяемый (immutable)'
#     )
#     print(f'Id объекта: {id(data)}')
#
#
# input_data = {'a': 10, 'b': 20}
# type_of_input(input_data)